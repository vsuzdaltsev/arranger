"""
# `keycloak_oidc_google_identity_provider`

Refer to the Terraform Registory for docs: [`keycloak_oidc_google_identity_provider`](https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider).
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


class OidcGoogleIdentityProvider(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.oidcGoogleIdentityProvider.OidcGoogleIdentityProvider",
):
    """Represents a {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider keycloak_oidc_google_identity_provider}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        client_id: builtins.str,
        client_secret: builtins.str,
        realm: builtins.str,
        accepts_prompt_none_forward_from_client: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        add_read_token_role_on_create: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        authenticate_by_default: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        default_scopes: typing.Optional[builtins.str] = None,
        disable_user_info: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
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
        hosted_domain: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        link_only: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        post_broker_login_flow_alias: typing.Optional[builtins.str] = None,
        provider_id: typing.Optional[builtins.str] = None,
        request_refresh_token: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        store_token: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        sync_mode: typing.Optional[builtins.str] = None,
        trust_email: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        use_user_ip_param: typing.Optional[
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
        """Create a new {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider keycloak_oidc_google_identity_provider} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param client_id: Client ID. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#client_id OidcGoogleIdentityProvider#client_id}
        :param client_secret: Client Secret. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#client_secret OidcGoogleIdentityProvider#client_secret}
        :param realm: Realm Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#realm OidcGoogleIdentityProvider#realm}
        :param accepts_prompt_none_forward_from_client: This is just used together with Identity Provider Authenticator or when kc_idp_hint points to this identity provider. In case that client sends a request with prompt=none and user is not yet authenticated, the error will not be directly returned to client, but the request with prompt=none will be forwarded to this identity provider. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#accepts_prompt_none_forward_from_client OidcGoogleIdentityProvider#accepts_prompt_none_forward_from_client}
        :param add_read_token_role_on_create: Enable/disable if new users can read any stored tokens. This assigns the broker.read-token role. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#add_read_token_role_on_create OidcGoogleIdentityProvider#add_read_token_role_on_create}
        :param authenticate_by_default: Enable/disable authenticate users by default. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#authenticate_by_default OidcGoogleIdentityProvider#authenticate_by_default}
        :param default_scopes: The scopes to be sent when asking for authorization. See the documentation for possible values, separator and default value'. Default: 'openid profile email' Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#default_scopes OidcGoogleIdentityProvider#default_scopes}
        :param disable_user_info: Disable usage of User Info service to obtain additional user information? Default is to use this OIDC service. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#disable_user_info OidcGoogleIdentityProvider#disable_user_info}
        :param enabled: Enable/disable this identity provider. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#enabled OidcGoogleIdentityProvider#enabled}
        :param extra_config: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#extra_config OidcGoogleIdentityProvider#extra_config}.
        :param first_broker_login_flow_alias: Alias of authentication flow, which is triggered after first login with this identity provider. Term 'First Login' means that there is not yet existing Keycloak account linked with the authenticated identity provider account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#first_broker_login_flow_alias OidcGoogleIdentityProvider#first_broker_login_flow_alias}
        :param gui_order: GUI Order. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#gui_order OidcGoogleIdentityProvider#gui_order}
        :param hide_on_login_page: Hide On Login Page. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#hide_on_login_page OidcGoogleIdentityProvider#hide_on_login_page}
        :param hosted_domain: Set 'hd' query parameter when logging in with Google. Google will list accounts only for this domain. Keycloak validates that the returned identity token has a claim for this domain. When '*' is entered, any hosted account can be used. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#hosted_domain OidcGoogleIdentityProvider#hosted_domain}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#id OidcGoogleIdentityProvider#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param link_only: If true, users cannot log in through this provider. They can only link to this provider. This is useful if you don't want to allow login from the provider, but want to integrate with a provider Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#link_only OidcGoogleIdentityProvider#link_only}
        :param post_broker_login_flow_alias: Alias of authentication flow, which is triggered after each login with this identity provider. Useful if you want additional verification of each user authenticated with this identity provider (for example OTP). Leave this empty if you don't want any additional authenticators to be triggered after login with this identity provider. Also note, that authenticator implementations must assume that user is already set in ClientSession as identity provider already set it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#post_broker_login_flow_alias OidcGoogleIdentityProvider#post_broker_login_flow_alias}
        :param provider_id: provider id, is always google, unless you have a extended custom implementation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#provider_id OidcGoogleIdentityProvider#provider_id}
        :param request_refresh_token: Set 'access_type' query parameter to 'offline' when redirecting to google authorization endpoint, to get a refresh token back. Useful if planning to use Token Exchange to retrieve Google token to access Google APIs when the user is not at the browser. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#request_refresh_token OidcGoogleIdentityProvider#request_refresh_token}
        :param store_token: Enable/disable if tokens must be stored after authenticating users. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#store_token OidcGoogleIdentityProvider#store_token}
        :param sync_mode: Sync Mode. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#sync_mode OidcGoogleIdentityProvider#sync_mode}
        :param trust_email: If enabled then email provided by this provider is not verified even if verification is enabled for the realm. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#trust_email OidcGoogleIdentityProvider#trust_email}
        :param use_user_ip_param: Set 'userIp' query parameter when invoking on Google's User Info service. This will use the user's ip address. Useful if Google is throttling access to the User Info service. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#use_user_ip_param OidcGoogleIdentityProvider#use_user_ip_param}
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
                _typecheckingstub__ce4d7f469dcf037ea46560953468b96e60e36eaf0217318d2a4d98e3db96f194
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(
                argname="argument id_", value=id_, expected_type=type_hints["id_"]
            )
        config = OidcGoogleIdentityProviderConfig(
            client_id=client_id,
            client_secret=client_secret,
            realm=realm,
            accepts_prompt_none_forward_from_client=accepts_prompt_none_forward_from_client,
            add_read_token_role_on_create=add_read_token_role_on_create,
            authenticate_by_default=authenticate_by_default,
            default_scopes=default_scopes,
            disable_user_info=disable_user_info,
            enabled=enabled,
            extra_config=extra_config,
            first_broker_login_flow_alias=first_broker_login_flow_alias,
            gui_order=gui_order,
            hide_on_login_page=hide_on_login_page,
            hosted_domain=hosted_domain,
            id=id,
            link_only=link_only,
            post_broker_login_flow_alias=post_broker_login_flow_alias,
            provider_id=provider_id,
            request_refresh_token=request_refresh_token,
            store_token=store_token,
            sync_mode=sync_mode,
            trust_email=trust_email,
            use_user_ip_param=use_user_ip_param,
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

    @jsii.member(jsii_name="resetDefaultScopes")
    def reset_default_scopes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultScopes", []))

    @jsii.member(jsii_name="resetDisableUserInfo")
    def reset_disable_user_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableUserInfo", []))

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

    @jsii.member(jsii_name="resetHostedDomain")
    def reset_hosted_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostedDomain", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLinkOnly")
    def reset_link_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinkOnly", []))

    @jsii.member(jsii_name="resetPostBrokerLoginFlowAlias")
    def reset_post_broker_login_flow_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPostBrokerLoginFlowAlias", []))

    @jsii.member(jsii_name="resetProviderId")
    def reset_provider_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProviderId", []))

    @jsii.member(jsii_name="resetRequestRefreshToken")
    def reset_request_refresh_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestRefreshToken", []))

    @jsii.member(jsii_name="resetStoreToken")
    def reset_store_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStoreToken", []))

    @jsii.member(jsii_name="resetSyncMode")
    def reset_sync_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSyncMode", []))

    @jsii.member(jsii_name="resetTrustEmail")
    def reset_trust_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrustEmail", []))

    @jsii.member(jsii_name="resetUseUserIpParam")
    def reset_use_user_ip_param(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseUserIpParam", []))

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
    @jsii.member(jsii_name="alias")
    def alias(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "alias"))

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

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
    @jsii.member(jsii_name="authenticateByDefaultInput")
    def authenticate_by_default_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "authenticateByDefaultInput"),
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
    @jsii.member(jsii_name="hostedDomainInput")
    def hosted_domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "hostedDomainInput")
        )

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

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
    @jsii.member(jsii_name="requestRefreshTokenInput")
    def request_refresh_token_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "requestRefreshTokenInput"),
        )

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
    @jsii.member(jsii_name="trustEmailInput")
    def trust_email_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "trustEmailInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="useUserIpParamInput")
    def use_user_ip_param_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "useUserIpParamInput"),
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
                _typecheckingstub__69f822f3cda9b8230e6841d106c48020a22f39d0fef9a1cb1267f297478070ae
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
                _typecheckingstub__45e561612b24a2a5624261ae44573b4eea14e6677fdcc5a49edcbb772c203195
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "addReadTokenRoleOnCreate", value)

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
                _typecheckingstub__a586aebfe091335b591bc5d1d0cd674330770dc28f257aaf646175b5c6667439
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "authenticateByDefault", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__c389a6e53564cf2bbc2e1b7578baf6a7e0bdac53fe64c3a952bf65c500871da4
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
                _typecheckingstub__6b073deeddc856dcd0507fdcab7b7eb54531e7e3e7f5b4f96a2428337444c330
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
                _typecheckingstub__1ff69281d816de09e48e85584e2b848ecd82c633fc50002156385bf7a632006d
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
                _typecheckingstub__8555d4e6c9545c4cdfce539bd2d7c542ae7e984f40fb56ad8ecb87f1a76dd6a2
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "disableUserInfo", value)

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
                _typecheckingstub__d08d26a77fe5daef2652a555e67beb5670c9788d8d573ab8b5b395cf87b55ea2
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
                _typecheckingstub__bff712eb48a87f62477ad4f7ebc5f27a9eceecaec5fb8c212cdadc529874f31f
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
                _typecheckingstub__04ac717693a06f9d7bb2e8d68ff78ba6b9b0b94fcb691080bc6756909d22bbd6
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
                _typecheckingstub__1ce23c5665e22bb0dabbcd16456d4e5ac8556b0c2010c32a90dd7a0528c957c9
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
                _typecheckingstub__f51c1ec7d7e9f597b6dda2a2d3f3a29ac92bf440993a9b661238b9033f481806
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "hideOnLoginPage", value)

    @builtins.property
    @jsii.member(jsii_name="hostedDomain")
    def hosted_domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostedDomain"))

    @hosted_domain.setter
    def hosted_domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__f57952c7a61e80a05c454f6dc14ffc015ef7964a4c380dde56a8507972b88c1d
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "hostedDomain", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__90dd600444d87bfc052e8a94019e185670b56712a191386bdcee57b1f9bbfa6e
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "id", value)

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
                _typecheckingstub__59e283054eeff319b57a8b7031196f2f170cb0ff560d9437c02573f8ec7636b1
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "linkOnly", value)

    @builtins.property
    @jsii.member(jsii_name="postBrokerLoginFlowAlias")
    def post_broker_login_flow_alias(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "postBrokerLoginFlowAlias"))

    @post_broker_login_flow_alias.setter
    def post_broker_login_flow_alias(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__22cc855059efd5d519ecb34b28f69b742fbe1c082b697ad5e2d53b0eb5234737
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
                _typecheckingstub__e89cfb263685c78526e01083b7e14bf6d8b9add955073336bd05dcdea1e0f29d
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
                _typecheckingstub__15b69827a3246fa641aa70b9b8e02c7eebbfd20e8cf392e310a7d8c143383fca
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "realm", value)

    @builtins.property
    @jsii.member(jsii_name="requestRefreshToken")
    def request_refresh_token(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "requestRefreshToken"),
        )

    @request_refresh_token.setter
    def request_refresh_token(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__f6f149252342effbec4e012fd5d63a7f8b703e88d183df242e1b55beff5450e2
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "requestRefreshToken", value)

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
                _typecheckingstub__6a519d3818b01e7a0f43555e0fba91606822473dcfa9458c1197c19ff93f740c
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
                _typecheckingstub__291eb43cc4601d08d1b4bbe9aa3d342fa91d5b0604ad87e73c23300d055bfcee
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "syncMode", value)

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
                _typecheckingstub__59482059a7d323373507e3aa58ab54f14f59d04f907e1da116f3f27dce9a8e2b
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "trustEmail", value)

    @builtins.property
    @jsii.member(jsii_name="useUserIpParam")
    def use_user_ip_param(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "useUserIpParam"),
        )

    @use_user_ip_param.setter
    def use_user_ip_param(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__99734687f35a20dce27b98429931df880ab11e7940f79b6f862ca702408c5ad4
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "useUserIpParam", value)


@jsii.data_type(
    jsii_type="keycloak.oidcGoogleIdentityProvider.OidcGoogleIdentityProviderConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "realm": "realm",
        "accepts_prompt_none_forward_from_client": "acceptsPromptNoneForwardFromClient",
        "add_read_token_role_on_create": "addReadTokenRoleOnCreate",
        "authenticate_by_default": "authenticateByDefault",
        "default_scopes": "defaultScopes",
        "disable_user_info": "disableUserInfo",
        "enabled": "enabled",
        "extra_config": "extraConfig",
        "first_broker_login_flow_alias": "firstBrokerLoginFlowAlias",
        "gui_order": "guiOrder",
        "hide_on_login_page": "hideOnLoginPage",
        "hosted_domain": "hostedDomain",
        "id": "id",
        "link_only": "linkOnly",
        "post_broker_login_flow_alias": "postBrokerLoginFlowAlias",
        "provider_id": "providerId",
        "request_refresh_token": "requestRefreshToken",
        "store_token": "storeToken",
        "sync_mode": "syncMode",
        "trust_email": "trustEmail",
        "use_user_ip_param": "useUserIpParam",
    },
)
class OidcGoogleIdentityProviderConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        client_id: builtins.str,
        client_secret: builtins.str,
        realm: builtins.str,
        accepts_prompt_none_forward_from_client: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        add_read_token_role_on_create: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        authenticate_by_default: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        default_scopes: typing.Optional[builtins.str] = None,
        disable_user_info: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
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
        hosted_domain: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        link_only: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        post_broker_login_flow_alias: typing.Optional[builtins.str] = None,
        provider_id: typing.Optional[builtins.str] = None,
        request_refresh_token: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        store_token: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        sync_mode: typing.Optional[builtins.str] = None,
        trust_email: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        use_user_ip_param: typing.Optional[
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
        :param client_id: Client ID. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#client_id OidcGoogleIdentityProvider#client_id}
        :param client_secret: Client Secret. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#client_secret OidcGoogleIdentityProvider#client_secret}
        :param realm: Realm Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#realm OidcGoogleIdentityProvider#realm}
        :param accepts_prompt_none_forward_from_client: This is just used together with Identity Provider Authenticator or when kc_idp_hint points to this identity provider. In case that client sends a request with prompt=none and user is not yet authenticated, the error will not be directly returned to client, but the request with prompt=none will be forwarded to this identity provider. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#accepts_prompt_none_forward_from_client OidcGoogleIdentityProvider#accepts_prompt_none_forward_from_client}
        :param add_read_token_role_on_create: Enable/disable if new users can read any stored tokens. This assigns the broker.read-token role. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#add_read_token_role_on_create OidcGoogleIdentityProvider#add_read_token_role_on_create}
        :param authenticate_by_default: Enable/disable authenticate users by default. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#authenticate_by_default OidcGoogleIdentityProvider#authenticate_by_default}
        :param default_scopes: The scopes to be sent when asking for authorization. See the documentation for possible values, separator and default value'. Default: 'openid profile email' Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#default_scopes OidcGoogleIdentityProvider#default_scopes}
        :param disable_user_info: Disable usage of User Info service to obtain additional user information? Default is to use this OIDC service. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#disable_user_info OidcGoogleIdentityProvider#disable_user_info}
        :param enabled: Enable/disable this identity provider. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#enabled OidcGoogleIdentityProvider#enabled}
        :param extra_config: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#extra_config OidcGoogleIdentityProvider#extra_config}.
        :param first_broker_login_flow_alias: Alias of authentication flow, which is triggered after first login with this identity provider. Term 'First Login' means that there is not yet existing Keycloak account linked with the authenticated identity provider account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#first_broker_login_flow_alias OidcGoogleIdentityProvider#first_broker_login_flow_alias}
        :param gui_order: GUI Order. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#gui_order OidcGoogleIdentityProvider#gui_order}
        :param hide_on_login_page: Hide On Login Page. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#hide_on_login_page OidcGoogleIdentityProvider#hide_on_login_page}
        :param hosted_domain: Set 'hd' query parameter when logging in with Google. Google will list accounts only for this domain. Keycloak validates that the returned identity token has a claim for this domain. When '*' is entered, any hosted account can be used. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#hosted_domain OidcGoogleIdentityProvider#hosted_domain}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#id OidcGoogleIdentityProvider#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param link_only: If true, users cannot log in through this provider. They can only link to this provider. This is useful if you don't want to allow login from the provider, but want to integrate with a provider Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#link_only OidcGoogleIdentityProvider#link_only}
        :param post_broker_login_flow_alias: Alias of authentication flow, which is triggered after each login with this identity provider. Useful if you want additional verification of each user authenticated with this identity provider (for example OTP). Leave this empty if you don't want any additional authenticators to be triggered after login with this identity provider. Also note, that authenticator implementations must assume that user is already set in ClientSession as identity provider already set it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#post_broker_login_flow_alias OidcGoogleIdentityProvider#post_broker_login_flow_alias}
        :param provider_id: provider id, is always google, unless you have a extended custom implementation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#provider_id OidcGoogleIdentityProvider#provider_id}
        :param request_refresh_token: Set 'access_type' query parameter to 'offline' when redirecting to google authorization endpoint, to get a refresh token back. Useful if planning to use Token Exchange to retrieve Google token to access Google APIs when the user is not at the browser. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#request_refresh_token OidcGoogleIdentityProvider#request_refresh_token}
        :param store_token: Enable/disable if tokens must be stored after authenticating users. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#store_token OidcGoogleIdentityProvider#store_token}
        :param sync_mode: Sync Mode. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#sync_mode OidcGoogleIdentityProvider#sync_mode}
        :param trust_email: If enabled then email provided by this provider is not verified even if verification is enabled for the realm. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#trust_email OidcGoogleIdentityProvider#trust_email}
        :param use_user_ip_param: Set 'userIp' query parameter when invoking on Google's User Info service. This will use the user's ip address. Useful if Google is throttling access to the User Info service. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#use_user_ip_param OidcGoogleIdentityProvider#use_user_ip_param}
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__ab9ead23c3a36534926e41ce3584b42217b77a692511030a2ee1b7e1e56fdadb
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
            check_type(
                argname="argument hosted_domain",
                value=hosted_domain,
                expected_type=type_hints["hosted_domain"],
            )
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(
                argname="argument link_only",
                value=link_only,
                expected_type=type_hints["link_only"],
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
                argname="argument request_refresh_token",
                value=request_refresh_token,
                expected_type=type_hints["request_refresh_token"],
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
                argname="argument use_user_ip_param",
                value=use_user_ip_param,
                expected_type=type_hints["use_user_ip_param"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_id": client_id,
            "client_secret": client_secret,
            "realm": realm,
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
        if default_scopes is not None:
            self._values["default_scopes"] = default_scopes
        if disable_user_info is not None:
            self._values["disable_user_info"] = disable_user_info
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
        if hosted_domain is not None:
            self._values["hosted_domain"] = hosted_domain
        if id is not None:
            self._values["id"] = id
        if link_only is not None:
            self._values["link_only"] = link_only
        if post_broker_login_flow_alias is not None:
            self._values["post_broker_login_flow_alias"] = post_broker_login_flow_alias
        if provider_id is not None:
            self._values["provider_id"] = provider_id
        if request_refresh_token is not None:
            self._values["request_refresh_token"] = request_refresh_token
        if store_token is not None:
            self._values["store_token"] = store_token
        if sync_mode is not None:
            self._values["sync_mode"] = sync_mode
        if trust_email is not None:
            self._values["trust_email"] = trust_email
        if use_user_ip_param is not None:
            self._values["use_user_ip_param"] = use_user_ip_param

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
    def client_id(self) -> builtins.str:
        """Client ID.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#client_id OidcGoogleIdentityProvider#client_id}
        """
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> builtins.str:
        """Client Secret.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#client_secret OidcGoogleIdentityProvider#client_secret}
        """
        result = self._values.get("client_secret")
        assert result is not None, "Required property 'client_secret' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def realm(self) -> builtins.str:
        """Realm Name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#realm OidcGoogleIdentityProvider#realm}
        """
        result = self._values.get("realm")
        assert result is not None, "Required property 'realm' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def accepts_prompt_none_forward_from_client(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """This is just used together with Identity Provider Authenticator or when kc_idp_hint points to this identity provider.

        In case that client sends a request with prompt=none and user is not yet authenticated, the error will not be directly returned to client, but the request with prompt=none will be forwarded to this identity provider.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#accepts_prompt_none_forward_from_client OidcGoogleIdentityProvider#accepts_prompt_none_forward_from_client}
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#add_read_token_role_on_create OidcGoogleIdentityProvider#add_read_token_role_on_create}
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#authenticate_by_default OidcGoogleIdentityProvider#authenticate_by_default}
        """
        result = self._values.get("authenticate_by_default")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def default_scopes(self) -> typing.Optional[builtins.str]:
        """The scopes to be sent when asking for authorization.

        See the documentation for possible values, separator and default value'. Default: 'openid profile email'

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#default_scopes OidcGoogleIdentityProvider#default_scopes}
        """
        result = self._values.get("default_scopes")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_user_info(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Disable usage of User Info service to obtain additional user information?  Default is to use this OIDC service.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#disable_user_info OidcGoogleIdentityProvider#disable_user_info}
        """
        result = self._values.get("disable_user_info")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Enable/disable this identity provider.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#enabled OidcGoogleIdentityProvider#enabled}
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
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#extra_config OidcGoogleIdentityProvider#extra_config}."""
        result = self._values.get("extra_config")
        return typing.cast(
            typing.Optional[typing.Mapping[builtins.str, builtins.str]], result
        )

    @builtins.property
    def first_broker_login_flow_alias(self) -> typing.Optional[builtins.str]:
        """Alias of authentication flow, which is triggered after first login with this identity provider.

        Term 'First Login' means that there is not yet existing Keycloak account linked with the authenticated identity provider account.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#first_broker_login_flow_alias OidcGoogleIdentityProvider#first_broker_login_flow_alias}
        """
        result = self._values.get("first_broker_login_flow_alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gui_order(self) -> typing.Optional[builtins.str]:
        """GUI Order.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#gui_order OidcGoogleIdentityProvider#gui_order}
        """
        result = self._values.get("gui_order")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hide_on_login_page(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Hide On Login Page.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#hide_on_login_page OidcGoogleIdentityProvider#hide_on_login_page}
        """
        result = self._values.get("hide_on_login_page")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def hosted_domain(self) -> typing.Optional[builtins.str]:
        """Set 'hd' query parameter when logging in with Google.

        Google will list accounts only for this domain. Keycloak validates that the returned identity token has a claim for this domain. When '*' is entered, any hosted account can be used.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#hosted_domain OidcGoogleIdentityProvider#hosted_domain}
        """
        result = self._values.get("hosted_domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#id OidcGoogleIdentityProvider#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def link_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """If true, users cannot log in through this provider.

        They can only link to this provider.  This is useful if you don't want to allow login from the provider, but want to integrate with a provider

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#link_only OidcGoogleIdentityProvider#link_only}
        """
        result = self._values.get("link_only")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def post_broker_login_flow_alias(self) -> typing.Optional[builtins.str]:
        """Alias of authentication flow, which is triggered after each login with this identity provider.

        Useful if you want additional verification of each user authenticated with this identity provider (for example OTP). Leave this empty if you don't want any additional authenticators to be triggered after login with this identity provider. Also note, that authenticator implementations must assume that user is already set in ClientSession as identity provider already set it.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#post_broker_login_flow_alias OidcGoogleIdentityProvider#post_broker_login_flow_alias}
        """
        result = self._values.get("post_broker_login_flow_alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provider_id(self) -> typing.Optional[builtins.str]:
        """provider id, is always google, unless you have a extended custom implementation.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#provider_id OidcGoogleIdentityProvider#provider_id}
        """
        result = self._values.get("provider_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_refresh_token(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Set 'access_type' query parameter to 'offline' when redirecting to google authorization endpoint, to get a refresh token back.

        Useful if planning to use Token Exchange to retrieve Google token to access Google APIs when the user is not at the browser.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#request_refresh_token OidcGoogleIdentityProvider#request_refresh_token}
        """
        result = self._values.get("request_refresh_token")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def store_token(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Enable/disable if tokens must be stored after authenticating users.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#store_token OidcGoogleIdentityProvider#store_token}
        """
        result = self._values.get("store_token")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def sync_mode(self) -> typing.Optional[builtins.str]:
        """Sync Mode.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#sync_mode OidcGoogleIdentityProvider#sync_mode}
        """
        result = self._values.get("sync_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def trust_email(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """If enabled then email provided by this provider is not verified even if verification is enabled for the realm.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#trust_email OidcGoogleIdentityProvider#trust_email}
        """
        result = self._values.get("trust_email")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def use_user_ip_param(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Set 'userIp' query parameter when invoking on Google's User Info service.

        This will use the user's ip address.  Useful if Google is throttling access to the User Info service.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/oidc_google_identity_provider#use_user_ip_param OidcGoogleIdentityProvider#use_user_ip_param}
        """
        result = self._values.get("use_user_ip_param")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OidcGoogleIdentityProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "OidcGoogleIdentityProvider",
    "OidcGoogleIdentityProviderConfig",
]

publication.publish()


def _typecheckingstub__ce4d7f469dcf037ea46560953468b96e60e36eaf0217318d2a4d98e3db96f194(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    client_id: builtins.str,
    client_secret: builtins.str,
    realm: builtins.str,
    accepts_prompt_none_forward_from_client: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    add_read_token_role_on_create: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    authenticate_by_default: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    default_scopes: typing.Optional[builtins.str] = None,
    disable_user_info: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    enabled: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    extra_config: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    first_broker_login_flow_alias: typing.Optional[builtins.str] = None,
    gui_order: typing.Optional[builtins.str] = None,
    hide_on_login_page: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    hosted_domain: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    link_only: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    post_broker_login_flow_alias: typing.Optional[builtins.str] = None,
    provider_id: typing.Optional[builtins.str] = None,
    request_refresh_token: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    store_token: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    sync_mode: typing.Optional[builtins.str] = None,
    trust_email: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    use_user_ip_param: typing.Optional[
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


def _typecheckingstub__69f822f3cda9b8230e6841d106c48020a22f39d0fef9a1cb1267f297478070ae(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__45e561612b24a2a5624261ae44573b4eea14e6677fdcc5a49edcbb772c203195(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a586aebfe091335b591bc5d1d0cd674330770dc28f257aaf646175b5c6667439(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c389a6e53564cf2bbc2e1b7578baf6a7e0bdac53fe64c3a952bf65c500871da4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6b073deeddc856dcd0507fdcab7b7eb54531e7e3e7f5b4f96a2428337444c330(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1ff69281d816de09e48e85584e2b848ecd82c633fc50002156385bf7a632006d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8555d4e6c9545c4cdfce539bd2d7c542ae7e984f40fb56ad8ecb87f1a76dd6a2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d08d26a77fe5daef2652a555e67beb5670c9788d8d573ab8b5b395cf87b55ea2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__bff712eb48a87f62477ad4f7ebc5f27a9eceecaec5fb8c212cdadc529874f31f(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__04ac717693a06f9d7bb2e8d68ff78ba6b9b0b94fcb691080bc6756909d22bbd6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1ce23c5665e22bb0dabbcd16456d4e5ac8556b0c2010c32a90dd7a0528c957c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f51c1ec7d7e9f597b6dda2a2d3f3a29ac92bf440993a9b661238b9033f481806(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f57952c7a61e80a05c454f6dc14ffc015ef7964a4c380dde56a8507972b88c1d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__90dd600444d87bfc052e8a94019e185670b56712a191386bdcee57b1f9bbfa6e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__59e283054eeff319b57a8b7031196f2f170cb0ff560d9437c02573f8ec7636b1(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__22cc855059efd5d519ecb34b28f69b742fbe1c082b697ad5e2d53b0eb5234737(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e89cfb263685c78526e01083b7e14bf6d8b9add955073336bd05dcdea1e0f29d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__15b69827a3246fa641aa70b9b8e02c7eebbfd20e8cf392e310a7d8c143383fca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f6f149252342effbec4e012fd5d63a7f8b703e88d183df242e1b55beff5450e2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6a519d3818b01e7a0f43555e0fba91606822473dcfa9458c1197c19ff93f740c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__291eb43cc4601d08d1b4bbe9aa3d342fa91d5b0604ad87e73c23300d055bfcee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__59482059a7d323373507e3aa58ab54f14f59d04f907e1da116f3f27dce9a8e2b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__99734687f35a20dce27b98429931df880ab11e7940f79b6f862ca702408c5ad4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ab9ead23c3a36534926e41ce3584b42217b77a692511030a2ee1b7e1e56fdadb(
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
    client_id: builtins.str,
    client_secret: builtins.str,
    realm: builtins.str,
    accepts_prompt_none_forward_from_client: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    add_read_token_role_on_create: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    authenticate_by_default: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    default_scopes: typing.Optional[builtins.str] = None,
    disable_user_info: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    enabled: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    extra_config: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    first_broker_login_flow_alias: typing.Optional[builtins.str] = None,
    gui_order: typing.Optional[builtins.str] = None,
    hide_on_login_page: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    hosted_domain: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    link_only: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    post_broker_login_flow_alias: typing.Optional[builtins.str] = None,
    provider_id: typing.Optional[builtins.str] = None,
    request_refresh_token: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    store_token: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    sync_mode: typing.Optional[builtins.str] = None,
    trust_email: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    use_user_ip_param: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
) -> None:
    """Type checking stubs"""
    pass
