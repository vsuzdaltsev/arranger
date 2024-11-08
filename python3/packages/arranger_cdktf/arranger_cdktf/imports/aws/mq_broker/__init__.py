'''
# `aws_mq_broker`

Refer to the Terraform Registory for docs: [`aws_mq_broker`](https://www.terraform.io/docs/providers/aws/r/mq_broker).
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


class MqBroker(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.mqBroker.MqBroker",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/mq_broker aws_mq_broker}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        broker_name: builtins.str,
        engine_type: builtins.str,
        engine_version: builtins.str,
        host_instance_type: builtins.str,
        user: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["MqBrokerUser", typing.Dict[builtins.str, typing.Any]]]],
        apply_immediately: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        authentication_strategy: typing.Optional[builtins.str] = None,
        auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        configuration: typing.Optional[typing.Union["MqBrokerConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        deployment_mode: typing.Optional[builtins.str] = None,
        encryption_options: typing.Optional[typing.Union["MqBrokerEncryptionOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        ldap_server_metadata: typing.Optional[typing.Union["MqBrokerLdapServerMetadata", typing.Dict[builtins.str, typing.Any]]] = None,
        logs: typing.Optional[typing.Union["MqBrokerLogs", typing.Dict[builtins.str, typing.Any]]] = None,
        maintenance_window_start_time: typing.Optional[typing.Union["MqBrokerMaintenanceWindowStartTime", typing.Dict[builtins.str, typing.Any]]] = None,
        publicly_accessible: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        storage_type: typing.Optional[builtins.str] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["MqBrokerTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/mq_broker aws_mq_broker} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param broker_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#broker_name MqBroker#broker_name}.
        :param engine_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#engine_type MqBroker#engine_type}.
        :param engine_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#engine_version MqBroker#engine_version}.
        :param host_instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#host_instance_type MqBroker#host_instance_type}.
        :param user: user block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#user MqBroker#user}
        :param apply_immediately: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#apply_immediately MqBroker#apply_immediately}.
        :param authentication_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#authentication_strategy MqBroker#authentication_strategy}.
        :param auto_minor_version_upgrade: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#auto_minor_version_upgrade MqBroker#auto_minor_version_upgrade}.
        :param configuration: configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#configuration MqBroker#configuration}
        :param deployment_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#deployment_mode MqBroker#deployment_mode}.
        :param encryption_options: encryption_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#encryption_options MqBroker#encryption_options}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#id MqBroker#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ldap_server_metadata: ldap_server_metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#ldap_server_metadata MqBroker#ldap_server_metadata}
        :param logs: logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#logs MqBroker#logs}
        :param maintenance_window_start_time: maintenance_window_start_time block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#maintenance_window_start_time MqBroker#maintenance_window_start_time}
        :param publicly_accessible: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#publicly_accessible MqBroker#publicly_accessible}.
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#security_groups MqBroker#security_groups}.
        :param storage_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#storage_type MqBroker#storage_type}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#subnet_ids MqBroker#subnet_ids}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#tags MqBroker#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#tags_all MqBroker#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#timeouts MqBroker#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bf08c6f8c17dec98f70b3b7808f35aa6467448b93cf567f565d37beb7de90b6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MqBrokerConfig(
            broker_name=broker_name,
            engine_type=engine_type,
            engine_version=engine_version,
            host_instance_type=host_instance_type,
            user=user,
            apply_immediately=apply_immediately,
            authentication_strategy=authentication_strategy,
            auto_minor_version_upgrade=auto_minor_version_upgrade,
            configuration=configuration,
            deployment_mode=deployment_mode,
            encryption_options=encryption_options,
            id=id,
            ldap_server_metadata=ldap_server_metadata,
            logs=logs,
            maintenance_window_start_time=maintenance_window_start_time,
            publicly_accessible=publicly_accessible,
            security_groups=security_groups,
            storage_type=storage_type,
            subnet_ids=subnet_ids,
            tags=tags,
            tags_all=tags_all,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putConfiguration")
    def put_configuration(
        self,
        *,
        id: typing.Optional[builtins.str] = None,
        revision: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#id MqBroker#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param revision: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#revision MqBroker#revision}.
        '''
        value = MqBrokerConfiguration(id=id, revision=revision)

        return typing.cast(None, jsii.invoke(self, "putConfiguration", [value]))

    @jsii.member(jsii_name="putEncryptionOptions")
    def put_encryption_options(
        self,
        *,
        kms_key_id: typing.Optional[builtins.str] = None,
        use_aws_owned_key: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#kms_key_id MqBroker#kms_key_id}.
        :param use_aws_owned_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#use_aws_owned_key MqBroker#use_aws_owned_key}.
        '''
        value = MqBrokerEncryptionOptions(
            kms_key_id=kms_key_id, use_aws_owned_key=use_aws_owned_key
        )

        return typing.cast(None, jsii.invoke(self, "putEncryptionOptions", [value]))

    @jsii.member(jsii_name="putLdapServerMetadata")
    def put_ldap_server_metadata(
        self,
        *,
        hosts: typing.Optional[typing.Sequence[builtins.str]] = None,
        role_base: typing.Optional[builtins.str] = None,
        role_name: typing.Optional[builtins.str] = None,
        role_search_matching: typing.Optional[builtins.str] = None,
        role_search_subtree: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        service_account_password: typing.Optional[builtins.str] = None,
        service_account_username: typing.Optional[builtins.str] = None,
        user_base: typing.Optional[builtins.str] = None,
        user_role_name: typing.Optional[builtins.str] = None,
        user_search_matching: typing.Optional[builtins.str] = None,
        user_search_subtree: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param hosts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#hosts MqBroker#hosts}.
        :param role_base: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#role_base MqBroker#role_base}.
        :param role_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#role_name MqBroker#role_name}.
        :param role_search_matching: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#role_search_matching MqBroker#role_search_matching}.
        :param role_search_subtree: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#role_search_subtree MqBroker#role_search_subtree}.
        :param service_account_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#service_account_password MqBroker#service_account_password}.
        :param service_account_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#service_account_username MqBroker#service_account_username}.
        :param user_base: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#user_base MqBroker#user_base}.
        :param user_role_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#user_role_name MqBroker#user_role_name}.
        :param user_search_matching: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#user_search_matching MqBroker#user_search_matching}.
        :param user_search_subtree: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#user_search_subtree MqBroker#user_search_subtree}.
        '''
        value = MqBrokerLdapServerMetadata(
            hosts=hosts,
            role_base=role_base,
            role_name=role_name,
            role_search_matching=role_search_matching,
            role_search_subtree=role_search_subtree,
            service_account_password=service_account_password,
            service_account_username=service_account_username,
            user_base=user_base,
            user_role_name=user_role_name,
            user_search_matching=user_search_matching,
            user_search_subtree=user_search_subtree,
        )

        return typing.cast(None, jsii.invoke(self, "putLdapServerMetadata", [value]))

    @jsii.member(jsii_name="putLogs")
    def put_logs(
        self,
        *,
        audit: typing.Optional[builtins.str] = None,
        general: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param audit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#audit MqBroker#audit}.
        :param general: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#general MqBroker#general}.
        '''
        value = MqBrokerLogs(audit=audit, general=general)

        return typing.cast(None, jsii.invoke(self, "putLogs", [value]))

    @jsii.member(jsii_name="putMaintenanceWindowStartTime")
    def put_maintenance_window_start_time(
        self,
        *,
        day_of_week: builtins.str,
        time_of_day: builtins.str,
        time_zone: builtins.str,
    ) -> None:
        '''
        :param day_of_week: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#day_of_week MqBroker#day_of_week}.
        :param time_of_day: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#time_of_day MqBroker#time_of_day}.
        :param time_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#time_zone MqBroker#time_zone}.
        '''
        value = MqBrokerMaintenanceWindowStartTime(
            day_of_week=day_of_week, time_of_day=time_of_day, time_zone=time_zone
        )

        return typing.cast(None, jsii.invoke(self, "putMaintenanceWindowStartTime", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#create MqBroker#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#delete MqBroker#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#update MqBroker#update}.
        '''
        value = MqBrokerTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putUser")
    def put_user(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["MqBrokerUser", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f656b1dde4ddfe0105381e9d5abe01bc7d3de204ea96170362aef251c2013f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUser", [value]))

    @jsii.member(jsii_name="resetApplyImmediately")
    def reset_apply_immediately(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplyImmediately", []))

    @jsii.member(jsii_name="resetAuthenticationStrategy")
    def reset_authentication_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthenticationStrategy", []))

    @jsii.member(jsii_name="resetAutoMinorVersionUpgrade")
    def reset_auto_minor_version_upgrade(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoMinorVersionUpgrade", []))

    @jsii.member(jsii_name="resetConfiguration")
    def reset_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfiguration", []))

    @jsii.member(jsii_name="resetDeploymentMode")
    def reset_deployment_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeploymentMode", []))

    @jsii.member(jsii_name="resetEncryptionOptions")
    def reset_encryption_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionOptions", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLdapServerMetadata")
    def reset_ldap_server_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLdapServerMetadata", []))

    @jsii.member(jsii_name="resetLogs")
    def reset_logs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogs", []))

    @jsii.member(jsii_name="resetMaintenanceWindowStartTime")
    def reset_maintenance_window_start_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaintenanceWindowStartTime", []))

    @jsii.member(jsii_name="resetPubliclyAccessible")
    def reset_publicly_accessible(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPubliclyAccessible", []))

    @jsii.member(jsii_name="resetSecurityGroups")
    def reset_security_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityGroups", []))

    @jsii.member(jsii_name="resetStorageType")
    def reset_storage_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageType", []))

    @jsii.member(jsii_name="resetSubnetIds")
    def reset_subnet_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetIds", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

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
    @jsii.member(jsii_name="configuration")
    def configuration(self) -> "MqBrokerConfigurationOutputReference":
        return typing.cast("MqBrokerConfigurationOutputReference", jsii.get(self, "configuration"))

    @builtins.property
    @jsii.member(jsii_name="encryptionOptions")
    def encryption_options(self) -> "MqBrokerEncryptionOptionsOutputReference":
        return typing.cast("MqBrokerEncryptionOptionsOutputReference", jsii.get(self, "encryptionOptions"))

    @builtins.property
    @jsii.member(jsii_name="instances")
    def instances(self) -> "MqBrokerInstancesList":
        return typing.cast("MqBrokerInstancesList", jsii.get(self, "instances"))

    @builtins.property
    @jsii.member(jsii_name="ldapServerMetadata")
    def ldap_server_metadata(self) -> "MqBrokerLdapServerMetadataOutputReference":
        return typing.cast("MqBrokerLdapServerMetadataOutputReference", jsii.get(self, "ldapServerMetadata"))

    @builtins.property
    @jsii.member(jsii_name="logs")
    def logs(self) -> "MqBrokerLogsOutputReference":
        return typing.cast("MqBrokerLogsOutputReference", jsii.get(self, "logs"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindowStartTime")
    def maintenance_window_start_time(
        self,
    ) -> "MqBrokerMaintenanceWindowStartTimeOutputReference":
        return typing.cast("MqBrokerMaintenanceWindowStartTimeOutputReference", jsii.get(self, "maintenanceWindowStartTime"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "MqBrokerTimeoutsOutputReference":
        return typing.cast("MqBrokerTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> "MqBrokerUserList":
        return typing.cast("MqBrokerUserList", jsii.get(self, "user"))

    @builtins.property
    @jsii.member(jsii_name="applyImmediatelyInput")
    def apply_immediately_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "applyImmediatelyInput"))

    @builtins.property
    @jsii.member(jsii_name="authenticationStrategyInput")
    def authentication_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authenticationStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="autoMinorVersionUpgradeInput")
    def auto_minor_version_upgrade_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "autoMinorVersionUpgradeInput"))

    @builtins.property
    @jsii.member(jsii_name="brokerNameInput")
    def broker_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "brokerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="configurationInput")
    def configuration_input(self) -> typing.Optional["MqBrokerConfiguration"]:
        return typing.cast(typing.Optional["MqBrokerConfiguration"], jsii.get(self, "configurationInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentModeInput")
    def deployment_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deploymentModeInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionOptionsInput")
    def encryption_options_input(self) -> typing.Optional["MqBrokerEncryptionOptions"]:
        return typing.cast(typing.Optional["MqBrokerEncryptionOptions"], jsii.get(self, "encryptionOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="engineTypeInput")
    def engine_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engineTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="engineVersionInput")
    def engine_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engineVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInstanceTypeInput")
    def host_instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInstanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ldapServerMetadataInput")
    def ldap_server_metadata_input(
        self,
    ) -> typing.Optional["MqBrokerLdapServerMetadata"]:
        return typing.cast(typing.Optional["MqBrokerLdapServerMetadata"], jsii.get(self, "ldapServerMetadataInput"))

    @builtins.property
    @jsii.member(jsii_name="logsInput")
    def logs_input(self) -> typing.Optional["MqBrokerLogs"]:
        return typing.cast(typing.Optional["MqBrokerLogs"], jsii.get(self, "logsInput"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindowStartTimeInput")
    def maintenance_window_start_time_input(
        self,
    ) -> typing.Optional["MqBrokerMaintenanceWindowStartTime"]:
        return typing.cast(typing.Optional["MqBrokerMaintenanceWindowStartTime"], jsii.get(self, "maintenanceWindowStartTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="publiclyAccessibleInput")
    def publicly_accessible_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "publiclyAccessibleInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupsInput")
    def security_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="storageTypeInput")
    def storage_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdsInput")
    def subnet_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetIdsInput"))

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
    ) -> typing.Optional[typing.Union["MqBrokerTimeouts", _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["MqBrokerTimeouts", _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="userInput")
    def user_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MqBrokerUser"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MqBrokerUser"]]], jsii.get(self, "userInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__c5197958997f78ea2b30ffd0d8245cf9e940de4266d95d087888a3621dbf709f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applyImmediately", value)

    @builtins.property
    @jsii.member(jsii_name="authenticationStrategy")
    def authentication_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authenticationStrategy"))

    @authentication_strategy.setter
    def authentication_strategy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9371d77e8c2ad0b7fb0fa8bcf04b83d433daf68d5c0ab60a54458b1dcd51a03b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationStrategy", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__4f424ba7a541ae7cf04bdc8f2ec08ba87f7b2b43ac970e847f9b9ceba529d4aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoMinorVersionUpgrade", value)

    @builtins.property
    @jsii.member(jsii_name="brokerName")
    def broker_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "brokerName"))

    @broker_name.setter
    def broker_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab37fdd8f8ccf9432b80f3fcf6ddf2e3dd00c2ee4d1ba3dc0e225a7c5192b83e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "brokerName", value)

    @builtins.property
    @jsii.member(jsii_name="deploymentMode")
    def deployment_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deploymentMode"))

    @deployment_mode.setter
    def deployment_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f12fe20189e970938590c574d4f90cad006ebd1734ddaf70cb950c42c5fbdd0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentMode", value)

    @builtins.property
    @jsii.member(jsii_name="engineType")
    def engine_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "engineType"))

    @engine_type.setter
    def engine_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcf790accbefd4f5a578ff8347eccc03ae8aeb575c080f038af3659b8e40b79c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engineType", value)

    @builtins.property
    @jsii.member(jsii_name="engineVersion")
    def engine_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "engineVersion"))

    @engine_version.setter
    def engine_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__485334e52a40f9d6f6e275e0e0b378c3bc2dac74bb4c1985a6016895ddc93886)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engineVersion", value)

    @builtins.property
    @jsii.member(jsii_name="hostInstanceType")
    def host_instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostInstanceType"))

    @host_instance_type.setter
    def host_instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbd59d110be2eb11c6eb433474c5f58394ed255c6f779788589b6913ef9114bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostInstanceType", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a646ea0b6f3d06abfde71b7909a33285e6fe41848364fd51929883d0704747b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__c549e559bc5e2dee9e1f65e5f798e8370e59ed7036b4915095b4d49bd04e0f2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publiclyAccessible", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroups")
    def security_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroups"))

    @security_groups.setter
    def security_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ea34d66f8527145c97ae85bea9811dbc3e3d71bd2e3d960e4a0c21bb2944bd3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroups", value)

    @builtins.property
    @jsii.member(jsii_name="storageType")
    def storage_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageType"))

    @storage_type.setter
    def storage_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c5c3a1d603e983ecedf2e4f24019348ad4497acb3fa74b5c84710e1df4a38aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageType", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a5d4cb8e292fb005fc21acb0e2c3fb627975cd41815a1718d8ef72f9da4be48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__802e935014537a291f87badb365a5b02884c933d4a707d5124693efbb7c74e89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96ac260ee715bfc833860718bf5781d78f610c6af138eacb19e73d358d637437)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.mqBroker.MqBrokerConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "broker_name": "brokerName",
        "engine_type": "engineType",
        "engine_version": "engineVersion",
        "host_instance_type": "hostInstanceType",
        "user": "user",
        "apply_immediately": "applyImmediately",
        "authentication_strategy": "authenticationStrategy",
        "auto_minor_version_upgrade": "autoMinorVersionUpgrade",
        "configuration": "configuration",
        "deployment_mode": "deploymentMode",
        "encryption_options": "encryptionOptions",
        "id": "id",
        "ldap_server_metadata": "ldapServerMetadata",
        "logs": "logs",
        "maintenance_window_start_time": "maintenanceWindowStartTime",
        "publicly_accessible": "publiclyAccessible",
        "security_groups": "securityGroups",
        "storage_type": "storageType",
        "subnet_ids": "subnetIds",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timeouts": "timeouts",
    },
)
class MqBrokerConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        broker_name: builtins.str,
        engine_type: builtins.str,
        engine_version: builtins.str,
        host_instance_type: builtins.str,
        user: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["MqBrokerUser", typing.Dict[builtins.str, typing.Any]]]],
        apply_immediately: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        authentication_strategy: typing.Optional[builtins.str] = None,
        auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        configuration: typing.Optional[typing.Union["MqBrokerConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        deployment_mode: typing.Optional[builtins.str] = None,
        encryption_options: typing.Optional[typing.Union["MqBrokerEncryptionOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        ldap_server_metadata: typing.Optional[typing.Union["MqBrokerLdapServerMetadata", typing.Dict[builtins.str, typing.Any]]] = None,
        logs: typing.Optional[typing.Union["MqBrokerLogs", typing.Dict[builtins.str, typing.Any]]] = None,
        maintenance_window_start_time: typing.Optional[typing.Union["MqBrokerMaintenanceWindowStartTime", typing.Dict[builtins.str, typing.Any]]] = None,
        publicly_accessible: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        storage_type: typing.Optional[builtins.str] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["MqBrokerTimeouts", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param broker_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#broker_name MqBroker#broker_name}.
        :param engine_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#engine_type MqBroker#engine_type}.
        :param engine_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#engine_version MqBroker#engine_version}.
        :param host_instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#host_instance_type MqBroker#host_instance_type}.
        :param user: user block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#user MqBroker#user}
        :param apply_immediately: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#apply_immediately MqBroker#apply_immediately}.
        :param authentication_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#authentication_strategy MqBroker#authentication_strategy}.
        :param auto_minor_version_upgrade: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#auto_minor_version_upgrade MqBroker#auto_minor_version_upgrade}.
        :param configuration: configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#configuration MqBroker#configuration}
        :param deployment_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#deployment_mode MqBroker#deployment_mode}.
        :param encryption_options: encryption_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#encryption_options MqBroker#encryption_options}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#id MqBroker#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ldap_server_metadata: ldap_server_metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#ldap_server_metadata MqBroker#ldap_server_metadata}
        :param logs: logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#logs MqBroker#logs}
        :param maintenance_window_start_time: maintenance_window_start_time block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#maintenance_window_start_time MqBroker#maintenance_window_start_time}
        :param publicly_accessible: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#publicly_accessible MqBroker#publicly_accessible}.
        :param security_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#security_groups MqBroker#security_groups}.
        :param storage_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#storage_type MqBroker#storage_type}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#subnet_ids MqBroker#subnet_ids}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#tags MqBroker#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#tags_all MqBroker#tags_all}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#timeouts MqBroker#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(configuration, dict):
            configuration = MqBrokerConfiguration(**configuration)
        if isinstance(encryption_options, dict):
            encryption_options = MqBrokerEncryptionOptions(**encryption_options)
        if isinstance(ldap_server_metadata, dict):
            ldap_server_metadata = MqBrokerLdapServerMetadata(**ldap_server_metadata)
        if isinstance(logs, dict):
            logs = MqBrokerLogs(**logs)
        if isinstance(maintenance_window_start_time, dict):
            maintenance_window_start_time = MqBrokerMaintenanceWindowStartTime(**maintenance_window_start_time)
        if isinstance(timeouts, dict):
            timeouts = MqBrokerTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74edaa5569ee13fa740d136f4788d25e2b47b18d67223aa6f66aafea7bef3c8b)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument broker_name", value=broker_name, expected_type=type_hints["broker_name"])
            check_type(argname="argument engine_type", value=engine_type, expected_type=type_hints["engine_type"])
            check_type(argname="argument engine_version", value=engine_version, expected_type=type_hints["engine_version"])
            check_type(argname="argument host_instance_type", value=host_instance_type, expected_type=type_hints["host_instance_type"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
            check_type(argname="argument apply_immediately", value=apply_immediately, expected_type=type_hints["apply_immediately"])
            check_type(argname="argument authentication_strategy", value=authentication_strategy, expected_type=type_hints["authentication_strategy"])
            check_type(argname="argument auto_minor_version_upgrade", value=auto_minor_version_upgrade, expected_type=type_hints["auto_minor_version_upgrade"])
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument deployment_mode", value=deployment_mode, expected_type=type_hints["deployment_mode"])
            check_type(argname="argument encryption_options", value=encryption_options, expected_type=type_hints["encryption_options"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ldap_server_metadata", value=ldap_server_metadata, expected_type=type_hints["ldap_server_metadata"])
            check_type(argname="argument logs", value=logs, expected_type=type_hints["logs"])
            check_type(argname="argument maintenance_window_start_time", value=maintenance_window_start_time, expected_type=type_hints["maintenance_window_start_time"])
            check_type(argname="argument publicly_accessible", value=publicly_accessible, expected_type=type_hints["publicly_accessible"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument storage_type", value=storage_type, expected_type=type_hints["storage_type"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "broker_name": broker_name,
            "engine_type": engine_type,
            "engine_version": engine_version,
            "host_instance_type": host_instance_type,
            "user": user,
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
        if authentication_strategy is not None:
            self._values["authentication_strategy"] = authentication_strategy
        if auto_minor_version_upgrade is not None:
            self._values["auto_minor_version_upgrade"] = auto_minor_version_upgrade
        if configuration is not None:
            self._values["configuration"] = configuration
        if deployment_mode is not None:
            self._values["deployment_mode"] = deployment_mode
        if encryption_options is not None:
            self._values["encryption_options"] = encryption_options
        if id is not None:
            self._values["id"] = id
        if ldap_server_metadata is not None:
            self._values["ldap_server_metadata"] = ldap_server_metadata
        if logs is not None:
            self._values["logs"] = logs
        if maintenance_window_start_time is not None:
            self._values["maintenance_window_start_time"] = maintenance_window_start_time
        if publicly_accessible is not None:
            self._values["publicly_accessible"] = publicly_accessible
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if storage_type is not None:
            self._values["storage_type"] = storage_type
        if subnet_ids is not None:
            self._values["subnet_ids"] = subnet_ids
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timeouts is not None:
            self._values["timeouts"] = timeouts

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
    def broker_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#broker_name MqBroker#broker_name}.'''
        result = self._values.get("broker_name")
        assert result is not None, "Required property 'broker_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def engine_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#engine_type MqBroker#engine_type}.'''
        result = self._values.get("engine_type")
        assert result is not None, "Required property 'engine_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def engine_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#engine_version MqBroker#engine_version}.'''
        result = self._values.get("engine_version")
        assert result is not None, "Required property 'engine_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host_instance_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#host_instance_type MqBroker#host_instance_type}.'''
        result = self._values.get("host_instance_type")
        assert result is not None, "Required property 'host_instance_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MqBrokerUser"]]:
        '''user block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#user MqBroker#user}
        '''
        result = self._values.get("user")
        assert result is not None, "Required property 'user' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MqBrokerUser"]], result)

    @builtins.property
    def apply_immediately(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#apply_immediately MqBroker#apply_immediately}.'''
        result = self._values.get("apply_immediately")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def authentication_strategy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#authentication_strategy MqBroker#authentication_strategy}.'''
        result = self._values.get("authentication_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auto_minor_version_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#auto_minor_version_upgrade MqBroker#auto_minor_version_upgrade}.'''
        result = self._values.get("auto_minor_version_upgrade")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def configuration(self) -> typing.Optional["MqBrokerConfiguration"]:
        '''configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#configuration MqBroker#configuration}
        '''
        result = self._values.get("configuration")
        return typing.cast(typing.Optional["MqBrokerConfiguration"], result)

    @builtins.property
    def deployment_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#deployment_mode MqBroker#deployment_mode}.'''
        result = self._values.get("deployment_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_options(self) -> typing.Optional["MqBrokerEncryptionOptions"]:
        '''encryption_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#encryption_options MqBroker#encryption_options}
        '''
        result = self._values.get("encryption_options")
        return typing.cast(typing.Optional["MqBrokerEncryptionOptions"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#id MqBroker#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ldap_server_metadata(self) -> typing.Optional["MqBrokerLdapServerMetadata"]:
        '''ldap_server_metadata block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#ldap_server_metadata MqBroker#ldap_server_metadata}
        '''
        result = self._values.get("ldap_server_metadata")
        return typing.cast(typing.Optional["MqBrokerLdapServerMetadata"], result)

    @builtins.property
    def logs(self) -> typing.Optional["MqBrokerLogs"]:
        '''logs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#logs MqBroker#logs}
        '''
        result = self._values.get("logs")
        return typing.cast(typing.Optional["MqBrokerLogs"], result)

    @builtins.property
    def maintenance_window_start_time(
        self,
    ) -> typing.Optional["MqBrokerMaintenanceWindowStartTime"]:
        '''maintenance_window_start_time block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#maintenance_window_start_time MqBroker#maintenance_window_start_time}
        '''
        result = self._values.get("maintenance_window_start_time")
        return typing.cast(typing.Optional["MqBrokerMaintenanceWindowStartTime"], result)

    @builtins.property
    def publicly_accessible(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#publicly_accessible MqBroker#publicly_accessible}.'''
        result = self._values.get("publicly_accessible")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#security_groups MqBroker#security_groups}.'''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def storage_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#storage_type MqBroker#storage_type}.'''
        result = self._values.get("storage_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#subnet_ids MqBroker#subnet_ids}.'''
        result = self._values.get("subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#tags MqBroker#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#tags_all MqBroker#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["MqBrokerTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#timeouts MqBroker#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["MqBrokerTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MqBrokerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.mqBroker.MqBrokerConfiguration",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "revision": "revision"},
)
class MqBrokerConfiguration:
    def __init__(
        self,
        *,
        id: typing.Optional[builtins.str] = None,
        revision: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#id MqBroker#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param revision: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#revision MqBroker#revision}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2a65d3497b8f1d24f81962d68a3be3f7aaea8908a1378c520fb5eab11fafcde)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument revision", value=revision, expected_type=type_hints["revision"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if revision is not None:
            self._values["revision"] = revision

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#id MqBroker#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def revision(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#revision MqBroker#revision}.'''
        result = self._values.get("revision")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MqBrokerConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MqBrokerConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.mqBroker.MqBrokerConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__199d02a965829a1752b4a5cab73855f2fbc5c70528d3af3953af8b9f4e0652c6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetRevision")
    def reset_revision(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRevision", []))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="revisionInput")
    def revision_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "revisionInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a653d37860ce117c9e641c40a03c3136fb00b5934a98c02e47390709827c35b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="revision")
    def revision(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "revision"))

    @revision.setter
    def revision(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1d29e6d74023817fd3f4556bd9ebbce2f3ff937573919888d54f981a58dacf6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "revision", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MqBrokerConfiguration]:
        return typing.cast(typing.Optional[MqBrokerConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[MqBrokerConfiguration]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc38d18d8a1caa6b50577b7fc9eb6ac4fad15c49aba470e825bf78f9c2d14375)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.mqBroker.MqBrokerEncryptionOptions",
    jsii_struct_bases=[],
    name_mapping={"kms_key_id": "kmsKeyId", "use_aws_owned_key": "useAwsOwnedKey"},
)
class MqBrokerEncryptionOptions:
    def __init__(
        self,
        *,
        kms_key_id: typing.Optional[builtins.str] = None,
        use_aws_owned_key: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#kms_key_id MqBroker#kms_key_id}.
        :param use_aws_owned_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#use_aws_owned_key MqBroker#use_aws_owned_key}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9eb820a5cbfd01cfe293c75b10033ffe8d22d2e6b910605ea898ba0d1e69dad)
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument use_aws_owned_key", value=use_aws_owned_key, expected_type=type_hints["use_aws_owned_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if use_aws_owned_key is not None:
            self._values["use_aws_owned_key"] = use_aws_owned_key

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#kms_key_id MqBroker#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_aws_owned_key(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#use_aws_owned_key MqBroker#use_aws_owned_key}.'''
        result = self._values.get("use_aws_owned_key")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MqBrokerEncryptionOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MqBrokerEncryptionOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.mqBroker.MqBrokerEncryptionOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2657e6ede4f4a1aa7884585665c32c59e65627975ee32dc9114487ee6671a043)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKmsKeyId")
    def reset_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyId", []))

    @jsii.member(jsii_name="resetUseAwsOwnedKey")
    def reset_use_aws_owned_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseAwsOwnedKey", []))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdInput")
    def kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="useAwsOwnedKeyInput")
    def use_aws_owned_key_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "useAwsOwnedKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ef9df1820577dc1bfa266ca32b3e2f3da0406df7ca7374a55fa80a91beba77d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="useAwsOwnedKey")
    def use_aws_owned_key(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "useAwsOwnedKey"))

    @use_aws_owned_key.setter
    def use_aws_owned_key(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f34a67d326f7e78982f54f5740f6ce28451bcb9e49d31ff6a17ff4b1846e233c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useAwsOwnedKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MqBrokerEncryptionOptions]:
        return typing.cast(typing.Optional[MqBrokerEncryptionOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[MqBrokerEncryptionOptions]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8dba6cf9227b6d173df4af851785faeccabad7a84e69fa43219860960119b7a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.mqBroker.MqBrokerInstances",
    jsii_struct_bases=[],
    name_mapping={},
)
class MqBrokerInstances:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MqBrokerInstances(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MqBrokerInstancesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.mqBroker.MqBrokerInstancesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ae9d50133db03f1e1c17f617ba6a8822f944994f516440f584684a35b79a240e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "MqBrokerInstancesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58d223f75be32bff9a33bb99732bd1324d93261adc0f4d2b2f859ccf5a0bd5bf)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MqBrokerInstancesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87151b8b93a0c28331cc5f6e55ab466c51be4ea13adddd749bed25f401b6adc8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a76ee80068d58ae2c4f985d7424d290f548bc4f1e04d9e286d38d7a5f1ca07ff)
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
            type_hints = typing.get_type_hints(_typecheckingstub__487bdc821c18c7aa45be2f953a6eac7357a26b99cf5af6da06d2d00f90dada77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class MqBrokerInstancesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.mqBroker.MqBrokerInstancesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bd11d25343b0a56c77a8f354f2268039489654589ff05785306662f6db295326)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="consoleUrl")
    def console_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consoleUrl"))

    @builtins.property
    @jsii.member(jsii_name="endpoints")
    def endpoints(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "endpoints"))

    @builtins.property
    @jsii.member(jsii_name="ipAddress")
    def ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddress"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MqBrokerInstances]:
        return typing.cast(typing.Optional[MqBrokerInstances], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[MqBrokerInstances]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2e83107abc35d5989c93562f5c6fd136e314e9075cff95fcfa28efdc159c917)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.mqBroker.MqBrokerLdapServerMetadata",
    jsii_struct_bases=[],
    name_mapping={
        "hosts": "hosts",
        "role_base": "roleBase",
        "role_name": "roleName",
        "role_search_matching": "roleSearchMatching",
        "role_search_subtree": "roleSearchSubtree",
        "service_account_password": "serviceAccountPassword",
        "service_account_username": "serviceAccountUsername",
        "user_base": "userBase",
        "user_role_name": "userRoleName",
        "user_search_matching": "userSearchMatching",
        "user_search_subtree": "userSearchSubtree",
    },
)
class MqBrokerLdapServerMetadata:
    def __init__(
        self,
        *,
        hosts: typing.Optional[typing.Sequence[builtins.str]] = None,
        role_base: typing.Optional[builtins.str] = None,
        role_name: typing.Optional[builtins.str] = None,
        role_search_matching: typing.Optional[builtins.str] = None,
        role_search_subtree: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        service_account_password: typing.Optional[builtins.str] = None,
        service_account_username: typing.Optional[builtins.str] = None,
        user_base: typing.Optional[builtins.str] = None,
        user_role_name: typing.Optional[builtins.str] = None,
        user_search_matching: typing.Optional[builtins.str] = None,
        user_search_subtree: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param hosts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#hosts MqBroker#hosts}.
        :param role_base: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#role_base MqBroker#role_base}.
        :param role_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#role_name MqBroker#role_name}.
        :param role_search_matching: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#role_search_matching MqBroker#role_search_matching}.
        :param role_search_subtree: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#role_search_subtree MqBroker#role_search_subtree}.
        :param service_account_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#service_account_password MqBroker#service_account_password}.
        :param service_account_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#service_account_username MqBroker#service_account_username}.
        :param user_base: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#user_base MqBroker#user_base}.
        :param user_role_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#user_role_name MqBroker#user_role_name}.
        :param user_search_matching: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#user_search_matching MqBroker#user_search_matching}.
        :param user_search_subtree: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#user_search_subtree MqBroker#user_search_subtree}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbe4de5410c7c817f15ac4b63a79142aa2f6fabf2b4fe0e3c70ad1ddb5ff9054)
            check_type(argname="argument hosts", value=hosts, expected_type=type_hints["hosts"])
            check_type(argname="argument role_base", value=role_base, expected_type=type_hints["role_base"])
            check_type(argname="argument role_name", value=role_name, expected_type=type_hints["role_name"])
            check_type(argname="argument role_search_matching", value=role_search_matching, expected_type=type_hints["role_search_matching"])
            check_type(argname="argument role_search_subtree", value=role_search_subtree, expected_type=type_hints["role_search_subtree"])
            check_type(argname="argument service_account_password", value=service_account_password, expected_type=type_hints["service_account_password"])
            check_type(argname="argument service_account_username", value=service_account_username, expected_type=type_hints["service_account_username"])
            check_type(argname="argument user_base", value=user_base, expected_type=type_hints["user_base"])
            check_type(argname="argument user_role_name", value=user_role_name, expected_type=type_hints["user_role_name"])
            check_type(argname="argument user_search_matching", value=user_search_matching, expected_type=type_hints["user_search_matching"])
            check_type(argname="argument user_search_subtree", value=user_search_subtree, expected_type=type_hints["user_search_subtree"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if hosts is not None:
            self._values["hosts"] = hosts
        if role_base is not None:
            self._values["role_base"] = role_base
        if role_name is not None:
            self._values["role_name"] = role_name
        if role_search_matching is not None:
            self._values["role_search_matching"] = role_search_matching
        if role_search_subtree is not None:
            self._values["role_search_subtree"] = role_search_subtree
        if service_account_password is not None:
            self._values["service_account_password"] = service_account_password
        if service_account_username is not None:
            self._values["service_account_username"] = service_account_username
        if user_base is not None:
            self._values["user_base"] = user_base
        if user_role_name is not None:
            self._values["user_role_name"] = user_role_name
        if user_search_matching is not None:
            self._values["user_search_matching"] = user_search_matching
        if user_search_subtree is not None:
            self._values["user_search_subtree"] = user_search_subtree

    @builtins.property
    def hosts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#hosts MqBroker#hosts}.'''
        result = self._values.get("hosts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def role_base(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#role_base MqBroker#role_base}.'''
        result = self._values.get("role_base")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#role_name MqBroker#role_name}.'''
        result = self._values.get("role_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_search_matching(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#role_search_matching MqBroker#role_search_matching}.'''
        result = self._values.get("role_search_matching")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_search_subtree(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#role_search_subtree MqBroker#role_search_subtree}.'''
        result = self._values.get("role_search_subtree")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def service_account_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#service_account_password MqBroker#service_account_password}.'''
        result = self._values.get("service_account_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_account_username(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#service_account_username MqBroker#service_account_username}.'''
        result = self._values.get("service_account_username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_base(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#user_base MqBroker#user_base}.'''
        result = self._values.get("user_base")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_role_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#user_role_name MqBroker#user_role_name}.'''
        result = self._values.get("user_role_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_search_matching(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#user_search_matching MqBroker#user_search_matching}.'''
        result = self._values.get("user_search_matching")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_search_subtree(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#user_search_subtree MqBroker#user_search_subtree}.'''
        result = self._values.get("user_search_subtree")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MqBrokerLdapServerMetadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MqBrokerLdapServerMetadataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.mqBroker.MqBrokerLdapServerMetadataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c56dc3ee375258a655b3a6a92ff857b5ac239e61547a87719a1b97c278aad67b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHosts")
    def reset_hosts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHosts", []))

    @jsii.member(jsii_name="resetRoleBase")
    def reset_role_base(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoleBase", []))

    @jsii.member(jsii_name="resetRoleName")
    def reset_role_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoleName", []))

    @jsii.member(jsii_name="resetRoleSearchMatching")
    def reset_role_search_matching(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoleSearchMatching", []))

    @jsii.member(jsii_name="resetRoleSearchSubtree")
    def reset_role_search_subtree(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoleSearchSubtree", []))

    @jsii.member(jsii_name="resetServiceAccountPassword")
    def reset_service_account_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceAccountPassword", []))

    @jsii.member(jsii_name="resetServiceAccountUsername")
    def reset_service_account_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceAccountUsername", []))

    @jsii.member(jsii_name="resetUserBase")
    def reset_user_base(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserBase", []))

    @jsii.member(jsii_name="resetUserRoleName")
    def reset_user_role_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserRoleName", []))

    @jsii.member(jsii_name="resetUserSearchMatching")
    def reset_user_search_matching(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserSearchMatching", []))

    @jsii.member(jsii_name="resetUserSearchSubtree")
    def reset_user_search_subtree(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserSearchSubtree", []))

    @builtins.property
    @jsii.member(jsii_name="hostsInput")
    def hosts_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "hostsInput"))

    @builtins.property
    @jsii.member(jsii_name="roleBaseInput")
    def role_base_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleBaseInput"))

    @builtins.property
    @jsii.member(jsii_name="roleNameInput")
    def role_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleNameInput"))

    @builtins.property
    @jsii.member(jsii_name="roleSearchMatchingInput")
    def role_search_matching_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleSearchMatchingInput"))

    @builtins.property
    @jsii.member(jsii_name="roleSearchSubtreeInput")
    def role_search_subtree_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "roleSearchSubtreeInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccountPasswordInput")
    def service_account_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccountPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccountUsernameInput")
    def service_account_username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccountUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="userBaseInput")
    def user_base_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userBaseInput"))

    @builtins.property
    @jsii.member(jsii_name="userRoleNameInput")
    def user_role_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userRoleNameInput"))

    @builtins.property
    @jsii.member(jsii_name="userSearchMatchingInput")
    def user_search_matching_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userSearchMatchingInput"))

    @builtins.property
    @jsii.member(jsii_name="userSearchSubtreeInput")
    def user_search_subtree_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "userSearchSubtreeInput"))

    @builtins.property
    @jsii.member(jsii_name="hosts")
    def hosts(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "hosts"))

    @hosts.setter
    def hosts(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__041a36ff8447cfb88e64a98b18e9a26d4bb608b0a2ee3d718122b2ed5134de59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hosts", value)

    @builtins.property
    @jsii.member(jsii_name="roleBase")
    def role_base(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleBase"))

    @role_base.setter
    def role_base(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f89d0228ac6006eb50d1322e8be57ef588304a3b6b614affc742ef7fc631ca6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleBase", value)

    @builtins.property
    @jsii.member(jsii_name="roleName")
    def role_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleName"))

    @role_name.setter
    def role_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef07be9fb922a69ffd9e44830987a9507fdea149214201c39695f60998e4fc33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleName", value)

    @builtins.property
    @jsii.member(jsii_name="roleSearchMatching")
    def role_search_matching(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleSearchMatching"))

    @role_search_matching.setter
    def role_search_matching(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdb94be9b190c09f439c60d01056057fd2b92972636976f39c7fba3811c0deea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleSearchMatching", value)

    @builtins.property
    @jsii.member(jsii_name="roleSearchSubtree")
    def role_search_subtree(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "roleSearchSubtree"))

    @role_search_subtree.setter
    def role_search_subtree(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1250ade6818f6af13b98562b7e21119cd77b22688eb82066eba4d90e76ee4dfc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleSearchSubtree", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccountPassword")
    def service_account_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccountPassword"))

    @service_account_password.setter
    def service_account_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc8e4320792bc8f9b4381ff037023c04d1d0fb6d2957ebec747797ede6fb178f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccountPassword", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccountUsername")
    def service_account_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccountUsername"))

    @service_account_username.setter
    def service_account_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffdafa8263caf04f0ab9f212092374b9dfec91e07eccc2102d07d2d21890a7bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccountUsername", value)

    @builtins.property
    @jsii.member(jsii_name="userBase")
    def user_base(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userBase"))

    @user_base.setter
    def user_base(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8770a227e81a38cb6daaa0528293c6f83c2ffcc61d2ab663dc1cae732eb1e6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userBase", value)

    @builtins.property
    @jsii.member(jsii_name="userRoleName")
    def user_role_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userRoleName"))

    @user_role_name.setter
    def user_role_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c2c88d83c8b4bca31e585fabb3da7638811c075dd58012e581f3385433448a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userRoleName", value)

    @builtins.property
    @jsii.member(jsii_name="userSearchMatching")
    def user_search_matching(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userSearchMatching"))

    @user_search_matching.setter
    def user_search_matching(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da8d41d61cc708493d8b2b3c603a06c4b90c04ef523099a31970e084de184221)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userSearchMatching", value)

    @builtins.property
    @jsii.member(jsii_name="userSearchSubtree")
    def user_search_subtree(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "userSearchSubtree"))

    @user_search_subtree.setter
    def user_search_subtree(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8eb2ccec2828c3af10a9598b7fad9c6dd8734d145b8137f37c0748f91a6e7903)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userSearchSubtree", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MqBrokerLdapServerMetadata]:
        return typing.cast(typing.Optional[MqBrokerLdapServerMetadata], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MqBrokerLdapServerMetadata],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd3a1a305b310fafd9d2c346c9ca7cdfe65996feadab6629b7cb29b44e629f4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.mqBroker.MqBrokerLogs",
    jsii_struct_bases=[],
    name_mapping={"audit": "audit", "general": "general"},
)
class MqBrokerLogs:
    def __init__(
        self,
        *,
        audit: typing.Optional[builtins.str] = None,
        general: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param audit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#audit MqBroker#audit}.
        :param general: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#general MqBroker#general}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39baa8ecf0ad2d8742f809c1f51a3eb6fdb5a90cb3761da7e3462a12ffaa49bb)
            check_type(argname="argument audit", value=audit, expected_type=type_hints["audit"])
            check_type(argname="argument general", value=general, expected_type=type_hints["general"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if audit is not None:
            self._values["audit"] = audit
        if general is not None:
            self._values["general"] = general

    @builtins.property
    def audit(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#audit MqBroker#audit}.'''
        result = self._values.get("audit")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def general(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#general MqBroker#general}.'''
        result = self._values.get("general")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MqBrokerLogs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MqBrokerLogsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.mqBroker.MqBrokerLogsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7eef2ccc6ed1f0c5116043d86064be26bac1ca0b78a7ca53d92dd5a2f7bf26a5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAudit")
    def reset_audit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAudit", []))

    @jsii.member(jsii_name="resetGeneral")
    def reset_general(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGeneral", []))

    @builtins.property
    @jsii.member(jsii_name="auditInput")
    def audit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "auditInput"))

    @builtins.property
    @jsii.member(jsii_name="generalInput")
    def general_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "generalInput"))

    @builtins.property
    @jsii.member(jsii_name="audit")
    def audit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "audit"))

    @audit.setter
    def audit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eabec2641730a9aa90956cfb6aaf7004169480dba954854d46ef34cc75810e9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "audit", value)

    @builtins.property
    @jsii.member(jsii_name="general")
    def general(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "general"))

    @general.setter
    def general(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd4fb06fe6043aca5fa159e988528e35da042d794ea774320f6dad83412fc7cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "general", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MqBrokerLogs]:
        return typing.cast(typing.Optional[MqBrokerLogs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[MqBrokerLogs]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__417123249973b6a97ce3a6a70eae19cedaeba976dd67264f4380b6e06364321d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.mqBroker.MqBrokerMaintenanceWindowStartTime",
    jsii_struct_bases=[],
    name_mapping={
        "day_of_week": "dayOfWeek",
        "time_of_day": "timeOfDay",
        "time_zone": "timeZone",
    },
)
class MqBrokerMaintenanceWindowStartTime:
    def __init__(
        self,
        *,
        day_of_week: builtins.str,
        time_of_day: builtins.str,
        time_zone: builtins.str,
    ) -> None:
        '''
        :param day_of_week: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#day_of_week MqBroker#day_of_week}.
        :param time_of_day: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#time_of_day MqBroker#time_of_day}.
        :param time_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#time_zone MqBroker#time_zone}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c19bbd792355a0370991c89221a58549c158dac49e070289a13f41952229cb92)
            check_type(argname="argument day_of_week", value=day_of_week, expected_type=type_hints["day_of_week"])
            check_type(argname="argument time_of_day", value=time_of_day, expected_type=type_hints["time_of_day"])
            check_type(argname="argument time_zone", value=time_zone, expected_type=type_hints["time_zone"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "day_of_week": day_of_week,
            "time_of_day": time_of_day,
            "time_zone": time_zone,
        }

    @builtins.property
    def day_of_week(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#day_of_week MqBroker#day_of_week}.'''
        result = self._values.get("day_of_week")
        assert result is not None, "Required property 'day_of_week' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def time_of_day(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#time_of_day MqBroker#time_of_day}.'''
        result = self._values.get("time_of_day")
        assert result is not None, "Required property 'time_of_day' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def time_zone(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#time_zone MqBroker#time_zone}.'''
        result = self._values.get("time_zone")
        assert result is not None, "Required property 'time_zone' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MqBrokerMaintenanceWindowStartTime(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MqBrokerMaintenanceWindowStartTimeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.mqBroker.MqBrokerMaintenanceWindowStartTimeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6c8de5d8d75d774bb844c48ba20a80217fa574f9e00aa2f14a27dc62ae07fb5f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="dayOfWeekInput")
    def day_of_week_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dayOfWeekInput"))

    @builtins.property
    @jsii.member(jsii_name="timeOfDayInput")
    def time_of_day_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeOfDayInput"))

    @builtins.property
    @jsii.member(jsii_name="timeZoneInput")
    def time_zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeZoneInput"))

    @builtins.property
    @jsii.member(jsii_name="dayOfWeek")
    def day_of_week(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dayOfWeek"))

    @day_of_week.setter
    def day_of_week(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4088f851dcd1affa10b5df986e51b34052c02abd6be922ae646a8907e9058ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dayOfWeek", value)

    @builtins.property
    @jsii.member(jsii_name="timeOfDay")
    def time_of_day(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeOfDay"))

    @time_of_day.setter
    def time_of_day(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aea1933fbb881aef36a4b170e663dda7b9172d4ecfdafe458d6bca3fa92f239a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeOfDay", value)

    @builtins.property
    @jsii.member(jsii_name="timeZone")
    def time_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeZone"))

    @time_zone.setter
    def time_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db9d72720bcd900a8c37a4ab8e66a1375ef83ddb58a122e71003fd938c6cb21e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeZone", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MqBrokerMaintenanceWindowStartTime]:
        return typing.cast(typing.Optional[MqBrokerMaintenanceWindowStartTime], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MqBrokerMaintenanceWindowStartTime],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d1e23a0a25c46ee38755d6a184e86f6d3fb62c9529c3586541ccf80a29a4097)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.mqBroker.MqBrokerTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class MqBrokerTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#create MqBroker#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#delete MqBroker#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#update MqBroker#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0783c00ab206ea1d58f5fbcff279993666d971c5f1575a58ff98d1e842248aae)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#create MqBroker#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#delete MqBroker#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#update MqBroker#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MqBrokerTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MqBrokerTimeoutsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.mqBroker.MqBrokerTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__561c021e9df01a1aa90065a5de70ecc73a1918cc8dbe779908dc75af5ef5bb49)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6864fa5a47221adee9c6c1d5380c5a4b55a636d5667cd5bf7e536c5eb602ccac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__286480a5b1f23120d21a4055d153a9a6d9261c22d861f9ae5eab01d485c801f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5276e66fc7d8eb834c1e9f75efb70fcd58e9dcf8a931472a2032963935a830dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MqBrokerTimeouts, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MqBrokerTimeouts, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MqBrokerTimeouts, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59ebbb263af8e54be3273d646fda03ef30088d087b04f8dae406c3f0da9d5a51)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.mqBroker.MqBrokerUser",
    jsii_struct_bases=[],
    name_mapping={
        "password": "password",
        "username": "username",
        "console_access": "consoleAccess",
        "groups": "groups",
    },
)
class MqBrokerUser:
    def __init__(
        self,
        *,
        password: builtins.str,
        username: builtins.str,
        console_access: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#password MqBroker#password}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#username MqBroker#username}.
        :param console_access: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#console_access MqBroker#console_access}.
        :param groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#groups MqBroker#groups}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4119ed99371b9ea32e692c39bf81275131ec7f3299fb9e4df737f2b3ded3a19)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument console_access", value=console_access, expected_type=type_hints["console_access"])
            check_type(argname="argument groups", value=groups, expected_type=type_hints["groups"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "password": password,
            "username": username,
        }
        if console_access is not None:
            self._values["console_access"] = console_access
        if groups is not None:
            self._values["groups"] = groups

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#password MqBroker#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#username MqBroker#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def console_access(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#console_access MqBroker#console_access}.'''
        result = self._values.get("console_access")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/mq_broker#groups MqBroker#groups}.'''
        result = self._values.get("groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MqBrokerUser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MqBrokerUserList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.mqBroker.MqBrokerUserList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__156cd202fee0ce9c1f8930c018f0684f1939e8c4818549e545684e50aaa978eb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "MqBrokerUserOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d19a228d7b98dea34c4e470c1530c3053c85e2ae08d65418d65722eaa0d66d24)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MqBrokerUserOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9776f20cb86c65fc81b767d6bc1d43fb3e98db9b76dc0c4852761e8561a34b27)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fa9d8ba2b6948b77a3f1bed5b2227a03b7dcbc6c6174c03a6fbdfd6376b75a67)
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
            type_hints = typing.get_type_hints(_typecheckingstub__97a42a9d5a325ac8c363b210580efbebf463097359d72d5b2c90848d0022ca4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MqBrokerUser]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MqBrokerUser]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MqBrokerUser]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38656617fe1c0ee9add850065694011a606aee82479a22ab20b6236f41b0159b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MqBrokerUserOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.mqBroker.MqBrokerUserOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4b57824e2bd8970cb0fbf9c252767c3d4311206bf3637d3a68c4647c70129c66)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetConsoleAccess")
    def reset_console_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConsoleAccess", []))

    @jsii.member(jsii_name="resetGroups")
    def reset_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroups", []))

    @builtins.property
    @jsii.member(jsii_name="consoleAccessInput")
    def console_access_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "consoleAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="groupsInput")
    def groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "groupsInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="consoleAccess")
    def console_access(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "consoleAccess"))

    @console_access.setter
    def console_access(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be1d710bb8895528a4dad02a79f21ed937cddf798760a57498a207d041c06443)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consoleAccess", value)

    @builtins.property
    @jsii.member(jsii_name="groups")
    def groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "groups"))

    @groups.setter
    def groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1dc67b1748229e897f299feb066348e8359d879a6c8f0eaeab74a31af0c9a23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groups", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7943f2a8dda515606803e4894dcc9485c706cb5357aa1c0572e2e2f0f5b1c350)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d11b8daf678e1ce10d9cf44363ba8b73406caec6427f042636a3abd2a3e03746)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MqBrokerUser, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MqBrokerUser, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MqBrokerUser, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5aa2219e06c4de30e81c195fff26103ec2e89414f179c5c7635bbd25b4d58c13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MqBroker",
    "MqBrokerConfig",
    "MqBrokerConfiguration",
    "MqBrokerConfigurationOutputReference",
    "MqBrokerEncryptionOptions",
    "MqBrokerEncryptionOptionsOutputReference",
    "MqBrokerInstances",
    "MqBrokerInstancesList",
    "MqBrokerInstancesOutputReference",
    "MqBrokerLdapServerMetadata",
    "MqBrokerLdapServerMetadataOutputReference",
    "MqBrokerLogs",
    "MqBrokerLogsOutputReference",
    "MqBrokerMaintenanceWindowStartTime",
    "MqBrokerMaintenanceWindowStartTimeOutputReference",
    "MqBrokerTimeouts",
    "MqBrokerTimeoutsOutputReference",
    "MqBrokerUser",
    "MqBrokerUserList",
    "MqBrokerUserOutputReference",
]

publication.publish()

def _typecheckingstub__5bf08c6f8c17dec98f70b3b7808f35aa6467448b93cf567f565d37beb7de90b6(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    broker_name: builtins.str,
    engine_type: builtins.str,
    engine_version: builtins.str,
    host_instance_type: builtins.str,
    user: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MqBrokerUser, typing.Dict[builtins.str, typing.Any]]]],
    apply_immediately: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    authentication_strategy: typing.Optional[builtins.str] = None,
    auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    configuration: typing.Optional[typing.Union[MqBrokerConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    deployment_mode: typing.Optional[builtins.str] = None,
    encryption_options: typing.Optional[typing.Union[MqBrokerEncryptionOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    ldap_server_metadata: typing.Optional[typing.Union[MqBrokerLdapServerMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
    logs: typing.Optional[typing.Union[MqBrokerLogs, typing.Dict[builtins.str, typing.Any]]] = None,
    maintenance_window_start_time: typing.Optional[typing.Union[MqBrokerMaintenanceWindowStartTime, typing.Dict[builtins.str, typing.Any]]] = None,
    publicly_accessible: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    storage_type: typing.Optional[builtins.str] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[MqBrokerTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__9f656b1dde4ddfe0105381e9d5abe01bc7d3de204ea96170362aef251c2013f4(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MqBrokerUser, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5197958997f78ea2b30ffd0d8245cf9e940de4266d95d087888a3621dbf709f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9371d77e8c2ad0b7fb0fa8bcf04b83d433daf68d5c0ab60a54458b1dcd51a03b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f424ba7a541ae7cf04bdc8f2ec08ba87f7b2b43ac970e847f9b9ceba529d4aa(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab37fdd8f8ccf9432b80f3fcf6ddf2e3dd00c2ee4d1ba3dc0e225a7c5192b83e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f12fe20189e970938590c574d4f90cad006ebd1734ddaf70cb950c42c5fbdd0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcf790accbefd4f5a578ff8347eccc03ae8aeb575c080f038af3659b8e40b79c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__485334e52a40f9d6f6e275e0e0b378c3bc2dac74bb4c1985a6016895ddc93886(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbd59d110be2eb11c6eb433474c5f58394ed255c6f779788589b6913ef9114bd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a646ea0b6f3d06abfde71b7909a33285e6fe41848364fd51929883d0704747b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c549e559bc5e2dee9e1f65e5f798e8370e59ed7036b4915095b4d49bd04e0f2b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ea34d66f8527145c97ae85bea9811dbc3e3d71bd2e3d960e4a0c21bb2944bd3(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c5c3a1d603e983ecedf2e4f24019348ad4497acb3fa74b5c84710e1df4a38aa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a5d4cb8e292fb005fc21acb0e2c3fb627975cd41815a1718d8ef72f9da4be48(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__802e935014537a291f87badb365a5b02884c933d4a707d5124693efbb7c74e89(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96ac260ee715bfc833860718bf5781d78f610c6af138eacb19e73d358d637437(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74edaa5569ee13fa740d136f4788d25e2b47b18d67223aa6f66aafea7bef3c8b(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    broker_name: builtins.str,
    engine_type: builtins.str,
    engine_version: builtins.str,
    host_instance_type: builtins.str,
    user: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MqBrokerUser, typing.Dict[builtins.str, typing.Any]]]],
    apply_immediately: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    authentication_strategy: typing.Optional[builtins.str] = None,
    auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    configuration: typing.Optional[typing.Union[MqBrokerConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    deployment_mode: typing.Optional[builtins.str] = None,
    encryption_options: typing.Optional[typing.Union[MqBrokerEncryptionOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    ldap_server_metadata: typing.Optional[typing.Union[MqBrokerLdapServerMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
    logs: typing.Optional[typing.Union[MqBrokerLogs, typing.Dict[builtins.str, typing.Any]]] = None,
    maintenance_window_start_time: typing.Optional[typing.Union[MqBrokerMaintenanceWindowStartTime, typing.Dict[builtins.str, typing.Any]]] = None,
    publicly_accessible: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    storage_type: typing.Optional[builtins.str] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeouts: typing.Optional[typing.Union[MqBrokerTimeouts, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2a65d3497b8f1d24f81962d68a3be3f7aaea8908a1378c520fb5eab11fafcde(
    *,
    id: typing.Optional[builtins.str] = None,
    revision: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__199d02a965829a1752b4a5cab73855f2fbc5c70528d3af3953af8b9f4e0652c6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a653d37860ce117c9e641c40a03c3136fb00b5934a98c02e47390709827c35b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1d29e6d74023817fd3f4556bd9ebbce2f3ff937573919888d54f981a58dacf6(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc38d18d8a1caa6b50577b7fc9eb6ac4fad15c49aba470e825bf78f9c2d14375(
    value: typing.Optional[MqBrokerConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9eb820a5cbfd01cfe293c75b10033ffe8d22d2e6b910605ea898ba0d1e69dad(
    *,
    kms_key_id: typing.Optional[builtins.str] = None,
    use_aws_owned_key: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2657e6ede4f4a1aa7884585665c32c59e65627975ee32dc9114487ee6671a043(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ef9df1820577dc1bfa266ca32b3e2f3da0406df7ca7374a55fa80a91beba77d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f34a67d326f7e78982f54f5740f6ce28451bcb9e49d31ff6a17ff4b1846e233c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dba6cf9227b6d173df4af851785faeccabad7a84e69fa43219860960119b7a7(
    value: typing.Optional[MqBrokerEncryptionOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae9d50133db03f1e1c17f617ba6a8822f944994f516440f584684a35b79a240e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58d223f75be32bff9a33bb99732bd1324d93261adc0f4d2b2f859ccf5a0bd5bf(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87151b8b93a0c28331cc5f6e55ab466c51be4ea13adddd749bed25f401b6adc8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a76ee80068d58ae2c4f985d7424d290f548bc4f1e04d9e286d38d7a5f1ca07ff(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__487bdc821c18c7aa45be2f953a6eac7357a26b99cf5af6da06d2d00f90dada77(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd11d25343b0a56c77a8f354f2268039489654589ff05785306662f6db295326(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2e83107abc35d5989c93562f5c6fd136e314e9075cff95fcfa28efdc159c917(
    value: typing.Optional[MqBrokerInstances],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbe4de5410c7c817f15ac4b63a79142aa2f6fabf2b4fe0e3c70ad1ddb5ff9054(
    *,
    hosts: typing.Optional[typing.Sequence[builtins.str]] = None,
    role_base: typing.Optional[builtins.str] = None,
    role_name: typing.Optional[builtins.str] = None,
    role_search_matching: typing.Optional[builtins.str] = None,
    role_search_subtree: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    service_account_password: typing.Optional[builtins.str] = None,
    service_account_username: typing.Optional[builtins.str] = None,
    user_base: typing.Optional[builtins.str] = None,
    user_role_name: typing.Optional[builtins.str] = None,
    user_search_matching: typing.Optional[builtins.str] = None,
    user_search_subtree: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c56dc3ee375258a655b3a6a92ff857b5ac239e61547a87719a1b97c278aad67b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__041a36ff8447cfb88e64a98b18e9a26d4bb608b0a2ee3d718122b2ed5134de59(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f89d0228ac6006eb50d1322e8be57ef588304a3b6b614affc742ef7fc631ca6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef07be9fb922a69ffd9e44830987a9507fdea149214201c39695f60998e4fc33(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdb94be9b190c09f439c60d01056057fd2b92972636976f39c7fba3811c0deea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1250ade6818f6af13b98562b7e21119cd77b22688eb82066eba4d90e76ee4dfc(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc8e4320792bc8f9b4381ff037023c04d1d0fb6d2957ebec747797ede6fb178f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffdafa8263caf04f0ab9f212092374b9dfec91e07eccc2102d07d2d21890a7bb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8770a227e81a38cb6daaa0528293c6f83c2ffcc61d2ab663dc1cae732eb1e6f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c2c88d83c8b4bca31e585fabb3da7638811c075dd58012e581f3385433448a0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da8d41d61cc708493d8b2b3c603a06c4b90c04ef523099a31970e084de184221(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8eb2ccec2828c3af10a9598b7fad9c6dd8734d145b8137f37c0748f91a6e7903(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd3a1a305b310fafd9d2c346c9ca7cdfe65996feadab6629b7cb29b44e629f4f(
    value: typing.Optional[MqBrokerLdapServerMetadata],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39baa8ecf0ad2d8742f809c1f51a3eb6fdb5a90cb3761da7e3462a12ffaa49bb(
    *,
    audit: typing.Optional[builtins.str] = None,
    general: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7eef2ccc6ed1f0c5116043d86064be26bac1ca0b78a7ca53d92dd5a2f7bf26a5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eabec2641730a9aa90956cfb6aaf7004169480dba954854d46ef34cc75810e9c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd4fb06fe6043aca5fa159e988528e35da042d794ea774320f6dad83412fc7cf(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__417123249973b6a97ce3a6a70eae19cedaeba976dd67264f4380b6e06364321d(
    value: typing.Optional[MqBrokerLogs],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c19bbd792355a0370991c89221a58549c158dac49e070289a13f41952229cb92(
    *,
    day_of_week: builtins.str,
    time_of_day: builtins.str,
    time_zone: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c8de5d8d75d774bb844c48ba20a80217fa574f9e00aa2f14a27dc62ae07fb5f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4088f851dcd1affa10b5df986e51b34052c02abd6be922ae646a8907e9058ac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aea1933fbb881aef36a4b170e663dda7b9172d4ecfdafe458d6bca3fa92f239a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db9d72720bcd900a8c37a4ab8e66a1375ef83ddb58a122e71003fd938c6cb21e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d1e23a0a25c46ee38755d6a184e86f6d3fb62c9529c3586541ccf80a29a4097(
    value: typing.Optional[MqBrokerMaintenanceWindowStartTime],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0783c00ab206ea1d58f5fbcff279993666d971c5f1575a58ff98d1e842248aae(
    *,
    create: typing.Optional[builtins.str] = None,
    delete: typing.Optional[builtins.str] = None,
    update: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__561c021e9df01a1aa90065a5de70ecc73a1918cc8dbe779908dc75af5ef5bb49(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6864fa5a47221adee9c6c1d5380c5a4b55a636d5667cd5bf7e536c5eb602ccac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__286480a5b1f23120d21a4055d153a9a6d9261c22d861f9ae5eab01d485c801f6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5276e66fc7d8eb834c1e9f75efb70fcd58e9dcf8a931472a2032963935a830dd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59ebbb263af8e54be3273d646fda03ef30088d087b04f8dae406c3f0da9d5a51(
    value: typing.Optional[typing.Union[MqBrokerTimeouts, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4119ed99371b9ea32e692c39bf81275131ec7f3299fb9e4df737f2b3ded3a19(
    *,
    password: builtins.str,
    username: builtins.str,
    console_access: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    groups: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__156cd202fee0ce9c1f8930c018f0684f1939e8c4818549e545684e50aaa978eb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d19a228d7b98dea34c4e470c1530c3053c85e2ae08d65418d65722eaa0d66d24(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9776f20cb86c65fc81b767d6bc1d43fb3e98db9b76dc0c4852761e8561a34b27(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa9d8ba2b6948b77a3f1bed5b2227a03b7dcbc6c6174c03a6fbdfd6376b75a67(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97a42a9d5a325ac8c363b210580efbebf463097359d72d5b2c90848d0022ca4c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38656617fe1c0ee9add850065694011a606aee82479a22ab20b6236f41b0159b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MqBrokerUser]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b57824e2bd8970cb0fbf9c252767c3d4311206bf3637d3a68c4647c70129c66(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be1d710bb8895528a4dad02a79f21ed937cddf798760a57498a207d041c06443(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1dc67b1748229e897f299feb066348e8359d879a6c8f0eaeab74a31af0c9a23(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7943f2a8dda515606803e4894dcc9485c706cb5357aa1c0572e2e2f0f5b1c350(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d11b8daf678e1ce10d9cf44363ba8b73406caec6427f042636a3abd2a3e03746(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5aa2219e06c4de30e81c195fff26103ec2e89414f179c5c7635bbd25b4d58c13(
    value: typing.Optional[typing.Union[MqBrokerUser, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
