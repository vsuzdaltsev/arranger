'''
# `aws_elasticsearch_domain`

Refer to the Terraform Registory for docs: [`aws_elasticsearch_domain`](https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain).
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


class ElasticsearchDomain(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomain",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain aws_elasticsearch_domain}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        domain_name: builtins.str,
        access_policies: typing.Optional[builtins.str] = None,
        advanced_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        advanced_security_options: typing.Optional[typing.Union["ElasticsearchDomainAdvancedSecurityOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        auto_tune_options: typing.Optional[typing.Union["ElasticsearchDomainAutoTuneOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_config: typing.Optional[typing.Union["ElasticsearchDomainClusterConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        cognito_options: typing.Optional[typing.Union["ElasticsearchDomainCognitoOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        domain_endpoint_options: typing.Optional[typing.Union["ElasticsearchDomainDomainEndpointOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        ebs_options: typing.Optional[typing.Union["ElasticsearchDomainEbsOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        elasticsearch_version: typing.Optional[builtins.str] = None,
        encrypt_at_rest: typing.Optional[typing.Union["ElasticsearchDomainEncryptAtRest", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        log_publishing_options: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ElasticsearchDomainLogPublishingOptions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        node_to_node_encryption: typing.Optional[typing.Union["ElasticsearchDomainNodeToNodeEncryption", typing.Dict[builtins.str, typing.Any]]] = None,
        snapshot_options: typing.Optional[typing.Union["ElasticsearchDomainSnapshotOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ElasticsearchDomainTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc_options: typing.Optional[typing.Union["ElasticsearchDomainVpcOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain aws_elasticsearch_domain} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#domain_name ElasticsearchDomain#domain_name}.
        :param access_policies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#access_policies ElasticsearchDomain#access_policies}.
        :param advanced_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#advanced_options ElasticsearchDomain#advanced_options}.
        :param advanced_security_options: advanced_security_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#advanced_security_options ElasticsearchDomain#advanced_security_options}
        :param auto_tune_options: auto_tune_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#auto_tune_options ElasticsearchDomain#auto_tune_options}
        :param cluster_config: cluster_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#cluster_config ElasticsearchDomain#cluster_config}
        :param cognito_options: cognito_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#cognito_options ElasticsearchDomain#cognito_options}
        :param domain_endpoint_options: domain_endpoint_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#domain_endpoint_options ElasticsearchDomain#domain_endpoint_options}
        :param ebs_options: ebs_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#ebs_options ElasticsearchDomain#ebs_options}
        :param elasticsearch_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#elasticsearch_version ElasticsearchDomain#elasticsearch_version}.
        :param encrypt_at_rest: encrypt_at_rest block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#encrypt_at_rest ElasticsearchDomain#encrypt_at_rest}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#id ElasticsearchDomain#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param log_publishing_options: log_publishing_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#log_publishing_options ElasticsearchDomain#log_publishing_options}
        :param node_to_node_encryption: node_to_node_encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#node_to_node_encryption ElasticsearchDomain#node_to_node_encryption}
        :param snapshot_options: snapshot_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#snapshot_options ElasticsearchDomain#snapshot_options}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#tags ElasticsearchDomain#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#tags_all ElasticsearchDomain#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#timeouts ElasticsearchDomain#timeouts}
        :param vpc_options: vpc_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#vpc_options ElasticsearchDomain#vpc_options}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d3da97f09d31cab3a80d4bf0d53ce6752c3a66bd3db00bcccde2f5c289f69f9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ElasticsearchDomainConfig(
            domain_name=domain_name,
            access_policies=access_policies,
            advanced_options=advanced_options,
            advanced_security_options=advanced_security_options,
            auto_tune_options=auto_tune_options,
            cluster_config=cluster_config,
            cognito_options=cognito_options,
            domain_endpoint_options=domain_endpoint_options,
            ebs_options=ebs_options,
            elasticsearch_version=elasticsearch_version,
            encrypt_at_rest=encrypt_at_rest,
            id=id,
            log_publishing_options=log_publishing_options,
            node_to_node_encryption=node_to_node_encryption,
            snapshot_options=snapshot_options,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
            vpc_options=vpc_options,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAdvancedSecurityOptions")
    def put_advanced_security_options(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        internal_user_database_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        master_user_options: typing.Optional[typing.Union["ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptions", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enabled ElasticsearchDomain#enabled}.
        :param internal_user_database_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#internal_user_database_enabled ElasticsearchDomain#internal_user_database_enabled}.
        :param master_user_options: master_user_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#master_user_options ElasticsearchDomain#master_user_options}
        '''
        value = ElasticsearchDomainAdvancedSecurityOptions(
            enabled=enabled,
            internal_user_database_enabled=internal_user_database_enabled,
            master_user_options=master_user_options,
        )

        return typing.cast(None, jsii.invoke(self, "putAdvancedSecurityOptions", [value]))

    @jsii.member(jsii_name="putAutoTuneOptions")
    def put_auto_tune_options(
        self,
        *,
        desired_state: builtins.str,
        maintenance_schedule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule", typing.Dict[builtins.str, typing.Any]]]]] = None,
        rollback_on_disable: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param desired_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#desired_state ElasticsearchDomain#desired_state}.
        :param maintenance_schedule: maintenance_schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#maintenance_schedule ElasticsearchDomain#maintenance_schedule}
        :param rollback_on_disable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#rollback_on_disable ElasticsearchDomain#rollback_on_disable}.
        '''
        value = ElasticsearchDomainAutoTuneOptions(
            desired_state=desired_state,
            maintenance_schedule=maintenance_schedule,
            rollback_on_disable=rollback_on_disable,
        )

        return typing.cast(None, jsii.invoke(self, "putAutoTuneOptions", [value]))

    @jsii.member(jsii_name="putClusterConfig")
    def put_cluster_config(
        self,
        *,
        cold_storage_options: typing.Optional[typing.Union["ElasticsearchDomainClusterConfigColdStorageOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        dedicated_master_count: typing.Optional[jsii.Number] = None,
        dedicated_master_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        dedicated_master_type: typing.Optional[builtins.str] = None,
        instance_count: typing.Optional[jsii.Number] = None,
        instance_type: typing.Optional[builtins.str] = None,
        warm_count: typing.Optional[jsii.Number] = None,
        warm_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        warm_type: typing.Optional[builtins.str] = None,
        zone_awareness_config: typing.Optional[typing.Union["ElasticsearchDomainClusterConfigZoneAwarenessConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        zone_awareness_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param cold_storage_options: cold_storage_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#cold_storage_options ElasticsearchDomain#cold_storage_options}
        :param dedicated_master_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#dedicated_master_count ElasticsearchDomain#dedicated_master_count}.
        :param dedicated_master_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#dedicated_master_enabled ElasticsearchDomain#dedicated_master_enabled}.
        :param dedicated_master_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#dedicated_master_type ElasticsearchDomain#dedicated_master_type}.
        :param instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#instance_count ElasticsearchDomain#instance_count}.
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#instance_type ElasticsearchDomain#instance_type}.
        :param warm_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#warm_count ElasticsearchDomain#warm_count}.
        :param warm_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#warm_enabled ElasticsearchDomain#warm_enabled}.
        :param warm_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#warm_type ElasticsearchDomain#warm_type}.
        :param zone_awareness_config: zone_awareness_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#zone_awareness_config ElasticsearchDomain#zone_awareness_config}
        :param zone_awareness_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#zone_awareness_enabled ElasticsearchDomain#zone_awareness_enabled}.
        '''
        value = ElasticsearchDomainClusterConfig(
            cold_storage_options=cold_storage_options,
            dedicated_master_count=dedicated_master_count,
            dedicated_master_enabled=dedicated_master_enabled,
            dedicated_master_type=dedicated_master_type,
            instance_count=instance_count,
            instance_type=instance_type,
            warm_count=warm_count,
            warm_enabled=warm_enabled,
            warm_type=warm_type,
            zone_awareness_config=zone_awareness_config,
            zone_awareness_enabled=zone_awareness_enabled,
        )

        return typing.cast(None, jsii.invoke(self, "putClusterConfig", [value]))

    @jsii.member(jsii_name="putCognitoOptions")
    def put_cognito_options(
        self,
        *,
        identity_pool_id: builtins.str,
        role_arn: builtins.str,
        user_pool_id: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param identity_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#identity_pool_id ElasticsearchDomain#identity_pool_id}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#role_arn ElasticsearchDomain#role_arn}.
        :param user_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#user_pool_id ElasticsearchDomain#user_pool_id}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enabled ElasticsearchDomain#enabled}.
        '''
        value = ElasticsearchDomainCognitoOptions(
            identity_pool_id=identity_pool_id,
            role_arn=role_arn,
            user_pool_id=user_pool_id,
            enabled=enabled,
        )

        return typing.cast(None, jsii.invoke(self, "putCognitoOptions", [value]))

    @jsii.member(jsii_name="putDomainEndpointOptions")
    def put_domain_endpoint_options(
        self,
        *,
        custom_endpoint: typing.Optional[builtins.str] = None,
        custom_endpoint_certificate_arn: typing.Optional[builtins.str] = None,
        custom_endpoint_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enforce_https: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tls_security_policy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param custom_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#custom_endpoint ElasticsearchDomain#custom_endpoint}.
        :param custom_endpoint_certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#custom_endpoint_certificate_arn ElasticsearchDomain#custom_endpoint_certificate_arn}.
        :param custom_endpoint_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#custom_endpoint_enabled ElasticsearchDomain#custom_endpoint_enabled}.
        :param enforce_https: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enforce_https ElasticsearchDomain#enforce_https}.
        :param tls_security_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#tls_security_policy ElasticsearchDomain#tls_security_policy}.
        '''
        value = ElasticsearchDomainDomainEndpointOptions(
            custom_endpoint=custom_endpoint,
            custom_endpoint_certificate_arn=custom_endpoint_certificate_arn,
            custom_endpoint_enabled=custom_endpoint_enabled,
            enforce_https=enforce_https,
            tls_security_policy=tls_security_policy,
        )

        return typing.cast(None, jsii.invoke(self, "putDomainEndpointOptions", [value]))

    @jsii.member(jsii_name="putEbsOptions")
    def put_ebs_options(
        self,
        *,
        ebs_enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        iops: typing.Optional[jsii.Number] = None,
        throughput: typing.Optional[jsii.Number] = None,
        volume_size: typing.Optional[jsii.Number] = None,
        volume_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ebs_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#ebs_enabled ElasticsearchDomain#ebs_enabled}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#iops ElasticsearchDomain#iops}.
        :param throughput: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#throughput ElasticsearchDomain#throughput}.
        :param volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#volume_size ElasticsearchDomain#volume_size}.
        :param volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#volume_type ElasticsearchDomain#volume_type}.
        '''
        value = ElasticsearchDomainEbsOptions(
            ebs_enabled=ebs_enabled,
            iops=iops,
            throughput=throughput,
            volume_size=volume_size,
            volume_type=volume_type,
        )

        return typing.cast(None, jsii.invoke(self, "putEbsOptions", [value]))

    @jsii.member(jsii_name="putEncryptAtRest")
    def put_encrypt_at_rest(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        kms_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enabled ElasticsearchDomain#enabled}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#kms_key_id ElasticsearchDomain#kms_key_id}.
        '''
        value = ElasticsearchDomainEncryptAtRest(
            enabled=enabled, kms_key_id=kms_key_id
        )

        return typing.cast(None, jsii.invoke(self, "putEncryptAtRest", [value]))

    @jsii.member(jsii_name="putLogPublishingOptions")
    def put_log_publishing_options(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ElasticsearchDomainLogPublishingOptions", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__255cc620afffd72ac20dbe063f316b3ee2f9c50f174ca8d8f20bff9143cb30f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLogPublishingOptions", [value]))

    @jsii.member(jsii_name="putNodeToNodeEncryption")
    def put_node_to_node_encryption(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enabled ElasticsearchDomain#enabled}.
        '''
        value = ElasticsearchDomainNodeToNodeEncryption(enabled=enabled)

        return typing.cast(None, jsii.invoke(self, "putNodeToNodeEncryption", [value]))

    @jsii.member(jsii_name="putSnapshotOptions")
    def put_snapshot_options(
        self,
        *,
        automated_snapshot_start_hour: jsii.Number,
    ) -> None:
        '''
        :param automated_snapshot_start_hour: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#automated_snapshot_start_hour ElasticsearchDomain#automated_snapshot_start_hour}.
        '''
        value = ElasticsearchDomainSnapshotOptions(
            automated_snapshot_start_hour=automated_snapshot_start_hour
        )

        return typing.cast(None, jsii.invoke(self, "putSnapshotOptions", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#create ElasticsearchDomain#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#delete ElasticsearchDomain#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#update ElasticsearchDomain#update}.
        '''
        value = ElasticsearchDomainTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putVpcOptions")
    def put_vpc_options(
        self,
        *,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#security_group_ids ElasticsearchDomain#security_group_ids}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#subnet_ids ElasticsearchDomain#subnet_ids}.
        '''
        value = ElasticsearchDomainVpcOptions(
            security_group_ids=security_group_ids, subnet_ids=subnet_ids
        )

        return typing.cast(None, jsii.invoke(self, "putVpcOptions", [value]))

    @jsii.member(jsii_name="resetAccessPolicies")
    def reset_access_policies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessPolicies", []))

    @jsii.member(jsii_name="resetAdvancedOptions")
    def reset_advanced_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdvancedOptions", []))

    @jsii.member(jsii_name="resetAdvancedSecurityOptions")
    def reset_advanced_security_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdvancedSecurityOptions", []))

    @jsii.member(jsii_name="resetAutoTuneOptions")
    def reset_auto_tune_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoTuneOptions", []))

    @jsii.member(jsii_name="resetClusterConfig")
    def reset_cluster_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterConfig", []))

    @jsii.member(jsii_name="resetCognitoOptions")
    def reset_cognito_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCognitoOptions", []))

    @jsii.member(jsii_name="resetDomainEndpointOptions")
    def reset_domain_endpoint_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDomainEndpointOptions", []))

    @jsii.member(jsii_name="resetEbsOptions")
    def reset_ebs_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbsOptions", []))

    @jsii.member(jsii_name="resetElasticsearchVersion")
    def reset_elasticsearch_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetElasticsearchVersion", []))

    @jsii.member(jsii_name="resetEncryptAtRest")
    def reset_encrypt_at_rest(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptAtRest", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLogPublishingOptions")
    def reset_log_publishing_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogPublishingOptions", []))

    @jsii.member(jsii_name="resetNodeToNodeEncryption")
    def reset_node_to_node_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeToNodeEncryption", []))

    @jsii.member(jsii_name="resetSnapshotOptions")
    def reset_snapshot_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnapshotOptions", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVpcOptions")
    def reset_vpc_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcOptions", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="advancedSecurityOptions")
    def advanced_security_options(
        self,
    ) -> "ElasticsearchDomainAdvancedSecurityOptionsOutputReference":
        return typing.cast("ElasticsearchDomainAdvancedSecurityOptionsOutputReference", jsii.get(self, "advancedSecurityOptions"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="autoTuneOptions")
    def auto_tune_options(self) -> "ElasticsearchDomainAutoTuneOptionsOutputReference":
        return typing.cast("ElasticsearchDomainAutoTuneOptionsOutputReference", jsii.get(self, "autoTuneOptions"))

    @builtins.property
    @jsii.member(jsii_name="clusterConfig")
    def cluster_config(self) -> "ElasticsearchDomainClusterConfigOutputReference":
        return typing.cast("ElasticsearchDomainClusterConfigOutputReference", jsii.get(self, "clusterConfig"))

    @builtins.property
    @jsii.member(jsii_name="cognitoOptions")
    def cognito_options(self) -> "ElasticsearchDomainCognitoOptionsOutputReference":
        return typing.cast("ElasticsearchDomainCognitoOptionsOutputReference", jsii.get(self, "cognitoOptions"))

    @builtins.property
    @jsii.member(jsii_name="domainEndpointOptions")
    def domain_endpoint_options(
        self,
    ) -> "ElasticsearchDomainDomainEndpointOptionsOutputReference":
        return typing.cast("ElasticsearchDomainDomainEndpointOptionsOutputReference", jsii.get(self, "domainEndpointOptions"))

    @builtins.property
    @jsii.member(jsii_name="domainId")
    def domain_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainId"))

    @builtins.property
    @jsii.member(jsii_name="ebsOptions")
    def ebs_options(self) -> "ElasticsearchDomainEbsOptionsOutputReference":
        return typing.cast("ElasticsearchDomainEbsOptionsOutputReference", jsii.get(self, "ebsOptions"))

    @builtins.property
    @jsii.member(jsii_name="encryptAtRest")
    def encrypt_at_rest(self) -> "ElasticsearchDomainEncryptAtRestOutputReference":
        return typing.cast("ElasticsearchDomainEncryptAtRestOutputReference", jsii.get(self, "encryptAtRest"))

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @builtins.property
    @jsii.member(jsii_name="kibanaEndpoint")
    def kibana_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kibanaEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="logPublishingOptions")
    def log_publishing_options(self) -> "ElasticsearchDomainLogPublishingOptionsList":
        return typing.cast("ElasticsearchDomainLogPublishingOptionsList", jsii.get(self, "logPublishingOptions"))

    @builtins.property
    @jsii.member(jsii_name="nodeToNodeEncryption")
    def node_to_node_encryption(
        self,
    ) -> "ElasticsearchDomainNodeToNodeEncryptionOutputReference":
        return typing.cast("ElasticsearchDomainNodeToNodeEncryptionOutputReference", jsii.get(self, "nodeToNodeEncryption"))

    @builtins.property
    @jsii.member(jsii_name="snapshotOptions")
    def snapshot_options(self) -> "ElasticsearchDomainSnapshotOptionsOutputReference":
        return typing.cast("ElasticsearchDomainSnapshotOptionsOutputReference", jsii.get(self, "snapshotOptions"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ElasticsearchDomainTimeoutsOutputReference":
        return typing.cast("ElasticsearchDomainTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="vpcOptions")
    def vpc_options(self) -> "ElasticsearchDomainVpcOptionsOutputReference":
        return typing.cast("ElasticsearchDomainVpcOptionsOutputReference", jsii.get(self, "vpcOptions"))

    @builtins.property
    @jsii.member(jsii_name="accessPoliciesInput")
    def access_policies_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessPoliciesInput"))

    @builtins.property
    @jsii.member(jsii_name="advancedOptionsInput")
    def advanced_options_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "advancedOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="advancedSecurityOptionsInput")
    def advanced_security_options_input(
        self,
    ) -> typing.Optional["ElasticsearchDomainAdvancedSecurityOptions"]:
        return typing.cast(typing.Optional["ElasticsearchDomainAdvancedSecurityOptions"], jsii.get(self, "advancedSecurityOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="autoTuneOptionsInput")
    def auto_tune_options_input(
        self,
    ) -> typing.Optional["ElasticsearchDomainAutoTuneOptions"]:
        return typing.cast(typing.Optional["ElasticsearchDomainAutoTuneOptions"], jsii.get(self, "autoTuneOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterConfigInput")
    def cluster_config_input(
        self,
    ) -> typing.Optional["ElasticsearchDomainClusterConfig"]:
        return typing.cast(typing.Optional["ElasticsearchDomainClusterConfig"], jsii.get(self, "clusterConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="cognitoOptionsInput")
    def cognito_options_input(
        self,
    ) -> typing.Optional["ElasticsearchDomainCognitoOptions"]:
        return typing.cast(typing.Optional["ElasticsearchDomainCognitoOptions"], jsii.get(self, "cognitoOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="domainEndpointOptionsInput")
    def domain_endpoint_options_input(
        self,
    ) -> typing.Optional["ElasticsearchDomainDomainEndpointOptions"]:
        return typing.cast(typing.Optional["ElasticsearchDomainDomainEndpointOptions"], jsii.get(self, "domainEndpointOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="domainNameInput")
    def domain_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainNameInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsOptionsInput")
    def ebs_options_input(self) -> typing.Optional["ElasticsearchDomainEbsOptions"]:
        return typing.cast(typing.Optional["ElasticsearchDomainEbsOptions"], jsii.get(self, "ebsOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="elasticsearchVersionInput")
    def elasticsearch_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "elasticsearchVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptAtRestInput")
    def encrypt_at_rest_input(
        self,
    ) -> typing.Optional["ElasticsearchDomainEncryptAtRest"]:
        return typing.cast(typing.Optional["ElasticsearchDomainEncryptAtRest"], jsii.get(self, "encryptAtRestInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="logPublishingOptionsInput")
    def log_publishing_options_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ElasticsearchDomainLogPublishingOptions"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ElasticsearchDomainLogPublishingOptions"]]], jsii.get(self, "logPublishingOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeToNodeEncryptionInput")
    def node_to_node_encryption_input(
        self,
    ) -> typing.Optional["ElasticsearchDomainNodeToNodeEncryption"]:
        return typing.cast(typing.Optional["ElasticsearchDomainNodeToNodeEncryption"], jsii.get(self, "nodeToNodeEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="snapshotOptionsInput")
    def snapshot_options_input(
        self,
    ) -> typing.Optional["ElasticsearchDomainSnapshotOptions"]:
        return typing.cast(typing.Optional["ElasticsearchDomainSnapshotOptions"], jsii.get(self, "snapshotOptionsInput"))

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
    ) -> typing.Optional[typing.Union["ElasticsearchDomainTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ElasticsearchDomainTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcOptionsInput")
    def vpc_options_input(self) -> typing.Optional["ElasticsearchDomainVpcOptions"]:
        return typing.cast(typing.Optional["ElasticsearchDomainVpcOptions"], jsii.get(self, "vpcOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="accessPolicies")
    def access_policies(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessPolicies"))

    @access_policies.setter
    def access_policies(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00fa3763d84412ba94ee632a8eef8ea0c775a937f9148893d8ec82bd511761ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessPolicies", value)

    @builtins.property
    @jsii.member(jsii_name="advancedOptions")
    def advanced_options(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "advancedOptions"))

    @advanced_options.setter
    def advanced_options(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aae4291790bbc230744e7c4a1e4305ca6928b8778c4c55cdb2b14725689ac3bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "advancedOptions", value)

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__585206f93b9284a2dbf322ac6dbe7004fce5b92fc891de42694f464f9ab9891f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="elasticsearchVersion")
    def elasticsearch_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "elasticsearchVersion"))

    @elasticsearch_version.setter
    def elasticsearch_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfe5226151713328155dff362e32499b4c2542d53862da13accfee5bb6ec3157)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticsearchVersion", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3bca2bbe32b9046aca1af278c9cbc0b8280c10a046e41a2a10955b1c7e40f31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9722096c981f240e78f2cbaf17f8e8b99bf84325a9d2ae203d7a61fccda372ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78244a80a4ae44052048db28acf1a5607663340e154d6471a0b0edec3a264889)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomainAdvancedSecurityOptions",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "internal_user_database_enabled": "internalUserDatabaseEnabled",
        "master_user_options": "masterUserOptions",
    },
)
class ElasticsearchDomainAdvancedSecurityOptions:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        internal_user_database_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        master_user_options: typing.Optional[typing.Union["ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptions", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enabled ElasticsearchDomain#enabled}.
        :param internal_user_database_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#internal_user_database_enabled ElasticsearchDomain#internal_user_database_enabled}.
        :param master_user_options: master_user_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#master_user_options ElasticsearchDomain#master_user_options}
        '''
        if isinstance(master_user_options, dict):
            master_user_options = ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptions(**master_user_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76174cdd3234959d6752fe751ddcdf8e7d3ca10594354d1e6c5f34c27f8e1202)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument internal_user_database_enabled", value=internal_user_database_enabled, expected_type=type_hints["internal_user_database_enabled"])
            check_type(argname="argument master_user_options", value=master_user_options, expected_type=type_hints["master_user_options"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled": enabled,
        }
        if internal_user_database_enabled is not None:
            self._values["internal_user_database_enabled"] = internal_user_database_enabled
        if master_user_options is not None:
            self._values["master_user_options"] = master_user_options

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enabled ElasticsearchDomain#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def internal_user_database_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#internal_user_database_enabled ElasticsearchDomain#internal_user_database_enabled}.'''
        result = self._values.get("internal_user_database_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def master_user_options(
        self,
    ) -> typing.Optional["ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptions"]:
        '''master_user_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#master_user_options ElasticsearchDomain#master_user_options}
        '''
        result = self._values.get("master_user_options")
        return typing.cast(typing.Optional["ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainAdvancedSecurityOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptions",
    jsii_struct_bases=[],
    name_mapping={
        "master_user_arn": "masterUserArn",
        "master_user_name": "masterUserName",
        "master_user_password": "masterUserPassword",
    },
)
class ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptions:
    def __init__(
        self,
        *,
        master_user_arn: typing.Optional[builtins.str] = None,
        master_user_name: typing.Optional[builtins.str] = None,
        master_user_password: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param master_user_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#master_user_arn ElasticsearchDomain#master_user_arn}.
        :param master_user_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#master_user_name ElasticsearchDomain#master_user_name}.
        :param master_user_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#master_user_password ElasticsearchDomain#master_user_password}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff024a8e397e688677a55ce8b7029c85b729f6fa7f0cd3b82db401f5ff87026e)
            check_type(argname="argument master_user_arn", value=master_user_arn, expected_type=type_hints["master_user_arn"])
            check_type(argname="argument master_user_name", value=master_user_name, expected_type=type_hints["master_user_name"])
            check_type(argname="argument master_user_password", value=master_user_password, expected_type=type_hints["master_user_password"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if master_user_arn is not None:
            self._values["master_user_arn"] = master_user_arn
        if master_user_name is not None:
            self._values["master_user_name"] = master_user_name
        if master_user_password is not None:
            self._values["master_user_password"] = master_user_password

    @builtins.property
    def master_user_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#master_user_arn ElasticsearchDomain#master_user_arn}.'''
        result = self._values.get("master_user_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def master_user_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#master_user_name ElasticsearchDomain#master_user_name}.'''
        result = self._values.get("master_user_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def master_user_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#master_user_password ElasticsearchDomain#master_user_password}.'''
        result = self._values.get("master_user_password")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dd28188f5f9e09658b9ea7c3ce57de02c873bd0f8ceeac7a322120548c934a9f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMasterUserArn")
    def reset_master_user_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMasterUserArn", []))

    @jsii.member(jsii_name="resetMasterUserName")
    def reset_master_user_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMasterUserName", []))

    @jsii.member(jsii_name="resetMasterUserPassword")
    def reset_master_user_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMasterUserPassword", []))

    @builtins.property
    @jsii.member(jsii_name="masterUserArnInput")
    def master_user_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "masterUserArnInput"))

    @builtins.property
    @jsii.member(jsii_name="masterUserNameInput")
    def master_user_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "masterUserNameInput"))

    @builtins.property
    @jsii.member(jsii_name="masterUserPasswordInput")
    def master_user_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "masterUserPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="masterUserArn")
    def master_user_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "masterUserArn"))

    @master_user_arn.setter
    def master_user_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__685195492bce25b8a88afd4fca03ed478b297d7a27c433de7f747bd32ac03e00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "masterUserArn", value)

    @builtins.property
    @jsii.member(jsii_name="masterUserName")
    def master_user_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "masterUserName"))

    @master_user_name.setter
    def master_user_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76aabdaba7c690f2326af4a2c518fb7eb5ef6f05185008dc001e35f5716e4b18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "masterUserName", value)

    @builtins.property
    @jsii.member(jsii_name="masterUserPassword")
    def master_user_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "masterUserPassword"))

    @master_user_password.setter
    def master_user_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7562effacc6009e685ddd3802cd691f77227fce3bab07a75121dadf03ce7c3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "masterUserPassword", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptions]:
        return typing.cast(typing.Optional[ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee8a5bd5290f29a5cba7983ca3ed0ee79f1412c9af1b98efe9815032a2b27998)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElasticsearchDomainAdvancedSecurityOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomainAdvancedSecurityOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__eebe9fe6b1fc85ba55e174a63e6acbab96f9ef8031ae7056595c751bd523d80c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMasterUserOptions")
    def put_master_user_options(
        self,
        *,
        master_user_arn: typing.Optional[builtins.str] = None,
        master_user_name: typing.Optional[builtins.str] = None,
        master_user_password: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param master_user_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#master_user_arn ElasticsearchDomain#master_user_arn}.
        :param master_user_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#master_user_name ElasticsearchDomain#master_user_name}.
        :param master_user_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#master_user_password ElasticsearchDomain#master_user_password}.
        '''
        value = ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptions(
            master_user_arn=master_user_arn,
            master_user_name=master_user_name,
            master_user_password=master_user_password,
        )

        return typing.cast(None, jsii.invoke(self, "putMasterUserOptions", [value]))

    @jsii.member(jsii_name="resetInternalUserDatabaseEnabled")
    def reset_internal_user_database_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInternalUserDatabaseEnabled", []))

    @jsii.member(jsii_name="resetMasterUserOptions")
    def reset_master_user_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMasterUserOptions", []))

    @builtins.property
    @jsii.member(jsii_name="masterUserOptions")
    def master_user_options(
        self,
    ) -> ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptionsOutputReference:
        return typing.cast(ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptionsOutputReference, jsii.get(self, "masterUserOptions"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="internalUserDatabaseEnabledInput")
    def internal_user_database_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalUserDatabaseEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="masterUserOptionsInput")
    def master_user_options_input(
        self,
    ) -> typing.Optional[ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptions]:
        return typing.cast(typing.Optional[ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptions], jsii.get(self, "masterUserOptionsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__ddc2c9fffbe7e55f7706d7794714b9f041bf2fe71b8aa4cf2bc073dbae41025d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalUserDatabaseEnabled")
    def internal_user_database_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "internalUserDatabaseEnabled"))

    @internal_user_database_enabled.setter
    def internal_user_database_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4dc3f0f8ab9813c6a467c68a8c1d6e73a85e6535bbcee7dcefae5d55c290a0d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalUserDatabaseEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ElasticsearchDomainAdvancedSecurityOptions]:
        return typing.cast(typing.Optional[ElasticsearchDomainAdvancedSecurityOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElasticsearchDomainAdvancedSecurityOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6b5714de15c286cd29338994d29d3caa786365c36bfb71d40b2c4f7338f1bf8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomainAutoTuneOptions",
    jsii_struct_bases=[],
    name_mapping={
        "desired_state": "desiredState",
        "maintenance_schedule": "maintenanceSchedule",
        "rollback_on_disable": "rollbackOnDisable",
    },
)
class ElasticsearchDomainAutoTuneOptions:
    def __init__(
        self,
        *,
        desired_state: builtins.str,
        maintenance_schedule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule", typing.Dict[builtins.str, typing.Any]]]]] = None,
        rollback_on_disable: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param desired_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#desired_state ElasticsearchDomain#desired_state}.
        :param maintenance_schedule: maintenance_schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#maintenance_schedule ElasticsearchDomain#maintenance_schedule}
        :param rollback_on_disable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#rollback_on_disable ElasticsearchDomain#rollback_on_disable}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a53f816fcb52385c3ac2f33f0b98238df1c607f3bbf77af26e386bbda00acc6b)
            check_type(argname="argument desired_state", value=desired_state, expected_type=type_hints["desired_state"])
            check_type(argname="argument maintenance_schedule", value=maintenance_schedule, expected_type=type_hints["maintenance_schedule"])
            check_type(argname="argument rollback_on_disable", value=rollback_on_disable, expected_type=type_hints["rollback_on_disable"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "desired_state": desired_state,
        }
        if maintenance_schedule is not None:
            self._values["maintenance_schedule"] = maintenance_schedule
        if rollback_on_disable is not None:
            self._values["rollback_on_disable"] = rollback_on_disable

    @builtins.property
    def desired_state(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#desired_state ElasticsearchDomain#desired_state}.'''
        result = self._values.get("desired_state")
        assert result is not None, "Required property 'desired_state' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def maintenance_schedule(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule"]]]:
        '''maintenance_schedule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#maintenance_schedule ElasticsearchDomain#maintenance_schedule}
        '''
        result = self._values.get("maintenance_schedule")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule"]]], result)

    @builtins.property
    def rollback_on_disable(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#rollback_on_disable ElasticsearchDomain#rollback_on_disable}.'''
        result = self._values.get("rollback_on_disable")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainAutoTuneOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule",
    jsii_struct_bases=[],
    name_mapping={
        "cron_expression_for_recurrence": "cronExpressionForRecurrence",
        "duration": "duration",
        "start_at": "startAt",
    },
)
class ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule:
    def __init__(
        self,
        *,
        cron_expression_for_recurrence: builtins.str,
        duration: typing.Union["ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration", typing.Dict[builtins.str, typing.Any]],
        start_at: builtins.str,
    ) -> None:
        '''
        :param cron_expression_for_recurrence: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#cron_expression_for_recurrence ElasticsearchDomain#cron_expression_for_recurrence}.
        :param duration: duration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#duration ElasticsearchDomain#duration}
        :param start_at: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#start_at ElasticsearchDomain#start_at}.
        '''
        if isinstance(duration, dict):
            duration = ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration(**duration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e356f742a4fa462b72e44fe9506472f535cfaced003c8dbce0a6675df39c1c32)
            check_type(argname="argument cron_expression_for_recurrence", value=cron_expression_for_recurrence, expected_type=type_hints["cron_expression_for_recurrence"])
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
            check_type(argname="argument start_at", value=start_at, expected_type=type_hints["start_at"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cron_expression_for_recurrence": cron_expression_for_recurrence,
            "duration": duration,
            "start_at": start_at,
        }

    @builtins.property
    def cron_expression_for_recurrence(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#cron_expression_for_recurrence ElasticsearchDomain#cron_expression_for_recurrence}.'''
        result = self._values.get("cron_expression_for_recurrence")
        assert result is not None, "Required property 'cron_expression_for_recurrence' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def duration(
        self,
    ) -> "ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration":
        '''duration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#duration ElasticsearchDomain#duration}
        '''
        result = self._values.get("duration")
        assert result is not None, "Required property 'duration' is missing"
        return typing.cast("ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration", result)

    @builtins.property
    def start_at(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#start_at ElasticsearchDomain#start_at}.'''
        result = self._values.get("start_at")
        assert result is not None, "Required property 'start_at' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration",
    jsii_struct_bases=[],
    name_mapping={"unit": "unit", "value": "value"},
)
class ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration:
    def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#unit ElasticsearchDomain#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#value ElasticsearchDomain#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ee6cb8696144b94768717236eba268ac5761fe8e98a482472dd5020cb484669)
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "unit": unit,
            "value": value,
        }

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#unit ElasticsearchDomain#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#value ElasticsearchDomain#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6a516a5473b1fd2e45452a5019a15d3a9e6617de4b0bffe0de4d17b599605693)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__476014720408fb784c63fd6f2167965ead8135ccdaa059027ebc89a08798e9c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64f321a53a920c0382a809e498262c04786f82d5cd7313b8b49bbde9feb0d8c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration]:
        return typing.cast(typing.Optional[ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__850de46e583db188c3d8777103bbc9c8a180427d4929fd78fc5e770dc33a445b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ece35779c6c1784d2d922f90f11555f8decce8d66ff7f4aacc9ab5be7fc9d8b6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfd62e791633c8d71e7dda56866a409f35a213f1ffe0e5334b35e6812eec21cf)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__843d936aec7e40d93356a5cfc10ff378ac32698371dc2a36a01e3c76c34756e8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__21d5707e2011dbd9884ff177b3ffded9babee4c8af609bec66383186936f18c5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5be31a5a307513337c134efbb2579ea40f092e4b1c7cbcb4b8097cfdf52582ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf775c58e3fdf9ade89e338f44d511764c81d1f4dfe4aa51f536635725f7ebc3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ca31677121bde88c89488a93b90a1201d7a1e7cabf663b656b1d2524bcf1e692)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDuration")
    def put_duration(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#unit ElasticsearchDomain#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#value ElasticsearchDomain#value}.
        '''
        value_ = ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration(
            unit=unit, value=value
        )

        return typing.cast(None, jsii.invoke(self, "putDuration", [value_]))

    @builtins.property
    @jsii.member(jsii_name="duration")
    def duration(
        self,
    ) -> ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDurationOutputReference:
        return typing.cast(ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDurationOutputReference, jsii.get(self, "duration"))

    @builtins.property
    @jsii.member(jsii_name="cronExpressionForRecurrenceInput")
    def cron_expression_for_recurrence_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cronExpressionForRecurrenceInput"))

    @builtins.property
    @jsii.member(jsii_name="durationInput")
    def duration_input(
        self,
    ) -> typing.Optional[ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration]:
        return typing.cast(typing.Optional[ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration], jsii.get(self, "durationInput"))

    @builtins.property
    @jsii.member(jsii_name="startAtInput")
    def start_at_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startAtInput"))

    @builtins.property
    @jsii.member(jsii_name="cronExpressionForRecurrence")
    def cron_expression_for_recurrence(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cronExpressionForRecurrence"))

    @cron_expression_for_recurrence.setter
    def cron_expression_for_recurrence(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b358a873ae6d932a9e9203cb0807333b82df7a91b07d6733ef59c4b65721d947)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cronExpressionForRecurrence", value)

    @builtins.property
    @jsii.member(jsii_name="startAt")
    def start_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startAt"))

    @start_at.setter
    def start_at(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__205edd25aa049b59fd03c27b2ed5ddef832aa18d7827bb860efee5c764e27532)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startAt", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe77012b5554218047f4f8236c3c19545d29bd04a36039e75b3b988fa1e7d77b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElasticsearchDomainAutoTuneOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomainAutoTuneOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c198b6f3fda8961d53e1afbc92d50575329100fafa8da1575c6f9dde04ed5115)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMaintenanceSchedule")
    def put_maintenance_schedule(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b2e410285b8ed729204d30d63ff3d82f3be575e00174932f1e91bae4fa8201f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMaintenanceSchedule", [value]))

    @jsii.member(jsii_name="resetMaintenanceSchedule")
    def reset_maintenance_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaintenanceSchedule", []))

    @jsii.member(jsii_name="resetRollbackOnDisable")
    def reset_rollback_on_disable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRollbackOnDisable", []))

    @builtins.property
    @jsii.member(jsii_name="maintenanceSchedule")
    def maintenance_schedule(
        self,
    ) -> ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleList:
        return typing.cast(ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleList, jsii.get(self, "maintenanceSchedule"))

    @builtins.property
    @jsii.member(jsii_name="desiredStateInput")
    def desired_state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "desiredStateInput"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceScheduleInput")
    def maintenance_schedule_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule]]], jsii.get(self, "maintenanceScheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="rollbackOnDisableInput")
    def rollback_on_disable_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rollbackOnDisableInput"))

    @builtins.property
    @jsii.member(jsii_name="desiredState")
    def desired_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "desiredState"))

    @desired_state.setter
    def desired_state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbf39a80a28ff988d7f3ad019f2487f583c1e9f3a085fcac22127225075fc3df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desiredState", value)

    @builtins.property
    @jsii.member(jsii_name="rollbackOnDisable")
    def rollback_on_disable(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rollbackOnDisable"))

    @rollback_on_disable.setter
    def rollback_on_disable(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e0260ff80363c3f99cc1e98c626c75f0c1537ebd3040803fc6a9610d5473a6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rollbackOnDisable", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElasticsearchDomainAutoTuneOptions]:
        return typing.cast(typing.Optional[ElasticsearchDomainAutoTuneOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElasticsearchDomainAutoTuneOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d45a02b28b9bb71aa9ece4f8c9026abef5b7e59fe71465bdfdfbe93b029c444)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomainClusterConfig",
    jsii_struct_bases=[],
    name_mapping={
        "cold_storage_options": "coldStorageOptions",
        "dedicated_master_count": "dedicatedMasterCount",
        "dedicated_master_enabled": "dedicatedMasterEnabled",
        "dedicated_master_type": "dedicatedMasterType",
        "instance_count": "instanceCount",
        "instance_type": "instanceType",
        "warm_count": "warmCount",
        "warm_enabled": "warmEnabled",
        "warm_type": "warmType",
        "zone_awareness_config": "zoneAwarenessConfig",
        "zone_awareness_enabled": "zoneAwarenessEnabled",
    },
)
class ElasticsearchDomainClusterConfig:
    def __init__(
        self,
        *,
        cold_storage_options: typing.Optional[typing.Union["ElasticsearchDomainClusterConfigColdStorageOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        dedicated_master_count: typing.Optional[jsii.Number] = None,
        dedicated_master_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        dedicated_master_type: typing.Optional[builtins.str] = None,
        instance_count: typing.Optional[jsii.Number] = None,
        instance_type: typing.Optional[builtins.str] = None,
        warm_count: typing.Optional[jsii.Number] = None,
        warm_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        warm_type: typing.Optional[builtins.str] = None,
        zone_awareness_config: typing.Optional[typing.Union["ElasticsearchDomainClusterConfigZoneAwarenessConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        zone_awareness_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param cold_storage_options: cold_storage_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#cold_storage_options ElasticsearchDomain#cold_storage_options}
        :param dedicated_master_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#dedicated_master_count ElasticsearchDomain#dedicated_master_count}.
        :param dedicated_master_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#dedicated_master_enabled ElasticsearchDomain#dedicated_master_enabled}.
        :param dedicated_master_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#dedicated_master_type ElasticsearchDomain#dedicated_master_type}.
        :param instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#instance_count ElasticsearchDomain#instance_count}.
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#instance_type ElasticsearchDomain#instance_type}.
        :param warm_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#warm_count ElasticsearchDomain#warm_count}.
        :param warm_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#warm_enabled ElasticsearchDomain#warm_enabled}.
        :param warm_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#warm_type ElasticsearchDomain#warm_type}.
        :param zone_awareness_config: zone_awareness_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#zone_awareness_config ElasticsearchDomain#zone_awareness_config}
        :param zone_awareness_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#zone_awareness_enabled ElasticsearchDomain#zone_awareness_enabled}.
        '''
        if isinstance(cold_storage_options, dict):
            cold_storage_options = ElasticsearchDomainClusterConfigColdStorageOptions(**cold_storage_options)
        if isinstance(zone_awareness_config, dict):
            zone_awareness_config = ElasticsearchDomainClusterConfigZoneAwarenessConfig(**zone_awareness_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81c0a7acc3844745ac6ed302f61fa9d093c7a51fa25f17d651970dde0331c7a3)
            check_type(argname="argument cold_storage_options", value=cold_storage_options, expected_type=type_hints["cold_storage_options"])
            check_type(argname="argument dedicated_master_count", value=dedicated_master_count, expected_type=type_hints["dedicated_master_count"])
            check_type(argname="argument dedicated_master_enabled", value=dedicated_master_enabled, expected_type=type_hints["dedicated_master_enabled"])
            check_type(argname="argument dedicated_master_type", value=dedicated_master_type, expected_type=type_hints["dedicated_master_type"])
            check_type(argname="argument instance_count", value=instance_count, expected_type=type_hints["instance_count"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument warm_count", value=warm_count, expected_type=type_hints["warm_count"])
            check_type(argname="argument warm_enabled", value=warm_enabled, expected_type=type_hints["warm_enabled"])
            check_type(argname="argument warm_type", value=warm_type, expected_type=type_hints["warm_type"])
            check_type(argname="argument zone_awareness_config", value=zone_awareness_config, expected_type=type_hints["zone_awareness_config"])
            check_type(argname="argument zone_awareness_enabled", value=zone_awareness_enabled, expected_type=type_hints["zone_awareness_enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cold_storage_options is not None:
            self._values["cold_storage_options"] = cold_storage_options
        if dedicated_master_count is not None:
            self._values["dedicated_master_count"] = dedicated_master_count
        if dedicated_master_enabled is not None:
            self._values["dedicated_master_enabled"] = dedicated_master_enabled
        if dedicated_master_type is not None:
            self._values["dedicated_master_type"] = dedicated_master_type
        if instance_count is not None:
            self._values["instance_count"] = instance_count
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if warm_count is not None:
            self._values["warm_count"] = warm_count
        if warm_enabled is not None:
            self._values["warm_enabled"] = warm_enabled
        if warm_type is not None:
            self._values["warm_type"] = warm_type
        if zone_awareness_config is not None:
            self._values["zone_awareness_config"] = zone_awareness_config
        if zone_awareness_enabled is not None:
            self._values["zone_awareness_enabled"] = zone_awareness_enabled

    @builtins.property
    def cold_storage_options(
        self,
    ) -> typing.Optional["ElasticsearchDomainClusterConfigColdStorageOptions"]:
        '''cold_storage_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#cold_storage_options ElasticsearchDomain#cold_storage_options}
        '''
        result = self._values.get("cold_storage_options")
        return typing.cast(typing.Optional["ElasticsearchDomainClusterConfigColdStorageOptions"], result)

    @builtins.property
    def dedicated_master_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#dedicated_master_count ElasticsearchDomain#dedicated_master_count}.'''
        result = self._values.get("dedicated_master_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def dedicated_master_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#dedicated_master_enabled ElasticsearchDomain#dedicated_master_enabled}.'''
        result = self._values.get("dedicated_master_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def dedicated_master_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#dedicated_master_type ElasticsearchDomain#dedicated_master_type}.'''
        result = self._values.get("dedicated_master_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#instance_count ElasticsearchDomain#instance_count}.'''
        result = self._values.get("instance_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def instance_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#instance_type ElasticsearchDomain#instance_type}.'''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def warm_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#warm_count ElasticsearchDomain#warm_count}.'''
        result = self._values.get("warm_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def warm_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#warm_enabled ElasticsearchDomain#warm_enabled}.'''
        result = self._values.get("warm_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def warm_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#warm_type ElasticsearchDomain#warm_type}.'''
        result = self._values.get("warm_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def zone_awareness_config(
        self,
    ) -> typing.Optional["ElasticsearchDomainClusterConfigZoneAwarenessConfig"]:
        '''zone_awareness_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#zone_awareness_config ElasticsearchDomain#zone_awareness_config}
        '''
        result = self._values.get("zone_awareness_config")
        return typing.cast(typing.Optional["ElasticsearchDomainClusterConfigZoneAwarenessConfig"], result)

    @builtins.property
    def zone_awareness_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#zone_awareness_enabled ElasticsearchDomain#zone_awareness_enabled}.'''
        result = self._values.get("zone_awareness_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomainClusterConfigColdStorageOptions",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class ElasticsearchDomainClusterConfigColdStorageOptions:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enabled ElasticsearchDomain#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__479d775c30bda984294d556f9abcce98f527241ec3c207e98048c3e1dff431e7)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enabled ElasticsearchDomain#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainClusterConfigColdStorageOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElasticsearchDomainClusterConfigColdStorageOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomainClusterConfigColdStorageOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__26c20d73f5f847ddabea4892b92cd636d36a2ceab85df3c1bbf4149ffb6b0b73)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ad348d90c6963a60891ffef745db65e8686fa9e96c6d40e0ec3c33fb9ee9e910)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ElasticsearchDomainClusterConfigColdStorageOptions]:
        return typing.cast(typing.Optional[ElasticsearchDomainClusterConfigColdStorageOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElasticsearchDomainClusterConfigColdStorageOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__edffec25ffd532006726e62bf6988d26e8f4e7b258726aef825d8f0c4b47bcaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElasticsearchDomainClusterConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomainClusterConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1f3153beeeaba79f2e818b6024ff7eb8e29f99dc8bc6926debe0980c2bd65f7e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putColdStorageOptions")
    def put_cold_storage_options(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enabled ElasticsearchDomain#enabled}.
        '''
        value = ElasticsearchDomainClusterConfigColdStorageOptions(enabled=enabled)

        return typing.cast(None, jsii.invoke(self, "putColdStorageOptions", [value]))

    @jsii.member(jsii_name="putZoneAwarenessConfig")
    def put_zone_awareness_config(
        self,
        *,
        availability_zone_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param availability_zone_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#availability_zone_count ElasticsearchDomain#availability_zone_count}.
        '''
        value = ElasticsearchDomainClusterConfigZoneAwarenessConfig(
            availability_zone_count=availability_zone_count
        )

        return typing.cast(None, jsii.invoke(self, "putZoneAwarenessConfig", [value]))

    @jsii.member(jsii_name="resetColdStorageOptions")
    def reset_cold_storage_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetColdStorageOptions", []))

    @jsii.member(jsii_name="resetDedicatedMasterCount")
    def reset_dedicated_master_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDedicatedMasterCount", []))

    @jsii.member(jsii_name="resetDedicatedMasterEnabled")
    def reset_dedicated_master_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDedicatedMasterEnabled", []))

    @jsii.member(jsii_name="resetDedicatedMasterType")
    def reset_dedicated_master_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDedicatedMasterType", []))

    @jsii.member(jsii_name="resetInstanceCount")
    def reset_instance_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceCount", []))

    @jsii.member(jsii_name="resetInstanceType")
    def reset_instance_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceType", []))

    @jsii.member(jsii_name="resetWarmCount")
    def reset_warm_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWarmCount", []))

    @jsii.member(jsii_name="resetWarmEnabled")
    def reset_warm_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWarmEnabled", []))

    @jsii.member(jsii_name="resetWarmType")
    def reset_warm_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWarmType", []))

    @jsii.member(jsii_name="resetZoneAwarenessConfig")
    def reset_zone_awareness_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZoneAwarenessConfig", []))

    @jsii.member(jsii_name="resetZoneAwarenessEnabled")
    def reset_zone_awareness_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZoneAwarenessEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="coldStorageOptions")
    def cold_storage_options(
        self,
    ) -> ElasticsearchDomainClusterConfigColdStorageOptionsOutputReference:
        return typing.cast(ElasticsearchDomainClusterConfigColdStorageOptionsOutputReference, jsii.get(self, "coldStorageOptions"))

    @builtins.property
    @jsii.member(jsii_name="zoneAwarenessConfig")
    def zone_awareness_config(
        self,
    ) -> "ElasticsearchDomainClusterConfigZoneAwarenessConfigOutputReference":
        return typing.cast("ElasticsearchDomainClusterConfigZoneAwarenessConfigOutputReference", jsii.get(self, "zoneAwarenessConfig"))

    @builtins.property
    @jsii.member(jsii_name="coldStorageOptionsInput")
    def cold_storage_options_input(
        self,
    ) -> typing.Optional[ElasticsearchDomainClusterConfigColdStorageOptions]:
        return typing.cast(typing.Optional[ElasticsearchDomainClusterConfigColdStorageOptions], jsii.get(self, "coldStorageOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="dedicatedMasterCountInput")
    def dedicated_master_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dedicatedMasterCountInput"))

    @builtins.property
    @jsii.member(jsii_name="dedicatedMasterEnabledInput")
    def dedicated_master_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "dedicatedMasterEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="dedicatedMasterTypeInput")
    def dedicated_master_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dedicatedMasterTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceCountInput")
    def instance_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "instanceCountInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="warmCountInput")
    def warm_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "warmCountInput"))

    @builtins.property
    @jsii.member(jsii_name="warmEnabledInput")
    def warm_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "warmEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="warmTypeInput")
    def warm_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "warmTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneAwarenessConfigInput")
    def zone_awareness_config_input(
        self,
    ) -> typing.Optional["ElasticsearchDomainClusterConfigZoneAwarenessConfig"]:
        return typing.cast(typing.Optional["ElasticsearchDomainClusterConfigZoneAwarenessConfig"], jsii.get(self, "zoneAwarenessConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneAwarenessEnabledInput")
    def zone_awareness_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "zoneAwarenessEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="dedicatedMasterCount")
    def dedicated_master_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dedicatedMasterCount"))

    @dedicated_master_count.setter
    def dedicated_master_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20c5c5757b8dba94544a9fe44bddc3cd7c311d96a72a38199bbbe38b6abcf680)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dedicatedMasterCount", value)

    @builtins.property
    @jsii.member(jsii_name="dedicatedMasterEnabled")
    def dedicated_master_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "dedicatedMasterEnabled"))

    @dedicated_master_enabled.setter
    def dedicated_master_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af44548e9560e1cd704963e2cdcb41444f72f9b6e05eb79fc21692e239de8c19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dedicatedMasterEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="dedicatedMasterType")
    def dedicated_master_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dedicatedMasterType"))

    @dedicated_master_type.setter
    def dedicated_master_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__143efb348dcaf873c68adba9782af2c4a1af54c6ab4a2e6f289f212c2f4dbd3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dedicatedMasterType", value)

    @builtins.property
    @jsii.member(jsii_name="instanceCount")
    def instance_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instanceCount"))

    @instance_count.setter
    def instance_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dda1326afb9746000331deb553e7d186aacf665c5c1fc7097e53b2a52a330c2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceCount", value)

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__527c276d79a9f15bbebb71d987d6f3aced9b2681c5e5e9249638fcc558665ed9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="warmCount")
    def warm_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "warmCount"))

    @warm_count.setter
    def warm_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8711a856553b3eebc3fdb9bc0a753ca0dc120eb5a7cfd50c30a6a548c3677c35)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "warmCount", value)

    @builtins.property
    @jsii.member(jsii_name="warmEnabled")
    def warm_enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "warmEnabled"))

    @warm_enabled.setter
    def warm_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac75e56da3ff5f98c22e56e014415871d74388cdd3874fd2562d55074ca382fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "warmEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="warmType")
    def warm_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "warmType"))

    @warm_type.setter
    def warm_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d64d192ec3b4fd1782a874675ed0ed2b89fd75ddbe761a18074a1e127ca5877)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "warmType", value)

    @builtins.property
    @jsii.member(jsii_name="zoneAwarenessEnabled")
    def zone_awareness_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "zoneAwarenessEnabled"))

    @zone_awareness_enabled.setter
    def zone_awareness_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac8d94cba14a59b227a36d4867b920cd9180eed8016778cff61b2c2fbab89778)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneAwarenessEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElasticsearchDomainClusterConfig]:
        return typing.cast(typing.Optional[ElasticsearchDomainClusterConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElasticsearchDomainClusterConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ff8519a781690a93a441f4acc801244dcc49e8d996cdcef70c76d6dc7ac1df2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomainClusterConfigZoneAwarenessConfig",
    jsii_struct_bases=[],
    name_mapping={"availability_zone_count": "availabilityZoneCount"},
)
class ElasticsearchDomainClusterConfigZoneAwarenessConfig:
    def __init__(
        self,
        *,
        availability_zone_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param availability_zone_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#availability_zone_count ElasticsearchDomain#availability_zone_count}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__247050f0a0a9abef8e81213dbc8fd21f0c9a096af3379cf9546dc1c2f33a9483)
            check_type(argname="argument availability_zone_count", value=availability_zone_count, expected_type=type_hints["availability_zone_count"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if availability_zone_count is not None:
            self._values["availability_zone_count"] = availability_zone_count

    @builtins.property
    def availability_zone_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#availability_zone_count ElasticsearchDomain#availability_zone_count}.'''
        result = self._values.get("availability_zone_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainClusterConfigZoneAwarenessConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElasticsearchDomainClusterConfigZoneAwarenessConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomainClusterConfigZoneAwarenessConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0808be7db6c351c3447489a31a87eb1931bddc5ffdf4a169c78f429b44334eea)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAvailabilityZoneCount")
    def reset_availability_zone_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailabilityZoneCount", []))

    @builtins.property
    @jsii.member(jsii_name="availabilityZoneCountInput")
    def availability_zone_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "availabilityZoneCountInput"))

    @builtins.property
    @jsii.member(jsii_name="availabilityZoneCount")
    def availability_zone_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "availabilityZoneCount"))

    @availability_zone_count.setter
    def availability_zone_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abd43063eaa20e48d0da22b18d1d40c16ee2d6e65489ca5e00e3166a76e1db61)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZoneCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ElasticsearchDomainClusterConfigZoneAwarenessConfig]:
        return typing.cast(typing.Optional[ElasticsearchDomainClusterConfigZoneAwarenessConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElasticsearchDomainClusterConfigZoneAwarenessConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9584c9490291add30aea492364a9c71bfbdf13d6b2aea84d4d37ac80bf56e6b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomainCognitoOptions",
    jsii_struct_bases=[],
    name_mapping={
        "identity_pool_id": "identityPoolId",
        "role_arn": "roleArn",
        "user_pool_id": "userPoolId",
        "enabled": "enabled",
    },
)
class ElasticsearchDomainCognitoOptions:
    def __init__(
        self,
        *,
        identity_pool_id: builtins.str,
        role_arn: builtins.str,
        user_pool_id: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param identity_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#identity_pool_id ElasticsearchDomain#identity_pool_id}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#role_arn ElasticsearchDomain#role_arn}.
        :param user_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#user_pool_id ElasticsearchDomain#user_pool_id}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enabled ElasticsearchDomain#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52aadd6cce9caeb647841cb9198ab84b2610e694c9c6f2883bc6cab43cb06b87)
            check_type(argname="argument identity_pool_id", value=identity_pool_id, expected_type=type_hints["identity_pool_id"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument user_pool_id", value=user_pool_id, expected_type=type_hints["user_pool_id"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "identity_pool_id": identity_pool_id,
            "role_arn": role_arn,
            "user_pool_id": user_pool_id,
        }
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def identity_pool_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#identity_pool_id ElasticsearchDomain#identity_pool_id}.'''
        result = self._values.get("identity_pool_id")
        assert result is not None, "Required property 'identity_pool_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#role_arn ElasticsearchDomain#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_pool_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#user_pool_id ElasticsearchDomain#user_pool_id}.'''
        result = self._values.get("user_pool_id")
        assert result is not None, "Required property 'user_pool_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enabled ElasticsearchDomain#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainCognitoOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElasticsearchDomainCognitoOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomainCognitoOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8a15cf92c49c64df8ed4268743f6b479124521b70d41720a4dda6a54c1165258)
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
    @jsii.member(jsii_name="identityPoolIdInput")
    def identity_pool_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityPoolIdInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="userPoolIdInput")
    def user_pool_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userPoolIdInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__ee81860aaffdffdcff57ff0729341e70959b44ad8ab4735931df860ccb04439f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="identityPoolId")
    def identity_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityPoolId"))

    @identity_pool_id.setter
    def identity_pool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dba75aa9e8dcaad27b88d5969c7347d38504923c653d289717f1ec94793a0e86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityPoolId", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98b0bb10148652611dc445cd008be6633d23f819ea6c40bff158f8fbefc9cd79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="userPoolId")
    def user_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userPoolId"))

    @user_pool_id.setter
    def user_pool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fcc2a734ad6e91c1e066fe7e295abc98c1e0a831b487e8eea3c660f31461dce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userPoolId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElasticsearchDomainCognitoOptions]:
        return typing.cast(typing.Optional[ElasticsearchDomainCognitoOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElasticsearchDomainCognitoOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e032b8a6ee3801241e78112b5bcde5c51f6f3b68040985a0ee226302e1ffd71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomainConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "domain_name": "domainName",
        "access_policies": "accessPolicies",
        "advanced_options": "advancedOptions",
        "advanced_security_options": "advancedSecurityOptions",
        "auto_tune_options": "autoTuneOptions",
        "cluster_config": "clusterConfig",
        "cognito_options": "cognitoOptions",
        "domain_endpoint_options": "domainEndpointOptions",
        "ebs_options": "ebsOptions",
        "elasticsearch_version": "elasticsearchVersion",
        "encrypt_at_rest": "encryptAtRest",
        "id": "id",
        "log_publishing_options": "logPublishingOptions",
        "node_to_node_encryption": "nodeToNodeEncryption",
        "snapshot_options": "snapshotOptions",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
        "vpc_options": "vpcOptions",
    },
)
class ElasticsearchDomainConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        domain_name: builtins.str,
        access_policies: typing.Optional[builtins.str] = None,
        advanced_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        advanced_security_options: typing.Optional[typing.Union[ElasticsearchDomainAdvancedSecurityOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        auto_tune_options: typing.Optional[typing.Union[ElasticsearchDomainAutoTuneOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_config: typing.Optional[typing.Union[ElasticsearchDomainClusterConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        cognito_options: typing.Optional[typing.Union[ElasticsearchDomainCognitoOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        domain_endpoint_options: typing.Optional[typing.Union["ElasticsearchDomainDomainEndpointOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        ebs_options: typing.Optional[typing.Union["ElasticsearchDomainEbsOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        elasticsearch_version: typing.Optional[builtins.str] = None,
        encrypt_at_rest: typing.Optional[typing.Union["ElasticsearchDomainEncryptAtRest", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        log_publishing_options: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ElasticsearchDomainLogPublishingOptions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        node_to_node_encryption: typing.Optional[typing.Union["ElasticsearchDomainNodeToNodeEncryption", typing.Dict[builtins.str, typing.Any]]] = None,
        snapshot_options: typing.Optional[typing.Union["ElasticsearchDomainSnapshotOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ElasticsearchDomainTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc_options: typing.Optional[typing.Union["ElasticsearchDomainVpcOptions", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#domain_name ElasticsearchDomain#domain_name}.
        :param access_policies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#access_policies ElasticsearchDomain#access_policies}.
        :param advanced_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#advanced_options ElasticsearchDomain#advanced_options}.
        :param advanced_security_options: advanced_security_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#advanced_security_options ElasticsearchDomain#advanced_security_options}
        :param auto_tune_options: auto_tune_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#auto_tune_options ElasticsearchDomain#auto_tune_options}
        :param cluster_config: cluster_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#cluster_config ElasticsearchDomain#cluster_config}
        :param cognito_options: cognito_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#cognito_options ElasticsearchDomain#cognito_options}
        :param domain_endpoint_options: domain_endpoint_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#domain_endpoint_options ElasticsearchDomain#domain_endpoint_options}
        :param ebs_options: ebs_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#ebs_options ElasticsearchDomain#ebs_options}
        :param elasticsearch_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#elasticsearch_version ElasticsearchDomain#elasticsearch_version}.
        :param encrypt_at_rest: encrypt_at_rest block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#encrypt_at_rest ElasticsearchDomain#encrypt_at_rest}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#id ElasticsearchDomain#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param log_publishing_options: log_publishing_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#log_publishing_options ElasticsearchDomain#log_publishing_options}
        :param node_to_node_encryption: node_to_node_encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#node_to_node_encryption ElasticsearchDomain#node_to_node_encryption}
        :param snapshot_options: snapshot_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#snapshot_options ElasticsearchDomain#snapshot_options}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#tags ElasticsearchDomain#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#tags_all ElasticsearchDomain#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#timeouts ElasticsearchDomain#timeouts}
        :param vpc_options: vpc_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#vpc_options ElasticsearchDomain#vpc_options}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(advanced_security_options, dict):
            advanced_security_options = ElasticsearchDomainAdvancedSecurityOptions(**advanced_security_options)
        if isinstance(auto_tune_options, dict):
            auto_tune_options = ElasticsearchDomainAutoTuneOptions(**auto_tune_options)
        if isinstance(cluster_config, dict):
            cluster_config = ElasticsearchDomainClusterConfig(**cluster_config)
        if isinstance(cognito_options, dict):
            cognito_options = ElasticsearchDomainCognitoOptions(**cognito_options)
        if isinstance(domain_endpoint_options, dict):
            domain_endpoint_options = ElasticsearchDomainDomainEndpointOptions(**domain_endpoint_options)
        if isinstance(ebs_options, dict):
            ebs_options = ElasticsearchDomainEbsOptions(**ebs_options)
        if isinstance(encrypt_at_rest, dict):
            encrypt_at_rest = ElasticsearchDomainEncryptAtRest(**encrypt_at_rest)
        if isinstance(node_to_node_encryption, dict):
            node_to_node_encryption = ElasticsearchDomainNodeToNodeEncryption(**node_to_node_encryption)
        if isinstance(snapshot_options, dict):
            snapshot_options = ElasticsearchDomainSnapshotOptions(**snapshot_options)
        if isinstance(timeouts, dict):
            timeouts = ElasticsearchDomainTimeouts(**timeouts)
        if isinstance(vpc_options, dict):
            vpc_options = ElasticsearchDomainVpcOptions(**vpc_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dac3d7f8dff11ce33c42b036c9827ed50f72569fb7c98c9e5857f12499794042)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument access_policies", value=access_policies, expected_type=type_hints["access_policies"])
            check_type(argname="argument advanced_options", value=advanced_options, expected_type=type_hints["advanced_options"])
            check_type(argname="argument advanced_security_options", value=advanced_security_options, expected_type=type_hints["advanced_security_options"])
            check_type(argname="argument auto_tune_options", value=auto_tune_options, expected_type=type_hints["auto_tune_options"])
            check_type(argname="argument cluster_config", value=cluster_config, expected_type=type_hints["cluster_config"])
            check_type(argname="argument cognito_options", value=cognito_options, expected_type=type_hints["cognito_options"])
            check_type(argname="argument domain_endpoint_options", value=domain_endpoint_options, expected_type=type_hints["domain_endpoint_options"])
            check_type(argname="argument ebs_options", value=ebs_options, expected_type=type_hints["ebs_options"])
            check_type(argname="argument elasticsearch_version", value=elasticsearch_version, expected_type=type_hints["elasticsearch_version"])
            check_type(argname="argument encrypt_at_rest", value=encrypt_at_rest, expected_type=type_hints["encrypt_at_rest"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument log_publishing_options", value=log_publishing_options, expected_type=type_hints["log_publishing_options"])
            check_type(argname="argument node_to_node_encryption", value=node_to_node_encryption, expected_type=type_hints["node_to_node_encryption"])
            check_type(argname="argument snapshot_options", value=snapshot_options, expected_type=type_hints["snapshot_options"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument vpc_options", value=vpc_options, expected_type=type_hints["vpc_options"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_name": domain_name,
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
        if access_policies is not None:
            self._values["access_policies"] = access_policies
        if advanced_options is not None:
            self._values["advanced_options"] = advanced_options
        if advanced_security_options is not None:
            self._values["advanced_security_options"] = advanced_security_options
        if auto_tune_options is not None:
            self._values["auto_tune_options"] = auto_tune_options
        if cluster_config is not None:
            self._values["cluster_config"] = cluster_config
        if cognito_options is not None:
            self._values["cognito_options"] = cognito_options
        if domain_endpoint_options is not None:
            self._values["domain_endpoint_options"] = domain_endpoint_options
        if ebs_options is not None:
            self._values["ebs_options"] = ebs_options
        if elasticsearch_version is not None:
            self._values["elasticsearch_version"] = elasticsearch_version
        if encrypt_at_rest is not None:
            self._values["encrypt_at_rest"] = encrypt_at_rest
        if id is not None:
            self._values["id"] = id
        if log_publishing_options is not None:
            self._values["log_publishing_options"] = log_publishing_options
        if node_to_node_encryption is not None:
            self._values["node_to_node_encryption"] = node_to_node_encryption
        if snapshot_options is not None:
            self._values["snapshot_options"] = snapshot_options
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if vpc_options is not None:
            self._values["vpc_options"] = vpc_options

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
    def domain_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#domain_name ElasticsearchDomain#domain_name}.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_policies(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#access_policies ElasticsearchDomain#access_policies}.'''
        result = self._values.get("access_policies")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def advanced_options(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#advanced_options ElasticsearchDomain#advanced_options}.'''
        result = self._values.get("advanced_options")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def advanced_security_options(
        self,
    ) -> typing.Optional[ElasticsearchDomainAdvancedSecurityOptions]:
        '''advanced_security_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#advanced_security_options ElasticsearchDomain#advanced_security_options}
        '''
        result = self._values.get("advanced_security_options")
        return typing.cast(typing.Optional[ElasticsearchDomainAdvancedSecurityOptions], result)

    @builtins.property
    def auto_tune_options(self) -> typing.Optional[ElasticsearchDomainAutoTuneOptions]:
        '''auto_tune_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#auto_tune_options ElasticsearchDomain#auto_tune_options}
        '''
        result = self._values.get("auto_tune_options")
        return typing.cast(typing.Optional[ElasticsearchDomainAutoTuneOptions], result)

    @builtins.property
    def cluster_config(self) -> typing.Optional[ElasticsearchDomainClusterConfig]:
        '''cluster_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#cluster_config ElasticsearchDomain#cluster_config}
        '''
        result = self._values.get("cluster_config")
        return typing.cast(typing.Optional[ElasticsearchDomainClusterConfig], result)

    @builtins.property
    def cognito_options(self) -> typing.Optional[ElasticsearchDomainCognitoOptions]:
        '''cognito_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#cognito_options ElasticsearchDomain#cognito_options}
        '''
        result = self._values.get("cognito_options")
        return typing.cast(typing.Optional[ElasticsearchDomainCognitoOptions], result)

    @builtins.property
    def domain_endpoint_options(
        self,
    ) -> typing.Optional["ElasticsearchDomainDomainEndpointOptions"]:
        '''domain_endpoint_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#domain_endpoint_options ElasticsearchDomain#domain_endpoint_options}
        '''
        result = self._values.get("domain_endpoint_options")
        return typing.cast(typing.Optional["ElasticsearchDomainDomainEndpointOptions"], result)

    @builtins.property
    def ebs_options(self) -> typing.Optional["ElasticsearchDomainEbsOptions"]:
        '''ebs_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#ebs_options ElasticsearchDomain#ebs_options}
        '''
        result = self._values.get("ebs_options")
        return typing.cast(typing.Optional["ElasticsearchDomainEbsOptions"], result)

    @builtins.property
    def elasticsearch_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#elasticsearch_version ElasticsearchDomain#elasticsearch_version}.'''
        result = self._values.get("elasticsearch_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encrypt_at_rest(self) -> typing.Optional["ElasticsearchDomainEncryptAtRest"]:
        '''encrypt_at_rest block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#encrypt_at_rest ElasticsearchDomain#encrypt_at_rest}
        '''
        result = self._values.get("encrypt_at_rest")
        return typing.cast(typing.Optional["ElasticsearchDomainEncryptAtRest"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#id ElasticsearchDomain#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_publishing_options(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ElasticsearchDomainLogPublishingOptions"]]]:
        '''log_publishing_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#log_publishing_options ElasticsearchDomain#log_publishing_options}
        '''
        result = self._values.get("log_publishing_options")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ElasticsearchDomainLogPublishingOptions"]]], result)

    @builtins.property
    def node_to_node_encryption(
        self,
    ) -> typing.Optional["ElasticsearchDomainNodeToNodeEncryption"]:
        '''node_to_node_encryption block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#node_to_node_encryption ElasticsearchDomain#node_to_node_encryption}
        '''
        result = self._values.get("node_to_node_encryption")
        return typing.cast(typing.Optional["ElasticsearchDomainNodeToNodeEncryption"], result)

    @builtins.property
    def snapshot_options(self) -> typing.Optional["ElasticsearchDomainSnapshotOptions"]:
        '''snapshot_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#snapshot_options ElasticsearchDomain#snapshot_options}
        '''
        result = self._values.get("snapshot_options")
        return typing.cast(typing.Optional["ElasticsearchDomainSnapshotOptions"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#tags ElasticsearchDomain#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#tags_all ElasticsearchDomain#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ElasticsearchDomainTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#timeouts ElasticsearchDomain#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ElasticsearchDomainTimeouts"], result)

    @builtins.property
    def vpc_options(self) -> typing.Optional["ElasticsearchDomainVpcOptions"]:
        '''vpc_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#vpc_options ElasticsearchDomain#vpc_options}
        '''
        result = self._values.get("vpc_options")
        return typing.cast(typing.Optional["ElasticsearchDomainVpcOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomainDomainEndpointOptions",
    jsii_struct_bases=[],
    name_mapping={
        "custom_endpoint": "customEndpoint",
        "custom_endpoint_certificate_arn": "customEndpointCertificateArn",
        "custom_endpoint_enabled": "customEndpointEnabled",
        "enforce_https": "enforceHttps",
        "tls_security_policy": "tlsSecurityPolicy",
    },
)
class ElasticsearchDomainDomainEndpointOptions:
    def __init__(
        self,
        *,
        custom_endpoint: typing.Optional[builtins.str] = None,
        custom_endpoint_certificate_arn: typing.Optional[builtins.str] = None,
        custom_endpoint_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enforce_https: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tls_security_policy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param custom_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#custom_endpoint ElasticsearchDomain#custom_endpoint}.
        :param custom_endpoint_certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#custom_endpoint_certificate_arn ElasticsearchDomain#custom_endpoint_certificate_arn}.
        :param custom_endpoint_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#custom_endpoint_enabled ElasticsearchDomain#custom_endpoint_enabled}.
        :param enforce_https: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enforce_https ElasticsearchDomain#enforce_https}.
        :param tls_security_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#tls_security_policy ElasticsearchDomain#tls_security_policy}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98c5eda916a697dc1f47d19df588fb41d70eb9f8500ea47d7d539696948f9a25)
            check_type(argname="argument custom_endpoint", value=custom_endpoint, expected_type=type_hints["custom_endpoint"])
            check_type(argname="argument custom_endpoint_certificate_arn", value=custom_endpoint_certificate_arn, expected_type=type_hints["custom_endpoint_certificate_arn"])
            check_type(argname="argument custom_endpoint_enabled", value=custom_endpoint_enabled, expected_type=type_hints["custom_endpoint_enabled"])
            check_type(argname="argument enforce_https", value=enforce_https, expected_type=type_hints["enforce_https"])
            check_type(argname="argument tls_security_policy", value=tls_security_policy, expected_type=type_hints["tls_security_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if custom_endpoint is not None:
            self._values["custom_endpoint"] = custom_endpoint
        if custom_endpoint_certificate_arn is not None:
            self._values["custom_endpoint_certificate_arn"] = custom_endpoint_certificate_arn
        if custom_endpoint_enabled is not None:
            self._values["custom_endpoint_enabled"] = custom_endpoint_enabled
        if enforce_https is not None:
            self._values["enforce_https"] = enforce_https
        if tls_security_policy is not None:
            self._values["tls_security_policy"] = tls_security_policy

    @builtins.property
    def custom_endpoint(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#custom_endpoint ElasticsearchDomain#custom_endpoint}.'''
        result = self._values.get("custom_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_endpoint_certificate_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#custom_endpoint_certificate_arn ElasticsearchDomain#custom_endpoint_certificate_arn}.'''
        result = self._values.get("custom_endpoint_certificate_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_endpoint_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#custom_endpoint_enabled ElasticsearchDomain#custom_endpoint_enabled}.'''
        result = self._values.get("custom_endpoint_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enforce_https(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enforce_https ElasticsearchDomain#enforce_https}.'''
        result = self._values.get("enforce_https")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def tls_security_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#tls_security_policy ElasticsearchDomain#tls_security_policy}.'''
        result = self._values.get("tls_security_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainDomainEndpointOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElasticsearchDomainDomainEndpointOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomainDomainEndpointOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a8eb64c2de8b9f1d847eaf63bbad5869ed18f854645157956659dd94c006a5c5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCustomEndpoint")
    def reset_custom_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomEndpoint", []))

    @jsii.member(jsii_name="resetCustomEndpointCertificateArn")
    def reset_custom_endpoint_certificate_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomEndpointCertificateArn", []))

    @jsii.member(jsii_name="resetCustomEndpointEnabled")
    def reset_custom_endpoint_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomEndpointEnabled", []))

    @jsii.member(jsii_name="resetEnforceHttps")
    def reset_enforce_https(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnforceHttps", []))

    @jsii.member(jsii_name="resetTlsSecurityPolicy")
    def reset_tls_security_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsSecurityPolicy", []))

    @builtins.property
    @jsii.member(jsii_name="customEndpointCertificateArnInput")
    def custom_endpoint_certificate_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customEndpointCertificateArnInput"))

    @builtins.property
    @jsii.member(jsii_name="customEndpointEnabledInput")
    def custom_endpoint_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "customEndpointEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="customEndpointInput")
    def custom_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="enforceHttpsInput")
    def enforce_https_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enforceHttpsInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsSecurityPolicyInput")
    def tls_security_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tlsSecurityPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="customEndpoint")
    def custom_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customEndpoint"))

    @custom_endpoint.setter
    def custom_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0247636f406b8b3be3c293347a5e623ea315c19d211bdec50f1982646db0949)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="customEndpointCertificateArn")
    def custom_endpoint_certificate_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customEndpointCertificateArn"))

    @custom_endpoint_certificate_arn.setter
    def custom_endpoint_certificate_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a18fb94a65eb46559cd7a302781cfd249d5443c1e02bea5787bff85a4d675659)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customEndpointCertificateArn", value)

    @builtins.property
    @jsii.member(jsii_name="customEndpointEnabled")
    def custom_endpoint_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "customEndpointEnabled"))

    @custom_endpoint_enabled.setter
    def custom_endpoint_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56554f6828d68425b01e0732ccdbfeaf6ea8af967be2fada0d5bacdb33374093)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customEndpointEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="enforceHttps")
    def enforce_https(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enforceHttps"))

    @enforce_https.setter
    def enforce_https(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__917ebffc5e2285e4a321409c6caa0d1d415954f39813c833238ff125b21e1e47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enforceHttps", value)

    @builtins.property
    @jsii.member(jsii_name="tlsSecurityPolicy")
    def tls_security_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsSecurityPolicy"))

    @tls_security_policy.setter
    def tls_security_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92f7d42e803935cd6b242c71b498807cd498e39e4df54f9fd8dd1645fd10c36b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsSecurityPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ElasticsearchDomainDomainEndpointOptions]:
        return typing.cast(typing.Optional[ElasticsearchDomainDomainEndpointOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElasticsearchDomainDomainEndpointOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac5d959bda80b472408c8cd8801df30187e3b1f6c741a11715a1e2a809154594)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomainEbsOptions",
    jsii_struct_bases=[],
    name_mapping={
        "ebs_enabled": "ebsEnabled",
        "iops": "iops",
        "throughput": "throughput",
        "volume_size": "volumeSize",
        "volume_type": "volumeType",
    },
)
class ElasticsearchDomainEbsOptions:
    def __init__(
        self,
        *,
        ebs_enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        iops: typing.Optional[jsii.Number] = None,
        throughput: typing.Optional[jsii.Number] = None,
        volume_size: typing.Optional[jsii.Number] = None,
        volume_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ebs_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#ebs_enabled ElasticsearchDomain#ebs_enabled}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#iops ElasticsearchDomain#iops}.
        :param throughput: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#throughput ElasticsearchDomain#throughput}.
        :param volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#volume_size ElasticsearchDomain#volume_size}.
        :param volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#volume_type ElasticsearchDomain#volume_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb5f06c4937a6d7c701258fe02d02299d5d57024866bbf40ffd418f3801478da)
            check_type(argname="argument ebs_enabled", value=ebs_enabled, expected_type=type_hints["ebs_enabled"])
            check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
            check_type(argname="argument throughput", value=throughput, expected_type=type_hints["throughput"])
            check_type(argname="argument volume_size", value=volume_size, expected_type=type_hints["volume_size"])
            check_type(argname="argument volume_type", value=volume_type, expected_type=type_hints["volume_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ebs_enabled": ebs_enabled,
        }
        if iops is not None:
            self._values["iops"] = iops
        if throughput is not None:
            self._values["throughput"] = throughput
        if volume_size is not None:
            self._values["volume_size"] = volume_size
        if volume_type is not None:
            self._values["volume_type"] = volume_type

    @builtins.property
    def ebs_enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#ebs_enabled ElasticsearchDomain#ebs_enabled}.'''
        result = self._values.get("ebs_enabled")
        assert result is not None, "Required property 'ebs_enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#iops ElasticsearchDomain#iops}.'''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def throughput(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#throughput ElasticsearchDomain#throughput}.'''
        result = self._values.get("throughput")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volume_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#volume_size ElasticsearchDomain#volume_size}.'''
        result = self._values.get("volume_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volume_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#volume_type ElasticsearchDomain#volume_type}.'''
        result = self._values.get("volume_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainEbsOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElasticsearchDomainEbsOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomainEbsOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0e8133e77704a8b7e55825a928bf2b57baee48fb9c2903be05893c01b65e526a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIops")
    def reset_iops(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIops", []))

    @jsii.member(jsii_name="resetThroughput")
    def reset_throughput(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThroughput", []))

    @jsii.member(jsii_name="resetVolumeSize")
    def reset_volume_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeSize", []))

    @jsii.member(jsii_name="resetVolumeType")
    def reset_volume_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeType", []))

    @builtins.property
    @jsii.member(jsii_name="ebsEnabledInput")
    def ebs_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "ebsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="iopsInput")
    def iops_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "iopsInput"))

    @builtins.property
    @jsii.member(jsii_name="throughputInput")
    def throughput_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "throughputInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeSizeInput")
    def volume_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "volumeSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeTypeInput")
    def volume_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsEnabled")
    def ebs_enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "ebsEnabled"))

    @ebs_enabled.setter
    def ebs_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62482df289d79da24c19c8a540cb57dfe0339aa32c3ccd18fcf2287b533b05ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="iops")
    def iops(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iops"))

    @iops.setter
    def iops(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1c66443b4fe689fe86e228e07ce16436626045ba839bb6b84a8d32868bea76f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iops", value)

    @builtins.property
    @jsii.member(jsii_name="throughput")
    def throughput(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "throughput"))

    @throughput.setter
    def throughput(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77cee7dd30c7d7288dc0fda41f1bbe7ec90b1ddca032816e230d74fe95b0fc6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "throughput", value)

    @builtins.property
    @jsii.member(jsii_name="volumeSize")
    def volume_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "volumeSize"))

    @volume_size.setter
    def volume_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__341f0e36f9025e21eeb8906c4d9bf49c10ab0fac1368b64bb59cea1332248ed5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeSize", value)

    @builtins.property
    @jsii.member(jsii_name="volumeType")
    def volume_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeType"))

    @volume_type.setter
    def volume_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56c6a5e4eddb07ffeb95079d132cc6fdd497cf8f7276d63c9dc52cc2ed1ce3bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElasticsearchDomainEbsOptions]:
        return typing.cast(typing.Optional[ElasticsearchDomainEbsOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElasticsearchDomainEbsOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ba7748b07b7297922470e1a897fd43ca4e4b2a47152dc59e9364dfa87391076)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomainEncryptAtRest",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "kms_key_id": "kmsKeyId"},
)
class ElasticsearchDomainEncryptAtRest:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        kms_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enabled ElasticsearchDomain#enabled}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#kms_key_id ElasticsearchDomain#kms_key_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cfab4306cd782ea53131e62333d1a504c7420e9fb97c5899b64e900987446a1)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled": enabled,
        }
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enabled ElasticsearchDomain#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#kms_key_id ElasticsearchDomain#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainEncryptAtRest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElasticsearchDomainEncryptAtRestOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomainEncryptAtRestOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__92d0a20c4abf9fea7290c7592883f681364bfcd1603bafc0d5e79c4498580ec8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKmsKeyId")
    def reset_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyId", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdInput")
    def kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__3aa657c7c5ff1e36d79e356e0bfc9acfe582a1cdeb746eb6844380d70afd74c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e04ab44b3162e8496171b908a7b9b9b4d7279a74419e881f32a6a25f453834fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElasticsearchDomainEncryptAtRest]:
        return typing.cast(typing.Optional[ElasticsearchDomainEncryptAtRest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElasticsearchDomainEncryptAtRest],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bdbec06005fb08b55ad90c2a78e774806c555993a8a567f1fdb06f9de55d5d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomainLogPublishingOptions",
    jsii_struct_bases=[],
    name_mapping={
        "cloudwatch_log_group_arn": "cloudwatchLogGroupArn",
        "log_type": "logType",
        "enabled": "enabled",
    },
)
class ElasticsearchDomainLogPublishingOptions:
    def __init__(
        self,
        *,
        cloudwatch_log_group_arn: builtins.str,
        log_type: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param cloudwatch_log_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#cloudwatch_log_group_arn ElasticsearchDomain#cloudwatch_log_group_arn}.
        :param log_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#log_type ElasticsearchDomain#log_type}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enabled ElasticsearchDomain#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0585db9221b7a257ffd12574bbb934f3596b4ae9ec03470fa84f775fca5ca77e)
            check_type(argname="argument cloudwatch_log_group_arn", value=cloudwatch_log_group_arn, expected_type=type_hints["cloudwatch_log_group_arn"])
            check_type(argname="argument log_type", value=log_type, expected_type=type_hints["log_type"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cloudwatch_log_group_arn": cloudwatch_log_group_arn,
            "log_type": log_type,
        }
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def cloudwatch_log_group_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#cloudwatch_log_group_arn ElasticsearchDomain#cloudwatch_log_group_arn}.'''
        result = self._values.get("cloudwatch_log_group_arn")
        assert result is not None, "Required property 'cloudwatch_log_group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#log_type ElasticsearchDomain#log_type}.'''
        result = self._values.get("log_type")
        assert result is not None, "Required property 'log_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enabled ElasticsearchDomain#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainLogPublishingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElasticsearchDomainLogPublishingOptionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomainLogPublishingOptionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9e8f004f8610f2f9abee81724d7d70c4fdf86fb71f3584fe3967e18512ddc979)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ElasticsearchDomainLogPublishingOptionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e66cf60568cd1b95c0f0459eaed338ce2ccf23f804eb7d14d100905be4e52955)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElasticsearchDomainLogPublishingOptionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__975e8b8b731546498218f00b8efeb07b9f52d651a881c741f8e8b60fd83c9e1e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__945a021205fdbf969290f9b6b53e03930f0c2c28b3a8fc0f3b479be139730329)
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
            type_hints = typing.get_type_hints(_typecheckingstub__12c61937dc9aa6f0d7a95c5c7438f0809793034204d55d8fef5fbbff3a895cbe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ElasticsearchDomainLogPublishingOptions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ElasticsearchDomainLogPublishingOptions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ElasticsearchDomainLogPublishingOptions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79882e959881311e7134ab90c2549936c6255d084d65db66dc57c27be193b87b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElasticsearchDomainLogPublishingOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomainLogPublishingOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__86d02c6450c5886225e5d2a58c370c2b8c3774912b6bff509893e64fc17a1aa6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogGroupArnInput")
    def cloudwatch_log_group_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudwatchLogGroupArnInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="logTypeInput")
    def log_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogGroupArn")
    def cloudwatch_log_group_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudwatchLogGroupArn"))

    @cloudwatch_log_group_arn.setter
    def cloudwatch_log_group_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77f60620b7a05454f92c4a388137cfde4eb13b1526f7121e9d2327384ff38748)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudwatchLogGroupArn", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__bfb4e290cb94c5cf7fc1946172b10c6749d00f99d910911d4f99dc5af01b5af1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="logType")
    def log_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logType"))

    @log_type.setter
    def log_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e226f4801db980310d55765a43963e212cc0196fe80e75c1ac0d9f150060bdf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElasticsearchDomainLogPublishingOptions, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElasticsearchDomainLogPublishingOptions, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElasticsearchDomainLogPublishingOptions, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da5084112e225495a28bce1a6deae989f5cab8c30bd84caf9fceda68f79193fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomainNodeToNodeEncryption",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class ElasticsearchDomainNodeToNodeEncryption:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enabled ElasticsearchDomain#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__186a00dd67441f02902b6c6bcb7845768802907c72f39e360a47eff97bff0a22)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled": enabled,
        }

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#enabled ElasticsearchDomain#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainNodeToNodeEncryption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElasticsearchDomainNodeToNodeEncryptionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomainNodeToNodeEncryptionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__911e9937d7ff3ebffb7f15fa49bccb695c8e8979cf12d092d9b6e13f772cae17)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

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
            type_hints = typing.get_type_hints(_typecheckingstub__545ce88fc1331a3f63f36a51974147c48e9d8848f177146122cfd4a918e2ee27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ElasticsearchDomainNodeToNodeEncryption]:
        return typing.cast(typing.Optional[ElasticsearchDomainNodeToNodeEncryption], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElasticsearchDomainNodeToNodeEncryption],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80768906faf1bfdc90d0ef962ec5186d03f38072b314ab0d5cafe5dccaa81cae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomainSnapshotOptions",
    jsii_struct_bases=[],
    name_mapping={"automated_snapshot_start_hour": "automatedSnapshotStartHour"},
)
class ElasticsearchDomainSnapshotOptions:
    def __init__(self, *, automated_snapshot_start_hour: jsii.Number) -> None:
        '''
        :param automated_snapshot_start_hour: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#automated_snapshot_start_hour ElasticsearchDomain#automated_snapshot_start_hour}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfde57cbb4d1b3fe9d144b9e5eb173dd52d676cdadb3b679e40f784a722d1181)
            check_type(argname="argument automated_snapshot_start_hour", value=automated_snapshot_start_hour, expected_type=type_hints["automated_snapshot_start_hour"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "automated_snapshot_start_hour": automated_snapshot_start_hour,
        }

    @builtins.property
    def automated_snapshot_start_hour(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#automated_snapshot_start_hour ElasticsearchDomain#automated_snapshot_start_hour}.'''
        result = self._values.get("automated_snapshot_start_hour")
        assert result is not None, "Required property 'automated_snapshot_start_hour' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainSnapshotOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElasticsearchDomainSnapshotOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomainSnapshotOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a444d6a0e8c6bc35f60fcdb8d2cca5a5f36e3eae18e848a3537cf21a65af49cb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="automatedSnapshotStartHourInput")
    def automated_snapshot_start_hour_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "automatedSnapshotStartHourInput"))

    @builtins.property
    @jsii.member(jsii_name="automatedSnapshotStartHour")
    def automated_snapshot_start_hour(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "automatedSnapshotStartHour"))

    @automated_snapshot_start_hour.setter
    def automated_snapshot_start_hour(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa7b4ab8b69e230f0185dfe793ec6d4c9da41cfb7e57afbdd67c797d89eb01eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "automatedSnapshotStartHour", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElasticsearchDomainSnapshotOptions]:
        return typing.cast(typing.Optional[ElasticsearchDomainSnapshotOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElasticsearchDomainSnapshotOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d536abf0614dc5d3838bc69b4d1db82cbcb83877230b23654c9eda2b3da4e013)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomainTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class ElasticsearchDomainTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#create ElasticsearchDomain#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#delete ElasticsearchDomain#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#update ElasticsearchDomain#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__314af1e3a61028744ff69ac9394e4cf26596724bdce69866f47111c0b2bc8520)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#create ElasticsearchDomain#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#delete ElasticsearchDomain#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#update ElasticsearchDomain#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElasticsearchDomainTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomainTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d8aed186a35fb020f0d7ce1ec00f47367e0af14fed97d421fd5c010866d102c7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d651b455f58e02cbe59f75a56d5ad94e2ed4d8be824c898c1717766bd92372fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dc0e5997eb9ebc093aad51cdcd4c80a69745f762b8d8e026bdb812411d93e08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00bc6f770d0321baecdd443c5d676c664f21ea623325dc6e662a238df7959936)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElasticsearchDomainTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElasticsearchDomainTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElasticsearchDomainTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e837698436e3543d28d2d4f8c2ab71e4964cf71ec272a40c7354576544c3885)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomainVpcOptions",
    jsii_struct_bases=[],
    name_mapping={"security_group_ids": "securityGroupIds", "subnet_ids": "subnetIds"},
)
class ElasticsearchDomainVpcOptions:
    def __init__(
        self,
        *,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#security_group_ids ElasticsearchDomain#security_group_ids}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#subnet_ids ElasticsearchDomain#subnet_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2434a2810f83ca81c6e2ed550d6fbabf6b8875fa5b8c9989477a2a153010e079)
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if subnet_ids is not None:
            self._values["subnet_ids"] = subnet_ids

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#security_group_ids ElasticsearchDomain#security_group_ids}.'''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain#subnet_ids ElasticsearchDomain#subnet_ids}.'''
        result = self._values.get("subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDomainVpcOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElasticsearchDomainVpcOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.elasticsearchDomain.ElasticsearchDomainVpcOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e1f780f230de07cf2f343560c02e4d2d2b8615d245aef0ff2bc75a83483aeee7)
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
    @jsii.member(jsii_name="availabilityZones")
    def availability_zones(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "availabilityZones"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__f83bde1f46946f43e89e6977dd8b328408068f6d22f378362f2453f32e73a174)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3710203880c8480551584a4cd95474ca19b602d1bbdeb4bcd4a9b18f9f5f5ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElasticsearchDomainVpcOptions]:
        return typing.cast(typing.Optional[ElasticsearchDomainVpcOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElasticsearchDomainVpcOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b969fa4344747f1e9d7e21c02605e8e543d0b75fa6cf4f83b86026ecd5ac521)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ElasticsearchDomain",
    "ElasticsearchDomainAdvancedSecurityOptions",
    "ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptions",
    "ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptionsOutputReference",
    "ElasticsearchDomainAdvancedSecurityOptionsOutputReference",
    "ElasticsearchDomainAutoTuneOptions",
    "ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule",
    "ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration",
    "ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDurationOutputReference",
    "ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleList",
    "ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleOutputReference",
    "ElasticsearchDomainAutoTuneOptionsOutputReference",
    "ElasticsearchDomainClusterConfig",
    "ElasticsearchDomainClusterConfigColdStorageOptions",
    "ElasticsearchDomainClusterConfigColdStorageOptionsOutputReference",
    "ElasticsearchDomainClusterConfigOutputReference",
    "ElasticsearchDomainClusterConfigZoneAwarenessConfig",
    "ElasticsearchDomainClusterConfigZoneAwarenessConfigOutputReference",
    "ElasticsearchDomainCognitoOptions",
    "ElasticsearchDomainCognitoOptionsOutputReference",
    "ElasticsearchDomainConfig",
    "ElasticsearchDomainDomainEndpointOptions",
    "ElasticsearchDomainDomainEndpointOptionsOutputReference",
    "ElasticsearchDomainEbsOptions",
    "ElasticsearchDomainEbsOptionsOutputReference",
    "ElasticsearchDomainEncryptAtRest",
    "ElasticsearchDomainEncryptAtRestOutputReference",
    "ElasticsearchDomainLogPublishingOptions",
    "ElasticsearchDomainLogPublishingOptionsList",
    "ElasticsearchDomainLogPublishingOptionsOutputReference",
    "ElasticsearchDomainNodeToNodeEncryption",
    "ElasticsearchDomainNodeToNodeEncryptionOutputReference",
    "ElasticsearchDomainSnapshotOptions",
    "ElasticsearchDomainSnapshotOptionsOutputReference",
    "ElasticsearchDomainTimeouts",
    "ElasticsearchDomainTimeoutsOutputReference",
    "ElasticsearchDomainVpcOptions",
    "ElasticsearchDomainVpcOptionsOutputReference",
]

publication.publish()

def _typecheckingstub__1d3da97f09d31cab3a80d4bf0d53ce6752c3a66bd3db00bcccde2f5c289f69f9(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    domain_name: builtins.str,
    access_policies: typing.Optional[builtins.str] = None,
    advanced_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    advanced_security_options: typing.Optional[typing.Union[ElasticsearchDomainAdvancedSecurityOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    auto_tune_options: typing.Optional[typing.Union[ElasticsearchDomainAutoTuneOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    cluster_config: typing.Optional[typing.Union[ElasticsearchDomainClusterConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    cognito_options: typing.Optional[typing.Union[ElasticsearchDomainCognitoOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    domain_endpoint_options: typing.Optional[typing.Union[ElasticsearchDomainDomainEndpointOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    ebs_options: typing.Optional[typing.Union[ElasticsearchDomainEbsOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    elasticsearch_version: typing.Optional[builtins.str] = None,
    encrypt_at_rest: typing.Optional[typing.Union[ElasticsearchDomainEncryptAtRest, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    log_publishing_options: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ElasticsearchDomainLogPublishingOptions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    node_to_node_encryption: typing.Optional[typing.Union[ElasticsearchDomainNodeToNodeEncryption, typing.Dict[builtins.str, typing.Any]]] = None,
    snapshot_options: typing.Optional[typing.Union[ElasticsearchDomainSnapshotOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[ElasticsearchDomainTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc_options: typing.Optional[typing.Union[ElasticsearchDomainVpcOptions, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__255cc620afffd72ac20dbe063f316b3ee2f9c50f174ca8d8f20bff9143cb30f5(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ElasticsearchDomainLogPublishingOptions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00fa3763d84412ba94ee632a8eef8ea0c775a937f9148893d8ec82bd511761ac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aae4291790bbc230744e7c4a1e4305ca6928b8778c4c55cdb2b14725689ac3bc(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__585206f93b9284a2dbf322ac6dbe7004fce5b92fc891de42694f464f9ab9891f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfe5226151713328155dff362e32499b4c2542d53862da13accfee5bb6ec3157(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3bca2bbe32b9046aca1af278c9cbc0b8280c10a046e41a2a10955b1c7e40f31(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9722096c981f240e78f2cbaf17f8e8b99bf84325a9d2ae203d7a61fccda372ff(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78244a80a4ae44052048db28acf1a5607663340e154d6471a0b0edec3a264889(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76174cdd3234959d6752fe751ddcdf8e7d3ca10594354d1e6c5f34c27f8e1202(
    *,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    internal_user_database_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    master_user_options: typing.Optional[typing.Union[ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptions, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff024a8e397e688677a55ce8b7029c85b729f6fa7f0cd3b82db401f5ff87026e(
    *,
    master_user_arn: typing.Optional[builtins.str] = None,
    master_user_name: typing.Optional[builtins.str] = None,
    master_user_password: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd28188f5f9e09658b9ea7c3ce57de02c873bd0f8ceeac7a322120548c934a9f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__685195492bce25b8a88afd4fca03ed478b297d7a27c433de7f747bd32ac03e00(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76aabdaba7c690f2326af4a2c518fb7eb5ef6f05185008dc001e35f5716e4b18(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7562effacc6009e685ddd3802cd691f77227fce3bab07a75121dadf03ce7c3c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee8a5bd5290f29a5cba7983ca3ed0ee79f1412c9af1b98efe9815032a2b27998(
    value: typing.Optional[ElasticsearchDomainAdvancedSecurityOptionsMasterUserOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eebe9fe6b1fc85ba55e174a63e6acbab96f9ef8031ae7056595c751bd523d80c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddc2c9fffbe7e55f7706d7794714b9f041bf2fe71b8aa4cf2bc073dbae41025d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dc3f0f8ab9813c6a467c68a8c1d6e73a85e6535bbcee7dcefae5d55c290a0d4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6b5714de15c286cd29338994d29d3caa786365c36bfb71d40b2c4f7338f1bf8(
    value: typing.Optional[ElasticsearchDomainAdvancedSecurityOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a53f816fcb52385c3ac2f33f0b98238df1c607f3bbf77af26e386bbda00acc6b(
    *,
    desired_state: builtins.str,
    maintenance_schedule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule, typing.Dict[builtins.str, typing.Any]]]]] = None,
    rollback_on_disable: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e356f742a4fa462b72e44fe9506472f535cfaced003c8dbce0a6675df39c1c32(
    *,
    cron_expression_for_recurrence: builtins.str,
    duration: typing.Union[ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration, typing.Dict[builtins.str, typing.Any]],
    start_at: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ee6cb8696144b94768717236eba268ac5761fe8e98a482472dd5020cb484669(
    *,
    unit: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a516a5473b1fd2e45452a5019a15d3a9e6617de4b0bffe0de4d17b599605693(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__476014720408fb784c63fd6f2167965ead8135ccdaa059027ebc89a08798e9c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64f321a53a920c0382a809e498262c04786f82d5cd7313b8b49bbde9feb0d8c5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__850de46e583db188c3d8777103bbc9c8a180427d4929fd78fc5e770dc33a445b(
    value: typing.Optional[ElasticsearchDomainAutoTuneOptionsMaintenanceScheduleDuration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ece35779c6c1784d2d922f90f11555f8decce8d66ff7f4aacc9ab5be7fc9d8b6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfd62e791633c8d71e7dda56866a409f35a213f1ffe0e5334b35e6812eec21cf(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__843d936aec7e40d93356a5cfc10ff378ac32698371dc2a36a01e3c76c34756e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21d5707e2011dbd9884ff177b3ffded9babee4c8af609bec66383186936f18c5(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5be31a5a307513337c134efbb2579ea40f092e4b1c7cbcb4b8097cfdf52582ff(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf775c58e3fdf9ade89e338f44d511764c81d1f4dfe4aa51f536635725f7ebc3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca31677121bde88c89488a93b90a1201d7a1e7cabf663b656b1d2524bcf1e692(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b358a873ae6d932a9e9203cb0807333b82df7a91b07d6733ef59c4b65721d947(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__205edd25aa049b59fd03c27b2ed5ddef832aa18d7827bb860efee5c764e27532(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe77012b5554218047f4f8236c3c19545d29bd04a36039e75b3b988fa1e7d77b(
    value: typing.Optional[typing.Union[ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c198b6f3fda8961d53e1afbc92d50575329100fafa8da1575c6f9dde04ed5115(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b2e410285b8ed729204d30d63ff3d82f3be575e00174932f1e91bae4fa8201f(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ElasticsearchDomainAutoTuneOptionsMaintenanceSchedule, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbf39a80a28ff988d7f3ad019f2487f583c1e9f3a085fcac22127225075fc3df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e0260ff80363c3f99cc1e98c626c75f0c1537ebd3040803fc6a9610d5473a6b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d45a02b28b9bb71aa9ece4f8c9026abef5b7e59fe71465bdfdfbe93b029c444(
    value: typing.Optional[ElasticsearchDomainAutoTuneOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81c0a7acc3844745ac6ed302f61fa9d093c7a51fa25f17d651970dde0331c7a3(
    *,
    cold_storage_options: typing.Optional[typing.Union[ElasticsearchDomainClusterConfigColdStorageOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    dedicated_master_count: typing.Optional[jsii.Number] = None,
    dedicated_master_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    dedicated_master_type: typing.Optional[builtins.str] = None,
    instance_count: typing.Optional[jsii.Number] = None,
    instance_type: typing.Optional[builtins.str] = None,
    warm_count: typing.Optional[jsii.Number] = None,
    warm_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    warm_type: typing.Optional[builtins.str] = None,
    zone_awareness_config: typing.Optional[typing.Union[ElasticsearchDomainClusterConfigZoneAwarenessConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    zone_awareness_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__479d775c30bda984294d556f9abcce98f527241ec3c207e98048c3e1dff431e7(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26c20d73f5f847ddabea4892b92cd636d36a2ceab85df3c1bbf4149ffb6b0b73(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad348d90c6963a60891ffef745db65e8686fa9e96c6d40e0ec3c33fb9ee9e910(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edffec25ffd532006726e62bf6988d26e8f4e7b258726aef825d8f0c4b47bcaf(
    value: typing.Optional[ElasticsearchDomainClusterConfigColdStorageOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f3153beeeaba79f2e818b6024ff7eb8e29f99dc8bc6926debe0980c2bd65f7e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20c5c5757b8dba94544a9fe44bddc3cd7c311d96a72a38199bbbe38b6abcf680(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af44548e9560e1cd704963e2cdcb41444f72f9b6e05eb79fc21692e239de8c19(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__143efb348dcaf873c68adba9782af2c4a1af54c6ab4a2e6f289f212c2f4dbd3e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dda1326afb9746000331deb553e7d186aacf665c5c1fc7097e53b2a52a330c2e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__527c276d79a9f15bbebb71d987d6f3aced9b2681c5e5e9249638fcc558665ed9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8711a856553b3eebc3fdb9bc0a753ca0dc120eb5a7cfd50c30a6a548c3677c35(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac75e56da3ff5f98c22e56e014415871d74388cdd3874fd2562d55074ca382fe(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d64d192ec3b4fd1782a874675ed0ed2b89fd75ddbe761a18074a1e127ca5877(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac8d94cba14a59b227a36d4867b920cd9180eed8016778cff61b2c2fbab89778(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ff8519a781690a93a441f4acc801244dcc49e8d996cdcef70c76d6dc7ac1df2(
    value: typing.Optional[ElasticsearchDomainClusterConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__247050f0a0a9abef8e81213dbc8fd21f0c9a096af3379cf9546dc1c2f33a9483(
    *,
    availability_zone_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0808be7db6c351c3447489a31a87eb1931bddc5ffdf4a169c78f429b44334eea(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abd43063eaa20e48d0da22b18d1d40c16ee2d6e65489ca5e00e3166a76e1db61(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9584c9490291add30aea492364a9c71bfbdf13d6b2aea84d4d37ac80bf56e6b5(
    value: typing.Optional[ElasticsearchDomainClusterConfigZoneAwarenessConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52aadd6cce9caeb647841cb9198ab84b2610e694c9c6f2883bc6cab43cb06b87(
    *,
    identity_pool_id: builtins.str,
    role_arn: builtins.str,
    user_pool_id: builtins.str,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a15cf92c49c64df8ed4268743f6b479124521b70d41720a4dda6a54c1165258(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee81860aaffdffdcff57ff0729341e70959b44ad8ab4735931df860ccb04439f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dba75aa9e8dcaad27b88d5969c7347d38504923c653d289717f1ec94793a0e86(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98b0bb10148652611dc445cd008be6633d23f819ea6c40bff158f8fbefc9cd79(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fcc2a734ad6e91c1e066fe7e295abc98c1e0a831b487e8eea3c660f31461dce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e032b8a6ee3801241e78112b5bcde5c51f6f3b68040985a0ee226302e1ffd71(
    value: typing.Optional[ElasticsearchDomainCognitoOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dac3d7f8dff11ce33c42b036c9827ed50f72569fb7c98c9e5857f12499794042(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    domain_name: builtins.str,
    access_policies: typing.Optional[builtins.str] = None,
    advanced_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    advanced_security_options: typing.Optional[typing.Union[ElasticsearchDomainAdvancedSecurityOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    auto_tune_options: typing.Optional[typing.Union[ElasticsearchDomainAutoTuneOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    cluster_config: typing.Optional[typing.Union[ElasticsearchDomainClusterConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    cognito_options: typing.Optional[typing.Union[ElasticsearchDomainCognitoOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    domain_endpoint_options: typing.Optional[typing.Union[ElasticsearchDomainDomainEndpointOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    ebs_options: typing.Optional[typing.Union[ElasticsearchDomainEbsOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    elasticsearch_version: typing.Optional[builtins.str] = None,
    encrypt_at_rest: typing.Optional[typing.Union[ElasticsearchDomainEncryptAtRest, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    log_publishing_options: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ElasticsearchDomainLogPublishingOptions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    node_to_node_encryption: typing.Optional[typing.Union[ElasticsearchDomainNodeToNodeEncryption, typing.Dict[builtins.str, typing.Any]]] = None,
    snapshot_options: typing.Optional[typing.Union[ElasticsearchDomainSnapshotOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[ElasticsearchDomainTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc_options: typing.Optional[typing.Union[ElasticsearchDomainVpcOptions, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98c5eda916a697dc1f47d19df588fb41d70eb9f8500ea47d7d539696948f9a25(
    *,
    custom_endpoint: typing.Optional[builtins.str] = None,
    custom_endpoint_certificate_arn: typing.Optional[builtins.str] = None,
    custom_endpoint_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enforce_https: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tls_security_policy: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8eb64c2de8b9f1d847eaf63bbad5869ed18f854645157956659dd94c006a5c5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0247636f406b8b3be3c293347a5e623ea315c19d211bdec50f1982646db0949(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a18fb94a65eb46559cd7a302781cfd249d5443c1e02bea5787bff85a4d675659(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56554f6828d68425b01e0732ccdbfeaf6ea8af967be2fada0d5bacdb33374093(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__917ebffc5e2285e4a321409c6caa0d1d415954f39813c833238ff125b21e1e47(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92f7d42e803935cd6b242c71b498807cd498e39e4df54f9fd8dd1645fd10c36b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac5d959bda80b472408c8cd8801df30187e3b1f6c741a11715a1e2a809154594(
    value: typing.Optional[ElasticsearchDomainDomainEndpointOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb5f06c4937a6d7c701258fe02d02299d5d57024866bbf40ffd418f3801478da(
    *,
    ebs_enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    iops: typing.Optional[jsii.Number] = None,
    throughput: typing.Optional[jsii.Number] = None,
    volume_size: typing.Optional[jsii.Number] = None,
    volume_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e8133e77704a8b7e55825a928bf2b57baee48fb9c2903be05893c01b65e526a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62482df289d79da24c19c8a540cb57dfe0339aa32c3ccd18fcf2287b533b05ac(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1c66443b4fe689fe86e228e07ce16436626045ba839bb6b84a8d32868bea76f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77cee7dd30c7d7288dc0fda41f1bbe7ec90b1ddca032816e230d74fe95b0fc6a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__341f0e36f9025e21eeb8906c4d9bf49c10ab0fac1368b64bb59cea1332248ed5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56c6a5e4eddb07ffeb95079d132cc6fdd497cf8f7276d63c9dc52cc2ed1ce3bd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ba7748b07b7297922470e1a897fd43ca4e4b2a47152dc59e9364dfa87391076(
    value: typing.Optional[ElasticsearchDomainEbsOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cfab4306cd782ea53131e62333d1a504c7420e9fb97c5899b64e900987446a1(
    *,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    kms_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92d0a20c4abf9fea7290c7592883f681364bfcd1603bafc0d5e79c4498580ec8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3aa657c7c5ff1e36d79e356e0bfc9acfe582a1cdeb746eb6844380d70afd74c1(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e04ab44b3162e8496171b908a7b9b9b4d7279a74419e881f32a6a25f453834fd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bdbec06005fb08b55ad90c2a78e774806c555993a8a567f1fdb06f9de55d5d2(
    value: typing.Optional[ElasticsearchDomainEncryptAtRest],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0585db9221b7a257ffd12574bbb934f3596b4ae9ec03470fa84f775fca5ca77e(
    *,
    cloudwatch_log_group_arn: builtins.str,
    log_type: builtins.str,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e8f004f8610f2f9abee81724d7d70c4fdf86fb71f3584fe3967e18512ddc979(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e66cf60568cd1b95c0f0459eaed338ce2ccf23f804eb7d14d100905be4e52955(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__975e8b8b731546498218f00b8efeb07b9f52d651a881c741f8e8b60fd83c9e1e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__945a021205fdbf969290f9b6b53e03930f0c2c28b3a8fc0f3b479be139730329(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12c61937dc9aa6f0d7a95c5c7438f0809793034204d55d8fef5fbbff3a895cbe(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79882e959881311e7134ab90c2549936c6255d084d65db66dc57c27be193b87b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ElasticsearchDomainLogPublishingOptions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86d02c6450c5886225e5d2a58c370c2b8c3774912b6bff509893e64fc17a1aa6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77f60620b7a05454f92c4a388137cfde4eb13b1526f7121e9d2327384ff38748(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfb4e290cb94c5cf7fc1946172b10c6749d00f99d910911d4f99dc5af01b5af1(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e226f4801db980310d55765a43963e212cc0196fe80e75c1ac0d9f150060bdf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da5084112e225495a28bce1a6deae989f5cab8c30bd84caf9fceda68f79193fa(
    value: typing.Optional[typing.Union[ElasticsearchDomainLogPublishingOptions, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__186a00dd67441f02902b6c6bcb7845768802907c72f39e360a47eff97bff0a22(
    *,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__911e9937d7ff3ebffb7f15fa49bccb695c8e8979cf12d092d9b6e13f772cae17(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__545ce88fc1331a3f63f36a51974147c48e9d8848f177146122cfd4a918e2ee27(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80768906faf1bfdc90d0ef962ec5186d03f38072b314ab0d5cafe5dccaa81cae(
    value: typing.Optional[ElasticsearchDomainNodeToNodeEncryption],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfde57cbb4d1b3fe9d144b9e5eb173dd52d676cdadb3b679e40f784a722d1181(
    *,
    automated_snapshot_start_hour: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a444d6a0e8c6bc35f60fcdb8d2cca5a5f36e3eae18e848a3537cf21a65af49cb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa7b4ab8b69e230f0185dfe793ec6d4c9da41cfb7e57afbdd67c797d89eb01eb(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d536abf0614dc5d3838bc69b4d1db82cbcb83877230b23654c9eda2b3da4e013(
    value: typing.Optional[ElasticsearchDomainSnapshotOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__314af1e3a61028744ff69ac9394e4cf26596724bdce69866f47111c0b2bc8520(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8aed186a35fb020f0d7ce1ec00f47367e0af14fed97d421fd5c010866d102c7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d651b455f58e02cbe59f75a56d5ad94e2ed4d8be824c898c1717766bd92372fc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dc0e5997eb9ebc093aad51cdcd4c80a69745f762b8d8e026bdb812411d93e08(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00bc6f770d0321baecdd443c5d676c664f21ea623325dc6e662a238df7959936(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e837698436e3543d28d2d4f8c2ab71e4964cf71ec272a40c7354576544c3885(
    value: typing.Optional[typing.Union[ElasticsearchDomainTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2434a2810f83ca81c6e2ed550d6fbabf6b8875fa5b8c9989477a2a153010e079(
    *,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1f780f230de07cf2f343560c02e4d2d2b8615d245aef0ff2bc75a83483aeee7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f83bde1f46946f43e89e6977dd8b328408068f6d22f378362f2453f32e73a174(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3710203880c8480551584a4cd95474ca19b602d1bbdeb4bcd4a9b18f9f5f5ba(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b969fa4344747f1e9d7e21c02605e8e543d0b75fa6cf4f83b86026ecd5ac521(
    value: typing.Optional[ElasticsearchDomainVpcOptions],
) -> None:
    """Type checking stubs"""
    pass
