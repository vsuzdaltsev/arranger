'''
# `aws_opensearch_domain`

Refer to the Terraform Registory for docs: [`aws_opensearch_domain`](https://www.terraform.io/docs/providers/aws/r/opensearch_domain).
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


class OpensearchDomain(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opensearchDomain.OpensearchDomain",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain aws_opensearch_domain}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        domain_name: builtins.str,
        access_policies: typing.Optional[builtins.str] = None,
        advanced_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        advanced_security_options: typing.Optional[typing.Union["OpensearchDomainAdvancedSecurityOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        auto_tune_options: typing.Optional[typing.Union["OpensearchDomainAutoTuneOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_config: typing.Optional[typing.Union["OpensearchDomainClusterConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        cognito_options: typing.Optional[typing.Union["OpensearchDomainCognitoOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        domain_endpoint_options: typing.Optional[typing.Union["OpensearchDomainDomainEndpointOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        ebs_options: typing.Optional[typing.Union["OpensearchDomainEbsOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        encrypt_at_rest: typing.Optional[typing.Union["OpensearchDomainEncryptAtRest", typing.Dict[builtins.str, typing.Any]]] = None,
        engine_version: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        log_publishing_options: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["OpensearchDomainLogPublishingOptions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        node_to_node_encryption: typing.Optional[typing.Union["OpensearchDomainNodeToNodeEncryption", typing.Dict[builtins.str, typing.Any]]] = None,
        snapshot_options: typing.Optional[typing.Union["OpensearchDomainSnapshotOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["OpensearchDomainTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc_options: typing.Optional[typing.Union["OpensearchDomainVpcOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain aws_opensearch_domain} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#domain_name OpensearchDomain#domain_name}.
        :param access_policies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#access_policies OpensearchDomain#access_policies}.
        :param advanced_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#advanced_options OpensearchDomain#advanced_options}.
        :param advanced_security_options: advanced_security_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#advanced_security_options OpensearchDomain#advanced_security_options}
        :param auto_tune_options: auto_tune_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#auto_tune_options OpensearchDomain#auto_tune_options}
        :param cluster_config: cluster_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#cluster_config OpensearchDomain#cluster_config}
        :param cognito_options: cognito_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#cognito_options OpensearchDomain#cognito_options}
        :param domain_endpoint_options: domain_endpoint_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#domain_endpoint_options OpensearchDomain#domain_endpoint_options}
        :param ebs_options: ebs_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#ebs_options OpensearchDomain#ebs_options}
        :param encrypt_at_rest: encrypt_at_rest block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#encrypt_at_rest OpensearchDomain#encrypt_at_rest}
        :param engine_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#engine_version OpensearchDomain#engine_version}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#id OpensearchDomain#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param log_publishing_options: log_publishing_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#log_publishing_options OpensearchDomain#log_publishing_options}
        :param node_to_node_encryption: node_to_node_encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#node_to_node_encryption OpensearchDomain#node_to_node_encryption}
        :param snapshot_options: snapshot_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#snapshot_options OpensearchDomain#snapshot_options}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#tags OpensearchDomain#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#tags_all OpensearchDomain#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#timeouts OpensearchDomain#timeouts}
        :param vpc_options: vpc_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#vpc_options OpensearchDomain#vpc_options}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3eec919b45d55b7ca41424513ec67823b95c9ffc69cff46ce5a033b162f2aee6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = OpensearchDomainConfig(
            domain_name=domain_name,
            access_policies=access_policies,
            advanced_options=advanced_options,
            advanced_security_options=advanced_security_options,
            auto_tune_options=auto_tune_options,
            cluster_config=cluster_config,
            cognito_options=cognito_options,
            domain_endpoint_options=domain_endpoint_options,
            ebs_options=ebs_options,
            encrypt_at_rest=encrypt_at_rest,
            engine_version=engine_version,
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
        anonymous_auth_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        internal_user_database_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        master_user_options: typing.Optional[typing.Union["OpensearchDomainAdvancedSecurityOptionsMasterUserOptions", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#enabled OpensearchDomain#enabled}.
        :param anonymous_auth_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#anonymous_auth_enabled OpensearchDomain#anonymous_auth_enabled}.
        :param internal_user_database_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#internal_user_database_enabled OpensearchDomain#internal_user_database_enabled}.
        :param master_user_options: master_user_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#master_user_options OpensearchDomain#master_user_options}
        '''
        value = OpensearchDomainAdvancedSecurityOptions(
            enabled=enabled,
            anonymous_auth_enabled=anonymous_auth_enabled,
            internal_user_database_enabled=internal_user_database_enabled,
            master_user_options=master_user_options,
        )

        return typing.cast(None, jsii.invoke(self, "putAdvancedSecurityOptions", [value]))

    @jsii.member(jsii_name="putAutoTuneOptions")
    def put_auto_tune_options(
        self,
        *,
        desired_state: builtins.str,
        maintenance_schedule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["OpensearchDomainAutoTuneOptionsMaintenanceSchedule", typing.Dict[builtins.str, typing.Any]]]]] = None,
        rollback_on_disable: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param desired_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#desired_state OpensearchDomain#desired_state}.
        :param maintenance_schedule: maintenance_schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#maintenance_schedule OpensearchDomain#maintenance_schedule}
        :param rollback_on_disable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#rollback_on_disable OpensearchDomain#rollback_on_disable}.
        '''
        value = OpensearchDomainAutoTuneOptions(
            desired_state=desired_state,
            maintenance_schedule=maintenance_schedule,
            rollback_on_disable=rollback_on_disable,
        )

        return typing.cast(None, jsii.invoke(self, "putAutoTuneOptions", [value]))

    @jsii.member(jsii_name="putClusterConfig")
    def put_cluster_config(
        self,
        *,
        cold_storage_options: typing.Optional[typing.Union["OpensearchDomainClusterConfigColdStorageOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        dedicated_master_count: typing.Optional[jsii.Number] = None,
        dedicated_master_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        dedicated_master_type: typing.Optional[builtins.str] = None,
        instance_count: typing.Optional[jsii.Number] = None,
        instance_type: typing.Optional[builtins.str] = None,
        warm_count: typing.Optional[jsii.Number] = None,
        warm_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        warm_type: typing.Optional[builtins.str] = None,
        zone_awareness_config: typing.Optional[typing.Union["OpensearchDomainClusterConfigZoneAwarenessConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        zone_awareness_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param cold_storage_options: cold_storage_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#cold_storage_options OpensearchDomain#cold_storage_options}
        :param dedicated_master_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#dedicated_master_count OpensearchDomain#dedicated_master_count}.
        :param dedicated_master_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#dedicated_master_enabled OpensearchDomain#dedicated_master_enabled}.
        :param dedicated_master_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#dedicated_master_type OpensearchDomain#dedicated_master_type}.
        :param instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#instance_count OpensearchDomain#instance_count}.
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#instance_type OpensearchDomain#instance_type}.
        :param warm_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#warm_count OpensearchDomain#warm_count}.
        :param warm_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#warm_enabled OpensearchDomain#warm_enabled}.
        :param warm_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#warm_type OpensearchDomain#warm_type}.
        :param zone_awareness_config: zone_awareness_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#zone_awareness_config OpensearchDomain#zone_awareness_config}
        :param zone_awareness_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#zone_awareness_enabled OpensearchDomain#zone_awareness_enabled}.
        '''
        value = OpensearchDomainClusterConfig(
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
        :param identity_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#identity_pool_id OpensearchDomain#identity_pool_id}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#role_arn OpensearchDomain#role_arn}.
        :param user_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#user_pool_id OpensearchDomain#user_pool_id}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#enabled OpensearchDomain#enabled}.
        '''
        value = OpensearchDomainCognitoOptions(
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
        :param custom_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#custom_endpoint OpensearchDomain#custom_endpoint}.
        :param custom_endpoint_certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#custom_endpoint_certificate_arn OpensearchDomain#custom_endpoint_certificate_arn}.
        :param custom_endpoint_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#custom_endpoint_enabled OpensearchDomain#custom_endpoint_enabled}.
        :param enforce_https: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#enforce_https OpensearchDomain#enforce_https}.
        :param tls_security_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#tls_security_policy OpensearchDomain#tls_security_policy}.
        '''
        value = OpensearchDomainDomainEndpointOptions(
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
        :param ebs_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#ebs_enabled OpensearchDomain#ebs_enabled}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#iops OpensearchDomain#iops}.
        :param throughput: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#throughput OpensearchDomain#throughput}.
        :param volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#volume_size OpensearchDomain#volume_size}.
        :param volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#volume_type OpensearchDomain#volume_type}.
        '''
        value = OpensearchDomainEbsOptions(
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
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#enabled OpensearchDomain#enabled}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#kms_key_id OpensearchDomain#kms_key_id}.
        '''
        value = OpensearchDomainEncryptAtRest(enabled=enabled, kms_key_id=kms_key_id)

        return typing.cast(None, jsii.invoke(self, "putEncryptAtRest", [value]))

    @jsii.member(jsii_name="putLogPublishingOptions")
    def put_log_publishing_options(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["OpensearchDomainLogPublishingOptions", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdba9f8a5d4fae2baba31a378f7e1df936d7fae7e90d2c6d75c0896ed32f5da6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLogPublishingOptions", [value]))

    @jsii.member(jsii_name="putNodeToNodeEncryption")
    def put_node_to_node_encryption(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#enabled OpensearchDomain#enabled}.
        '''
        value = OpensearchDomainNodeToNodeEncryption(enabled=enabled)

        return typing.cast(None, jsii.invoke(self, "putNodeToNodeEncryption", [value]))

    @jsii.member(jsii_name="putSnapshotOptions")
    def put_snapshot_options(
        self,
        *,
        automated_snapshot_start_hour: jsii.Number,
    ) -> None:
        '''
        :param automated_snapshot_start_hour: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#automated_snapshot_start_hour OpensearchDomain#automated_snapshot_start_hour}.
        '''
        value = OpensearchDomainSnapshotOptions(
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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#create OpensearchDomain#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#delete OpensearchDomain#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#update OpensearchDomain#update}.
        '''
        value = OpensearchDomainTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putVpcOptions")
    def put_vpc_options(
        self,
        *,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#security_group_ids OpensearchDomain#security_group_ids}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#subnet_ids OpensearchDomain#subnet_ids}.
        '''
        value = OpensearchDomainVpcOptions(
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

    @jsii.member(jsii_name="resetEncryptAtRest")
    def reset_encrypt_at_rest(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptAtRest", []))

    @jsii.member(jsii_name="resetEngineVersion")
    def reset_engine_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEngineVersion", []))

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
    ) -> "OpensearchDomainAdvancedSecurityOptionsOutputReference":
        return typing.cast("OpensearchDomainAdvancedSecurityOptionsOutputReference", jsii.get(self, "advancedSecurityOptions"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="autoTuneOptions")
    def auto_tune_options(self) -> "OpensearchDomainAutoTuneOptionsOutputReference":
        return typing.cast("OpensearchDomainAutoTuneOptionsOutputReference", jsii.get(self, "autoTuneOptions"))

    @builtins.property
    @jsii.member(jsii_name="clusterConfig")
    def cluster_config(self) -> "OpensearchDomainClusterConfigOutputReference":
        return typing.cast("OpensearchDomainClusterConfigOutputReference", jsii.get(self, "clusterConfig"))

    @builtins.property
    @jsii.member(jsii_name="cognitoOptions")
    def cognito_options(self) -> "OpensearchDomainCognitoOptionsOutputReference":
        return typing.cast("OpensearchDomainCognitoOptionsOutputReference", jsii.get(self, "cognitoOptions"))

    @builtins.property
    @jsii.member(jsii_name="domainEndpointOptions")
    def domain_endpoint_options(
        self,
    ) -> "OpensearchDomainDomainEndpointOptionsOutputReference":
        return typing.cast("OpensearchDomainDomainEndpointOptionsOutputReference", jsii.get(self, "domainEndpointOptions"))

    @builtins.property
    @jsii.member(jsii_name="domainId")
    def domain_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainId"))

    @builtins.property
    @jsii.member(jsii_name="ebsOptions")
    def ebs_options(self) -> "OpensearchDomainEbsOptionsOutputReference":
        return typing.cast("OpensearchDomainEbsOptionsOutputReference", jsii.get(self, "ebsOptions"))

    @builtins.property
    @jsii.member(jsii_name="encryptAtRest")
    def encrypt_at_rest(self) -> "OpensearchDomainEncryptAtRestOutputReference":
        return typing.cast("OpensearchDomainEncryptAtRestOutputReference", jsii.get(self, "encryptAtRest"))

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
    def log_publishing_options(self) -> "OpensearchDomainLogPublishingOptionsList":
        return typing.cast("OpensearchDomainLogPublishingOptionsList", jsii.get(self, "logPublishingOptions"))

    @builtins.property
    @jsii.member(jsii_name="nodeToNodeEncryption")
    def node_to_node_encryption(
        self,
    ) -> "OpensearchDomainNodeToNodeEncryptionOutputReference":
        return typing.cast("OpensearchDomainNodeToNodeEncryptionOutputReference", jsii.get(self, "nodeToNodeEncryption"))

    @builtins.property
    @jsii.member(jsii_name="snapshotOptions")
    def snapshot_options(self) -> "OpensearchDomainSnapshotOptionsOutputReference":
        return typing.cast("OpensearchDomainSnapshotOptionsOutputReference", jsii.get(self, "snapshotOptions"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "OpensearchDomainTimeoutsOutputReference":
        return typing.cast("OpensearchDomainTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="vpcOptions")
    def vpc_options(self) -> "OpensearchDomainVpcOptionsOutputReference":
        return typing.cast("OpensearchDomainVpcOptionsOutputReference", jsii.get(self, "vpcOptions"))

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
    ) -> typing.Optional["OpensearchDomainAdvancedSecurityOptions"]:
        return typing.cast(typing.Optional["OpensearchDomainAdvancedSecurityOptions"], jsii.get(self, "advancedSecurityOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="autoTuneOptionsInput")
    def auto_tune_options_input(
        self,
    ) -> typing.Optional["OpensearchDomainAutoTuneOptions"]:
        return typing.cast(typing.Optional["OpensearchDomainAutoTuneOptions"], jsii.get(self, "autoTuneOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterConfigInput")
    def cluster_config_input(self) -> typing.Optional["OpensearchDomainClusterConfig"]:
        return typing.cast(typing.Optional["OpensearchDomainClusterConfig"], jsii.get(self, "clusterConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="cognitoOptionsInput")
    def cognito_options_input(
        self,
    ) -> typing.Optional["OpensearchDomainCognitoOptions"]:
        return typing.cast(typing.Optional["OpensearchDomainCognitoOptions"], jsii.get(self, "cognitoOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="domainEndpointOptionsInput")
    def domain_endpoint_options_input(
        self,
    ) -> typing.Optional["OpensearchDomainDomainEndpointOptions"]:
        return typing.cast(typing.Optional["OpensearchDomainDomainEndpointOptions"], jsii.get(self, "domainEndpointOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="domainNameInput")
    def domain_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainNameInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsOptionsInput")
    def ebs_options_input(self) -> typing.Optional["OpensearchDomainEbsOptions"]:
        return typing.cast(typing.Optional["OpensearchDomainEbsOptions"], jsii.get(self, "ebsOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptAtRestInput")
    def encrypt_at_rest_input(self) -> typing.Optional["OpensearchDomainEncryptAtRest"]:
        return typing.cast(typing.Optional["OpensearchDomainEncryptAtRest"], jsii.get(self, "encryptAtRestInput"))

    @builtins.property
    @jsii.member(jsii_name="engineVersionInput")
    def engine_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engineVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="logPublishingOptionsInput")
    def log_publishing_options_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["OpensearchDomainLogPublishingOptions"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["OpensearchDomainLogPublishingOptions"]]], jsii.get(self, "logPublishingOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeToNodeEncryptionInput")
    def node_to_node_encryption_input(
        self,
    ) -> typing.Optional["OpensearchDomainNodeToNodeEncryption"]:
        return typing.cast(typing.Optional["OpensearchDomainNodeToNodeEncryption"], jsii.get(self, "nodeToNodeEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="snapshotOptionsInput")
    def snapshot_options_input(
        self,
    ) -> typing.Optional["OpensearchDomainSnapshotOptions"]:
        return typing.cast(typing.Optional["OpensearchDomainSnapshotOptions"], jsii.get(self, "snapshotOptionsInput"))

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
    ) -> typing.Optional[typing.Union["OpensearchDomainTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["OpensearchDomainTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcOptionsInput")
    def vpc_options_input(self) -> typing.Optional["OpensearchDomainVpcOptions"]:
        return typing.cast(typing.Optional["OpensearchDomainVpcOptions"], jsii.get(self, "vpcOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="accessPolicies")
    def access_policies(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessPolicies"))

    @access_policies.setter
    def access_policies(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44f2621ddf2663f5403545486d7b83097e0852adea2b03153f0b4a1148cf2ef6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0cec8ae3c5c509e3cd49b65ca19a3c915bf7ee3ab2e430e51dd770fa908d3d40)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "advancedOptions", value)

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0aa358ea527377fb52dd7fd6f5825ee3db935773f3479b386b584e1b55e2af22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="engineVersion")
    def engine_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "engineVersion"))

    @engine_version.setter
    def engine_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8dbf20a3ebd3c252792daf251397b7234615eca21a6a0a602af3fb7466152d19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engineVersion", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d15704cd50b86c41b78761823cd9ed8f9671f535064c74a0b69fd102d6eea18c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f414675affec435a6c58f97d4fca8bcff50f27a11c4eeba626d073e9bc5f8a58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be99ef674767ba442079ebef29df760414cbdb663c0e46fb55f36490300baf12)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.opensearchDomain.OpensearchDomainAdvancedSecurityOptions",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "anonymous_auth_enabled": "anonymousAuthEnabled",
        "internal_user_database_enabled": "internalUserDatabaseEnabled",
        "master_user_options": "masterUserOptions",
    },
)
class OpensearchDomainAdvancedSecurityOptions:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        anonymous_auth_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        internal_user_database_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        master_user_options: typing.Optional[typing.Union["OpensearchDomainAdvancedSecurityOptionsMasterUserOptions", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#enabled OpensearchDomain#enabled}.
        :param anonymous_auth_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#anonymous_auth_enabled OpensearchDomain#anonymous_auth_enabled}.
        :param internal_user_database_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#internal_user_database_enabled OpensearchDomain#internal_user_database_enabled}.
        :param master_user_options: master_user_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#master_user_options OpensearchDomain#master_user_options}
        '''
        if isinstance(master_user_options, dict):
            master_user_options = OpensearchDomainAdvancedSecurityOptionsMasterUserOptions(**master_user_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e93fff473e9af3e1fc261985781bab87b5cd2aed876b9bb1d65d7c5a8db48f9b)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument anonymous_auth_enabled", value=anonymous_auth_enabled, expected_type=type_hints["anonymous_auth_enabled"])
            check_type(argname="argument internal_user_database_enabled", value=internal_user_database_enabled, expected_type=type_hints["internal_user_database_enabled"])
            check_type(argname="argument master_user_options", value=master_user_options, expected_type=type_hints["master_user_options"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled": enabled,
        }
        if anonymous_auth_enabled is not None:
            self._values["anonymous_auth_enabled"] = anonymous_auth_enabled
        if internal_user_database_enabled is not None:
            self._values["internal_user_database_enabled"] = internal_user_database_enabled
        if master_user_options is not None:
            self._values["master_user_options"] = master_user_options

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#enabled OpensearchDomain#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def anonymous_auth_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#anonymous_auth_enabled OpensearchDomain#anonymous_auth_enabled}.'''
        result = self._values.get("anonymous_auth_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def internal_user_database_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#internal_user_database_enabled OpensearchDomain#internal_user_database_enabled}.'''
        result = self._values.get("internal_user_database_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def master_user_options(
        self,
    ) -> typing.Optional["OpensearchDomainAdvancedSecurityOptionsMasterUserOptions"]:
        '''master_user_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#master_user_options OpensearchDomain#master_user_options}
        '''
        result = self._values.get("master_user_options")
        return typing.cast(typing.Optional["OpensearchDomainAdvancedSecurityOptionsMasterUserOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpensearchDomainAdvancedSecurityOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.opensearchDomain.OpensearchDomainAdvancedSecurityOptionsMasterUserOptions",
    jsii_struct_bases=[],
    name_mapping={
        "master_user_arn": "masterUserArn",
        "master_user_name": "masterUserName",
        "master_user_password": "masterUserPassword",
    },
)
class OpensearchDomainAdvancedSecurityOptionsMasterUserOptions:
    def __init__(
        self,
        *,
        master_user_arn: typing.Optional[builtins.str] = None,
        master_user_name: typing.Optional[builtins.str] = None,
        master_user_password: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param master_user_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#master_user_arn OpensearchDomain#master_user_arn}.
        :param master_user_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#master_user_name OpensearchDomain#master_user_name}.
        :param master_user_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#master_user_password OpensearchDomain#master_user_password}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e2afa0275fdac20fc9f041b591d770b6f8e2885d3705c9ecff3eba0a51f810d)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#master_user_arn OpensearchDomain#master_user_arn}.'''
        result = self._values.get("master_user_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def master_user_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#master_user_name OpensearchDomain#master_user_name}.'''
        result = self._values.get("master_user_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def master_user_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#master_user_password OpensearchDomain#master_user_password}.'''
        result = self._values.get("master_user_password")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpensearchDomainAdvancedSecurityOptionsMasterUserOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpensearchDomainAdvancedSecurityOptionsMasterUserOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opensearchDomain.OpensearchDomainAdvancedSecurityOptionsMasterUserOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1774a8a6714f3c4ed4ccf0d0f0d71b98f5e2434c26e09154cc73fc07c11061b0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0f971bd74ea3b8abea38d7a3c4849a3c67db82f159ded42b8f3608948f138806)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "masterUserArn", value)

    @builtins.property
    @jsii.member(jsii_name="masterUserName")
    def master_user_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "masterUserName"))

    @master_user_name.setter
    def master_user_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af27b520f20ea06e9e58f82e3f622aa135d81bd0bd19d51d11e6b392b37d686e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "masterUserName", value)

    @builtins.property
    @jsii.member(jsii_name="masterUserPassword")
    def master_user_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "masterUserPassword"))

    @master_user_password.setter
    def master_user_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74a79ce2fa2ab8fc7515f6f92675b6db81a6a8dc34252a2c27cb9982ec9a22f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "masterUserPassword", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OpensearchDomainAdvancedSecurityOptionsMasterUserOptions]:
        return typing.cast(typing.Optional[OpensearchDomainAdvancedSecurityOptionsMasterUserOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpensearchDomainAdvancedSecurityOptionsMasterUserOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c4d90b14668d819eccd9a85b09de01b53face6722d031ca3b616cfb6adfe366)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OpensearchDomainAdvancedSecurityOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opensearchDomain.OpensearchDomainAdvancedSecurityOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4d57e4923f2da451b53b0725d3f0322a29de9590349d3fd7014a65921da15e1a)
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
        :param master_user_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#master_user_arn OpensearchDomain#master_user_arn}.
        :param master_user_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#master_user_name OpensearchDomain#master_user_name}.
        :param master_user_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#master_user_password OpensearchDomain#master_user_password}.
        '''
        value = OpensearchDomainAdvancedSecurityOptionsMasterUserOptions(
            master_user_arn=master_user_arn,
            master_user_name=master_user_name,
            master_user_password=master_user_password,
        )

        return typing.cast(None, jsii.invoke(self, "putMasterUserOptions", [value]))

    @jsii.member(jsii_name="resetAnonymousAuthEnabled")
    def reset_anonymous_auth_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnonymousAuthEnabled", []))

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
    ) -> OpensearchDomainAdvancedSecurityOptionsMasterUserOptionsOutputReference:
        return typing.cast(OpensearchDomainAdvancedSecurityOptionsMasterUserOptionsOutputReference, jsii.get(self, "masterUserOptions"))

    @builtins.property
    @jsii.member(jsii_name="anonymousAuthEnabledInput")
    def anonymous_auth_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "anonymousAuthEnabledInput"))

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
    ) -> typing.Optional[OpensearchDomainAdvancedSecurityOptionsMasterUserOptions]:
        return typing.cast(typing.Optional[OpensearchDomainAdvancedSecurityOptionsMasterUserOptions], jsii.get(self, "masterUserOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="anonymousAuthEnabled")
    def anonymous_auth_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "anonymousAuthEnabled"))

    @anonymous_auth_enabled.setter
    def anonymous_auth_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ac8d37cf4f05e24826f81a418531b18b43dc316ed7b04782795ea23d753235a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "anonymousAuthEnabled", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__2fce51da7de836da65c1d47187c4ee6b0a38f712fedb94684c18ba0d6c12e75b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2d8aa76bf975e2e0b4c7630c7737e22b2160a0dc3ecc694b356cd2fd99bed325)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalUserDatabaseEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OpensearchDomainAdvancedSecurityOptions]:
        return typing.cast(typing.Optional[OpensearchDomainAdvancedSecurityOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpensearchDomainAdvancedSecurityOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bfa7665913d961c8f325e0581122bd30187626e2ef015a9f291fa15770954f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.opensearchDomain.OpensearchDomainAutoTuneOptions",
    jsii_struct_bases=[],
    name_mapping={
        "desired_state": "desiredState",
        "maintenance_schedule": "maintenanceSchedule",
        "rollback_on_disable": "rollbackOnDisable",
    },
)
class OpensearchDomainAutoTuneOptions:
    def __init__(
        self,
        *,
        desired_state: builtins.str,
        maintenance_schedule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["OpensearchDomainAutoTuneOptionsMaintenanceSchedule", typing.Dict[builtins.str, typing.Any]]]]] = None,
        rollback_on_disable: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param desired_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#desired_state OpensearchDomain#desired_state}.
        :param maintenance_schedule: maintenance_schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#maintenance_schedule OpensearchDomain#maintenance_schedule}
        :param rollback_on_disable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#rollback_on_disable OpensearchDomain#rollback_on_disable}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b074447e70909491001362252fe10821830b0262456b33cad218c923f1d261d)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#desired_state OpensearchDomain#desired_state}.'''
        result = self._values.get("desired_state")
        assert result is not None, "Required property 'desired_state' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def maintenance_schedule(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["OpensearchDomainAutoTuneOptionsMaintenanceSchedule"]]]:
        '''maintenance_schedule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#maintenance_schedule OpensearchDomain#maintenance_schedule}
        '''
        result = self._values.get("maintenance_schedule")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["OpensearchDomainAutoTuneOptionsMaintenanceSchedule"]]], result)

    @builtins.property
    def rollback_on_disable(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#rollback_on_disable OpensearchDomain#rollback_on_disable}.'''
        result = self._values.get("rollback_on_disable")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpensearchDomainAutoTuneOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.opensearchDomain.OpensearchDomainAutoTuneOptionsMaintenanceSchedule",
    jsii_struct_bases=[],
    name_mapping={
        "cron_expression_for_recurrence": "cronExpressionForRecurrence",
        "duration": "duration",
        "start_at": "startAt",
    },
)
class OpensearchDomainAutoTuneOptionsMaintenanceSchedule:
    def __init__(
        self,
        *,
        cron_expression_for_recurrence: builtins.str,
        duration: typing.Union["OpensearchDomainAutoTuneOptionsMaintenanceScheduleDuration", typing.Dict[builtins.str, typing.Any]],
        start_at: builtins.str,
    ) -> None:
        '''
        :param cron_expression_for_recurrence: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#cron_expression_for_recurrence OpensearchDomain#cron_expression_for_recurrence}.
        :param duration: duration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#duration OpensearchDomain#duration}
        :param start_at: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#start_at OpensearchDomain#start_at}.
        '''
        if isinstance(duration, dict):
            duration = OpensearchDomainAutoTuneOptionsMaintenanceScheduleDuration(**duration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab45bf853f73598a6ccf997b973a1582b533772d2441a3fe194b0a5ca15ae06e)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#cron_expression_for_recurrence OpensearchDomain#cron_expression_for_recurrence}.'''
        result = self._values.get("cron_expression_for_recurrence")
        assert result is not None, "Required property 'cron_expression_for_recurrence' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def duration(self) -> "OpensearchDomainAutoTuneOptionsMaintenanceScheduleDuration":
        '''duration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#duration OpensearchDomain#duration}
        '''
        result = self._values.get("duration")
        assert result is not None, "Required property 'duration' is missing"
        return typing.cast("OpensearchDomainAutoTuneOptionsMaintenanceScheduleDuration", result)

    @builtins.property
    def start_at(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#start_at OpensearchDomain#start_at}.'''
        result = self._values.get("start_at")
        assert result is not None, "Required property 'start_at' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpensearchDomainAutoTuneOptionsMaintenanceSchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.opensearchDomain.OpensearchDomainAutoTuneOptionsMaintenanceScheduleDuration",
    jsii_struct_bases=[],
    name_mapping={"unit": "unit", "value": "value"},
)
class OpensearchDomainAutoTuneOptionsMaintenanceScheduleDuration:
    def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#unit OpensearchDomain#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#value OpensearchDomain#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fdbc09fc77e37a5f756a2f3616e2b07a0acd90dd45847abb5fd52248d110d05b)
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "unit": unit,
            "value": value,
        }

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#unit OpensearchDomain#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#value OpensearchDomain#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpensearchDomainAutoTuneOptionsMaintenanceScheduleDuration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpensearchDomainAutoTuneOptionsMaintenanceScheduleDurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opensearchDomain.OpensearchDomainAutoTuneOptionsMaintenanceScheduleDurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__062a67e0d9f401663c9f66428066fd977678ea0b751249478a371b79b69c113f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9af5e3b3c766e785dc29e80eda9caeff30e35b71bea6da895b67f3d61c870491)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0342c85f45208f25ba40b77a253030a716c151f7ffa254a1647abbbf785479b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OpensearchDomainAutoTuneOptionsMaintenanceScheduleDuration]:
        return typing.cast(typing.Optional[OpensearchDomainAutoTuneOptionsMaintenanceScheduleDuration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpensearchDomainAutoTuneOptionsMaintenanceScheduleDuration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__532e37649b5235109a5f03529d34edf29b8e5ac418393124aed495954bbdf40e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OpensearchDomainAutoTuneOptionsMaintenanceScheduleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opensearchDomain.OpensearchDomainAutoTuneOptionsMaintenanceScheduleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__808c288ab47e3aaad8b60a9c2a7059b1a36f4e4ddfc508127e965db76d37821c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OpensearchDomainAutoTuneOptionsMaintenanceScheduleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32ec2d59231b5e405750686faa220f24ec8d02fcf56c9647520f8ec13b25db5e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OpensearchDomainAutoTuneOptionsMaintenanceScheduleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bd0390b7a1602f3a3e34cfee41dd46a24a4c5ff4afac2b21c74deba2e8eb7a1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f153fcca8df97bb2194d0ff8ff3f8eb7feb339b06532390fe279fb0f92dc12ea)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a64407e4dfbd55f772e623fcd98093920f6b8a859afb4d07b1abb4047f0062dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpensearchDomainAutoTuneOptionsMaintenanceSchedule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpensearchDomainAutoTuneOptionsMaintenanceSchedule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpensearchDomainAutoTuneOptionsMaintenanceSchedule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d67babed7a54fe97c2c4bc73115ffe901b786d80270c69b27abaf90ddeddca6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OpensearchDomainAutoTuneOptionsMaintenanceScheduleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opensearchDomain.OpensearchDomainAutoTuneOptionsMaintenanceScheduleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8af68c62f31a3feca4716ae0d64061d67c03201b66197199325baf4e0655fedb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDuration")
    def put_duration(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#unit OpensearchDomain#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#value OpensearchDomain#value}.
        '''
        value_ = OpensearchDomainAutoTuneOptionsMaintenanceScheduleDuration(
            unit=unit, value=value
        )

        return typing.cast(None, jsii.invoke(self, "putDuration", [value_]))

    @builtins.property
    @jsii.member(jsii_name="duration")
    def duration(
        self,
    ) -> OpensearchDomainAutoTuneOptionsMaintenanceScheduleDurationOutputReference:
        return typing.cast(OpensearchDomainAutoTuneOptionsMaintenanceScheduleDurationOutputReference, jsii.get(self, "duration"))

    @builtins.property
    @jsii.member(jsii_name="cronExpressionForRecurrenceInput")
    def cron_expression_for_recurrence_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cronExpressionForRecurrenceInput"))

    @builtins.property
    @jsii.member(jsii_name="durationInput")
    def duration_input(
        self,
    ) -> typing.Optional[OpensearchDomainAutoTuneOptionsMaintenanceScheduleDuration]:
        return typing.cast(typing.Optional[OpensearchDomainAutoTuneOptionsMaintenanceScheduleDuration], jsii.get(self, "durationInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__69a2d6dd7115f13601122e5de25dbf48624703cb3e5d565a2e1fb39e8ab3f7ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cronExpressionForRecurrence", value)

    @builtins.property
    @jsii.member(jsii_name="startAt")
    def start_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startAt"))

    @start_at.setter
    def start_at(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d4e5d6973f1d4069c5f2b54cd0acf8d04a3db69f95122cb2bb951f526fcab8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startAt", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OpensearchDomainAutoTuneOptionsMaintenanceSchedule, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OpensearchDomainAutoTuneOptionsMaintenanceSchedule, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OpensearchDomainAutoTuneOptionsMaintenanceSchedule, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac43099682dfe2e261c67d6b772940ee1dc18dc268505e6deed521e8f7bd7c2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OpensearchDomainAutoTuneOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opensearchDomain.OpensearchDomainAutoTuneOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__17851dcb7db7b8b73ecf9a7100fb4b8c1c60f1b08690ff7e172acbcbb5085b1f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMaintenanceSchedule")
    def put_maintenance_schedule(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[OpensearchDomainAutoTuneOptionsMaintenanceSchedule, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea7b412d362958803bff269a7567e0f0cedaa97dbce5ee1a1d7f1f31a813509a)
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
    ) -> OpensearchDomainAutoTuneOptionsMaintenanceScheduleList:
        return typing.cast(OpensearchDomainAutoTuneOptionsMaintenanceScheduleList, jsii.get(self, "maintenanceSchedule"))

    @builtins.property
    @jsii.member(jsii_name="desiredStateInput")
    def desired_state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "desiredStateInput"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceScheduleInput")
    def maintenance_schedule_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpensearchDomainAutoTuneOptionsMaintenanceSchedule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpensearchDomainAutoTuneOptionsMaintenanceSchedule]]], jsii.get(self, "maintenanceScheduleInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__10c129d2eac2686de2d8efed60983ec6560b006afa965079bc732137d330429b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desiredState", value)

    @builtins.property
    @jsii.member(jsii_name="rollbackOnDisable")
    def rollback_on_disable(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rollbackOnDisable"))

    @rollback_on_disable.setter
    def rollback_on_disable(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff612dd31473d8e3e9f74f6a28274b71a5f188ea45cde85cf99b25d990af35b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rollbackOnDisable", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OpensearchDomainAutoTuneOptions]:
        return typing.cast(typing.Optional[OpensearchDomainAutoTuneOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpensearchDomainAutoTuneOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e726e2949e470a994c7bf6766385d0c73538c6677e0ad379cd002ea353bda5f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.opensearchDomain.OpensearchDomainClusterConfig",
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
class OpensearchDomainClusterConfig:
    def __init__(
        self,
        *,
        cold_storage_options: typing.Optional[typing.Union["OpensearchDomainClusterConfigColdStorageOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        dedicated_master_count: typing.Optional[jsii.Number] = None,
        dedicated_master_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        dedicated_master_type: typing.Optional[builtins.str] = None,
        instance_count: typing.Optional[jsii.Number] = None,
        instance_type: typing.Optional[builtins.str] = None,
        warm_count: typing.Optional[jsii.Number] = None,
        warm_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        warm_type: typing.Optional[builtins.str] = None,
        zone_awareness_config: typing.Optional[typing.Union["OpensearchDomainClusterConfigZoneAwarenessConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        zone_awareness_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param cold_storage_options: cold_storage_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#cold_storage_options OpensearchDomain#cold_storage_options}
        :param dedicated_master_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#dedicated_master_count OpensearchDomain#dedicated_master_count}.
        :param dedicated_master_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#dedicated_master_enabled OpensearchDomain#dedicated_master_enabled}.
        :param dedicated_master_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#dedicated_master_type OpensearchDomain#dedicated_master_type}.
        :param instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#instance_count OpensearchDomain#instance_count}.
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#instance_type OpensearchDomain#instance_type}.
        :param warm_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#warm_count OpensearchDomain#warm_count}.
        :param warm_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#warm_enabled OpensearchDomain#warm_enabled}.
        :param warm_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#warm_type OpensearchDomain#warm_type}.
        :param zone_awareness_config: zone_awareness_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#zone_awareness_config OpensearchDomain#zone_awareness_config}
        :param zone_awareness_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#zone_awareness_enabled OpensearchDomain#zone_awareness_enabled}.
        '''
        if isinstance(cold_storage_options, dict):
            cold_storage_options = OpensearchDomainClusterConfigColdStorageOptions(**cold_storage_options)
        if isinstance(zone_awareness_config, dict):
            zone_awareness_config = OpensearchDomainClusterConfigZoneAwarenessConfig(**zone_awareness_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e8411e07992a73a9fa186e95118bf9daf8f7371c6879ceeb1620d56122e97a6)
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
    ) -> typing.Optional["OpensearchDomainClusterConfigColdStorageOptions"]:
        '''cold_storage_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#cold_storage_options OpensearchDomain#cold_storage_options}
        '''
        result = self._values.get("cold_storage_options")
        return typing.cast(typing.Optional["OpensearchDomainClusterConfigColdStorageOptions"], result)

    @builtins.property
    def dedicated_master_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#dedicated_master_count OpensearchDomain#dedicated_master_count}.'''
        result = self._values.get("dedicated_master_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def dedicated_master_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#dedicated_master_enabled OpensearchDomain#dedicated_master_enabled}.'''
        result = self._values.get("dedicated_master_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def dedicated_master_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#dedicated_master_type OpensearchDomain#dedicated_master_type}.'''
        result = self._values.get("dedicated_master_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#instance_count OpensearchDomain#instance_count}.'''
        result = self._values.get("instance_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def instance_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#instance_type OpensearchDomain#instance_type}.'''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def warm_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#warm_count OpensearchDomain#warm_count}.'''
        result = self._values.get("warm_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def warm_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#warm_enabled OpensearchDomain#warm_enabled}.'''
        result = self._values.get("warm_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def warm_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#warm_type OpensearchDomain#warm_type}.'''
        result = self._values.get("warm_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def zone_awareness_config(
        self,
    ) -> typing.Optional["OpensearchDomainClusterConfigZoneAwarenessConfig"]:
        '''zone_awareness_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#zone_awareness_config OpensearchDomain#zone_awareness_config}
        '''
        result = self._values.get("zone_awareness_config")
        return typing.cast(typing.Optional["OpensearchDomainClusterConfigZoneAwarenessConfig"], result)

    @builtins.property
    def zone_awareness_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#zone_awareness_enabled OpensearchDomain#zone_awareness_enabled}.'''
        result = self._values.get("zone_awareness_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpensearchDomainClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.opensearchDomain.OpensearchDomainClusterConfigColdStorageOptions",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class OpensearchDomainClusterConfigColdStorageOptions:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#enabled OpensearchDomain#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6f679694137ede29004677107a0d83034fd0a8d92e2b24c1b6611f2b8505058)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#enabled OpensearchDomain#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpensearchDomainClusterConfigColdStorageOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpensearchDomainClusterConfigColdStorageOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opensearchDomain.OpensearchDomainClusterConfigColdStorageOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3af9e7a62f6142b795de219833c35fecfc628e538f828683082fe3bc99c89350)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2d05b8fed77b36618ac20c6837e16f73aa592bb3c678e1afd84200756bbdd785)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OpensearchDomainClusterConfigColdStorageOptions]:
        return typing.cast(typing.Optional[OpensearchDomainClusterConfigColdStorageOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpensearchDomainClusterConfigColdStorageOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec71b183fa6e49eff8cc80b803f5f62dc81da36733efb3bc6e4bf608e6777129)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OpensearchDomainClusterConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opensearchDomain.OpensearchDomainClusterConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__35195fcac4e7e4a00e95509a8f80693e1dd0e1a73bc860cca8a267100a701496)
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
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#enabled OpensearchDomain#enabled}.
        '''
        value = OpensearchDomainClusterConfigColdStorageOptions(enabled=enabled)

        return typing.cast(None, jsii.invoke(self, "putColdStorageOptions", [value]))

    @jsii.member(jsii_name="putZoneAwarenessConfig")
    def put_zone_awareness_config(
        self,
        *,
        availability_zone_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param availability_zone_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#availability_zone_count OpensearchDomain#availability_zone_count}.
        '''
        value = OpensearchDomainClusterConfigZoneAwarenessConfig(
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
    ) -> OpensearchDomainClusterConfigColdStorageOptionsOutputReference:
        return typing.cast(OpensearchDomainClusterConfigColdStorageOptionsOutputReference, jsii.get(self, "coldStorageOptions"))

    @builtins.property
    @jsii.member(jsii_name="zoneAwarenessConfig")
    def zone_awareness_config(
        self,
    ) -> "OpensearchDomainClusterConfigZoneAwarenessConfigOutputReference":
        return typing.cast("OpensearchDomainClusterConfigZoneAwarenessConfigOutputReference", jsii.get(self, "zoneAwarenessConfig"))

    @builtins.property
    @jsii.member(jsii_name="coldStorageOptionsInput")
    def cold_storage_options_input(
        self,
    ) -> typing.Optional[OpensearchDomainClusterConfigColdStorageOptions]:
        return typing.cast(typing.Optional[OpensearchDomainClusterConfigColdStorageOptions], jsii.get(self, "coldStorageOptionsInput"))

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
    ) -> typing.Optional["OpensearchDomainClusterConfigZoneAwarenessConfig"]:
        return typing.cast(typing.Optional["OpensearchDomainClusterConfigZoneAwarenessConfig"], jsii.get(self, "zoneAwarenessConfigInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__fe4e89c479869ee71fd60000738272a04f894ec6d1cb1e3b61d7c55d8e03b7be)
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
            type_hints = typing.get_type_hints(_typecheckingstub__88da7401e66d3b1d575785c02ccab83cd817aa2be0457f1fbe844102df87f56e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dedicatedMasterEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="dedicatedMasterType")
    def dedicated_master_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dedicatedMasterType"))

    @dedicated_master_type.setter
    def dedicated_master_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b646b0fb23a4ab6fdbb8c14eb66a3f13be1db837f4321d424296b88f6350e2d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dedicatedMasterType", value)

    @builtins.property
    @jsii.member(jsii_name="instanceCount")
    def instance_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instanceCount"))

    @instance_count.setter
    def instance_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2f585da7bb8f8a0b914b86b905efc677b356468c743b8e8b5ed17cf12ea85f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceCount", value)

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35f954c1acf223d0e7f4c82a434b3b7eab3103886ef0d0013a20c369232ccd35)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="warmCount")
    def warm_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "warmCount"))

    @warm_count.setter
    def warm_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e2df952d93da8c659820a9148d1b7a0215b684db50012f719a1daaaf143cd2c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b2019f61bbcd29b457e9d57e1f099f37d0a9d272a90cc701d3f783df0b68b739)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "warmEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="warmType")
    def warm_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "warmType"))

    @warm_type.setter
    def warm_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d144c56029757b44d8335e5b450a5bc39574ab12896e986c77dd6b5234b6dd6c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9d9438ff45986e60f09fdc5872f515477b376c50671da3ec621d3425180c7aaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneAwarenessEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OpensearchDomainClusterConfig]:
        return typing.cast(typing.Optional[OpensearchDomainClusterConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpensearchDomainClusterConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__116b8f76b85b5a133780556611dd0694160a1551b3846d101dcc65fd1576da2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.opensearchDomain.OpensearchDomainClusterConfigZoneAwarenessConfig",
    jsii_struct_bases=[],
    name_mapping={"availability_zone_count": "availabilityZoneCount"},
)
class OpensearchDomainClusterConfigZoneAwarenessConfig:
    def __init__(
        self,
        *,
        availability_zone_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param availability_zone_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#availability_zone_count OpensearchDomain#availability_zone_count}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3acd43b0418006b6d43ebfb4f78f881127e6e7dacacb6db11d66888a1d845dac)
            check_type(argname="argument availability_zone_count", value=availability_zone_count, expected_type=type_hints["availability_zone_count"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if availability_zone_count is not None:
            self._values["availability_zone_count"] = availability_zone_count

    @builtins.property
    def availability_zone_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#availability_zone_count OpensearchDomain#availability_zone_count}.'''
        result = self._values.get("availability_zone_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpensearchDomainClusterConfigZoneAwarenessConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpensearchDomainClusterConfigZoneAwarenessConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opensearchDomain.OpensearchDomainClusterConfigZoneAwarenessConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f72dd99c5e5cef476fb453a2b1e9c266df81c065e02fd3971d8317674c9d32a5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3db1758006a01189b8ba1cdf7d43be4e4a7a4fff395bd45196fd73ecf32ede02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZoneCount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OpensearchDomainClusterConfigZoneAwarenessConfig]:
        return typing.cast(typing.Optional[OpensearchDomainClusterConfigZoneAwarenessConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpensearchDomainClusterConfigZoneAwarenessConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26ce3bb0b6649c7462d41f0f3079498dd7c6902083d37c83a59c6b19079a4bcc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.opensearchDomain.OpensearchDomainCognitoOptions",
    jsii_struct_bases=[],
    name_mapping={
        "identity_pool_id": "identityPoolId",
        "role_arn": "roleArn",
        "user_pool_id": "userPoolId",
        "enabled": "enabled",
    },
)
class OpensearchDomainCognitoOptions:
    def __init__(
        self,
        *,
        identity_pool_id: builtins.str,
        role_arn: builtins.str,
        user_pool_id: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param identity_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#identity_pool_id OpensearchDomain#identity_pool_id}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#role_arn OpensearchDomain#role_arn}.
        :param user_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#user_pool_id OpensearchDomain#user_pool_id}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#enabled OpensearchDomain#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82ba46ecdd55fceeb74cee551b76c3087d9185eb50fc6c127ebd2d9443d86a68)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#identity_pool_id OpensearchDomain#identity_pool_id}.'''
        result = self._values.get("identity_pool_id")
        assert result is not None, "Required property 'identity_pool_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#role_arn OpensearchDomain#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_pool_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#user_pool_id OpensearchDomain#user_pool_id}.'''
        result = self._values.get("user_pool_id")
        assert result is not None, "Required property 'user_pool_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#enabled OpensearchDomain#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpensearchDomainCognitoOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpensearchDomainCognitoOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opensearchDomain.OpensearchDomainCognitoOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c9b3bf6c9b4f8c3e9e87ec6ec4aa85bb652a3df058ba9291f204f28da0518637)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e7705533ecbfabc38d20199c02ac6e3acb8e88769ec6c0c521a3619e62aaaabc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="identityPoolId")
    def identity_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityPoolId"))

    @identity_pool_id.setter
    def identity_pool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fded7922fd6e2bc25c6e3f51dc3292e86dd02fbaf2edda8274b66effd29be08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityPoolId", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__443a8e96af0473350199a90d06a1e6529293bcf7e9f1ef7c60ca65bc6d4781db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="userPoolId")
    def user_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userPoolId"))

    @user_pool_id.setter
    def user_pool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02f428e6c77b8c0801003de15797402d76a6dced332ad366c7cbab7e4bc1ddc6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userPoolId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OpensearchDomainCognitoOptions]:
        return typing.cast(typing.Optional[OpensearchDomainCognitoOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpensearchDomainCognitoOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72528ecee96b72ce27123e9786d6e458f75d6ccfd7b030d021498540afaeec84)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.opensearchDomain.OpensearchDomainConfig",
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
        "encrypt_at_rest": "encryptAtRest",
        "engine_version": "engineVersion",
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
class OpensearchDomainConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        advanced_security_options: typing.Optional[typing.Union[OpensearchDomainAdvancedSecurityOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        auto_tune_options: typing.Optional[typing.Union[OpensearchDomainAutoTuneOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        cluster_config: typing.Optional[typing.Union[OpensearchDomainClusterConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        cognito_options: typing.Optional[typing.Union[OpensearchDomainCognitoOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        domain_endpoint_options: typing.Optional[typing.Union["OpensearchDomainDomainEndpointOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        ebs_options: typing.Optional[typing.Union["OpensearchDomainEbsOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        encrypt_at_rest: typing.Optional[typing.Union["OpensearchDomainEncryptAtRest", typing.Dict[builtins.str, typing.Any]]] = None,
        engine_version: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        log_publishing_options: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["OpensearchDomainLogPublishingOptions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        node_to_node_encryption: typing.Optional[typing.Union["OpensearchDomainNodeToNodeEncryption", typing.Dict[builtins.str, typing.Any]]] = None,
        snapshot_options: typing.Optional[typing.Union["OpensearchDomainSnapshotOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["OpensearchDomainTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        vpc_options: typing.Optional[typing.Union["OpensearchDomainVpcOptions", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param domain_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#domain_name OpensearchDomain#domain_name}.
        :param access_policies: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#access_policies OpensearchDomain#access_policies}.
        :param advanced_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#advanced_options OpensearchDomain#advanced_options}.
        :param advanced_security_options: advanced_security_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#advanced_security_options OpensearchDomain#advanced_security_options}
        :param auto_tune_options: auto_tune_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#auto_tune_options OpensearchDomain#auto_tune_options}
        :param cluster_config: cluster_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#cluster_config OpensearchDomain#cluster_config}
        :param cognito_options: cognito_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#cognito_options OpensearchDomain#cognito_options}
        :param domain_endpoint_options: domain_endpoint_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#domain_endpoint_options OpensearchDomain#domain_endpoint_options}
        :param ebs_options: ebs_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#ebs_options OpensearchDomain#ebs_options}
        :param encrypt_at_rest: encrypt_at_rest block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#encrypt_at_rest OpensearchDomain#encrypt_at_rest}
        :param engine_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#engine_version OpensearchDomain#engine_version}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#id OpensearchDomain#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param log_publishing_options: log_publishing_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#log_publishing_options OpensearchDomain#log_publishing_options}
        :param node_to_node_encryption: node_to_node_encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#node_to_node_encryption OpensearchDomain#node_to_node_encryption}
        :param snapshot_options: snapshot_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#snapshot_options OpensearchDomain#snapshot_options}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#tags OpensearchDomain#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#tags_all OpensearchDomain#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#timeouts OpensearchDomain#timeouts}
        :param vpc_options: vpc_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#vpc_options OpensearchDomain#vpc_options}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(advanced_security_options, dict):
            advanced_security_options = OpensearchDomainAdvancedSecurityOptions(**advanced_security_options)
        if isinstance(auto_tune_options, dict):
            auto_tune_options = OpensearchDomainAutoTuneOptions(**auto_tune_options)
        if isinstance(cluster_config, dict):
            cluster_config = OpensearchDomainClusterConfig(**cluster_config)
        if isinstance(cognito_options, dict):
            cognito_options = OpensearchDomainCognitoOptions(**cognito_options)
        if isinstance(domain_endpoint_options, dict):
            domain_endpoint_options = OpensearchDomainDomainEndpointOptions(**domain_endpoint_options)
        if isinstance(ebs_options, dict):
            ebs_options = OpensearchDomainEbsOptions(**ebs_options)
        if isinstance(encrypt_at_rest, dict):
            encrypt_at_rest = OpensearchDomainEncryptAtRest(**encrypt_at_rest)
        if isinstance(node_to_node_encryption, dict):
            node_to_node_encryption = OpensearchDomainNodeToNodeEncryption(**node_to_node_encryption)
        if isinstance(snapshot_options, dict):
            snapshot_options = OpensearchDomainSnapshotOptions(**snapshot_options)
        if isinstance(timeouts, dict):
            timeouts = OpensearchDomainTimeouts(**timeouts)
        if isinstance(vpc_options, dict):
            vpc_options = OpensearchDomainVpcOptions(**vpc_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7d8e58dc8b23bf0478a5796d7265063a6026a196acb9b811ed2a94fb3081373)
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
            check_type(argname="argument encrypt_at_rest", value=encrypt_at_rest, expected_type=type_hints["encrypt_at_rest"])
            check_type(argname="argument engine_version", value=engine_version, expected_type=type_hints["engine_version"])
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
        if encrypt_at_rest is not None:
            self._values["encrypt_at_rest"] = encrypt_at_rest
        if engine_version is not None:
            self._values["engine_version"] = engine_version
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#domain_name OpensearchDomain#domain_name}.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_policies(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#access_policies OpensearchDomain#access_policies}.'''
        result = self._values.get("access_policies")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def advanced_options(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#advanced_options OpensearchDomain#advanced_options}.'''
        result = self._values.get("advanced_options")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def advanced_security_options(
        self,
    ) -> typing.Optional[OpensearchDomainAdvancedSecurityOptions]:
        '''advanced_security_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#advanced_security_options OpensearchDomain#advanced_security_options}
        '''
        result = self._values.get("advanced_security_options")
        return typing.cast(typing.Optional[OpensearchDomainAdvancedSecurityOptions], result)

    @builtins.property
    def auto_tune_options(self) -> typing.Optional[OpensearchDomainAutoTuneOptions]:
        '''auto_tune_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#auto_tune_options OpensearchDomain#auto_tune_options}
        '''
        result = self._values.get("auto_tune_options")
        return typing.cast(typing.Optional[OpensearchDomainAutoTuneOptions], result)

    @builtins.property
    def cluster_config(self) -> typing.Optional[OpensearchDomainClusterConfig]:
        '''cluster_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#cluster_config OpensearchDomain#cluster_config}
        '''
        result = self._values.get("cluster_config")
        return typing.cast(typing.Optional[OpensearchDomainClusterConfig], result)

    @builtins.property
    def cognito_options(self) -> typing.Optional[OpensearchDomainCognitoOptions]:
        '''cognito_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#cognito_options OpensearchDomain#cognito_options}
        '''
        result = self._values.get("cognito_options")
        return typing.cast(typing.Optional[OpensearchDomainCognitoOptions], result)

    @builtins.property
    def domain_endpoint_options(
        self,
    ) -> typing.Optional["OpensearchDomainDomainEndpointOptions"]:
        '''domain_endpoint_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#domain_endpoint_options OpensearchDomain#domain_endpoint_options}
        '''
        result = self._values.get("domain_endpoint_options")
        return typing.cast(typing.Optional["OpensearchDomainDomainEndpointOptions"], result)

    @builtins.property
    def ebs_options(self) -> typing.Optional["OpensearchDomainEbsOptions"]:
        '''ebs_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#ebs_options OpensearchDomain#ebs_options}
        '''
        result = self._values.get("ebs_options")
        return typing.cast(typing.Optional["OpensearchDomainEbsOptions"], result)

    @builtins.property
    def encrypt_at_rest(self) -> typing.Optional["OpensearchDomainEncryptAtRest"]:
        '''encrypt_at_rest block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#encrypt_at_rest OpensearchDomain#encrypt_at_rest}
        '''
        result = self._values.get("encrypt_at_rest")
        return typing.cast(typing.Optional["OpensearchDomainEncryptAtRest"], result)

    @builtins.property
    def engine_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#engine_version OpensearchDomain#engine_version}.'''
        result = self._values.get("engine_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#id OpensearchDomain#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_publishing_options(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["OpensearchDomainLogPublishingOptions"]]]:
        '''log_publishing_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#log_publishing_options OpensearchDomain#log_publishing_options}
        '''
        result = self._values.get("log_publishing_options")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["OpensearchDomainLogPublishingOptions"]]], result)

    @builtins.property
    def node_to_node_encryption(
        self,
    ) -> typing.Optional["OpensearchDomainNodeToNodeEncryption"]:
        '''node_to_node_encryption block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#node_to_node_encryption OpensearchDomain#node_to_node_encryption}
        '''
        result = self._values.get("node_to_node_encryption")
        return typing.cast(typing.Optional["OpensearchDomainNodeToNodeEncryption"], result)

    @builtins.property
    def snapshot_options(self) -> typing.Optional["OpensearchDomainSnapshotOptions"]:
        '''snapshot_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#snapshot_options OpensearchDomain#snapshot_options}
        '''
        result = self._values.get("snapshot_options")
        return typing.cast(typing.Optional["OpensearchDomainSnapshotOptions"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#tags OpensearchDomain#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#tags_all OpensearchDomain#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["OpensearchDomainTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#timeouts OpensearchDomain#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["OpensearchDomainTimeouts"], result)

    @builtins.property
    def vpc_options(self) -> typing.Optional["OpensearchDomainVpcOptions"]:
        '''vpc_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#vpc_options OpensearchDomain#vpc_options}
        '''
        result = self._values.get("vpc_options")
        return typing.cast(typing.Optional["OpensearchDomainVpcOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpensearchDomainConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.opensearchDomain.OpensearchDomainDomainEndpointOptions",
    jsii_struct_bases=[],
    name_mapping={
        "custom_endpoint": "customEndpoint",
        "custom_endpoint_certificate_arn": "customEndpointCertificateArn",
        "custom_endpoint_enabled": "customEndpointEnabled",
        "enforce_https": "enforceHttps",
        "tls_security_policy": "tlsSecurityPolicy",
    },
)
class OpensearchDomainDomainEndpointOptions:
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
        :param custom_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#custom_endpoint OpensearchDomain#custom_endpoint}.
        :param custom_endpoint_certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#custom_endpoint_certificate_arn OpensearchDomain#custom_endpoint_certificate_arn}.
        :param custom_endpoint_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#custom_endpoint_enabled OpensearchDomain#custom_endpoint_enabled}.
        :param enforce_https: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#enforce_https OpensearchDomain#enforce_https}.
        :param tls_security_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#tls_security_policy OpensearchDomain#tls_security_policy}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a481a2ea6c26ecfe6df74dfdd00fc0aa89ed787a91133f01f4e2c6ae45460638)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#custom_endpoint OpensearchDomain#custom_endpoint}.'''
        result = self._values.get("custom_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_endpoint_certificate_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#custom_endpoint_certificate_arn OpensearchDomain#custom_endpoint_certificate_arn}.'''
        result = self._values.get("custom_endpoint_certificate_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_endpoint_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#custom_endpoint_enabled OpensearchDomain#custom_endpoint_enabled}.'''
        result = self._values.get("custom_endpoint_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enforce_https(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#enforce_https OpensearchDomain#enforce_https}.'''
        result = self._values.get("enforce_https")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def tls_security_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#tls_security_policy OpensearchDomain#tls_security_policy}.'''
        result = self._values.get("tls_security_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpensearchDomainDomainEndpointOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpensearchDomainDomainEndpointOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opensearchDomain.OpensearchDomainDomainEndpointOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__85e290a944a57b8a6cbb3182f58ceddc0d461024f373bfdcf2aeac15467a6ecb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a34279941ee07bc43152c17e8123ba40cea8b70d16800cfbd21a42cf7038b046)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="customEndpointCertificateArn")
    def custom_endpoint_certificate_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customEndpointCertificateArn"))

    @custom_endpoint_certificate_arn.setter
    def custom_endpoint_certificate_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad0076af8950487fb9e05c94a3f59f5308f329a771f0b142ddbbffe9b4edcdce)
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
            type_hints = typing.get_type_hints(_typecheckingstub__51de53d0e6050d4cd69cd3001fdd508dd5bb27a2c1c3b3b8671a8cfe541cbd60)
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
            type_hints = typing.get_type_hints(_typecheckingstub__df6522c1890d06423d761485bd692277bb820b0e07cb47e85d1f22da8640eefd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enforceHttps", value)

    @builtins.property
    @jsii.member(jsii_name="tlsSecurityPolicy")
    def tls_security_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsSecurityPolicy"))

    @tls_security_policy.setter
    def tls_security_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6b5a011faa20042688e4e884281f82e4f27ad4592dc2f696216118e4e2f0557)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsSecurityPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OpensearchDomainDomainEndpointOptions]:
        return typing.cast(typing.Optional[OpensearchDomainDomainEndpointOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpensearchDomainDomainEndpointOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d28c2c2bf4de0f9ebb85f7d28553eca133036ac3b572dc2fe2396954465badc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.opensearchDomain.OpensearchDomainEbsOptions",
    jsii_struct_bases=[],
    name_mapping={
        "ebs_enabled": "ebsEnabled",
        "iops": "iops",
        "throughput": "throughput",
        "volume_size": "volumeSize",
        "volume_type": "volumeType",
    },
)
class OpensearchDomainEbsOptions:
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
        :param ebs_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#ebs_enabled OpensearchDomain#ebs_enabled}.
        :param iops: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#iops OpensearchDomain#iops}.
        :param throughput: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#throughput OpensearchDomain#throughput}.
        :param volume_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#volume_size OpensearchDomain#volume_size}.
        :param volume_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#volume_type OpensearchDomain#volume_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__128e69b2b7faaaea88e5356416be7adcacedd923c6173d9e2c55a019e17d9943)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#ebs_enabled OpensearchDomain#ebs_enabled}.'''
        result = self._values.get("ebs_enabled")
        assert result is not None, "Required property 'ebs_enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def iops(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#iops OpensearchDomain#iops}.'''
        result = self._values.get("iops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def throughput(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#throughput OpensearchDomain#throughput}.'''
        result = self._values.get("throughput")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volume_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#volume_size OpensearchDomain#volume_size}.'''
        result = self._values.get("volume_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def volume_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#volume_type OpensearchDomain#volume_type}.'''
        result = self._values.get("volume_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpensearchDomainEbsOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpensearchDomainEbsOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opensearchDomain.OpensearchDomainEbsOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cb390da6264d9d7e57dac0e10321054ae348e10281b44abd3dd5b560898f4bef)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d53b8b9b356662dd0eac0c2cdd30e4e727d8a747f12599fba4aaafea50f7dbbc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ebsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="iops")
    def iops(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iops"))

    @iops.setter
    def iops(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__540eca8610447a215e4ae35858aeae300cc4581294bc2d6aeca7842528308f89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iops", value)

    @builtins.property
    @jsii.member(jsii_name="throughput")
    def throughput(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "throughput"))

    @throughput.setter
    def throughput(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35626a25806142d00de73ae151e49829d31e200e8b1876c777ee88888b868281)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "throughput", value)

    @builtins.property
    @jsii.member(jsii_name="volumeSize")
    def volume_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "volumeSize"))

    @volume_size.setter
    def volume_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a65b45e8a762bb7da552bc6dda822f6002c9491342b421acf2fd6daed9d8c914)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeSize", value)

    @builtins.property
    @jsii.member(jsii_name="volumeType")
    def volume_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeType"))

    @volume_type.setter
    def volume_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a27ad4ea9d7dd90632b326f09c7ba307f388a5324a5d53790a46398b4f37c4d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OpensearchDomainEbsOptions]:
        return typing.cast(typing.Optional[OpensearchDomainEbsOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpensearchDomainEbsOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b36959087e470ba015ecfed181f2799b4fdb9e009ef291190482e3ccf24cd79f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.opensearchDomain.OpensearchDomainEncryptAtRest",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "kms_key_id": "kmsKeyId"},
)
class OpensearchDomainEncryptAtRest:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        kms_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#enabled OpensearchDomain#enabled}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#kms_key_id OpensearchDomain#kms_key_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07a05bb7fd50049f0d3c9f42b76f1c991bb4c0710db13faec10b7fd7c1e11a5d)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled": enabled,
        }
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#enabled OpensearchDomain#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#kms_key_id OpensearchDomain#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpensearchDomainEncryptAtRest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpensearchDomainEncryptAtRestOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opensearchDomain.OpensearchDomainEncryptAtRestOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b634bbc336ad8d339b1a5c6def865bfbb3f1acf61c9cd5bbfd818ebfd1ba51e6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5887fd79fd013722d52386bc4477c9f91dd201d365f33e3dd2065e3d919cee68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8ba96a39357d37022c585dfdd972729ccc145c7713971140e2aab666ac5259d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OpensearchDomainEncryptAtRest]:
        return typing.cast(typing.Optional[OpensearchDomainEncryptAtRest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpensearchDomainEncryptAtRest],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58dbaf3cd611006fc86db1eb8512da719a4b171787c136bf88383041c8e8131b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.opensearchDomain.OpensearchDomainLogPublishingOptions",
    jsii_struct_bases=[],
    name_mapping={
        "cloudwatch_log_group_arn": "cloudwatchLogGroupArn",
        "log_type": "logType",
        "enabled": "enabled",
    },
)
class OpensearchDomainLogPublishingOptions:
    def __init__(
        self,
        *,
        cloudwatch_log_group_arn: builtins.str,
        log_type: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param cloudwatch_log_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#cloudwatch_log_group_arn OpensearchDomain#cloudwatch_log_group_arn}.
        :param log_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#log_type OpensearchDomain#log_type}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#enabled OpensearchDomain#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64fbf5664718e975dce76f146efe5929688e410adb04f1dbc38dfeec73cbe741)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#cloudwatch_log_group_arn OpensearchDomain#cloudwatch_log_group_arn}.'''
        result = self._values.get("cloudwatch_log_group_arn")
        assert result is not None, "Required property 'cloudwatch_log_group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#log_type OpensearchDomain#log_type}.'''
        result = self._values.get("log_type")
        assert result is not None, "Required property 'log_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#enabled OpensearchDomain#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpensearchDomainLogPublishingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpensearchDomainLogPublishingOptionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opensearchDomain.OpensearchDomainLogPublishingOptionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__db3cf701e12de8187663d2bec0fa8cfb54ba6311af211cda949ef37c4c78aa65)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "OpensearchDomainLogPublishingOptionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1e18e00b1f1d3ebcd365c45cb5b0aadf71714d2f8250763a492cbf38559a158)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("OpensearchDomainLogPublishingOptionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5ec05b8f6458a364e5c6b4e3cd4fb35ffcf332f91eefe92b33cbbdfc3f0a9fb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b99fee39afc7acfb8d8d3d13359db4ee65f1edafbca3c44012dc0a61d7cf1eb7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5cab6f02d00d1f2a574278f712cfc9c448c3c3441d7c3a2a865ec7b52171b313)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpensearchDomainLogPublishingOptions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpensearchDomainLogPublishingOptions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpensearchDomainLogPublishingOptions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7662dd8efa1907acc9e2e7ed00f0dcdeca8abecab7b312017f97274e7d0d4e0f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OpensearchDomainLogPublishingOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opensearchDomain.OpensearchDomainLogPublishingOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c4c256ea7f67898c33ffb8e6157b21c43f8f3c8baef4e3aef893e96cab6c68da)
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
            type_hints = typing.get_type_hints(_typecheckingstub__12a13440b8a912404dd560676b422c79d0014fe99852121c84bb8753c025c78c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1660bf675411784e4dd4a0ff205c2ba235126d05bd34e2f497088a1eef990075)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="logType")
    def log_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logType"))

    @log_type.setter
    def log_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__240aab396853f34af9a6da953cbe19e80414446cbe77f10424948fc7baa4d9c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OpensearchDomainLogPublishingOptions, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OpensearchDomainLogPublishingOptions, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OpensearchDomainLogPublishingOptions, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64712fc46ea9ff6eebb30031a3fd00559076ed395d93203cff101a2df2405cb1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.opensearchDomain.OpensearchDomainNodeToNodeEncryption",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class OpensearchDomainNodeToNodeEncryption:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#enabled OpensearchDomain#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecf13ba91843ec9f9b540a26f7e97270d429309787b96b6f95c25b4b61b77169)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled": enabled,
        }

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#enabled OpensearchDomain#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpensearchDomainNodeToNodeEncryption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpensearchDomainNodeToNodeEncryptionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opensearchDomain.OpensearchDomainNodeToNodeEncryptionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0b1a1f733b02d8f393a1c23b08d988347cc1c182f05da456cefd2b007c6eb426)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b09ce538e712e41fa7b4cb2ddaa13825fd09615a59d0e5907f7736c8fbae7309)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OpensearchDomainNodeToNodeEncryption]:
        return typing.cast(typing.Optional[OpensearchDomainNodeToNodeEncryption], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpensearchDomainNodeToNodeEncryption],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15eb1be025dbaa01505962c7e1ed7bee928e239b7215c5b20de9d595a2b6ca12)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.opensearchDomain.OpensearchDomainSnapshotOptions",
    jsii_struct_bases=[],
    name_mapping={"automated_snapshot_start_hour": "automatedSnapshotStartHour"},
)
class OpensearchDomainSnapshotOptions:
    def __init__(self, *, automated_snapshot_start_hour: jsii.Number) -> None:
        '''
        :param automated_snapshot_start_hour: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#automated_snapshot_start_hour OpensearchDomain#automated_snapshot_start_hour}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67f96926ff0aa516bdd6f197da8551b74fa69a47ba2d02ee39f2a45a06643d8f)
            check_type(argname="argument automated_snapshot_start_hour", value=automated_snapshot_start_hour, expected_type=type_hints["automated_snapshot_start_hour"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "automated_snapshot_start_hour": automated_snapshot_start_hour,
        }

    @builtins.property
    def automated_snapshot_start_hour(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#automated_snapshot_start_hour OpensearchDomain#automated_snapshot_start_hour}.'''
        result = self._values.get("automated_snapshot_start_hour")
        assert result is not None, "Required property 'automated_snapshot_start_hour' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpensearchDomainSnapshotOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpensearchDomainSnapshotOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opensearchDomain.OpensearchDomainSnapshotOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__077a7af36748dc61befd8fba462f94da967e76203417fc90b29b351652c9c22b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__add3711ca613ec699a0a2bfd28640fd83659bef67358bd8c83735f80ab9574cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "automatedSnapshotStartHour", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OpensearchDomainSnapshotOptions]:
        return typing.cast(typing.Optional[OpensearchDomainSnapshotOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpensearchDomainSnapshotOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7ab7e7ed3868a161090536ef9f18d90a3e99f4f09e51d1c63cd1dbac255c4d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.opensearchDomain.OpensearchDomainTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class OpensearchDomainTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#create OpensearchDomain#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#delete OpensearchDomain#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#update OpensearchDomain#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f70387e9a6f078be732a8630d70d17fa6fda52a57cb29f412b24df6b7869a19)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#create OpensearchDomain#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#delete OpensearchDomain#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#update OpensearchDomain#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpensearchDomainTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpensearchDomainTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opensearchDomain.OpensearchDomainTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c742449d4947ddb832c477e01e0b426f31b537bb63135ba0bab2944f0e4fe378)
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
            type_hints = typing.get_type_hints(_typecheckingstub__993ec8a687a1d85c93ca7f14df0f64a129cd4d834ae1769a553daa09c555408f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23306386e83ddbf13ded69ebbe7d32cf65dd11e670ac95461fa40470539d2d4b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b5eb3d62aacdfa3e177778397bf9a9df3c2896a32e8bf074ffdd8fcc5e00b90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[OpensearchDomainTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[OpensearchDomainTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[OpensearchDomainTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4693db2e2ce2f908942279686405f293a1b2e6ab6257f68f7f4ad1b3939b963e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.opensearchDomain.OpensearchDomainVpcOptions",
    jsii_struct_bases=[],
    name_mapping={"security_group_ids": "securityGroupIds", "subnet_ids": "subnetIds"},
)
class OpensearchDomainVpcOptions:
    def __init__(
        self,
        *,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#security_group_ids OpensearchDomain#security_group_ids}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#subnet_ids OpensearchDomain#subnet_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02f1e4b2b5437e421fbc215f37e521ed821efad1c0e50f3a402becd6cf12786e)
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if subnet_ids is not None:
            self._values["subnet_ids"] = subnet_ids

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#security_group_ids OpensearchDomain#security_group_ids}.'''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/opensearch_domain#subnet_ids OpensearchDomain#subnet_ids}.'''
        result = self._values.get("subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpensearchDomainVpcOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpensearchDomainVpcOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.opensearchDomain.OpensearchDomainVpcOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ec9b3137899bec35ea251ff9a95f0d2688d167e358aec8bf5c27362511027dca)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1dfd336526e0042e6f13e40d1a96deb84309b5c2af266ef655cdef28150e0b74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7ddb33cad569a1383b74dfb2e3957ac14c3ac8a37c8696ac013a2b40f390a8c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OpensearchDomainVpcOptions]:
        return typing.cast(typing.Optional[OpensearchDomainVpcOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpensearchDomainVpcOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb459a93699c3ebccc471a1a1f027f4648e1ff77782a23d38251f1fd28b71650)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "OpensearchDomain",
    "OpensearchDomainAdvancedSecurityOptions",
    "OpensearchDomainAdvancedSecurityOptionsMasterUserOptions",
    "OpensearchDomainAdvancedSecurityOptionsMasterUserOptionsOutputReference",
    "OpensearchDomainAdvancedSecurityOptionsOutputReference",
    "OpensearchDomainAutoTuneOptions",
    "OpensearchDomainAutoTuneOptionsMaintenanceSchedule",
    "OpensearchDomainAutoTuneOptionsMaintenanceScheduleDuration",
    "OpensearchDomainAutoTuneOptionsMaintenanceScheduleDurationOutputReference",
    "OpensearchDomainAutoTuneOptionsMaintenanceScheduleList",
    "OpensearchDomainAutoTuneOptionsMaintenanceScheduleOutputReference",
    "OpensearchDomainAutoTuneOptionsOutputReference",
    "OpensearchDomainClusterConfig",
    "OpensearchDomainClusterConfigColdStorageOptions",
    "OpensearchDomainClusterConfigColdStorageOptionsOutputReference",
    "OpensearchDomainClusterConfigOutputReference",
    "OpensearchDomainClusterConfigZoneAwarenessConfig",
    "OpensearchDomainClusterConfigZoneAwarenessConfigOutputReference",
    "OpensearchDomainCognitoOptions",
    "OpensearchDomainCognitoOptionsOutputReference",
    "OpensearchDomainConfig",
    "OpensearchDomainDomainEndpointOptions",
    "OpensearchDomainDomainEndpointOptionsOutputReference",
    "OpensearchDomainEbsOptions",
    "OpensearchDomainEbsOptionsOutputReference",
    "OpensearchDomainEncryptAtRest",
    "OpensearchDomainEncryptAtRestOutputReference",
    "OpensearchDomainLogPublishingOptions",
    "OpensearchDomainLogPublishingOptionsList",
    "OpensearchDomainLogPublishingOptionsOutputReference",
    "OpensearchDomainNodeToNodeEncryption",
    "OpensearchDomainNodeToNodeEncryptionOutputReference",
    "OpensearchDomainSnapshotOptions",
    "OpensearchDomainSnapshotOptionsOutputReference",
    "OpensearchDomainTimeouts",
    "OpensearchDomainTimeoutsOutputReference",
    "OpensearchDomainVpcOptions",
    "OpensearchDomainVpcOptionsOutputReference",
]

publication.publish()

def _typecheckingstub__3eec919b45d55b7ca41424513ec67823b95c9ffc69cff46ce5a033b162f2aee6(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    domain_name: builtins.str,
    access_policies: typing.Optional[builtins.str] = None,
    advanced_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    advanced_security_options: typing.Optional[typing.Union[OpensearchDomainAdvancedSecurityOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    auto_tune_options: typing.Optional[typing.Union[OpensearchDomainAutoTuneOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    cluster_config: typing.Optional[typing.Union[OpensearchDomainClusterConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    cognito_options: typing.Optional[typing.Union[OpensearchDomainCognitoOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    domain_endpoint_options: typing.Optional[typing.Union[OpensearchDomainDomainEndpointOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    ebs_options: typing.Optional[typing.Union[OpensearchDomainEbsOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    encrypt_at_rest: typing.Optional[typing.Union[OpensearchDomainEncryptAtRest, typing.Dict[builtins.str, typing.Any]]] = None,
    engine_version: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    log_publishing_options: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[OpensearchDomainLogPublishingOptions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    node_to_node_encryption: typing.Optional[typing.Union[OpensearchDomainNodeToNodeEncryption, typing.Dict[builtins.str, typing.Any]]] = None,
    snapshot_options: typing.Optional[typing.Union[OpensearchDomainSnapshotOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[OpensearchDomainTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc_options: typing.Optional[typing.Union[OpensearchDomainVpcOptions, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__cdba9f8a5d4fae2baba31a378f7e1df936d7fae7e90d2c6d75c0896ed32f5da6(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[OpensearchDomainLogPublishingOptions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44f2621ddf2663f5403545486d7b83097e0852adea2b03153f0b4a1148cf2ef6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cec8ae3c5c509e3cd49b65ca19a3c915bf7ee3ab2e430e51dd770fa908d3d40(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0aa358ea527377fb52dd7fd6f5825ee3db935773f3479b386b584e1b55e2af22(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dbf20a3ebd3c252792daf251397b7234615eca21a6a0a602af3fb7466152d19(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d15704cd50b86c41b78761823cd9ed8f9671f535064c74a0b69fd102d6eea18c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f414675affec435a6c58f97d4fca8bcff50f27a11c4eeba626d073e9bc5f8a58(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be99ef674767ba442079ebef29df760414cbdb663c0e46fb55f36490300baf12(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e93fff473e9af3e1fc261985781bab87b5cd2aed876b9bb1d65d7c5a8db48f9b(
    *,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    anonymous_auth_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    internal_user_database_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    master_user_options: typing.Optional[typing.Union[OpensearchDomainAdvancedSecurityOptionsMasterUserOptions, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e2afa0275fdac20fc9f041b591d770b6f8e2885d3705c9ecff3eba0a51f810d(
    *,
    master_user_arn: typing.Optional[builtins.str] = None,
    master_user_name: typing.Optional[builtins.str] = None,
    master_user_password: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1774a8a6714f3c4ed4ccf0d0f0d71b98f5e2434c26e09154cc73fc07c11061b0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f971bd74ea3b8abea38d7a3c4849a3c67db82f159ded42b8f3608948f138806(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af27b520f20ea06e9e58f82e3f622aa135d81bd0bd19d51d11e6b392b37d686e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74a79ce2fa2ab8fc7515f6f92675b6db81a6a8dc34252a2c27cb9982ec9a22f0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c4d90b14668d819eccd9a85b09de01b53face6722d031ca3b616cfb6adfe366(
    value: typing.Optional[OpensearchDomainAdvancedSecurityOptionsMasterUserOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d57e4923f2da451b53b0725d3f0322a29de9590349d3fd7014a65921da15e1a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ac8d37cf4f05e24826f81a418531b18b43dc316ed7b04782795ea23d753235a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fce51da7de836da65c1d47187c4ee6b0a38f712fedb94684c18ba0d6c12e75b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d8aa76bf975e2e0b4c7630c7737e22b2160a0dc3ecc694b356cd2fd99bed325(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bfa7665913d961c8f325e0581122bd30187626e2ef015a9f291fa15770954f0(
    value: typing.Optional[OpensearchDomainAdvancedSecurityOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b074447e70909491001362252fe10821830b0262456b33cad218c923f1d261d(
    *,
    desired_state: builtins.str,
    maintenance_schedule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[OpensearchDomainAutoTuneOptionsMaintenanceSchedule, typing.Dict[builtins.str, typing.Any]]]]] = None,
    rollback_on_disable: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab45bf853f73598a6ccf997b973a1582b533772d2441a3fe194b0a5ca15ae06e(
    *,
    cron_expression_for_recurrence: builtins.str,
    duration: typing.Union[OpensearchDomainAutoTuneOptionsMaintenanceScheduleDuration, typing.Dict[builtins.str, typing.Any]],
    start_at: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdbc09fc77e37a5f756a2f3616e2b07a0acd90dd45847abb5fd52248d110d05b(
    *,
    unit: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__062a67e0d9f401663c9f66428066fd977678ea0b751249478a371b79b69c113f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9af5e3b3c766e785dc29e80eda9caeff30e35b71bea6da895b67f3d61c870491(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0342c85f45208f25ba40b77a253030a716c151f7ffa254a1647abbbf785479b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__532e37649b5235109a5f03529d34edf29b8e5ac418393124aed495954bbdf40e(
    value: typing.Optional[OpensearchDomainAutoTuneOptionsMaintenanceScheduleDuration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__808c288ab47e3aaad8b60a9c2a7059b1a36f4e4ddfc508127e965db76d37821c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32ec2d59231b5e405750686faa220f24ec8d02fcf56c9647520f8ec13b25db5e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bd0390b7a1602f3a3e34cfee41dd46a24a4c5ff4afac2b21c74deba2e8eb7a1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f153fcca8df97bb2194d0ff8ff3f8eb7feb339b06532390fe279fb0f92dc12ea(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a64407e4dfbd55f772e623fcd98093920f6b8a859afb4d07b1abb4047f0062dd(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d67babed7a54fe97c2c4bc73115ffe901b786d80270c69b27abaf90ddeddca6c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpensearchDomainAutoTuneOptionsMaintenanceSchedule]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8af68c62f31a3feca4716ae0d64061d67c03201b66197199325baf4e0655fedb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69a2d6dd7115f13601122e5de25dbf48624703cb3e5d565a2e1fb39e8ab3f7ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d4e5d6973f1d4069c5f2b54cd0acf8d04a3db69f95122cb2bb951f526fcab8a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac43099682dfe2e261c67d6b772940ee1dc18dc268505e6deed521e8f7bd7c2e(
    value: typing.Optional[typing.Union[OpensearchDomainAutoTuneOptionsMaintenanceSchedule, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17851dcb7db7b8b73ecf9a7100fb4b8c1c60f1b08690ff7e172acbcbb5085b1f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea7b412d362958803bff269a7567e0f0cedaa97dbce5ee1a1d7f1f31a813509a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[OpensearchDomainAutoTuneOptionsMaintenanceSchedule, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10c129d2eac2686de2d8efed60983ec6560b006afa965079bc732137d330429b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff612dd31473d8e3e9f74f6a28274b71a5f188ea45cde85cf99b25d990af35b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e726e2949e470a994c7bf6766385d0c73538c6677e0ad379cd002ea353bda5f2(
    value: typing.Optional[OpensearchDomainAutoTuneOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e8411e07992a73a9fa186e95118bf9daf8f7371c6879ceeb1620d56122e97a6(
    *,
    cold_storage_options: typing.Optional[typing.Union[OpensearchDomainClusterConfigColdStorageOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    dedicated_master_count: typing.Optional[jsii.Number] = None,
    dedicated_master_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    dedicated_master_type: typing.Optional[builtins.str] = None,
    instance_count: typing.Optional[jsii.Number] = None,
    instance_type: typing.Optional[builtins.str] = None,
    warm_count: typing.Optional[jsii.Number] = None,
    warm_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    warm_type: typing.Optional[builtins.str] = None,
    zone_awareness_config: typing.Optional[typing.Union[OpensearchDomainClusterConfigZoneAwarenessConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    zone_awareness_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6f679694137ede29004677107a0d83034fd0a8d92e2b24c1b6611f2b8505058(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3af9e7a62f6142b795de219833c35fecfc628e538f828683082fe3bc99c89350(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d05b8fed77b36618ac20c6837e16f73aa592bb3c678e1afd84200756bbdd785(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec71b183fa6e49eff8cc80b803f5f62dc81da36733efb3bc6e4bf608e6777129(
    value: typing.Optional[OpensearchDomainClusterConfigColdStorageOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35195fcac4e7e4a00e95509a8f80693e1dd0e1a73bc860cca8a267100a701496(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe4e89c479869ee71fd60000738272a04f894ec6d1cb1e3b61d7c55d8e03b7be(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88da7401e66d3b1d575785c02ccab83cd817aa2be0457f1fbe844102df87f56e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b646b0fb23a4ab6fdbb8c14eb66a3f13be1db837f4321d424296b88f6350e2d9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2f585da7bb8f8a0b914b86b905efc677b356468c743b8e8b5ed17cf12ea85f3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35f954c1acf223d0e7f4c82a434b3b7eab3103886ef0d0013a20c369232ccd35(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e2df952d93da8c659820a9148d1b7a0215b684db50012f719a1daaaf143cd2c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2019f61bbcd29b457e9d57e1f099f37d0a9d272a90cc701d3f783df0b68b739(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d144c56029757b44d8335e5b450a5bc39574ab12896e986c77dd6b5234b6dd6c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d9438ff45986e60f09fdc5872f515477b376c50671da3ec621d3425180c7aaf(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__116b8f76b85b5a133780556611dd0694160a1551b3846d101dcc65fd1576da2a(
    value: typing.Optional[OpensearchDomainClusterConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3acd43b0418006b6d43ebfb4f78f881127e6e7dacacb6db11d66888a1d845dac(
    *,
    availability_zone_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f72dd99c5e5cef476fb453a2b1e9c266df81c065e02fd3971d8317674c9d32a5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3db1758006a01189b8ba1cdf7d43be4e4a7a4fff395bd45196fd73ecf32ede02(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26ce3bb0b6649c7462d41f0f3079498dd7c6902083d37c83a59c6b19079a4bcc(
    value: typing.Optional[OpensearchDomainClusterConfigZoneAwarenessConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82ba46ecdd55fceeb74cee551b76c3087d9185eb50fc6c127ebd2d9443d86a68(
    *,
    identity_pool_id: builtins.str,
    role_arn: builtins.str,
    user_pool_id: builtins.str,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9b3bf6c9b4f8c3e9e87ec6ec4aa85bb652a3df058ba9291f204f28da0518637(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7705533ecbfabc38d20199c02ac6e3acb8e88769ec6c0c521a3619e62aaaabc(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fded7922fd6e2bc25c6e3f51dc3292e86dd02fbaf2edda8274b66effd29be08(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__443a8e96af0473350199a90d06a1e6529293bcf7e9f1ef7c60ca65bc6d4781db(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02f428e6c77b8c0801003de15797402d76a6dced332ad366c7cbab7e4bc1ddc6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72528ecee96b72ce27123e9786d6e458f75d6ccfd7b030d021498540afaeec84(
    value: typing.Optional[OpensearchDomainCognitoOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7d8e58dc8b23bf0478a5796d7265063a6026a196acb9b811ed2a94fb3081373(
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
    advanced_security_options: typing.Optional[typing.Union[OpensearchDomainAdvancedSecurityOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    auto_tune_options: typing.Optional[typing.Union[OpensearchDomainAutoTuneOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    cluster_config: typing.Optional[typing.Union[OpensearchDomainClusterConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    cognito_options: typing.Optional[typing.Union[OpensearchDomainCognitoOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    domain_endpoint_options: typing.Optional[typing.Union[OpensearchDomainDomainEndpointOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    ebs_options: typing.Optional[typing.Union[OpensearchDomainEbsOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    encrypt_at_rest: typing.Optional[typing.Union[OpensearchDomainEncryptAtRest, typing.Dict[builtins.str, typing.Any]]] = None,
    engine_version: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    log_publishing_options: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[OpensearchDomainLogPublishingOptions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    node_to_node_encryption: typing.Optional[typing.Union[OpensearchDomainNodeToNodeEncryption, typing.Dict[builtins.str, typing.Any]]] = None,
    snapshot_options: typing.Optional[typing.Union[OpensearchDomainSnapshotOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[OpensearchDomainTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc_options: typing.Optional[typing.Union[OpensearchDomainVpcOptions, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a481a2ea6c26ecfe6df74dfdd00fc0aa89ed787a91133f01f4e2c6ae45460638(
    *,
    custom_endpoint: typing.Optional[builtins.str] = None,
    custom_endpoint_certificate_arn: typing.Optional[builtins.str] = None,
    custom_endpoint_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enforce_https: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tls_security_policy: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85e290a944a57b8a6cbb3182f58ceddc0d461024f373bfdcf2aeac15467a6ecb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a34279941ee07bc43152c17e8123ba40cea8b70d16800cfbd21a42cf7038b046(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad0076af8950487fb9e05c94a3f59f5308f329a771f0b142ddbbffe9b4edcdce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51de53d0e6050d4cd69cd3001fdd508dd5bb27a2c1c3b3b8671a8cfe541cbd60(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df6522c1890d06423d761485bd692277bb820b0e07cb47e85d1f22da8640eefd(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6b5a011faa20042688e4e884281f82e4f27ad4592dc2f696216118e4e2f0557(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d28c2c2bf4de0f9ebb85f7d28553eca133036ac3b572dc2fe2396954465badc(
    value: typing.Optional[OpensearchDomainDomainEndpointOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__128e69b2b7faaaea88e5356416be7adcacedd923c6173d9e2c55a019e17d9943(
    *,
    ebs_enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    iops: typing.Optional[jsii.Number] = None,
    throughput: typing.Optional[jsii.Number] = None,
    volume_size: typing.Optional[jsii.Number] = None,
    volume_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb390da6264d9d7e57dac0e10321054ae348e10281b44abd3dd5b560898f4bef(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d53b8b9b356662dd0eac0c2cdd30e4e727d8a747f12599fba4aaafea50f7dbbc(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__540eca8610447a215e4ae35858aeae300cc4581294bc2d6aeca7842528308f89(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35626a25806142d00de73ae151e49829d31e200e8b1876c777ee88888b868281(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a65b45e8a762bb7da552bc6dda822f6002c9491342b421acf2fd6daed9d8c914(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a27ad4ea9d7dd90632b326f09c7ba307f388a5324a5d53790a46398b4f37c4d5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b36959087e470ba015ecfed181f2799b4fdb9e009ef291190482e3ccf24cd79f(
    value: typing.Optional[OpensearchDomainEbsOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07a05bb7fd50049f0d3c9f42b76f1c991bb4c0710db13faec10b7fd7c1e11a5d(
    *,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    kms_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b634bbc336ad8d339b1a5c6def865bfbb3f1acf61c9cd5bbfd818ebfd1ba51e6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5887fd79fd013722d52386bc4477c9f91dd201d365f33e3dd2065e3d919cee68(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8ba96a39357d37022c585dfdd972729ccc145c7713971140e2aab666ac5259d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58dbaf3cd611006fc86db1eb8512da719a4b171787c136bf88383041c8e8131b(
    value: typing.Optional[OpensearchDomainEncryptAtRest],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64fbf5664718e975dce76f146efe5929688e410adb04f1dbc38dfeec73cbe741(
    *,
    cloudwatch_log_group_arn: builtins.str,
    log_type: builtins.str,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db3cf701e12de8187663d2bec0fa8cfb54ba6311af211cda949ef37c4c78aa65(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1e18e00b1f1d3ebcd365c45cb5b0aadf71714d2f8250763a492cbf38559a158(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5ec05b8f6458a364e5c6b4e3cd4fb35ffcf332f91eefe92b33cbbdfc3f0a9fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b99fee39afc7acfb8d8d3d13359db4ee65f1edafbca3c44012dc0a61d7cf1eb7(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cab6f02d00d1f2a574278f712cfc9c448c3c3441d7c3a2a865ec7b52171b313(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7662dd8efa1907acc9e2e7ed00f0dcdeca8abecab7b312017f97274e7d0d4e0f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[OpensearchDomainLogPublishingOptions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4c256ea7f67898c33ffb8e6157b21c43f8f3c8baef4e3aef893e96cab6c68da(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12a13440b8a912404dd560676b422c79d0014fe99852121c84bb8753c025c78c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1660bf675411784e4dd4a0ff205c2ba235126d05bd34e2f497088a1eef990075(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__240aab396853f34af9a6da953cbe19e80414446cbe77f10424948fc7baa4d9c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64712fc46ea9ff6eebb30031a3fd00559076ed395d93203cff101a2df2405cb1(
    value: typing.Optional[typing.Union[OpensearchDomainLogPublishingOptions, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecf13ba91843ec9f9b540a26f7e97270d429309787b96b6f95c25b4b61b77169(
    *,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b1a1f733b02d8f393a1c23b08d988347cc1c182f05da456cefd2b007c6eb426(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b09ce538e712e41fa7b4cb2ddaa13825fd09615a59d0e5907f7736c8fbae7309(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15eb1be025dbaa01505962c7e1ed7bee928e239b7215c5b20de9d595a2b6ca12(
    value: typing.Optional[OpensearchDomainNodeToNodeEncryption],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67f96926ff0aa516bdd6f197da8551b74fa69a47ba2d02ee39f2a45a06643d8f(
    *,
    automated_snapshot_start_hour: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__077a7af36748dc61befd8fba462f94da967e76203417fc90b29b351652c9c22b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__add3711ca613ec699a0a2bfd28640fd83659bef67358bd8c83735f80ab9574cc(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7ab7e7ed3868a161090536ef9f18d90a3e99f4f09e51d1c63cd1dbac255c4d5(
    value: typing.Optional[OpensearchDomainSnapshotOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f70387e9a6f078be732a8630d70d17fa6fda52a57cb29f412b24df6b7869a19(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c742449d4947ddb832c477e01e0b426f31b537bb63135ba0bab2944f0e4fe378(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__993ec8a687a1d85c93ca7f14df0f64a129cd4d834ae1769a553daa09c555408f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23306386e83ddbf13ded69ebbe7d32cf65dd11e670ac95461fa40470539d2d4b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b5eb3d62aacdfa3e177778397bf9a9df3c2896a32e8bf074ffdd8fcc5e00b90(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4693db2e2ce2f908942279686405f293a1b2e6ab6257f68f7f4ad1b3939b963e(
    value: typing.Optional[typing.Union[OpensearchDomainTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02f1e4b2b5437e421fbc215f37e521ed821efad1c0e50f3a402becd6cf12786e(
    *,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec9b3137899bec35ea251ff9a95f0d2688d167e358aec8bf5c27362511027dca(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1dfd336526e0042e6f13e40d1a96deb84309b5c2af266ef655cdef28150e0b74(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7ddb33cad569a1383b74dfb2e3957ac14c3ac8a37c8696ac013a2b40f390a8c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb459a93699c3ebccc471a1a1f027f4648e1ff77782a23d38251f1fd28b71650(
    value: typing.Optional[OpensearchDomainVpcOptions],
) -> None:
    """Type checking stubs"""
    pass
