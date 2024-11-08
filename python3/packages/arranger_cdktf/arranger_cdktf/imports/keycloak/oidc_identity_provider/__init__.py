"""
# `keycloak_oidc_identity_provider`

Refer to the Terraform Registory for docs: [`keycloak_oidc_identity_provider`](https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider).
"""
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


class OidcIdentityProvider(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.oidcIdentityProvider.OidcIdentityProvider",
):
    """Represents a {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider keycloak_oidc_identity_provider}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        alias: builtins.str,
        authorization_url: builtins.str,
        client_id: builtins.str,
        client_secret: builtins.str,
        realm: builtins.str,
        token_url: builtins.str,
        accepts_prompt_none_forward_from_client: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        add_read_token_role_on_create: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        authenticate_by_default: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        backchannel_supported: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        default_scopes: typing.Optional[builtins.str] = None,
        disable_user_info: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        display_name: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        extra_config: typing.Optional[
            typing.Mapping[builtins.str, builtins.str]
        ] = None,
        first_broker_login_flow_alias: typing.Optional[builtins.str] = None,
        gui_order: typing.Optional[builtins.str] = None,
        hide_on_login_page: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        id: typing.Optional[builtins.str] = None,
        issuer: typing.Optional[builtins.str] = None,
        jwks_url: typing.Optional[builtins.str] = None,
        link_only: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        login_hint: typing.Optional[builtins.str] = None,
        logout_url: typing.Optional[builtins.str] = None,
        post_broker_login_flow_alias: typing.Optional[builtins.str] = None,
        provider_id: typing.Optional[builtins.str] = None,
        store_token: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        sync_mode: typing.Optional[builtins.str] = None,
        trust_email: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        ui_locales: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        user_info_url: typing.Optional[builtins.str] = None,
        validate_signature: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        connection: typing.Optional[
            typing.Union[
                typing.Union[
                    _cdktf_9a9027ec.SSHProvisionerConnection,
                    typing.Dict[builtins.str, typing.Any],
                ],
                typing.Union[
                    _cdktf_9a9027ec.WinrmProvisionerConnection,
                    typing.Dict[builtins.str, typing.Any],
                ],
            ]
        ] = None,
        count: typing.Optional[
            typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]
        ] = None,
        depends_on: typing.Optional[
            typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]
        ] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.TerraformResourceLifecycle,
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[
            typing.Sequence[
                typing.Union[
                    typing.Union[
                        _cdktf_9a9027ec.FileProvisioner,
                        typing.Dict[builtins.str, typing.Any],
                    ],
                    typing.Union[
                        _cdktf_9a9027ec.LocalExecProvisioner,
                        typing.Dict[builtins.str, typing.Any],
                    ],
                    typing.Union[
                        _cdktf_9a9027ec.RemoteExecProvisioner,
                        typing.Dict[builtins.str, typing.Any],
                    ],
                ]
            ]
        ] = None,
    ) -> None:
        """Create a new {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider keycloak_oidc_identity_provider} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param alias: The alias uniquely identifies an identity provider and it is also used to build the redirect uri. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#alias OidcIdentityProvider#alias}
        :param authorization_url: OIDC authorization URL. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#authorization_url OidcIdentityProvider#authorization_url}
        :param client_id: Client ID. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#client_id OidcIdentityProvider#client_id}
        :param client_secret: Client Secret. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#client_secret OidcIdentityProvider#client_secret}
        :param realm: Realm Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#realm OidcIdentityProvider#realm}
        :param token_url: Token URL. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#token_url OidcIdentityProvider#token_url}
        :param accepts_prompt_none_forward_from_client: This is just used together with Identity Provider Authenticator or when kc_idp_hint points to this identity provider. In case that client sends a request with prompt=none and user is not yet authenticated, the error will not be directly returned to client, but the request with prompt=none will be forwarded to this identity provider. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#accepts_prompt_none_forward_from_client OidcIdentityProvider#accepts_prompt_none_forward_from_client}
        :param add_read_token_role_on_create: Enable/disable if new users can read any stored tokens. This assigns the broker.read-token role. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#add_read_token_role_on_create OidcIdentityProvider#add_read_token_role_on_create}
        :param authenticate_by_default: Enable/disable authenticate users by default. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#authenticate_by_default OidcIdentityProvider#authenticate_by_default}
        :param backchannel_supported: Does the external IDP support backchannel logout? Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#backchannel_supported OidcIdentityProvider#backchannel_supported}
        :param default_scopes: The scopes to be sent when asking for authorization. It can be a space-separated list of scopes. Defaults to 'openid'. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#default_scopes OidcIdentityProvider#default_scopes}
        :param disable_user_info: Disable usage of User Info service to obtain additional user information? Default is to use this OIDC service. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#disable_user_info OidcIdentityProvider#disable_user_info}
        :param display_name: Friendly name for Identity Providers. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#display_name OidcIdentityProvider#display_name}
        :param enabled: Enable/disable this identity provider. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#enabled OidcIdentityProvider#enabled}
        :param extra_config: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#extra_config OidcIdentityProvider#extra_config}.
        :param first_broker_login_flow_alias: Alias of authentication flow, which is triggered after first login with this identity provider. Term 'First Login' means that there is not yet existing Keycloak account linked with the authenticated identity provider account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#first_broker_login_flow_alias OidcIdentityProvider#first_broker_login_flow_alias}
        :param gui_order: GUI Order. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#gui_order OidcIdentityProvider#gui_order}
        :param hide_on_login_page: Hide On Login Page. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#hide_on_login_page OidcIdentityProvider#hide_on_login_page}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#id OidcIdentityProvider#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param issuer: The issuer identifier for the issuer of the response. If not provided, no validation will be performed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#issuer OidcIdentityProvider#issuer}
        :param jwks_url: JSON Web Key Set URL. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#jwks_url OidcIdentityProvider#jwks_url}
        :param link_only: If true, users cannot log in through this provider. They can only link to this provider. This is useful if you don't want to allow login from the provider, but want to integrate with a provider Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#link_only OidcIdentityProvider#link_only}
        :param login_hint: Login Hint. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#login_hint OidcIdentityProvider#login_hint}
        :param logout_url: Logout URL. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#logout_url OidcIdentityProvider#logout_url}
        :param post_broker_login_flow_alias: Alias of authentication flow, which is triggered after each login with this identity provider. Useful if you want additional verification of each user authenticated with this identity provider (for example OTP). Leave this empty if you don't want any additional authenticators to be triggered after login with this identity provider. Also note, that authenticator implementations must assume that user is already set in ClientSession as identity provider already set it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#post_broker_login_flow_alias OidcIdentityProvider#post_broker_login_flow_alias}
        :param provider_id: provider id, is always oidc, unless you have a custom implementation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#provider_id OidcIdentityProvider#provider_id}
        :param store_token: Enable/disable if tokens must be stored after authenticating users. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#store_token OidcIdentityProvider#store_token}
        :param sync_mode: Sync Mode. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#sync_mode OidcIdentityProvider#sync_mode}
        :param trust_email: If enabled then email provided by this provider is not verified even if verification is enabled for the realm. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#trust_email OidcIdentityProvider#trust_email}
        :param ui_locales: Pass current locale to identity provider. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#ui_locales OidcIdentityProvider#ui_locales}
        :param user_info_url: User Info URL. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#user_info_url OidcIdentityProvider#user_info_url}
        :param validate_signature: Enable/disable signature validation of external IDP signatures. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#validate_signature OidcIdentityProvider#validate_signature}
        :param connection:
        :param count:
        :param depends_on:
        :param for_each:
        :param lifecycle:
        :param provider:
        :param provisioners:
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__ef9a2d88a75bd9f56efea1e4e62d253c51b5e058f3885112eed887bb5e513ddd
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(
                argname="argument id_", value=id_, expected_type=type_hints["id_"]
            )
        config = OidcIdentityProviderConfig(
            alias=alias,
            authorization_url=authorization_url,
            client_id=client_id,
            client_secret=client_secret,
            realm=realm,
            token_url=token_url,
            accepts_prompt_none_forward_from_client=accepts_prompt_none_forward_from_client,
            add_read_token_role_on_create=add_read_token_role_on_create,
            authenticate_by_default=authenticate_by_default,
            backchannel_supported=backchannel_supported,
            default_scopes=default_scopes,
            disable_user_info=disable_user_info,
            display_name=display_name,
            enabled=enabled,
            extra_config=extra_config,
            first_broker_login_flow_alias=first_broker_login_flow_alias,
            gui_order=gui_order,
            hide_on_login_page=hide_on_login_page,
            id=id,
            issuer=issuer,
            jwks_url=jwks_url,
            link_only=link_only,
            login_hint=login_hint,
            logout_url=logout_url,
            post_broker_login_flow_alias=post_broker_login_flow_alias,
            provider_id=provider_id,
            store_token=store_token,
            sync_mode=sync_mode,
            trust_email=trust_email,
            ui_locales=ui_locales,
            user_info_url=user_info_url,
            validate_signature=validate_signature,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetAcceptsPromptNoneForwardFromClient")
    def reset_accepts_prompt_none_forward_from_client(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetAcceptsPromptNoneForwardFromClient", [])
        )

    @jsii.member(jsii_name="resetAddReadTokenRoleOnCreate")
    def reset_add_read_token_role_on_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddReadTokenRoleOnCreate", []))

    @jsii.member(jsii_name="resetAuthenticateByDefault")
    def reset_authenticate_by_default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthenticateByDefault", []))

    @jsii.member(jsii_name="resetBackchannelSupported")
    def reset_backchannel_supported(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackchannelSupported", []))

    @jsii.member(jsii_name="resetDefaultScopes")
    def reset_default_scopes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultScopes", []))

    @jsii.member(jsii_name="resetDisableUserInfo")
    def reset_disable_user_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableUserInfo", []))

    @jsii.member(jsii_name="resetDisplayName")
    def reset_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayName", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetExtraConfig")
    def reset_extra_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtraConfig", []))

    @jsii.member(jsii_name="resetFirstBrokerLoginFlowAlias")
    def reset_first_broker_login_flow_alias(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetFirstBrokerLoginFlowAlias", [])
        )

    @jsii.member(jsii_name="resetGuiOrder")
    def reset_gui_order(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGuiOrder", []))

    @jsii.member(jsii_name="resetHideOnLoginPage")
    def reset_hide_on_login_page(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHideOnLoginPage", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIssuer")
    def reset_issuer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIssuer", []))

    @jsii.member(jsii_name="resetJwksUrl")
    def reset_jwks_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJwksUrl", []))

    @jsii.member(jsii_name="resetLinkOnly")
    def reset_link_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinkOnly", []))

    @jsii.member(jsii_name="resetLoginHint")
    def reset_login_hint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoginHint", []))

    @jsii.member(jsii_name="resetLogoutUrl")
    def reset_logout_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogoutUrl", []))

    @jsii.member(jsii_name="resetPostBrokerLoginFlowAlias")
    def reset_post_broker_login_flow_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPostBrokerLoginFlowAlias", []))

    @jsii.member(jsii_name="resetProviderId")
    def reset_provider_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProviderId", []))

    @jsii.member(jsii_name="resetStoreToken")
    def reset_store_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStoreToken", []))

    @jsii.member(jsii_name="resetSyncMode")
    def reset_sync_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSyncMode", []))

    @jsii.member(jsii_name="resetTrustEmail")
    def reset_trust_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrustEmail", []))

    @jsii.member(jsii_name="resetUiLocales")
    def reset_ui_locales(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUiLocales", []))

    @jsii.member(jsii_name="resetUserInfoUrl")
    def reset_user_info_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserInfoUrl", []))

    @jsii.member(jsii_name="resetValidateSignature")
    def reset_validate_signature(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValidateSignature", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(
            typing.Mapping[builtins.str, typing.Any],
            jsii.invoke(self, "synthesizeAttributes", []),
        )

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="internalId")
    def internal_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "internalId"))

    @builtins.property
    @jsii.member(jsii_name="acceptsPromptNoneForwardFromClientInput")
    def accepts_prompt_none_forward_from_client_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "acceptsPromptNoneForwardFromClientInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="addReadTokenRoleOnCreateInput")
    def add_read_token_role_on_create_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "addReadTokenRoleOnCreateInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="authenticateByDefaultInput")
    def authenticate_by_default_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "authenticateByDefaultInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="authorizationUrlInput")
    def authorization_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "authorizationUrlInput")
        )

    @builtins.property
    @jsii.member(jsii_name="backchannelSupportedInput")
    def backchannel_supported_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "backchannelSupportedInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "clientIdInput")
        )

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "clientSecretInput")
        )

    @builtins.property
    @jsii.member(jsii_name="defaultScopesInput")
    def default_scopes_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "defaultScopesInput")
        )

    @builtins.property
    @jsii.member(jsii_name="disableUserInfoInput")
    def disable_user_info_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "disableUserInfoInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "displayNameInput")
        )

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "enabledInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="extraConfigInput")
    def extra_config_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(
            typing.Optional[typing.Mapping[builtins.str, builtins.str]],
            jsii.get(self, "extraConfigInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="firstBrokerLoginFlowAliasInput")
    def first_broker_login_flow_alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "firstBrokerLoginFlowAliasInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="guiOrderInput")
    def gui_order_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "guiOrderInput")
        )

    @builtins.property
    @jsii.member(jsii_name="hideOnLoginPageInput")
    def hide_on_login_page_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "hideOnLoginPageInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="issuerInput")
    def issuer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "issuerInput"))

    @builtins.property
    @jsii.member(jsii_name="jwksUrlInput")
    def jwks_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "jwksUrlInput")
        )

    @builtins.property
    @jsii.member(jsii_name="linkOnlyInput")
    def link_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "linkOnlyInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="loginHintInput")
    def login_hint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "loginHintInput")
        )

    @builtins.property
    @jsii.member(jsii_name="logoutUrlInput")
    def logout_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "logoutUrlInput")
        )

    @builtins.property
    @jsii.member(jsii_name="postBrokerLoginFlowAliasInput")
    def post_broker_login_flow_alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "postBrokerLoginFlowAliasInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="providerIdInput")
    def provider_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "providerIdInput")
        )

    @builtins.property
    @jsii.member(jsii_name="realmInput")
    def realm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "realmInput"))

    @builtins.property
    @jsii.member(jsii_name="storeTokenInput")
    def store_token_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "storeTokenInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="syncModeInput")
    def sync_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "syncModeInput")
        )

    @builtins.property
    @jsii.member(jsii_name="tokenUrlInput")
    def token_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "tokenUrlInput")
        )

    @builtins.property
    @jsii.member(jsii_name="trustEmailInput")
    def trust_email_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "trustEmailInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="uiLocalesInput")
    def ui_locales_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "uiLocalesInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="userInfoUrlInput")
    def user_info_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "userInfoUrlInput")
        )

    @builtins.property
    @jsii.member(jsii_name="validateSignatureInput")
    def validate_signature_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "validateSignatureInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="acceptsPromptNoneForwardFromClient")
    def accepts_prompt_none_forward_from_client(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "acceptsPromptNoneForwardFromClient"),
        )

    @accepts_prompt_none_forward_from_client.setter
    def accepts_prompt_none_forward_from_client(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__80dd9c503815b165fdf70bb0f3e7847f4882460ab06a177f10295608d92845dc
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "acceptsPromptNoneForwardFromClient", value)

    @builtins.property
    @jsii.member(jsii_name="addReadTokenRoleOnCreate")
    def add_read_token_role_on_create(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "addReadTokenRoleOnCreate"),
        )

    @add_read_token_role_on_create.setter
    def add_read_token_role_on_create(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__4ef67cd26e33229055d2c89d684d0bf6071d5aa6af5d23c05ad6cde0110f5eca
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "addReadTokenRoleOnCreate", value)

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d804b151a1cb22ff3444056ddddfeb9bb7b27a61fc5575fdc0a5118d0fef486f
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="authenticateByDefault")
    def authenticate_by_default(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "authenticateByDefault"),
        )

    @authenticate_by_default.setter
    def authenticate_by_default(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__e0d8240d514d6a47c1d03604c830ca082ce88c58f190f864b525b08c80307075
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "authenticateByDefault", value)

    @builtins.property
    @jsii.member(jsii_name="authorizationUrl")
    def authorization_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authorizationUrl"))

    @authorization_url.setter
    def authorization_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__635d7a7a6650b51465f842e8401ef6523b737264c6d9fb8a26d0992da60440d3
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "authorizationUrl", value)

    @builtins.property
    @jsii.member(jsii_name="backchannelSupported")
    def backchannel_supported(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "backchannelSupported"),
        )

    @backchannel_supported.setter
    def backchannel_supported(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__955926e783b0c03c5c96a2bdd218b9faab62f91ab5c7f3981ba523570527b456
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "backchannelSupported", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__e436d066e1e19a90880248f37d3e07b22398a10700efc9693c86fe98df669aed
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__58a3f4fc38b16b78d396b1fc08d6d24c63c64b652bcfe2179364e67873e5e988
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="defaultScopes")
    def default_scopes(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultScopes"))

    @default_scopes.setter
    def default_scopes(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__69658fde344f6e685e352d1ba1e4111669b84b89a5de54d777b0623853602939
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "defaultScopes", value)

    @builtins.property
    @jsii.member(jsii_name="disableUserInfo")
    def disable_user_info(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "disableUserInfo"),
        )

    @disable_user_info.setter
    def disable_user_info(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b6a7516998b4bcceda799f5949c8e92294934f83c5399ba535e930dcc5df7953
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "disableUserInfo", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b0f92dc649646a6bdf011ae403edd02221f9477b6a2878d89029fbfef3356867
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "enabled"),
        )

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__8cc85f69e23b46953f520ff7caac672378846912737429cd4410dc10f9ed0c78
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="extraConfig")
    def extra_config(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(
            typing.Mapping[builtins.str, builtins.str], jsii.get(self, "extraConfig")
        )

    @extra_config.setter
    def extra_config(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__04674e1a21f7205bf152ba8da9998e570742cb7694c04df9fa2c693039b1be06
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "extraConfig", value)

    @builtins.property
    @jsii.member(jsii_name="firstBrokerLoginFlowAlias")
    def first_broker_login_flow_alias(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firstBrokerLoginFlowAlias"))

    @first_broker_login_flow_alias.setter
    def first_broker_login_flow_alias(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__264f98d3232120e758f246aa0cc69c147a21c3d25993e5f313e2233111c22a5a
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "firstBrokerLoginFlowAlias", value)

    @builtins.property
    @jsii.member(jsii_name="guiOrder")
    def gui_order(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "guiOrder"))

    @gui_order.setter
    def gui_order(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__74782c940d00a357a25e9b9fa2e8ade5673d321d88c1442dc90ea2e7db821f0e
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "guiOrder", value)

    @builtins.property
    @jsii.member(jsii_name="hideOnLoginPage")
    def hide_on_login_page(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "hideOnLoginPage"),
        )

    @hide_on_login_page.setter
    def hide_on_login_page(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__0c0ec35d177af0b9f19b5922464ecda47e8d7bb6c70d4453106b4d6475eb0020
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "hideOnLoginPage", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__3ed947e772e933e67aee9b9cebf11d0dbea858823267299acf6b9e3caaf09f37
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="issuer")
    def issuer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issuer"))

    @issuer.setter
    def issuer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__5434e949bcf6c757088b9d0bb2395fed2e35486c18df4928f5831ad62d4ba085
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "issuer", value)

    @builtins.property
    @jsii.member(jsii_name="jwksUrl")
    def jwks_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jwksUrl"))

    @jwks_url.setter
    def jwks_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__78a471f3cfff54197465560ed2dd0bb04873797c9048bfcb22f21be0a0119d22
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "jwksUrl", value)

    @builtins.property
    @jsii.member(jsii_name="linkOnly")
    def link_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "linkOnly"),
        )

    @link_only.setter
    def link_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__8cffffdc57db6c7cb8665c3858ae8842317f20fa794fd9245faf051f9501ee9a
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "linkOnly", value)

    @builtins.property
    @jsii.member(jsii_name="loginHint")
    def login_hint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loginHint"))

    @login_hint.setter
    def login_hint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__e86cc9afbd861834e6317467ce04dac4589e3ae3d748b453779d8512aade1564
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "loginHint", value)

    @builtins.property
    @jsii.member(jsii_name="logoutUrl")
    def logout_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logoutUrl"))

    @logout_url.setter
    def logout_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d7ee4e926c9f21412e2b671f3e1c4641d0ddc55306ea13c0f9c39bd5719c00c3
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "logoutUrl", value)

    @builtins.property
    @jsii.member(jsii_name="postBrokerLoginFlowAlias")
    def post_broker_login_flow_alias(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "postBrokerLoginFlowAlias"))

    @post_broker_login_flow_alias.setter
    def post_broker_login_flow_alias(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__96de58e76dbe89ae92bbeff1a957cba8fccc5d354e83ba82f591be87438e64b8
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "postBrokerLoginFlowAlias", value)

    @builtins.property
    @jsii.member(jsii_name="providerId")
    def provider_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "providerId"))

    @provider_id.setter
    def provider_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__40aaffe9fde210c42f884c74193bc4bbe7a58e696c190f88419f265e76e7c255
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "providerId", value)

    @builtins.property
    @jsii.member(jsii_name="realm")
    def realm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "realm"))

    @realm.setter
    def realm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__69c6c04010cd9deab2e246736c371f247dcf0545f7d988787113a8e812e2a84a
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "realm", value)

    @builtins.property
    @jsii.member(jsii_name="storeToken")
    def store_token(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "storeToken"),
        )

    @store_token.setter
    def store_token(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b856ca7561801dd170ddaba3e2f68bdeec843c9452a960c03f82e23a9dbc42c0
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "storeToken", value)

    @builtins.property
    @jsii.member(jsii_name="syncMode")
    def sync_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "syncMode"))

    @sync_mode.setter
    def sync_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__6567043d182de4d600186a64a242a5dabf1109e81ef418fd170ac192c6e05c21
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "syncMode", value)

    @builtins.property
    @jsii.member(jsii_name="tokenUrl")
    def token_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tokenUrl"))

    @token_url.setter
    def token_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__ca2f036ef759bef5ee38ad56b6a785183c4f8c3fad25e5aba95b04ea802f3017
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "tokenUrl", value)

    @builtins.property
    @jsii.member(jsii_name="trustEmail")
    def trust_email(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "trustEmail"),
        )

    @trust_email.setter
    def trust_email(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__c2ef45fc351bc560f447cfba6c74a2ca86b98f3c00962a972e4559c554a924fa
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "trustEmail", value)

    @builtins.property
    @jsii.member(jsii_name="uiLocales")
    def ui_locales(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "uiLocales"),
        )

    @ui_locales.setter
    def ui_locales(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__2375b065380cfa73e40cffb759d7cd499d0d56fd294d6dd54f516897b4402d43
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "uiLocales", value)

    @builtins.property
    @jsii.member(jsii_name="userInfoUrl")
    def user_info_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userInfoUrl"))

    @user_info_url.setter
    def user_info_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a961af4c4b0e7588de4bfdc5631a6a4012256d1f7df4769a398eae3a55b1fcdf
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "userInfoUrl", value)

    @builtins.property
    @jsii.member(jsii_name="validateSignature")
    def validate_signature(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "validateSignature"),
        )

    @validate_signature.setter
    def validate_signature(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d6657582afcd45de05991f111d4450dac159624bfc6560c651eaa04e5a88faa8
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "validateSignature", value)


@jsii.data_type(
    jsii_type="keycloak.oidcIdentityProvider.OidcIdentityProviderConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "alias": "alias",
        "authorization_url": "authorizationUrl",
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "realm": "realm",
        "token_url": "tokenUrl",
        "accepts_prompt_none_forward_from_client": "acceptsPromptNoneForwardFromClient",
        "add_read_token_role_on_create": "addReadTokenRoleOnCreate",
        "authenticate_by_default": "authenticateByDefault",
        "backchannel_supported": "backchannelSupported",
        "default_scopes": "defaultScopes",
        "disable_user_info": "disableUserInfo",
        "display_name": "displayName",
        "enabled": "enabled",
        "extra_config": "extraConfig",
        "first_broker_login_flow_alias": "firstBrokerLoginFlowAlias",
        "gui_order": "guiOrder",
        "hide_on_login_page": "hideOnLoginPage",
        "id": "id",
        "issuer": "issuer",
        "jwks_url": "jwksUrl",
        "link_only": "linkOnly",
        "login_hint": "loginHint",
        "logout_url": "logoutUrl",
        "post_broker_login_flow_alias": "postBrokerLoginFlowAlias",
        "provider_id": "providerId",
        "store_token": "storeToken",
        "sync_mode": "syncMode",
        "trust_email": "trustEmail",
        "ui_locales": "uiLocales",
        "user_info_url": "userInfoUrl",
        "validate_signature": "validateSignature",
    },
)
class OidcIdentityProviderConfig(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[
            typing.Union[
                typing.Union[
                    _cdktf_9a9027ec.SSHProvisionerConnection,
                    typing.Dict[builtins.str, typing.Any],
                ],
                typing.Union[
                    _cdktf_9a9027ec.WinrmProvisionerConnection,
                    typing.Dict[builtins.str, typing.Any],
                ],
            ]
        ] = None,
        count: typing.Optional[
            typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]
        ] = None,
        depends_on: typing.Optional[
            typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]
        ] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.TerraformResourceLifecycle,
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[
            typing.Sequence[
                typing.Union[
                    typing.Union[
                        _cdktf_9a9027ec.FileProvisioner,
                        typing.Dict[builtins.str, typing.Any],
                    ],
                    typing.Union[
                        _cdktf_9a9027ec.LocalExecProvisioner,
                        typing.Dict[builtins.str, typing.Any],
                    ],
                    typing.Union[
                        _cdktf_9a9027ec.RemoteExecProvisioner,
                        typing.Dict[builtins.str, typing.Any],
                    ],
                ]
            ]
        ] = None,
        alias: builtins.str,
        authorization_url: builtins.str,
        client_id: builtins.str,
        client_secret: builtins.str,
        realm: builtins.str,
        token_url: builtins.str,
        accepts_prompt_none_forward_from_client: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        add_read_token_role_on_create: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        authenticate_by_default: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        backchannel_supported: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        default_scopes: typing.Optional[builtins.str] = None,
        disable_user_info: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        display_name: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        extra_config: typing.Optional[
            typing.Mapping[builtins.str, builtins.str]
        ] = None,
        first_broker_login_flow_alias: typing.Optional[builtins.str] = None,
        gui_order: typing.Optional[builtins.str] = None,
        hide_on_login_page: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        id: typing.Optional[builtins.str] = None,
        issuer: typing.Optional[builtins.str] = None,
        jwks_url: typing.Optional[builtins.str] = None,
        link_only: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        login_hint: typing.Optional[builtins.str] = None,
        logout_url: typing.Optional[builtins.str] = None,
        post_broker_login_flow_alias: typing.Optional[builtins.str] = None,
        provider_id: typing.Optional[builtins.str] = None,
        store_token: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        sync_mode: typing.Optional[builtins.str] = None,
        trust_email: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        ui_locales: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        user_info_url: typing.Optional[builtins.str] = None,
        validate_signature: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
    ) -> None:
        """
        :param connection:
        :param count:
        :param depends_on:
        :param for_each:
        :param lifecycle:
        :param provider:
        :param provisioners:
        :param alias: The alias uniquely identifies an identity provider and it is also used to build the redirect uri. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#alias OidcIdentityProvider#alias}
        :param authorization_url: OIDC authorization URL. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#authorization_url OidcIdentityProvider#authorization_url}
        :param client_id: Client ID. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#client_id OidcIdentityProvider#client_id}
        :param client_secret: Client Secret. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#client_secret OidcIdentityProvider#client_secret}
        :param realm: Realm Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#realm OidcIdentityProvider#realm}
        :param token_url: Token URL. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#token_url OidcIdentityProvider#token_url}
        :param accepts_prompt_none_forward_from_client: This is just used together with Identity Provider Authenticator or when kc_idp_hint points to this identity provider. In case that client sends a request with prompt=none and user is not yet authenticated, the error will not be directly returned to client, but the request with prompt=none will be forwarded to this identity provider. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#accepts_prompt_none_forward_from_client OidcIdentityProvider#accepts_prompt_none_forward_from_client}
        :param add_read_token_role_on_create: Enable/disable if new users can read any stored tokens. This assigns the broker.read-token role. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#add_read_token_role_on_create OidcIdentityProvider#add_read_token_role_on_create}
        :param authenticate_by_default: Enable/disable authenticate users by default. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#authenticate_by_default OidcIdentityProvider#authenticate_by_default}
        :param backchannel_supported: Does the external IDP support backchannel logout? Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#backchannel_supported OidcIdentityProvider#backchannel_supported}
        :param default_scopes: The scopes to be sent when asking for authorization. It can be a space-separated list of scopes. Defaults to 'openid'. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#default_scopes OidcIdentityProvider#default_scopes}
        :param disable_user_info: Disable usage of User Info service to obtain additional user information? Default is to use this OIDC service. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#disable_user_info OidcIdentityProvider#disable_user_info}
        :param display_name: Friendly name for Identity Providers. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#display_name OidcIdentityProvider#display_name}
        :param enabled: Enable/disable this identity provider. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#enabled OidcIdentityProvider#enabled}
        :param extra_config: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#extra_config OidcIdentityProvider#extra_config}.
        :param first_broker_login_flow_alias: Alias of authentication flow, which is triggered after first login with this identity provider. Term 'First Login' means that there is not yet existing Keycloak account linked with the authenticated identity provider account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#first_broker_login_flow_alias OidcIdentityProvider#first_broker_login_flow_alias}
        :param gui_order: GUI Order. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#gui_order OidcIdentityProvider#gui_order}
        :param hide_on_login_page: Hide On Login Page. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#hide_on_login_page OidcIdentityProvider#hide_on_login_page}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#id OidcIdentityProvider#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param issuer: The issuer identifier for the issuer of the response. If not provided, no validation will be performed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#issuer OidcIdentityProvider#issuer}
        :param jwks_url: JSON Web Key Set URL. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#jwks_url OidcIdentityProvider#jwks_url}
        :param link_only: If true, users cannot log in through this provider. They can only link to this provider. This is useful if you don't want to allow login from the provider, but want to integrate with a provider Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#link_only OidcIdentityProvider#link_only}
        :param login_hint: Login Hint. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#login_hint OidcIdentityProvider#login_hint}
        :param logout_url: Logout URL. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#logout_url OidcIdentityProvider#logout_url}
        :param post_broker_login_flow_alias: Alias of authentication flow, which is triggered after each login with this identity provider. Useful if you want additional verification of each user authenticated with this identity provider (for example OTP). Leave this empty if you don't want any additional authenticators to be triggered after login with this identity provider. Also note, that authenticator implementations must assume that user is already set in ClientSession as identity provider already set it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#post_broker_login_flow_alias OidcIdentityProvider#post_broker_login_flow_alias}
        :param provider_id: provider id, is always oidc, unless you have a custom implementation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#provider_id OidcIdentityProvider#provider_id}
        :param store_token: Enable/disable if tokens must be stored after authenticating users. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#store_token OidcIdentityProvider#store_token}
        :param sync_mode: Sync Mode. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#sync_mode OidcIdentityProvider#sync_mode}
        :param trust_email: If enabled then email provided by this provider is not verified even if verification is enabled for the realm. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#trust_email OidcIdentityProvider#trust_email}
        :param ui_locales: Pass current locale to identity provider. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#ui_locales OidcIdentityProvider#ui_locales}
        :param user_info_url: User Info URL. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#user_info_url OidcIdentityProvider#user_info_url}
        :param validate_signature: Enable/disable signature validation of external IDP signatures. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#validate_signature OidcIdentityProvider#validate_signature}
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d7d6d143c04968242d4fb7625bb3d8398478a6e44c90e9bfb62183fbd067eaca
            )
            check_type(
                argname="argument connection",
                value=connection,
                expected_type=type_hints["connection"],
            )
            check_type(
                argname="argument count", value=count, expected_type=type_hints["count"]
            )
            check_type(
                argname="argument depends_on",
                value=depends_on,
                expected_type=type_hints["depends_on"],
            )
            check_type(
                argname="argument for_each",
                value=for_each,
                expected_type=type_hints["for_each"],
            )
            check_type(
                argname="argument lifecycle",
                value=lifecycle,
                expected_type=type_hints["lifecycle"],
            )
            check_type(
                argname="argument provider",
                value=provider,
                expected_type=type_hints["provider"],
            )
            check_type(
                argname="argument provisioners",
                value=provisioners,
                expected_type=type_hints["provisioners"],
            )
            check_type(
                argname="argument alias", value=alias, expected_type=type_hints["alias"]
            )
            check_type(
                argname="argument authorization_url",
                value=authorization_url,
                expected_type=type_hints["authorization_url"],
            )
            check_type(
                argname="argument client_id",
                value=client_id,
                expected_type=type_hints["client_id"],
            )
            check_type(
                argname="argument client_secret",
                value=client_secret,
                expected_type=type_hints["client_secret"],
            )
            check_type(
                argname="argument realm", value=realm, expected_type=type_hints["realm"]
            )
            check_type(
                argname="argument token_url",
                value=token_url,
                expected_type=type_hints["token_url"],
            )
            check_type(
                argname="argument accepts_prompt_none_forward_from_client",
                value=accepts_prompt_none_forward_from_client,
                expected_type=type_hints["accepts_prompt_none_forward_from_client"],
            )
            check_type(
                argname="argument add_read_token_role_on_create",
                value=add_read_token_role_on_create,
                expected_type=type_hints["add_read_token_role_on_create"],
            )
            check_type(
                argname="argument authenticate_by_default",
                value=authenticate_by_default,
                expected_type=type_hints["authenticate_by_default"],
            )
            check_type(
                argname="argument backchannel_supported",
                value=backchannel_supported,
                expected_type=type_hints["backchannel_supported"],
            )
            check_type(
                argname="argument default_scopes",
                value=default_scopes,
                expected_type=type_hints["default_scopes"],
            )
            check_type(
                argname="argument disable_user_info",
                value=disable_user_info,
                expected_type=type_hints["disable_user_info"],
            )
            check_type(
                argname="argument display_name",
                value=display_name,
                expected_type=type_hints["display_name"],
            )
            check_type(
                argname="argument enabled",
                value=enabled,
                expected_type=type_hints["enabled"],
            )
            check_type(
                argname="argument extra_config",
                value=extra_config,
                expected_type=type_hints["extra_config"],
            )
            check_type(
                argname="argument first_broker_login_flow_alias",
                value=first_broker_login_flow_alias,
                expected_type=type_hints["first_broker_login_flow_alias"],
            )
            check_type(
                argname="argument gui_order",
                value=gui_order,
                expected_type=type_hints["gui_order"],
            )
            check_type(
                argname="argument hide_on_login_page",
                value=hide_on_login_page,
                expected_type=type_hints["hide_on_login_page"],
            )
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(
                argname="argument issuer",
                value=issuer,
                expected_type=type_hints["issuer"],
            )
            check_type(
                argname="argument jwks_url",
                value=jwks_url,
                expected_type=type_hints["jwks_url"],
            )
            check_type(
                argname="argument link_only",
                value=link_only,
                expected_type=type_hints["link_only"],
            )
            check_type(
                argname="argument login_hint",
                value=login_hint,
                expected_type=type_hints["login_hint"],
            )
            check_type(
                argname="argument logout_url",
                value=logout_url,
                expected_type=type_hints["logout_url"],
            )
            check_type(
                argname="argument post_broker_login_flow_alias",
                value=post_broker_login_flow_alias,
                expected_type=type_hints["post_broker_login_flow_alias"],
            )
            check_type(
                argname="argument provider_id",
                value=provider_id,
                expected_type=type_hints["provider_id"],
            )
            check_type(
                argname="argument store_token",
                value=store_token,
                expected_type=type_hints["store_token"],
            )
            check_type(
                argname="argument sync_mode",
                value=sync_mode,
                expected_type=type_hints["sync_mode"],
            )
            check_type(
                argname="argument trust_email",
                value=trust_email,
                expected_type=type_hints["trust_email"],
            )
            check_type(
                argname="argument ui_locales",
                value=ui_locales,
                expected_type=type_hints["ui_locales"],
            )
            check_type(
                argname="argument user_info_url",
                value=user_info_url,
                expected_type=type_hints["user_info_url"],
            )
            check_type(
                argname="argument validate_signature",
                value=validate_signature,
                expected_type=type_hints["validate_signature"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "alias": alias,
            "authorization_url": authorization_url,
            "client_id": client_id,
            "client_secret": client_secret,
            "realm": realm,
            "token_url": token_url,
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
        if accepts_prompt_none_forward_from_client is not None:
            self._values[
                "accepts_prompt_none_forward_from_client"
            ] = accepts_prompt_none_forward_from_client
        if add_read_token_role_on_create is not None:
            self._values[
                "add_read_token_role_on_create"
            ] = add_read_token_role_on_create
        if authenticate_by_default is not None:
            self._values["authenticate_by_default"] = authenticate_by_default
        if backchannel_supported is not None:
            self._values["backchannel_supported"] = backchannel_supported
        if default_scopes is not None:
            self._values["default_scopes"] = default_scopes
        if disable_user_info is not None:
            self._values["disable_user_info"] = disable_user_info
        if display_name is not None:
            self._values["display_name"] = display_name
        if enabled is not None:
            self._values["enabled"] = enabled
        if extra_config is not None:
            self._values["extra_config"] = extra_config
        if first_broker_login_flow_alias is not None:
            self._values[
                "first_broker_login_flow_alias"
            ] = first_broker_login_flow_alias
        if gui_order is not None:
            self._values["gui_order"] = gui_order
        if hide_on_login_page is not None:
            self._values["hide_on_login_page"] = hide_on_login_page
        if id is not None:
            self._values["id"] = id
        if issuer is not None:
            self._values["issuer"] = issuer
        if jwks_url is not None:
            self._values["jwks_url"] = jwks_url
        if link_only is not None:
            self._values["link_only"] = link_only
        if login_hint is not None:
            self._values["login_hint"] = login_hint
        if logout_url is not None:
            self._values["logout_url"] = logout_url
        if post_broker_login_flow_alias is not None:
            self._values["post_broker_login_flow_alias"] = post_broker_login_flow_alias
        if provider_id is not None:
            self._values["provider_id"] = provider_id
        if store_token is not None:
            self._values["store_token"] = store_token
        if sync_mode is not None:
            self._values["sync_mode"] = sync_mode
        if trust_email is not None:
            self._values["trust_email"] = trust_email
        if ui_locales is not None:
            self._values["ui_locales"] = ui_locales
        if user_info_url is not None:
            self._values["user_info_url"] = user_info_url
        if validate_signature is not None:
            self._values["validate_signature"] = validate_signature

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.SSHProvisionerConnection,
            _cdktf_9a9027ec.WinrmProvisionerConnection,
        ]
    ]:
        """
        :stability: experimental
        """
        result = self._values.get("connection")
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.SSHProvisionerConnection,
                    _cdktf_9a9027ec.WinrmProvisionerConnection,
                ]
            ],
            result,
        )

    @builtins.property
    def count(
        self,
    ) -> typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]]:
        """
        :stability: experimental
        """
        result = self._values.get("count")
        return typing.cast(
            typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]],
            result,
        )

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        """
        :stability: experimental
        """
        result = self._values.get("depends_on")
        return typing.cast(
            typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result
        )

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        """
        :stability: experimental
        """
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        """
        :stability: experimental
        """
        result = self._values.get("lifecycle")
        return typing.cast(
            typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result
        )

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        """
        :stability: experimental
        """
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[
        typing.List[
            typing.Union[
                _cdktf_9a9027ec.FileProvisioner,
                _cdktf_9a9027ec.LocalExecProvisioner,
                _cdktf_9a9027ec.RemoteExecProvisioner,
            ]
        ]
    ]:
        """
        :stability: experimental
        """
        result = self._values.get("provisioners")
        return typing.cast(
            typing.Optional[
                typing.List[
                    typing.Union[
                        _cdktf_9a9027ec.FileProvisioner,
                        _cdktf_9a9027ec.LocalExecProvisioner,
                        _cdktf_9a9027ec.RemoteExecProvisioner,
                    ]
                ]
            ],
            result,
        )

    @builtins.property
    def alias(self) -> builtins.str:
        """The alias uniquely identifies an identity provider and it is also used to build the redirect uri.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#alias OidcIdentityProvider#alias}
        """
        result = self._values.get("alias")
        assert result is not None, "Required property 'alias' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorization_url(self) -> builtins.str:
        """OIDC authorization URL.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#authorization_url OidcIdentityProvider#authorization_url}
        """
        result = self._values.get("authorization_url")
        assert result is not None, "Required property 'authorization_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_id(self) -> builtins.str:
        """Client ID.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#client_id OidcIdentityProvider#client_id}
        """
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> builtins.str:
        """Client Secret.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#client_secret OidcIdentityProvider#client_secret}
        """
        result = self._values.get("client_secret")
        assert result is not None, "Required property 'client_secret' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def realm(self) -> builtins.str:
        """Realm Name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#realm OidcIdentityProvider#realm}
        """
        result = self._values.get("realm")
        assert result is not None, "Required property 'realm' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def token_url(self) -> builtins.str:
        """Token URL.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#token_url OidcIdentityProvider#token_url}
        """
        result = self._values.get("token_url")
        assert result is not None, "Required property 'token_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def accepts_prompt_none_forward_from_client(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """This is just used together with Identity Provider Authenticator or when kc_idp_hint points to this identity provider.

        In case that client sends a request with prompt=none and user is not yet authenticated, the error will not be directly returned to client, but the request with prompt=none will be forwarded to this identity provider.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#accepts_prompt_none_forward_from_client OidcIdentityProvider#accepts_prompt_none_forward_from_client}
        """
        result = self._values.get("accepts_prompt_none_forward_from_client")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def add_read_token_role_on_create(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Enable/disable if new users can read any stored tokens. This assigns the broker.read-token role.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#add_read_token_role_on_create OidcIdentityProvider#add_read_token_role_on_create}
        """
        result = self._values.get("add_read_token_role_on_create")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def authenticate_by_default(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Enable/disable authenticate users by default.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#authenticate_by_default OidcIdentityProvider#authenticate_by_default}
        """
        result = self._values.get("authenticate_by_default")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def backchannel_supported(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Does the external IDP support backchannel logout?

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#backchannel_supported OidcIdentityProvider#backchannel_supported}
        """
        result = self._values.get("backchannel_supported")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def default_scopes(self) -> typing.Optional[builtins.str]:
        """The scopes to be sent when asking for authorization.

        It can be a space-separated list of scopes. Defaults to 'openid'.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#default_scopes OidcIdentityProvider#default_scopes}
        """
        result = self._values.get("default_scopes")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_user_info(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Disable usage of User Info service to obtain additional user information?  Default is to use this OIDC service.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#disable_user_info OidcIdentityProvider#disable_user_info}
        """
        result = self._values.get("disable_user_info")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        """Friendly name for Identity Providers.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#display_name OidcIdentityProvider#display_name}
        """
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Enable/disable this identity provider.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#enabled OidcIdentityProvider#enabled}
        """
        result = self._values.get("enabled")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def extra_config(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#extra_config OidcIdentityProvider#extra_config}."""
        result = self._values.get("extra_config")
        return typing.cast(
            typing.Optional[typing.Mapping[builtins.str, builtins.str]], result
        )

    @builtins.property
    def first_broker_login_flow_alias(self) -> typing.Optional[builtins.str]:
        """Alias of authentication flow, which is triggered after first login with this identity provider.

        Term 'First Login' means that there is not yet existing Keycloak account linked with the authenticated identity provider account.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#first_broker_login_flow_alias OidcIdentityProvider#first_broker_login_flow_alias}
        """
        result = self._values.get("first_broker_login_flow_alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gui_order(self) -> typing.Optional[builtins.str]:
        """GUI Order.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#gui_order OidcIdentityProvider#gui_order}
        """
        result = self._values.get("gui_order")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hide_on_login_page(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Hide On Login Page.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#hide_on_login_page OidcIdentityProvider#hide_on_login_page}
        """
        result = self._values.get("hide_on_login_page")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#id OidcIdentityProvider#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def issuer(self) -> typing.Optional[builtins.str]:
        """The issuer identifier for the issuer of the response. If not provided, no validation will be performed.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#issuer OidcIdentityProvider#issuer}
        """
        result = self._values.get("issuer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def jwks_url(self) -> typing.Optional[builtins.str]:
        """JSON Web Key Set URL.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#jwks_url OidcIdentityProvider#jwks_url}
        """
        result = self._values.get("jwks_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def link_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """If true, users cannot log in through this provider.

        They can only link to this provider.  This is useful if you don't want to allow login from the provider, but want to integrate with a provider

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#link_only OidcIdentityProvider#link_only}
        """
        result = self._values.get("link_only")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def login_hint(self) -> typing.Optional[builtins.str]:
        """Login Hint.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#login_hint OidcIdentityProvider#login_hint}
        """
        result = self._values.get("login_hint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logout_url(self) -> typing.Optional[builtins.str]:
        """Logout URL.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#logout_url OidcIdentityProvider#logout_url}
        """
        result = self._values.get("logout_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def post_broker_login_flow_alias(self) -> typing.Optional[builtins.str]:
        """Alias of authentication flow, which is triggered after each login with this identity provider.

        Useful if you want additional verification of each user authenticated with this identity provider (for example OTP). Leave this empty if you don't want any additional authenticators to be triggered after login with this identity provider. Also note, that authenticator implementations must assume that user is already set in ClientSession as identity provider already set it.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#post_broker_login_flow_alias OidcIdentityProvider#post_broker_login_flow_alias}
        """
        result = self._values.get("post_broker_login_flow_alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provider_id(self) -> typing.Optional[builtins.str]:
        """provider id, is always oidc, unless you have a custom implementation.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#provider_id OidcIdentityProvider#provider_id}
        """
        result = self._values.get("provider_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def store_token(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Enable/disable if tokens must be stored after authenticating users.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#store_token OidcIdentityProvider#store_token}
        """
        result = self._values.get("store_token")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def sync_mode(self) -> typing.Optional[builtins.str]:
        """Sync Mode.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#sync_mode OidcIdentityProvider#sync_mode}
        """
        result = self._values.get("sync_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def trust_email(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """If enabled then email provided by this provider is not verified even if verification is enabled for the realm.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#trust_email OidcIdentityProvider#trust_email}
        """
        result = self._values.get("trust_email")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def ui_locales(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Pass current locale to identity provider.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#ui_locales OidcIdentityProvider#ui_locales}
        """
        result = self._values.get("ui_locales")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def user_info_url(self) -> typing.Optional[builtins.str]:
        """User Info URL.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#user_info_url OidcIdentityProvider#user_info_url}
        """
        result = self._values.get("user_info_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def validate_signature(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Enable/disable signature validation of external IDP signatures.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_identity_provider#validate_signature OidcIdentityProvider#validate_signature}
        """
        result = self._values.get("validate_signature")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OidcIdentityProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "OidcIdentityProvider",
    "OidcIdentityProviderConfig",
]

publication.publish()


def _typecheckingstub__ef9a2d88a75bd9f56efea1e4e62d253c51b5e058f3885112eed887bb5e513ddd(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    alias: builtins.str,
    authorization_url: builtins.str,
    client_id: builtins.str,
    client_secret: builtins.str,
    realm: builtins.str,
    token_url: builtins.str,
    accepts_prompt_none_forward_from_client: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    add_read_token_role_on_create: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    authenticate_by_default: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    backchannel_supported: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    default_scopes: typing.Optional[builtins.str] = None,
    disable_user_info: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    display_name: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    extra_config: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    first_broker_login_flow_alias: typing.Optional[builtins.str] = None,
    gui_order: typing.Optional[builtins.str] = None,
    hide_on_login_page: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    id: typing.Optional[builtins.str] = None,
    issuer: typing.Optional[builtins.str] = None,
    jwks_url: typing.Optional[builtins.str] = None,
    link_only: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    login_hint: typing.Optional[builtins.str] = None,
    logout_url: typing.Optional[builtins.str] = None,
    post_broker_login_flow_alias: typing.Optional[builtins.str] = None,
    provider_id: typing.Optional[builtins.str] = None,
    store_token: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    sync_mode: typing.Optional[builtins.str] = None,
    trust_email: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    ui_locales: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    user_info_url: typing.Optional[builtins.str] = None,
    validate_signature: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    connection: typing.Optional[
        typing.Union[
            typing.Union[
                _cdktf_9a9027ec.SSHProvisionerConnection,
                typing.Dict[builtins.str, typing.Any],
            ],
            typing.Union[
                _cdktf_9a9027ec.WinrmProvisionerConnection,
                typing.Dict[builtins.str, typing.Any],
            ],
        ]
    ] = None,
    count: typing.Optional[
        typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]
    ] = None,
    depends_on: typing.Optional[
        typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]
    ] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.TerraformResourceLifecycle,
            typing.Dict[builtins.str, typing.Any],
        ]
    ] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[
        typing.Sequence[
            typing.Union[
                typing.Union[
                    _cdktf_9a9027ec.FileProvisioner,
                    typing.Dict[builtins.str, typing.Any],
                ],
                typing.Union[
                    _cdktf_9a9027ec.LocalExecProvisioner,
                    typing.Dict[builtins.str, typing.Any],
                ],
                typing.Union[
                    _cdktf_9a9027ec.RemoteExecProvisioner,
                    typing.Dict[builtins.str, typing.Any],
                ],
            ]
        ]
    ] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__80dd9c503815b165fdf70bb0f3e7847f4882460ab06a177f10295608d92845dc(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4ef67cd26e33229055d2c89d684d0bf6071d5aa6af5d23c05ad6cde0110f5eca(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d804b151a1cb22ff3444056ddddfeb9bb7b27a61fc5575fdc0a5118d0fef486f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e0d8240d514d6a47c1d03604c830ca082ce88c58f190f864b525b08c80307075(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__635d7a7a6650b51465f842e8401ef6523b737264c6d9fb8a26d0992da60440d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__955926e783b0c03c5c96a2bdd218b9faab62f91ab5c7f3981ba523570527b456(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e436d066e1e19a90880248f37d3e07b22398a10700efc9693c86fe98df669aed(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__58a3f4fc38b16b78d396b1fc08d6d24c63c64b652bcfe2179364e67873e5e988(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__69658fde344f6e685e352d1ba1e4111669b84b89a5de54d777b0623853602939(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b6a7516998b4bcceda799f5949c8e92294934f83c5399ba535e930dcc5df7953(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b0f92dc649646a6bdf011ae403edd02221f9477b6a2878d89029fbfef3356867(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8cc85f69e23b46953f520ff7caac672378846912737429cd4410dc10f9ed0c78(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__04674e1a21f7205bf152ba8da9998e570742cb7694c04df9fa2c693039b1be06(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__264f98d3232120e758f246aa0cc69c147a21c3d25993e5f313e2233111c22a5a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__74782c940d00a357a25e9b9fa2e8ade5673d321d88c1442dc90ea2e7db821f0e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0c0ec35d177af0b9f19b5922464ecda47e8d7bb6c70d4453106b4d6475eb0020(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3ed947e772e933e67aee9b9cebf11d0dbea858823267299acf6b9e3caaf09f37(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__5434e949bcf6c757088b9d0bb2395fed2e35486c18df4928f5831ad62d4ba085(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__78a471f3cfff54197465560ed2dd0bb04873797c9048bfcb22f21be0a0119d22(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8cffffdc57db6c7cb8665c3858ae8842317f20fa794fd9245faf051f9501ee9a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e86cc9afbd861834e6317467ce04dac4589e3ae3d748b453779d8512aade1564(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d7ee4e926c9f21412e2b671f3e1c4641d0ddc55306ea13c0f9c39bd5719c00c3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__96de58e76dbe89ae92bbeff1a957cba8fccc5d354e83ba82f591be87438e64b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__40aaffe9fde210c42f884c74193bc4bbe7a58e696c190f88419f265e76e7c255(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__69c6c04010cd9deab2e246736c371f247dcf0545f7d988787113a8e812e2a84a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b856ca7561801dd170ddaba3e2f68bdeec843c9452a960c03f82e23a9dbc42c0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6567043d182de4d600186a64a242a5dabf1109e81ef418fd170ac192c6e05c21(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ca2f036ef759bef5ee38ad56b6a785183c4f8c3fad25e5aba95b04ea802f3017(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c2ef45fc351bc560f447cfba6c74a2ca86b98f3c00962a972e4559c554a924fa(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__2375b065380cfa73e40cffb759d7cd499d0d56fd294d6dd54f516897b4402d43(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a961af4c4b0e7588de4bfdc5631a6a4012256d1f7df4769a398eae3a55b1fcdf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d6657582afcd45de05991f111d4450dac159624bfc6560c651eaa04e5a88faa8(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d7d6d143c04968242d4fb7625bb3d8398478a6e44c90e9bfb62183fbd067eaca(
    *,
    connection: typing.Optional[
        typing.Union[
            typing.Union[
                _cdktf_9a9027ec.SSHProvisionerConnection,
                typing.Dict[builtins.str, typing.Any],
            ],
            typing.Union[
                _cdktf_9a9027ec.WinrmProvisionerConnection,
                typing.Dict[builtins.str, typing.Any],
            ],
        ]
    ] = None,
    count: typing.Optional[
        typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]
    ] = None,
    depends_on: typing.Optional[
        typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]
    ] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.TerraformResourceLifecycle,
            typing.Dict[builtins.str, typing.Any],
        ]
    ] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[
        typing.Sequence[
            typing.Union[
                typing.Union[
                    _cdktf_9a9027ec.FileProvisioner,
                    typing.Dict[builtins.str, typing.Any],
                ],
                typing.Union[
                    _cdktf_9a9027ec.LocalExecProvisioner,
                    typing.Dict[builtins.str, typing.Any],
                ],
                typing.Union[
                    _cdktf_9a9027ec.RemoteExecProvisioner,
                    typing.Dict[builtins.str, typing.Any],
                ],
            ]
        ]
    ] = None,
    alias: builtins.str,
    authorization_url: builtins.str,
    client_id: builtins.str,
    client_secret: builtins.str,
    realm: builtins.str,
    token_url: builtins.str,
    accepts_prompt_none_forward_from_client: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    add_read_token_role_on_create: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    authenticate_by_default: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    backchannel_supported: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    default_scopes: typing.Optional[builtins.str] = None,
    disable_user_info: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    display_name: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    extra_config: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    first_broker_login_flow_alias: typing.Optional[builtins.str] = None,
    gui_order: typing.Optional[builtins.str] = None,
    hide_on_login_page: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    id: typing.Optional[builtins.str] = None,
    issuer: typing.Optional[builtins.str] = None,
    jwks_url: typing.Optional[builtins.str] = None,
    link_only: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    login_hint: typing.Optional[builtins.str] = None,
    logout_url: typing.Optional[builtins.str] = None,
    post_broker_login_flow_alias: typing.Optional[builtins.str] = None,
    provider_id: typing.Optional[builtins.str] = None,
    store_token: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    sync_mode: typing.Optional[builtins.str] = None,
    trust_email: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    ui_locales: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    user_info_url: typing.Optional[builtins.str] = None,
    validate_signature: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
) -> None:
    """Type checking stubs"""
    pass
