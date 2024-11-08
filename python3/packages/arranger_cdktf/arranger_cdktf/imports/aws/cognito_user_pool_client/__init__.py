'''
# `aws_cognito_user_pool_client`

Refer to the Terraform Registory for docs: [`aws_cognito_user_pool_client`](https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client).
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


class CognitoUserPoolClient(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoUserPoolClient.CognitoUserPoolClient",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client aws_cognito_user_pool_client}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        user_pool_id: builtins.str,
        access_token_validity: typing.Optional[jsii.Number] = None,
        allowed_oauth_flows: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_oauth_flows_user_pool_client: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        allowed_oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
        analytics_configuration: typing.Optional[typing.Union["CognitoUserPoolClientAnalyticsConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        auth_session_validity: typing.Optional[jsii.Number] = None,
        callback_urls: typing.Optional[typing.Sequence[builtins.str]] = None,
        default_redirect_uri: typing.Optional[builtins.str] = None,
        enable_propagate_additional_user_context_data: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_token_revocation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        explicit_auth_flows: typing.Optional[typing.Sequence[builtins.str]] = None,
        generate_secret: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        id_token_validity: typing.Optional[jsii.Number] = None,
        logout_urls: typing.Optional[typing.Sequence[builtins.str]] = None,
        prevent_user_existence_errors: typing.Optional[builtins.str] = None,
        read_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
        refresh_token_validity: typing.Optional[jsii.Number] = None,
        supported_identity_providers: typing.Optional[typing.Sequence[builtins.str]] = None,
        token_validity_units: typing.Optional[typing.Union["CognitoUserPoolClientTokenValidityUnits", typing.Dict[builtins.str, typing.Any]]] = None,
        write_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client aws_cognito_user_pool_client} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#name CognitoUserPoolClient#name}.
        :param user_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#user_pool_id CognitoUserPoolClient#user_pool_id}.
        :param access_token_validity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#access_token_validity CognitoUserPoolClient#access_token_validity}.
        :param allowed_oauth_flows: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#allowed_oauth_flows CognitoUserPoolClient#allowed_oauth_flows}.
        :param allowed_oauth_flows_user_pool_client: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#allowed_oauth_flows_user_pool_client CognitoUserPoolClient#allowed_oauth_flows_user_pool_client}.
        :param allowed_oauth_scopes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#allowed_oauth_scopes CognitoUserPoolClient#allowed_oauth_scopes}.
        :param analytics_configuration: analytics_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#analytics_configuration CognitoUserPoolClient#analytics_configuration}
        :param auth_session_validity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#auth_session_validity CognitoUserPoolClient#auth_session_validity}.
        :param callback_urls: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#callback_urls CognitoUserPoolClient#callback_urls}.
        :param default_redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#default_redirect_uri CognitoUserPoolClient#default_redirect_uri}.
        :param enable_propagate_additional_user_context_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#enable_propagate_additional_user_context_data CognitoUserPoolClient#enable_propagate_additional_user_context_data}.
        :param enable_token_revocation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#enable_token_revocation CognitoUserPoolClient#enable_token_revocation}.
        :param explicit_auth_flows: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#explicit_auth_flows CognitoUserPoolClient#explicit_auth_flows}.
        :param generate_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#generate_secret CognitoUserPoolClient#generate_secret}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#id CognitoUserPoolClient#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param id_token_validity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#id_token_validity CognitoUserPoolClient#id_token_validity}.
        :param logout_urls: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#logout_urls CognitoUserPoolClient#logout_urls}.
        :param prevent_user_existence_errors: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#prevent_user_existence_errors CognitoUserPoolClient#prevent_user_existence_errors}.
        :param read_attributes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#read_attributes CognitoUserPoolClient#read_attributes}.
        :param refresh_token_validity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#refresh_token_validity CognitoUserPoolClient#refresh_token_validity}.
        :param supported_identity_providers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#supported_identity_providers CognitoUserPoolClient#supported_identity_providers}.
        :param token_validity_units: token_validity_units block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#token_validity_units CognitoUserPoolClient#token_validity_units}
        :param write_attributes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#write_attributes CognitoUserPoolClient#write_attributes}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__511c7ff14a8932ea37343d7b24259d7e75d80a14afa327ef308819678ce6e1cc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CognitoUserPoolClientConfig(
            name=name,
            user_pool_id=user_pool_id,
            access_token_validity=access_token_validity,
            allowed_oauth_flows=allowed_oauth_flows,
            allowed_oauth_flows_user_pool_client=allowed_oauth_flows_user_pool_client,
            allowed_oauth_scopes=allowed_oauth_scopes,
            analytics_configuration=analytics_configuration,
            auth_session_validity=auth_session_validity,
            callback_urls=callback_urls,
            default_redirect_uri=default_redirect_uri,
            enable_propagate_additional_user_context_data=enable_propagate_additional_user_context_data,
            enable_token_revocation=enable_token_revocation,
            explicit_auth_flows=explicit_auth_flows,
            generate_secret=generate_secret,
            id=id,
            id_token_validity=id_token_validity,
            logout_urls=logout_urls,
            prevent_user_existence_errors=prevent_user_existence_errors,
            read_attributes=read_attributes,
            refresh_token_validity=refresh_token_validity,
            supported_identity_providers=supported_identity_providers,
            token_validity_units=token_validity_units,
            write_attributes=write_attributes,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAnalyticsConfiguration")
    def put_analytics_configuration(
        self,
        *,
        application_arn: typing.Optional[builtins.str] = None,
        application_id: typing.Optional[builtins.str] = None,
        external_id: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        user_data_shared: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param application_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#application_arn CognitoUserPoolClient#application_arn}.
        :param application_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#application_id CognitoUserPoolClient#application_id}.
        :param external_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#external_id CognitoUserPoolClient#external_id}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#role_arn CognitoUserPoolClient#role_arn}.
        :param user_data_shared: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#user_data_shared CognitoUserPoolClient#user_data_shared}.
        '''
        value = CognitoUserPoolClientAnalyticsConfiguration(
            application_arn=application_arn,
            application_id=application_id,
            external_id=external_id,
            role_arn=role_arn,
            user_data_shared=user_data_shared,
        )

        return typing.cast(None, jsii.invoke(self, "putAnalyticsConfiguration", [value]))

    @jsii.member(jsii_name="putTokenValidityUnits")
    def put_token_validity_units(
        self,
        *,
        access_token: typing.Optional[builtins.str] = None,
        id_token: typing.Optional[builtins.str] = None,
        refresh_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#access_token CognitoUserPoolClient#access_token}.
        :param id_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#id_token CognitoUserPoolClient#id_token}.
        :param refresh_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#refresh_token CognitoUserPoolClient#refresh_token}.
        '''
        value = CognitoUserPoolClientTokenValidityUnits(
            access_token=access_token, id_token=id_token, refresh_token=refresh_token
        )

        return typing.cast(None, jsii.invoke(self, "putTokenValidityUnits", [value]))

    @jsii.member(jsii_name="resetAccessTokenValidity")
    def reset_access_token_validity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessTokenValidity", []))

    @jsii.member(jsii_name="resetAllowedOauthFlows")
    def reset_allowed_oauth_flows(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedOauthFlows", []))

    @jsii.member(jsii_name="resetAllowedOauthFlowsUserPoolClient")
    def reset_allowed_oauth_flows_user_pool_client(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedOauthFlowsUserPoolClient", []))

    @jsii.member(jsii_name="resetAllowedOauthScopes")
    def reset_allowed_oauth_scopes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedOauthScopes", []))

    @jsii.member(jsii_name="resetAnalyticsConfiguration")
    def reset_analytics_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnalyticsConfiguration", []))

    @jsii.member(jsii_name="resetAuthSessionValidity")
    def reset_auth_session_validity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthSessionValidity", []))

    @jsii.member(jsii_name="resetCallbackUrls")
    def reset_callback_urls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCallbackUrls", []))

    @jsii.member(jsii_name="resetDefaultRedirectUri")
    def reset_default_redirect_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultRedirectUri", []))

    @jsii.member(jsii_name="resetEnablePropagateAdditionalUserContextData")
    def reset_enable_propagate_additional_user_context_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnablePropagateAdditionalUserContextData", []))

    @jsii.member(jsii_name="resetEnableTokenRevocation")
    def reset_enable_token_revocation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableTokenRevocation", []))

    @jsii.member(jsii_name="resetExplicitAuthFlows")
    def reset_explicit_auth_flows(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExplicitAuthFlows", []))

    @jsii.member(jsii_name="resetGenerateSecret")
    def reset_generate_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGenerateSecret", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdTokenValidity")
    def reset_id_token_validity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdTokenValidity", []))

    @jsii.member(jsii_name="resetLogoutUrls")
    def reset_logout_urls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogoutUrls", []))

    @jsii.member(jsii_name="resetPreventUserExistenceErrors")
    def reset_prevent_user_existence_errors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreventUserExistenceErrors", []))

    @jsii.member(jsii_name="resetReadAttributes")
    def reset_read_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadAttributes", []))

    @jsii.member(jsii_name="resetRefreshTokenValidity")
    def reset_refresh_token_validity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRefreshTokenValidity", []))

    @jsii.member(jsii_name="resetSupportedIdentityProviders")
    def reset_supported_identity_providers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSupportedIdentityProviders", []))

    @jsii.member(jsii_name="resetTokenValidityUnits")
    def reset_token_validity_units(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenValidityUnits", []))

    @jsii.member(jsii_name="resetWriteAttributes")
    def reset_write_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWriteAttributes", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="analyticsConfiguration")
    def analytics_configuration(
        self,
    ) -> "CognitoUserPoolClientAnalyticsConfigurationOutputReference":
        return typing.cast("CognitoUserPoolClientAnalyticsConfigurationOutputReference", jsii.get(self, "analyticsConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @builtins.property
    @jsii.member(jsii_name="tokenValidityUnits")
    def token_validity_units(
        self,
    ) -> "CognitoUserPoolClientTokenValidityUnitsOutputReference":
        return typing.cast("CognitoUserPoolClientTokenValidityUnitsOutputReference", jsii.get(self, "tokenValidityUnits"))

    @builtins.property
    @jsii.member(jsii_name="accessTokenValidityInput")
    def access_token_validity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "accessTokenValidityInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedOauthFlowsInput")
    def allowed_oauth_flows_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedOauthFlowsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedOauthFlowsUserPoolClientInput")
    def allowed_oauth_flows_user_pool_client_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "allowedOauthFlowsUserPoolClientInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedOauthScopesInput")
    def allowed_oauth_scopes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedOauthScopesInput"))

    @builtins.property
    @jsii.member(jsii_name="analyticsConfigurationInput")
    def analytics_configuration_input(
        self,
    ) -> typing.Optional["CognitoUserPoolClientAnalyticsConfiguration"]:
        return typing.cast(typing.Optional["CognitoUserPoolClientAnalyticsConfiguration"], jsii.get(self, "analyticsConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="authSessionValidityInput")
    def auth_session_validity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "authSessionValidityInput"))

    @builtins.property
    @jsii.member(jsii_name="callbackUrlsInput")
    def callback_urls_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "callbackUrlsInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultRedirectUriInput")
    def default_redirect_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultRedirectUriInput"))

    @builtins.property
    @jsii.member(jsii_name="enablePropagateAdditionalUserContextDataInput")
    def enable_propagate_additional_user_context_data_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enablePropagateAdditionalUserContextDataInput"))

    @builtins.property
    @jsii.member(jsii_name="enableTokenRevocationInput")
    def enable_token_revocation_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableTokenRevocationInput"))

    @builtins.property
    @jsii.member(jsii_name="explicitAuthFlowsInput")
    def explicit_auth_flows_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "explicitAuthFlowsInput"))

    @builtins.property
    @jsii.member(jsii_name="generateSecretInput")
    def generate_secret_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "generateSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="idTokenValidityInput")
    def id_token_validity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idTokenValidityInput"))

    @builtins.property
    @jsii.member(jsii_name="logoutUrlsInput")
    def logout_urls_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "logoutUrlsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="preventUserExistenceErrorsInput")
    def prevent_user_existence_errors_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preventUserExistenceErrorsInput"))

    @builtins.property
    @jsii.member(jsii_name="readAttributesInput")
    def read_attributes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "readAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="refreshTokenValidityInput")
    def refresh_token_validity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "refreshTokenValidityInput"))

    @builtins.property
    @jsii.member(jsii_name="supportedIdentityProvidersInput")
    def supported_identity_providers_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "supportedIdentityProvidersInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenValidityUnitsInput")
    def token_validity_units_input(
        self,
    ) -> typing.Optional["CognitoUserPoolClientTokenValidityUnits"]:
        return typing.cast(typing.Optional["CognitoUserPoolClientTokenValidityUnits"], jsii.get(self, "tokenValidityUnitsInput"))

    @builtins.property
    @jsii.member(jsii_name="userPoolIdInput")
    def user_pool_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userPoolIdInput"))

    @builtins.property
    @jsii.member(jsii_name="writeAttributesInput")
    def write_attributes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "writeAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="accessTokenValidity")
    def access_token_validity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "accessTokenValidity"))

    @access_token_validity.setter
    def access_token_validity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__590d0554e9ba4ac843b8edc65cd137c735daedaa4ee1384800e40fa8ec31b1d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessTokenValidity", value)

    @builtins.property
    @jsii.member(jsii_name="allowedOauthFlows")
    def allowed_oauth_flows(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedOauthFlows"))

    @allowed_oauth_flows.setter
    def allowed_oauth_flows(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0d1a1696ef080498b7b8acb0f2832e9dd66ec32060a7cc533c711b235416d16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedOauthFlows", value)

    @builtins.property
    @jsii.member(jsii_name="allowedOauthFlowsUserPoolClient")
    def allowed_oauth_flows_user_pool_client(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "allowedOauthFlowsUserPoolClient"))

    @allowed_oauth_flows_user_pool_client.setter
    def allowed_oauth_flows_user_pool_client(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d87f6f3a66fea2a5dfd3988c344796685dfb3ef334a49b6165ea9f4ee5e6cee2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedOauthFlowsUserPoolClient", value)

    @builtins.property
    @jsii.member(jsii_name="allowedOauthScopes")
    def allowed_oauth_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedOauthScopes"))

    @allowed_oauth_scopes.setter
    def allowed_oauth_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4825593a1592d08175fa18bc123637df107132f5ace254565277d5915ab0cbe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedOauthScopes", value)

    @builtins.property
    @jsii.member(jsii_name="authSessionValidity")
    def auth_session_validity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "authSessionValidity"))

    @auth_session_validity.setter
    def auth_session_validity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e358e3c6cd53a16161eccd74bf573f23615986256c406fd0b41207524a09fd96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authSessionValidity", value)

    @builtins.property
    @jsii.member(jsii_name="callbackUrls")
    def callback_urls(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "callbackUrls"))

    @callback_urls.setter
    def callback_urls(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__212c00a4cb167809ba119ca361788d043de54842e19d42a6e9d2d35078777fd4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "callbackUrls", value)

    @builtins.property
    @jsii.member(jsii_name="defaultRedirectUri")
    def default_redirect_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultRedirectUri"))

    @default_redirect_uri.setter
    def default_redirect_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c1f102576c59414fd937570336019b955baece2cbf88158e8758913405599bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultRedirectUri", value)

    @builtins.property
    @jsii.member(jsii_name="enablePropagateAdditionalUserContextData")
    def enable_propagate_additional_user_context_data(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enablePropagateAdditionalUserContextData"))

    @enable_propagate_additional_user_context_data.setter
    def enable_propagate_additional_user_context_data(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcaea5209f61cbe6afd4653f4cc3c2e147eafd75fd90f6bf882304b967d9d79d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enablePropagateAdditionalUserContextData", value)

    @builtins.property
    @jsii.member(jsii_name="enableTokenRevocation")
    def enable_token_revocation(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableTokenRevocation"))

    @enable_token_revocation.setter
    def enable_token_revocation(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a2276616df227891437371a2209259a8b29b94c6d240b503d6057af833aa4ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableTokenRevocation", value)

    @builtins.property
    @jsii.member(jsii_name="explicitAuthFlows")
    def explicit_auth_flows(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "explicitAuthFlows"))

    @explicit_auth_flows.setter
    def explicit_auth_flows(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__458de31a6b3aac524cff1074f2578cae179d48869797df1c827ced14c998da8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "explicitAuthFlows", value)

    @builtins.property
    @jsii.member(jsii_name="generateSecret")
    def generate_secret(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "generateSecret"))

    @generate_secret.setter
    def generate_secret(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14fe65ee9b13938e11b9a4640b98d86865cf3af58a33d4bfe04869e24da43917)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "generateSecret", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f54e5693c7326838c2c547c8e607adbb98ba7c78761bf4690358df514a3fb65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="idTokenValidity")
    def id_token_validity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "idTokenValidity"))

    @id_token_validity.setter
    def id_token_validity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b196a51b57cb6fbe5a53490d4304107b430cd373084eb462d21779cd047c736)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idTokenValidity", value)

    @builtins.property
    @jsii.member(jsii_name="logoutUrls")
    def logout_urls(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "logoutUrls"))

    @logout_urls.setter
    def logout_urls(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9907bc104e9b083023dbd0abdfe0367bb86fa8114b34f0c805375a9c2712dec4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logoutUrls", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd48699517039e99885b9ab49e844ead27cf33d740ffd2def2215dc2c7bd56a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="preventUserExistenceErrors")
    def prevent_user_existence_errors(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "preventUserExistenceErrors"))

    @prevent_user_existence_errors.setter
    def prevent_user_existence_errors(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80b5891819658be40b6a79bed6c694d2701236436806613d87f40a98dc88bed3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preventUserExistenceErrors", value)

    @builtins.property
    @jsii.member(jsii_name="readAttributes")
    def read_attributes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "readAttributes"))

    @read_attributes.setter
    def read_attributes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0905b9118deeb1da73fcfea14322f912694ec9083fa246ab392f57e062859d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="refreshTokenValidity")
    def refresh_token_validity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "refreshTokenValidity"))

    @refresh_token_validity.setter
    def refresh_token_validity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__445b955cc4b2929df1e7a1bfe66fb4fa0e4455053f01a505c20a52f501cf8687)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "refreshTokenValidity", value)

    @builtins.property
    @jsii.member(jsii_name="supportedIdentityProviders")
    def supported_identity_providers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "supportedIdentityProviders"))

    @supported_identity_providers.setter
    def supported_identity_providers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abf243cdb5ed85edefb47f2dcd213ae23b293587d252460f5f66af28fc6a73ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "supportedIdentityProviders", value)

    @builtins.property
    @jsii.member(jsii_name="userPoolId")
    def user_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userPoolId"))

    @user_pool_id.setter
    def user_pool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d11b8ca34e95643134bd3d4b6cb56e1f214625a97a144c2b9bb01ab05ef13a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userPoolId", value)

    @builtins.property
    @jsii.member(jsii_name="writeAttributes")
    def write_attributes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "writeAttributes"))

    @write_attributes.setter
    def write_attributes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfdbd30c57b72063f742c9e40d5e425bbd1c9f3bcec639dfac106cad43ef9f5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writeAttributes", value)


@jsii.data_type(
    jsii_type="aws.cognitoUserPoolClient.CognitoUserPoolClientAnalyticsConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "application_arn": "applicationArn",
        "application_id": "applicationId",
        "external_id": "externalId",
        "role_arn": "roleArn",
        "user_data_shared": "userDataShared",
    },
)
class CognitoUserPoolClientAnalyticsConfiguration:
    def __init__(
        self,
        *,
        application_arn: typing.Optional[builtins.str] = None,
        application_id: typing.Optional[builtins.str] = None,
        external_id: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        user_data_shared: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param application_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#application_arn CognitoUserPoolClient#application_arn}.
        :param application_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#application_id CognitoUserPoolClient#application_id}.
        :param external_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#external_id CognitoUserPoolClient#external_id}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#role_arn CognitoUserPoolClient#role_arn}.
        :param user_data_shared: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#user_data_shared CognitoUserPoolClient#user_data_shared}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__405d23f642cabccb14cef6b4e62389a08e41e6799fcb3f2d25b23d5e03a99467)
            check_type(argname="argument application_arn", value=application_arn, expected_type=type_hints["application_arn"])
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument external_id", value=external_id, expected_type=type_hints["external_id"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument user_data_shared", value=user_data_shared, expected_type=type_hints["user_data_shared"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if application_arn is not None:
            self._values["application_arn"] = application_arn
        if application_id is not None:
            self._values["application_id"] = application_id
        if external_id is not None:
            self._values["external_id"] = external_id
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if user_data_shared is not None:
            self._values["user_data_shared"] = user_data_shared

    @builtins.property
    def application_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#application_arn CognitoUserPoolClient#application_arn}.'''
        result = self._values.get("application_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def application_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#application_id CognitoUserPoolClient#application_id}.'''
        result = self._values.get("application_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def external_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#external_id CognitoUserPoolClient#external_id}.'''
        result = self._values.get("external_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#role_arn CognitoUserPoolClient#role_arn}.'''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_data_shared(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#user_data_shared CognitoUserPoolClient#user_data_shared}.'''
        result = self._values.get("user_data_shared")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoUserPoolClientAnalyticsConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CognitoUserPoolClientAnalyticsConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoUserPoolClient.CognitoUserPoolClientAnalyticsConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__62851741af7c2fbc3315881e24aa8286fd550342c491f64739e6a9de0d6c058c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetApplicationArn")
    def reset_application_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplicationArn", []))

    @jsii.member(jsii_name="resetApplicationId")
    def reset_application_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplicationId", []))

    @jsii.member(jsii_name="resetExternalId")
    def reset_external_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalId", []))

    @jsii.member(jsii_name="resetRoleArn")
    def reset_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoleArn", []))

    @jsii.member(jsii_name="resetUserDataShared")
    def reset_user_data_shared(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserDataShared", []))

    @builtins.property
    @jsii.member(jsii_name="applicationArnInput")
    def application_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationArnInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationIdInput")
    def application_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationIdInput"))

    @builtins.property
    @jsii.member(jsii_name="externalIdInput")
    def external_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "externalIdInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="userDataSharedInput")
    def user_data_shared_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "userDataSharedInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationArn")
    def application_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationArn"))

    @application_arn.setter
    def application_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5492b978669298f7f3927be77721312b240f4e1090fa63397603d6f9d28b27f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationArn", value)

    @builtins.property
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a88640c4a02a7d8a7295542cd451050026908fec262d65f4b1e28b62c74de34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value)

    @builtins.property
    @jsii.member(jsii_name="externalId")
    def external_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalId"))

    @external_id.setter
    def external_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__530b4f88711c255323d54388898279038fadb4d655f6f605c0cbf6a8fdfa2d6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalId", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5813c87c348a084f5f8b38559f36ed04a21322d73ff8fbdaf389a6d2bd22b21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="userDataShared")
    def user_data_shared(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "userDataShared"))

    @user_data_shared.setter
    def user_data_shared(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e5af869f8ffc7c1db3733a1fa3732a90116f32c22151b98ea2795fccc9f4e12)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userDataShared", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CognitoUserPoolClientAnalyticsConfiguration]:
        return typing.cast(typing.Optional[CognitoUserPoolClientAnalyticsConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoUserPoolClientAnalyticsConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b14f03dc499843465713ee6be840a371ca2ebb0c979ab4fb3d9c1a228742ac5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cognitoUserPoolClient.CognitoUserPoolClientConfig",
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
        "user_pool_id": "userPoolId",
        "access_token_validity": "accessTokenValidity",
        "allowed_oauth_flows": "allowedOauthFlows",
        "allowed_oauth_flows_user_pool_client": "allowedOauthFlowsUserPoolClient",
        "allowed_oauth_scopes": "allowedOauthScopes",
        "analytics_configuration": "analyticsConfiguration",
        "auth_session_validity": "authSessionValidity",
        "callback_urls": "callbackUrls",
        "default_redirect_uri": "defaultRedirectUri",
        "enable_propagate_additional_user_context_data": "enablePropagateAdditionalUserContextData",
        "enable_token_revocation": "enableTokenRevocation",
        "explicit_auth_flows": "explicitAuthFlows",
        "generate_secret": "generateSecret",
        "id": "id",
        "id_token_validity": "idTokenValidity",
        "logout_urls": "logoutUrls",
        "prevent_user_existence_errors": "preventUserExistenceErrors",
        "read_attributes": "readAttributes",
        "refresh_token_validity": "refreshTokenValidity",
        "supported_identity_providers": "supportedIdentityProviders",
        "token_validity_units": "tokenValidityUnits",
        "write_attributes": "writeAttributes",
    },
)
class CognitoUserPoolClientConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        user_pool_id: builtins.str,
        access_token_validity: typing.Optional[jsii.Number] = None,
        allowed_oauth_flows: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_oauth_flows_user_pool_client: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        allowed_oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
        analytics_configuration: typing.Optional[typing.Union[CognitoUserPoolClientAnalyticsConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
        auth_session_validity: typing.Optional[jsii.Number] = None,
        callback_urls: typing.Optional[typing.Sequence[builtins.str]] = None,
        default_redirect_uri: typing.Optional[builtins.str] = None,
        enable_propagate_additional_user_context_data: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enable_token_revocation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        explicit_auth_flows: typing.Optional[typing.Sequence[builtins.str]] = None,
        generate_secret: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        id_token_validity: typing.Optional[jsii.Number] = None,
        logout_urls: typing.Optional[typing.Sequence[builtins.str]] = None,
        prevent_user_existence_errors: typing.Optional[builtins.str] = None,
        read_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
        refresh_token_validity: typing.Optional[jsii.Number] = None,
        supported_identity_providers: typing.Optional[typing.Sequence[builtins.str]] = None,
        token_validity_units: typing.Optional[typing.Union["CognitoUserPoolClientTokenValidityUnits", typing.Dict[builtins.str, typing.Any]]] = None,
        write_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#name CognitoUserPoolClient#name}.
        :param user_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#user_pool_id CognitoUserPoolClient#user_pool_id}.
        :param access_token_validity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#access_token_validity CognitoUserPoolClient#access_token_validity}.
        :param allowed_oauth_flows: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#allowed_oauth_flows CognitoUserPoolClient#allowed_oauth_flows}.
        :param allowed_oauth_flows_user_pool_client: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#allowed_oauth_flows_user_pool_client CognitoUserPoolClient#allowed_oauth_flows_user_pool_client}.
        :param allowed_oauth_scopes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#allowed_oauth_scopes CognitoUserPoolClient#allowed_oauth_scopes}.
        :param analytics_configuration: analytics_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#analytics_configuration CognitoUserPoolClient#analytics_configuration}
        :param auth_session_validity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#auth_session_validity CognitoUserPoolClient#auth_session_validity}.
        :param callback_urls: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#callback_urls CognitoUserPoolClient#callback_urls}.
        :param default_redirect_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#default_redirect_uri CognitoUserPoolClient#default_redirect_uri}.
        :param enable_propagate_additional_user_context_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#enable_propagate_additional_user_context_data CognitoUserPoolClient#enable_propagate_additional_user_context_data}.
        :param enable_token_revocation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#enable_token_revocation CognitoUserPoolClient#enable_token_revocation}.
        :param explicit_auth_flows: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#explicit_auth_flows CognitoUserPoolClient#explicit_auth_flows}.
        :param generate_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#generate_secret CognitoUserPoolClient#generate_secret}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#id CognitoUserPoolClient#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param id_token_validity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#id_token_validity CognitoUserPoolClient#id_token_validity}.
        :param logout_urls: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#logout_urls CognitoUserPoolClient#logout_urls}.
        :param prevent_user_existence_errors: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#prevent_user_existence_errors CognitoUserPoolClient#prevent_user_existence_errors}.
        :param read_attributes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#read_attributes CognitoUserPoolClient#read_attributes}.
        :param refresh_token_validity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#refresh_token_validity CognitoUserPoolClient#refresh_token_validity}.
        :param supported_identity_providers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#supported_identity_providers CognitoUserPoolClient#supported_identity_providers}.
        :param token_validity_units: token_validity_units block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#token_validity_units CognitoUserPoolClient#token_validity_units}
        :param write_attributes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#write_attributes CognitoUserPoolClient#write_attributes}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(analytics_configuration, dict):
            analytics_configuration = CognitoUserPoolClientAnalyticsConfiguration(**analytics_configuration)
        if isinstance(token_validity_units, dict):
            token_validity_units = CognitoUserPoolClientTokenValidityUnits(**token_validity_units)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5cc412ddd01de243d85ab49f0ae03ecdd7f5add90f27fc1a29f0c69edac82c59)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument user_pool_id", value=user_pool_id, expected_type=type_hints["user_pool_id"])
            check_type(argname="argument access_token_validity", value=access_token_validity, expected_type=type_hints["access_token_validity"])
            check_type(argname="argument allowed_oauth_flows", value=allowed_oauth_flows, expected_type=type_hints["allowed_oauth_flows"])
            check_type(argname="argument allowed_oauth_flows_user_pool_client", value=allowed_oauth_flows_user_pool_client, expected_type=type_hints["allowed_oauth_flows_user_pool_client"])
            check_type(argname="argument allowed_oauth_scopes", value=allowed_oauth_scopes, expected_type=type_hints["allowed_oauth_scopes"])
            check_type(argname="argument analytics_configuration", value=analytics_configuration, expected_type=type_hints["analytics_configuration"])
            check_type(argname="argument auth_session_validity", value=auth_session_validity, expected_type=type_hints["auth_session_validity"])
            check_type(argname="argument callback_urls", value=callback_urls, expected_type=type_hints["callback_urls"])
            check_type(argname="argument default_redirect_uri", value=default_redirect_uri, expected_type=type_hints["default_redirect_uri"])
            check_type(argname="argument enable_propagate_additional_user_context_data", value=enable_propagate_additional_user_context_data, expected_type=type_hints["enable_propagate_additional_user_context_data"])
            check_type(argname="argument enable_token_revocation", value=enable_token_revocation, expected_type=type_hints["enable_token_revocation"])
            check_type(argname="argument explicit_auth_flows", value=explicit_auth_flows, expected_type=type_hints["explicit_auth_flows"])
            check_type(argname="argument generate_secret", value=generate_secret, expected_type=type_hints["generate_secret"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument id_token_validity", value=id_token_validity, expected_type=type_hints["id_token_validity"])
            check_type(argname="argument logout_urls", value=logout_urls, expected_type=type_hints["logout_urls"])
            check_type(argname="argument prevent_user_existence_errors", value=prevent_user_existence_errors, expected_type=type_hints["prevent_user_existence_errors"])
            check_type(argname="argument read_attributes", value=read_attributes, expected_type=type_hints["read_attributes"])
            check_type(argname="argument refresh_token_validity", value=refresh_token_validity, expected_type=type_hints["refresh_token_validity"])
            check_type(argname="argument supported_identity_providers", value=supported_identity_providers, expected_type=type_hints["supported_identity_providers"])
            check_type(argname="argument token_validity_units", value=token_validity_units, expected_type=type_hints["token_validity_units"])
            check_type(argname="argument write_attributes", value=write_attributes, expected_type=type_hints["write_attributes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "user_pool_id": user_pool_id,
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
        if access_token_validity is not None:
            self._values["access_token_validity"] = access_token_validity
        if allowed_oauth_flows is not None:
            self._values["allowed_oauth_flows"] = allowed_oauth_flows
        if allowed_oauth_flows_user_pool_client is not None:
            self._values["allowed_oauth_flows_user_pool_client"] = allowed_oauth_flows_user_pool_client
        if allowed_oauth_scopes is not None:
            self._values["allowed_oauth_scopes"] = allowed_oauth_scopes
        if analytics_configuration is not None:
            self._values["analytics_configuration"] = analytics_configuration
        if auth_session_validity is not None:
            self._values["auth_session_validity"] = auth_session_validity
        if callback_urls is not None:
            self._values["callback_urls"] = callback_urls
        if default_redirect_uri is not None:
            self._values["default_redirect_uri"] = default_redirect_uri
        if enable_propagate_additional_user_context_data is not None:
            self._values["enable_propagate_additional_user_context_data"] = enable_propagate_additional_user_context_data
        if enable_token_revocation is not None:
            self._values["enable_token_revocation"] = enable_token_revocation
        if explicit_auth_flows is not None:
            self._values["explicit_auth_flows"] = explicit_auth_flows
        if generate_secret is not None:
            self._values["generate_secret"] = generate_secret
        if id is not None:
            self._values["id"] = id
        if id_token_validity is not None:
            self._values["id_token_validity"] = id_token_validity
        if logout_urls is not None:
            self._values["logout_urls"] = logout_urls
        if prevent_user_existence_errors is not None:
            self._values["prevent_user_existence_errors"] = prevent_user_existence_errors
        if read_attributes is not None:
            self._values["read_attributes"] = read_attributes
        if refresh_token_validity is not None:
            self._values["refresh_token_validity"] = refresh_token_validity
        if supported_identity_providers is not None:
            self._values["supported_identity_providers"] = supported_identity_providers
        if token_validity_units is not None:
            self._values["token_validity_units"] = token_validity_units
        if write_attributes is not None:
            self._values["write_attributes"] = write_attributes

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#name CognitoUserPoolClient#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_pool_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#user_pool_id CognitoUserPoolClient#user_pool_id}.'''
        result = self._values.get("user_pool_id")
        assert result is not None, "Required property 'user_pool_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_token_validity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#access_token_validity CognitoUserPoolClient#access_token_validity}.'''
        result = self._values.get("access_token_validity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def allowed_oauth_flows(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#allowed_oauth_flows CognitoUserPoolClient#allowed_oauth_flows}.'''
        result = self._values.get("allowed_oauth_flows")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allowed_oauth_flows_user_pool_client(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#allowed_oauth_flows_user_pool_client CognitoUserPoolClient#allowed_oauth_flows_user_pool_client}.'''
        result = self._values.get("allowed_oauth_flows_user_pool_client")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def allowed_oauth_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#allowed_oauth_scopes CognitoUserPoolClient#allowed_oauth_scopes}.'''
        result = self._values.get("allowed_oauth_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def analytics_configuration(
        self,
    ) -> typing.Optional[CognitoUserPoolClientAnalyticsConfiguration]:
        '''analytics_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#analytics_configuration CognitoUserPoolClient#analytics_configuration}
        '''
        result = self._values.get("analytics_configuration")
        return typing.cast(typing.Optional[CognitoUserPoolClientAnalyticsConfiguration], result)

    @builtins.property
    def auth_session_validity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#auth_session_validity CognitoUserPoolClient#auth_session_validity}.'''
        result = self._values.get("auth_session_validity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def callback_urls(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#callback_urls CognitoUserPoolClient#callback_urls}.'''
        result = self._values.get("callback_urls")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def default_redirect_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#default_redirect_uri CognitoUserPoolClient#default_redirect_uri}.'''
        result = self._values.get("default_redirect_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_propagate_additional_user_context_data(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#enable_propagate_additional_user_context_data CognitoUserPoolClient#enable_propagate_additional_user_context_data}.'''
        result = self._values.get("enable_propagate_additional_user_context_data")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enable_token_revocation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#enable_token_revocation CognitoUserPoolClient#enable_token_revocation}.'''
        result = self._values.get("enable_token_revocation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def explicit_auth_flows(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#explicit_auth_flows CognitoUserPoolClient#explicit_auth_flows}.'''
        result = self._values.get("explicit_auth_flows")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def generate_secret(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#generate_secret CognitoUserPoolClient#generate_secret}.'''
        result = self._values.get("generate_secret")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#id CognitoUserPoolClient#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id_token_validity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#id_token_validity CognitoUserPoolClient#id_token_validity}.'''
        result = self._values.get("id_token_validity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def logout_urls(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#logout_urls CognitoUserPoolClient#logout_urls}.'''
        result = self._values.get("logout_urls")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def prevent_user_existence_errors(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#prevent_user_existence_errors CognitoUserPoolClient#prevent_user_existence_errors}.'''
        result = self._values.get("prevent_user_existence_errors")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_attributes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#read_attributes CognitoUserPoolClient#read_attributes}.'''
        result = self._values.get("read_attributes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def refresh_token_validity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#refresh_token_validity CognitoUserPoolClient#refresh_token_validity}.'''
        result = self._values.get("refresh_token_validity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def supported_identity_providers(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#supported_identity_providers CognitoUserPoolClient#supported_identity_providers}.'''
        result = self._values.get("supported_identity_providers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def token_validity_units(
        self,
    ) -> typing.Optional["CognitoUserPoolClientTokenValidityUnits"]:
        '''token_validity_units block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#token_validity_units CognitoUserPoolClient#token_validity_units}
        '''
        result = self._values.get("token_validity_units")
        return typing.cast(typing.Optional["CognitoUserPoolClientTokenValidityUnits"], result)

    @builtins.property
    def write_attributes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#write_attributes CognitoUserPoolClient#write_attributes}.'''
        result = self._values.get("write_attributes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoUserPoolClientConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.cognitoUserPoolClient.CognitoUserPoolClientTokenValidityUnits",
    jsii_struct_bases=[],
    name_mapping={
        "access_token": "accessToken",
        "id_token": "idToken",
        "refresh_token": "refreshToken",
    },
)
class CognitoUserPoolClientTokenValidityUnits:
    def __init__(
        self,
        *,
        access_token: typing.Optional[builtins.str] = None,
        id_token: typing.Optional[builtins.str] = None,
        refresh_token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#access_token CognitoUserPoolClient#access_token}.
        :param id_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#id_token CognitoUserPoolClient#id_token}.
        :param refresh_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#refresh_token CognitoUserPoolClient#refresh_token}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35df8aa532c7e6fb01cc582686bb625e5db497c55b3fb4242513d88e68be77a9)
            check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
            check_type(argname="argument id_token", value=id_token, expected_type=type_hints["id_token"])
            check_type(argname="argument refresh_token", value=refresh_token, expected_type=type_hints["refresh_token"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if access_token is not None:
            self._values["access_token"] = access_token
        if id_token is not None:
            self._values["id_token"] = id_token
        if refresh_token is not None:
            self._values["refresh_token"] = refresh_token

    @builtins.property
    def access_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#access_token CognitoUserPoolClient#access_token}.'''
        result = self._values.get("access_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#id_token CognitoUserPoolClient#id_token}.'''
        result = self._values.get("id_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def refresh_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_user_pool_client#refresh_token CognitoUserPoolClient#refresh_token}.'''
        result = self._values.get("refresh_token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoUserPoolClientTokenValidityUnits(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CognitoUserPoolClientTokenValidityUnitsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoUserPoolClient.CognitoUserPoolClientTokenValidityUnitsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b587fbfaa72c1f23d4c2c3fd0454a89a4051686ba347cacfe82af9dd451b74d3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAccessToken")
    def reset_access_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessToken", []))

    @jsii.member(jsii_name="resetIdToken")
    def reset_id_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdToken", []))

    @jsii.member(jsii_name="resetRefreshToken")
    def reset_refresh_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRefreshToken", []))

    @builtins.property
    @jsii.member(jsii_name="accessTokenInput")
    def access_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="idTokenInput")
    def id_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="refreshTokenInput")
    def refresh_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "refreshTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="accessToken")
    def access_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessToken"))

    @access_token.setter
    def access_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e003b878db5a58571df59fd557ab9dd60d8d1c7faa4b94a29b745c28bb1c3d55)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessToken", value)

    @builtins.property
    @jsii.member(jsii_name="idToken")
    def id_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "idToken"))

    @id_token.setter
    def id_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5121e0b70f71ccf1bcf8ee7ba75e6151c0d76bc4e16530acf55baca2bfc6916f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idToken", value)

    @builtins.property
    @jsii.member(jsii_name="refreshToken")
    def refresh_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "refreshToken"))

    @refresh_token.setter
    def refresh_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d562a5397ff47082335aef5dd9f30cdaeaa11e46b3dc75e90e1d9579cbb29a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "refreshToken", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CognitoUserPoolClientTokenValidityUnits]:
        return typing.cast(typing.Optional[CognitoUserPoolClientTokenValidityUnits], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoUserPoolClientTokenValidityUnits],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e9aeea842db244b19fda5302295ff60d937165e6bc2560d072d764873b0ac61)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CognitoUserPoolClient",
    "CognitoUserPoolClientAnalyticsConfiguration",
    "CognitoUserPoolClientAnalyticsConfigurationOutputReference",
    "CognitoUserPoolClientConfig",
    "CognitoUserPoolClientTokenValidityUnits",
    "CognitoUserPoolClientTokenValidityUnitsOutputReference",
]

publication.publish()

def _typecheckingstub__511c7ff14a8932ea37343d7b24259d7e75d80a14afa327ef308819678ce6e1cc(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    user_pool_id: builtins.str,
    access_token_validity: typing.Optional[jsii.Number] = None,
    allowed_oauth_flows: typing.Optional[typing.Sequence[builtins.str]] = None,
    allowed_oauth_flows_user_pool_client: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    allowed_oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    analytics_configuration: typing.Optional[typing.Union[CognitoUserPoolClientAnalyticsConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    auth_session_validity: typing.Optional[jsii.Number] = None,
    callback_urls: typing.Optional[typing.Sequence[builtins.str]] = None,
    default_redirect_uri: typing.Optional[builtins.str] = None,
    enable_propagate_additional_user_context_data: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_token_revocation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    explicit_auth_flows: typing.Optional[typing.Sequence[builtins.str]] = None,
    generate_secret: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    id_token_validity: typing.Optional[jsii.Number] = None,
    logout_urls: typing.Optional[typing.Sequence[builtins.str]] = None,
    prevent_user_existence_errors: typing.Optional[builtins.str] = None,
    read_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
    refresh_token_validity: typing.Optional[jsii.Number] = None,
    supported_identity_providers: typing.Optional[typing.Sequence[builtins.str]] = None,
    token_validity_units: typing.Optional[typing.Union[CognitoUserPoolClientTokenValidityUnits, typing.Dict[builtins.str, typing.Any]]] = None,
    write_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
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

def _typecheckingstub__590d0554e9ba4ac843b8edc65cd137c735daedaa4ee1384800e40fa8ec31b1d9(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0d1a1696ef080498b7b8acb0f2832e9dd66ec32060a7cc533c711b235416d16(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d87f6f3a66fea2a5dfd3988c344796685dfb3ef334a49b6165ea9f4ee5e6cee2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4825593a1592d08175fa18bc123637df107132f5ace254565277d5915ab0cbe(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e358e3c6cd53a16161eccd74bf573f23615986256c406fd0b41207524a09fd96(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__212c00a4cb167809ba119ca361788d043de54842e19d42a6e9d2d35078777fd4(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c1f102576c59414fd937570336019b955baece2cbf88158e8758913405599bd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcaea5209f61cbe6afd4653f4cc3c2e147eafd75fd90f6bf882304b967d9d79d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a2276616df227891437371a2209259a8b29b94c6d240b503d6057af833aa4ea(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__458de31a6b3aac524cff1074f2578cae179d48869797df1c827ced14c998da8e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14fe65ee9b13938e11b9a4640b98d86865cf3af58a33d4bfe04869e24da43917(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f54e5693c7326838c2c547c8e607adbb98ba7c78761bf4690358df514a3fb65(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b196a51b57cb6fbe5a53490d4304107b430cd373084eb462d21779cd047c736(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9907bc104e9b083023dbd0abdfe0367bb86fa8114b34f0c805375a9c2712dec4(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd48699517039e99885b9ab49e844ead27cf33d740ffd2def2215dc2c7bd56a2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80b5891819658be40b6a79bed6c694d2701236436806613d87f40a98dc88bed3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0905b9118deeb1da73fcfea14322f912694ec9083fa246ab392f57e062859d4(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__445b955cc4b2929df1e7a1bfe66fb4fa0e4455053f01a505c20a52f501cf8687(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abf243cdb5ed85edefb47f2dcd213ae23b293587d252460f5f66af28fc6a73ae(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d11b8ca34e95643134bd3d4b6cb56e1f214625a97a144c2b9bb01ab05ef13a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfdbd30c57b72063f742c9e40d5e425bbd1c9f3bcec639dfac106cad43ef9f5b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__405d23f642cabccb14cef6b4e62389a08e41e6799fcb3f2d25b23d5e03a99467(
    *,
    application_arn: typing.Optional[builtins.str] = None,
    application_id: typing.Optional[builtins.str] = None,
    external_id: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
    user_data_shared: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62851741af7c2fbc3315881e24aa8286fd550342c491f64739e6a9de0d6c058c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5492b978669298f7f3927be77721312b240f4e1090fa63397603d6f9d28b27f7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a88640c4a02a7d8a7295542cd451050026908fec262d65f4b1e28b62c74de34(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__530b4f88711c255323d54388898279038fadb4d655f6f605c0cbf6a8fdfa2d6e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5813c87c348a084f5f8b38559f36ed04a21322d73ff8fbdaf389a6d2bd22b21(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e5af869f8ffc7c1db3733a1fa3732a90116f32c22151b98ea2795fccc9f4e12(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b14f03dc499843465713ee6be840a371ca2ebb0c979ab4fb3d9c1a228742ac5(
    value: typing.Optional[CognitoUserPoolClientAnalyticsConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cc412ddd01de243d85ab49f0ae03ecdd7f5add90f27fc1a29f0c69edac82c59(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    user_pool_id: builtins.str,
    access_token_validity: typing.Optional[jsii.Number] = None,
    allowed_oauth_flows: typing.Optional[typing.Sequence[builtins.str]] = None,
    allowed_oauth_flows_user_pool_client: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    allowed_oauth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    analytics_configuration: typing.Optional[typing.Union[CognitoUserPoolClientAnalyticsConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    auth_session_validity: typing.Optional[jsii.Number] = None,
    callback_urls: typing.Optional[typing.Sequence[builtins.str]] = None,
    default_redirect_uri: typing.Optional[builtins.str] = None,
    enable_propagate_additional_user_context_data: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enable_token_revocation: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    explicit_auth_flows: typing.Optional[typing.Sequence[builtins.str]] = None,
    generate_secret: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    id_token_validity: typing.Optional[jsii.Number] = None,
    logout_urls: typing.Optional[typing.Sequence[builtins.str]] = None,
    prevent_user_existence_errors: typing.Optional[builtins.str] = None,
    read_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
    refresh_token_validity: typing.Optional[jsii.Number] = None,
    supported_identity_providers: typing.Optional[typing.Sequence[builtins.str]] = None,
    token_validity_units: typing.Optional[typing.Union[CognitoUserPoolClientTokenValidityUnits, typing.Dict[builtins.str, typing.Any]]] = None,
    write_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35df8aa532c7e6fb01cc582686bb625e5db497c55b3fb4242513d88e68be77a9(
    *,
    access_token: typing.Optional[builtins.str] = None,
    id_token: typing.Optional[builtins.str] = None,
    refresh_token: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b587fbfaa72c1f23d4c2c3fd0454a89a4051686ba347cacfe82af9dd451b74d3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e003b878db5a58571df59fd557ab9dd60d8d1c7faa4b94a29b745c28bb1c3d55(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5121e0b70f71ccf1bcf8ee7ba75e6151c0d76bc4e16530acf55baca2bfc6916f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d562a5397ff47082335aef5dd9f30cdaeaa11e46b3dc75e90e1d9579cbb29a4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e9aeea842db244b19fda5302295ff60d937165e6bc2560d072d764873b0ac61(
    value: typing.Optional[CognitoUserPoolClientTokenValidityUnits],
) -> None:
    """Type checking stubs"""
    pass
