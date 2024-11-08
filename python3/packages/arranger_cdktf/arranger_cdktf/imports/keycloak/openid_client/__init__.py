"""
# `keycloak_openid_client`

Refer to the Terraform Registory for docs: [`keycloak_openid_client`](https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client).
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


class OpenidClient(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.openidClient.OpenidClient",
):
    """Represents a {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client keycloak_openid_client}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        access_type: builtins.str,
        client_id: builtins.str,
        realm_id: builtins.str,
        access_token_lifespan: typing.Optional[builtins.str] = None,
        admin_url: typing.Optional[builtins.str] = None,
        authentication_flow_binding_overrides: typing.Optional[
            typing.Union[
                "OpenidClientAuthenticationFlowBindingOverrides",
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        authorization: typing.Optional[
            typing.Union[
                "OpenidClientAuthorization", typing.Dict[builtins.str, typing.Any]
            ]
        ] = None,
        backchannel_logout_revoke_offline_sessions: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        backchannel_logout_session_required: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        backchannel_logout_url: typing.Optional[builtins.str] = None,
        base_url: typing.Optional[builtins.str] = None,
        client_authenticator_type: typing.Optional[builtins.str] = None,
        client_offline_session_idle_timeout: typing.Optional[builtins.str] = None,
        client_offline_session_max_lifespan: typing.Optional[builtins.str] = None,
        client_secret: typing.Optional[builtins.str] = None,
        client_session_idle_timeout: typing.Optional[builtins.str] = None,
        client_session_max_lifespan: typing.Optional[builtins.str] = None,
        consent_required: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        consent_screen_text: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        direct_access_grants_enabled: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        display_on_consent_screen: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        enabled: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        exclude_session_state_from_auth_response: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        extra_config: typing.Optional[
            typing.Mapping[builtins.str, builtins.str]
        ] = None,
        frontchannel_logout_enabled: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        frontchannel_logout_url: typing.Optional[builtins.str] = None,
        full_scope_allowed: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        id: typing.Optional[builtins.str] = None,
        implicit_flow_enabled: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        import_: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        login_theme: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        oauth2_device_authorization_grant_enabled: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        oauth2_device_code_lifespan: typing.Optional[builtins.str] = None,
        oauth2_device_polling_interval: typing.Optional[builtins.str] = None,
        pkce_code_challenge_method: typing.Optional[builtins.str] = None,
        root_url: typing.Optional[builtins.str] = None,
        service_accounts_enabled: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        standard_flow_enabled: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        use_refresh_tokens: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        use_refresh_tokens_client_credentials: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        valid_post_logout_redirect_uris: typing.Optional[
            typing.Sequence[builtins.str]
        ] = None,
        valid_redirect_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        web_origins: typing.Optional[typing.Sequence[builtins.str]] = None,
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
        """Create a new {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client keycloak_openid_client} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param access_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#access_type OpenidClient#access_type}.
        :param client_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#client_id OpenidClient#client_id}.
        :param realm_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#realm_id OpenidClient#realm_id}.
        :param access_token_lifespan: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#access_token_lifespan OpenidClient#access_token_lifespan}.
        :param admin_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#admin_url OpenidClient#admin_url}.
        :param authentication_flow_binding_overrides: authentication_flow_binding_overrides block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#authentication_flow_binding_overrides OpenidClient#authentication_flow_binding_overrides}
        :param authorization: authorization block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#authorization OpenidClient#authorization}
        :param backchannel_logout_revoke_offline_sessions: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#backchannel_logout_revoke_offline_sessions OpenidClient#backchannel_logout_revoke_offline_sessions}.
        :param backchannel_logout_session_required: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#backchannel_logout_session_required OpenidClient#backchannel_logout_session_required}.
        :param backchannel_logout_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#backchannel_logout_url OpenidClient#backchannel_logout_url}.
        :param base_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#base_url OpenidClient#base_url}.
        :param client_authenticator_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#client_authenticator_type OpenidClient#client_authenticator_type}.
        :param client_offline_session_idle_timeout: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#client_offline_session_idle_timeout OpenidClient#client_offline_session_idle_timeout}.
        :param client_offline_session_max_lifespan: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#client_offline_session_max_lifespan OpenidClient#client_offline_session_max_lifespan}.
        :param client_secret: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#client_secret OpenidClient#client_secret}.
        :param client_session_idle_timeout: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#client_session_idle_timeout OpenidClient#client_session_idle_timeout}.
        :param client_session_max_lifespan: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#client_session_max_lifespan OpenidClient#client_session_max_lifespan}.
        :param consent_required: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#consent_required OpenidClient#consent_required}.
        :param consent_screen_text: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#consent_screen_text OpenidClient#consent_screen_text}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#description OpenidClient#description}.
        :param direct_access_grants_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#direct_access_grants_enabled OpenidClient#direct_access_grants_enabled}.
        :param display_on_consent_screen: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#display_on_consent_screen OpenidClient#display_on_consent_screen}.
        :param enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#enabled OpenidClient#enabled}.
        :param exclude_session_state_from_auth_response: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#exclude_session_state_from_auth_response OpenidClient#exclude_session_state_from_auth_response}.
        :param extra_config: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#extra_config OpenidClient#extra_config}.
        :param frontchannel_logout_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#frontchannel_logout_enabled OpenidClient#frontchannel_logout_enabled}.
        :param frontchannel_logout_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#frontchannel_logout_url OpenidClient#frontchannel_logout_url}.
        :param full_scope_allowed: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#full_scope_allowed OpenidClient#full_scope_allowed}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#id OpenidClient#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param implicit_flow_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#implicit_flow_enabled OpenidClient#implicit_flow_enabled}.
        :param import_: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#import OpenidClient#import}.
        :param login_theme: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#login_theme OpenidClient#login_theme}.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#name OpenidClient#name}.
        :param oauth2_device_authorization_grant_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#oauth2_device_authorization_grant_enabled OpenidClient#oauth2_device_authorization_grant_enabled}.
        :param oauth2_device_code_lifespan: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#oauth2_device_code_lifespan OpenidClient#oauth2_device_code_lifespan}.
        :param oauth2_device_polling_interval: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#oauth2_device_polling_interval OpenidClient#oauth2_device_polling_interval}.
        :param pkce_code_challenge_method: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#pkce_code_challenge_method OpenidClient#pkce_code_challenge_method}.
        :param root_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#root_url OpenidClient#root_url}.
        :param service_accounts_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#service_accounts_enabled OpenidClient#service_accounts_enabled}.
        :param standard_flow_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#standard_flow_enabled OpenidClient#standard_flow_enabled}.
        :param use_refresh_tokens: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#use_refresh_tokens OpenidClient#use_refresh_tokens}.
        :param use_refresh_tokens_client_credentials: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#use_refresh_tokens_client_credentials OpenidClient#use_refresh_tokens_client_credentials}.
        :param valid_post_logout_redirect_uris: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#valid_post_logout_redirect_uris OpenidClient#valid_post_logout_redirect_uris}.
        :param valid_redirect_uris: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#valid_redirect_uris OpenidClient#valid_redirect_uris}.
        :param web_origins: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#web_origins OpenidClient#web_origins}.
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
                _typecheckingstub__634549952117d7ea9db0cdfc0783c356f24cdaa3377a46d2f39ad23186e866a0
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(
                argname="argument id_", value=id_, expected_type=type_hints["id_"]
            )
        config = OpenidClientConfig(
            access_type=access_type,
            client_id=client_id,
            realm_id=realm_id,
            access_token_lifespan=access_token_lifespan,
            admin_url=admin_url,
            authentication_flow_binding_overrides=authentication_flow_binding_overrides,
            authorization=authorization,
            backchannel_logout_revoke_offline_sessions=backchannel_logout_revoke_offline_sessions,
            backchannel_logout_session_required=backchannel_logout_session_required,
            backchannel_logout_url=backchannel_logout_url,
            base_url=base_url,
            client_authenticator_type=client_authenticator_type,
            client_offline_session_idle_timeout=client_offline_session_idle_timeout,
            client_offline_session_max_lifespan=client_offline_session_max_lifespan,
            client_secret=client_secret,
            client_session_idle_timeout=client_session_idle_timeout,
            client_session_max_lifespan=client_session_max_lifespan,
            consent_required=consent_required,
            consent_screen_text=consent_screen_text,
            description=description,
            direct_access_grants_enabled=direct_access_grants_enabled,
            display_on_consent_screen=display_on_consent_screen,
            enabled=enabled,
            exclude_session_state_from_auth_response=exclude_session_state_from_auth_response,
            extra_config=extra_config,
            frontchannel_logout_enabled=frontchannel_logout_enabled,
            frontchannel_logout_url=frontchannel_logout_url,
            full_scope_allowed=full_scope_allowed,
            id=id,
            implicit_flow_enabled=implicit_flow_enabled,
            import_=import_,
            login_theme=login_theme,
            name=name,
            oauth2_device_authorization_grant_enabled=oauth2_device_authorization_grant_enabled,
            oauth2_device_code_lifespan=oauth2_device_code_lifespan,
            oauth2_device_polling_interval=oauth2_device_polling_interval,
            pkce_code_challenge_method=pkce_code_challenge_method,
            root_url=root_url,
            service_accounts_enabled=service_accounts_enabled,
            standard_flow_enabled=standard_flow_enabled,
            use_refresh_tokens=use_refresh_tokens,
            use_refresh_tokens_client_credentials=use_refresh_tokens_client_credentials,
            valid_post_logout_redirect_uris=valid_post_logout_redirect_uris,
            valid_redirect_uris=valid_redirect_uris,
            web_origins=web_origins,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAuthenticationFlowBindingOverrides")
    def put_authentication_flow_binding_overrides(
        self,
        *,
        browser_id: typing.Optional[builtins.str] = None,
        direct_grant_id: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param browser_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#browser_id OpenidClient#browser_id}.
        :param direct_grant_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#direct_grant_id OpenidClient#direct_grant_id}.
        """
        value = OpenidClientAuthenticationFlowBindingOverrides(
            browser_id=browser_id, direct_grant_id=direct_grant_id
        )

        return typing.cast(
            None, jsii.invoke(self, "putAuthenticationFlowBindingOverrides", [value])
        )

    @jsii.member(jsii_name="putAuthorization")
    def put_authorization(
        self,
        *,
        policy_enforcement_mode: builtins.str,
        allow_remote_resource_management: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        decision_strategy: typing.Optional[builtins.str] = None,
        keep_defaults: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
    ) -> None:
        """
        :param policy_enforcement_mode: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#policy_enforcement_mode OpenidClient#policy_enforcement_mode}.
        :param allow_remote_resource_management: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#allow_remote_resource_management OpenidClient#allow_remote_resource_management}.
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#decision_strategy OpenidClient#decision_strategy}.
        :param keep_defaults: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#keep_defaults OpenidClient#keep_defaults}.
        """
        value = OpenidClientAuthorization(
            policy_enforcement_mode=policy_enforcement_mode,
            allow_remote_resource_management=allow_remote_resource_management,
            decision_strategy=decision_strategy,
            keep_defaults=keep_defaults,
        )

        return typing.cast(None, jsii.invoke(self, "putAuthorization", [value]))

    @jsii.member(jsii_name="resetAccessTokenLifespan")
    def reset_access_token_lifespan(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessTokenLifespan", []))

    @jsii.member(jsii_name="resetAdminUrl")
    def reset_admin_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdminUrl", []))

    @jsii.member(jsii_name="resetAuthenticationFlowBindingOverrides")
    def reset_authentication_flow_binding_overrides(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetAuthenticationFlowBindingOverrides", [])
        )

    @jsii.member(jsii_name="resetAuthorization")
    def reset_authorization(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthorization", []))

    @jsii.member(jsii_name="resetBackchannelLogoutRevokeOfflineSessions")
    def reset_backchannel_logout_revoke_offline_sessions(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetBackchannelLogoutRevokeOfflineSessions", [])
        )

    @jsii.member(jsii_name="resetBackchannelLogoutSessionRequired")
    def reset_backchannel_logout_session_required(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetBackchannelLogoutSessionRequired", [])
        )

    @jsii.member(jsii_name="resetBackchannelLogoutUrl")
    def reset_backchannel_logout_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackchannelLogoutUrl", []))

    @jsii.member(jsii_name="resetBaseUrl")
    def reset_base_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBaseUrl", []))

    @jsii.member(jsii_name="resetClientAuthenticatorType")
    def reset_client_authenticator_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientAuthenticatorType", []))

    @jsii.member(jsii_name="resetClientOfflineSessionIdleTimeout")
    def reset_client_offline_session_idle_timeout(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetClientOfflineSessionIdleTimeout", [])
        )

    @jsii.member(jsii_name="resetClientOfflineSessionMaxLifespan")
    def reset_client_offline_session_max_lifespan(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetClientOfflineSessionMaxLifespan", [])
        )

    @jsii.member(jsii_name="resetClientSecret")
    def reset_client_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientSecret", []))

    @jsii.member(jsii_name="resetClientSessionIdleTimeout")
    def reset_client_session_idle_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientSessionIdleTimeout", []))

    @jsii.member(jsii_name="resetClientSessionMaxLifespan")
    def reset_client_session_max_lifespan(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientSessionMaxLifespan", []))

    @jsii.member(jsii_name="resetConsentRequired")
    def reset_consent_required(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConsentRequired", []))

    @jsii.member(jsii_name="resetConsentScreenText")
    def reset_consent_screen_text(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConsentScreenText", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDirectAccessGrantsEnabled")
    def reset_direct_access_grants_enabled(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetDirectAccessGrantsEnabled", [])
        )

    @jsii.member(jsii_name="resetDisplayOnConsentScreen")
    def reset_display_on_consent_screen(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayOnConsentScreen", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetExcludeSessionStateFromAuthResponse")
    def reset_exclude_session_state_from_auth_response(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetExcludeSessionStateFromAuthResponse", [])
        )

    @jsii.member(jsii_name="resetExtraConfig")
    def reset_extra_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtraConfig", []))

    @jsii.member(jsii_name="resetFrontchannelLogoutEnabled")
    def reset_frontchannel_logout_enabled(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetFrontchannelLogoutEnabled", [])
        )

    @jsii.member(jsii_name="resetFrontchannelLogoutUrl")
    def reset_frontchannel_logout_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFrontchannelLogoutUrl", []))

    @jsii.member(jsii_name="resetFullScopeAllowed")
    def reset_full_scope_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFullScopeAllowed", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetImplicitFlowEnabled")
    def reset_implicit_flow_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImplicitFlowEnabled", []))

    @jsii.member(jsii_name="resetImport")
    def reset_import(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImport", []))

    @jsii.member(jsii_name="resetLoginTheme")
    def reset_login_theme(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoginTheme", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

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

    @jsii.member(jsii_name="resetPkceCodeChallengeMethod")
    def reset_pkce_code_challenge_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPkceCodeChallengeMethod", []))

    @jsii.member(jsii_name="resetRootUrl")
    def reset_root_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootUrl", []))

    @jsii.member(jsii_name="resetServiceAccountsEnabled")
    def reset_service_accounts_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceAccountsEnabled", []))

    @jsii.member(jsii_name="resetStandardFlowEnabled")
    def reset_standard_flow_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStandardFlowEnabled", []))

    @jsii.member(jsii_name="resetUseRefreshTokens")
    def reset_use_refresh_tokens(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseRefreshTokens", []))

    @jsii.member(jsii_name="resetUseRefreshTokensClientCredentials")
    def reset_use_refresh_tokens_client_credentials(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetUseRefreshTokensClientCredentials", [])
        )

    @jsii.member(jsii_name="resetValidPostLogoutRedirectUris")
    def reset_valid_post_logout_redirect_uris(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetValidPostLogoutRedirectUris", [])
        )

    @jsii.member(jsii_name="resetValidRedirectUris")
    def reset_valid_redirect_uris(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValidRedirectUris", []))

    @jsii.member(jsii_name="resetWebOrigins")
    def reset_web_origins(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebOrigins", []))

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
    @jsii.member(jsii_name="authenticationFlowBindingOverrides")
    def authentication_flow_binding_overrides(
        self,
    ) -> "OpenidClientAuthenticationFlowBindingOverridesOutputReference":
        return typing.cast(
            "OpenidClientAuthenticationFlowBindingOverridesOutputReference",
            jsii.get(self, "authenticationFlowBindingOverrides"),
        )

    @builtins.property
    @jsii.member(jsii_name="authorization")
    def authorization(self) -> "OpenidClientAuthorizationOutputReference":
        return typing.cast(
            "OpenidClientAuthorizationOutputReference", jsii.get(self, "authorization")
        )

    @builtins.property
    @jsii.member(jsii_name="resourceServerId")
    def resource_server_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceServerId"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccountUserId")
    def service_account_user_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccountUserId"))

    @builtins.property
    @jsii.member(jsii_name="accessTokenLifespanInput")
    def access_token_lifespan_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "accessTokenLifespanInput")
        )

    @builtins.property
    @jsii.member(jsii_name="accessTypeInput")
    def access_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "accessTypeInput")
        )

    @builtins.property
    @jsii.member(jsii_name="adminUrlInput")
    def admin_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "adminUrlInput")
        )

    @builtins.property
    @jsii.member(jsii_name="authenticationFlowBindingOverridesInput")
    def authentication_flow_binding_overrides_input(
        self,
    ) -> typing.Optional["OpenidClientAuthenticationFlowBindingOverrides"]:
        return typing.cast(
            typing.Optional["OpenidClientAuthenticationFlowBindingOverrides"],
            jsii.get(self, "authenticationFlowBindingOverridesInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="authorizationInput")
    def authorization_input(self) -> typing.Optional["OpenidClientAuthorization"]:
        return typing.cast(
            typing.Optional["OpenidClientAuthorization"],
            jsii.get(self, "authorizationInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="backchannelLogoutRevokeOfflineSessionsInput")
    def backchannel_logout_revoke_offline_sessions_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "backchannelLogoutRevokeOfflineSessionsInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="backchannelLogoutSessionRequiredInput")
    def backchannel_logout_session_required_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "backchannelLogoutSessionRequiredInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="backchannelLogoutUrlInput")
    def backchannel_logout_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "backchannelLogoutUrlInput")
        )

    @builtins.property
    @jsii.member(jsii_name="baseUrlInput")
    def base_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "baseUrlInput")
        )

    @builtins.property
    @jsii.member(jsii_name="clientAuthenticatorTypeInput")
    def client_authenticator_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "clientAuthenticatorTypeInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "clientIdInput")
        )

    @builtins.property
    @jsii.member(jsii_name="clientOfflineSessionIdleTimeoutInput")
    def client_offline_session_idle_timeout_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "clientOfflineSessionIdleTimeoutInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="clientOfflineSessionMaxLifespanInput")
    def client_offline_session_max_lifespan_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "clientOfflineSessionMaxLifespanInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "clientSecretInput")
        )

    @builtins.property
    @jsii.member(jsii_name="clientSessionIdleTimeoutInput")
    def client_session_idle_timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "clientSessionIdleTimeoutInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="clientSessionMaxLifespanInput")
    def client_session_max_lifespan_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "clientSessionMaxLifespanInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="consentRequiredInput")
    def consent_required_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "consentRequiredInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="consentScreenTextInput")
    def consent_screen_text_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "consentScreenTextInput")
        )

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "descriptionInput")
        )

    @builtins.property
    @jsii.member(jsii_name="directAccessGrantsEnabledInput")
    def direct_access_grants_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "directAccessGrantsEnabledInput"),
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
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "enabledInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="excludeSessionStateFromAuthResponseInput")
    def exclude_session_state_from_auth_response_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "excludeSessionStateFromAuthResponseInput"),
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
    @jsii.member(jsii_name="frontchannelLogoutEnabledInput")
    def frontchannel_logout_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "frontchannelLogoutEnabledInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="frontchannelLogoutUrlInput")
    def frontchannel_logout_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "frontchannelLogoutUrlInput")
        )

    @builtins.property
    @jsii.member(jsii_name="fullScopeAllowedInput")
    def full_scope_allowed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "fullScopeAllowedInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="implicitFlowEnabledInput")
    def implicit_flow_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "implicitFlowEnabledInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="importInput")
    def import_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "importInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="loginThemeInput")
    def login_theme_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "loginThemeInput")
        )

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

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
    @jsii.member(jsii_name="pkceCodeChallengeMethodInput")
    def pkce_code_challenge_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "pkceCodeChallengeMethodInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="realmIdInput")
    def realm_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "realmIdInput")
        )

    @builtins.property
    @jsii.member(jsii_name="rootUrlInput")
    def root_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "rootUrlInput")
        )

    @builtins.property
    @jsii.member(jsii_name="serviceAccountsEnabledInput")
    def service_accounts_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "serviceAccountsEnabledInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="standardFlowEnabledInput")
    def standard_flow_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "standardFlowEnabledInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="useRefreshTokensClientCredentialsInput")
    def use_refresh_tokens_client_credentials_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "useRefreshTokensClientCredentialsInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="useRefreshTokensInput")
    def use_refresh_tokens_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "useRefreshTokensInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="validPostLogoutRedirectUrisInput")
    def valid_post_logout_redirect_uris_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]],
            jsii.get(self, "validPostLogoutRedirectUrisInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="validRedirectUrisInput")
    def valid_redirect_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]],
            jsii.get(self, "validRedirectUrisInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="webOriginsInput")
    def web_origins_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]],
            jsii.get(self, "webOriginsInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="accessTokenLifespan")
    def access_token_lifespan(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessTokenLifespan"))

    @access_token_lifespan.setter
    def access_token_lifespan(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__1f7e24f3bbaae1708b01d4941d0ce8b2dcd2994a97ef5fda0e9d0e947d511ce6
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "accessTokenLifespan", value)

    @builtins.property
    @jsii.member(jsii_name="accessType")
    def access_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessType"))

    @access_type.setter
    def access_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__67a307c26e2552fc48bea862da4c76c59351341009dce73fb2580f11e9f41bde
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "accessType", value)

    @builtins.property
    @jsii.member(jsii_name="adminUrl")
    def admin_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adminUrl"))

    @admin_url.setter
    def admin_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__6cdd47d444d5d5d220ae8d50b75a7733ae91c4c15d6a35c4ba22b858df85a5a6
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "adminUrl", value)

    @builtins.property
    @jsii.member(jsii_name="backchannelLogoutRevokeOfflineSessions")
    def backchannel_logout_revoke_offline_sessions(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "backchannelLogoutRevokeOfflineSessions"),
        )

    @backchannel_logout_revoke_offline_sessions.setter
    def backchannel_logout_revoke_offline_sessions(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__3c8b2bf5768a0a14fb978477486f880d2595202293b7e6da380b5558dd152ce5
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "backchannelLogoutRevokeOfflineSessions", value)

    @builtins.property
    @jsii.member(jsii_name="backchannelLogoutSessionRequired")
    def backchannel_logout_session_required(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "backchannelLogoutSessionRequired"),
        )

    @backchannel_logout_session_required.setter
    def backchannel_logout_session_required(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d75d1585f9c18b7af7bd332c5e181b306daac7423a5dda901e99522b8c307b88
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "backchannelLogoutSessionRequired", value)

    @builtins.property
    @jsii.member(jsii_name="backchannelLogoutUrl")
    def backchannel_logout_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backchannelLogoutUrl"))

    @backchannel_logout_url.setter
    def backchannel_logout_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__db2a3a200d15bce74a61808374530a4f30ccfdecf68e906e8fa71214e05235fa
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "backchannelLogoutUrl", value)

    @builtins.property
    @jsii.member(jsii_name="baseUrl")
    def base_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "baseUrl"))

    @base_url.setter
    def base_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a3560b0461d6b7c35214928f4300e5d573f4c4f84ae94255ea55f921b69e21e6
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "baseUrl", value)

    @builtins.property
    @jsii.member(jsii_name="clientAuthenticatorType")
    def client_authenticator_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientAuthenticatorType"))

    @client_authenticator_type.setter
    def client_authenticator_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__082d2c9226374d8e92cb0d2760428e684ca1b82cbe10b619adc93f6b56c2c003
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "clientAuthenticatorType", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__6c272a3d27e6fb2e81ce21e768fb98e333ab45d1a55dbe7a2092783a8f5be3b7
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientOfflineSessionIdleTimeout")
    def client_offline_session_idle_timeout(self) -> builtins.str:
        return typing.cast(
            builtins.str, jsii.get(self, "clientOfflineSessionIdleTimeout")
        )

    @client_offline_session_idle_timeout.setter
    def client_offline_session_idle_timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__e5846e325b50fb3caa612c448e66462130cdcbcac79dedabb9b872afe15339b2
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "clientOfflineSessionIdleTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="clientOfflineSessionMaxLifespan")
    def client_offline_session_max_lifespan(self) -> builtins.str:
        return typing.cast(
            builtins.str, jsii.get(self, "clientOfflineSessionMaxLifespan")
        )

    @client_offline_session_max_lifespan.setter
    def client_offline_session_max_lifespan(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__41cf4441d5b54e0994965446094ee7c57f6f48c029e1334f086efae01220aafe
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "clientOfflineSessionMaxLifespan", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__6f760c5b50bb1f5d90556f1c2e3ac41f6ed100bd8439ece866071a09906f1288
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="clientSessionIdleTimeout")
    def client_session_idle_timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSessionIdleTimeout"))

    @client_session_idle_timeout.setter
    def client_session_idle_timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__2c91a6132989026c2c06ba7c31c6e14134a211179e7973fa12273c69b05856c7
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "clientSessionIdleTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="clientSessionMaxLifespan")
    def client_session_max_lifespan(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSessionMaxLifespan"))

    @client_session_max_lifespan.setter
    def client_session_max_lifespan(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__7de9688a1b7742bab7480c770467ae85e92e847a92cf901ba8b16bd3161481e8
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "clientSessionMaxLifespan", value)

    @builtins.property
    @jsii.member(jsii_name="consentRequired")
    def consent_required(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "consentRequired"),
        )

    @consent_required.setter
    def consent_required(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__779a8570f4c72fa4fdefbd2b9819c3fe2dc4a91d587d45fc608e0333705ad686
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "consentRequired", value)

    @builtins.property
    @jsii.member(jsii_name="consentScreenText")
    def consent_screen_text(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "consentScreenText"))

    @consent_screen_text.setter
    def consent_screen_text(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__be8d53178a33955814bc546da442adc4dba43f839d0c4089223e001707bc8847
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "consentScreenText", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__c84831f84fdb3a3605c2e109d5eb369abe7c453023959618d4a72d435a6e5642
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="directAccessGrantsEnabled")
    def direct_access_grants_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "directAccessGrantsEnabled"),
        )

    @direct_access_grants_enabled.setter
    def direct_access_grants_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__8f7deec0d9b3016e751b2c57ca3ecfe35cff166fa3f9203abbd76df58efc751e
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "directAccessGrantsEnabled", value)

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
                _typecheckingstub__610075f4af08d3db9754ca2ced3853780a7c9067d2f9023521f2cb7cd006ac62
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "displayOnConsentScreen", value)

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
                _typecheckingstub__ded75aa3172914314ba67b87b5ac7cc773c47d53d88b1b9e3bd372846b2ac37d
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="excludeSessionStateFromAuthResponse")
    def exclude_session_state_from_auth_response(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "excludeSessionStateFromAuthResponse"),
        )

    @exclude_session_state_from_auth_response.setter
    def exclude_session_state_from_auth_response(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__69bb6cd38b6c01df0da6d11f7f6470bcb34251a2e22675c212b75da2b9baa4d7
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "excludeSessionStateFromAuthResponse", value)

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
                _typecheckingstub__fc545ba780855b5cb93c6d4061fc66482422192341b767caae5678d851ebad00
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "extraConfig", value)

    @builtins.property
    @jsii.member(jsii_name="frontchannelLogoutEnabled")
    def frontchannel_logout_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "frontchannelLogoutEnabled"),
        )

    @frontchannel_logout_enabled.setter
    def frontchannel_logout_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b1d5015a2ac2653a696901f900c90ee7fcf23e0b38df3227b813acaea164b2cc
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "frontchannelLogoutEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="frontchannelLogoutUrl")
    def frontchannel_logout_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "frontchannelLogoutUrl"))

    @frontchannel_logout_url.setter
    def frontchannel_logout_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b8c3695b84acaa4bf76cd199821936b33d321f0b3d5c6b09b1c7b7f2546e60ec
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "frontchannelLogoutUrl", value)

    @builtins.property
    @jsii.member(jsii_name="fullScopeAllowed")
    def full_scope_allowed(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "fullScopeAllowed"),
        )

    @full_scope_allowed.setter
    def full_scope_allowed(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__0134873a9e50a1a618b2ace6174fa3aa80e8fd76f24188de6de2d5592f9bc584
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "fullScopeAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__9e335c3c07548af99f990ad410eb07ed368c134ba6fd0cec50da87e9712f7c9d
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="implicitFlowEnabled")
    def implicit_flow_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "implicitFlowEnabled"),
        )

    @implicit_flow_enabled.setter
    def implicit_flow_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b8f6d5eedc2ea6576399751af2bcbf5b61a159ec8bbe540ec386707b7601cfef
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "implicitFlowEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="import")
    def import_(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "import"),
        )

    @import_.setter
    def import_(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a193e3313c2264aad1c986d3dc1ff2aeabd6478cb3998a94272eefe9b4151fc7
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "import", value)

    @builtins.property
    @jsii.member(jsii_name="loginTheme")
    def login_theme(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loginTheme"))

    @login_theme.setter
    def login_theme(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__3cb5314364fbae339899526e94f1a17c576a813b2334f43c221eceaa97a976fe
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "loginTheme", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__59da3fa5510d12459f882dcd383b456e792d98c1ea95f062ad69d5f7d3090efd
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "name", value)

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
                _typecheckingstub__9ff5e641e930dcc492d30ec9da187113f55cc3f7d249747789ec33bd4d2d0e95
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
                _typecheckingstub__1fcde79d4dc991edc87b12a3fbbb207a0573572809533d7c5e77cf6162b44c36
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
                _typecheckingstub__20d7bb6da8ec7c76a6734b5b81aeec1de877d646246a81f58c561240610391e7
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "oauth2DevicePollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="pkceCodeChallengeMethod")
    def pkce_code_challenge_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pkceCodeChallengeMethod"))

    @pkce_code_challenge_method.setter
    def pkce_code_challenge_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__ad6b697b9d36ef958a135d4ad3a2dfe3f2b221628b67132d7a9f340a6acbcdd4
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "pkceCodeChallengeMethod", value)

    @builtins.property
    @jsii.member(jsii_name="realmId")
    def realm_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "realmId"))

    @realm_id.setter
    def realm_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__e9a6280f1e2cb13260aed3fa557ca3c6f5600d38eb033d2065ac5473ccfe6ed1
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "realmId", value)

    @builtins.property
    @jsii.member(jsii_name="rootUrl")
    def root_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rootUrl"))

    @root_url.setter
    def root_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__67d00cce56d515ac75ddb1469e41f3117c72e0a6cf8733bd38af7df92e398b00
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "rootUrl", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccountsEnabled")
    def service_accounts_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "serviceAccountsEnabled"),
        )

    @service_accounts_enabled.setter
    def service_accounts_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__0ba14ed351b0f9a3f090d760b562114359d9411e5b7571db06f5af7d48ed0557
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "serviceAccountsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="standardFlowEnabled")
    def standard_flow_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "standardFlowEnabled"),
        )

    @standard_flow_enabled.setter
    def standard_flow_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__796fc44b2c1a5472481009bd6d6eaaad257cd707564004a7eec7b7d24f3e66bb
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "standardFlowEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="useRefreshTokens")
    def use_refresh_tokens(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "useRefreshTokens"),
        )

    @use_refresh_tokens.setter
    def use_refresh_tokens(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__9c56992c0cc687f24563a6444b7c318be3e3ca3dde65bcda6860a6bc71a0a305
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "useRefreshTokens", value)

    @builtins.property
    @jsii.member(jsii_name="useRefreshTokensClientCredentials")
    def use_refresh_tokens_client_credentials(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "useRefreshTokensClientCredentials"),
        )

    @use_refresh_tokens_client_credentials.setter
    def use_refresh_tokens_client_credentials(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__c89fe7d8e0a78ac0fec3d62f1a99bea86231be0d4ecf0cd3e51e798d7b001edc
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "useRefreshTokensClientCredentials", value)

    @builtins.property
    @jsii.member(jsii_name="validPostLogoutRedirectUris")
    def valid_post_logout_redirect_uris(self) -> typing.List[builtins.str]:
        return typing.cast(
            typing.List[builtins.str], jsii.get(self, "validPostLogoutRedirectUris")
        )

    @valid_post_logout_redirect_uris.setter
    def valid_post_logout_redirect_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__0a3873f2ac0be44e474dadb41ca19e27d7431fd53ea4cef24ece3f361bb87593
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "validPostLogoutRedirectUris", value)

    @builtins.property
    @jsii.member(jsii_name="validRedirectUris")
    def valid_redirect_uris(self) -> typing.List[builtins.str]:
        return typing.cast(
            typing.List[builtins.str], jsii.get(self, "validRedirectUris")
        )

    @valid_redirect_uris.setter
    def valid_redirect_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__4a2e5d87738ad8ba9b5c3de1643eeca3a8383a3de7e8d189cba7e3e0d1f18386
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "validRedirectUris", value)

    @builtins.property
    @jsii.member(jsii_name="webOrigins")
    def web_origins(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "webOrigins"))

    @web_origins.setter
    def web_origins(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__3439274c89f2b0efd03243a0d0eb6b4ec281ec9233bbdb1f055736d7e14b8532
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "webOrigins", value)


@jsii.data_type(
    jsii_type="keycloak.openidClient.OpenidClientAuthenticationFlowBindingOverrides",
    jsii_struct_bases=[],
    name_mapping={"browser_id": "browserId", "direct_grant_id": "directGrantId"},
)
class OpenidClientAuthenticationFlowBindingOverrides:
    def __init__(
        self,
        *,
        browser_id: typing.Optional[builtins.str] = None,
        direct_grant_id: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param browser_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#browser_id OpenidClient#browser_id}.
        :param direct_grant_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#direct_grant_id OpenidClient#direct_grant_id}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d099d158e8c0e1a4b793fc7d1ad3f9d2658d772bcde4a5fb346f314ad8e3c0ea
            )
            check_type(
                argname="argument browser_id",
                value=browser_id,
                expected_type=type_hints["browser_id"],
            )
            check_type(
                argname="argument direct_grant_id",
                value=direct_grant_id,
                expected_type=type_hints["direct_grant_id"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if browser_id is not None:
            self._values["browser_id"] = browser_id
        if direct_grant_id is not None:
            self._values["direct_grant_id"] = direct_grant_id

    @builtins.property
    def browser_id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#browser_id OpenidClient#browser_id}."""
        result = self._values.get("browser_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def direct_grant_id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#direct_grant_id OpenidClient#direct_grant_id}."""
        result = self._values.get("direct_grant_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpenidClientAuthenticationFlowBindingOverrides(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpenidClientAuthenticationFlowBindingOverridesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.openidClient.OpenidClientAuthenticationFlowBindingOverridesOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__272281f75bc70268e972fc3b335377b81764c3c5d7ef29692a643a1e5dfd5615
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
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBrowserId")
    def reset_browser_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBrowserId", []))

    @jsii.member(jsii_name="resetDirectGrantId")
    def reset_direct_grant_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDirectGrantId", []))

    @builtins.property
    @jsii.member(jsii_name="browserIdInput")
    def browser_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "browserIdInput")
        )

    @builtins.property
    @jsii.member(jsii_name="directGrantIdInput")
    def direct_grant_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "directGrantIdInput")
        )

    @builtins.property
    @jsii.member(jsii_name="browserId")
    def browser_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "browserId"))

    @browser_id.setter
    def browser_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__842b6eecf134f01c5dcb6dd8bc4e087d92cf696de550e5a5f5c5eb2a1e67401e
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "browserId", value)

    @builtins.property
    @jsii.member(jsii_name="directGrantId")
    def direct_grant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directGrantId"))

    @direct_grant_id.setter
    def direct_grant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__9345a5cc6a85f39c4fa2e51befc32e39e422561c685709a9bfb7abc1a63670eb
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "directGrantId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OpenidClientAuthenticationFlowBindingOverrides]:
        return typing.cast(
            typing.Optional[OpenidClientAuthenticationFlowBindingOverrides],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpenidClientAuthenticationFlowBindingOverrides],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__72c115a179fa7a1f110cbc8799826d0a97acc010de0275b6911d72759713ec17
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="keycloak.openidClient.OpenidClientAuthorization",
    jsii_struct_bases=[],
    name_mapping={
        "policy_enforcement_mode": "policyEnforcementMode",
        "allow_remote_resource_management": "allowRemoteResourceManagement",
        "decision_strategy": "decisionStrategy",
        "keep_defaults": "keepDefaults",
    },
)
class OpenidClientAuthorization:
    def __init__(
        self,
        *,
        policy_enforcement_mode: builtins.str,
        allow_remote_resource_management: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        decision_strategy: typing.Optional[builtins.str] = None,
        keep_defaults: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
    ) -> None:
        """
        :param policy_enforcement_mode: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#policy_enforcement_mode OpenidClient#policy_enforcement_mode}.
        :param allow_remote_resource_management: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#allow_remote_resource_management OpenidClient#allow_remote_resource_management}.
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#decision_strategy OpenidClient#decision_strategy}.
        :param keep_defaults: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#keep_defaults OpenidClient#keep_defaults}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__eb33dd10a48afb782a9e67e47174e40f5fa8a1d019fdf273454451ef26dfb744
            )
            check_type(
                argname="argument policy_enforcement_mode",
                value=policy_enforcement_mode,
                expected_type=type_hints["policy_enforcement_mode"],
            )
            check_type(
                argname="argument allow_remote_resource_management",
                value=allow_remote_resource_management,
                expected_type=type_hints["allow_remote_resource_management"],
            )
            check_type(
                argname="argument decision_strategy",
                value=decision_strategy,
                expected_type=type_hints["decision_strategy"],
            )
            check_type(
                argname="argument keep_defaults",
                value=keep_defaults,
                expected_type=type_hints["keep_defaults"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_enforcement_mode": policy_enforcement_mode,
        }
        if allow_remote_resource_management is not None:
            self._values[
                "allow_remote_resource_management"
            ] = allow_remote_resource_management
        if decision_strategy is not None:
            self._values["decision_strategy"] = decision_strategy
        if keep_defaults is not None:
            self._values["keep_defaults"] = keep_defaults

    @builtins.property
    def policy_enforcement_mode(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#policy_enforcement_mode OpenidClient#policy_enforcement_mode}."""
        result = self._values.get("policy_enforcement_mode")
        assert (
            result is not None
        ), "Required property 'policy_enforcement_mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_remote_resource_management(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#allow_remote_resource_management OpenidClient#allow_remote_resource_management}."""
        result = self._values.get("allow_remote_resource_management")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def decision_strategy(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#decision_strategy OpenidClient#decision_strategy}."""
        result = self._values.get("decision_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def keep_defaults(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#keep_defaults OpenidClient#keep_defaults}."""
        result = self._values.get("keep_defaults")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpenidClientAuthorization(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpenidClientAuthorizationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.openidClient.OpenidClientAuthorizationOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__82ce42e9317106653675d487554ee6499f657f1eed34a0606c9af30c16eb6962
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
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowRemoteResourceManagement")
    def reset_allow_remote_resource_management(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetAllowRemoteResourceManagement", [])
        )

    @jsii.member(jsii_name="resetDecisionStrategy")
    def reset_decision_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDecisionStrategy", []))

    @jsii.member(jsii_name="resetKeepDefaults")
    def reset_keep_defaults(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeepDefaults", []))

    @builtins.property
    @jsii.member(jsii_name="allowRemoteResourceManagementInput")
    def allow_remote_resource_management_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "allowRemoteResourceManagementInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="decisionStrategyInput")
    def decision_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "decisionStrategyInput")
        )

    @builtins.property
    @jsii.member(jsii_name="keepDefaultsInput")
    def keep_defaults_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "keepDefaultsInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="policyEnforcementModeInput")
    def policy_enforcement_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "policyEnforcementModeInput")
        )

    @builtins.property
    @jsii.member(jsii_name="allowRemoteResourceManagement")
    def allow_remote_resource_management(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "allowRemoteResourceManagement"),
        )

    @allow_remote_resource_management.setter
    def allow_remote_resource_management(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__6cc83925456eb366db06e981946e34710dd791f177b8406b552fbe5d835659ee
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "allowRemoteResourceManagement", value)

    @builtins.property
    @jsii.member(jsii_name="decisionStrategy")
    def decision_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "decisionStrategy"))

    @decision_strategy.setter
    def decision_strategy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__e119a3b242582379cb1898694f244ec16c4cd7a6b270eb47541ca30d95ecd3ae
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "decisionStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="keepDefaults")
    def keep_defaults(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "keepDefaults"),
        )

    @keep_defaults.setter
    def keep_defaults(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__be706a5c1596f5a76cc54743da1b0dd1bbbf45ef6fe396b0b76473ad146e7d30
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "keepDefaults", value)

    @builtins.property
    @jsii.member(jsii_name="policyEnforcementMode")
    def policy_enforcement_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policyEnforcementMode"))

    @policy_enforcement_mode.setter
    def policy_enforcement_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__9f204b2cdcdd7813a9e8004765b3f286f612ded887954ccc831e27e24e65240a
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "policyEnforcementMode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OpenidClientAuthorization]:
        return typing.cast(
            typing.Optional[OpenidClientAuthorization], jsii.get(self, "internalValue")
        )

    @internal_value.setter
    def internal_value(self, value: typing.Optional[OpenidClientAuthorization]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__ada659dd5b9dc309443e6fc2ab70af5a260f2ca6a69ffcd0a2fcf81af7c8001b
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="keycloak.openidClient.OpenidClientConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "access_type": "accessType",
        "client_id": "clientId",
        "realm_id": "realmId",
        "access_token_lifespan": "accessTokenLifespan",
        "admin_url": "adminUrl",
        "authentication_flow_binding_overrides": "authenticationFlowBindingOverrides",
        "authorization": "authorization",
        "backchannel_logout_revoke_offline_sessions": "backchannelLogoutRevokeOfflineSessions",
        "backchannel_logout_session_required": "backchannelLogoutSessionRequired",
        "backchannel_logout_url": "backchannelLogoutUrl",
        "base_url": "baseUrl",
        "client_authenticator_type": "clientAuthenticatorType",
        "client_offline_session_idle_timeout": "clientOfflineSessionIdleTimeout",
        "client_offline_session_max_lifespan": "clientOfflineSessionMaxLifespan",
        "client_secret": "clientSecret",
        "client_session_idle_timeout": "clientSessionIdleTimeout",
        "client_session_max_lifespan": "clientSessionMaxLifespan",
        "consent_required": "consentRequired",
        "consent_screen_text": "consentScreenText",
        "description": "description",
        "direct_access_grants_enabled": "directAccessGrantsEnabled",
        "display_on_consent_screen": "displayOnConsentScreen",
        "enabled": "enabled",
        "exclude_session_state_from_auth_response": "excludeSessionStateFromAuthResponse",
        "extra_config": "extraConfig",
        "frontchannel_logout_enabled": "frontchannelLogoutEnabled",
        "frontchannel_logout_url": "frontchannelLogoutUrl",
        "full_scope_allowed": "fullScopeAllowed",
        "id": "id",
        "implicit_flow_enabled": "implicitFlowEnabled",
        "import_": "import",
        "login_theme": "loginTheme",
        "name": "name",
        "oauth2_device_authorization_grant_enabled": "oauth2DeviceAuthorizationGrantEnabled",
        "oauth2_device_code_lifespan": "oauth2DeviceCodeLifespan",
        "oauth2_device_polling_interval": "oauth2DevicePollingInterval",
        "pkce_code_challenge_method": "pkceCodeChallengeMethod",
        "root_url": "rootUrl",
        "service_accounts_enabled": "serviceAccountsEnabled",
        "standard_flow_enabled": "standardFlowEnabled",
        "use_refresh_tokens": "useRefreshTokens",
        "use_refresh_tokens_client_credentials": "useRefreshTokensClientCredentials",
        "valid_post_logout_redirect_uris": "validPostLogoutRedirectUris",
        "valid_redirect_uris": "validRedirectUris",
        "web_origins": "webOrigins",
    },
)
class OpenidClientConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        access_type: builtins.str,
        client_id: builtins.str,
        realm_id: builtins.str,
        access_token_lifespan: typing.Optional[builtins.str] = None,
        admin_url: typing.Optional[builtins.str] = None,
        authentication_flow_binding_overrides: typing.Optional[
            typing.Union[
                OpenidClientAuthenticationFlowBindingOverrides,
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        authorization: typing.Optional[
            typing.Union[
                OpenidClientAuthorization, typing.Dict[builtins.str, typing.Any]
            ]
        ] = None,
        backchannel_logout_revoke_offline_sessions: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        backchannel_logout_session_required: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        backchannel_logout_url: typing.Optional[builtins.str] = None,
        base_url: typing.Optional[builtins.str] = None,
        client_authenticator_type: typing.Optional[builtins.str] = None,
        client_offline_session_idle_timeout: typing.Optional[builtins.str] = None,
        client_offline_session_max_lifespan: typing.Optional[builtins.str] = None,
        client_secret: typing.Optional[builtins.str] = None,
        client_session_idle_timeout: typing.Optional[builtins.str] = None,
        client_session_max_lifespan: typing.Optional[builtins.str] = None,
        consent_required: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        consent_screen_text: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        direct_access_grants_enabled: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        display_on_consent_screen: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        enabled: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        exclude_session_state_from_auth_response: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        extra_config: typing.Optional[
            typing.Mapping[builtins.str, builtins.str]
        ] = None,
        frontchannel_logout_enabled: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        frontchannel_logout_url: typing.Optional[builtins.str] = None,
        full_scope_allowed: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        id: typing.Optional[builtins.str] = None,
        implicit_flow_enabled: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        import_: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        login_theme: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        oauth2_device_authorization_grant_enabled: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        oauth2_device_code_lifespan: typing.Optional[builtins.str] = None,
        oauth2_device_polling_interval: typing.Optional[builtins.str] = None,
        pkce_code_challenge_method: typing.Optional[builtins.str] = None,
        root_url: typing.Optional[builtins.str] = None,
        service_accounts_enabled: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        standard_flow_enabled: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        use_refresh_tokens: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        use_refresh_tokens_client_credentials: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        valid_post_logout_redirect_uris: typing.Optional[
            typing.Sequence[builtins.str]
        ] = None,
        valid_redirect_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        web_origins: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param connection:
        :param count:
        :param depends_on:
        :param for_each:
        :param lifecycle:
        :param provider:
        :param provisioners:
        :param access_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#access_type OpenidClient#access_type}.
        :param client_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#client_id OpenidClient#client_id}.
        :param realm_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#realm_id OpenidClient#realm_id}.
        :param access_token_lifespan: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#access_token_lifespan OpenidClient#access_token_lifespan}.
        :param admin_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#admin_url OpenidClient#admin_url}.
        :param authentication_flow_binding_overrides: authentication_flow_binding_overrides block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#authentication_flow_binding_overrides OpenidClient#authentication_flow_binding_overrides}
        :param authorization: authorization block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#authorization OpenidClient#authorization}
        :param backchannel_logout_revoke_offline_sessions: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#backchannel_logout_revoke_offline_sessions OpenidClient#backchannel_logout_revoke_offline_sessions}.
        :param backchannel_logout_session_required: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#backchannel_logout_session_required OpenidClient#backchannel_logout_session_required}.
        :param backchannel_logout_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#backchannel_logout_url OpenidClient#backchannel_logout_url}.
        :param base_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#base_url OpenidClient#base_url}.
        :param client_authenticator_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#client_authenticator_type OpenidClient#client_authenticator_type}.
        :param client_offline_session_idle_timeout: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#client_offline_session_idle_timeout OpenidClient#client_offline_session_idle_timeout}.
        :param client_offline_session_max_lifespan: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#client_offline_session_max_lifespan OpenidClient#client_offline_session_max_lifespan}.
        :param client_secret: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#client_secret OpenidClient#client_secret}.
        :param client_session_idle_timeout: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#client_session_idle_timeout OpenidClient#client_session_idle_timeout}.
        :param client_session_max_lifespan: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#client_session_max_lifespan OpenidClient#client_session_max_lifespan}.
        :param consent_required: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#consent_required OpenidClient#consent_required}.
        :param consent_screen_text: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#consent_screen_text OpenidClient#consent_screen_text}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#description OpenidClient#description}.
        :param direct_access_grants_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#direct_access_grants_enabled OpenidClient#direct_access_grants_enabled}.
        :param display_on_consent_screen: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#display_on_consent_screen OpenidClient#display_on_consent_screen}.
        :param enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#enabled OpenidClient#enabled}.
        :param exclude_session_state_from_auth_response: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#exclude_session_state_from_auth_response OpenidClient#exclude_session_state_from_auth_response}.
        :param extra_config: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#extra_config OpenidClient#extra_config}.
        :param frontchannel_logout_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#frontchannel_logout_enabled OpenidClient#frontchannel_logout_enabled}.
        :param frontchannel_logout_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#frontchannel_logout_url OpenidClient#frontchannel_logout_url}.
        :param full_scope_allowed: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#full_scope_allowed OpenidClient#full_scope_allowed}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#id OpenidClient#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param implicit_flow_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#implicit_flow_enabled OpenidClient#implicit_flow_enabled}.
        :param import_: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#import OpenidClient#import}.
        :param login_theme: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#login_theme OpenidClient#login_theme}.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#name OpenidClient#name}.
        :param oauth2_device_authorization_grant_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#oauth2_device_authorization_grant_enabled OpenidClient#oauth2_device_authorization_grant_enabled}.
        :param oauth2_device_code_lifespan: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#oauth2_device_code_lifespan OpenidClient#oauth2_device_code_lifespan}.
        :param oauth2_device_polling_interval: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#oauth2_device_polling_interval OpenidClient#oauth2_device_polling_interval}.
        :param pkce_code_challenge_method: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#pkce_code_challenge_method OpenidClient#pkce_code_challenge_method}.
        :param root_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#root_url OpenidClient#root_url}.
        :param service_accounts_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#service_accounts_enabled OpenidClient#service_accounts_enabled}.
        :param standard_flow_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#standard_flow_enabled OpenidClient#standard_flow_enabled}.
        :param use_refresh_tokens: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#use_refresh_tokens OpenidClient#use_refresh_tokens}.
        :param use_refresh_tokens_client_credentials: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#use_refresh_tokens_client_credentials OpenidClient#use_refresh_tokens_client_credentials}.
        :param valid_post_logout_redirect_uris: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#valid_post_logout_redirect_uris OpenidClient#valid_post_logout_redirect_uris}.
        :param valid_redirect_uris: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#valid_redirect_uris OpenidClient#valid_redirect_uris}.
        :param web_origins: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#web_origins OpenidClient#web_origins}.
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(authentication_flow_binding_overrides, dict):
            authentication_flow_binding_overrides = (
                OpenidClientAuthenticationFlowBindingOverrides(
                    **authentication_flow_binding_overrides
                )
            )
        if isinstance(authorization, dict):
            authorization = OpenidClientAuthorization(**authorization)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b2aa39420a8e11d38d329cc4d56510afcb7e36b3034204499e9ad6d53c1f9862
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
                argname="argument access_type",
                value=access_type,
                expected_type=type_hints["access_type"],
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
                argname="argument access_token_lifespan",
                value=access_token_lifespan,
                expected_type=type_hints["access_token_lifespan"],
            )
            check_type(
                argname="argument admin_url",
                value=admin_url,
                expected_type=type_hints["admin_url"],
            )
            check_type(
                argname="argument authentication_flow_binding_overrides",
                value=authentication_flow_binding_overrides,
                expected_type=type_hints["authentication_flow_binding_overrides"],
            )
            check_type(
                argname="argument authorization",
                value=authorization,
                expected_type=type_hints["authorization"],
            )
            check_type(
                argname="argument backchannel_logout_revoke_offline_sessions",
                value=backchannel_logout_revoke_offline_sessions,
                expected_type=type_hints["backchannel_logout_revoke_offline_sessions"],
            )
            check_type(
                argname="argument backchannel_logout_session_required",
                value=backchannel_logout_session_required,
                expected_type=type_hints["backchannel_logout_session_required"],
            )
            check_type(
                argname="argument backchannel_logout_url",
                value=backchannel_logout_url,
                expected_type=type_hints["backchannel_logout_url"],
            )
            check_type(
                argname="argument base_url",
                value=base_url,
                expected_type=type_hints["base_url"],
            )
            check_type(
                argname="argument client_authenticator_type",
                value=client_authenticator_type,
                expected_type=type_hints["client_authenticator_type"],
            )
            check_type(
                argname="argument client_offline_session_idle_timeout",
                value=client_offline_session_idle_timeout,
                expected_type=type_hints["client_offline_session_idle_timeout"],
            )
            check_type(
                argname="argument client_offline_session_max_lifespan",
                value=client_offline_session_max_lifespan,
                expected_type=type_hints["client_offline_session_max_lifespan"],
            )
            check_type(
                argname="argument client_secret",
                value=client_secret,
                expected_type=type_hints["client_secret"],
            )
            check_type(
                argname="argument client_session_idle_timeout",
                value=client_session_idle_timeout,
                expected_type=type_hints["client_session_idle_timeout"],
            )
            check_type(
                argname="argument client_session_max_lifespan",
                value=client_session_max_lifespan,
                expected_type=type_hints["client_session_max_lifespan"],
            )
            check_type(
                argname="argument consent_required",
                value=consent_required,
                expected_type=type_hints["consent_required"],
            )
            check_type(
                argname="argument consent_screen_text",
                value=consent_screen_text,
                expected_type=type_hints["consent_screen_text"],
            )
            check_type(
                argname="argument description",
                value=description,
                expected_type=type_hints["description"],
            )
            check_type(
                argname="argument direct_access_grants_enabled",
                value=direct_access_grants_enabled,
                expected_type=type_hints["direct_access_grants_enabled"],
            )
            check_type(
                argname="argument display_on_consent_screen",
                value=display_on_consent_screen,
                expected_type=type_hints["display_on_consent_screen"],
            )
            check_type(
                argname="argument enabled",
                value=enabled,
                expected_type=type_hints["enabled"],
            )
            check_type(
                argname="argument exclude_session_state_from_auth_response",
                value=exclude_session_state_from_auth_response,
                expected_type=type_hints["exclude_session_state_from_auth_response"],
            )
            check_type(
                argname="argument extra_config",
                value=extra_config,
                expected_type=type_hints["extra_config"],
            )
            check_type(
                argname="argument frontchannel_logout_enabled",
                value=frontchannel_logout_enabled,
                expected_type=type_hints["frontchannel_logout_enabled"],
            )
            check_type(
                argname="argument frontchannel_logout_url",
                value=frontchannel_logout_url,
                expected_type=type_hints["frontchannel_logout_url"],
            )
            check_type(
                argname="argument full_scope_allowed",
                value=full_scope_allowed,
                expected_type=type_hints["full_scope_allowed"],
            )
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(
                argname="argument implicit_flow_enabled",
                value=implicit_flow_enabled,
                expected_type=type_hints["implicit_flow_enabled"],
            )
            check_type(
                argname="argument import_",
                value=import_,
                expected_type=type_hints["import_"],
            )
            check_type(
                argname="argument login_theme",
                value=login_theme,
                expected_type=type_hints["login_theme"],
            )
            check_type(
                argname="argument name", value=name, expected_type=type_hints["name"]
            )
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
            check_type(
                argname="argument pkce_code_challenge_method",
                value=pkce_code_challenge_method,
                expected_type=type_hints["pkce_code_challenge_method"],
            )
            check_type(
                argname="argument root_url",
                value=root_url,
                expected_type=type_hints["root_url"],
            )
            check_type(
                argname="argument service_accounts_enabled",
                value=service_accounts_enabled,
                expected_type=type_hints["service_accounts_enabled"],
            )
            check_type(
                argname="argument standard_flow_enabled",
                value=standard_flow_enabled,
                expected_type=type_hints["standard_flow_enabled"],
            )
            check_type(
                argname="argument use_refresh_tokens",
                value=use_refresh_tokens,
                expected_type=type_hints["use_refresh_tokens"],
            )
            check_type(
                argname="argument use_refresh_tokens_client_credentials",
                value=use_refresh_tokens_client_credentials,
                expected_type=type_hints["use_refresh_tokens_client_credentials"],
            )
            check_type(
                argname="argument valid_post_logout_redirect_uris",
                value=valid_post_logout_redirect_uris,
                expected_type=type_hints["valid_post_logout_redirect_uris"],
            )
            check_type(
                argname="argument valid_redirect_uris",
                value=valid_redirect_uris,
                expected_type=type_hints["valid_redirect_uris"],
            )
            check_type(
                argname="argument web_origins",
                value=web_origins,
                expected_type=type_hints["web_origins"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_type": access_type,
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
        if access_token_lifespan is not None:
            self._values["access_token_lifespan"] = access_token_lifespan
        if admin_url is not None:
            self._values["admin_url"] = admin_url
        if authentication_flow_binding_overrides is not None:
            self._values[
                "authentication_flow_binding_overrides"
            ] = authentication_flow_binding_overrides
        if authorization is not None:
            self._values["authorization"] = authorization
        if backchannel_logout_revoke_offline_sessions is not None:
            self._values[
                "backchannel_logout_revoke_offline_sessions"
            ] = backchannel_logout_revoke_offline_sessions
        if backchannel_logout_session_required is not None:
            self._values[
                "backchannel_logout_session_required"
            ] = backchannel_logout_session_required
        if backchannel_logout_url is not None:
            self._values["backchannel_logout_url"] = backchannel_logout_url
        if base_url is not None:
            self._values["base_url"] = base_url
        if client_authenticator_type is not None:
            self._values["client_authenticator_type"] = client_authenticator_type
        if client_offline_session_idle_timeout is not None:
            self._values[
                "client_offline_session_idle_timeout"
            ] = client_offline_session_idle_timeout
        if client_offline_session_max_lifespan is not None:
            self._values[
                "client_offline_session_max_lifespan"
            ] = client_offline_session_max_lifespan
        if client_secret is not None:
            self._values["client_secret"] = client_secret
        if client_session_idle_timeout is not None:
            self._values["client_session_idle_timeout"] = client_session_idle_timeout
        if client_session_max_lifespan is not None:
            self._values["client_session_max_lifespan"] = client_session_max_lifespan
        if consent_required is not None:
            self._values["consent_required"] = consent_required
        if consent_screen_text is not None:
            self._values["consent_screen_text"] = consent_screen_text
        if description is not None:
            self._values["description"] = description
        if direct_access_grants_enabled is not None:
            self._values["direct_access_grants_enabled"] = direct_access_grants_enabled
        if display_on_consent_screen is not None:
            self._values["display_on_consent_screen"] = display_on_consent_screen
        if enabled is not None:
            self._values["enabled"] = enabled
        if exclude_session_state_from_auth_response is not None:
            self._values[
                "exclude_session_state_from_auth_response"
            ] = exclude_session_state_from_auth_response
        if extra_config is not None:
            self._values["extra_config"] = extra_config
        if frontchannel_logout_enabled is not None:
            self._values["frontchannel_logout_enabled"] = frontchannel_logout_enabled
        if frontchannel_logout_url is not None:
            self._values["frontchannel_logout_url"] = frontchannel_logout_url
        if full_scope_allowed is not None:
            self._values["full_scope_allowed"] = full_scope_allowed
        if id is not None:
            self._values["id"] = id
        if implicit_flow_enabled is not None:
            self._values["implicit_flow_enabled"] = implicit_flow_enabled
        if import_ is not None:
            self._values["import_"] = import_
        if login_theme is not None:
            self._values["login_theme"] = login_theme
        if name is not None:
            self._values["name"] = name
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
        if pkce_code_challenge_method is not None:
            self._values["pkce_code_challenge_method"] = pkce_code_challenge_method
        if root_url is not None:
            self._values["root_url"] = root_url
        if service_accounts_enabled is not None:
            self._values["service_accounts_enabled"] = service_accounts_enabled
        if standard_flow_enabled is not None:
            self._values["standard_flow_enabled"] = standard_flow_enabled
        if use_refresh_tokens is not None:
            self._values["use_refresh_tokens"] = use_refresh_tokens
        if use_refresh_tokens_client_credentials is not None:
            self._values[
                "use_refresh_tokens_client_credentials"
            ] = use_refresh_tokens_client_credentials
        if valid_post_logout_redirect_uris is not None:
            self._values[
                "valid_post_logout_redirect_uris"
            ] = valid_post_logout_redirect_uris
        if valid_redirect_uris is not None:
            self._values["valid_redirect_uris"] = valid_redirect_uris
        if web_origins is not None:
            self._values["web_origins"] = web_origins

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
    def access_type(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#access_type OpenidClient#access_type}."""
        result = self._values.get("access_type")
        assert result is not None, "Required property 'access_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_id(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#client_id OpenidClient#client_id}."""
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def realm_id(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#realm_id OpenidClient#realm_id}."""
        result = self._values.get("realm_id")
        assert result is not None, "Required property 'realm_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_token_lifespan(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#access_token_lifespan OpenidClient#access_token_lifespan}."""
        result = self._values.get("access_token_lifespan")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def admin_url(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#admin_url OpenidClient#admin_url}."""
        result = self._values.get("admin_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def authentication_flow_binding_overrides(
        self,
    ) -> typing.Optional[OpenidClientAuthenticationFlowBindingOverrides]:
        """authentication_flow_binding_overrides block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#authentication_flow_binding_overrides OpenidClient#authentication_flow_binding_overrides}
        """
        result = self._values.get("authentication_flow_binding_overrides")
        return typing.cast(
            typing.Optional[OpenidClientAuthenticationFlowBindingOverrides], result
        )

    @builtins.property
    def authorization(self) -> typing.Optional[OpenidClientAuthorization]:
        """authorization block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#authorization OpenidClient#authorization}
        """
        result = self._values.get("authorization")
        return typing.cast(typing.Optional[OpenidClientAuthorization], result)

    @builtins.property
    def backchannel_logout_revoke_offline_sessions(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#backchannel_logout_revoke_offline_sessions OpenidClient#backchannel_logout_revoke_offline_sessions}."""
        result = self._values.get("backchannel_logout_revoke_offline_sessions")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def backchannel_logout_session_required(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#backchannel_logout_session_required OpenidClient#backchannel_logout_session_required}."""
        result = self._values.get("backchannel_logout_session_required")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def backchannel_logout_url(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#backchannel_logout_url OpenidClient#backchannel_logout_url}."""
        result = self._values.get("backchannel_logout_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def base_url(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#base_url OpenidClient#base_url}."""
        result = self._values.get("base_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_authenticator_type(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#client_authenticator_type OpenidClient#client_authenticator_type}."""
        result = self._values.get("client_authenticator_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_offline_session_idle_timeout(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#client_offline_session_idle_timeout OpenidClient#client_offline_session_idle_timeout}."""
        result = self._values.get("client_offline_session_idle_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_offline_session_max_lifespan(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#client_offline_session_max_lifespan OpenidClient#client_offline_session_max_lifespan}."""
        result = self._values.get("client_offline_session_max_lifespan")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_secret(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#client_secret OpenidClient#client_secret}."""
        result = self._values.get("client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_session_idle_timeout(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#client_session_idle_timeout OpenidClient#client_session_idle_timeout}."""
        result = self._values.get("client_session_idle_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_session_max_lifespan(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#client_session_max_lifespan OpenidClient#client_session_max_lifespan}."""
        result = self._values.get("client_session_max_lifespan")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def consent_required(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#consent_required OpenidClient#consent_required}."""
        result = self._values.get("consent_required")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def consent_screen_text(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#consent_screen_text OpenidClient#consent_screen_text}."""
        result = self._values.get("consent_screen_text")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#description OpenidClient#description}."""
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def direct_access_grants_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#direct_access_grants_enabled OpenidClient#direct_access_grants_enabled}."""
        result = self._values.get("direct_access_grants_enabled")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def display_on_consent_screen(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#display_on_consent_screen OpenidClient#display_on_consent_screen}."""
        result = self._values.get("display_on_consent_screen")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#enabled OpenidClient#enabled}."""
        result = self._values.get("enabled")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def exclude_session_state_from_auth_response(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#exclude_session_state_from_auth_response OpenidClient#exclude_session_state_from_auth_response}."""
        result = self._values.get("exclude_session_state_from_auth_response")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def extra_config(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#extra_config OpenidClient#extra_config}."""
        result = self._values.get("extra_config")
        return typing.cast(
            typing.Optional[typing.Mapping[builtins.str, builtins.str]], result
        )

    @builtins.property
    def frontchannel_logout_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#frontchannel_logout_enabled OpenidClient#frontchannel_logout_enabled}."""
        result = self._values.get("frontchannel_logout_enabled")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def frontchannel_logout_url(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#frontchannel_logout_url OpenidClient#frontchannel_logout_url}."""
        result = self._values.get("frontchannel_logout_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def full_scope_allowed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#full_scope_allowed OpenidClient#full_scope_allowed}."""
        result = self._values.get("full_scope_allowed")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#id OpenidClient#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def implicit_flow_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#implicit_flow_enabled OpenidClient#implicit_flow_enabled}."""
        result = self._values.get("implicit_flow_enabled")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def import_(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#import OpenidClient#import}."""
        result = self._values.get("import_")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def login_theme(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#login_theme OpenidClient#login_theme}."""
        result = self._values.get("login_theme")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#name OpenidClient#name}."""
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth2_device_authorization_grant_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#oauth2_device_authorization_grant_enabled OpenidClient#oauth2_device_authorization_grant_enabled}."""
        result = self._values.get("oauth2_device_authorization_grant_enabled")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def oauth2_device_code_lifespan(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#oauth2_device_code_lifespan OpenidClient#oauth2_device_code_lifespan}."""
        result = self._values.get("oauth2_device_code_lifespan")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth2_device_polling_interval(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#oauth2_device_polling_interval OpenidClient#oauth2_device_polling_interval}."""
        result = self._values.get("oauth2_device_polling_interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pkce_code_challenge_method(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#pkce_code_challenge_method OpenidClient#pkce_code_challenge_method}."""
        result = self._values.get("pkce_code_challenge_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def root_url(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#root_url OpenidClient#root_url}."""
        result = self._values.get("root_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_accounts_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#service_accounts_enabled OpenidClient#service_accounts_enabled}."""
        result = self._values.get("service_accounts_enabled")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def standard_flow_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#standard_flow_enabled OpenidClient#standard_flow_enabled}."""
        result = self._values.get("standard_flow_enabled")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def use_refresh_tokens(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#use_refresh_tokens OpenidClient#use_refresh_tokens}."""
        result = self._values.get("use_refresh_tokens")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def use_refresh_tokens_client_credentials(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#use_refresh_tokens_client_credentials OpenidClient#use_refresh_tokens_client_credentials}."""
        result = self._values.get("use_refresh_tokens_client_credentials")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def valid_post_logout_redirect_uris(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#valid_post_logout_redirect_uris OpenidClient#valid_post_logout_redirect_uris}."""
        result = self._values.get("valid_post_logout_redirect_uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def valid_redirect_uris(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#valid_redirect_uris OpenidClient#valid_redirect_uris}."""
        result = self._values.get("valid_redirect_uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def web_origins(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client#web_origins OpenidClient#web_origins}."""
        result = self._values.get("web_origins")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpenidClientConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "OpenidClient",
    "OpenidClientAuthenticationFlowBindingOverrides",
    "OpenidClientAuthenticationFlowBindingOverridesOutputReference",
    "OpenidClientAuthorization",
    "OpenidClientAuthorizationOutputReference",
    "OpenidClientConfig",
]

publication.publish()


def _typecheckingstub__634549952117d7ea9db0cdfc0783c356f24cdaa3377a46d2f39ad23186e866a0(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    access_type: builtins.str,
    client_id: builtins.str,
    realm_id: builtins.str,
    access_token_lifespan: typing.Optional[builtins.str] = None,
    admin_url: typing.Optional[builtins.str] = None,
    authentication_flow_binding_overrides: typing.Optional[
        typing.Union[
            OpenidClientAuthenticationFlowBindingOverrides,
            typing.Dict[builtins.str, typing.Any],
        ]
    ] = None,
    authorization: typing.Optional[
        typing.Union[OpenidClientAuthorization, typing.Dict[builtins.str, typing.Any]]
    ] = None,
    backchannel_logout_revoke_offline_sessions: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    backchannel_logout_session_required: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    backchannel_logout_url: typing.Optional[builtins.str] = None,
    base_url: typing.Optional[builtins.str] = None,
    client_authenticator_type: typing.Optional[builtins.str] = None,
    client_offline_session_idle_timeout: typing.Optional[builtins.str] = None,
    client_offline_session_max_lifespan: typing.Optional[builtins.str] = None,
    client_secret: typing.Optional[builtins.str] = None,
    client_session_idle_timeout: typing.Optional[builtins.str] = None,
    client_session_max_lifespan: typing.Optional[builtins.str] = None,
    consent_required: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    consent_screen_text: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    direct_access_grants_enabled: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    display_on_consent_screen: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    enabled: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    exclude_session_state_from_auth_response: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    extra_config: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    frontchannel_logout_enabled: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    frontchannel_logout_url: typing.Optional[builtins.str] = None,
    full_scope_allowed: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    id: typing.Optional[builtins.str] = None,
    implicit_flow_enabled: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    import_: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    login_theme: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    oauth2_device_authorization_grant_enabled: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    oauth2_device_code_lifespan: typing.Optional[builtins.str] = None,
    oauth2_device_polling_interval: typing.Optional[builtins.str] = None,
    pkce_code_challenge_method: typing.Optional[builtins.str] = None,
    root_url: typing.Optional[builtins.str] = None,
    service_accounts_enabled: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    standard_flow_enabled: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    use_refresh_tokens: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    use_refresh_tokens_client_credentials: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    valid_post_logout_redirect_uris: typing.Optional[
        typing.Sequence[builtins.str]
    ] = None,
    valid_redirect_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
    web_origins: typing.Optional[typing.Sequence[builtins.str]] = None,
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


def _typecheckingstub__1f7e24f3bbaae1708b01d4941d0ce8b2dcd2994a97ef5fda0e9d0e947d511ce6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__67a307c26e2552fc48bea862da4c76c59351341009dce73fb2580f11e9f41bde(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6cdd47d444d5d5d220ae8d50b75a7733ae91c4c15d6a35c4ba22b858df85a5a6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3c8b2bf5768a0a14fb978477486f880d2595202293b7e6da380b5558dd152ce5(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d75d1585f9c18b7af7bd332c5e181b306daac7423a5dda901e99522b8c307b88(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__db2a3a200d15bce74a61808374530a4f30ccfdecf68e906e8fa71214e05235fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a3560b0461d6b7c35214928f4300e5d573f4c4f84ae94255ea55f921b69e21e6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__082d2c9226374d8e92cb0d2760428e684ca1b82cbe10b619adc93f6b56c2c003(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6c272a3d27e6fb2e81ce21e768fb98e333ab45d1a55dbe7a2092783a8f5be3b7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e5846e325b50fb3caa612c448e66462130cdcbcac79dedabb9b872afe15339b2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__41cf4441d5b54e0994965446094ee7c57f6f48c029e1334f086efae01220aafe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6f760c5b50bb1f5d90556f1c2e3ac41f6ed100bd8439ece866071a09906f1288(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__2c91a6132989026c2c06ba7c31c6e14134a211179e7973fa12273c69b05856c7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7de9688a1b7742bab7480c770467ae85e92e847a92cf901ba8b16bd3161481e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__779a8570f4c72fa4fdefbd2b9819c3fe2dc4a91d587d45fc608e0333705ad686(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__be8d53178a33955814bc546da442adc4dba43f839d0c4089223e001707bc8847(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c84831f84fdb3a3605c2e109d5eb369abe7c453023959618d4a72d435a6e5642(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8f7deec0d9b3016e751b2c57ca3ecfe35cff166fa3f9203abbd76df58efc751e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__610075f4af08d3db9754ca2ced3853780a7c9067d2f9023521f2cb7cd006ac62(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ded75aa3172914314ba67b87b5ac7cc773c47d53d88b1b9e3bd372846b2ac37d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__69bb6cd38b6c01df0da6d11f7f6470bcb34251a2e22675c212b75da2b9baa4d7(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__fc545ba780855b5cb93c6d4061fc66482422192341b767caae5678d851ebad00(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b1d5015a2ac2653a696901f900c90ee7fcf23e0b38df3227b813acaea164b2cc(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b8c3695b84acaa4bf76cd199821936b33d321f0b3d5c6b09b1c7b7f2546e60ec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0134873a9e50a1a618b2ace6174fa3aa80e8fd76f24188de6de2d5592f9bc584(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9e335c3c07548af99f990ad410eb07ed368c134ba6fd0cec50da87e9712f7c9d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b8f6d5eedc2ea6576399751af2bcbf5b61a159ec8bbe540ec386707b7601cfef(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a193e3313c2264aad1c986d3dc1ff2aeabd6478cb3998a94272eefe9b4151fc7(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3cb5314364fbae339899526e94f1a17c576a813b2334f43c221eceaa97a976fe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__59da3fa5510d12459f882dcd383b456e792d98c1ea95f062ad69d5f7d3090efd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9ff5e641e930dcc492d30ec9da187113f55cc3f7d249747789ec33bd4d2d0e95(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1fcde79d4dc991edc87b12a3fbbb207a0573572809533d7c5e77cf6162b44c36(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__20d7bb6da8ec7c76a6734b5b81aeec1de877d646246a81f58c561240610391e7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ad6b697b9d36ef958a135d4ad3a2dfe3f2b221628b67132d7a9f340a6acbcdd4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e9a6280f1e2cb13260aed3fa557ca3c6f5600d38eb033d2065ac5473ccfe6ed1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__67d00cce56d515ac75ddb1469e41f3117c72e0a6cf8733bd38af7df92e398b00(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0ba14ed351b0f9a3f090d760b562114359d9411e5b7571db06f5af7d48ed0557(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__796fc44b2c1a5472481009bd6d6eaaad257cd707564004a7eec7b7d24f3e66bb(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9c56992c0cc687f24563a6444b7c318be3e3ca3dde65bcda6860a6bc71a0a305(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c89fe7d8e0a78ac0fec3d62f1a99bea86231be0d4ecf0cd3e51e798d7b001edc(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0a3873f2ac0be44e474dadb41ca19e27d7431fd53ea4cef24ece3f361bb87593(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4a2e5d87738ad8ba9b5c3de1643eeca3a8383a3de7e8d189cba7e3e0d1f18386(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3439274c89f2b0efd03243a0d0eb6b4ec281ec9233bbdb1f055736d7e14b8532(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d099d158e8c0e1a4b793fc7d1ad3f9d2658d772bcde4a5fb346f314ad8e3c0ea(
    *,
    browser_id: typing.Optional[builtins.str] = None,
    direct_grant_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__272281f75bc70268e972fc3b335377b81764c3c5d7ef29692a643a1e5dfd5615(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__842b6eecf134f01c5dcb6dd8bc4e087d92cf696de550e5a5f5c5eb2a1e67401e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9345a5cc6a85f39c4fa2e51befc32e39e422561c685709a9bfb7abc1a63670eb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__72c115a179fa7a1f110cbc8799826d0a97acc010de0275b6911d72759713ec17(
    value: typing.Optional[OpenidClientAuthenticationFlowBindingOverrides],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__eb33dd10a48afb782a9e67e47174e40f5fa8a1d019fdf273454451ef26dfb744(
    *,
    policy_enforcement_mode: builtins.str,
    allow_remote_resource_management: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    decision_strategy: typing.Optional[builtins.str] = None,
    keep_defaults: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__82ce42e9317106653675d487554ee6499f657f1eed34a0606c9af30c16eb6962(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6cc83925456eb366db06e981946e34710dd791f177b8406b552fbe5d835659ee(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e119a3b242582379cb1898694f244ec16c4cd7a6b270eb47541ca30d95ecd3ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__be706a5c1596f5a76cc54743da1b0dd1bbbf45ef6fe396b0b76473ad146e7d30(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9f204b2cdcdd7813a9e8004765b3f286f612ded887954ccc831e27e24e65240a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ada659dd5b9dc309443e6fc2ab70af5a260f2ca6a69ffcd0a2fcf81af7c8001b(
    value: typing.Optional[OpenidClientAuthorization],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b2aa39420a8e11d38d329cc4d56510afcb7e36b3034204499e9ad6d53c1f9862(
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
    access_type: builtins.str,
    client_id: builtins.str,
    realm_id: builtins.str,
    access_token_lifespan: typing.Optional[builtins.str] = None,
    admin_url: typing.Optional[builtins.str] = None,
    authentication_flow_binding_overrides: typing.Optional[
        typing.Union[
            OpenidClientAuthenticationFlowBindingOverrides,
            typing.Dict[builtins.str, typing.Any],
        ]
    ] = None,
    authorization: typing.Optional[
        typing.Union[OpenidClientAuthorization, typing.Dict[builtins.str, typing.Any]]
    ] = None,
    backchannel_logout_revoke_offline_sessions: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    backchannel_logout_session_required: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    backchannel_logout_url: typing.Optional[builtins.str] = None,
    base_url: typing.Optional[builtins.str] = None,
    client_authenticator_type: typing.Optional[builtins.str] = None,
    client_offline_session_idle_timeout: typing.Optional[builtins.str] = None,
    client_offline_session_max_lifespan: typing.Optional[builtins.str] = None,
    client_secret: typing.Optional[builtins.str] = None,
    client_session_idle_timeout: typing.Optional[builtins.str] = None,
    client_session_max_lifespan: typing.Optional[builtins.str] = None,
    consent_required: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    consent_screen_text: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    direct_access_grants_enabled: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    display_on_consent_screen: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    enabled: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    exclude_session_state_from_auth_response: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    extra_config: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    frontchannel_logout_enabled: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    frontchannel_logout_url: typing.Optional[builtins.str] = None,
    full_scope_allowed: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    id: typing.Optional[builtins.str] = None,
    implicit_flow_enabled: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    import_: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    login_theme: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    oauth2_device_authorization_grant_enabled: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    oauth2_device_code_lifespan: typing.Optional[builtins.str] = None,
    oauth2_device_polling_interval: typing.Optional[builtins.str] = None,
    pkce_code_challenge_method: typing.Optional[builtins.str] = None,
    root_url: typing.Optional[builtins.str] = None,
    service_accounts_enabled: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    standard_flow_enabled: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    use_refresh_tokens: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    use_refresh_tokens_client_credentials: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    valid_post_logout_redirect_uris: typing.Optional[
        typing.Sequence[builtins.str]
    ] = None,
    valid_redirect_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
    web_origins: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
