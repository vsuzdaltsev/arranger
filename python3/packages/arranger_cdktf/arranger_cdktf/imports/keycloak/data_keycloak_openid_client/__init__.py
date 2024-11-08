"""
# `data_keycloak_openid_client`

Refer to the Terraform Registory for docs: [`data_keycloak_openid_client`](https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/openid_client).
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


class DataKeycloakOpenidClient(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.dataKeycloakOpenidClient.DataKeycloakOpenidClient",
):
    """Represents a {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/openid_client keycloak_openid_client}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        client_id: builtins.str,
        realm_id: builtins.str,
        consent_screen_text: typing.Optional[builtins.str] = None,
        display_on_consent_screen: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        extra_config: typing.Optional[
            typing.Mapping[builtins.str, builtins.str]
        ] = None,
        id: typing.Optional[builtins.str] = None,
        oauth2_device_authorization_grant_enabled: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        oauth2_device_code_lifespan: typing.Optional[builtins.str] = None,
        oauth2_device_polling_interval: typing.Optional[builtins.str] = None,
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
        """Create a new {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/openid_client keycloak_openid_client} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param client_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/openid_client#client_id DataKeycloakOpenidClient#client_id}.
        :param realm_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/openid_client#realm_id DataKeycloakOpenidClient#realm_id}.
        :param consent_screen_text: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/openid_client#consent_screen_text DataKeycloakOpenidClient#consent_screen_text}.
        :param display_on_consent_screen: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/openid_client#display_on_consent_screen DataKeycloakOpenidClient#display_on_consent_screen}.
        :param extra_config: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/openid_client#extra_config DataKeycloakOpenidClient#extra_config}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/openid_client#id DataKeycloakOpenidClient#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param oauth2_device_authorization_grant_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/openid_client#oauth2_device_authorization_grant_enabled DataKeycloakOpenidClient#oauth2_device_authorization_grant_enabled}.
        :param oauth2_device_code_lifespan: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/openid_client#oauth2_device_code_lifespan DataKeycloakOpenidClient#oauth2_device_code_lifespan}.
        :param oauth2_device_polling_interval: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/openid_client#oauth2_device_polling_interval DataKeycloakOpenidClient#oauth2_device_polling_interval}.
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
                _typecheckingstub__af2588c0b391cbb7c6fbace5b757052495512838630958d94757bde679fbc783
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(
                argname="argument id_", value=id_, expected_type=type_hints["id_"]
            )
        config = DataKeycloakOpenidClientConfig(
            client_id=client_id,
            realm_id=realm_id,
            consent_screen_text=consent_screen_text,
            display_on_consent_screen=display_on_consent_screen,
            extra_config=extra_config,
            id=id,
            oauth2_device_authorization_grant_enabled=oauth2_device_authorization_grant_enabled,
            oauth2_device_code_lifespan=oauth2_device_code_lifespan,
            oauth2_device_polling_interval=oauth2_device_polling_interval,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetConsentScreenText")
    def reset_consent_screen_text(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConsentScreenText", []))

    @jsii.member(jsii_name="resetDisplayOnConsentScreen")
    def reset_display_on_consent_screen(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayOnConsentScreen", []))

    @jsii.member(jsii_name="resetExtraConfig")
    def reset_extra_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtraConfig", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOauth2DeviceAuthorizationGrantEnabled")
    def reset_oauth2_device_authorization_grant_enabled(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetOauth2DeviceAuthorizationGrantEnabled", [])
        )

    @jsii.member(jsii_name="resetOauth2DeviceCodeLifespan")
    def reset_oauth2_device_code_lifespan(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauth2DeviceCodeLifespan", []))

    @jsii.member(jsii_name="resetOauth2DevicePollingInterval")
    def reset_oauth2_device_polling_interval(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetOauth2DevicePollingInterval", [])
        )

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
    @jsii.member(jsii_name="accessTokenLifespan")
    def access_token_lifespan(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessTokenLifespan"))

    @builtins.property
    @jsii.member(jsii_name="accessType")
    def access_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessType"))

    @builtins.property
    @jsii.member(jsii_name="adminUrl")
    def admin_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adminUrl"))

    @builtins.property
    @jsii.member(jsii_name="authenticationFlowBindingOverrides")
    def authentication_flow_binding_overrides(
        self,
    ) -> "DataKeycloakOpenidClientAuthenticationFlowBindingOverridesList":
        return typing.cast(
            "DataKeycloakOpenidClientAuthenticationFlowBindingOverridesList",
            jsii.get(self, "authenticationFlowBindingOverrides"),
        )

    @builtins.property
    @jsii.member(jsii_name="authorization")
    def authorization(self) -> "DataKeycloakOpenidClientAuthorizationList":
        return typing.cast(
            "DataKeycloakOpenidClientAuthorizationList", jsii.get(self, "authorization")
        )

    @builtins.property
    @jsii.member(jsii_name="backchannelLogoutRevokeOfflineSessions")
    def backchannel_logout_revoke_offline_sessions(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(
            _cdktf_9a9027ec.IResolvable,
            jsii.get(self, "backchannelLogoutRevokeOfflineSessions"),
        )

    @builtins.property
    @jsii.member(jsii_name="backchannelLogoutSessionRequired")
    def backchannel_logout_session_required(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(
            _cdktf_9a9027ec.IResolvable,
            jsii.get(self, "backchannelLogoutSessionRequired"),
        )

    @builtins.property
    @jsii.member(jsii_name="backchannelLogoutUrl")
    def backchannel_logout_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backchannelLogoutUrl"))

    @builtins.property
    @jsii.member(jsii_name="baseUrl")
    def base_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "baseUrl"))

    @builtins.property
    @jsii.member(jsii_name="clientAuthenticatorType")
    def client_authenticator_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientAuthenticatorType"))

    @builtins.property
    @jsii.member(jsii_name="clientOfflineSessionIdleTimeout")
    def client_offline_session_idle_timeout(self) -> builtins.str:
        return typing.cast(
            builtins.str, jsii.get(self, "clientOfflineSessionIdleTimeout")
        )

    @builtins.property
    @jsii.member(jsii_name="clientOfflineSessionMaxLifespan")
    def client_offline_session_max_lifespan(self) -> builtins.str:
        return typing.cast(
            builtins.str, jsii.get(self, "clientOfflineSessionMaxLifespan")
        )

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @builtins.property
    @jsii.member(jsii_name="clientSessionIdleTimeout")
    def client_session_idle_timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSessionIdleTimeout"))

    @builtins.property
    @jsii.member(jsii_name="clientSessionMaxLifespan")
    def client_session_max_lifespan(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSessionMaxLifespan"))

    @builtins.property
    @jsii.member(jsii_name="consentRequired")
    def consent_required(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(
            _cdktf_9a9027ec.IResolvable, jsii.get(self, "consentRequired")
        )

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="directAccessGrantsEnabled")
    def direct_access_grants_enabled(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(
            _cdktf_9a9027ec.IResolvable, jsii.get(self, "directAccessGrantsEnabled")
        )

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "enabled"))

    @builtins.property
    @jsii.member(jsii_name="excludeSessionStateFromAuthResponse")
    def exclude_session_state_from_auth_response(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(
            _cdktf_9a9027ec.IResolvable,
            jsii.get(self, "excludeSessionStateFromAuthResponse"),
        )

    @builtins.property
    @jsii.member(jsii_name="frontchannelLogoutEnabled")
    def frontchannel_logout_enabled(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(
            _cdktf_9a9027ec.IResolvable, jsii.get(self, "frontchannelLogoutEnabled")
        )

    @builtins.property
    @jsii.member(jsii_name="frontchannelLogoutUrl")
    def frontchannel_logout_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "frontchannelLogoutUrl"))

    @builtins.property
    @jsii.member(jsii_name="fullScopeAllowed")
    def full_scope_allowed(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(
            _cdktf_9a9027ec.IResolvable, jsii.get(self, "fullScopeAllowed")
        )

    @builtins.property
    @jsii.member(jsii_name="implicitFlowEnabled")
    def implicit_flow_enabled(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(
            _cdktf_9a9027ec.IResolvable, jsii.get(self, "implicitFlowEnabled")
        )

    @builtins.property
    @jsii.member(jsii_name="loginTheme")
    def login_theme(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loginTheme"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="pkceCodeChallengeMethod")
    def pkce_code_challenge_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pkceCodeChallengeMethod"))

    @builtins.property
    @jsii.member(jsii_name="resourceServerId")
    def resource_server_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceServerId"))

    @builtins.property
    @jsii.member(jsii_name="rootUrl")
    def root_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rootUrl"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccountsEnabled")
    def service_accounts_enabled(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(
            _cdktf_9a9027ec.IResolvable, jsii.get(self, "serviceAccountsEnabled")
        )

    @builtins.property
    @jsii.member(jsii_name="serviceAccountUserId")
    def service_account_user_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccountUserId"))

    @builtins.property
    @jsii.member(jsii_name="standardFlowEnabled")
    def standard_flow_enabled(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(
            _cdktf_9a9027ec.IResolvable, jsii.get(self, "standardFlowEnabled")
        )

    @builtins.property
    @jsii.member(jsii_name="useRefreshTokens")
    def use_refresh_tokens(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(
            _cdktf_9a9027ec.IResolvable, jsii.get(self, "useRefreshTokens")
        )

    @builtins.property
    @jsii.member(jsii_name="useRefreshTokensClientCredentials")
    def use_refresh_tokens_client_credentials(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(
            _cdktf_9a9027ec.IResolvable,
            jsii.get(self, "useRefreshTokensClientCredentials"),
        )

    @builtins.property
    @jsii.member(jsii_name="validPostLogoutRedirectUris")
    def valid_post_logout_redirect_uris(self) -> typing.List[builtins.str]:
        return typing.cast(
            typing.List[builtins.str], jsii.get(self, "validPostLogoutRedirectUris")
        )

    @builtins.property
    @jsii.member(jsii_name="validRedirectUris")
    def valid_redirect_uris(self) -> typing.List[builtins.str]:
        return typing.cast(
            typing.List[builtins.str], jsii.get(self, "validRedirectUris")
        )

    @builtins.property
    @jsii.member(jsii_name="webOrigins")
    def web_origins(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "webOrigins"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "clientIdInput")
        )

    @builtins.property
    @jsii.member(jsii_name="consentScreenTextInput")
    def consent_screen_text_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "consentScreenTextInput")
        )

    @builtins.property
    @jsii.member(jsii_name="displayOnConsentScreenInput")
    def display_on_consent_screen_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "displayOnConsentScreenInput"),
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
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="oauth2DeviceAuthorizationGrantEnabledInput")
    def oauth2_device_authorization_grant_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "oauth2DeviceAuthorizationGrantEnabledInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="oauth2DeviceCodeLifespanInput")
    def oauth2_device_code_lifespan_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "oauth2DeviceCodeLifespanInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="oauth2DevicePollingIntervalInput")
    def oauth2_device_polling_interval_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "oauth2DevicePollingIntervalInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="realmIdInput")
    def realm_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "realmIdInput")
        )

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__3ba6dbae7eb3d4268da575fbc62495c7a63a79b5c97eabe11fd8822215275c83
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="consentScreenText")
    def consent_screen_text(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consentScreenText"))

    @consent_screen_text.setter
    def consent_screen_text(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__28ce1f3ec34a2963200bd4b6984ca45fc0313687426bedef0cc16b1f902880e4
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "consentScreenText", value)

    @builtins.property
    @jsii.member(jsii_name="displayOnConsentScreen")
    def display_on_consent_screen(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "displayOnConsentScreen"),
        )

    @display_on_consent_screen.setter
    def display_on_consent_screen(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__08bf0dccc736c6d2932220627584372299955e875c7ce192827d90def2de5d58
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "displayOnConsentScreen", value)

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
                _typecheckingstub__dbd0ef4733dd17f289bc4c93e171c3a147f932fe6af669d1bf6547b102d7dfe5
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "extraConfig", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__8b59c99dd02fab0d23bb0424e3690bdd186875e85e34d023600ec74a08b18116
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="oauth2DeviceAuthorizationGrantEnabled")
    def oauth2_device_authorization_grant_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "oauth2DeviceAuthorizationGrantEnabled"),
        )

    @oauth2_device_authorization_grant_enabled.setter
    def oauth2_device_authorization_grant_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__2999204914cace111f96bd8927887bb65517f6eeff5801043821c6a3c1f5b010
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "oauth2DeviceAuthorizationGrantEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="oauth2DeviceCodeLifespan")
    def oauth2_device_code_lifespan(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oauth2DeviceCodeLifespan"))

    @oauth2_device_code_lifespan.setter
    def oauth2_device_code_lifespan(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__594f1aa60347e70f704f6ee8d0bae7f908ea9bb2634ad0beacab219ed0f03b9e
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "oauth2DeviceCodeLifespan", value)

    @builtins.property
    @jsii.member(jsii_name="oauth2DevicePollingInterval")
    def oauth2_device_polling_interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oauth2DevicePollingInterval"))

    @oauth2_device_polling_interval.setter
    def oauth2_device_polling_interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__af50920f66f699f92cd81cb5bde74dab051f17d0e5bdc1b9679df62740569560
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "oauth2DevicePollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="realmId")
    def realm_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "realmId"))

    @realm_id.setter
    def realm_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a944bfe1cc28bb422a08ef3166b544aaf8889787c5b59d6b7a1b72f73c8a5d2c
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "realmId", value)


@jsii.data_type(
    jsii_type="keycloak.dataKeycloakOpenidClient.DataKeycloakOpenidClientAuthenticationFlowBindingOverrides",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataKeycloakOpenidClientAuthenticationFlowBindingOverrides:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return (
            "DataKeycloakOpenidClientAuthenticationFlowBindingOverrides(%s)"
            % ", ".join(k + "=" + repr(v) for k, v in self._values.items())
        )


class DataKeycloakOpenidClientAuthenticationFlowBindingOverridesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.dataKeycloakOpenidClient.DataKeycloakOpenidClientAuthenticationFlowBindingOverridesList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__4c843dcd48792cce8a49241d459ebc7a0d3751c1d33c683518f6dcbb56478ae8
            )
            check_type(
                argname="argument terraform_resource",
                value=terraform_resource,
                expected_type=type_hints["terraform_resource"],
            )
            check_type(
                argname="argument terraform_attribute",
                value=terraform_attribute,
                expected_type=type_hints["terraform_attribute"],
            )
            check_type(
                argname="argument wraps_set",
                value=wraps_set,
                expected_type=type_hints["wraps_set"],
            )
        jsii.create(
            self.__class__, self, [terraform_resource, terraform_attribute, wraps_set]
        )

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataKeycloakOpenidClientAuthenticationFlowBindingOverridesOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__0894d7f48bc19b89203f60305de7d0fd3effc58b5b44b3cdf868442003cc432b
            )
            check_type(
                argname="argument index", value=index, expected_type=type_hints["index"]
            )
        return typing.cast(
            "DataKeycloakOpenidClientAuthenticationFlowBindingOverridesOutputReference",
            jsii.invoke(self, "get", [index]),
        )

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        """The attribute on the parent resource this class is referencing."""
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b18c07be46d66037dc418cc48b8fe6db4e664f1efddbbce5cc1a7f9c1a9ce914
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        """The parent resource."""
        return typing.cast(
            _cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource")
        )

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__712e6db1ac7795a466dd9e9eb3e968278e8a2a0814f06e66b7267c436fead43d
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        """whether the list is wrapping a set (will add tolist() to be able to access an item via an index)."""
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b3012dc6f99cc0d03d777a6c288c8aa56e0d931a6ddff13d96cf023456cfa369
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "wrapsSet", value)


class DataKeycloakOpenidClientAuthenticationFlowBindingOverridesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.dataKeycloakOpenidClient.DataKeycloakOpenidClientAuthenticationFlowBindingOverridesOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__801063e9c6e501405d6d0f0bb9b60742a1fa0b0392c9bba3f5200ee2a4fc5652
            )
            check_type(
                argname="argument terraform_resource",
                value=terraform_resource,
                expected_type=type_hints["terraform_resource"],
            )
            check_type(
                argname="argument terraform_attribute",
                value=terraform_attribute,
                expected_type=type_hints["terraform_attribute"],
            )
            check_type(
                argname="argument complex_object_index",
                value=complex_object_index,
                expected_type=type_hints["complex_object_index"],
            )
            check_type(
                argname="argument complex_object_is_from_set",
                value=complex_object_is_from_set,
                expected_type=type_hints["complex_object_is_from_set"],
            )
        jsii.create(
            self.__class__,
            self,
            [
                terraform_resource,
                terraform_attribute,
                complex_object_index,
                complex_object_is_from_set,
            ],
        )

    @builtins.property
    @jsii.member(jsii_name="browserId")
    def browser_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "browserId"))

    @builtins.property
    @jsii.member(jsii_name="directGrantId")
    def direct_grant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directGrantId"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataKeycloakOpenidClientAuthenticationFlowBindingOverrides]:
        return typing.cast(
            typing.Optional[DataKeycloakOpenidClientAuthenticationFlowBindingOverrides],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            DataKeycloakOpenidClientAuthenticationFlowBindingOverrides
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d5a5ccdeac7a39df07e1728b46ab331a55d8cbdc348a7a3b97371d5191aa2542
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="keycloak.dataKeycloakOpenidClient.DataKeycloakOpenidClientAuthorization",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataKeycloakOpenidClientAuthorization:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKeycloakOpenidClientAuthorization(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKeycloakOpenidClientAuthorizationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.dataKeycloakOpenidClient.DataKeycloakOpenidClientAuthorizationList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__cade826ae03b93f548fd44b20c85f1ec227485a48e410f9bff9d9b514622f27f
            )
            check_type(
                argname="argument terraform_resource",
                value=terraform_resource,
                expected_type=type_hints["terraform_resource"],
            )
            check_type(
                argname="argument terraform_attribute",
                value=terraform_attribute,
                expected_type=type_hints["terraform_attribute"],
            )
            check_type(
                argname="argument wraps_set",
                value=wraps_set,
                expected_type=type_hints["wraps_set"],
            )
        jsii.create(
            self.__class__, self, [terraform_resource, terraform_attribute, wraps_set]
        )

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataKeycloakOpenidClientAuthorizationOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__7ce85cc527e7f3f6c967719fcc7ea03ccc20d66c88437ba1ac2beb8d2a8eba56
            )
            check_type(
                argname="argument index", value=index, expected_type=type_hints["index"]
            )
        return typing.cast(
            "DataKeycloakOpenidClientAuthorizationOutputReference",
            jsii.invoke(self, "get", [index]),
        )

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        """The attribute on the parent resource this class is referencing."""
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__39be7985e4a26fee443866e2eb9fe24c25861097a3618d5c7524bacd56b276ab
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        """The parent resource."""
        return typing.cast(
            _cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource")
        )

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__dd512ae36239a83e0b7e621cc9271fcc65e535d7b583228d67311e6458548629
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        """whether the list is wrapping a set (will add tolist() to be able to access an item via an index)."""
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__55e472169f91ab36e42f33db2c6a673027418ceeb81c72764bcd486c7da35ced
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "wrapsSet", value)


class DataKeycloakOpenidClientAuthorizationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.dataKeycloakOpenidClient.DataKeycloakOpenidClientAuthorizationOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__2994fd0684700f18cf7e4132bf8cd0772c0ec1ea73e2cc12d2bf05d907863836
            )
            check_type(
                argname="argument terraform_resource",
                value=terraform_resource,
                expected_type=type_hints["terraform_resource"],
            )
            check_type(
                argname="argument terraform_attribute",
                value=terraform_attribute,
                expected_type=type_hints["terraform_attribute"],
            )
            check_type(
                argname="argument complex_object_index",
                value=complex_object_index,
                expected_type=type_hints["complex_object_index"],
            )
            check_type(
                argname="argument complex_object_is_from_set",
                value=complex_object_is_from_set,
                expected_type=type_hints["complex_object_is_from_set"],
            )
        jsii.create(
            self.__class__,
            self,
            [
                terraform_resource,
                terraform_attribute,
                complex_object_index,
                complex_object_is_from_set,
            ],
        )

    @builtins.property
    @jsii.member(jsii_name="allowRemoteResourceManagement")
    def allow_remote_resource_management(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(
            _cdktf_9a9027ec.IResolvable, jsii.get(self, "allowRemoteResourceManagement")
        )

    @builtins.property
    @jsii.member(jsii_name="decisionStrategy")
    def decision_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "decisionStrategy"))

    @builtins.property
    @jsii.member(jsii_name="keepDefaults")
    def keep_defaults(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "keepDefaults"))

    @builtins.property
    @jsii.member(jsii_name="policyEnforcementMode")
    def policy_enforcement_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policyEnforcementMode"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataKeycloakOpenidClientAuthorization]:
        return typing.cast(
            typing.Optional[DataKeycloakOpenidClientAuthorization],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKeycloakOpenidClientAuthorization],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d810dd708052ac7f9b2bb37edf8f3ec20e8f105291d87bbd9643d8e9215bad4a
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="keycloak.dataKeycloakOpenidClient.DataKeycloakOpenidClientConfig",
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
        "realm_id": "realmId",
        "consent_screen_text": "consentScreenText",
        "display_on_consent_screen": "displayOnConsentScreen",
        "extra_config": "extraConfig",
        "id": "id",
        "oauth2_device_authorization_grant_enabled": "oauth2DeviceAuthorizationGrantEnabled",
        "oauth2_device_code_lifespan": "oauth2DeviceCodeLifespan",
        "oauth2_device_polling_interval": "oauth2DevicePollingInterval",
    },
)
class DataKeycloakOpenidClientConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        realm_id: builtins.str,
        consent_screen_text: typing.Optional[builtins.str] = None,
        display_on_consent_screen: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        extra_config: typing.Optional[
            typing.Mapping[builtins.str, builtins.str]
        ] = None,
        id: typing.Optional[builtins.str] = None,
        oauth2_device_authorization_grant_enabled: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        oauth2_device_code_lifespan: typing.Optional[builtins.str] = None,
        oauth2_device_polling_interval: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param connection:
        :param count:
        :param depends_on:
        :param for_each:
        :param lifecycle:
        :param provider:
        :param provisioners:
        :param client_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/openid_client#client_id DataKeycloakOpenidClient#client_id}.
        :param realm_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/openid_client#realm_id DataKeycloakOpenidClient#realm_id}.
        :param consent_screen_text: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/openid_client#consent_screen_text DataKeycloakOpenidClient#consent_screen_text}.
        :param display_on_consent_screen: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/openid_client#display_on_consent_screen DataKeycloakOpenidClient#display_on_consent_screen}.
        :param extra_config: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/openid_client#extra_config DataKeycloakOpenidClient#extra_config}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/openid_client#id DataKeycloakOpenidClient#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param oauth2_device_authorization_grant_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/openid_client#oauth2_device_authorization_grant_enabled DataKeycloakOpenidClient#oauth2_device_authorization_grant_enabled}.
        :param oauth2_device_code_lifespan: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/openid_client#oauth2_device_code_lifespan DataKeycloakOpenidClient#oauth2_device_code_lifespan}.
        :param oauth2_device_polling_interval: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/openid_client#oauth2_device_polling_interval DataKeycloakOpenidClient#oauth2_device_polling_interval}.
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__70e68bdf31ec7f57121522330ff46583df6ed0e0f38931619d68566d3c58d689
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
                argname="argument realm_id",
                value=realm_id,
                expected_type=type_hints["realm_id"],
            )
            check_type(
                argname="argument consent_screen_text",
                value=consent_screen_text,
                expected_type=type_hints["consent_screen_text"],
            )
            check_type(
                argname="argument display_on_consent_screen",
                value=display_on_consent_screen,
                expected_type=type_hints["display_on_consent_screen"],
            )
            check_type(
                argname="argument extra_config",
                value=extra_config,
                expected_type=type_hints["extra_config"],
            )
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(
                argname="argument oauth2_device_authorization_grant_enabled",
                value=oauth2_device_authorization_grant_enabled,
                expected_type=type_hints["oauth2_device_authorization_grant_enabled"],
            )
            check_type(
                argname="argument oauth2_device_code_lifespan",
                value=oauth2_device_code_lifespan,
                expected_type=type_hints["oauth2_device_code_lifespan"],
            )
            check_type(
                argname="argument oauth2_device_polling_interval",
                value=oauth2_device_polling_interval,
                expected_type=type_hints["oauth2_device_polling_interval"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_id": client_id,
            "realm_id": realm_id,
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
        if consent_screen_text is not None:
            self._values["consent_screen_text"] = consent_screen_text
        if display_on_consent_screen is not None:
            self._values["display_on_consent_screen"] = display_on_consent_screen
        if extra_config is not None:
            self._values["extra_config"] = extra_config
        if id is not None:
            self._values["id"] = id
        if oauth2_device_authorization_grant_enabled is not None:
            self._values[
                "oauth2_device_authorization_grant_enabled"
            ] = oauth2_device_authorization_grant_enabled
        if oauth2_device_code_lifespan is not None:
            self._values["oauth2_device_code_lifespan"] = oauth2_device_code_lifespan
        if oauth2_device_polling_interval is not None:
            self._values[
                "oauth2_device_polling_interval"
            ] = oauth2_device_polling_interval

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
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/openid_client#client_id DataKeycloakOpenidClient#client_id}."""
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def realm_id(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/openid_client#realm_id DataKeycloakOpenidClient#realm_id}."""
        result = self._values.get("realm_id")
        assert result is not None, "Required property 'realm_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def consent_screen_text(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/openid_client#consent_screen_text DataKeycloakOpenidClient#consent_screen_text}."""
        result = self._values.get("consent_screen_text")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_on_consent_screen(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/openid_client#display_on_consent_screen DataKeycloakOpenidClient#display_on_consent_screen}."""
        result = self._values.get("display_on_consent_screen")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def extra_config(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/openid_client#extra_config DataKeycloakOpenidClient#extra_config}."""
        result = self._values.get("extra_config")
        return typing.cast(
            typing.Optional[typing.Mapping[builtins.str, builtins.str]], result
        )

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/openid_client#id DataKeycloakOpenidClient#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth2_device_authorization_grant_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/openid_client#oauth2_device_authorization_grant_enabled DataKeycloakOpenidClient#oauth2_device_authorization_grant_enabled}."""
        result = self._values.get("oauth2_device_authorization_grant_enabled")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def oauth2_device_code_lifespan(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/openid_client#oauth2_device_code_lifespan DataKeycloakOpenidClient#oauth2_device_code_lifespan}."""
        result = self._values.get("oauth2_device_code_lifespan")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth2_device_polling_interval(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/openid_client#oauth2_device_polling_interval DataKeycloakOpenidClient#oauth2_device_polling_interval}."""
        result = self._values.get("oauth2_device_polling_interval")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKeycloakOpenidClientConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DataKeycloakOpenidClient",
    "DataKeycloakOpenidClientAuthenticationFlowBindingOverrides",
    "DataKeycloakOpenidClientAuthenticationFlowBindingOverridesList",
    "DataKeycloakOpenidClientAuthenticationFlowBindingOverridesOutputReference",
    "DataKeycloakOpenidClientAuthorization",
    "DataKeycloakOpenidClientAuthorizationList",
    "DataKeycloakOpenidClientAuthorizationOutputReference",
    "DataKeycloakOpenidClientConfig",
]

publication.publish()


def _typecheckingstub__af2588c0b391cbb7c6fbace5b757052495512838630958d94757bde679fbc783(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    client_id: builtins.str,
    realm_id: builtins.str,
    consent_screen_text: typing.Optional[builtins.str] = None,
    display_on_consent_screen: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    extra_config: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    id: typing.Optional[builtins.str] = None,
    oauth2_device_authorization_grant_enabled: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    oauth2_device_code_lifespan: typing.Optional[builtins.str] = None,
    oauth2_device_polling_interval: typing.Optional[builtins.str] = None,
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


def _typecheckingstub__3ba6dbae7eb3d4268da575fbc62495c7a63a79b5c97eabe11fd8822215275c83(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__28ce1f3ec34a2963200bd4b6984ca45fc0313687426bedef0cc16b1f902880e4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__08bf0dccc736c6d2932220627584372299955e875c7ce192827d90def2de5d58(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__dbd0ef4733dd17f289bc4c93e171c3a147f932fe6af669d1bf6547b102d7dfe5(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8b59c99dd02fab0d23bb0424e3690bdd186875e85e34d023600ec74a08b18116(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__2999204914cace111f96bd8927887bb65517f6eeff5801043821c6a3c1f5b010(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__594f1aa60347e70f704f6ee8d0bae7f908ea9bb2634ad0beacab219ed0f03b9e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__af50920f66f699f92cd81cb5bde74dab051f17d0e5bdc1b9679df62740569560(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a944bfe1cc28bb422a08ef3166b544aaf8889787c5b59d6b7a1b72f73c8a5d2c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4c843dcd48792cce8a49241d459ebc7a0d3751c1d33c683518f6dcbb56478ae8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0894d7f48bc19b89203f60305de7d0fd3effc58b5b44b3cdf868442003cc432b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b18c07be46d66037dc418cc48b8fe6db4e664f1efddbbce5cc1a7f9c1a9ce914(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__712e6db1ac7795a466dd9e9eb3e968278e8a2a0814f06e66b7267c436fead43d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b3012dc6f99cc0d03d777a6c288c8aa56e0d931a6ddff13d96cf023456cfa369(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__801063e9c6e501405d6d0f0bb9b60742a1fa0b0392c9bba3f5200ee2a4fc5652(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d5a5ccdeac7a39df07e1728b46ab331a55d8cbdc348a7a3b97371d5191aa2542(
    value: typing.Optional[DataKeycloakOpenidClientAuthenticationFlowBindingOverrides],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__cade826ae03b93f548fd44b20c85f1ec227485a48e410f9bff9d9b514622f27f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7ce85cc527e7f3f6c967719fcc7ea03ccc20d66c88437ba1ac2beb8d2a8eba56(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__39be7985e4a26fee443866e2eb9fe24c25861097a3618d5c7524bacd56b276ab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__dd512ae36239a83e0b7e621cc9271fcc65e535d7b583228d67311e6458548629(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__55e472169f91ab36e42f33db2c6a673027418ceeb81c72764bcd486c7da35ced(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__2994fd0684700f18cf7e4132bf8cd0772c0ec1ea73e2cc12d2bf05d907863836(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d810dd708052ac7f9b2bb37edf8f3ec20e8f105291d87bbd9643d8e9215bad4a(
    value: typing.Optional[DataKeycloakOpenidClientAuthorization],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__70e68bdf31ec7f57121522330ff46583df6ed0e0f38931619d68566d3c58d689(
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
    realm_id: builtins.str,
    consent_screen_text: typing.Optional[builtins.str] = None,
    display_on_consent_screen: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    extra_config: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    id: typing.Optional[builtins.str] = None,
    oauth2_device_authorization_grant_enabled: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    oauth2_device_code_lifespan: typing.Optional[builtins.str] = None,
    oauth2_device_polling_interval: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
