'''
# `aws_cognito_user_pool`

Refer to the Terraform Registory for docs: [`aws_cognito_user_pool`](https://www.terraform.io/docs/providers/aws/r/cognito_user_pool).
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


class CognitoUserPool(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoUserPool.CognitoUserPool",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool aws_cognito_user_pool}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        account_recovery_setting: typing.Optional[typing.Union["CognitoUserPoolAccountRecoverySetting", typing.Dict[builtins.str, typing.Any]]] = None,
        admin_create_user_config: typing.Optional[typing.Union["CognitoUserPoolAdminCreateUserConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        alias_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
        auto_verified_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
        deletion_protection: typing.Optional[builtins.str] = None,
        device_configuration: typing.Optional[typing.Union["CognitoUserPoolDeviceConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        email_configuration: typing.Optional[typing.Union["CognitoUserPoolEmailConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        email_verification_message: typing.Optional[builtins.str] = None,
        email_verification_subject: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        lambda_config: typing.Optional[typing.Union["CognitoUserPoolLambdaConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        mfa_configuration: typing.Optional[builtins.str] = None,
        password_policy: typing.Optional[typing.Union["CognitoUserPoolPasswordPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        schema: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CognitoUserPoolSchema", typing.Dict[builtins.str, typing.Any]]]]] = None,
        sms_authentication_message: typing.Optional[builtins.str] = None,
        sms_configuration: typing.Optional[typing.Union["CognitoUserPoolSmsConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        sms_verification_message: typing.Optional[builtins.str] = None,
        software_token_mfa_configuration: typing.Optional[typing.Union["CognitoUserPoolSoftwareTokenMfaConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        user_attribute_update_settings: typing.Optional[typing.Union["CognitoUserPoolUserAttributeUpdateSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        username_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
        username_configuration: typing.Optional[typing.Union["CognitoUserPoolUsernameConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        user_pool_add_ons: typing.Optional[typing.Union["CognitoUserPoolUserPoolAddOns", typing.Dict[builtins.str, typing.Any]]] = None,
        verification_message_template: typing.Optional[typing.Union["CognitoUserPoolVerificationMessageTemplate", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool aws_cognito_user_pool} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#name CognitoUserPool#name}.
        :param account_recovery_setting: account_recovery_setting block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#account_recovery_setting CognitoUserPool#account_recovery_setting}
        :param admin_create_user_config: admin_create_user_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#admin_create_user_config CognitoUserPool#admin_create_user_config}
        :param alias_attributes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#alias_attributes CognitoUserPool#alias_attributes}.
        :param auto_verified_attributes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#auto_verified_attributes CognitoUserPool#auto_verified_attributes}.
        :param deletion_protection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#deletion_protection CognitoUserPool#deletion_protection}.
        :param device_configuration: device_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#device_configuration CognitoUserPool#device_configuration}
        :param email_configuration: email_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#email_configuration CognitoUserPool#email_configuration}
        :param email_verification_message: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#email_verification_message CognitoUserPool#email_verification_message}.
        :param email_verification_subject: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#email_verification_subject CognitoUserPool#email_verification_subject}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#id CognitoUserPool#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param lambda_config: lambda_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#lambda_config CognitoUserPool#lambda_config}
        :param mfa_configuration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#mfa_configuration CognitoUserPool#mfa_configuration}.
        :param password_policy: password_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#password_policy CognitoUserPool#password_policy}
        :param schema: schema block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#schema CognitoUserPool#schema}
        :param sms_authentication_message: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#sms_authentication_message CognitoUserPool#sms_authentication_message}.
        :param sms_configuration: sms_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#sms_configuration CognitoUserPool#sms_configuration}
        :param sms_verification_message: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#sms_verification_message CognitoUserPool#sms_verification_message}.
        :param software_token_mfa_configuration: software_token_mfa_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#software_token_mfa_configuration CognitoUserPool#software_token_mfa_configuration}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#tags CognitoUserPool#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#tags_all CognitoUserPool#tags_all}.
        :param user_attribute_update_settings: user_attribute_update_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#user_attribute_update_settings CognitoUserPool#user_attribute_update_settings}
        :param username_attributes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#username_attributes CognitoUserPool#username_attributes}.
        :param username_configuration: username_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#username_configuration CognitoUserPool#username_configuration}
        :param user_pool_add_ons: user_pool_add_ons block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#user_pool_add_ons CognitoUserPool#user_pool_add_ons}
        :param verification_message_template: verification_message_template block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#verification_message_template CognitoUserPool#verification_message_template}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06e1d3ff826ca7315cd3b6d7b32321e317e80234e7d73f28b6b65792dbec0d4d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CognitoUserPoolConfig(
            name=name,
            account_recovery_setting=account_recovery_setting,
            admin_create_user_config=admin_create_user_config,
            alias_attributes=alias_attributes,
            auto_verified_attributes=auto_verified_attributes,
            deletion_protection=deletion_protection,
            device_configuration=device_configuration,
            email_configuration=email_configuration,
            email_verification_message=email_verification_message,
            email_verification_subject=email_verification_subject,
            id=id,
            lambda_config=lambda_config,
            mfa_configuration=mfa_configuration,
            password_policy=password_policy,
            schema=schema,
            sms_authentication_message=sms_authentication_message,
            sms_configuration=sms_configuration,
            sms_verification_message=sms_verification_message,
            software_token_mfa_configuration=software_token_mfa_configuration,
            tags=tags,
            tags_all=tags_all,
            user_attribute_update_settings=user_attribute_update_settings,
            username_attributes=username_attributes,
            username_configuration=username_configuration,
            user_pool_add_ons=user_pool_add_ons,
            verification_message_template=verification_message_template,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAccountRecoverySetting")
    def put_account_recovery_setting(
        self,
        *,
        recovery_mechanism: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CognitoUserPoolAccountRecoverySettingRecoveryMechanism", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param recovery_mechanism: recovery_mechanism block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#recovery_mechanism CognitoUserPool#recovery_mechanism}
        '''
        value = CognitoUserPoolAccountRecoverySetting(
            recovery_mechanism=recovery_mechanism
        )

        return typing.cast(None, jsii.invoke(self, "putAccountRecoverySetting", [value]))

    @jsii.member(jsii_name="putAdminCreateUserConfig")
    def put_admin_create_user_config(
        self,
        *,
        allow_admin_create_user_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        invite_message_template: typing.Optional[typing.Union["CognitoUserPoolAdminCreateUserConfigInviteMessageTemplate", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param allow_admin_create_user_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#allow_admin_create_user_only CognitoUserPool#allow_admin_create_user_only}.
        :param invite_message_template: invite_message_template block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#invite_message_template CognitoUserPool#invite_message_template}
        '''
        value = CognitoUserPoolAdminCreateUserConfig(
            allow_admin_create_user_only=allow_admin_create_user_only,
            invite_message_template=invite_message_template,
        )

        return typing.cast(None, jsii.invoke(self, "putAdminCreateUserConfig", [value]))

    @jsii.member(jsii_name="putDeviceConfiguration")
    def put_device_configuration(
        self,
        *,
        challenge_required_on_new_device: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        device_only_remembered_on_user_prompt: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param challenge_required_on_new_device: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#challenge_required_on_new_device CognitoUserPool#challenge_required_on_new_device}.
        :param device_only_remembered_on_user_prompt: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#device_only_remembered_on_user_prompt CognitoUserPool#device_only_remembered_on_user_prompt}.
        '''
        value = CognitoUserPoolDeviceConfiguration(
            challenge_required_on_new_device=challenge_required_on_new_device,
            device_only_remembered_on_user_prompt=device_only_remembered_on_user_prompt,
        )

        return typing.cast(None, jsii.invoke(self, "putDeviceConfiguration", [value]))

    @jsii.member(jsii_name="putEmailConfiguration")
    def put_email_configuration(
        self,
        *,
        configuration_set: typing.Optional[builtins.str] = None,
        email_sending_account: typing.Optional[builtins.str] = None,
        from_email_address: typing.Optional[builtins.str] = None,
        reply_to_email_address: typing.Optional[builtins.str] = None,
        source_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param configuration_set: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#configuration_set CognitoUserPool#configuration_set}.
        :param email_sending_account: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#email_sending_account CognitoUserPool#email_sending_account}.
        :param from_email_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#from_email_address CognitoUserPool#from_email_address}.
        :param reply_to_email_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#reply_to_email_address CognitoUserPool#reply_to_email_address}.
        :param source_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#source_arn CognitoUserPool#source_arn}.
        '''
        value = CognitoUserPoolEmailConfiguration(
            configuration_set=configuration_set,
            email_sending_account=email_sending_account,
            from_email_address=from_email_address,
            reply_to_email_address=reply_to_email_address,
            source_arn=source_arn,
        )

        return typing.cast(None, jsii.invoke(self, "putEmailConfiguration", [value]))

    @jsii.member(jsii_name="putLambdaConfig")
    def put_lambda_config(
        self,
        *,
        create_auth_challenge: typing.Optional[builtins.str] = None,
        custom_email_sender: typing.Optional[typing.Union["CognitoUserPoolLambdaConfigCustomEmailSender", typing.Dict[builtins.str, typing.Any]]] = None,
        custom_message: typing.Optional[builtins.str] = None,
        custom_sms_sender: typing.Optional[typing.Union["CognitoUserPoolLambdaConfigCustomSmsSender", typing.Dict[builtins.str, typing.Any]]] = None,
        define_auth_challenge: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        post_authentication: typing.Optional[builtins.str] = None,
        post_confirmation: typing.Optional[builtins.str] = None,
        pre_authentication: typing.Optional[builtins.str] = None,
        pre_sign_up: typing.Optional[builtins.str] = None,
        pre_token_generation: typing.Optional[builtins.str] = None,
        user_migration: typing.Optional[builtins.str] = None,
        verify_auth_challenge_response: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create_auth_challenge: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#create_auth_challenge CognitoUserPool#create_auth_challenge}.
        :param custom_email_sender: custom_email_sender block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#custom_email_sender CognitoUserPool#custom_email_sender}
        :param custom_message: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#custom_message CognitoUserPool#custom_message}.
        :param custom_sms_sender: custom_sms_sender block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#custom_sms_sender CognitoUserPool#custom_sms_sender}
        :param define_auth_challenge: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#define_auth_challenge CognitoUserPool#define_auth_challenge}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#kms_key_id CognitoUserPool#kms_key_id}.
        :param post_authentication: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#post_authentication CognitoUserPool#post_authentication}.
        :param post_confirmation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#post_confirmation CognitoUserPool#post_confirmation}.
        :param pre_authentication: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#pre_authentication CognitoUserPool#pre_authentication}.
        :param pre_sign_up: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#pre_sign_up CognitoUserPool#pre_sign_up}.
        :param pre_token_generation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#pre_token_generation CognitoUserPool#pre_token_generation}.
        :param user_migration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#user_migration CognitoUserPool#user_migration}.
        :param verify_auth_challenge_response: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#verify_auth_challenge_response CognitoUserPool#verify_auth_challenge_response}.
        '''
        value = CognitoUserPoolLambdaConfig(
            create_auth_challenge=create_auth_challenge,
            custom_email_sender=custom_email_sender,
            custom_message=custom_message,
            custom_sms_sender=custom_sms_sender,
            define_auth_challenge=define_auth_challenge,
            kms_key_id=kms_key_id,
            post_authentication=post_authentication,
            post_confirmation=post_confirmation,
            pre_authentication=pre_authentication,
            pre_sign_up=pre_sign_up,
            pre_token_generation=pre_token_generation,
            user_migration=user_migration,
            verify_auth_challenge_response=verify_auth_challenge_response,
        )

        return typing.cast(None, jsii.invoke(self, "putLambdaConfig", [value]))

    @jsii.member(jsii_name="putPasswordPolicy")
    def put_password_policy(
        self,
        *,
        minimum_length: typing.Optional[jsii.Number] = None,
        require_lowercase: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        require_numbers: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        require_symbols: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        require_uppercase: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        temporary_password_validity_days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param minimum_length: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#minimum_length CognitoUserPool#minimum_length}.
        :param require_lowercase: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#require_lowercase CognitoUserPool#require_lowercase}.
        :param require_numbers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#require_numbers CognitoUserPool#require_numbers}.
        :param require_symbols: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#require_symbols CognitoUserPool#require_symbols}.
        :param require_uppercase: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#require_uppercase CognitoUserPool#require_uppercase}.
        :param temporary_password_validity_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#temporary_password_validity_days CognitoUserPool#temporary_password_validity_days}.
        '''
        value = CognitoUserPoolPasswordPolicy(
            minimum_length=minimum_length,
            require_lowercase=require_lowercase,
            require_numbers=require_numbers,
            require_symbols=require_symbols,
            require_uppercase=require_uppercase,
            temporary_password_validity_days=temporary_password_validity_days,
        )

        return typing.cast(None, jsii.invoke(self, "putPasswordPolicy", [value]))

    @jsii.member(jsii_name="putSchema")
    def put_schema(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CognitoUserPoolSchema", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__608ff9723e6a8c20ac963438358fa1967663cf505351d4e19aa3b4f256c8713b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSchema", [value]))

    @jsii.member(jsii_name="putSmsConfiguration")
    def put_sms_configuration(
        self,
        *,
        external_id: builtins.str,
        sns_caller_arn: builtins.str,
        sns_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param external_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#external_id CognitoUserPool#external_id}.
        :param sns_caller_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#sns_caller_arn CognitoUserPool#sns_caller_arn}.
        :param sns_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#sns_region CognitoUserPool#sns_region}.
        '''
        value = CognitoUserPoolSmsConfiguration(
            external_id=external_id,
            sns_caller_arn=sns_caller_arn,
            sns_region=sns_region,
        )

        return typing.cast(None, jsii.invoke(self, "putSmsConfiguration", [value]))

    @jsii.member(jsii_name="putSoftwareTokenMfaConfiguration")
    def put_software_token_mfa_configuration(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#enabled CognitoUserPool#enabled}.
        '''
        value = CognitoUserPoolSoftwareTokenMfaConfiguration(enabled=enabled)

        return typing.cast(None, jsii.invoke(self, "putSoftwareTokenMfaConfiguration", [value]))

    @jsii.member(jsii_name="putUserAttributeUpdateSettings")
    def put_user_attribute_update_settings(
        self,
        *,
        attributes_require_verification_before_update: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param attributes_require_verification_before_update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#attributes_require_verification_before_update CognitoUserPool#attributes_require_verification_before_update}.
        '''
        value = CognitoUserPoolUserAttributeUpdateSettings(
            attributes_require_verification_before_update=attributes_require_verification_before_update,
        )

        return typing.cast(None, jsii.invoke(self, "putUserAttributeUpdateSettings", [value]))

    @jsii.member(jsii_name="putUsernameConfiguration")
    def put_username_configuration(
        self,
        *,
        case_sensitive: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param case_sensitive: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#case_sensitive CognitoUserPool#case_sensitive}.
        '''
        value = CognitoUserPoolUsernameConfiguration(case_sensitive=case_sensitive)

        return typing.cast(None, jsii.invoke(self, "putUsernameConfiguration", [value]))

    @jsii.member(jsii_name="putUserPoolAddOns")
    def put_user_pool_add_ons(self, *, advanced_security_mode: builtins.str) -> None:
        '''
        :param advanced_security_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#advanced_security_mode CognitoUserPool#advanced_security_mode}.
        '''
        value = CognitoUserPoolUserPoolAddOns(
            advanced_security_mode=advanced_security_mode
        )

        return typing.cast(None, jsii.invoke(self, "putUserPoolAddOns", [value]))

    @jsii.member(jsii_name="putVerificationMessageTemplate")
    def put_verification_message_template(
        self,
        *,
        default_email_option: typing.Optional[builtins.str] = None,
        email_message: typing.Optional[builtins.str] = None,
        email_message_by_link: typing.Optional[builtins.str] = None,
        email_subject: typing.Optional[builtins.str] = None,
        email_subject_by_link: typing.Optional[builtins.str] = None,
        sms_message: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param default_email_option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#default_email_option CognitoUserPool#default_email_option}.
        :param email_message: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#email_message CognitoUserPool#email_message}.
        :param email_message_by_link: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#email_message_by_link CognitoUserPool#email_message_by_link}.
        :param email_subject: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#email_subject CognitoUserPool#email_subject}.
        :param email_subject_by_link: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#email_subject_by_link CognitoUserPool#email_subject_by_link}.
        :param sms_message: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#sms_message CognitoUserPool#sms_message}.
        '''
        value = CognitoUserPoolVerificationMessageTemplate(
            default_email_option=default_email_option,
            email_message=email_message,
            email_message_by_link=email_message_by_link,
            email_subject=email_subject,
            email_subject_by_link=email_subject_by_link,
            sms_message=sms_message,
        )

        return typing.cast(None, jsii.invoke(self, "putVerificationMessageTemplate", [value]))

    @jsii.member(jsii_name="resetAccountRecoverySetting")
    def reset_account_recovery_setting(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountRecoverySetting", []))

    @jsii.member(jsii_name="resetAdminCreateUserConfig")
    def reset_admin_create_user_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdminCreateUserConfig", []))

    @jsii.member(jsii_name="resetAliasAttributes")
    def reset_alias_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAliasAttributes", []))

    @jsii.member(jsii_name="resetAutoVerifiedAttributes")
    def reset_auto_verified_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoVerifiedAttributes", []))

    @jsii.member(jsii_name="resetDeletionProtection")
    def reset_deletion_protection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeletionProtection", []))

    @jsii.member(jsii_name="resetDeviceConfiguration")
    def reset_device_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeviceConfiguration", []))

    @jsii.member(jsii_name="resetEmailConfiguration")
    def reset_email_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailConfiguration", []))

    @jsii.member(jsii_name="resetEmailVerificationMessage")
    def reset_email_verification_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailVerificationMessage", []))

    @jsii.member(jsii_name="resetEmailVerificationSubject")
    def reset_email_verification_subject(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailVerificationSubject", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLambdaConfig")
    def reset_lambda_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLambdaConfig", []))

    @jsii.member(jsii_name="resetMfaConfiguration")
    def reset_mfa_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMfaConfiguration", []))

    @jsii.member(jsii_name="resetPasswordPolicy")
    def reset_password_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordPolicy", []))

    @jsii.member(jsii_name="resetSchema")
    def reset_schema(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchema", []))

    @jsii.member(jsii_name="resetSmsAuthenticationMessage")
    def reset_sms_authentication_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSmsAuthenticationMessage", []))

    @jsii.member(jsii_name="resetSmsConfiguration")
    def reset_sms_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSmsConfiguration", []))

    @jsii.member(jsii_name="resetSmsVerificationMessage")
    def reset_sms_verification_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSmsVerificationMessage", []))

    @jsii.member(jsii_name="resetSoftwareTokenMfaConfiguration")
    def reset_software_token_mfa_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSoftwareTokenMfaConfiguration", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetUserAttributeUpdateSettings")
    def reset_user_attribute_update_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserAttributeUpdateSettings", []))

    @jsii.member(jsii_name="resetUsernameAttributes")
    def reset_username_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsernameAttributes", []))

    @jsii.member(jsii_name="resetUsernameConfiguration")
    def reset_username_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsernameConfiguration", []))

    @jsii.member(jsii_name="resetUserPoolAddOns")
    def reset_user_pool_add_ons(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserPoolAddOns", []))

    @jsii.member(jsii_name="resetVerificationMessageTemplate")
    def reset_verification_message_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVerificationMessageTemplate", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="accountRecoverySetting")
    def account_recovery_setting(
        self,
    ) -> "CognitoUserPoolAccountRecoverySettingOutputReference":
        return typing.cast("CognitoUserPoolAccountRecoverySettingOutputReference", jsii.get(self, "accountRecoverySetting"))

    @builtins.property
    @jsii.member(jsii_name="adminCreateUserConfig")
    def admin_create_user_config(
        self,
    ) -> "CognitoUserPoolAdminCreateUserConfigOutputReference":
        return typing.cast("CognitoUserPoolAdminCreateUserConfigOutputReference", jsii.get(self, "adminCreateUserConfig"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="creationDate")
    def creation_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "creationDate"))

    @builtins.property
    @jsii.member(jsii_name="customDomain")
    def custom_domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customDomain"))

    @builtins.property
    @jsii.member(jsii_name="deviceConfiguration")
    def device_configuration(
        self,
    ) -> "CognitoUserPoolDeviceConfigurationOutputReference":
        return typing.cast("CognitoUserPoolDeviceConfigurationOutputReference", jsii.get(self, "deviceConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @builtins.property
    @jsii.member(jsii_name="emailConfiguration")
    def email_configuration(self) -> "CognitoUserPoolEmailConfigurationOutputReference":
        return typing.cast("CognitoUserPoolEmailConfigurationOutputReference", jsii.get(self, "emailConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @builtins.property
    @jsii.member(jsii_name="estimatedNumberOfUsers")
    def estimated_number_of_users(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "estimatedNumberOfUsers"))

    @builtins.property
    @jsii.member(jsii_name="lambdaConfig")
    def lambda_config(self) -> "CognitoUserPoolLambdaConfigOutputReference":
        return typing.cast("CognitoUserPoolLambdaConfigOutputReference", jsii.get(self, "lambdaConfig"))

    @builtins.property
    @jsii.member(jsii_name="lastModifiedDate")
    def last_modified_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastModifiedDate"))

    @builtins.property
    @jsii.member(jsii_name="passwordPolicy")
    def password_policy(self) -> "CognitoUserPoolPasswordPolicyOutputReference":
        return typing.cast("CognitoUserPoolPasswordPolicyOutputReference", jsii.get(self, "passwordPolicy"))

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(self) -> "CognitoUserPoolSchemaList":
        return typing.cast("CognitoUserPoolSchemaList", jsii.get(self, "schema"))

    @builtins.property
    @jsii.member(jsii_name="smsConfiguration")
    def sms_configuration(self) -> "CognitoUserPoolSmsConfigurationOutputReference":
        return typing.cast("CognitoUserPoolSmsConfigurationOutputReference", jsii.get(self, "smsConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="softwareTokenMfaConfiguration")
    def software_token_mfa_configuration(
        self,
    ) -> "CognitoUserPoolSoftwareTokenMfaConfigurationOutputReference":
        return typing.cast("CognitoUserPoolSoftwareTokenMfaConfigurationOutputReference", jsii.get(self, "softwareTokenMfaConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="userAttributeUpdateSettings")
    def user_attribute_update_settings(
        self,
    ) -> "CognitoUserPoolUserAttributeUpdateSettingsOutputReference":
        return typing.cast("CognitoUserPoolUserAttributeUpdateSettingsOutputReference", jsii.get(self, "userAttributeUpdateSettings"))

    @builtins.property
    @jsii.member(jsii_name="usernameConfiguration")
    def username_configuration(
        self,
    ) -> "CognitoUserPoolUsernameConfigurationOutputReference":
        return typing.cast("CognitoUserPoolUsernameConfigurationOutputReference", jsii.get(self, "usernameConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="userPoolAddOns")
    def user_pool_add_ons(self) -> "CognitoUserPoolUserPoolAddOnsOutputReference":
        return typing.cast("CognitoUserPoolUserPoolAddOnsOutputReference", jsii.get(self, "userPoolAddOns"))

    @builtins.property
    @jsii.member(jsii_name="verificationMessageTemplate")
    def verification_message_template(
        self,
    ) -> "CognitoUserPoolVerificationMessageTemplateOutputReference":
        return typing.cast("CognitoUserPoolVerificationMessageTemplateOutputReference", jsii.get(self, "verificationMessageTemplate"))

    @builtins.property
    @jsii.member(jsii_name="accountRecoverySettingInput")
    def account_recovery_setting_input(
        self,
    ) -> typing.Optional["CognitoUserPoolAccountRecoverySetting"]:
        return typing.cast(typing.Optional["CognitoUserPoolAccountRecoverySetting"], jsii.get(self, "accountRecoverySettingInput"))

    @builtins.property
    @jsii.member(jsii_name="adminCreateUserConfigInput")
    def admin_create_user_config_input(
        self,
    ) -> typing.Optional["CognitoUserPoolAdminCreateUserConfig"]:
        return typing.cast(typing.Optional["CognitoUserPoolAdminCreateUserConfig"], jsii.get(self, "adminCreateUserConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="aliasAttributesInput")
    def alias_attributes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "aliasAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="autoVerifiedAttributesInput")
    def auto_verified_attributes_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "autoVerifiedAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="deletionProtectionInput")
    def deletion_protection_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deletionProtectionInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceConfigurationInput")
    def device_configuration_input(
        self,
    ) -> typing.Optional["CognitoUserPoolDeviceConfiguration"]:
        return typing.cast(typing.Optional["CognitoUserPoolDeviceConfiguration"], jsii.get(self, "deviceConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="emailConfigurationInput")
    def email_configuration_input(
        self,
    ) -> typing.Optional["CognitoUserPoolEmailConfiguration"]:
        return typing.cast(typing.Optional["CognitoUserPoolEmailConfiguration"], jsii.get(self, "emailConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="emailVerificationMessageInput")
    def email_verification_message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailVerificationMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="emailVerificationSubjectInput")
    def email_verification_subject_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailVerificationSubjectInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaConfigInput")
    def lambda_config_input(self) -> typing.Optional["CognitoUserPoolLambdaConfig"]:
        return typing.cast(typing.Optional["CognitoUserPoolLambdaConfig"], jsii.get(self, "lambdaConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="mfaConfigurationInput")
    def mfa_configuration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mfaConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordPolicyInput")
    def password_policy_input(self) -> typing.Optional["CognitoUserPoolPasswordPolicy"]:
        return typing.cast(typing.Optional["CognitoUserPoolPasswordPolicy"], jsii.get(self, "passwordPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaInput")
    def schema_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CognitoUserPoolSchema"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CognitoUserPoolSchema"]]], jsii.get(self, "schemaInput"))

    @builtins.property
    @jsii.member(jsii_name="smsAuthenticationMessageInput")
    def sms_authentication_message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "smsAuthenticationMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="smsConfigurationInput")
    def sms_configuration_input(
        self,
    ) -> typing.Optional["CognitoUserPoolSmsConfiguration"]:
        return typing.cast(typing.Optional["CognitoUserPoolSmsConfiguration"], jsii.get(self, "smsConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="smsVerificationMessageInput")
    def sms_verification_message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "smsVerificationMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="softwareTokenMfaConfigurationInput")
    def software_token_mfa_configuration_input(
        self,
    ) -> typing.Optional["CognitoUserPoolSoftwareTokenMfaConfiguration"]:
        return typing.cast(typing.Optional["CognitoUserPoolSoftwareTokenMfaConfiguration"], jsii.get(self, "softwareTokenMfaConfigurationInput"))

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
    @jsii.member(jsii_name="userAttributeUpdateSettingsInput")
    def user_attribute_update_settings_input(
        self,
    ) -> typing.Optional["CognitoUserPoolUserAttributeUpdateSettings"]:
        return typing.cast(typing.Optional["CognitoUserPoolUserAttributeUpdateSettings"], jsii.get(self, "userAttributeUpdateSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameAttributesInput")
    def username_attributes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "usernameAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameConfigurationInput")
    def username_configuration_input(
        self,
    ) -> typing.Optional["CognitoUserPoolUsernameConfiguration"]:
        return typing.cast(typing.Optional["CognitoUserPoolUsernameConfiguration"], jsii.get(self, "usernameConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="userPoolAddOnsInput")
    def user_pool_add_ons_input(
        self,
    ) -> typing.Optional["CognitoUserPoolUserPoolAddOns"]:
        return typing.cast(typing.Optional["CognitoUserPoolUserPoolAddOns"], jsii.get(self, "userPoolAddOnsInput"))

    @builtins.property
    @jsii.member(jsii_name="verificationMessageTemplateInput")
    def verification_message_template_input(
        self,
    ) -> typing.Optional["CognitoUserPoolVerificationMessageTemplate"]:
        return typing.cast(typing.Optional["CognitoUserPoolVerificationMessageTemplate"], jsii.get(self, "verificationMessageTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="aliasAttributes")
    def alias_attributes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "aliasAttributes"))

    @alias_attributes.setter
    def alias_attributes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40cb89ce20c5565184911ff97db6324df1edbefdb5e330c5a3b011aee5732e40)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aliasAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="autoVerifiedAttributes")
    def auto_verified_attributes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "autoVerifiedAttributes"))

    @auto_verified_attributes.setter
    def auto_verified_attributes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cb88b8bc18d16a5e4b6bf9686a4802509d1971eb498b8d453719ecc072d70a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoVerifiedAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="deletionProtection")
    def deletion_protection(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deletionProtection"))

    @deletion_protection.setter
    def deletion_protection(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b30385f0e8c9b1870232afe1bb8d1d02b41301824fa1f749323a52966b328c1e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deletionProtection", value)

    @builtins.property
    @jsii.member(jsii_name="emailVerificationMessage")
    def email_verification_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emailVerificationMessage"))

    @email_verification_message.setter
    def email_verification_message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b634754503aedd6d6bd5d80e8cd1207fd9fa0060c44da01abad5643078dad6e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailVerificationMessage", value)

    @builtins.property
    @jsii.member(jsii_name="emailVerificationSubject")
    def email_verification_subject(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emailVerificationSubject"))

    @email_verification_subject.setter
    def email_verification_subject(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__828dcb94d1ffad079a59f24c1ab4c8c17ca7cb778d4e23258dd880c164ff6221)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailVerificationSubject", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ca97c8c4307b55a75e101acf168258c3d16e1df9abcc9f8c48c68672667c610)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="mfaConfiguration")
    def mfa_configuration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mfaConfiguration"))

    @mfa_configuration.setter
    def mfa_configuration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ec8dd242b38eea95411d6ad89d0acc26040bb50715dcc6eedae3e374f8ca245)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mfaConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f72b6a2cf09216a81ccd18c9d0610974e451865228b047f8eafcc0fe6fc21f4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="smsAuthenticationMessage")
    def sms_authentication_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "smsAuthenticationMessage"))

    @sms_authentication_message.setter
    def sms_authentication_message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f23dd9b76788e74cb18078c5f36cbce5453ff77b9128c746434c5d1b8bb7f136)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "smsAuthenticationMessage", value)

    @builtins.property
    @jsii.member(jsii_name="smsVerificationMessage")
    def sms_verification_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "smsVerificationMessage"))

    @sms_verification_message.setter
    def sms_verification_message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fc9db5855b1b6accf6ea213716a078279d83ec652c4ff0b6430740403bc2ef6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "smsVerificationMessage", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ba953fa001f32bbc87af3c3d8c349cbd0ddf23536d2afd6cf2da2f8ae017166)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bfb289bea30767ef4f952dff3db8e690d4fb063a6204bc0ee8b390b1eec9d6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="usernameAttributes")
    def username_attributes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "usernameAttributes"))

    @username_attributes.setter
    def username_attributes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fc24fdb86ac2ba14684e4f2efc5b334234ed0c8774f6c650a4b01103934e0a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usernameAttributes", value)


@jsii.data_type(
    jsii_type="aws.cognitoUserPool.CognitoUserPoolAccountRecoverySetting",
    jsii_struct_bases=[],
    name_mapping={"recovery_mechanism": "recoveryMechanism"},
)
class CognitoUserPoolAccountRecoverySetting:
    def __init__(
        self,
        *,
        recovery_mechanism: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CognitoUserPoolAccountRecoverySettingRecoveryMechanism", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param recovery_mechanism: recovery_mechanism block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#recovery_mechanism CognitoUserPool#recovery_mechanism}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a2a866a5eb8386d03fb01e5b24ef733b7c2c9aa33279f89612982d8c584520a)
            check_type(argname="argument recovery_mechanism", value=recovery_mechanism, expected_type=type_hints["recovery_mechanism"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "recovery_mechanism": recovery_mechanism,
        }

    @builtins.property
    def recovery_mechanism(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CognitoUserPoolAccountRecoverySettingRecoveryMechanism"]]:
        '''recovery_mechanism block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#recovery_mechanism CognitoUserPool#recovery_mechanism}
        '''
        result = self._values.get("recovery_mechanism")
        assert result is not None, "Required property 'recovery_mechanism' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CognitoUserPoolAccountRecoverySettingRecoveryMechanism"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoUserPoolAccountRecoverySetting(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CognitoUserPoolAccountRecoverySettingOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoUserPool.CognitoUserPoolAccountRecoverySettingOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__04bd0663f7d4db01b60ccda155b928f7fc17b7a0bb63b5a3d87bfba3c5cff618)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRecoveryMechanism")
    def put_recovery_mechanism(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CognitoUserPoolAccountRecoverySettingRecoveryMechanism", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74dfbba34806de912b0652a779d392752207e914599116b03ff615b3db35ca02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRecoveryMechanism", [value]))

    @builtins.property
    @jsii.member(jsii_name="recoveryMechanism")
    def recovery_mechanism(
        self,
    ) -> "CognitoUserPoolAccountRecoverySettingRecoveryMechanismList":
        return typing.cast("CognitoUserPoolAccountRecoverySettingRecoveryMechanismList", jsii.get(self, "recoveryMechanism"))

    @builtins.property
    @jsii.member(jsii_name="recoveryMechanismInput")
    def recovery_mechanism_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CognitoUserPoolAccountRecoverySettingRecoveryMechanism"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CognitoUserPoolAccountRecoverySettingRecoveryMechanism"]]], jsii.get(self, "recoveryMechanismInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CognitoUserPoolAccountRecoverySetting]:
        return typing.cast(typing.Optional[CognitoUserPoolAccountRecoverySetting], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoUserPoolAccountRecoverySetting],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3788d067c92d6017b6a530ddd9d5d0ea14fd177908e661e2dcd57ed1eb71be41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cognitoUserPool.CognitoUserPoolAccountRecoverySettingRecoveryMechanism",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "priority": "priority"},
)
class CognitoUserPoolAccountRecoverySettingRecoveryMechanism:
    def __init__(self, *, name: builtins.str, priority: jsii.Number) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#name CognitoUserPool#name}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#priority CognitoUserPool#priority}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd5566e78887d2d66ca142cb668f68d552c3b01e3b804e747f3cc769a066f642)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "priority": priority,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#name CognitoUserPool#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def priority(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#priority CognitoUserPool#priority}.'''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoUserPoolAccountRecoverySettingRecoveryMechanism(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CognitoUserPoolAccountRecoverySettingRecoveryMechanismList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoUserPool.CognitoUserPoolAccountRecoverySettingRecoveryMechanismList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e3c8c7bd71aa77675cfc0c4a71d58ed0aedf8b9f6de8b8bc64257320f0c98a7f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CognitoUserPoolAccountRecoverySettingRecoveryMechanismOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__011a813bc94e9050e4aa56fa252792c99c2c6f38c0574df69be4471577dbfae7)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CognitoUserPoolAccountRecoverySettingRecoveryMechanismOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__744bdb08d938e13b0343997d413d5a099f79965e03e87e9eec7a41fdafd044f2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e73378e2cc83d561c4daa10dbc3301d1c2b80ca0dfba49c5a6120c1907253109)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6aa239f7089e71cf31ab2c68496d9dc31fe3ff6f1a82b7e63604bfab4b568cfe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CognitoUserPoolAccountRecoverySettingRecoveryMechanism]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CognitoUserPoolAccountRecoverySettingRecoveryMechanism]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CognitoUserPoolAccountRecoverySettingRecoveryMechanism]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88c4e0b05d63844c08c6505c3c2f093ae65d26c2ffaf9b4ae8334fd120d03115)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CognitoUserPoolAccountRecoverySettingRecoveryMechanismOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoUserPool.CognitoUserPoolAccountRecoverySettingRecoveryMechanismOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5a4d947ae80ba814ae8357091f641ac2ec864965bc137712745c1cad07d1afeb)
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
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe8ab36d93a3a5290ad1904c70f17cd65a696727c38d36cdca522152149eb9c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f671f3639fee79d71a190de383a04e05780f09668fdb547809438410791086ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CognitoUserPoolAccountRecoverySettingRecoveryMechanism, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CognitoUserPoolAccountRecoverySettingRecoveryMechanism, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CognitoUserPoolAccountRecoverySettingRecoveryMechanism, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea718cd11203b1ea530e16ec43fdc629da5cc10ab47eaeeec1067e8220900822)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cognitoUserPool.CognitoUserPoolAdminCreateUserConfig",
    jsii_struct_bases=[],
    name_mapping={
        "allow_admin_create_user_only": "allowAdminCreateUserOnly",
        "invite_message_template": "inviteMessageTemplate",
    },
)
class CognitoUserPoolAdminCreateUserConfig:
    def __init__(
        self,
        *,
        allow_admin_create_user_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        invite_message_template: typing.Optional[typing.Union["CognitoUserPoolAdminCreateUserConfigInviteMessageTemplate", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param allow_admin_create_user_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#allow_admin_create_user_only CognitoUserPool#allow_admin_create_user_only}.
        :param invite_message_template: invite_message_template block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#invite_message_template CognitoUserPool#invite_message_template}
        '''
        if isinstance(invite_message_template, dict):
            invite_message_template = CognitoUserPoolAdminCreateUserConfigInviteMessageTemplate(**invite_message_template)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ed501c34d1ff99dbcef2b1b3b6b10ed4d56c4d444da22cadb74114818ca6dfa)
            check_type(argname="argument allow_admin_create_user_only", value=allow_admin_create_user_only, expected_type=type_hints["allow_admin_create_user_only"])
            check_type(argname="argument invite_message_template", value=invite_message_template, expected_type=type_hints["invite_message_template"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if allow_admin_create_user_only is not None:
            self._values["allow_admin_create_user_only"] = allow_admin_create_user_only
        if invite_message_template is not None:
            self._values["invite_message_template"] = invite_message_template

    @builtins.property
    def allow_admin_create_user_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#allow_admin_create_user_only CognitoUserPool#allow_admin_create_user_only}.'''
        result = self._values.get("allow_admin_create_user_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def invite_message_template(
        self,
    ) -> typing.Optional["CognitoUserPoolAdminCreateUserConfigInviteMessageTemplate"]:
        '''invite_message_template block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#invite_message_template CognitoUserPool#invite_message_template}
        '''
        result = self._values.get("invite_message_template")
        return typing.cast(typing.Optional["CognitoUserPoolAdminCreateUserConfigInviteMessageTemplate"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoUserPoolAdminCreateUserConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.cognitoUserPool.CognitoUserPoolAdminCreateUserConfigInviteMessageTemplate",
    jsii_struct_bases=[],
    name_mapping={
        "email_message": "emailMessage",
        "email_subject": "emailSubject",
        "sms_message": "smsMessage",
    },
)
class CognitoUserPoolAdminCreateUserConfigInviteMessageTemplate:
    def __init__(
        self,
        *,
        email_message: typing.Optional[builtins.str] = None,
        email_subject: typing.Optional[builtins.str] = None,
        sms_message: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param email_message: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#email_message CognitoUserPool#email_message}.
        :param email_subject: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#email_subject CognitoUserPool#email_subject}.
        :param sms_message: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#sms_message CognitoUserPool#sms_message}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aaf70e8b4b61546c54113f041cdefac184e711e839df05e14142e26e70d8a453)
            check_type(argname="argument email_message", value=email_message, expected_type=type_hints["email_message"])
            check_type(argname="argument email_subject", value=email_subject, expected_type=type_hints["email_subject"])
            check_type(argname="argument sms_message", value=sms_message, expected_type=type_hints["sms_message"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if email_message is not None:
            self._values["email_message"] = email_message
        if email_subject is not None:
            self._values["email_subject"] = email_subject
        if sms_message is not None:
            self._values["sms_message"] = sms_message

    @builtins.property
    def email_message(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#email_message CognitoUserPool#email_message}.'''
        result = self._values.get("email_message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def email_subject(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#email_subject CognitoUserPool#email_subject}.'''
        result = self._values.get("email_subject")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sms_message(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#sms_message CognitoUserPool#sms_message}.'''
        result = self._values.get("sms_message")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoUserPoolAdminCreateUserConfigInviteMessageTemplate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CognitoUserPoolAdminCreateUserConfigInviteMessageTemplateOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoUserPool.CognitoUserPoolAdminCreateUserConfigInviteMessageTemplateOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4d4e523f5b65f89c16e3e798c372bc703ba7d5a10c2e4374327bdc0cc57bb88c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEmailMessage")
    def reset_email_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailMessage", []))

    @jsii.member(jsii_name="resetEmailSubject")
    def reset_email_subject(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailSubject", []))

    @jsii.member(jsii_name="resetSmsMessage")
    def reset_sms_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSmsMessage", []))

    @builtins.property
    @jsii.member(jsii_name="emailMessageInput")
    def email_message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="emailSubjectInput")
    def email_subject_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailSubjectInput"))

    @builtins.property
    @jsii.member(jsii_name="smsMessageInput")
    def sms_message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "smsMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="emailMessage")
    def email_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emailMessage"))

    @email_message.setter
    def email_message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de7d20ad8a380fa5410a755011f8191b6519cdaa01cdd05966a140ca2291b458)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailMessage", value)

    @builtins.property
    @jsii.member(jsii_name="emailSubject")
    def email_subject(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emailSubject"))

    @email_subject.setter
    def email_subject(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1822f8b1e9276c616af6b2fab64ce0048728d9ba6743a6c1c8ab5515f4e2ef4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailSubject", value)

    @builtins.property
    @jsii.member(jsii_name="smsMessage")
    def sms_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "smsMessage"))

    @sms_message.setter
    def sms_message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a92f088781e1f5df77bbe4b77c92731278e092cc0bc1198f0204d7b0ff95530)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "smsMessage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CognitoUserPoolAdminCreateUserConfigInviteMessageTemplate]:
        return typing.cast(typing.Optional[CognitoUserPoolAdminCreateUserConfigInviteMessageTemplate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoUserPoolAdminCreateUserConfigInviteMessageTemplate],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40e84ce8462fd16f69c018d4c8d7cc704a6d9ed4bc0f650139c6f66f4a491300)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CognitoUserPoolAdminCreateUserConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoUserPool.CognitoUserPoolAdminCreateUserConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__732fa655ebd9d4092a152b2568aa669a5b7dc89c06b9f3a1cf8ff8d5fcd9ea36)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putInviteMessageTemplate")
    def put_invite_message_template(
        self,
        *,
        email_message: typing.Optional[builtins.str] = None,
        email_subject: typing.Optional[builtins.str] = None,
        sms_message: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param email_message: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#email_message CognitoUserPool#email_message}.
        :param email_subject: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#email_subject CognitoUserPool#email_subject}.
        :param sms_message: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#sms_message CognitoUserPool#sms_message}.
        '''
        value = CognitoUserPoolAdminCreateUserConfigInviteMessageTemplate(
            email_message=email_message,
            email_subject=email_subject,
            sms_message=sms_message,
        )

        return typing.cast(None, jsii.invoke(self, "putInviteMessageTemplate", [value]))

    @jsii.member(jsii_name="resetAllowAdminCreateUserOnly")
    def reset_allow_admin_create_user_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowAdminCreateUserOnly", []))

    @jsii.member(jsii_name="resetInviteMessageTemplate")
    def reset_invite_message_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInviteMessageTemplate", []))

    @builtins.property
    @jsii.member(jsii_name="inviteMessageTemplate")
    def invite_message_template(
        self,
    ) -> CognitoUserPoolAdminCreateUserConfigInviteMessageTemplateOutputReference:
        return typing.cast(CognitoUserPoolAdminCreateUserConfigInviteMessageTemplateOutputReference, jsii.get(self, "inviteMessageTemplate"))

    @builtins.property
    @jsii.member(jsii_name="allowAdminCreateUserOnlyInput")
    def allow_admin_create_user_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "allowAdminCreateUserOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="inviteMessageTemplateInput")
    def invite_message_template_input(
        self,
    ) -> typing.Optional[CognitoUserPoolAdminCreateUserConfigInviteMessageTemplate]:
        return typing.cast(typing.Optional[CognitoUserPoolAdminCreateUserConfigInviteMessageTemplate], jsii.get(self, "inviteMessageTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="allowAdminCreateUserOnly")
    def allow_admin_create_user_only(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "allowAdminCreateUserOnly"))

    @allow_admin_create_user_only.setter
    def allow_admin_create_user_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64f81e7291968f44223648aa4c9db295432e618d8b77636ac47ada4988019cd2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowAdminCreateUserOnly", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CognitoUserPoolAdminCreateUserConfig]:
        return typing.cast(typing.Optional[CognitoUserPoolAdminCreateUserConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoUserPoolAdminCreateUserConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1190de545fb089a7ec15d081df5cc68af9db7bbb57362b113e21c8b6a5c959f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cognitoUserPool.CognitoUserPoolConfig",
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
        "account_recovery_setting": "accountRecoverySetting",
        "admin_create_user_config": "adminCreateUserConfig",
        "alias_attributes": "aliasAttributes",
        "auto_verified_attributes": "autoVerifiedAttributes",
        "deletion_protection": "deletionProtection",
        "device_configuration": "deviceConfiguration",
        "email_configuration": "emailConfiguration",
        "email_verification_message": "emailVerificationMessage",
        "email_verification_subject": "emailVerificationSubject",
        "id": "id",
        "lambda_config": "lambdaConfig",
        "mfa_configuration": "mfaConfiguration",
        "password_policy": "passwordPolicy",
        "schema": "schema",
        "sms_authentication_message": "smsAuthenticationMessage",
        "sms_configuration": "smsConfiguration",
        "sms_verification_message": "smsVerificationMessage",
        "software_token_mfa_configuration": "softwareTokenMfaConfiguration",
        "tags": "tags",
        "tags_all": "tagsAll",
        "user_attribute_update_settings": "userAttributeUpdateSettings",
        "username_attributes": "usernameAttributes",
        "username_configuration": "usernameConfiguration",
        "user_pool_add_ons": "userPoolAddOns",
        "verification_message_template": "verificationMessageTemplate",
    },
)
class CognitoUserPoolConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        account_recovery_setting: typing.Optional[typing.Union[CognitoUserPoolAccountRecoverySetting, typing.Dict[builtins.str, typing.Any]]] = None,
        admin_create_user_config: typing.Optional[typing.Union[CognitoUserPoolAdminCreateUserConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        alias_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
        auto_verified_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
        deletion_protection: typing.Optional[builtins.str] = None,
        device_configuration: typing.Optional[typing.Union["CognitoUserPoolDeviceConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        email_configuration: typing.Optional[typing.Union["CognitoUserPoolEmailConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        email_verification_message: typing.Optional[builtins.str] = None,
        email_verification_subject: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        lambda_config: typing.Optional[typing.Union["CognitoUserPoolLambdaConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        mfa_configuration: typing.Optional[builtins.str] = None,
        password_policy: typing.Optional[typing.Union["CognitoUserPoolPasswordPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        schema: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CognitoUserPoolSchema", typing.Dict[builtins.str, typing.Any]]]]] = None,
        sms_authentication_message: typing.Optional[builtins.str] = None,
        sms_configuration: typing.Optional[typing.Union["CognitoUserPoolSmsConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        sms_verification_message: typing.Optional[builtins.str] = None,
        software_token_mfa_configuration: typing.Optional[typing.Union["CognitoUserPoolSoftwareTokenMfaConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        user_attribute_update_settings: typing.Optional[typing.Union["CognitoUserPoolUserAttributeUpdateSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        username_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
        username_configuration: typing.Optional[typing.Union["CognitoUserPoolUsernameConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        user_pool_add_ons: typing.Optional[typing.Union["CognitoUserPoolUserPoolAddOns", typing.Dict[builtins.str, typing.Any]]] = None,
        verification_message_template: typing.Optional[typing.Union["CognitoUserPoolVerificationMessageTemplate", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#name CognitoUserPool#name}.
        :param account_recovery_setting: account_recovery_setting block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#account_recovery_setting CognitoUserPool#account_recovery_setting}
        :param admin_create_user_config: admin_create_user_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#admin_create_user_config CognitoUserPool#admin_create_user_config}
        :param alias_attributes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#alias_attributes CognitoUserPool#alias_attributes}.
        :param auto_verified_attributes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#auto_verified_attributes CognitoUserPool#auto_verified_attributes}.
        :param deletion_protection: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#deletion_protection CognitoUserPool#deletion_protection}.
        :param device_configuration: device_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#device_configuration CognitoUserPool#device_configuration}
        :param email_configuration: email_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#email_configuration CognitoUserPool#email_configuration}
        :param email_verification_message: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#email_verification_message CognitoUserPool#email_verification_message}.
        :param email_verification_subject: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#email_verification_subject CognitoUserPool#email_verification_subject}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#id CognitoUserPool#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param lambda_config: lambda_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#lambda_config CognitoUserPool#lambda_config}
        :param mfa_configuration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#mfa_configuration CognitoUserPool#mfa_configuration}.
        :param password_policy: password_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#password_policy CognitoUserPool#password_policy}
        :param schema: schema block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#schema CognitoUserPool#schema}
        :param sms_authentication_message: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#sms_authentication_message CognitoUserPool#sms_authentication_message}.
        :param sms_configuration: sms_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#sms_configuration CognitoUserPool#sms_configuration}
        :param sms_verification_message: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#sms_verification_message CognitoUserPool#sms_verification_message}.
        :param software_token_mfa_configuration: software_token_mfa_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#software_token_mfa_configuration CognitoUserPool#software_token_mfa_configuration}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#tags CognitoUserPool#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#tags_all CognitoUserPool#tags_all}.
        :param user_attribute_update_settings: user_attribute_update_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#user_attribute_update_settings CognitoUserPool#user_attribute_update_settings}
        :param username_attributes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#username_attributes CognitoUserPool#username_attributes}.
        :param username_configuration: username_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#username_configuration CognitoUserPool#username_configuration}
        :param user_pool_add_ons: user_pool_add_ons block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#user_pool_add_ons CognitoUserPool#user_pool_add_ons}
        :param verification_message_template: verification_message_template block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#verification_message_template CognitoUserPool#verification_message_template}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(account_recovery_setting, dict):
            account_recovery_setting = CognitoUserPoolAccountRecoverySetting(**account_recovery_setting)
        if isinstance(admin_create_user_config, dict):
            admin_create_user_config = CognitoUserPoolAdminCreateUserConfig(**admin_create_user_config)
        if isinstance(device_configuration, dict):
            device_configuration = CognitoUserPoolDeviceConfiguration(**device_configuration)
        if isinstance(email_configuration, dict):
            email_configuration = CognitoUserPoolEmailConfiguration(**email_configuration)
        if isinstance(lambda_config, dict):
            lambda_config = CognitoUserPoolLambdaConfig(**lambda_config)
        if isinstance(password_policy, dict):
            password_policy = CognitoUserPoolPasswordPolicy(**password_policy)
        if isinstance(sms_configuration, dict):
            sms_configuration = CognitoUserPoolSmsConfiguration(**sms_configuration)
        if isinstance(software_token_mfa_configuration, dict):
            software_token_mfa_configuration = CognitoUserPoolSoftwareTokenMfaConfiguration(**software_token_mfa_configuration)
        if isinstance(user_attribute_update_settings, dict):
            user_attribute_update_settings = CognitoUserPoolUserAttributeUpdateSettings(**user_attribute_update_settings)
        if isinstance(username_configuration, dict):
            username_configuration = CognitoUserPoolUsernameConfiguration(**username_configuration)
        if isinstance(user_pool_add_ons, dict):
            user_pool_add_ons = CognitoUserPoolUserPoolAddOns(**user_pool_add_ons)
        if isinstance(verification_message_template, dict):
            verification_message_template = CognitoUserPoolVerificationMessageTemplate(**verification_message_template)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9065476a5f52e9e06ca579c683af1ee03b7bd5ce59c489f0c8f9f4479bac0595)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument account_recovery_setting", value=account_recovery_setting, expected_type=type_hints["account_recovery_setting"])
            check_type(argname="argument admin_create_user_config", value=admin_create_user_config, expected_type=type_hints["admin_create_user_config"])
            check_type(argname="argument alias_attributes", value=alias_attributes, expected_type=type_hints["alias_attributes"])
            check_type(argname="argument auto_verified_attributes", value=auto_verified_attributes, expected_type=type_hints["auto_verified_attributes"])
            check_type(argname="argument deletion_protection", value=deletion_protection, expected_type=type_hints["deletion_protection"])
            check_type(argname="argument device_configuration", value=device_configuration, expected_type=type_hints["device_configuration"])
            check_type(argname="argument email_configuration", value=email_configuration, expected_type=type_hints["email_configuration"])
            check_type(argname="argument email_verification_message", value=email_verification_message, expected_type=type_hints["email_verification_message"])
            check_type(argname="argument email_verification_subject", value=email_verification_subject, expected_type=type_hints["email_verification_subject"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument lambda_config", value=lambda_config, expected_type=type_hints["lambda_config"])
            check_type(argname="argument mfa_configuration", value=mfa_configuration, expected_type=type_hints["mfa_configuration"])
            check_type(argname="argument password_policy", value=password_policy, expected_type=type_hints["password_policy"])
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            check_type(argname="argument sms_authentication_message", value=sms_authentication_message, expected_type=type_hints["sms_authentication_message"])
            check_type(argname="argument sms_configuration", value=sms_configuration, expected_type=type_hints["sms_configuration"])
            check_type(argname="argument sms_verification_message", value=sms_verification_message, expected_type=type_hints["sms_verification_message"])
            check_type(argname="argument software_token_mfa_configuration", value=software_token_mfa_configuration, expected_type=type_hints["software_token_mfa_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument user_attribute_update_settings", value=user_attribute_update_settings, expected_type=type_hints["user_attribute_update_settings"])
            check_type(argname="argument username_attributes", value=username_attributes, expected_type=type_hints["username_attributes"])
            check_type(argname="argument username_configuration", value=username_configuration, expected_type=type_hints["username_configuration"])
            check_type(argname="argument user_pool_add_ons", value=user_pool_add_ons, expected_type=type_hints["user_pool_add_ons"])
            check_type(argname="argument verification_message_template", value=verification_message_template, expected_type=type_hints["verification_message_template"])
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
        if account_recovery_setting is not None:
            self._values["account_recovery_setting"] = account_recovery_setting
        if admin_create_user_config is not None:
            self._values["admin_create_user_config"] = admin_create_user_config
        if alias_attributes is not None:
            self._values["alias_attributes"] = alias_attributes
        if auto_verified_attributes is not None:
            self._values["auto_verified_attributes"] = auto_verified_attributes
        if deletion_protection is not None:
            self._values["deletion_protection"] = deletion_protection
        if device_configuration is not None:
            self._values["device_configuration"] = device_configuration
        if email_configuration is not None:
            self._values["email_configuration"] = email_configuration
        if email_verification_message is not None:
            self._values["email_verification_message"] = email_verification_message
        if email_verification_subject is not None:
            self._values["email_verification_subject"] = email_verification_subject
        if id is not None:
            self._values["id"] = id
        if lambda_config is not None:
            self._values["lambda_config"] = lambda_config
        if mfa_configuration is not None:
            self._values["mfa_configuration"] = mfa_configuration
        if password_policy is not None:
            self._values["password_policy"] = password_policy
        if schema is not None:
            self._values["schema"] = schema
        if sms_authentication_message is not None:
            self._values["sms_authentication_message"] = sms_authentication_message
        if sms_configuration is not None:
            self._values["sms_configuration"] = sms_configuration
        if sms_verification_message is not None:
            self._values["sms_verification_message"] = sms_verification_message
        if software_token_mfa_configuration is not None:
            self._values["software_token_mfa_configuration"] = software_token_mfa_configuration
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if user_attribute_update_settings is not None:
            self._values["user_attribute_update_settings"] = user_attribute_update_settings
        if username_attributes is not None:
            self._values["username_attributes"] = username_attributes
        if username_configuration is not None:
            self._values["username_configuration"] = username_configuration
        if user_pool_add_ons is not None:
            self._values["user_pool_add_ons"] = user_pool_add_ons
        if verification_message_template is not None:
            self._values["verification_message_template"] = verification_message_template

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#name CognitoUserPool#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_recovery_setting(
        self,
    ) -> typing.Optional[CognitoUserPoolAccountRecoverySetting]:
        '''account_recovery_setting block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#account_recovery_setting CognitoUserPool#account_recovery_setting}
        '''
        result = self._values.get("account_recovery_setting")
        return typing.cast(typing.Optional[CognitoUserPoolAccountRecoverySetting], result)

    @builtins.property
    def admin_create_user_config(
        self,
    ) -> typing.Optional[CognitoUserPoolAdminCreateUserConfig]:
        '''admin_create_user_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#admin_create_user_config CognitoUserPool#admin_create_user_config}
        '''
        result = self._values.get("admin_create_user_config")
        return typing.cast(typing.Optional[CognitoUserPoolAdminCreateUserConfig], result)

    @builtins.property
    def alias_attributes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#alias_attributes CognitoUserPool#alias_attributes}.'''
        result = self._values.get("alias_attributes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def auto_verified_attributes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#auto_verified_attributes CognitoUserPool#auto_verified_attributes}.'''
        result = self._values.get("auto_verified_attributes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def deletion_protection(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#deletion_protection CognitoUserPool#deletion_protection}.'''
        result = self._values.get("deletion_protection")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def device_configuration(
        self,
    ) -> typing.Optional["CognitoUserPoolDeviceConfiguration"]:
        '''device_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#device_configuration CognitoUserPool#device_configuration}
        '''
        result = self._values.get("device_configuration")
        return typing.cast(typing.Optional["CognitoUserPoolDeviceConfiguration"], result)

    @builtins.property
    def email_configuration(
        self,
    ) -> typing.Optional["CognitoUserPoolEmailConfiguration"]:
        '''email_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#email_configuration CognitoUserPool#email_configuration}
        '''
        result = self._values.get("email_configuration")
        return typing.cast(typing.Optional["CognitoUserPoolEmailConfiguration"], result)

    @builtins.property
    def email_verification_message(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#email_verification_message CognitoUserPool#email_verification_message}.'''
        result = self._values.get("email_verification_message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def email_verification_subject(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#email_verification_subject CognitoUserPool#email_verification_subject}.'''
        result = self._values.get("email_verification_subject")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#id CognitoUserPool#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lambda_config(self) -> typing.Optional["CognitoUserPoolLambdaConfig"]:
        '''lambda_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#lambda_config CognitoUserPool#lambda_config}
        '''
        result = self._values.get("lambda_config")
        return typing.cast(typing.Optional["CognitoUserPoolLambdaConfig"], result)

    @builtins.property
    def mfa_configuration(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#mfa_configuration CognitoUserPool#mfa_configuration}.'''
        result = self._values.get("mfa_configuration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password_policy(self) -> typing.Optional["CognitoUserPoolPasswordPolicy"]:
        '''password_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#password_policy CognitoUserPool#password_policy}
        '''
        result = self._values.get("password_policy")
        return typing.cast(typing.Optional["CognitoUserPoolPasswordPolicy"], result)

    @builtins.property
    def schema(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CognitoUserPoolSchema"]]]:
        '''schema block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#schema CognitoUserPool#schema}
        '''
        result = self._values.get("schema")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CognitoUserPoolSchema"]]], result)

    @builtins.property
    def sms_authentication_message(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#sms_authentication_message CognitoUserPool#sms_authentication_message}.'''
        result = self._values.get("sms_authentication_message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sms_configuration(self) -> typing.Optional["CognitoUserPoolSmsConfiguration"]:
        '''sms_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#sms_configuration CognitoUserPool#sms_configuration}
        '''
        result = self._values.get("sms_configuration")
        return typing.cast(typing.Optional["CognitoUserPoolSmsConfiguration"], result)

    @builtins.property
    def sms_verification_message(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#sms_verification_message CognitoUserPool#sms_verification_message}.'''
        result = self._values.get("sms_verification_message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def software_token_mfa_configuration(
        self,
    ) -> typing.Optional["CognitoUserPoolSoftwareTokenMfaConfiguration"]:
        '''software_token_mfa_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#software_token_mfa_configuration CognitoUserPool#software_token_mfa_configuration}
        '''
        result = self._values.get("software_token_mfa_configuration")
        return typing.cast(typing.Optional["CognitoUserPoolSoftwareTokenMfaConfiguration"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#tags CognitoUserPool#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#tags_all CognitoUserPool#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def user_attribute_update_settings(
        self,
    ) -> typing.Optional["CognitoUserPoolUserAttributeUpdateSettings"]:
        '''user_attribute_update_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#user_attribute_update_settings CognitoUserPool#user_attribute_update_settings}
        '''
        result = self._values.get("user_attribute_update_settings")
        return typing.cast(typing.Optional["CognitoUserPoolUserAttributeUpdateSettings"], result)

    @builtins.property
    def username_attributes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#username_attributes CognitoUserPool#username_attributes}.'''
        result = self._values.get("username_attributes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def username_configuration(
        self,
    ) -> typing.Optional["CognitoUserPoolUsernameConfiguration"]:
        '''username_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#username_configuration CognitoUserPool#username_configuration}
        '''
        result = self._values.get("username_configuration")
        return typing.cast(typing.Optional["CognitoUserPoolUsernameConfiguration"], result)

    @builtins.property
    def user_pool_add_ons(self) -> typing.Optional["CognitoUserPoolUserPoolAddOns"]:
        '''user_pool_add_ons block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#user_pool_add_ons CognitoUserPool#user_pool_add_ons}
        '''
        result = self._values.get("user_pool_add_ons")
        return typing.cast(typing.Optional["CognitoUserPoolUserPoolAddOns"], result)

    @builtins.property
    def verification_message_template(
        self,
    ) -> typing.Optional["CognitoUserPoolVerificationMessageTemplate"]:
        '''verification_message_template block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#verification_message_template CognitoUserPool#verification_message_template}
        '''
        result = self._values.get("verification_message_template")
        return typing.cast(typing.Optional["CognitoUserPoolVerificationMessageTemplate"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoUserPoolConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.cognitoUserPool.CognitoUserPoolDeviceConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "challenge_required_on_new_device": "challengeRequiredOnNewDevice",
        "device_only_remembered_on_user_prompt": "deviceOnlyRememberedOnUserPrompt",
    },
)
class CognitoUserPoolDeviceConfiguration:
    def __init__(
        self,
        *,
        challenge_required_on_new_device: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        device_only_remembered_on_user_prompt: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param challenge_required_on_new_device: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#challenge_required_on_new_device CognitoUserPool#challenge_required_on_new_device}.
        :param device_only_remembered_on_user_prompt: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#device_only_remembered_on_user_prompt CognitoUserPool#device_only_remembered_on_user_prompt}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a010cf5c2f46551a912f7a77be663271213feb8536142d46832f3161be48415)
            check_type(argname="argument challenge_required_on_new_device", value=challenge_required_on_new_device, expected_type=type_hints["challenge_required_on_new_device"])
            check_type(argname="argument device_only_remembered_on_user_prompt", value=device_only_remembered_on_user_prompt, expected_type=type_hints["device_only_remembered_on_user_prompt"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if challenge_required_on_new_device is not None:
            self._values["challenge_required_on_new_device"] = challenge_required_on_new_device
        if device_only_remembered_on_user_prompt is not None:
            self._values["device_only_remembered_on_user_prompt"] = device_only_remembered_on_user_prompt

    @builtins.property
    def challenge_required_on_new_device(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#challenge_required_on_new_device CognitoUserPool#challenge_required_on_new_device}.'''
        result = self._values.get("challenge_required_on_new_device")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def device_only_remembered_on_user_prompt(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#device_only_remembered_on_user_prompt CognitoUserPool#device_only_remembered_on_user_prompt}.'''
        result = self._values.get("device_only_remembered_on_user_prompt")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoUserPoolDeviceConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CognitoUserPoolDeviceConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoUserPool.CognitoUserPoolDeviceConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d8cff7c1cd338c00a47a1e60cc2b8ee99f8490040f748b66508f59f47b363c70)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetChallengeRequiredOnNewDevice")
    def reset_challenge_required_on_new_device(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetChallengeRequiredOnNewDevice", []))

    @jsii.member(jsii_name="resetDeviceOnlyRememberedOnUserPrompt")
    def reset_device_only_remembered_on_user_prompt(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeviceOnlyRememberedOnUserPrompt", []))

    @builtins.property
    @jsii.member(jsii_name="challengeRequiredOnNewDeviceInput")
    def challenge_required_on_new_device_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "challengeRequiredOnNewDeviceInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceOnlyRememberedOnUserPromptInput")
    def device_only_remembered_on_user_prompt_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "deviceOnlyRememberedOnUserPromptInput"))

    @builtins.property
    @jsii.member(jsii_name="challengeRequiredOnNewDevice")
    def challenge_required_on_new_device(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "challengeRequiredOnNewDevice"))

    @challenge_required_on_new_device.setter
    def challenge_required_on_new_device(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d2b44741949b636c9b2e2ef9b748e3c20b6a400966235731e87c1b6b79a48c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "challengeRequiredOnNewDevice", value)

    @builtins.property
    @jsii.member(jsii_name="deviceOnlyRememberedOnUserPrompt")
    def device_only_remembered_on_user_prompt(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "deviceOnlyRememberedOnUserPrompt"))

    @device_only_remembered_on_user_prompt.setter
    def device_only_remembered_on_user_prompt(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b2359a13cc9f037bceceb36c6d4aa3051e7dcf51e60df9461298273d1d83bd2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceOnlyRememberedOnUserPrompt", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CognitoUserPoolDeviceConfiguration]:
        return typing.cast(typing.Optional[CognitoUserPoolDeviceConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoUserPoolDeviceConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45fe1421fcae7af911426355c53165fb9cd650040ef479835f5e4732c5a2aa09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cognitoUserPool.CognitoUserPoolEmailConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "configuration_set": "configurationSet",
        "email_sending_account": "emailSendingAccount",
        "from_email_address": "fromEmailAddress",
        "reply_to_email_address": "replyToEmailAddress",
        "source_arn": "sourceArn",
    },
)
class CognitoUserPoolEmailConfiguration:
    def __init__(
        self,
        *,
        configuration_set: typing.Optional[builtins.str] = None,
        email_sending_account: typing.Optional[builtins.str] = None,
        from_email_address: typing.Optional[builtins.str] = None,
        reply_to_email_address: typing.Optional[builtins.str] = None,
        source_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param configuration_set: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#configuration_set CognitoUserPool#configuration_set}.
        :param email_sending_account: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#email_sending_account CognitoUserPool#email_sending_account}.
        :param from_email_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#from_email_address CognitoUserPool#from_email_address}.
        :param reply_to_email_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#reply_to_email_address CognitoUserPool#reply_to_email_address}.
        :param source_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#source_arn CognitoUserPool#source_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7fb4ed4151b6a7671bfebf1c6751d2878ca00fdf83370c14026cbd59047e383)
            check_type(argname="argument configuration_set", value=configuration_set, expected_type=type_hints["configuration_set"])
            check_type(argname="argument email_sending_account", value=email_sending_account, expected_type=type_hints["email_sending_account"])
            check_type(argname="argument from_email_address", value=from_email_address, expected_type=type_hints["from_email_address"])
            check_type(argname="argument reply_to_email_address", value=reply_to_email_address, expected_type=type_hints["reply_to_email_address"])
            check_type(argname="argument source_arn", value=source_arn, expected_type=type_hints["source_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if configuration_set is not None:
            self._values["configuration_set"] = configuration_set
        if email_sending_account is not None:
            self._values["email_sending_account"] = email_sending_account
        if from_email_address is not None:
            self._values["from_email_address"] = from_email_address
        if reply_to_email_address is not None:
            self._values["reply_to_email_address"] = reply_to_email_address
        if source_arn is not None:
            self._values["source_arn"] = source_arn

    @builtins.property
    def configuration_set(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#configuration_set CognitoUserPool#configuration_set}.'''
        result = self._values.get("configuration_set")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def email_sending_account(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#email_sending_account CognitoUserPool#email_sending_account}.'''
        result = self._values.get("email_sending_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def from_email_address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#from_email_address CognitoUserPool#from_email_address}.'''
        result = self._values.get("from_email_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def reply_to_email_address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#reply_to_email_address CognitoUserPool#reply_to_email_address}.'''
        result = self._values.get("reply_to_email_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#source_arn CognitoUserPool#source_arn}.'''
        result = self._values.get("source_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoUserPoolEmailConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CognitoUserPoolEmailConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoUserPool.CognitoUserPoolEmailConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fb84ee699ee5393d85add1a17660b3ef7313fab0bfbe1b8d15b268c311d78346)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetConfigurationSet")
    def reset_configuration_set(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigurationSet", []))

    @jsii.member(jsii_name="resetEmailSendingAccount")
    def reset_email_sending_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailSendingAccount", []))

    @jsii.member(jsii_name="resetFromEmailAddress")
    def reset_from_email_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFromEmailAddress", []))

    @jsii.member(jsii_name="resetReplyToEmailAddress")
    def reset_reply_to_email_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplyToEmailAddress", []))

    @jsii.member(jsii_name="resetSourceArn")
    def reset_source_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceArn", []))

    @builtins.property
    @jsii.member(jsii_name="configurationSetInput")
    def configuration_set_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configurationSetInput"))

    @builtins.property
    @jsii.member(jsii_name="emailSendingAccountInput")
    def email_sending_account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailSendingAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="fromEmailAddressInput")
    def from_email_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fromEmailAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="replyToEmailAddressInput")
    def reply_to_email_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replyToEmailAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceArnInput")
    def source_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceArnInput"))

    @builtins.property
    @jsii.member(jsii_name="configurationSet")
    def configuration_set(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configurationSet"))

    @configuration_set.setter
    def configuration_set(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94f05606213b48cb26e806104fca7b6c1df028639b0a2ba01baee0afb449c200)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationSet", value)

    @builtins.property
    @jsii.member(jsii_name="emailSendingAccount")
    def email_sending_account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emailSendingAccount"))

    @email_sending_account.setter
    def email_sending_account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__049fea58f45309d4e95f7a0aa108809d77a525b1d96e0db7a0141a908a6dd259)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailSendingAccount", value)

    @builtins.property
    @jsii.member(jsii_name="fromEmailAddress")
    def from_email_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fromEmailAddress"))

    @from_email_address.setter
    def from_email_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8310772714b880365abb03deb0e893a100ee9a51d730e5f62d3b0f584eecab26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fromEmailAddress", value)

    @builtins.property
    @jsii.member(jsii_name="replyToEmailAddress")
    def reply_to_email_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replyToEmailAddress"))

    @reply_to_email_address.setter
    def reply_to_email_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__199ab049940fdd83c494118073f078fc58845b4ba609e6c085a0e90fcd463f47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replyToEmailAddress", value)

    @builtins.property
    @jsii.member(jsii_name="sourceArn")
    def source_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceArn"))

    @source_arn.setter
    def source_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de1a389a1c6f207fd1f6f04957c11437d71d2f8eb2ae81f8cb38907586892116)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CognitoUserPoolEmailConfiguration]:
        return typing.cast(typing.Optional[CognitoUserPoolEmailConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoUserPoolEmailConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__325a9c2a620154d9796da0a0d8d695aa02ade190732b3e41e62b424334f65655)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cognitoUserPool.CognitoUserPoolLambdaConfig",
    jsii_struct_bases=[],
    name_mapping={
        "create_auth_challenge": "createAuthChallenge",
        "custom_email_sender": "customEmailSender",
        "custom_message": "customMessage",
        "custom_sms_sender": "customSmsSender",
        "define_auth_challenge": "defineAuthChallenge",
        "kms_key_id": "kmsKeyId",
        "post_authentication": "postAuthentication",
        "post_confirmation": "postConfirmation",
        "pre_authentication": "preAuthentication",
        "pre_sign_up": "preSignUp",
        "pre_token_generation": "preTokenGeneration",
        "user_migration": "userMigration",
        "verify_auth_challenge_response": "verifyAuthChallengeResponse",
    },
)
class CognitoUserPoolLambdaConfig:
    def __init__(
        self,
        *,
        create_auth_challenge: typing.Optional[builtins.str] = None,
        custom_email_sender: typing.Optional[typing.Union["CognitoUserPoolLambdaConfigCustomEmailSender", typing.Dict[builtins.str, typing.Any]]] = None,
        custom_message: typing.Optional[builtins.str] = None,
        custom_sms_sender: typing.Optional[typing.Union["CognitoUserPoolLambdaConfigCustomSmsSender", typing.Dict[builtins.str, typing.Any]]] = None,
        define_auth_challenge: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        post_authentication: typing.Optional[builtins.str] = None,
        post_confirmation: typing.Optional[builtins.str] = None,
        pre_authentication: typing.Optional[builtins.str] = None,
        pre_sign_up: typing.Optional[builtins.str] = None,
        pre_token_generation: typing.Optional[builtins.str] = None,
        user_migration: typing.Optional[builtins.str] = None,
        verify_auth_challenge_response: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create_auth_challenge: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#create_auth_challenge CognitoUserPool#create_auth_challenge}.
        :param custom_email_sender: custom_email_sender block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#custom_email_sender CognitoUserPool#custom_email_sender}
        :param custom_message: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#custom_message CognitoUserPool#custom_message}.
        :param custom_sms_sender: custom_sms_sender block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#custom_sms_sender CognitoUserPool#custom_sms_sender}
        :param define_auth_challenge: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#define_auth_challenge CognitoUserPool#define_auth_challenge}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#kms_key_id CognitoUserPool#kms_key_id}.
        :param post_authentication: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#post_authentication CognitoUserPool#post_authentication}.
        :param post_confirmation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#post_confirmation CognitoUserPool#post_confirmation}.
        :param pre_authentication: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#pre_authentication CognitoUserPool#pre_authentication}.
        :param pre_sign_up: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#pre_sign_up CognitoUserPool#pre_sign_up}.
        :param pre_token_generation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#pre_token_generation CognitoUserPool#pre_token_generation}.
        :param user_migration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#user_migration CognitoUserPool#user_migration}.
        :param verify_auth_challenge_response: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#verify_auth_challenge_response CognitoUserPool#verify_auth_challenge_response}.
        '''
        if isinstance(custom_email_sender, dict):
            custom_email_sender = CognitoUserPoolLambdaConfigCustomEmailSender(**custom_email_sender)
        if isinstance(custom_sms_sender, dict):
            custom_sms_sender = CognitoUserPoolLambdaConfigCustomSmsSender(**custom_sms_sender)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__921a22131d4af0f89a123e0738bb6b5c6ab1711c68f4625b67e7576d6fb4e635)
            check_type(argname="argument create_auth_challenge", value=create_auth_challenge, expected_type=type_hints["create_auth_challenge"])
            check_type(argname="argument custom_email_sender", value=custom_email_sender, expected_type=type_hints["custom_email_sender"])
            check_type(argname="argument custom_message", value=custom_message, expected_type=type_hints["custom_message"])
            check_type(argname="argument custom_sms_sender", value=custom_sms_sender, expected_type=type_hints["custom_sms_sender"])
            check_type(argname="argument define_auth_challenge", value=define_auth_challenge, expected_type=type_hints["define_auth_challenge"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument post_authentication", value=post_authentication, expected_type=type_hints["post_authentication"])
            check_type(argname="argument post_confirmation", value=post_confirmation, expected_type=type_hints["post_confirmation"])
            check_type(argname="argument pre_authentication", value=pre_authentication, expected_type=type_hints["pre_authentication"])
            check_type(argname="argument pre_sign_up", value=pre_sign_up, expected_type=type_hints["pre_sign_up"])
            check_type(argname="argument pre_token_generation", value=pre_token_generation, expected_type=type_hints["pre_token_generation"])
            check_type(argname="argument user_migration", value=user_migration, expected_type=type_hints["user_migration"])
            check_type(argname="argument verify_auth_challenge_response", value=verify_auth_challenge_response, expected_type=type_hints["verify_auth_challenge_response"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create_auth_challenge is not None:
            self._values["create_auth_challenge"] = create_auth_challenge
        if custom_email_sender is not None:
            self._values["custom_email_sender"] = custom_email_sender
        if custom_message is not None:
            self._values["custom_message"] = custom_message
        if custom_sms_sender is not None:
            self._values["custom_sms_sender"] = custom_sms_sender
        if define_auth_challenge is not None:
            self._values["define_auth_challenge"] = define_auth_challenge
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if post_authentication is not None:
            self._values["post_authentication"] = post_authentication
        if post_confirmation is not None:
            self._values["post_confirmation"] = post_confirmation
        if pre_authentication is not None:
            self._values["pre_authentication"] = pre_authentication
        if pre_sign_up is not None:
            self._values["pre_sign_up"] = pre_sign_up
        if pre_token_generation is not None:
            self._values["pre_token_generation"] = pre_token_generation
        if user_migration is not None:
            self._values["user_migration"] = user_migration
        if verify_auth_challenge_response is not None:
            self._values["verify_auth_challenge_response"] = verify_auth_challenge_response

    @builtins.property
    def create_auth_challenge(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#create_auth_challenge CognitoUserPool#create_auth_challenge}.'''
        result = self._values.get("create_auth_challenge")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_email_sender(
        self,
    ) -> typing.Optional["CognitoUserPoolLambdaConfigCustomEmailSender"]:
        '''custom_email_sender block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#custom_email_sender CognitoUserPool#custom_email_sender}
        '''
        result = self._values.get("custom_email_sender")
        return typing.cast(typing.Optional["CognitoUserPoolLambdaConfigCustomEmailSender"], result)

    @builtins.property
    def custom_message(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#custom_message CognitoUserPool#custom_message}.'''
        result = self._values.get("custom_message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_sms_sender(
        self,
    ) -> typing.Optional["CognitoUserPoolLambdaConfigCustomSmsSender"]:
        '''custom_sms_sender block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#custom_sms_sender CognitoUserPool#custom_sms_sender}
        '''
        result = self._values.get("custom_sms_sender")
        return typing.cast(typing.Optional["CognitoUserPoolLambdaConfigCustomSmsSender"], result)

    @builtins.property
    def define_auth_challenge(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#define_auth_challenge CognitoUserPool#define_auth_challenge}.'''
        result = self._values.get("define_auth_challenge")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#kms_key_id CognitoUserPool#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def post_authentication(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#post_authentication CognitoUserPool#post_authentication}.'''
        result = self._values.get("post_authentication")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def post_confirmation(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#post_confirmation CognitoUserPool#post_confirmation}.'''
        result = self._values.get("post_confirmation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pre_authentication(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#pre_authentication CognitoUserPool#pre_authentication}.'''
        result = self._values.get("pre_authentication")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pre_sign_up(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#pre_sign_up CognitoUserPool#pre_sign_up}.'''
        result = self._values.get("pre_sign_up")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pre_token_generation(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#pre_token_generation CognitoUserPool#pre_token_generation}.'''
        result = self._values.get("pre_token_generation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_migration(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#user_migration CognitoUserPool#user_migration}.'''
        result = self._values.get("user_migration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def verify_auth_challenge_response(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#verify_auth_challenge_response CognitoUserPool#verify_auth_challenge_response}.'''
        result = self._values.get("verify_auth_challenge_response")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoUserPoolLambdaConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.cognitoUserPool.CognitoUserPoolLambdaConfigCustomEmailSender",
    jsii_struct_bases=[],
    name_mapping={"lambda_arn": "lambdaArn", "lambda_version": "lambdaVersion"},
)
class CognitoUserPoolLambdaConfigCustomEmailSender:
    def __init__(
        self,
        *,
        lambda_arn: builtins.str,
        lambda_version: builtins.str,
    ) -> None:
        '''
        :param lambda_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#lambda_arn CognitoUserPool#lambda_arn}.
        :param lambda_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#lambda_version CognitoUserPool#lambda_version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6095b8cd76719db6a292914ee8d667f4228bef27f1f614ba6033c0e32c847a72)
            check_type(argname="argument lambda_arn", value=lambda_arn, expected_type=type_hints["lambda_arn"])
            check_type(argname="argument lambda_version", value=lambda_version, expected_type=type_hints["lambda_version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "lambda_arn": lambda_arn,
            "lambda_version": lambda_version,
        }

    @builtins.property
    def lambda_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#lambda_arn CognitoUserPool#lambda_arn}.'''
        result = self._values.get("lambda_arn")
        assert result is not None, "Required property 'lambda_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lambda_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#lambda_version CognitoUserPool#lambda_version}.'''
        result = self._values.get("lambda_version")
        assert result is not None, "Required property 'lambda_version' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoUserPoolLambdaConfigCustomEmailSender(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CognitoUserPoolLambdaConfigCustomEmailSenderOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoUserPool.CognitoUserPoolLambdaConfigCustomEmailSenderOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5b98345e7c384e45e525003432927ba5bba2a8cb6b7dba0e41a8e6b8f9a5253a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="lambdaArnInput")
    def lambda_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lambdaArnInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaVersionInput")
    def lambda_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lambdaVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaArn")
    def lambda_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lambdaArn"))

    @lambda_arn.setter
    def lambda_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e35efcfb1c380a3a72108e4c734401adff713edf61766d53df6585ae3720542)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lambdaArn", value)

    @builtins.property
    @jsii.member(jsii_name="lambdaVersion")
    def lambda_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lambdaVersion"))

    @lambda_version.setter
    def lambda_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77f6f14d278a451432ddb02791dd2209fcdc347106664e582690adba92ef0c48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lambdaVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CognitoUserPoolLambdaConfigCustomEmailSender]:
        return typing.cast(typing.Optional[CognitoUserPoolLambdaConfigCustomEmailSender], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoUserPoolLambdaConfigCustomEmailSender],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e34167bbb3d31f13f4ae95919ecf9e36de0c2af5b7e2c650a7a594b356ab9c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cognitoUserPool.CognitoUserPoolLambdaConfigCustomSmsSender",
    jsii_struct_bases=[],
    name_mapping={"lambda_arn": "lambdaArn", "lambda_version": "lambdaVersion"},
)
class CognitoUserPoolLambdaConfigCustomSmsSender:
    def __init__(
        self,
        *,
        lambda_arn: builtins.str,
        lambda_version: builtins.str,
    ) -> None:
        '''
        :param lambda_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#lambda_arn CognitoUserPool#lambda_arn}.
        :param lambda_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#lambda_version CognitoUserPool#lambda_version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d32f31153e300f918605eb1fca4728f0f20922b395d409921d34f17d5e530c2)
            check_type(argname="argument lambda_arn", value=lambda_arn, expected_type=type_hints["lambda_arn"])
            check_type(argname="argument lambda_version", value=lambda_version, expected_type=type_hints["lambda_version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "lambda_arn": lambda_arn,
            "lambda_version": lambda_version,
        }

    @builtins.property
    def lambda_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#lambda_arn CognitoUserPool#lambda_arn}.'''
        result = self._values.get("lambda_arn")
        assert result is not None, "Required property 'lambda_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lambda_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#lambda_version CognitoUserPool#lambda_version}.'''
        result = self._values.get("lambda_version")
        assert result is not None, "Required property 'lambda_version' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoUserPoolLambdaConfigCustomSmsSender(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CognitoUserPoolLambdaConfigCustomSmsSenderOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoUserPool.CognitoUserPoolLambdaConfigCustomSmsSenderOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__512a5ca89756a3d3ee9fb944c1acaca1a933e782fa8c160f74e6fe41b097d0fd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="lambdaArnInput")
    def lambda_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lambdaArnInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaVersionInput")
    def lambda_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lambdaVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaArn")
    def lambda_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lambdaArn"))

    @lambda_arn.setter
    def lambda_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4beac845563b9f1396faa446e2fe7eb09ad868ea2f044c00414404646aaf102)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lambdaArn", value)

    @builtins.property
    @jsii.member(jsii_name="lambdaVersion")
    def lambda_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lambdaVersion"))

    @lambda_version.setter
    def lambda_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e6872cd6ac54b3b4c5274468ec2e2c636f1d8aeb45869992e6e885dc2ec2234)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lambdaVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CognitoUserPoolLambdaConfigCustomSmsSender]:
        return typing.cast(typing.Optional[CognitoUserPoolLambdaConfigCustomSmsSender], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoUserPoolLambdaConfigCustomSmsSender],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06f1ddf134678efcb0c9c46c5416030a69b357339c4a6f198ef770ca67e11e66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CognitoUserPoolLambdaConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoUserPool.CognitoUserPoolLambdaConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__69c7f887620337930a74fc51563969f0336ce376d90dbdcf4719a33a7b0518ea)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCustomEmailSender")
    def put_custom_email_sender(
        self,
        *,
        lambda_arn: builtins.str,
        lambda_version: builtins.str,
    ) -> None:
        '''
        :param lambda_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#lambda_arn CognitoUserPool#lambda_arn}.
        :param lambda_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#lambda_version CognitoUserPool#lambda_version}.
        '''
        value = CognitoUserPoolLambdaConfigCustomEmailSender(
            lambda_arn=lambda_arn, lambda_version=lambda_version
        )

        return typing.cast(None, jsii.invoke(self, "putCustomEmailSender", [value]))

    @jsii.member(jsii_name="putCustomSmsSender")
    def put_custom_sms_sender(
        self,
        *,
        lambda_arn: builtins.str,
        lambda_version: builtins.str,
    ) -> None:
        '''
        :param lambda_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#lambda_arn CognitoUserPool#lambda_arn}.
        :param lambda_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#lambda_version CognitoUserPool#lambda_version}.
        '''
        value = CognitoUserPoolLambdaConfigCustomSmsSender(
            lambda_arn=lambda_arn, lambda_version=lambda_version
        )

        return typing.cast(None, jsii.invoke(self, "putCustomSmsSender", [value]))

    @jsii.member(jsii_name="resetCreateAuthChallenge")
    def reset_create_auth_challenge(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreateAuthChallenge", []))

    @jsii.member(jsii_name="resetCustomEmailSender")
    def reset_custom_email_sender(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomEmailSender", []))

    @jsii.member(jsii_name="resetCustomMessage")
    def reset_custom_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomMessage", []))

    @jsii.member(jsii_name="resetCustomSmsSender")
    def reset_custom_sms_sender(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomSmsSender", []))

    @jsii.member(jsii_name="resetDefineAuthChallenge")
    def reset_define_auth_challenge(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefineAuthChallenge", []))

    @jsii.member(jsii_name="resetKmsKeyId")
    def reset_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyId", []))

    @jsii.member(jsii_name="resetPostAuthentication")
    def reset_post_authentication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPostAuthentication", []))

    @jsii.member(jsii_name="resetPostConfirmation")
    def reset_post_confirmation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPostConfirmation", []))

    @jsii.member(jsii_name="resetPreAuthentication")
    def reset_pre_authentication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreAuthentication", []))

    @jsii.member(jsii_name="resetPreSignUp")
    def reset_pre_sign_up(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreSignUp", []))

    @jsii.member(jsii_name="resetPreTokenGeneration")
    def reset_pre_token_generation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreTokenGeneration", []))

    @jsii.member(jsii_name="resetUserMigration")
    def reset_user_migration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserMigration", []))

    @jsii.member(jsii_name="resetVerifyAuthChallengeResponse")
    def reset_verify_auth_challenge_response(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVerifyAuthChallengeResponse", []))

    @builtins.property
    @jsii.member(jsii_name="customEmailSender")
    def custom_email_sender(
        self,
    ) -> CognitoUserPoolLambdaConfigCustomEmailSenderOutputReference:
        return typing.cast(CognitoUserPoolLambdaConfigCustomEmailSenderOutputReference, jsii.get(self, "customEmailSender"))

    @builtins.property
    @jsii.member(jsii_name="customSmsSender")
    def custom_sms_sender(
        self,
    ) -> CognitoUserPoolLambdaConfigCustomSmsSenderOutputReference:
        return typing.cast(CognitoUserPoolLambdaConfigCustomSmsSenderOutputReference, jsii.get(self, "customSmsSender"))

    @builtins.property
    @jsii.member(jsii_name="createAuthChallengeInput")
    def create_auth_challenge_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createAuthChallengeInput"))

    @builtins.property
    @jsii.member(jsii_name="customEmailSenderInput")
    def custom_email_sender_input(
        self,
    ) -> typing.Optional[CognitoUserPoolLambdaConfigCustomEmailSender]:
        return typing.cast(typing.Optional[CognitoUserPoolLambdaConfigCustomEmailSender], jsii.get(self, "customEmailSenderInput"))

    @builtins.property
    @jsii.member(jsii_name="customMessageInput")
    def custom_message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="customSmsSenderInput")
    def custom_sms_sender_input(
        self,
    ) -> typing.Optional[CognitoUserPoolLambdaConfigCustomSmsSender]:
        return typing.cast(typing.Optional[CognitoUserPoolLambdaConfigCustomSmsSender], jsii.get(self, "customSmsSenderInput"))

    @builtins.property
    @jsii.member(jsii_name="defineAuthChallengeInput")
    def define_auth_challenge_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defineAuthChallengeInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdInput")
    def kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="postAuthenticationInput")
    def post_authentication_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "postAuthenticationInput"))

    @builtins.property
    @jsii.member(jsii_name="postConfirmationInput")
    def post_confirmation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "postConfirmationInput"))

    @builtins.property
    @jsii.member(jsii_name="preAuthenticationInput")
    def pre_authentication_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preAuthenticationInput"))

    @builtins.property
    @jsii.member(jsii_name="preSignUpInput")
    def pre_sign_up_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preSignUpInput"))

    @builtins.property
    @jsii.member(jsii_name="preTokenGenerationInput")
    def pre_token_generation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preTokenGenerationInput"))

    @builtins.property
    @jsii.member(jsii_name="userMigrationInput")
    def user_migration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userMigrationInput"))

    @builtins.property
    @jsii.member(jsii_name="verifyAuthChallengeResponseInput")
    def verify_auth_challenge_response_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "verifyAuthChallengeResponseInput"))

    @builtins.property
    @jsii.member(jsii_name="createAuthChallenge")
    def create_auth_challenge(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createAuthChallenge"))

    @create_auth_challenge.setter
    def create_auth_challenge(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1beb01f9c3606387be0862e08b9d89fe4d2eed9cdd0f8a922bd923e96c9bb3c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createAuthChallenge", value)

    @builtins.property
    @jsii.member(jsii_name="customMessage")
    def custom_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customMessage"))

    @custom_message.setter
    def custom_message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ce7d56ba20a8337530f056650ad40b466ea0f2c864667e3681a650fa0e55c8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customMessage", value)

    @builtins.property
    @jsii.member(jsii_name="defineAuthChallenge")
    def define_auth_challenge(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defineAuthChallenge"))

    @define_auth_challenge.setter
    def define_auth_challenge(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5cc2d3d9aca4347d0c5cf73cafcb2929a85778cc5d4da59a3b30229ebd2730b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defineAuthChallenge", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a92ad234970e9aea3aea010dadbdde05ecf9c3f11dc83956a907d052cf0cf914)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="postAuthentication")
    def post_authentication(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "postAuthentication"))

    @post_authentication.setter
    def post_authentication(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d10cafd0f8fd86c415c9e1a97ad965bfcfab14a643d6b58e27fe456962d53bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "postAuthentication", value)

    @builtins.property
    @jsii.member(jsii_name="postConfirmation")
    def post_confirmation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "postConfirmation"))

    @post_confirmation.setter
    def post_confirmation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b078ac57ccaa795ec379b94f0e5d84e3721bc9d68bcdb57e82803298b1909a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "postConfirmation", value)

    @builtins.property
    @jsii.member(jsii_name="preAuthentication")
    def pre_authentication(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "preAuthentication"))

    @pre_authentication.setter
    def pre_authentication(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fd9ca628eecbf8e61de3f4332022be82af0802aae3d428cc7c4e10d7a2538c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preAuthentication", value)

    @builtins.property
    @jsii.member(jsii_name="preSignUp")
    def pre_sign_up(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "preSignUp"))

    @pre_sign_up.setter
    def pre_sign_up(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60e1a44269b49bdc64d7818d75e35c27feb741323b5a0ef115dbd5c24591a335)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preSignUp", value)

    @builtins.property
    @jsii.member(jsii_name="preTokenGeneration")
    def pre_token_generation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "preTokenGeneration"))

    @pre_token_generation.setter
    def pre_token_generation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57570b030dc631da5f4973b0d167bbed99aaef1b4887dda88cb8b9d11d5fca96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preTokenGeneration", value)

    @builtins.property
    @jsii.member(jsii_name="userMigration")
    def user_migration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userMigration"))

    @user_migration.setter
    def user_migration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d28d7b8b26c31e809d5b279837967ab5c6a38a19725ba4955c973febcd146e50)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userMigration", value)

    @builtins.property
    @jsii.member(jsii_name="verifyAuthChallengeResponse")
    def verify_auth_challenge_response(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "verifyAuthChallengeResponse"))

    @verify_auth_challenge_response.setter
    def verify_auth_challenge_response(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1356145767004b067c04aa53508179592df23a7e0e4c09b691dae2bfec0ea924)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verifyAuthChallengeResponse", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CognitoUserPoolLambdaConfig]:
        return typing.cast(typing.Optional[CognitoUserPoolLambdaConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoUserPoolLambdaConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cee9ee8ce7d33cc282558693f864147f7cbe9950da2e9f54ec7f2c5749440096)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cognitoUserPool.CognitoUserPoolPasswordPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "minimum_length": "minimumLength",
        "require_lowercase": "requireLowercase",
        "require_numbers": "requireNumbers",
        "require_symbols": "requireSymbols",
        "require_uppercase": "requireUppercase",
        "temporary_password_validity_days": "temporaryPasswordValidityDays",
    },
)
class CognitoUserPoolPasswordPolicy:
    def __init__(
        self,
        *,
        minimum_length: typing.Optional[jsii.Number] = None,
        require_lowercase: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        require_numbers: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        require_symbols: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        require_uppercase: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        temporary_password_validity_days: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param minimum_length: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#minimum_length CognitoUserPool#minimum_length}.
        :param require_lowercase: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#require_lowercase CognitoUserPool#require_lowercase}.
        :param require_numbers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#require_numbers CognitoUserPool#require_numbers}.
        :param require_symbols: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#require_symbols CognitoUserPool#require_symbols}.
        :param require_uppercase: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#require_uppercase CognitoUserPool#require_uppercase}.
        :param temporary_password_validity_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#temporary_password_validity_days CognitoUserPool#temporary_password_validity_days}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1fe5ce57974d712919c40b100670bbc64be833a5b5a42a7f3b2d1032d12a598)
            check_type(argname="argument minimum_length", value=minimum_length, expected_type=type_hints["minimum_length"])
            check_type(argname="argument require_lowercase", value=require_lowercase, expected_type=type_hints["require_lowercase"])
            check_type(argname="argument require_numbers", value=require_numbers, expected_type=type_hints["require_numbers"])
            check_type(argname="argument require_symbols", value=require_symbols, expected_type=type_hints["require_symbols"])
            check_type(argname="argument require_uppercase", value=require_uppercase, expected_type=type_hints["require_uppercase"])
            check_type(argname="argument temporary_password_validity_days", value=temporary_password_validity_days, expected_type=type_hints["temporary_password_validity_days"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if minimum_length is not None:
            self._values["minimum_length"] = minimum_length
        if require_lowercase is not None:
            self._values["require_lowercase"] = require_lowercase
        if require_numbers is not None:
            self._values["require_numbers"] = require_numbers
        if require_symbols is not None:
            self._values["require_symbols"] = require_symbols
        if require_uppercase is not None:
            self._values["require_uppercase"] = require_uppercase
        if temporary_password_validity_days is not None:
            self._values["temporary_password_validity_days"] = temporary_password_validity_days

    @builtins.property
    def minimum_length(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#minimum_length CognitoUserPool#minimum_length}.'''
        result = self._values.get("minimum_length")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def require_lowercase(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#require_lowercase CognitoUserPool#require_lowercase}.'''
        result = self._values.get("require_lowercase")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def require_numbers(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#require_numbers CognitoUserPool#require_numbers}.'''
        result = self._values.get("require_numbers")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def require_symbols(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#require_symbols CognitoUserPool#require_symbols}.'''
        result = self._values.get("require_symbols")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def require_uppercase(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#require_uppercase CognitoUserPool#require_uppercase}.'''
        result = self._values.get("require_uppercase")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def temporary_password_validity_days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#temporary_password_validity_days CognitoUserPool#temporary_password_validity_days}.'''
        result = self._values.get("temporary_password_validity_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoUserPoolPasswordPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CognitoUserPoolPasswordPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoUserPool.CognitoUserPoolPasswordPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c53d65bb8ac699fa9ea6e94e6e5cee3939cc6d8ddaaf9189ce32a4c834183527)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMinimumLength")
    def reset_minimum_length(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimumLength", []))

    @jsii.member(jsii_name="resetRequireLowercase")
    def reset_require_lowercase(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequireLowercase", []))

    @jsii.member(jsii_name="resetRequireNumbers")
    def reset_require_numbers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequireNumbers", []))

    @jsii.member(jsii_name="resetRequireSymbols")
    def reset_require_symbols(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequireSymbols", []))

    @jsii.member(jsii_name="resetRequireUppercase")
    def reset_require_uppercase(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequireUppercase", []))

    @jsii.member(jsii_name="resetTemporaryPasswordValidityDays")
    def reset_temporary_password_validity_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTemporaryPasswordValidityDays", []))

    @builtins.property
    @jsii.member(jsii_name="minimumLengthInput")
    def minimum_length_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minimumLengthInput"))

    @builtins.property
    @jsii.member(jsii_name="requireLowercaseInput")
    def require_lowercase_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "requireLowercaseInput"))

    @builtins.property
    @jsii.member(jsii_name="requireNumbersInput")
    def require_numbers_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "requireNumbersInput"))

    @builtins.property
    @jsii.member(jsii_name="requireSymbolsInput")
    def require_symbols_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "requireSymbolsInput"))

    @builtins.property
    @jsii.member(jsii_name="requireUppercaseInput")
    def require_uppercase_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "requireUppercaseInput"))

    @builtins.property
    @jsii.member(jsii_name="temporaryPasswordValidityDaysInput")
    def temporary_password_validity_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "temporaryPasswordValidityDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumLength")
    def minimum_length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minimumLength"))

    @minimum_length.setter
    def minimum_length(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8c3a732b760f729d428afa9ac037ba1652d54783dcbb51ee6aa0b60b35a7215)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumLength", value)

    @builtins.property
    @jsii.member(jsii_name="requireLowercase")
    def require_lowercase(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "requireLowercase"))

    @require_lowercase.setter
    def require_lowercase(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2c169242b0063effd021e5e2a24c874357312aba383c16bb033da2921b13c05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requireLowercase", value)

    @builtins.property
    @jsii.member(jsii_name="requireNumbers")
    def require_numbers(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "requireNumbers"))

    @require_numbers.setter
    def require_numbers(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72c0450c252a61b390c2182833021703dda9d86fc5683039151f7abb0a9fadb9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requireNumbers", value)

    @builtins.property
    @jsii.member(jsii_name="requireSymbols")
    def require_symbols(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "requireSymbols"))

    @require_symbols.setter
    def require_symbols(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__533619fb3ab473a27ff6c5393db7c4cdeace1ad6b19cf492c4d61bcd21b57dbf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requireSymbols", value)

    @builtins.property
    @jsii.member(jsii_name="requireUppercase")
    def require_uppercase(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "requireUppercase"))

    @require_uppercase.setter
    def require_uppercase(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11eb6ab5776c82bc8d861ebc3c21f797887a83872bfb7ee623052ac2f47f5933)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requireUppercase", value)

    @builtins.property
    @jsii.member(jsii_name="temporaryPasswordValidityDays")
    def temporary_password_validity_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "temporaryPasswordValidityDays"))

    @temporary_password_validity_days.setter
    def temporary_password_validity_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80c689db06bb721ca7e75baf83396e98805e55a0ef01b508e3b39019409dffec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "temporaryPasswordValidityDays", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CognitoUserPoolPasswordPolicy]:
        return typing.cast(typing.Optional[CognitoUserPoolPasswordPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoUserPoolPasswordPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e0f43b33f60975590f518237788fb9f7adf3169958a3b8e258c62eeb1b77b22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cognitoUserPool.CognitoUserPoolSchema",
    jsii_struct_bases=[],
    name_mapping={
        "attribute_data_type": "attributeDataType",
        "name": "name",
        "developer_only_attribute": "developerOnlyAttribute",
        "mutable": "mutable",
        "number_attribute_constraints": "numberAttributeConstraints",
        "required": "required",
        "string_attribute_constraints": "stringAttributeConstraints",
    },
)
class CognitoUserPoolSchema:
    def __init__(
        self,
        *,
        attribute_data_type: builtins.str,
        name: builtins.str,
        developer_only_attribute: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        mutable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        number_attribute_constraints: typing.Optional[typing.Union["CognitoUserPoolSchemaNumberAttributeConstraints", typing.Dict[builtins.str, typing.Any]]] = None,
        required: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        string_attribute_constraints: typing.Optional[typing.Union["CognitoUserPoolSchemaStringAttributeConstraints", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param attribute_data_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#attribute_data_type CognitoUserPool#attribute_data_type}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#name CognitoUserPool#name}.
        :param developer_only_attribute: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#developer_only_attribute CognitoUserPool#developer_only_attribute}.
        :param mutable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#mutable CognitoUserPool#mutable}.
        :param number_attribute_constraints: number_attribute_constraints block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#number_attribute_constraints CognitoUserPool#number_attribute_constraints}
        :param required: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#required CognitoUserPool#required}.
        :param string_attribute_constraints: string_attribute_constraints block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#string_attribute_constraints CognitoUserPool#string_attribute_constraints}
        '''
        if isinstance(number_attribute_constraints, dict):
            number_attribute_constraints = CognitoUserPoolSchemaNumberAttributeConstraints(**number_attribute_constraints)
        if isinstance(string_attribute_constraints, dict):
            string_attribute_constraints = CognitoUserPoolSchemaStringAttributeConstraints(**string_attribute_constraints)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33a49c31faa6cf4b8d8c9f10fa8938fc60a05766851e9152e6b549277d636aa6)
            check_type(argname="argument attribute_data_type", value=attribute_data_type, expected_type=type_hints["attribute_data_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument developer_only_attribute", value=developer_only_attribute, expected_type=type_hints["developer_only_attribute"])
            check_type(argname="argument mutable", value=mutable, expected_type=type_hints["mutable"])
            check_type(argname="argument number_attribute_constraints", value=number_attribute_constraints, expected_type=type_hints["number_attribute_constraints"])
            check_type(argname="argument required", value=required, expected_type=type_hints["required"])
            check_type(argname="argument string_attribute_constraints", value=string_attribute_constraints, expected_type=type_hints["string_attribute_constraints"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "attribute_data_type": attribute_data_type,
            "name": name,
        }
        if developer_only_attribute is not None:
            self._values["developer_only_attribute"] = developer_only_attribute
        if mutable is not None:
            self._values["mutable"] = mutable
        if number_attribute_constraints is not None:
            self._values["number_attribute_constraints"] = number_attribute_constraints
        if required is not None:
            self._values["required"] = required
        if string_attribute_constraints is not None:
            self._values["string_attribute_constraints"] = string_attribute_constraints

    @builtins.property
    def attribute_data_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#attribute_data_type CognitoUserPool#attribute_data_type}.'''
        result = self._values.get("attribute_data_type")
        assert result is not None, "Required property 'attribute_data_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#name CognitoUserPool#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def developer_only_attribute(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#developer_only_attribute CognitoUserPool#developer_only_attribute}.'''
        result = self._values.get("developer_only_attribute")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def mutable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#mutable CognitoUserPool#mutable}.'''
        result = self._values.get("mutable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def number_attribute_constraints(
        self,
    ) -> typing.Optional["CognitoUserPoolSchemaNumberAttributeConstraints"]:
        '''number_attribute_constraints block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#number_attribute_constraints CognitoUserPool#number_attribute_constraints}
        '''
        result = self._values.get("number_attribute_constraints")
        return typing.cast(typing.Optional["CognitoUserPoolSchemaNumberAttributeConstraints"], result)

    @builtins.property
    def required(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#required CognitoUserPool#required}.'''
        result = self._values.get("required")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def string_attribute_constraints(
        self,
    ) -> typing.Optional["CognitoUserPoolSchemaStringAttributeConstraints"]:
        '''string_attribute_constraints block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#string_attribute_constraints CognitoUserPool#string_attribute_constraints}
        '''
        result = self._values.get("string_attribute_constraints")
        return typing.cast(typing.Optional["CognitoUserPoolSchemaStringAttributeConstraints"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoUserPoolSchema(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CognitoUserPoolSchemaList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoUserPool.CognitoUserPoolSchemaList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2c33094c7ad85d88c6b6dd25f7a5d095c8099c456af55036a2dfe704e2582dac)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "CognitoUserPoolSchemaOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08a4c7a6be6c88dba528dc9239419661a084e9fa1faf9d2c024d68390de6a0e3)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CognitoUserPoolSchemaOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fd9d72b89f32df9ab496e54c1c2498beb9c5c7d8ca0bd43f5ef6e9b6421454b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cb9d32daec06043b30f76b75e4ed74261f8a8cc6cbe397f62ec59796f919af38)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b4ec178f19bb7a64f724164890ea240899b57b3e7751ee7e6ab0639519f112e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CognitoUserPoolSchema]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CognitoUserPoolSchema]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CognitoUserPoolSchema]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c2994f25b821c55bc7539279d4d9e66831ecd83edfcb2b7607dfae249c81114)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cognitoUserPool.CognitoUserPoolSchemaNumberAttributeConstraints",
    jsii_struct_bases=[],
    name_mapping={"max_value": "maxValue", "min_value": "minValue"},
)
class CognitoUserPoolSchemaNumberAttributeConstraints:
    def __init__(
        self,
        *,
        max_value: typing.Optional[builtins.str] = None,
        min_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param max_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#max_value CognitoUserPool#max_value}.
        :param min_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#min_value CognitoUserPool#min_value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7c5f24763303c8c7330bc017efa31a5056ceb1666ddd0a8f4138893e6c23aa6)
            check_type(argname="argument max_value", value=max_value, expected_type=type_hints["max_value"])
            check_type(argname="argument min_value", value=min_value, expected_type=type_hints["min_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if max_value is not None:
            self._values["max_value"] = max_value
        if min_value is not None:
            self._values["min_value"] = min_value

    @builtins.property
    def max_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#max_value CognitoUserPool#max_value}.'''
        result = self._values.get("max_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#min_value CognitoUserPool#min_value}.'''
        result = self._values.get("min_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoUserPoolSchemaNumberAttributeConstraints(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CognitoUserPoolSchemaNumberAttributeConstraintsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoUserPool.CognitoUserPoolSchemaNumberAttributeConstraintsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8b30e823c4a06bfb9f5c2b39d605ae7876723dae2863ac036e5b505173176257)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMaxValue")
    def reset_max_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxValue", []))

    @jsii.member(jsii_name="resetMinValue")
    def reset_min_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinValue", []))

    @builtins.property
    @jsii.member(jsii_name="maxValueInput")
    def max_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxValueInput"))

    @builtins.property
    @jsii.member(jsii_name="minValueInput")
    def min_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minValueInput"))

    @builtins.property
    @jsii.member(jsii_name="maxValue")
    def max_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxValue"))

    @max_value.setter
    def max_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddce0bc5b31566b690ebcf4276a60580e746dfc450be2c3742202ba611d0be32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxValue", value)

    @builtins.property
    @jsii.member(jsii_name="minValue")
    def min_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minValue"))

    @min_value.setter
    def min_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42ef5b65d7dfbc203203c05f59e54f9241812352c7832a9a658cf6f7cfeb8c3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CognitoUserPoolSchemaNumberAttributeConstraints]:
        return typing.cast(typing.Optional[CognitoUserPoolSchemaNumberAttributeConstraints], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoUserPoolSchemaNumberAttributeConstraints],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22c475d76d71a1550fea1a9920904799f8b709721b910361a1081e5b0ce9207e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CognitoUserPoolSchemaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoUserPool.CognitoUserPoolSchemaOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9c704c718b60553cd2afe705982c784635195afbcbfd0a56a41db97392711c49)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putNumberAttributeConstraints")
    def put_number_attribute_constraints(
        self,
        *,
        max_value: typing.Optional[builtins.str] = None,
        min_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param max_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#max_value CognitoUserPool#max_value}.
        :param min_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#min_value CognitoUserPool#min_value}.
        '''
        value = CognitoUserPoolSchemaNumberAttributeConstraints(
            max_value=max_value, min_value=min_value
        )

        return typing.cast(None, jsii.invoke(self, "putNumberAttributeConstraints", [value]))

    @jsii.member(jsii_name="putStringAttributeConstraints")
    def put_string_attribute_constraints(
        self,
        *,
        max_length: typing.Optional[builtins.str] = None,
        min_length: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param max_length: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#max_length CognitoUserPool#max_length}.
        :param min_length: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#min_length CognitoUserPool#min_length}.
        '''
        value = CognitoUserPoolSchemaStringAttributeConstraints(
            max_length=max_length, min_length=min_length
        )

        return typing.cast(None, jsii.invoke(self, "putStringAttributeConstraints", [value]))

    @jsii.member(jsii_name="resetDeveloperOnlyAttribute")
    def reset_developer_only_attribute(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeveloperOnlyAttribute", []))

    @jsii.member(jsii_name="resetMutable")
    def reset_mutable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMutable", []))

    @jsii.member(jsii_name="resetNumberAttributeConstraints")
    def reset_number_attribute_constraints(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumberAttributeConstraints", []))

    @jsii.member(jsii_name="resetRequired")
    def reset_required(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequired", []))

    @jsii.member(jsii_name="resetStringAttributeConstraints")
    def reset_string_attribute_constraints(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStringAttributeConstraints", []))

    @builtins.property
    @jsii.member(jsii_name="numberAttributeConstraints")
    def number_attribute_constraints(
        self,
    ) -> CognitoUserPoolSchemaNumberAttributeConstraintsOutputReference:
        return typing.cast(CognitoUserPoolSchemaNumberAttributeConstraintsOutputReference, jsii.get(self, "numberAttributeConstraints"))

    @builtins.property
    @jsii.member(jsii_name="stringAttributeConstraints")
    def string_attribute_constraints(
        self,
    ) -> "CognitoUserPoolSchemaStringAttributeConstraintsOutputReference":
        return typing.cast("CognitoUserPoolSchemaStringAttributeConstraintsOutputReference", jsii.get(self, "stringAttributeConstraints"))

    @builtins.property
    @jsii.member(jsii_name="attributeDataTypeInput")
    def attribute_data_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "attributeDataTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="developerOnlyAttributeInput")
    def developer_only_attribute_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "developerOnlyAttributeInput"))

    @builtins.property
    @jsii.member(jsii_name="mutableInput")
    def mutable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "mutableInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="numberAttributeConstraintsInput")
    def number_attribute_constraints_input(
        self,
    ) -> typing.Optional[CognitoUserPoolSchemaNumberAttributeConstraints]:
        return typing.cast(typing.Optional[CognitoUserPoolSchemaNumberAttributeConstraints], jsii.get(self, "numberAttributeConstraintsInput"))

    @builtins.property
    @jsii.member(jsii_name="requiredInput")
    def required_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "requiredInput"))

    @builtins.property
    @jsii.member(jsii_name="stringAttributeConstraintsInput")
    def string_attribute_constraints_input(
        self,
    ) -> typing.Optional["CognitoUserPoolSchemaStringAttributeConstraints"]:
        return typing.cast(typing.Optional["CognitoUserPoolSchemaStringAttributeConstraints"], jsii.get(self, "stringAttributeConstraintsInput"))

    @builtins.property
    @jsii.member(jsii_name="attributeDataType")
    def attribute_data_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attributeDataType"))

    @attribute_data_type.setter
    def attribute_data_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b850f791b8d096b953e9696120282f56e64ff90150efa5c4d1bec8a6b105e279)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributeDataType", value)

    @builtins.property
    @jsii.member(jsii_name="developerOnlyAttribute")
    def developer_only_attribute(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "developerOnlyAttribute"))

    @developer_only_attribute.setter
    def developer_only_attribute(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf1520dfd340a7dbd619bd7a087bde137e495b24c22f6c0e9d2b610666a01631)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "developerOnlyAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="mutable")
    def mutable(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "mutable"))

    @mutable.setter
    def mutable(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70a03b57c72b6165c18a8a4f64bfb071847bb19c1a5b79fc81c6e58af9d2a1df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mutable", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28b730dbbc3a846972d3fb0d34aaf53b495b69ce954301bedb3e2dd1452d01fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="required")
    def required(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "required"))

    @required.setter
    def required(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b3b7f154d59bdd904a8ad1be18850624ab6f5a266626ab6c9f7d41f124db7a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "required", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CognitoUserPoolSchema, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CognitoUserPoolSchema, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CognitoUserPoolSchema, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29dcdbc3d10b8468d1d595f338e0d738c56a988badfdbc0e40962fc9d2636b43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cognitoUserPool.CognitoUserPoolSchemaStringAttributeConstraints",
    jsii_struct_bases=[],
    name_mapping={"max_length": "maxLength", "min_length": "minLength"},
)
class CognitoUserPoolSchemaStringAttributeConstraints:
    def __init__(
        self,
        *,
        max_length: typing.Optional[builtins.str] = None,
        min_length: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param max_length: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#max_length CognitoUserPool#max_length}.
        :param min_length: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#min_length CognitoUserPool#min_length}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c32f5d8703de297e9aa585b8e55f971aa64256ca931cfbcb7e39b2e01f5612f)
            check_type(argname="argument max_length", value=max_length, expected_type=type_hints["max_length"])
            check_type(argname="argument min_length", value=min_length, expected_type=type_hints["min_length"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if max_length is not None:
            self._values["max_length"] = max_length
        if min_length is not None:
            self._values["min_length"] = min_length

    @builtins.property
    def max_length(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#max_length CognitoUserPool#max_length}.'''
        result = self._values.get("max_length")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def min_length(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#min_length CognitoUserPool#min_length}.'''
        result = self._values.get("min_length")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoUserPoolSchemaStringAttributeConstraints(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CognitoUserPoolSchemaStringAttributeConstraintsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoUserPool.CognitoUserPoolSchemaStringAttributeConstraintsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bc946c1699ca69c0af0312aa393db95a39206f19f54ef98c58b41207d08889e6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMaxLength")
    def reset_max_length(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxLength", []))

    @jsii.member(jsii_name="resetMinLength")
    def reset_min_length(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinLength", []))

    @builtins.property
    @jsii.member(jsii_name="maxLengthInput")
    def max_length_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxLengthInput"))

    @builtins.property
    @jsii.member(jsii_name="minLengthInput")
    def min_length_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minLengthInput"))

    @builtins.property
    @jsii.member(jsii_name="maxLength")
    def max_length(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxLength"))

    @max_length.setter
    def max_length(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__311f9cd4c9badd993c0ef16e9b97062cfaf96765cbb4c6f4328909b88cea3cc3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxLength", value)

    @builtins.property
    @jsii.member(jsii_name="minLength")
    def min_length(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minLength"))

    @min_length.setter
    def min_length(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8fceb356316bcad660e7d88f480960a31ef3c6fdba03f221594be2b1e212094)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minLength", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CognitoUserPoolSchemaStringAttributeConstraints]:
        return typing.cast(typing.Optional[CognitoUserPoolSchemaStringAttributeConstraints], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoUserPoolSchemaStringAttributeConstraints],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5669076083f775edfd07c9937ffe85f19656deef6228114129d4cd7545c1c268)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cognitoUserPool.CognitoUserPoolSmsConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "external_id": "externalId",
        "sns_caller_arn": "snsCallerArn",
        "sns_region": "snsRegion",
    },
)
class CognitoUserPoolSmsConfiguration:
    def __init__(
        self,
        *,
        external_id: builtins.str,
        sns_caller_arn: builtins.str,
        sns_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param external_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#external_id CognitoUserPool#external_id}.
        :param sns_caller_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#sns_caller_arn CognitoUserPool#sns_caller_arn}.
        :param sns_region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#sns_region CognitoUserPool#sns_region}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0089ed0c7a599d33a204c64963e87984621035efe6ec18a961122d5513f940ca)
            check_type(argname="argument external_id", value=external_id, expected_type=type_hints["external_id"])
            check_type(argname="argument sns_caller_arn", value=sns_caller_arn, expected_type=type_hints["sns_caller_arn"])
            check_type(argname="argument sns_region", value=sns_region, expected_type=type_hints["sns_region"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "external_id": external_id,
            "sns_caller_arn": sns_caller_arn,
        }
        if sns_region is not None:
            self._values["sns_region"] = sns_region

    @builtins.property
    def external_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#external_id CognitoUserPool#external_id}.'''
        result = self._values.get("external_id")
        assert result is not None, "Required property 'external_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sns_caller_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#sns_caller_arn CognitoUserPool#sns_caller_arn}.'''
        result = self._values.get("sns_caller_arn")
        assert result is not None, "Required property 'sns_caller_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sns_region(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#sns_region CognitoUserPool#sns_region}.'''
        result = self._values.get("sns_region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoUserPoolSmsConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CognitoUserPoolSmsConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoUserPool.CognitoUserPoolSmsConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__03ff63022d33f787f530ea83ac62f512eb7300be60ea38422b3794b99a8c7a04)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetSnsRegion")
    def reset_sns_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnsRegion", []))

    @builtins.property
    @jsii.member(jsii_name="externalIdInput")
    def external_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "externalIdInput"))

    @builtins.property
    @jsii.member(jsii_name="snsCallerArnInput")
    def sns_caller_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snsCallerArnInput"))

    @builtins.property
    @jsii.member(jsii_name="snsRegionInput")
    def sns_region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snsRegionInput"))

    @builtins.property
    @jsii.member(jsii_name="externalId")
    def external_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalId"))

    @external_id.setter
    def external_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4d0fe5d800273a1b68d9e051ed9d39f9ea1aa54c4ddc8f86648a732a0b05e2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalId", value)

    @builtins.property
    @jsii.member(jsii_name="snsCallerArn")
    def sns_caller_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "snsCallerArn"))

    @sns_caller_arn.setter
    def sns_caller_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f231ca4e37a86e11613e50661df221ba8d74954098b1cfbacf0e501caa5a992a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snsCallerArn", value)

    @builtins.property
    @jsii.member(jsii_name="snsRegion")
    def sns_region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "snsRegion"))

    @sns_region.setter
    def sns_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9be010180109c98b74db48fe42d8219ed81ca628b945ccff26ffb4dcd36337e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snsRegion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CognitoUserPoolSmsConfiguration]:
        return typing.cast(typing.Optional[CognitoUserPoolSmsConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoUserPoolSmsConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__144612962a427e2ef4d19427853c526b9e050f7c87beea39f3bb91944ba37c57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cognitoUserPool.CognitoUserPoolSoftwareTokenMfaConfiguration",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class CognitoUserPoolSoftwareTokenMfaConfiguration:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#enabled CognitoUserPool#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f5f78faa64fd53fcae2ffa98d8d857e6e3246c0486c87fd93a798d65c7f9ea5)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled": enabled,
        }

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#enabled CognitoUserPool#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoUserPoolSoftwareTokenMfaConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CognitoUserPoolSoftwareTokenMfaConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoUserPool.CognitoUserPoolSoftwareTokenMfaConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5f41262cb49d92243432a72fe29a727fd42078001568b103b9573f183fbf8c69)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8b9e2825f9d0bf8d1cc2231690fc6914e00fcab47112c84d6502f304ad5abd4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CognitoUserPoolSoftwareTokenMfaConfiguration]:
        return typing.cast(typing.Optional[CognitoUserPoolSoftwareTokenMfaConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoUserPoolSoftwareTokenMfaConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8197444980e5cfad47164c26b248126d55e83d67d0231bdeceaa86b9a9adaf13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cognitoUserPool.CognitoUserPoolUserAttributeUpdateSettings",
    jsii_struct_bases=[],
    name_mapping={
        "attributes_require_verification_before_update": "attributesRequireVerificationBeforeUpdate",
    },
)
class CognitoUserPoolUserAttributeUpdateSettings:
    def __init__(
        self,
        *,
        attributes_require_verification_before_update: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param attributes_require_verification_before_update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#attributes_require_verification_before_update CognitoUserPool#attributes_require_verification_before_update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10c3646eaf6c3274fc259397e341d0e9917f2aad790897aef08eb728b7d5d557)
            check_type(argname="argument attributes_require_verification_before_update", value=attributes_require_verification_before_update, expected_type=type_hints["attributes_require_verification_before_update"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "attributes_require_verification_before_update": attributes_require_verification_before_update,
        }

    @builtins.property
    def attributes_require_verification_before_update(
        self,
    ) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#attributes_require_verification_before_update CognitoUserPool#attributes_require_verification_before_update}.'''
        result = self._values.get("attributes_require_verification_before_update")
        assert result is not None, "Required property 'attributes_require_verification_before_update' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoUserPoolUserAttributeUpdateSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CognitoUserPoolUserAttributeUpdateSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoUserPool.CognitoUserPoolUserAttributeUpdateSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__148c5d3adb6f61f8bf72bff14e1e5b575c863e4103f2e8c21413d20d6fa68339)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="attributesRequireVerificationBeforeUpdateInput")
    def attributes_require_verification_before_update_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "attributesRequireVerificationBeforeUpdateInput"))

    @builtins.property
    @jsii.member(jsii_name="attributesRequireVerificationBeforeUpdate")
    def attributes_require_verification_before_update(
        self,
    ) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attributesRequireVerificationBeforeUpdate"))

    @attributes_require_verification_before_update.setter
    def attributes_require_verification_before_update(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7dcb40b55a37465275b653c17a3603f25d6ac0da54cf2dfc2b7b45235b6e294b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributesRequireVerificationBeforeUpdate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CognitoUserPoolUserAttributeUpdateSettings]:
        return typing.cast(typing.Optional[CognitoUserPoolUserAttributeUpdateSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoUserPoolUserAttributeUpdateSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dec85ce390048317b1c80aa7255d04eb6a2b35301410d3363c3efddac0d92cb1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cognitoUserPool.CognitoUserPoolUserPoolAddOns",
    jsii_struct_bases=[],
    name_mapping={"advanced_security_mode": "advancedSecurityMode"},
)
class CognitoUserPoolUserPoolAddOns:
    def __init__(self, *, advanced_security_mode: builtins.str) -> None:
        '''
        :param advanced_security_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#advanced_security_mode CognitoUserPool#advanced_security_mode}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22ff2e85f830002e5ac62ab0e59329ef95f1858b44443bfbb042ec03b4c2c8ee)
            check_type(argname="argument advanced_security_mode", value=advanced_security_mode, expected_type=type_hints["advanced_security_mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "advanced_security_mode": advanced_security_mode,
        }

    @builtins.property
    def advanced_security_mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#advanced_security_mode CognitoUserPool#advanced_security_mode}.'''
        result = self._values.get("advanced_security_mode")
        assert result is not None, "Required property 'advanced_security_mode' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoUserPoolUserPoolAddOns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CognitoUserPoolUserPoolAddOnsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoUserPool.CognitoUserPoolUserPoolAddOnsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f2296122a3247c3959f1dd95b9f53986676aa6c42d2311143db3a8ae9dfd2917)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="advancedSecurityModeInput")
    def advanced_security_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "advancedSecurityModeInput"))

    @builtins.property
    @jsii.member(jsii_name="advancedSecurityMode")
    def advanced_security_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "advancedSecurityMode"))

    @advanced_security_mode.setter
    def advanced_security_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95008bd32b2fc919a80d8b798e0c170d3654abafa557fc360b100c899005f62a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "advancedSecurityMode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CognitoUserPoolUserPoolAddOns]:
        return typing.cast(typing.Optional[CognitoUserPoolUserPoolAddOns], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoUserPoolUserPoolAddOns],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4813779483dbc52c743943cce34ddcfbbac0e6934aeb7e74001a5503f71fc0b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cognitoUserPool.CognitoUserPoolUsernameConfiguration",
    jsii_struct_bases=[],
    name_mapping={"case_sensitive": "caseSensitive"},
)
class CognitoUserPoolUsernameConfiguration:
    def __init__(
        self,
        *,
        case_sensitive: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param case_sensitive: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#case_sensitive CognitoUserPool#case_sensitive}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bd5583e1176a9e91d22e2d75e914d5567e6292e02c204fc770085a6e7f81c1c)
            check_type(argname="argument case_sensitive", value=case_sensitive, expected_type=type_hints["case_sensitive"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "case_sensitive": case_sensitive,
        }

    @builtins.property
    def case_sensitive(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#case_sensitive CognitoUserPool#case_sensitive}.'''
        result = self._values.get("case_sensitive")
        assert result is not None, "Required property 'case_sensitive' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoUserPoolUsernameConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CognitoUserPoolUsernameConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoUserPool.CognitoUserPoolUsernameConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__415b235326f26f5d37beaeb7dfeb23f2930bd8c192f5c9bbb98d358e63c7d9f1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="caseSensitiveInput")
    def case_sensitive_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "caseSensitiveInput"))

    @builtins.property
    @jsii.member(jsii_name="caseSensitive")
    def case_sensitive(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "caseSensitive"))

    @case_sensitive.setter
    def case_sensitive(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__356edcc51d3ea1c63960c3bf97a73953bd6c1be5c5b811c1ae4d4300ed4bb6b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caseSensitive", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CognitoUserPoolUsernameConfiguration]:
        return typing.cast(typing.Optional[CognitoUserPoolUsernameConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoUserPoolUsernameConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19d01f834092fef92e67b1fc61235a1de9e1573ea61844d8f2e9466662086e3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cognitoUserPool.CognitoUserPoolVerificationMessageTemplate",
    jsii_struct_bases=[],
    name_mapping={
        "default_email_option": "defaultEmailOption",
        "email_message": "emailMessage",
        "email_message_by_link": "emailMessageByLink",
        "email_subject": "emailSubject",
        "email_subject_by_link": "emailSubjectByLink",
        "sms_message": "smsMessage",
    },
)
class CognitoUserPoolVerificationMessageTemplate:
    def __init__(
        self,
        *,
        default_email_option: typing.Optional[builtins.str] = None,
        email_message: typing.Optional[builtins.str] = None,
        email_message_by_link: typing.Optional[builtins.str] = None,
        email_subject: typing.Optional[builtins.str] = None,
        email_subject_by_link: typing.Optional[builtins.str] = None,
        sms_message: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param default_email_option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#default_email_option CognitoUserPool#default_email_option}.
        :param email_message: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#email_message CognitoUserPool#email_message}.
        :param email_message_by_link: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#email_message_by_link CognitoUserPool#email_message_by_link}.
        :param email_subject: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#email_subject CognitoUserPool#email_subject}.
        :param email_subject_by_link: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#email_subject_by_link CognitoUserPool#email_subject_by_link}.
        :param sms_message: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#sms_message CognitoUserPool#sms_message}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc0b2d7f4e89270442b852991f665e01037bc1bf71be01eb3a759f5dedefe926)
            check_type(argname="argument default_email_option", value=default_email_option, expected_type=type_hints["default_email_option"])
            check_type(argname="argument email_message", value=email_message, expected_type=type_hints["email_message"])
            check_type(argname="argument email_message_by_link", value=email_message_by_link, expected_type=type_hints["email_message_by_link"])
            check_type(argname="argument email_subject", value=email_subject, expected_type=type_hints["email_subject"])
            check_type(argname="argument email_subject_by_link", value=email_subject_by_link, expected_type=type_hints["email_subject_by_link"])
            check_type(argname="argument sms_message", value=sms_message, expected_type=type_hints["sms_message"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if default_email_option is not None:
            self._values["default_email_option"] = default_email_option
        if email_message is not None:
            self._values["email_message"] = email_message
        if email_message_by_link is not None:
            self._values["email_message_by_link"] = email_message_by_link
        if email_subject is not None:
            self._values["email_subject"] = email_subject
        if email_subject_by_link is not None:
            self._values["email_subject_by_link"] = email_subject_by_link
        if sms_message is not None:
            self._values["sms_message"] = sms_message

    @builtins.property
    def default_email_option(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#default_email_option CognitoUserPool#default_email_option}.'''
        result = self._values.get("default_email_option")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def email_message(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#email_message CognitoUserPool#email_message}.'''
        result = self._values.get("email_message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def email_message_by_link(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#email_message_by_link CognitoUserPool#email_message_by_link}.'''
        result = self._values.get("email_message_by_link")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def email_subject(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#email_subject CognitoUserPool#email_subject}.'''
        result = self._values.get("email_subject")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def email_subject_by_link(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#email_subject_by_link CognitoUserPool#email_subject_by_link}.'''
        result = self._values.get("email_subject_by_link")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sms_message(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool#sms_message CognitoUserPool#sms_message}.'''
        result = self._values.get("sms_message")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoUserPoolVerificationMessageTemplate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CognitoUserPoolVerificationMessageTemplateOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoUserPool.CognitoUserPoolVerificationMessageTemplateOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4b93cddfa5a20cefb2d051276f647cd4afdb720d7a44446931a50a246ac7fb98)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDefaultEmailOption")
    def reset_default_email_option(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultEmailOption", []))

    @jsii.member(jsii_name="resetEmailMessage")
    def reset_email_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailMessage", []))

    @jsii.member(jsii_name="resetEmailMessageByLink")
    def reset_email_message_by_link(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailMessageByLink", []))

    @jsii.member(jsii_name="resetEmailSubject")
    def reset_email_subject(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailSubject", []))

    @jsii.member(jsii_name="resetEmailSubjectByLink")
    def reset_email_subject_by_link(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailSubjectByLink", []))

    @jsii.member(jsii_name="resetSmsMessage")
    def reset_sms_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSmsMessage", []))

    @builtins.property
    @jsii.member(jsii_name="defaultEmailOptionInput")
    def default_email_option_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultEmailOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="emailMessageByLinkInput")
    def email_message_by_link_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailMessageByLinkInput"))

    @builtins.property
    @jsii.member(jsii_name="emailMessageInput")
    def email_message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="emailSubjectByLinkInput")
    def email_subject_by_link_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailSubjectByLinkInput"))

    @builtins.property
    @jsii.member(jsii_name="emailSubjectInput")
    def email_subject_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailSubjectInput"))

    @builtins.property
    @jsii.member(jsii_name="smsMessageInput")
    def sms_message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "smsMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultEmailOption")
    def default_email_option(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultEmailOption"))

    @default_email_option.setter
    def default_email_option(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e55e8eb3b27bc6d55cc990d38dddbfcdc3037abc6dbf19f1ad5ec812457d8b27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultEmailOption", value)

    @builtins.property
    @jsii.member(jsii_name="emailMessage")
    def email_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emailMessage"))

    @email_message.setter
    def email_message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c0383cf073aa40d14c1ec0d4a06888b620cf1018d070447c564595d7beb5c60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailMessage", value)

    @builtins.property
    @jsii.member(jsii_name="emailMessageByLink")
    def email_message_by_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emailMessageByLink"))

    @email_message_by_link.setter
    def email_message_by_link(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d3bdc6cecfb24ef589885922aef8994d10d16ef943adbaf408ef96bd1414ced)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailMessageByLink", value)

    @builtins.property
    @jsii.member(jsii_name="emailSubject")
    def email_subject(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emailSubject"))

    @email_subject.setter
    def email_subject(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f9e176da9ee98cc250b698132595bfa2ecc4d3fd98c669688fde1caedd56910)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailSubject", value)

    @builtins.property
    @jsii.member(jsii_name="emailSubjectByLink")
    def email_subject_by_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emailSubjectByLink"))

    @email_subject_by_link.setter
    def email_subject_by_link(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a68646309f941732298bd611fc314e9fb2cca6acff2f6de391f13c2e47c3f723)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailSubjectByLink", value)

    @builtins.property
    @jsii.member(jsii_name="smsMessage")
    def sms_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "smsMessage"))

    @sms_message.setter
    def sms_message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcb6747f0e1ae228f6ec338d2322cff9622bb7fa746ca316c0390e501102270c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "smsMessage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CognitoUserPoolVerificationMessageTemplate]:
        return typing.cast(typing.Optional[CognitoUserPoolVerificationMessageTemplate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoUserPoolVerificationMessageTemplate],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97be6c217b8f0ed1b18ffbb1153bfd9846cc3a9cf8cc777e8f8a2e52784ab00c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CognitoUserPool",
    "CognitoUserPoolAccountRecoverySetting",
    "CognitoUserPoolAccountRecoverySettingOutputReference",
    "CognitoUserPoolAccountRecoverySettingRecoveryMechanism",
    "CognitoUserPoolAccountRecoverySettingRecoveryMechanismList",
    "CognitoUserPoolAccountRecoverySettingRecoveryMechanismOutputReference",
    "CognitoUserPoolAdminCreateUserConfig",
    "CognitoUserPoolAdminCreateUserConfigInviteMessageTemplate",
    "CognitoUserPoolAdminCreateUserConfigInviteMessageTemplateOutputReference",
    "CognitoUserPoolAdminCreateUserConfigOutputReference",
    "CognitoUserPoolConfig",
    "CognitoUserPoolDeviceConfiguration",
    "CognitoUserPoolDeviceConfigurationOutputReference",
    "CognitoUserPoolEmailConfiguration",
    "CognitoUserPoolEmailConfigurationOutputReference",
    "CognitoUserPoolLambdaConfig",
    "CognitoUserPoolLambdaConfigCustomEmailSender",
    "CognitoUserPoolLambdaConfigCustomEmailSenderOutputReference",
    "CognitoUserPoolLambdaConfigCustomSmsSender",
    "CognitoUserPoolLambdaConfigCustomSmsSenderOutputReference",
    "CognitoUserPoolLambdaConfigOutputReference",
    "CognitoUserPoolPasswordPolicy",
    "CognitoUserPoolPasswordPolicyOutputReference",
    "CognitoUserPoolSchema",
    "CognitoUserPoolSchemaList",
    "CognitoUserPoolSchemaNumberAttributeConstraints",
    "CognitoUserPoolSchemaNumberAttributeConstraintsOutputReference",
    "CognitoUserPoolSchemaOutputReference",
    "CognitoUserPoolSchemaStringAttributeConstraints",
    "CognitoUserPoolSchemaStringAttributeConstraintsOutputReference",
    "CognitoUserPoolSmsConfiguration",
    "CognitoUserPoolSmsConfigurationOutputReference",
    "CognitoUserPoolSoftwareTokenMfaConfiguration",
    "CognitoUserPoolSoftwareTokenMfaConfigurationOutputReference",
    "CognitoUserPoolUserAttributeUpdateSettings",
    "CognitoUserPoolUserAttributeUpdateSettingsOutputReference",
    "CognitoUserPoolUserPoolAddOns",
    "CognitoUserPoolUserPoolAddOnsOutputReference",
    "CognitoUserPoolUsernameConfiguration",
    "CognitoUserPoolUsernameConfigurationOutputReference",
    "CognitoUserPoolVerificationMessageTemplate",
    "CognitoUserPoolVerificationMessageTemplateOutputReference",
]

publication.publish()

def _typecheckingstub__06e1d3ff826ca7315cd3b6d7b32321e317e80234e7d73f28b6b65792dbec0d4d(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    account_recovery_setting: typing.Optional[typing.Union[CognitoUserPoolAccountRecoverySetting, typing.Dict[builtins.str, typing.Any]]] = None,
    admin_create_user_config: typing.Optional[typing.Union[CognitoUserPoolAdminCreateUserConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    alias_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
    auto_verified_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
    deletion_protection: typing.Optional[builtins.str] = None,
    device_configuration: typing.Optional[typing.Union[CognitoUserPoolDeviceConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    email_configuration: typing.Optional[typing.Union[CognitoUserPoolEmailConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    email_verification_message: typing.Optional[builtins.str] = None,
    email_verification_subject: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    lambda_config: typing.Optional[typing.Union[CognitoUserPoolLambdaConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    mfa_configuration: typing.Optional[builtins.str] = None,
    password_policy: typing.Optional[typing.Union[CognitoUserPoolPasswordPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    schema: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CognitoUserPoolSchema, typing.Dict[builtins.str, typing.Any]]]]] = None,
    sms_authentication_message: typing.Optional[builtins.str] = None,
    sms_configuration: typing.Optional[typing.Union[CognitoUserPoolSmsConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    sms_verification_message: typing.Optional[builtins.str] = None,
    software_token_mfa_configuration: typing.Optional[typing.Union[CognitoUserPoolSoftwareTokenMfaConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    user_attribute_update_settings: typing.Optional[typing.Union[CognitoUserPoolUserAttributeUpdateSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    username_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
    username_configuration: typing.Optional[typing.Union[CognitoUserPoolUsernameConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    user_pool_add_ons: typing.Optional[typing.Union[CognitoUserPoolUserPoolAddOns, typing.Dict[builtins.str, typing.Any]]] = None,
    verification_message_template: typing.Optional[typing.Union[CognitoUserPoolVerificationMessageTemplate, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__608ff9723e6a8c20ac963438358fa1967663cf505351d4e19aa3b4f256c8713b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CognitoUserPoolSchema, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40cb89ce20c5565184911ff97db6324df1edbefdb5e330c5a3b011aee5732e40(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cb88b8bc18d16a5e4b6bf9686a4802509d1971eb498b8d453719ecc072d70a6(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b30385f0e8c9b1870232afe1bb8d1d02b41301824fa1f749323a52966b328c1e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b634754503aedd6d6bd5d80e8cd1207fd9fa0060c44da01abad5643078dad6e4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__828dcb94d1ffad079a59f24c1ab4c8c17ca7cb778d4e23258dd880c164ff6221(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ca97c8c4307b55a75e101acf168258c3d16e1df9abcc9f8c48c68672667c610(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ec8dd242b38eea95411d6ad89d0acc26040bb50715dcc6eedae3e374f8ca245(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f72b6a2cf09216a81ccd18c9d0610974e451865228b047f8eafcc0fe6fc21f4f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f23dd9b76788e74cb18078c5f36cbce5453ff77b9128c746434c5d1b8bb7f136(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fc9db5855b1b6accf6ea213716a078279d83ec652c4ff0b6430740403bc2ef6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ba953fa001f32bbc87af3c3d8c349cbd0ddf23536d2afd6cf2da2f8ae017166(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bfb289bea30767ef4f952dff3db8e690d4fb063a6204bc0ee8b390b1eec9d6b(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fc24fdb86ac2ba14684e4f2efc5b334234ed0c8774f6c650a4b01103934e0a0(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a2a866a5eb8386d03fb01e5b24ef733b7c2c9aa33279f89612982d8c584520a(
    *,
    recovery_mechanism: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CognitoUserPoolAccountRecoverySettingRecoveryMechanism, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04bd0663f7d4db01b60ccda155b928f7fc17b7a0bb63b5a3d87bfba3c5cff618(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74dfbba34806de912b0652a779d392752207e914599116b03ff615b3db35ca02(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CognitoUserPoolAccountRecoverySettingRecoveryMechanism, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3788d067c92d6017b6a530ddd9d5d0ea14fd177908e661e2dcd57ed1eb71be41(
    value: typing.Optional[CognitoUserPoolAccountRecoverySetting],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd5566e78887d2d66ca142cb668f68d552c3b01e3b804e747f3cc769a066f642(
    *,
    name: builtins.str,
    priority: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3c8c7bd71aa77675cfc0c4a71d58ed0aedf8b9f6de8b8bc64257320f0c98a7f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__011a813bc94e9050e4aa56fa252792c99c2c6f38c0574df69be4471577dbfae7(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__744bdb08d938e13b0343997d413d5a099f79965e03e87e9eec7a41fdafd044f2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e73378e2cc83d561c4daa10dbc3301d1c2b80ca0dfba49c5a6120c1907253109(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6aa239f7089e71cf31ab2c68496d9dc31fe3ff6f1a82b7e63604bfab4b568cfe(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88c4e0b05d63844c08c6505c3c2f093ae65d26c2ffaf9b4ae8334fd120d03115(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CognitoUserPoolAccountRecoverySettingRecoveryMechanism]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a4d947ae80ba814ae8357091f641ac2ec864965bc137712745c1cad07d1afeb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe8ab36d93a3a5290ad1904c70f17cd65a696727c38d36cdca522152149eb9c1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f671f3639fee79d71a190de383a04e05780f09668fdb547809438410791086ca(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea718cd11203b1ea530e16ec43fdc629da5cc10ab47eaeeec1067e8220900822(
    value: typing.Optional[typing.Union[CognitoUserPoolAccountRecoverySettingRecoveryMechanism, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ed501c34d1ff99dbcef2b1b3b6b10ed4d56c4d444da22cadb74114818ca6dfa(
    *,
    allow_admin_create_user_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    invite_message_template: typing.Optional[typing.Union[CognitoUserPoolAdminCreateUserConfigInviteMessageTemplate, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aaf70e8b4b61546c54113f041cdefac184e711e839df05e14142e26e70d8a453(
    *,
    email_message: typing.Optional[builtins.str] = None,
    email_subject: typing.Optional[builtins.str] = None,
    sms_message: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d4e523f5b65f89c16e3e798c372bc703ba7d5a10c2e4374327bdc0cc57bb88c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de7d20ad8a380fa5410a755011f8191b6519cdaa01cdd05966a140ca2291b458(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1822f8b1e9276c616af6b2fab64ce0048728d9ba6743a6c1c8ab5515f4e2ef4e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a92f088781e1f5df77bbe4b77c92731278e092cc0bc1198f0204d7b0ff95530(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40e84ce8462fd16f69c018d4c8d7cc704a6d9ed4bc0f650139c6f66f4a491300(
    value: typing.Optional[CognitoUserPoolAdminCreateUserConfigInviteMessageTemplate],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__732fa655ebd9d4092a152b2568aa669a5b7dc89c06b9f3a1cf8ff8d5fcd9ea36(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64f81e7291968f44223648aa4c9db295432e618d8b77636ac47ada4988019cd2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1190de545fb089a7ec15d081df5cc68af9db7bbb57362b113e21c8b6a5c959f0(
    value: typing.Optional[CognitoUserPoolAdminCreateUserConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9065476a5f52e9e06ca579c683af1ee03b7bd5ce59c489f0c8f9f4479bac0595(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    account_recovery_setting: typing.Optional[typing.Union[CognitoUserPoolAccountRecoverySetting, typing.Dict[builtins.str, typing.Any]]] = None,
    admin_create_user_config: typing.Optional[typing.Union[CognitoUserPoolAdminCreateUserConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    alias_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
    auto_verified_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
    deletion_protection: typing.Optional[builtins.str] = None,
    device_configuration: typing.Optional[typing.Union[CognitoUserPoolDeviceConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    email_configuration: typing.Optional[typing.Union[CognitoUserPoolEmailConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    email_verification_message: typing.Optional[builtins.str] = None,
    email_verification_subject: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    lambda_config: typing.Optional[typing.Union[CognitoUserPoolLambdaConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    mfa_configuration: typing.Optional[builtins.str] = None,
    password_policy: typing.Optional[typing.Union[CognitoUserPoolPasswordPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    schema: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CognitoUserPoolSchema, typing.Dict[builtins.str, typing.Any]]]]] = None,
    sms_authentication_message: typing.Optional[builtins.str] = None,
    sms_configuration: typing.Optional[typing.Union[CognitoUserPoolSmsConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    sms_verification_message: typing.Optional[builtins.str] = None,
    software_token_mfa_configuration: typing.Optional[typing.Union[CognitoUserPoolSoftwareTokenMfaConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    user_attribute_update_settings: typing.Optional[typing.Union[CognitoUserPoolUserAttributeUpdateSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    username_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
    username_configuration: typing.Optional[typing.Union[CognitoUserPoolUsernameConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    user_pool_add_ons: typing.Optional[typing.Union[CognitoUserPoolUserPoolAddOns, typing.Dict[builtins.str, typing.Any]]] = None,
    verification_message_template: typing.Optional[typing.Union[CognitoUserPoolVerificationMessageTemplate, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a010cf5c2f46551a912f7a77be663271213feb8536142d46832f3161be48415(
    *,
    challenge_required_on_new_device: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    device_only_remembered_on_user_prompt: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8cff7c1cd338c00a47a1e60cc2b8ee99f8490040f748b66508f59f47b363c70(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d2b44741949b636c9b2e2ef9b748e3c20b6a400966235731e87c1b6b79a48c2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b2359a13cc9f037bceceb36c6d4aa3051e7dcf51e60df9461298273d1d83bd2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45fe1421fcae7af911426355c53165fb9cd650040ef479835f5e4732c5a2aa09(
    value: typing.Optional[CognitoUserPoolDeviceConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7fb4ed4151b6a7671bfebf1c6751d2878ca00fdf83370c14026cbd59047e383(
    *,
    configuration_set: typing.Optional[builtins.str] = None,
    email_sending_account: typing.Optional[builtins.str] = None,
    from_email_address: typing.Optional[builtins.str] = None,
    reply_to_email_address: typing.Optional[builtins.str] = None,
    source_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb84ee699ee5393d85add1a17660b3ef7313fab0bfbe1b8d15b268c311d78346(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94f05606213b48cb26e806104fca7b6c1df028639b0a2ba01baee0afb449c200(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__049fea58f45309d4e95f7a0aa108809d77a525b1d96e0db7a0141a908a6dd259(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8310772714b880365abb03deb0e893a100ee9a51d730e5f62d3b0f584eecab26(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__199ab049940fdd83c494118073f078fc58845b4ba609e6c085a0e90fcd463f47(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de1a389a1c6f207fd1f6f04957c11437d71d2f8eb2ae81f8cb38907586892116(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__325a9c2a620154d9796da0a0d8d695aa02ade190732b3e41e62b424334f65655(
    value: typing.Optional[CognitoUserPoolEmailConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__921a22131d4af0f89a123e0738bb6b5c6ab1711c68f4625b67e7576d6fb4e635(
    *,
    create_auth_challenge: typing.Optional[builtins.str] = None,
    custom_email_sender: typing.Optional[typing.Union[CognitoUserPoolLambdaConfigCustomEmailSender, typing.Dict[builtins.str, typing.Any]]] = None,
    custom_message: typing.Optional[builtins.str] = None,
    custom_sms_sender: typing.Optional[typing.Union[CognitoUserPoolLambdaConfigCustomSmsSender, typing.Dict[builtins.str, typing.Any]]] = None,
    define_auth_challenge: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    post_authentication: typing.Optional[builtins.str] = None,
    post_confirmation: typing.Optional[builtins.str] = None,
    pre_authentication: typing.Optional[builtins.str] = None,
    pre_sign_up: typing.Optional[builtins.str] = None,
    pre_token_generation: typing.Optional[builtins.str] = None,
    user_migration: typing.Optional[builtins.str] = None,
    verify_auth_challenge_response: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6095b8cd76719db6a292914ee8d667f4228bef27f1f614ba6033c0e32c847a72(
    *,
    lambda_arn: builtins.str,
    lambda_version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b98345e7c384e45e525003432927ba5bba2a8cb6b7dba0e41a8e6b8f9a5253a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e35efcfb1c380a3a72108e4c734401adff713edf61766d53df6585ae3720542(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77f6f14d278a451432ddb02791dd2209fcdc347106664e582690adba92ef0c48(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e34167bbb3d31f13f4ae95919ecf9e36de0c2af5b7e2c650a7a594b356ab9c7(
    value: typing.Optional[CognitoUserPoolLambdaConfigCustomEmailSender],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d32f31153e300f918605eb1fca4728f0f20922b395d409921d34f17d5e530c2(
    *,
    lambda_arn: builtins.str,
    lambda_version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__512a5ca89756a3d3ee9fb944c1acaca1a933e782fa8c160f74e6fe41b097d0fd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4beac845563b9f1396faa446e2fe7eb09ad868ea2f044c00414404646aaf102(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e6872cd6ac54b3b4c5274468ec2e2c636f1d8aeb45869992e6e885dc2ec2234(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06f1ddf134678efcb0c9c46c5416030a69b357339c4a6f198ef770ca67e11e66(
    value: typing.Optional[CognitoUserPoolLambdaConfigCustomSmsSender],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69c7f887620337930a74fc51563969f0336ce376d90dbdcf4719a33a7b0518ea(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1beb01f9c3606387be0862e08b9d89fe4d2eed9cdd0f8a922bd923e96c9bb3c3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ce7d56ba20a8337530f056650ad40b466ea0f2c864667e3681a650fa0e55c8a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5cc2d3d9aca4347d0c5cf73cafcb2929a85778cc5d4da59a3b30229ebd2730b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a92ad234970e9aea3aea010dadbdde05ecf9c3f11dc83956a907d052cf0cf914(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d10cafd0f8fd86c415c9e1a97ad965bfcfab14a643d6b58e27fe456962d53bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b078ac57ccaa795ec379b94f0e5d84e3721bc9d68bcdb57e82803298b1909a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fd9ca628eecbf8e61de3f4332022be82af0802aae3d428cc7c4e10d7a2538c7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60e1a44269b49bdc64d7818d75e35c27feb741323b5a0ef115dbd5c24591a335(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57570b030dc631da5f4973b0d167bbed99aaef1b4887dda88cb8b9d11d5fca96(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d28d7b8b26c31e809d5b279837967ab5c6a38a19725ba4955c973febcd146e50(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1356145767004b067c04aa53508179592df23a7e0e4c09b691dae2bfec0ea924(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cee9ee8ce7d33cc282558693f864147f7cbe9950da2e9f54ec7f2c5749440096(
    value: typing.Optional[CognitoUserPoolLambdaConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1fe5ce57974d712919c40b100670bbc64be833a5b5a42a7f3b2d1032d12a598(
    *,
    minimum_length: typing.Optional[jsii.Number] = None,
    require_lowercase: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    require_numbers: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    require_symbols: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    require_uppercase: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    temporary_password_validity_days: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c53d65bb8ac699fa9ea6e94e6e5cee3939cc6d8ddaaf9189ce32a4c834183527(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8c3a732b760f729d428afa9ac037ba1652d54783dcbb51ee6aa0b60b35a7215(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2c169242b0063effd021e5e2a24c874357312aba383c16bb033da2921b13c05(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72c0450c252a61b390c2182833021703dda9d86fc5683039151f7abb0a9fadb9(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__533619fb3ab473a27ff6c5393db7c4cdeace1ad6b19cf492c4d61bcd21b57dbf(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11eb6ab5776c82bc8d861ebc3c21f797887a83872bfb7ee623052ac2f47f5933(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80c689db06bb721ca7e75baf83396e98805e55a0ef01b508e3b39019409dffec(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e0f43b33f60975590f518237788fb9f7adf3169958a3b8e258c62eeb1b77b22(
    value: typing.Optional[CognitoUserPoolPasswordPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33a49c31faa6cf4b8d8c9f10fa8938fc60a05766851e9152e6b549277d636aa6(
    *,
    attribute_data_type: builtins.str,
    name: builtins.str,
    developer_only_attribute: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    mutable: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    number_attribute_constraints: typing.Optional[typing.Union[CognitoUserPoolSchemaNumberAttributeConstraints, typing.Dict[builtins.str, typing.Any]]] = None,
    required: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    string_attribute_constraints: typing.Optional[typing.Union[CognitoUserPoolSchemaStringAttributeConstraints, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c33094c7ad85d88c6b6dd25f7a5d095c8099c456af55036a2dfe704e2582dac(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08a4c7a6be6c88dba528dc9239419661a084e9fa1faf9d2c024d68390de6a0e3(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fd9d72b89f32df9ab496e54c1c2498beb9c5c7d8ca0bd43f5ef6e9b6421454b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb9d32daec06043b30f76b75e4ed74261f8a8cc6cbe397f62ec59796f919af38(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4ec178f19bb7a64f724164890ea240899b57b3e7751ee7e6ab0639519f112e4(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c2994f25b821c55bc7539279d4d9e66831ecd83edfcb2b7607dfae249c81114(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CognitoUserPoolSchema]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7c5f24763303c8c7330bc017efa31a5056ceb1666ddd0a8f4138893e6c23aa6(
    *,
    max_value: typing.Optional[builtins.str] = None,
    min_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b30e823c4a06bfb9f5c2b39d605ae7876723dae2863ac036e5b505173176257(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddce0bc5b31566b690ebcf4276a60580e746dfc450be2c3742202ba611d0be32(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42ef5b65d7dfbc203203c05f59e54f9241812352c7832a9a658cf6f7cfeb8c3a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22c475d76d71a1550fea1a9920904799f8b709721b910361a1081e5b0ce9207e(
    value: typing.Optional[CognitoUserPoolSchemaNumberAttributeConstraints],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c704c718b60553cd2afe705982c784635195afbcbfd0a56a41db97392711c49(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b850f791b8d096b953e9696120282f56e64ff90150efa5c4d1bec8a6b105e279(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf1520dfd340a7dbd619bd7a087bde137e495b24c22f6c0e9d2b610666a01631(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70a03b57c72b6165c18a8a4f64bfb071847bb19c1a5b79fc81c6e58af9d2a1df(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28b730dbbc3a846972d3fb0d34aaf53b495b69ce954301bedb3e2dd1452d01fd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b3b7f154d59bdd904a8ad1be18850624ab6f5a266626ab6c9f7d41f124db7a6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29dcdbc3d10b8468d1d595f338e0d738c56a988badfdbc0e40962fc9d2636b43(
    value: typing.Optional[typing.Union[CognitoUserPoolSchema, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c32f5d8703de297e9aa585b8e55f971aa64256ca931cfbcb7e39b2e01f5612f(
    *,
    max_length: typing.Optional[builtins.str] = None,
    min_length: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc946c1699ca69c0af0312aa393db95a39206f19f54ef98c58b41207d08889e6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__311f9cd4c9badd993c0ef16e9b97062cfaf96765cbb4c6f4328909b88cea3cc3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8fceb356316bcad660e7d88f480960a31ef3c6fdba03f221594be2b1e212094(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5669076083f775edfd07c9937ffe85f19656deef6228114129d4cd7545c1c268(
    value: typing.Optional[CognitoUserPoolSchemaStringAttributeConstraints],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0089ed0c7a599d33a204c64963e87984621035efe6ec18a961122d5513f940ca(
    *,
    external_id: builtins.str,
    sns_caller_arn: builtins.str,
    sns_region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03ff63022d33f787f530ea83ac62f512eb7300be60ea38422b3794b99a8c7a04(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4d0fe5d800273a1b68d9e051ed9d39f9ea1aa54c4ddc8f86648a732a0b05e2e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f231ca4e37a86e11613e50661df221ba8d74954098b1cfbacf0e501caa5a992a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9be010180109c98b74db48fe42d8219ed81ca628b945ccff26ffb4dcd36337e3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__144612962a427e2ef4d19427853c526b9e050f7c87beea39f3bb91944ba37c57(
    value: typing.Optional[CognitoUserPoolSmsConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f5f78faa64fd53fcae2ffa98d8d857e6e3246c0486c87fd93a798d65c7f9ea5(
    *,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f41262cb49d92243432a72fe29a727fd42078001568b103b9573f183fbf8c69(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b9e2825f9d0bf8d1cc2231690fc6914e00fcab47112c84d6502f304ad5abd4a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8197444980e5cfad47164c26b248126d55e83d67d0231bdeceaa86b9a9adaf13(
    value: typing.Optional[CognitoUserPoolSoftwareTokenMfaConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10c3646eaf6c3274fc259397e341d0e9917f2aad790897aef08eb728b7d5d557(
    *,
    attributes_require_verification_before_update: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__148c5d3adb6f61f8bf72bff14e1e5b575c863e4103f2e8c21413d20d6fa68339(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7dcb40b55a37465275b653c17a3603f25d6ac0da54cf2dfc2b7b45235b6e294b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dec85ce390048317b1c80aa7255d04eb6a2b35301410d3363c3efddac0d92cb1(
    value: typing.Optional[CognitoUserPoolUserAttributeUpdateSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22ff2e85f830002e5ac62ab0e59329ef95f1858b44443bfbb042ec03b4c2c8ee(
    *,
    advanced_security_mode: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2296122a3247c3959f1dd95b9f53986676aa6c42d2311143db3a8ae9dfd2917(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95008bd32b2fc919a80d8b798e0c170d3654abafa557fc360b100c899005f62a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4813779483dbc52c743943cce34ddcfbbac0e6934aeb7e74001a5503f71fc0b6(
    value: typing.Optional[CognitoUserPoolUserPoolAddOns],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bd5583e1176a9e91d22e2d75e914d5567e6292e02c204fc770085a6e7f81c1c(
    *,
    case_sensitive: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__415b235326f26f5d37beaeb7dfeb23f2930bd8c192f5c9bbb98d358e63c7d9f1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__356edcc51d3ea1c63960c3bf97a73953bd6c1be5c5b811c1ae4d4300ed4bb6b5(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19d01f834092fef92e67b1fc61235a1de9e1573ea61844d8f2e9466662086e3f(
    value: typing.Optional[CognitoUserPoolUsernameConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc0b2d7f4e89270442b852991f665e01037bc1bf71be01eb3a759f5dedefe926(
    *,
    default_email_option: typing.Optional[builtins.str] = None,
    email_message: typing.Optional[builtins.str] = None,
    email_message_by_link: typing.Optional[builtins.str] = None,
    email_subject: typing.Optional[builtins.str] = None,
    email_subject_by_link: typing.Optional[builtins.str] = None,
    sms_message: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b93cddfa5a20cefb2d051276f647cd4afdb720d7a44446931a50a246ac7fb98(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e55e8eb3b27bc6d55cc990d38dddbfcdc3037abc6dbf19f1ad5ec812457d8b27(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c0383cf073aa40d14c1ec0d4a06888b620cf1018d070447c564595d7beb5c60(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d3bdc6cecfb24ef589885922aef8994d10d16ef943adbaf408ef96bd1414ced(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f9e176da9ee98cc250b698132595bfa2ecc4d3fd98c669688fde1caedd56910(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a68646309f941732298bd611fc314e9fb2cca6acff2f6de391f13c2e47c3f723(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcb6747f0e1ae228f6ec338d2322cff9622bb7fa746ca316c0390e501102270c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97be6c217b8f0ed1b18ffbb1153bfd9846cc3a9cf8cc777e8f8a2e52784ab00c(
    value: typing.Optional[CognitoUserPoolVerificationMessageTemplate],
) -> None:
    """Type checking stubs"""
    pass
