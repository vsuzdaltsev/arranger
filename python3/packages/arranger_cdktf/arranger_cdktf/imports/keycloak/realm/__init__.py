"""
# `keycloak_realm`

Refer to the Terraform Registory for docs: [`keycloak_realm`](https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm).
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


class Realm(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.realm.Realm",
):
    """Represents a {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm keycloak_realm}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        realm: builtins.str,
        access_code_lifespan: typing.Optional[builtins.str] = None,
        access_code_lifespan_login: typing.Optional[builtins.str] = None,
        access_code_lifespan_user_action: typing.Optional[builtins.str] = None,
        access_token_lifespan: typing.Optional[builtins.str] = None,
        access_token_lifespan_for_implicit_flow: typing.Optional[builtins.str] = None,
        account_theme: typing.Optional[builtins.str] = None,
        action_token_generated_by_admin_lifespan: typing.Optional[builtins.str] = None,
        action_token_generated_by_user_lifespan: typing.Optional[builtins.str] = None,
        admin_theme: typing.Optional[builtins.str] = None,
        attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        browser_flow: typing.Optional[builtins.str] = None,
        client_authentication_flow: typing.Optional[builtins.str] = None,
        client_session_idle_timeout: typing.Optional[builtins.str] = None,
        client_session_max_lifespan: typing.Optional[builtins.str] = None,
        default_default_client_scopes: typing.Optional[
            typing.Sequence[builtins.str]
        ] = None,
        default_optional_client_scopes: typing.Optional[
            typing.Sequence[builtins.str]
        ] = None,
        default_signature_algorithm: typing.Optional[builtins.str] = None,
        direct_grant_flow: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        display_name_html: typing.Optional[builtins.str] = None,
        docker_authentication_flow: typing.Optional[builtins.str] = None,
        duplicate_emails_allowed: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        edit_username_allowed: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        email_theme: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        id: typing.Optional[builtins.str] = None,
        internal_id: typing.Optional[builtins.str] = None,
        internationalization: typing.Optional[
            typing.Union[
                "RealmInternationalization", typing.Dict[builtins.str, typing.Any]
            ]
        ] = None,
        login_theme: typing.Optional[builtins.str] = None,
        login_with_email_allowed: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        oauth2_device_code_lifespan: typing.Optional[builtins.str] = None,
        oauth2_device_polling_interval: typing.Optional[jsii.Number] = None,
        offline_session_idle_timeout: typing.Optional[builtins.str] = None,
        offline_session_max_lifespan: typing.Optional[builtins.str] = None,
        offline_session_max_lifespan_enabled: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        otp_policy: typing.Optional[
            typing.Union["RealmOtpPolicy", typing.Dict[builtins.str, typing.Any]]
        ] = None,
        password_policy: typing.Optional[builtins.str] = None,
        refresh_token_max_reuse: typing.Optional[jsii.Number] = None,
        registration_allowed: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        registration_email_as_username: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        registration_flow: typing.Optional[builtins.str] = None,
        remember_me: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        reset_credentials_flow: typing.Optional[builtins.str] = None,
        reset_password_allowed: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        revoke_refresh_token: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        security_defenses: typing.Optional[
            typing.Union["RealmSecurityDefenses", typing.Dict[builtins.str, typing.Any]]
        ] = None,
        smtp_server: typing.Optional[
            typing.Union["RealmSmtpServer", typing.Dict[builtins.str, typing.Any]]
        ] = None,
        ssl_required: typing.Optional[builtins.str] = None,
        sso_session_idle_timeout: typing.Optional[builtins.str] = None,
        sso_session_idle_timeout_remember_me: typing.Optional[builtins.str] = None,
        sso_session_max_lifespan: typing.Optional[builtins.str] = None,
        sso_session_max_lifespan_remember_me: typing.Optional[builtins.str] = None,
        user_managed_access: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        verify_email: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        web_authn_passwordless_policy: typing.Optional[
            typing.Union[
                "RealmWebAuthnPasswordlessPolicy", typing.Dict[builtins.str, typing.Any]
            ]
        ] = None,
        web_authn_policy: typing.Optional[
            typing.Union["RealmWebAuthnPolicy", typing.Dict[builtins.str, typing.Any]]
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
        """Create a new {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm keycloak_realm} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param realm: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#realm Realm#realm}.
        :param access_code_lifespan: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#access_code_lifespan Realm#access_code_lifespan}.
        :param access_code_lifespan_login: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#access_code_lifespan_login Realm#access_code_lifespan_login}.
        :param access_code_lifespan_user_action: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#access_code_lifespan_user_action Realm#access_code_lifespan_user_action}.
        :param access_token_lifespan: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#access_token_lifespan Realm#access_token_lifespan}.
        :param access_token_lifespan_for_implicit_flow: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#access_token_lifespan_for_implicit_flow Realm#access_token_lifespan_for_implicit_flow}.
        :param account_theme: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#account_theme Realm#account_theme}.
        :param action_token_generated_by_admin_lifespan: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#action_token_generated_by_admin_lifespan Realm#action_token_generated_by_admin_lifespan}.
        :param action_token_generated_by_user_lifespan: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#action_token_generated_by_user_lifespan Realm#action_token_generated_by_user_lifespan}.
        :param admin_theme: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#admin_theme Realm#admin_theme}.
        :param attributes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#attributes Realm#attributes}.
        :param browser_flow: Which flow should be used for BrowserFlow. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#browser_flow Realm#browser_flow}
        :param client_authentication_flow: Which flow should be used for ClientAuthenticationFlow. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#client_authentication_flow Realm#client_authentication_flow}
        :param client_session_idle_timeout: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#client_session_idle_timeout Realm#client_session_idle_timeout}.
        :param client_session_max_lifespan: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#client_session_max_lifespan Realm#client_session_max_lifespan}.
        :param default_default_client_scopes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#default_default_client_scopes Realm#default_default_client_scopes}.
        :param default_optional_client_scopes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#default_optional_client_scopes Realm#default_optional_client_scopes}.
        :param default_signature_algorithm: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#default_signature_algorithm Realm#default_signature_algorithm}.
        :param direct_grant_flow: Which flow should be used for DirectGrantFlow. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#direct_grant_flow Realm#direct_grant_flow}
        :param display_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#display_name Realm#display_name}.
        :param display_name_html: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#display_name_html Realm#display_name_html}.
        :param docker_authentication_flow: Which flow should be used for DockerAuthenticationFlow. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#docker_authentication_flow Realm#docker_authentication_flow}
        :param duplicate_emails_allowed: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#duplicate_emails_allowed Realm#duplicate_emails_allowed}.
        :param edit_username_allowed: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#edit_username_allowed Realm#edit_username_allowed}.
        :param email_theme: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#email_theme Realm#email_theme}.
        :param enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#enabled Realm#enabled}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#id Realm#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param internal_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#internal_id Realm#internal_id}.
        :param internationalization: internationalization block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#internationalization Realm#internationalization}
        :param login_theme: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#login_theme Realm#login_theme}.
        :param login_with_email_allowed: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#login_with_email_allowed Realm#login_with_email_allowed}.
        :param oauth2_device_code_lifespan: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#oauth2_device_code_lifespan Realm#oauth2_device_code_lifespan}.
        :param oauth2_device_polling_interval: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#oauth2_device_polling_interval Realm#oauth2_device_polling_interval}.
        :param offline_session_idle_timeout: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#offline_session_idle_timeout Realm#offline_session_idle_timeout}.
        :param offline_session_max_lifespan: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#offline_session_max_lifespan Realm#offline_session_max_lifespan}.
        :param offline_session_max_lifespan_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#offline_session_max_lifespan_enabled Realm#offline_session_max_lifespan_enabled}.
        :param otp_policy: otp_policy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#otp_policy Realm#otp_policy}
        :param password_policy: String that represents the passwordPolicies that are in place. Each policy is separated with " and ". Supported policies can be found in the server-info providers page. example: "upperCase(1) and length(8) and forceExpiredPasswordChange(365) and notUsername(undefined)" Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#password_policy Realm#password_policy}
        :param refresh_token_max_reuse: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#refresh_token_max_reuse Realm#refresh_token_max_reuse}.
        :param registration_allowed: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#registration_allowed Realm#registration_allowed}.
        :param registration_email_as_username: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#registration_email_as_username Realm#registration_email_as_username}.
        :param registration_flow: Which flow should be used for RegistrationFlow. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#registration_flow Realm#registration_flow}
        :param remember_me: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#remember_me Realm#remember_me}.
        :param reset_credentials_flow: Which flow should be used for ResetCredentialsFlow. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#reset_credentials_flow Realm#reset_credentials_flow}
        :param reset_password_allowed: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#reset_password_allowed Realm#reset_password_allowed}.
        :param revoke_refresh_token: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#revoke_refresh_token Realm#revoke_refresh_token}.
        :param security_defenses: security_defenses block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#security_defenses Realm#security_defenses}
        :param smtp_server: smtp_server block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#smtp_server Realm#smtp_server}
        :param ssl_required: SSL Required: Values can be 'none', 'external' or 'all'. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#ssl_required Realm#ssl_required}
        :param sso_session_idle_timeout: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#sso_session_idle_timeout Realm#sso_session_idle_timeout}.
        :param sso_session_idle_timeout_remember_me: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#sso_session_idle_timeout_remember_me Realm#sso_session_idle_timeout_remember_me}.
        :param sso_session_max_lifespan: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#sso_session_max_lifespan Realm#sso_session_max_lifespan}.
        :param sso_session_max_lifespan_remember_me: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#sso_session_max_lifespan_remember_me Realm#sso_session_max_lifespan_remember_me}.
        :param user_managed_access: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#user_managed_access Realm#user_managed_access}.
        :param verify_email: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#verify_email Realm#verify_email}.
        :param web_authn_passwordless_policy: web_authn_passwordless_policy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#web_authn_passwordless_policy Realm#web_authn_passwordless_policy}
        :param web_authn_policy: web_authn_policy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#web_authn_policy Realm#web_authn_policy}
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
                _typecheckingstub__3884c9ca449eb14a5003cf4a9e6dd8be906cad1cc4bce9dc8927112aab746bff
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(
                argname="argument id_", value=id_, expected_type=type_hints["id_"]
            )
        config = RealmConfig(
            realm=realm,
            access_code_lifespan=access_code_lifespan,
            access_code_lifespan_login=access_code_lifespan_login,
            access_code_lifespan_user_action=access_code_lifespan_user_action,
            access_token_lifespan=access_token_lifespan,
            access_token_lifespan_for_implicit_flow=access_token_lifespan_for_implicit_flow,
            account_theme=account_theme,
            action_token_generated_by_admin_lifespan=action_token_generated_by_admin_lifespan,
            action_token_generated_by_user_lifespan=action_token_generated_by_user_lifespan,
            admin_theme=admin_theme,
            attributes=attributes,
            browser_flow=browser_flow,
            client_authentication_flow=client_authentication_flow,
            client_session_idle_timeout=client_session_idle_timeout,
            client_session_max_lifespan=client_session_max_lifespan,
            default_default_client_scopes=default_default_client_scopes,
            default_optional_client_scopes=default_optional_client_scopes,
            default_signature_algorithm=default_signature_algorithm,
            direct_grant_flow=direct_grant_flow,
            display_name=display_name,
            display_name_html=display_name_html,
            docker_authentication_flow=docker_authentication_flow,
            duplicate_emails_allowed=duplicate_emails_allowed,
            edit_username_allowed=edit_username_allowed,
            email_theme=email_theme,
            enabled=enabled,
            id=id,
            internal_id=internal_id,
            internationalization=internationalization,
            login_theme=login_theme,
            login_with_email_allowed=login_with_email_allowed,
            oauth2_device_code_lifespan=oauth2_device_code_lifespan,
            oauth2_device_polling_interval=oauth2_device_polling_interval,
            offline_session_idle_timeout=offline_session_idle_timeout,
            offline_session_max_lifespan=offline_session_max_lifespan,
            offline_session_max_lifespan_enabled=offline_session_max_lifespan_enabled,
            otp_policy=otp_policy,
            password_policy=password_policy,
            refresh_token_max_reuse=refresh_token_max_reuse,
            registration_allowed=registration_allowed,
            registration_email_as_username=registration_email_as_username,
            registration_flow=registration_flow,
            remember_me=remember_me,
            reset_credentials_flow=reset_credentials_flow,
            reset_password_allowed=reset_password_allowed,
            revoke_refresh_token=revoke_refresh_token,
            security_defenses=security_defenses,
            smtp_server=smtp_server,
            ssl_required=ssl_required,
            sso_session_idle_timeout=sso_session_idle_timeout,
            sso_session_idle_timeout_remember_me=sso_session_idle_timeout_remember_me,
            sso_session_max_lifespan=sso_session_max_lifespan,
            sso_session_max_lifespan_remember_me=sso_session_max_lifespan_remember_me,
            user_managed_access=user_managed_access,
            verify_email=verify_email,
            web_authn_passwordless_policy=web_authn_passwordless_policy,
            web_authn_policy=web_authn_policy,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putInternationalization")
    def put_internationalization(
        self,
        *,
        default_locale: builtins.str,
        supported_locales: typing.Sequence[builtins.str],
    ) -> None:
        """
        :param default_locale: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#default_locale Realm#default_locale}.
        :param supported_locales: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#supported_locales Realm#supported_locales}.
        """
        value = RealmInternationalization(
            default_locale=default_locale, supported_locales=supported_locales
        )

        return typing.cast(None, jsii.invoke(self, "putInternationalization", [value]))

    @jsii.member(jsii_name="putOtpPolicy")
    def put_otp_policy(
        self,
        *,
        algorithm: typing.Optional[builtins.str] = None,
        digits: typing.Optional[jsii.Number] = None,
        initial_counter: typing.Optional[jsii.Number] = None,
        look_ahead_window: typing.Optional[jsii.Number] = None,
        period: typing.Optional[jsii.Number] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param algorithm: What hashing algorithm should be used to generate the OTP. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#algorithm Realm#algorithm}
        :param digits: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#digits Realm#digits}.
        :param initial_counter: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#initial_counter Realm#initial_counter}.
        :param look_ahead_window: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#look_ahead_window Realm#look_ahead_window}.
        :param period: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#period Realm#period}.
        :param type: OTP Type, totp for Time-Based One Time Password or hotp for counter base one time password. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#type Realm#type}
        """
        value = RealmOtpPolicy(
            algorithm=algorithm,
            digits=digits,
            initial_counter=initial_counter,
            look_ahead_window=look_ahead_window,
            period=period,
            type=type,
        )

        return typing.cast(None, jsii.invoke(self, "putOtpPolicy", [value]))

    @jsii.member(jsii_name="putSecurityDefenses")
    def put_security_defenses(
        self,
        *,
        brute_force_detection: typing.Optional[
            typing.Union[
                "RealmSecurityDefensesBruteForceDetection",
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        headers: typing.Optional[
            typing.Union[
                "RealmSecurityDefensesHeaders", typing.Dict[builtins.str, typing.Any]
            ]
        ] = None,
    ) -> None:
        """
        :param brute_force_detection: brute_force_detection block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#brute_force_detection Realm#brute_force_detection}
        :param headers: headers block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#headers Realm#headers}
        """
        value = RealmSecurityDefenses(
            brute_force_detection=brute_force_detection, headers=headers
        )

        return typing.cast(None, jsii.invoke(self, "putSecurityDefenses", [value]))

    @jsii.member(jsii_name="putSmtpServer")
    def put_smtp_server(
        self,
        *,
        from_: builtins.str,
        host: builtins.str,
        auth: typing.Optional[
            typing.Union["RealmSmtpServerAuth", typing.Dict[builtins.str, typing.Any]]
        ] = None,
        envelope_from: typing.Optional[builtins.str] = None,
        from_display_name: typing.Optional[builtins.str] = None,
        port: typing.Optional[builtins.str] = None,
        reply_to: typing.Optional[builtins.str] = None,
        reply_to_display_name: typing.Optional[builtins.str] = None,
        ssl: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        starttls: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
    ) -> None:
        """
        :param from_: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#from Realm#from}.
        :param host: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#host Realm#host}.
        :param auth: auth block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#auth Realm#auth}
        :param envelope_from: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#envelope_from Realm#envelope_from}.
        :param from_display_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#from_display_name Realm#from_display_name}.
        :param port: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#port Realm#port}.
        :param reply_to: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#reply_to Realm#reply_to}.
        :param reply_to_display_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#reply_to_display_name Realm#reply_to_display_name}.
        :param ssl: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#ssl Realm#ssl}.
        :param starttls: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#starttls Realm#starttls}.
        """
        value = RealmSmtpServer(
            from_=from_,
            host=host,
            auth=auth,
            envelope_from=envelope_from,
            from_display_name=from_display_name,
            port=port,
            reply_to=reply_to,
            reply_to_display_name=reply_to_display_name,
            ssl=ssl,
            starttls=starttls,
        )

        return typing.cast(None, jsii.invoke(self, "putSmtpServer", [value]))

    @jsii.member(jsii_name="putWebAuthnPasswordlessPolicy")
    def put_web_authn_passwordless_policy(
        self,
        *,
        acceptable_aaguids: typing.Optional[typing.Sequence[builtins.str]] = None,
        attestation_conveyance_preference: typing.Optional[builtins.str] = None,
        authenticator_attachment: typing.Optional[builtins.str] = None,
        avoid_same_authenticator_register: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        create_timeout: typing.Optional[jsii.Number] = None,
        relying_party_entity_name: typing.Optional[builtins.str] = None,
        relying_party_id: typing.Optional[builtins.str] = None,
        require_resident_key: typing.Optional[builtins.str] = None,
        signature_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        user_verification_requirement: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param acceptable_aaguids: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#acceptable_aaguids Realm#acceptable_aaguids}.
        :param attestation_conveyance_preference: Either none, indirect or direct. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#attestation_conveyance_preference Realm#attestation_conveyance_preference}
        :param authenticator_attachment: Either platform or cross-platform. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#authenticator_attachment Realm#authenticator_attachment}
        :param avoid_same_authenticator_register: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#avoid_same_authenticator_register Realm#avoid_same_authenticator_register}.
        :param create_timeout: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#create_timeout Realm#create_timeout}.
        :param relying_party_entity_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#relying_party_entity_name Realm#relying_party_entity_name}.
        :param relying_party_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#relying_party_id Realm#relying_party_id}.
        :param require_resident_key: Either Yes or No. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#require_resident_key Realm#require_resident_key}
        :param signature_algorithms: Keycloak lists ES256, ES384, ES512, RS256, RS384, RS512, RS1 at the time of writing. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#signature_algorithms Realm#signature_algorithms}
        :param user_verification_requirement: Either required, preferred or discouraged. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#user_verification_requirement Realm#user_verification_requirement}
        """
        value = RealmWebAuthnPasswordlessPolicy(
            acceptable_aaguids=acceptable_aaguids,
            attestation_conveyance_preference=attestation_conveyance_preference,
            authenticator_attachment=authenticator_attachment,
            avoid_same_authenticator_register=avoid_same_authenticator_register,
            create_timeout=create_timeout,
            relying_party_entity_name=relying_party_entity_name,
            relying_party_id=relying_party_id,
            require_resident_key=require_resident_key,
            signature_algorithms=signature_algorithms,
            user_verification_requirement=user_verification_requirement,
        )

        return typing.cast(
            None, jsii.invoke(self, "putWebAuthnPasswordlessPolicy", [value])
        )

    @jsii.member(jsii_name="putWebAuthnPolicy")
    def put_web_authn_policy(
        self,
        *,
        acceptable_aaguids: typing.Optional[typing.Sequence[builtins.str]] = None,
        attestation_conveyance_preference: typing.Optional[builtins.str] = None,
        authenticator_attachment: typing.Optional[builtins.str] = None,
        avoid_same_authenticator_register: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        create_timeout: typing.Optional[jsii.Number] = None,
        relying_party_entity_name: typing.Optional[builtins.str] = None,
        relying_party_id: typing.Optional[builtins.str] = None,
        require_resident_key: typing.Optional[builtins.str] = None,
        signature_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        user_verification_requirement: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param acceptable_aaguids: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#acceptable_aaguids Realm#acceptable_aaguids}.
        :param attestation_conveyance_preference: Either none, indirect or direct. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#attestation_conveyance_preference Realm#attestation_conveyance_preference}
        :param authenticator_attachment: Either platform or cross-platform. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#authenticator_attachment Realm#authenticator_attachment}
        :param avoid_same_authenticator_register: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#avoid_same_authenticator_register Realm#avoid_same_authenticator_register}.
        :param create_timeout: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#create_timeout Realm#create_timeout}.
        :param relying_party_entity_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#relying_party_entity_name Realm#relying_party_entity_name}.
        :param relying_party_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#relying_party_id Realm#relying_party_id}.
        :param require_resident_key: Either Yes or No. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#require_resident_key Realm#require_resident_key}
        :param signature_algorithms: Keycloak lists ES256, ES384, ES512, RS256, RS384, RS512, RS1 at the time of writing. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#signature_algorithms Realm#signature_algorithms}
        :param user_verification_requirement: Either required, preferred or discouraged. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#user_verification_requirement Realm#user_verification_requirement}
        """
        value = RealmWebAuthnPolicy(
            acceptable_aaguids=acceptable_aaguids,
            attestation_conveyance_preference=attestation_conveyance_preference,
            authenticator_attachment=authenticator_attachment,
            avoid_same_authenticator_register=avoid_same_authenticator_register,
            create_timeout=create_timeout,
            relying_party_entity_name=relying_party_entity_name,
            relying_party_id=relying_party_id,
            require_resident_key=require_resident_key,
            signature_algorithms=signature_algorithms,
            user_verification_requirement=user_verification_requirement,
        )

        return typing.cast(None, jsii.invoke(self, "putWebAuthnPolicy", [value]))

    @jsii.member(jsii_name="resetAccessCodeLifespan")
    def reset_access_code_lifespan(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessCodeLifespan", []))

    @jsii.member(jsii_name="resetAccessCodeLifespanLogin")
    def reset_access_code_lifespan_login(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessCodeLifespanLogin", []))

    @jsii.member(jsii_name="resetAccessCodeLifespanUserAction")
    def reset_access_code_lifespan_user_action(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetAccessCodeLifespanUserAction", [])
        )

    @jsii.member(jsii_name="resetAccessTokenLifespan")
    def reset_access_token_lifespan(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessTokenLifespan", []))

    @jsii.member(jsii_name="resetAccessTokenLifespanForImplicitFlow")
    def reset_access_token_lifespan_for_implicit_flow(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetAccessTokenLifespanForImplicitFlow", [])
        )

    @jsii.member(jsii_name="resetAccountTheme")
    def reset_account_theme(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountTheme", []))

    @jsii.member(jsii_name="resetActionTokenGeneratedByAdminLifespan")
    def reset_action_token_generated_by_admin_lifespan(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetActionTokenGeneratedByAdminLifespan", [])
        )

    @jsii.member(jsii_name="resetActionTokenGeneratedByUserLifespan")
    def reset_action_token_generated_by_user_lifespan(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetActionTokenGeneratedByUserLifespan", [])
        )

    @jsii.member(jsii_name="resetAdminTheme")
    def reset_admin_theme(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdminTheme", []))

    @jsii.member(jsii_name="resetAttributes")
    def reset_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttributes", []))

    @jsii.member(jsii_name="resetBrowserFlow")
    def reset_browser_flow(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBrowserFlow", []))

    @jsii.member(jsii_name="resetClientAuthenticationFlow")
    def reset_client_authentication_flow(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientAuthenticationFlow", []))

    @jsii.member(jsii_name="resetClientSessionIdleTimeout")
    def reset_client_session_idle_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientSessionIdleTimeout", []))

    @jsii.member(jsii_name="resetClientSessionMaxLifespan")
    def reset_client_session_max_lifespan(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientSessionMaxLifespan", []))

    @jsii.member(jsii_name="resetDefaultDefaultClientScopes")
    def reset_default_default_client_scopes(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetDefaultDefaultClientScopes", [])
        )

    @jsii.member(jsii_name="resetDefaultOptionalClientScopes")
    def reset_default_optional_client_scopes(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetDefaultOptionalClientScopes", [])
        )

    @jsii.member(jsii_name="resetDefaultSignatureAlgorithm")
    def reset_default_signature_algorithm(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetDefaultSignatureAlgorithm", [])
        )

    @jsii.member(jsii_name="resetDirectGrantFlow")
    def reset_direct_grant_flow(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDirectGrantFlow", []))

    @jsii.member(jsii_name="resetDisplayName")
    def reset_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayName", []))

    @jsii.member(jsii_name="resetDisplayNameHtml")
    def reset_display_name_html(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayNameHtml", []))

    @jsii.member(jsii_name="resetDockerAuthenticationFlow")
    def reset_docker_authentication_flow(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDockerAuthenticationFlow", []))

    @jsii.member(jsii_name="resetDuplicateEmailsAllowed")
    def reset_duplicate_emails_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDuplicateEmailsAllowed", []))

    @jsii.member(jsii_name="resetEditUsernameAllowed")
    def reset_edit_username_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEditUsernameAllowed", []))

    @jsii.member(jsii_name="resetEmailTheme")
    def reset_email_theme(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailTheme", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInternalId")
    def reset_internal_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInternalId", []))

    @jsii.member(jsii_name="resetInternationalization")
    def reset_internationalization(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInternationalization", []))

    @jsii.member(jsii_name="resetLoginTheme")
    def reset_login_theme(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoginTheme", []))

    @jsii.member(jsii_name="resetLoginWithEmailAllowed")
    def reset_login_with_email_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoginWithEmailAllowed", []))

    @jsii.member(jsii_name="resetOauth2DeviceCodeLifespan")
    def reset_oauth2_device_code_lifespan(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOauth2DeviceCodeLifespan", []))

    @jsii.member(jsii_name="resetOauth2DevicePollingInterval")
    def reset_oauth2_device_polling_interval(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetOauth2DevicePollingInterval", [])
        )

    @jsii.member(jsii_name="resetOfflineSessionIdleTimeout")
    def reset_offline_session_idle_timeout(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetOfflineSessionIdleTimeout", [])
        )

    @jsii.member(jsii_name="resetOfflineSessionMaxLifespan")
    def reset_offline_session_max_lifespan(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetOfflineSessionMaxLifespan", [])
        )

    @jsii.member(jsii_name="resetOfflineSessionMaxLifespanEnabled")
    def reset_offline_session_max_lifespan_enabled(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetOfflineSessionMaxLifespanEnabled", [])
        )

    @jsii.member(jsii_name="resetOtpPolicy")
    def reset_otp_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOtpPolicy", []))

    @jsii.member(jsii_name="resetPasswordPolicy")
    def reset_password_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPasswordPolicy", []))

    @jsii.member(jsii_name="resetRefreshTokenMaxReuse")
    def reset_refresh_token_max_reuse(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRefreshTokenMaxReuse", []))

    @jsii.member(jsii_name="resetRegistrationAllowed")
    def reset_registration_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegistrationAllowed", []))

    @jsii.member(jsii_name="resetRegistrationEmailAsUsername")
    def reset_registration_email_as_username(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetRegistrationEmailAsUsername", [])
        )

    @jsii.member(jsii_name="resetRegistrationFlow")
    def reset_registration_flow(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegistrationFlow", []))

    @jsii.member(jsii_name="resetRememberMe")
    def reset_remember_me(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRememberMe", []))

    @jsii.member(jsii_name="resetResetCredentialsFlow")
    def reset_reset_credentials_flow(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResetCredentialsFlow", []))

    @jsii.member(jsii_name="resetResetPasswordAllowed")
    def reset_reset_password_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResetPasswordAllowed", []))

    @jsii.member(jsii_name="resetRevokeRefreshToken")
    def reset_revoke_refresh_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRevokeRefreshToken", []))

    @jsii.member(jsii_name="resetSecurityDefenses")
    def reset_security_defenses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityDefenses", []))

    @jsii.member(jsii_name="resetSmtpServer")
    def reset_smtp_server(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSmtpServer", []))

    @jsii.member(jsii_name="resetSslRequired")
    def reset_ssl_required(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslRequired", []))

    @jsii.member(jsii_name="resetSsoSessionIdleTimeout")
    def reset_sso_session_idle_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSsoSessionIdleTimeout", []))

    @jsii.member(jsii_name="resetSsoSessionIdleTimeoutRememberMe")
    def reset_sso_session_idle_timeout_remember_me(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetSsoSessionIdleTimeoutRememberMe", [])
        )

    @jsii.member(jsii_name="resetSsoSessionMaxLifespan")
    def reset_sso_session_max_lifespan(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSsoSessionMaxLifespan", []))

    @jsii.member(jsii_name="resetSsoSessionMaxLifespanRememberMe")
    def reset_sso_session_max_lifespan_remember_me(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetSsoSessionMaxLifespanRememberMe", [])
        )

    @jsii.member(jsii_name="resetUserManagedAccess")
    def reset_user_managed_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserManagedAccess", []))

    @jsii.member(jsii_name="resetVerifyEmail")
    def reset_verify_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVerifyEmail", []))

    @jsii.member(jsii_name="resetWebAuthnPasswordlessPolicy")
    def reset_web_authn_passwordless_policy(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetWebAuthnPasswordlessPolicy", [])
        )

    @jsii.member(jsii_name="resetWebAuthnPolicy")
    def reset_web_authn_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebAuthnPolicy", []))

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
    @jsii.member(jsii_name="internationalization")
    def internationalization(self) -> "RealmInternationalizationOutputReference":
        return typing.cast(
            "RealmInternationalizationOutputReference",
            jsii.get(self, "internationalization"),
        )

    @builtins.property
    @jsii.member(jsii_name="otpPolicy")
    def otp_policy(self) -> "RealmOtpPolicyOutputReference":
        return typing.cast("RealmOtpPolicyOutputReference", jsii.get(self, "otpPolicy"))

    @builtins.property
    @jsii.member(jsii_name="securityDefenses")
    def security_defenses(self) -> "RealmSecurityDefensesOutputReference":
        return typing.cast(
            "RealmSecurityDefensesOutputReference", jsii.get(self, "securityDefenses")
        )

    @builtins.property
    @jsii.member(jsii_name="smtpServer")
    def smtp_server(self) -> "RealmSmtpServerOutputReference":
        return typing.cast(
            "RealmSmtpServerOutputReference", jsii.get(self, "smtpServer")
        )

    @builtins.property
    @jsii.member(jsii_name="webAuthnPasswordlessPolicy")
    def web_authn_passwordless_policy(
        self,
    ) -> "RealmWebAuthnPasswordlessPolicyOutputReference":
        return typing.cast(
            "RealmWebAuthnPasswordlessPolicyOutputReference",
            jsii.get(self, "webAuthnPasswordlessPolicy"),
        )

    @builtins.property
    @jsii.member(jsii_name="webAuthnPolicy")
    def web_authn_policy(self) -> "RealmWebAuthnPolicyOutputReference":
        return typing.cast(
            "RealmWebAuthnPolicyOutputReference", jsii.get(self, "webAuthnPolicy")
        )

    @builtins.property
    @jsii.member(jsii_name="accessCodeLifespanInput")
    def access_code_lifespan_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "accessCodeLifespanInput")
        )

    @builtins.property
    @jsii.member(jsii_name="accessCodeLifespanLoginInput")
    def access_code_lifespan_login_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "accessCodeLifespanLoginInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="accessCodeLifespanUserActionInput")
    def access_code_lifespan_user_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "accessCodeLifespanUserActionInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="accessTokenLifespanForImplicitFlowInput")
    def access_token_lifespan_for_implicit_flow_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "accessTokenLifespanForImplicitFlowInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="accessTokenLifespanInput")
    def access_token_lifespan_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "accessTokenLifespanInput")
        )

    @builtins.property
    @jsii.member(jsii_name="accountThemeInput")
    def account_theme_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "accountThemeInput")
        )

    @builtins.property
    @jsii.member(jsii_name="actionTokenGeneratedByAdminLifespanInput")
    def action_token_generated_by_admin_lifespan_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "actionTokenGeneratedByAdminLifespanInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="actionTokenGeneratedByUserLifespanInput")
    def action_token_generated_by_user_lifespan_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "actionTokenGeneratedByUserLifespanInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="adminThemeInput")
    def admin_theme_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "adminThemeInput")
        )

    @builtins.property
    @jsii.member(jsii_name="attributesInput")
    def attributes_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(
            typing.Optional[typing.Mapping[builtins.str, builtins.str]],
            jsii.get(self, "attributesInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="browserFlowInput")
    def browser_flow_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "browserFlowInput")
        )

    @builtins.property
    @jsii.member(jsii_name="clientAuthenticationFlowInput")
    def client_authentication_flow_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "clientAuthenticationFlowInput"),
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
    @jsii.member(jsii_name="defaultDefaultClientScopesInput")
    def default_default_client_scopes_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]],
            jsii.get(self, "defaultDefaultClientScopesInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="defaultOptionalClientScopesInput")
    def default_optional_client_scopes_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]],
            jsii.get(self, "defaultOptionalClientScopesInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="defaultSignatureAlgorithmInput")
    def default_signature_algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "defaultSignatureAlgorithmInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="directGrantFlowInput")
    def direct_grant_flow_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "directGrantFlowInput")
        )

    @builtins.property
    @jsii.member(jsii_name="displayNameHtmlInput")
    def display_name_html_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "displayNameHtmlInput")
        )

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "displayNameInput")
        )

    @builtins.property
    @jsii.member(jsii_name="dockerAuthenticationFlowInput")
    def docker_authentication_flow_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "dockerAuthenticationFlowInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="duplicateEmailsAllowedInput")
    def duplicate_emails_allowed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "duplicateEmailsAllowedInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="editUsernameAllowedInput")
    def edit_username_allowed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "editUsernameAllowedInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="emailThemeInput")
    def email_theme_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "emailThemeInput")
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
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="internalIdInput")
    def internal_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "internalIdInput")
        )

    @builtins.property
    @jsii.member(jsii_name="internationalizationInput")
    def internationalization_input(
        self,
    ) -> typing.Optional["RealmInternationalization"]:
        return typing.cast(
            typing.Optional["RealmInternationalization"],
            jsii.get(self, "internationalizationInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="loginThemeInput")
    def login_theme_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "loginThemeInput")
        )

    @builtins.property
    @jsii.member(jsii_name="loginWithEmailAllowedInput")
    def login_with_email_allowed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "loginWithEmailAllowedInput"),
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
    def oauth2_device_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(
            typing.Optional[jsii.Number],
            jsii.get(self, "oauth2DevicePollingIntervalInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="offlineSessionIdleTimeoutInput")
    def offline_session_idle_timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "offlineSessionIdleTimeoutInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="offlineSessionMaxLifespanEnabledInput")
    def offline_session_max_lifespan_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "offlineSessionMaxLifespanEnabledInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="offlineSessionMaxLifespanInput")
    def offline_session_max_lifespan_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "offlineSessionMaxLifespanInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="otpPolicyInput")
    def otp_policy_input(self) -> typing.Optional["RealmOtpPolicy"]:
        return typing.cast(
            typing.Optional["RealmOtpPolicy"], jsii.get(self, "otpPolicyInput")
        )

    @builtins.property
    @jsii.member(jsii_name="passwordPolicyInput")
    def password_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "passwordPolicyInput")
        )

    @builtins.property
    @jsii.member(jsii_name="realmInput")
    def realm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "realmInput"))

    @builtins.property
    @jsii.member(jsii_name="refreshTokenMaxReuseInput")
    def refresh_token_max_reuse_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(
            typing.Optional[jsii.Number], jsii.get(self, "refreshTokenMaxReuseInput")
        )

    @builtins.property
    @jsii.member(jsii_name="registrationAllowedInput")
    def registration_allowed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "registrationAllowedInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="registrationEmailAsUsernameInput")
    def registration_email_as_username_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "registrationEmailAsUsernameInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="registrationFlowInput")
    def registration_flow_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "registrationFlowInput")
        )

    @builtins.property
    @jsii.member(jsii_name="rememberMeInput")
    def remember_me_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "rememberMeInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="resetCredentialsFlowInput")
    def reset_credentials_flow_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "resetCredentialsFlowInput")
        )

    @builtins.property
    @jsii.member(jsii_name="resetPasswordAllowedInput")
    def reset_password_allowed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "resetPasswordAllowedInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="revokeRefreshTokenInput")
    def revoke_refresh_token_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "revokeRefreshTokenInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="securityDefensesInput")
    def security_defenses_input(self) -> typing.Optional["RealmSecurityDefenses"]:
        return typing.cast(
            typing.Optional["RealmSecurityDefenses"],
            jsii.get(self, "securityDefensesInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="smtpServerInput")
    def smtp_server_input(self) -> typing.Optional["RealmSmtpServer"]:
        return typing.cast(
            typing.Optional["RealmSmtpServer"], jsii.get(self, "smtpServerInput")
        )

    @builtins.property
    @jsii.member(jsii_name="sslRequiredInput")
    def ssl_required_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "sslRequiredInput")
        )

    @builtins.property
    @jsii.member(jsii_name="ssoSessionIdleTimeoutInput")
    def sso_session_idle_timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "ssoSessionIdleTimeoutInput")
        )

    @builtins.property
    @jsii.member(jsii_name="ssoSessionIdleTimeoutRememberMeInput")
    def sso_session_idle_timeout_remember_me_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "ssoSessionIdleTimeoutRememberMeInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="ssoSessionMaxLifespanInput")
    def sso_session_max_lifespan_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "ssoSessionMaxLifespanInput")
        )

    @builtins.property
    @jsii.member(jsii_name="ssoSessionMaxLifespanRememberMeInput")
    def sso_session_max_lifespan_remember_me_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "ssoSessionMaxLifespanRememberMeInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="userManagedAccessInput")
    def user_managed_access_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "userManagedAccessInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="verifyEmailInput")
    def verify_email_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "verifyEmailInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="webAuthnPasswordlessPolicyInput")
    def web_authn_passwordless_policy_input(
        self,
    ) -> typing.Optional["RealmWebAuthnPasswordlessPolicy"]:
        return typing.cast(
            typing.Optional["RealmWebAuthnPasswordlessPolicy"],
            jsii.get(self, "webAuthnPasswordlessPolicyInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="webAuthnPolicyInput")
    def web_authn_policy_input(self) -> typing.Optional["RealmWebAuthnPolicy"]:
        return typing.cast(
            typing.Optional["RealmWebAuthnPolicy"],
            jsii.get(self, "webAuthnPolicyInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="accessCodeLifespan")
    def access_code_lifespan(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessCodeLifespan"))

    @access_code_lifespan.setter
    def access_code_lifespan(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__4efff962e4bd300f374e414a220e9d866949f903bca2e248ac330ef95bdaebfe
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "accessCodeLifespan", value)

    @builtins.property
    @jsii.member(jsii_name="accessCodeLifespanLogin")
    def access_code_lifespan_login(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessCodeLifespanLogin"))

    @access_code_lifespan_login.setter
    def access_code_lifespan_login(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__86e316ca73cd9630d38187e69d67cd95e11cf4a1e77d5de54c71d9b17e2d3bc7
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "accessCodeLifespanLogin", value)

    @builtins.property
    @jsii.member(jsii_name="accessCodeLifespanUserAction")
    def access_code_lifespan_user_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessCodeLifespanUserAction"))

    @access_code_lifespan_user_action.setter
    def access_code_lifespan_user_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__ec9320a12ae161db794450a3921ec2efabaf1a43cd5388ef666d332c621ed876
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "accessCodeLifespanUserAction", value)

    @builtins.property
    @jsii.member(jsii_name="accessTokenLifespan")
    def access_token_lifespan(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessTokenLifespan"))

    @access_token_lifespan.setter
    def access_token_lifespan(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d5ec6b81495fd42e38b2c2fb0bfdf6ea441333b905f996f8e24a0aada769da2c
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "accessTokenLifespan", value)

    @builtins.property
    @jsii.member(jsii_name="accessTokenLifespanForImplicitFlow")
    def access_token_lifespan_for_implicit_flow(self) -> builtins.str:
        return typing.cast(
            builtins.str, jsii.get(self, "accessTokenLifespanForImplicitFlow")
        )

    @access_token_lifespan_for_implicit_flow.setter
    def access_token_lifespan_for_implicit_flow(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__db4ee232a0635d41812a7d5c35ae9ab0e005ed62826004b46c0e93fc62f225eb
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "accessTokenLifespanForImplicitFlow", value)

    @builtins.property
    @jsii.member(jsii_name="accountTheme")
    def account_theme(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountTheme"))

    @account_theme.setter
    def account_theme(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b83590f5078715338f047a5b6dd38a8a06994070b4d90dbb7b602cc540176c1d
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "accountTheme", value)

    @builtins.property
    @jsii.member(jsii_name="actionTokenGeneratedByAdminLifespan")
    def action_token_generated_by_admin_lifespan(self) -> builtins.str:
        return typing.cast(
            builtins.str, jsii.get(self, "actionTokenGeneratedByAdminLifespan")
        )

    @action_token_generated_by_admin_lifespan.setter
    def action_token_generated_by_admin_lifespan(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__47f68b1d0bc4a48746793c9152307b61e626a993e81cde2262c8478869ceea75
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "actionTokenGeneratedByAdminLifespan", value)

    @builtins.property
    @jsii.member(jsii_name="actionTokenGeneratedByUserLifespan")
    def action_token_generated_by_user_lifespan(self) -> builtins.str:
        return typing.cast(
            builtins.str, jsii.get(self, "actionTokenGeneratedByUserLifespan")
        )

    @action_token_generated_by_user_lifespan.setter
    def action_token_generated_by_user_lifespan(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a7b44e8dd5cdac65963743fba935a4b904d2446995792e28852035da7c0e18a4
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "actionTokenGeneratedByUserLifespan", value)

    @builtins.property
    @jsii.member(jsii_name="adminTheme")
    def admin_theme(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adminTheme"))

    @admin_theme.setter
    def admin_theme(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__2a4fd3f52a8d5f0296d732c68e62e19fd3718bca08032ced2a32954501c4f91f
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "adminTheme", value)

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(
            typing.Mapping[builtins.str, builtins.str], jsii.get(self, "attributes")
        )

    @attributes.setter
    def attributes(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__e1b3cb4b6cda8d217ec50331f039a2e8082024f76ebfd7f82ac6ca5fe790a5af
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "attributes", value)

    @builtins.property
    @jsii.member(jsii_name="browserFlow")
    def browser_flow(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "browserFlow"))

    @browser_flow.setter
    def browser_flow(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d9b45f952efc5f43c46890bcc417f4f50aae588e97886317ff6db60707b9376c
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "browserFlow", value)

    @builtins.property
    @jsii.member(jsii_name="clientAuthenticationFlow")
    def client_authentication_flow(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientAuthenticationFlow"))

    @client_authentication_flow.setter
    def client_authentication_flow(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__fb9259639782ba4f95809a3b43467fe3669a8077384ee4f622668d3e7fcdd801
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "clientAuthenticationFlow", value)

    @builtins.property
    @jsii.member(jsii_name="clientSessionIdleTimeout")
    def client_session_idle_timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSessionIdleTimeout"))

    @client_session_idle_timeout.setter
    def client_session_idle_timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b671e68bdc74504f61f72c63dc2895eda0e901cfb173c5c9dfd7364e7383ad11
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
                _typecheckingstub__391a826fefc8eaf8a4aced7d829f2899fff625bf2a305df859a8701447ad6e9c
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "clientSessionMaxLifespan", value)

    @builtins.property
    @jsii.member(jsii_name="defaultDefaultClientScopes")
    def default_default_client_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(
            typing.List[builtins.str], jsii.get(self, "defaultDefaultClientScopes")
        )

    @default_default_client_scopes.setter
    def default_default_client_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d26a828a4c4d30f00392d9208746de7dc26f09a8cb48f174b90434fba969106c
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "defaultDefaultClientScopes", value)

    @builtins.property
    @jsii.member(jsii_name="defaultOptionalClientScopes")
    def default_optional_client_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(
            typing.List[builtins.str], jsii.get(self, "defaultOptionalClientScopes")
        )

    @default_optional_client_scopes.setter
    def default_optional_client_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__8015412d14543cfc1494322d20f962dee3b491bc36dd2cbdf8ece717b7ef1e7e
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "defaultOptionalClientScopes", value)

    @builtins.property
    @jsii.member(jsii_name="defaultSignatureAlgorithm")
    def default_signature_algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultSignatureAlgorithm"))

    @default_signature_algorithm.setter
    def default_signature_algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__db2c4f995dc204d42c1416213895f9a8b739f0750757438e2e95b6f355d560b1
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "defaultSignatureAlgorithm", value)

    @builtins.property
    @jsii.member(jsii_name="directGrantFlow")
    def direct_grant_flow(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directGrantFlow"))

    @direct_grant_flow.setter
    def direct_grant_flow(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__5a780941836b54d3fd9557a7cf6377c7ce206babbd72edbbd45d84b21512337f
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "directGrantFlow", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__bdcc88b646f345f19db9b382d600d62b3ccfc70a2ed47372119bbfb67f688f9c
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="displayNameHtml")
    def display_name_html(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayNameHtml"))

    @display_name_html.setter
    def display_name_html(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__80789a7175c3ec01c637bb3a7952156c6db63b5199cbe9a1aa92d2b8bfe59935
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "displayNameHtml", value)

    @builtins.property
    @jsii.member(jsii_name="dockerAuthenticationFlow")
    def docker_authentication_flow(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dockerAuthenticationFlow"))

    @docker_authentication_flow.setter
    def docker_authentication_flow(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__29ef7d9b2e4f1a93c4b917ce928e7328570f89eb82b6ea7a1a88e18f6e9d9243
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "dockerAuthenticationFlow", value)

    @builtins.property
    @jsii.member(jsii_name="duplicateEmailsAllowed")
    def duplicate_emails_allowed(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "duplicateEmailsAllowed"),
        )

    @duplicate_emails_allowed.setter
    def duplicate_emails_allowed(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a26862e4a2007c2c1e0316b7ce79ad2a02fa112feed9ef3e882a6ce72e424756
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "duplicateEmailsAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="editUsernameAllowed")
    def edit_username_allowed(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "editUsernameAllowed"),
        )

    @edit_username_allowed.setter
    def edit_username_allowed(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__caa421a139755aeb9c8975d5d324b1ead9d2b73f959dce9845b772ddd2275bb0
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "editUsernameAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="emailTheme")
    def email_theme(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emailTheme"))

    @email_theme.setter
    def email_theme(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__3dabdd7b04eaf76bdb10de9c7603523681d25f90faec63f7f6f326ed42399672
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "emailTheme", value)

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
                _typecheckingstub__60b55c532ab0a8770d0b03a6bcb226f956d74c8c2a06266a052f6e17f15b4d77
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d4773891b72ecc0d05c2713e857ddcb8b3c8912c55cb1525faf39360961b08c9
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="internalId")
    def internal_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "internalId"))

    @internal_id.setter
    def internal_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b160919c6b300e9b23e6aefeb7a5a93c131505f31cdc0207ca769d258a52bfa1
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalId", value)

    @builtins.property
    @jsii.member(jsii_name="loginTheme")
    def login_theme(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loginTheme"))

    @login_theme.setter
    def login_theme(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__3a423024e3c28e3333258ba58cd26fae5bcf8e416207e21d40dc1113c92958c5
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "loginTheme", value)

    @builtins.property
    @jsii.member(jsii_name="loginWithEmailAllowed")
    def login_with_email_allowed(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "loginWithEmailAllowed"),
        )

    @login_with_email_allowed.setter
    def login_with_email_allowed(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__3573a19e26ea0f2d1b94269ce06afc13117ea6790053b316ddd4709b9a022257
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "loginWithEmailAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="oauth2DeviceCodeLifespan")
    def oauth2_device_code_lifespan(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oauth2DeviceCodeLifespan"))

    @oauth2_device_code_lifespan.setter
    def oauth2_device_code_lifespan(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d66bc4eba8def70dd798430e5c8a162c575ad5fc6ff03c28bde2aac8c6f1a202
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "oauth2DeviceCodeLifespan", value)

    @builtins.property
    @jsii.member(jsii_name="oauth2DevicePollingInterval")
    def oauth2_device_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "oauth2DevicePollingInterval"))

    @oauth2_device_polling_interval.setter
    def oauth2_device_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__071b008188bc5347eec40ca8552bf64586f5b5fadeab0b5e9c0349757e752f3b
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "oauth2DevicePollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="offlineSessionIdleTimeout")
    def offline_session_idle_timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "offlineSessionIdleTimeout"))

    @offline_session_idle_timeout.setter
    def offline_session_idle_timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a778fcb47fbba7095b9894be5fbb8a41cefb396d0c8f04e635d3b78f8ba8b5b5
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "offlineSessionIdleTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="offlineSessionMaxLifespan")
    def offline_session_max_lifespan(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "offlineSessionMaxLifespan"))

    @offline_session_max_lifespan.setter
    def offline_session_max_lifespan(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d6632f60953ec77de327b82fc8e2558299b55451b5174ded8784c0b59b0a6f79
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "offlineSessionMaxLifespan", value)

    @builtins.property
    @jsii.member(jsii_name="offlineSessionMaxLifespanEnabled")
    def offline_session_max_lifespan_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "offlineSessionMaxLifespanEnabled"),
        )

    @offline_session_max_lifespan_enabled.setter
    def offline_session_max_lifespan_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__7b66b1a999513e1630443529ab2cd80c6ae73606c4d14bc514818a58f1ec716e
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "offlineSessionMaxLifespanEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="passwordPolicy")
    def password_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "passwordPolicy"))

    @password_policy.setter
    def password_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d8c02a71cc8b4f38d86d88d09240feecdae71c26f0ff04ced2491a67c6ba8558
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "passwordPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="realm")
    def realm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "realm"))

    @realm.setter
    def realm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__2c8aad4a7e393c01bef949b1a5e7909fae6a35e328dd0762757826268792b9b8
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "realm", value)

    @builtins.property
    @jsii.member(jsii_name="refreshTokenMaxReuse")
    def refresh_token_max_reuse(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "refreshTokenMaxReuse"))

    @refresh_token_max_reuse.setter
    def refresh_token_max_reuse(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__494523c218ae47b190e3443e34fd6c7a6bc91a03965bb1a9cc0305ddf37154ae
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "refreshTokenMaxReuse", value)

    @builtins.property
    @jsii.member(jsii_name="registrationAllowed")
    def registration_allowed(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "registrationAllowed"),
        )

    @registration_allowed.setter
    def registration_allowed(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__29346830421cb5a106f84d810ed52aec6f25b7d11a366b316afcf38f4a8dd086
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "registrationAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="registrationEmailAsUsername")
    def registration_email_as_username(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "registrationEmailAsUsername"),
        )

    @registration_email_as_username.setter
    def registration_email_as_username(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__62afce0efa55d2cea1123911b06ca8c64ad28bd47d25d0ae63573218e391f2a6
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "registrationEmailAsUsername", value)

    @builtins.property
    @jsii.member(jsii_name="registrationFlow")
    def registration_flow(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "registrationFlow"))

    @registration_flow.setter
    def registration_flow(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__2e09dbcca9be5ea274fd0b8d40908be00ff6ced221b0bbd040a5fcb38059b390
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "registrationFlow", value)

    @builtins.property
    @jsii.member(jsii_name="rememberMe")
    def remember_me(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "rememberMe"),
        )

    @remember_me.setter
    def remember_me(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__daa614f5432bb09427b0f97ad3e7272708534a11b6f4a2d6a89e00c84dae1985
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "rememberMe", value)

    @builtins.property
    @jsii.member(jsii_name="resetCredentialsFlow")
    def reset_credentials_flow(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resetCredentialsFlow"))

    @reset_credentials_flow.setter
    def reset_credentials_flow(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__248e0c9aade6ee6a877068d57935f2a9802e873ce9c8b55c2c6c6c3acfda3e01
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "resetCredentialsFlow", value)

    @builtins.property
    @jsii.member(jsii_name="resetPasswordAllowed")
    def reset_password_allowed(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "resetPasswordAllowed"),
        )

    @reset_password_allowed.setter
    def reset_password_allowed(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__bf69e0f0b12a90dc2a50116c58849d86acad201d92a22e51d729a5f755901e8a
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "resetPasswordAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="revokeRefreshToken")
    def revoke_refresh_token(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "revokeRefreshToken"),
        )

    @revoke_refresh_token.setter
    def revoke_refresh_token(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__f51a8645decd8f777be02ffe9b32beb76758818168c1a76d835a12c76e6b72ac
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "revokeRefreshToken", value)

    @builtins.property
    @jsii.member(jsii_name="sslRequired")
    def ssl_required(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslRequired"))

    @ssl_required.setter
    def ssl_required(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__550a66edbf13bb4be7b8f4279b3e3d6eb95b2d79ab2c416216b2d4007bed3da7
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "sslRequired", value)

    @builtins.property
    @jsii.member(jsii_name="ssoSessionIdleTimeout")
    def sso_session_idle_timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ssoSessionIdleTimeout"))

    @sso_session_idle_timeout.setter
    def sso_session_idle_timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__0cc04ba50537f9687df4b40ea30ef0bb92f275d2b610aab08e1670169d0e9490
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "ssoSessionIdleTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="ssoSessionIdleTimeoutRememberMe")
    def sso_session_idle_timeout_remember_me(self) -> builtins.str:
        return typing.cast(
            builtins.str, jsii.get(self, "ssoSessionIdleTimeoutRememberMe")
        )

    @sso_session_idle_timeout_remember_me.setter
    def sso_session_idle_timeout_remember_me(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__7fd08b9cfebdad9aa94805b012ed9ae17625536e27c5b2589a41862ae232ecf0
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "ssoSessionIdleTimeoutRememberMe", value)

    @builtins.property
    @jsii.member(jsii_name="ssoSessionMaxLifespan")
    def sso_session_max_lifespan(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ssoSessionMaxLifespan"))

    @sso_session_max_lifespan.setter
    def sso_session_max_lifespan(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__511a507599a9c1e044fd95b9f31b71579b29c3202556991c67f75543d64bca6b
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "ssoSessionMaxLifespan", value)

    @builtins.property
    @jsii.member(jsii_name="ssoSessionMaxLifespanRememberMe")
    def sso_session_max_lifespan_remember_me(self) -> builtins.str:
        return typing.cast(
            builtins.str, jsii.get(self, "ssoSessionMaxLifespanRememberMe")
        )

    @sso_session_max_lifespan_remember_me.setter
    def sso_session_max_lifespan_remember_me(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__dc6978ae6cfe8c776bd581acd4b7c9f3dfc25f41152e7941f01d2e2125520da0
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "ssoSessionMaxLifespanRememberMe", value)

    @builtins.property
    @jsii.member(jsii_name="userManagedAccess")
    def user_managed_access(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "userManagedAccess"),
        )

    @user_managed_access.setter
    def user_managed_access(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__1de33be22bcec879f3ba3d72f715d4748381e0632e812857f61f1ab864c3d7ac
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "userManagedAccess", value)

    @builtins.property
    @jsii.member(jsii_name="verifyEmail")
    def verify_email(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "verifyEmail"),
        )

    @verify_email.setter
    def verify_email(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__9d97db664249b19e0087c1e8b9b4dab4e90760e5d1fe0189e12b58042c2570d6
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "verifyEmail", value)


@jsii.data_type(
    jsii_type="keycloak.realm.RealmConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "realm": "realm",
        "access_code_lifespan": "accessCodeLifespan",
        "access_code_lifespan_login": "accessCodeLifespanLogin",
        "access_code_lifespan_user_action": "accessCodeLifespanUserAction",
        "access_token_lifespan": "accessTokenLifespan",
        "access_token_lifespan_for_implicit_flow": "accessTokenLifespanForImplicitFlow",
        "account_theme": "accountTheme",
        "action_token_generated_by_admin_lifespan": "actionTokenGeneratedByAdminLifespan",
        "action_token_generated_by_user_lifespan": "actionTokenGeneratedByUserLifespan",
        "admin_theme": "adminTheme",
        "attributes": "attributes",
        "browser_flow": "browserFlow",
        "client_authentication_flow": "clientAuthenticationFlow",
        "client_session_idle_timeout": "clientSessionIdleTimeout",
        "client_session_max_lifespan": "clientSessionMaxLifespan",
        "default_default_client_scopes": "defaultDefaultClientScopes",
        "default_optional_client_scopes": "defaultOptionalClientScopes",
        "default_signature_algorithm": "defaultSignatureAlgorithm",
        "direct_grant_flow": "directGrantFlow",
        "display_name": "displayName",
        "display_name_html": "displayNameHtml",
        "docker_authentication_flow": "dockerAuthenticationFlow",
        "duplicate_emails_allowed": "duplicateEmailsAllowed",
        "edit_username_allowed": "editUsernameAllowed",
        "email_theme": "emailTheme",
        "enabled": "enabled",
        "id": "id",
        "internal_id": "internalId",
        "internationalization": "internationalization",
        "login_theme": "loginTheme",
        "login_with_email_allowed": "loginWithEmailAllowed",
        "oauth2_device_code_lifespan": "oauth2DeviceCodeLifespan",
        "oauth2_device_polling_interval": "oauth2DevicePollingInterval",
        "offline_session_idle_timeout": "offlineSessionIdleTimeout",
        "offline_session_max_lifespan": "offlineSessionMaxLifespan",
        "offline_session_max_lifespan_enabled": "offlineSessionMaxLifespanEnabled",
        "otp_policy": "otpPolicy",
        "password_policy": "passwordPolicy",
        "refresh_token_max_reuse": "refreshTokenMaxReuse",
        "registration_allowed": "registrationAllowed",
        "registration_email_as_username": "registrationEmailAsUsername",
        "registration_flow": "registrationFlow",
        "remember_me": "rememberMe",
        "reset_credentials_flow": "resetCredentialsFlow",
        "reset_password_allowed": "resetPasswordAllowed",
        "revoke_refresh_token": "revokeRefreshToken",
        "security_defenses": "securityDefenses",
        "smtp_server": "smtpServer",
        "ssl_required": "sslRequired",
        "sso_session_idle_timeout": "ssoSessionIdleTimeout",
        "sso_session_idle_timeout_remember_me": "ssoSessionIdleTimeoutRememberMe",
        "sso_session_max_lifespan": "ssoSessionMaxLifespan",
        "sso_session_max_lifespan_remember_me": "ssoSessionMaxLifespanRememberMe",
        "user_managed_access": "userManagedAccess",
        "verify_email": "verifyEmail",
        "web_authn_passwordless_policy": "webAuthnPasswordlessPolicy",
        "web_authn_policy": "webAuthnPolicy",
    },
)
class RealmConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        realm: builtins.str,
        access_code_lifespan: typing.Optional[builtins.str] = None,
        access_code_lifespan_login: typing.Optional[builtins.str] = None,
        access_code_lifespan_user_action: typing.Optional[builtins.str] = None,
        access_token_lifespan: typing.Optional[builtins.str] = None,
        access_token_lifespan_for_implicit_flow: typing.Optional[builtins.str] = None,
        account_theme: typing.Optional[builtins.str] = None,
        action_token_generated_by_admin_lifespan: typing.Optional[builtins.str] = None,
        action_token_generated_by_user_lifespan: typing.Optional[builtins.str] = None,
        admin_theme: typing.Optional[builtins.str] = None,
        attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        browser_flow: typing.Optional[builtins.str] = None,
        client_authentication_flow: typing.Optional[builtins.str] = None,
        client_session_idle_timeout: typing.Optional[builtins.str] = None,
        client_session_max_lifespan: typing.Optional[builtins.str] = None,
        default_default_client_scopes: typing.Optional[
            typing.Sequence[builtins.str]
        ] = None,
        default_optional_client_scopes: typing.Optional[
            typing.Sequence[builtins.str]
        ] = None,
        default_signature_algorithm: typing.Optional[builtins.str] = None,
        direct_grant_flow: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        display_name_html: typing.Optional[builtins.str] = None,
        docker_authentication_flow: typing.Optional[builtins.str] = None,
        duplicate_emails_allowed: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        edit_username_allowed: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        email_theme: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        id: typing.Optional[builtins.str] = None,
        internal_id: typing.Optional[builtins.str] = None,
        internationalization: typing.Optional[
            typing.Union[
                "RealmInternationalization", typing.Dict[builtins.str, typing.Any]
            ]
        ] = None,
        login_theme: typing.Optional[builtins.str] = None,
        login_with_email_allowed: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        oauth2_device_code_lifespan: typing.Optional[builtins.str] = None,
        oauth2_device_polling_interval: typing.Optional[jsii.Number] = None,
        offline_session_idle_timeout: typing.Optional[builtins.str] = None,
        offline_session_max_lifespan: typing.Optional[builtins.str] = None,
        offline_session_max_lifespan_enabled: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        otp_policy: typing.Optional[
            typing.Union["RealmOtpPolicy", typing.Dict[builtins.str, typing.Any]]
        ] = None,
        password_policy: typing.Optional[builtins.str] = None,
        refresh_token_max_reuse: typing.Optional[jsii.Number] = None,
        registration_allowed: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        registration_email_as_username: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        registration_flow: typing.Optional[builtins.str] = None,
        remember_me: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        reset_credentials_flow: typing.Optional[builtins.str] = None,
        reset_password_allowed: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        revoke_refresh_token: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        security_defenses: typing.Optional[
            typing.Union["RealmSecurityDefenses", typing.Dict[builtins.str, typing.Any]]
        ] = None,
        smtp_server: typing.Optional[
            typing.Union["RealmSmtpServer", typing.Dict[builtins.str, typing.Any]]
        ] = None,
        ssl_required: typing.Optional[builtins.str] = None,
        sso_session_idle_timeout: typing.Optional[builtins.str] = None,
        sso_session_idle_timeout_remember_me: typing.Optional[builtins.str] = None,
        sso_session_max_lifespan: typing.Optional[builtins.str] = None,
        sso_session_max_lifespan_remember_me: typing.Optional[builtins.str] = None,
        user_managed_access: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        verify_email: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        web_authn_passwordless_policy: typing.Optional[
            typing.Union[
                "RealmWebAuthnPasswordlessPolicy", typing.Dict[builtins.str, typing.Any]
            ]
        ] = None,
        web_authn_policy: typing.Optional[
            typing.Union["RealmWebAuthnPolicy", typing.Dict[builtins.str, typing.Any]]
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
        :param realm: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#realm Realm#realm}.
        :param access_code_lifespan: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#access_code_lifespan Realm#access_code_lifespan}.
        :param access_code_lifespan_login: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#access_code_lifespan_login Realm#access_code_lifespan_login}.
        :param access_code_lifespan_user_action: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#access_code_lifespan_user_action Realm#access_code_lifespan_user_action}.
        :param access_token_lifespan: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#access_token_lifespan Realm#access_token_lifespan}.
        :param access_token_lifespan_for_implicit_flow: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#access_token_lifespan_for_implicit_flow Realm#access_token_lifespan_for_implicit_flow}.
        :param account_theme: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#account_theme Realm#account_theme}.
        :param action_token_generated_by_admin_lifespan: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#action_token_generated_by_admin_lifespan Realm#action_token_generated_by_admin_lifespan}.
        :param action_token_generated_by_user_lifespan: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#action_token_generated_by_user_lifespan Realm#action_token_generated_by_user_lifespan}.
        :param admin_theme: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#admin_theme Realm#admin_theme}.
        :param attributes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#attributes Realm#attributes}.
        :param browser_flow: Which flow should be used for BrowserFlow. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#browser_flow Realm#browser_flow}
        :param client_authentication_flow: Which flow should be used for ClientAuthenticationFlow. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#client_authentication_flow Realm#client_authentication_flow}
        :param client_session_idle_timeout: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#client_session_idle_timeout Realm#client_session_idle_timeout}.
        :param client_session_max_lifespan: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#client_session_max_lifespan Realm#client_session_max_lifespan}.
        :param default_default_client_scopes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#default_default_client_scopes Realm#default_default_client_scopes}.
        :param default_optional_client_scopes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#default_optional_client_scopes Realm#default_optional_client_scopes}.
        :param default_signature_algorithm: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#default_signature_algorithm Realm#default_signature_algorithm}.
        :param direct_grant_flow: Which flow should be used for DirectGrantFlow. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#direct_grant_flow Realm#direct_grant_flow}
        :param display_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#display_name Realm#display_name}.
        :param display_name_html: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#display_name_html Realm#display_name_html}.
        :param docker_authentication_flow: Which flow should be used for DockerAuthenticationFlow. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#docker_authentication_flow Realm#docker_authentication_flow}
        :param duplicate_emails_allowed: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#duplicate_emails_allowed Realm#duplicate_emails_allowed}.
        :param edit_username_allowed: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#edit_username_allowed Realm#edit_username_allowed}.
        :param email_theme: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#email_theme Realm#email_theme}.
        :param enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#enabled Realm#enabled}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#id Realm#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param internal_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#internal_id Realm#internal_id}.
        :param internationalization: internationalization block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#internationalization Realm#internationalization}
        :param login_theme: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#login_theme Realm#login_theme}.
        :param login_with_email_allowed: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#login_with_email_allowed Realm#login_with_email_allowed}.
        :param oauth2_device_code_lifespan: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#oauth2_device_code_lifespan Realm#oauth2_device_code_lifespan}.
        :param oauth2_device_polling_interval: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#oauth2_device_polling_interval Realm#oauth2_device_polling_interval}.
        :param offline_session_idle_timeout: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#offline_session_idle_timeout Realm#offline_session_idle_timeout}.
        :param offline_session_max_lifespan: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#offline_session_max_lifespan Realm#offline_session_max_lifespan}.
        :param offline_session_max_lifespan_enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#offline_session_max_lifespan_enabled Realm#offline_session_max_lifespan_enabled}.
        :param otp_policy: otp_policy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#otp_policy Realm#otp_policy}
        :param password_policy: String that represents the passwordPolicies that are in place. Each policy is separated with " and ". Supported policies can be found in the server-info providers page. example: "upperCase(1) and length(8) and forceExpiredPasswordChange(365) and notUsername(undefined)" Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#password_policy Realm#password_policy}
        :param refresh_token_max_reuse: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#refresh_token_max_reuse Realm#refresh_token_max_reuse}.
        :param registration_allowed: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#registration_allowed Realm#registration_allowed}.
        :param registration_email_as_username: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#registration_email_as_username Realm#registration_email_as_username}.
        :param registration_flow: Which flow should be used for RegistrationFlow. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#registration_flow Realm#registration_flow}
        :param remember_me: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#remember_me Realm#remember_me}.
        :param reset_credentials_flow: Which flow should be used for ResetCredentialsFlow. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#reset_credentials_flow Realm#reset_credentials_flow}
        :param reset_password_allowed: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#reset_password_allowed Realm#reset_password_allowed}.
        :param revoke_refresh_token: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#revoke_refresh_token Realm#revoke_refresh_token}.
        :param security_defenses: security_defenses block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#security_defenses Realm#security_defenses}
        :param smtp_server: smtp_server block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#smtp_server Realm#smtp_server}
        :param ssl_required: SSL Required: Values can be 'none', 'external' or 'all'. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#ssl_required Realm#ssl_required}
        :param sso_session_idle_timeout: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#sso_session_idle_timeout Realm#sso_session_idle_timeout}.
        :param sso_session_idle_timeout_remember_me: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#sso_session_idle_timeout_remember_me Realm#sso_session_idle_timeout_remember_me}.
        :param sso_session_max_lifespan: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#sso_session_max_lifespan Realm#sso_session_max_lifespan}.
        :param sso_session_max_lifespan_remember_me: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#sso_session_max_lifespan_remember_me Realm#sso_session_max_lifespan_remember_me}.
        :param user_managed_access: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#user_managed_access Realm#user_managed_access}.
        :param verify_email: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#verify_email Realm#verify_email}.
        :param web_authn_passwordless_policy: web_authn_passwordless_policy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#web_authn_passwordless_policy Realm#web_authn_passwordless_policy}
        :param web_authn_policy: web_authn_policy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#web_authn_policy Realm#web_authn_policy}
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(internationalization, dict):
            internationalization = RealmInternationalization(**internationalization)
        if isinstance(otp_policy, dict):
            otp_policy = RealmOtpPolicy(**otp_policy)
        if isinstance(security_defenses, dict):
            security_defenses = RealmSecurityDefenses(**security_defenses)
        if isinstance(smtp_server, dict):
            smtp_server = RealmSmtpServer(**smtp_server)
        if isinstance(web_authn_passwordless_policy, dict):
            web_authn_passwordless_policy = RealmWebAuthnPasswordlessPolicy(
                **web_authn_passwordless_policy
            )
        if isinstance(web_authn_policy, dict):
            web_authn_policy = RealmWebAuthnPolicy(**web_authn_policy)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__f805730adb3685af83d5cf884414d8f42c4dfadb884bbbd7a9e1fd9c9a630b19
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
                argname="argument realm", value=realm, expected_type=type_hints["realm"]
            )
            check_type(
                argname="argument access_code_lifespan",
                value=access_code_lifespan,
                expected_type=type_hints["access_code_lifespan"],
            )
            check_type(
                argname="argument access_code_lifespan_login",
                value=access_code_lifespan_login,
                expected_type=type_hints["access_code_lifespan_login"],
            )
            check_type(
                argname="argument access_code_lifespan_user_action",
                value=access_code_lifespan_user_action,
                expected_type=type_hints["access_code_lifespan_user_action"],
            )
            check_type(
                argname="argument access_token_lifespan",
                value=access_token_lifespan,
                expected_type=type_hints["access_token_lifespan"],
            )
            check_type(
                argname="argument access_token_lifespan_for_implicit_flow",
                value=access_token_lifespan_for_implicit_flow,
                expected_type=type_hints["access_token_lifespan_for_implicit_flow"],
            )
            check_type(
                argname="argument account_theme",
                value=account_theme,
                expected_type=type_hints["account_theme"],
            )
            check_type(
                argname="argument action_token_generated_by_admin_lifespan",
                value=action_token_generated_by_admin_lifespan,
                expected_type=type_hints["action_token_generated_by_admin_lifespan"],
            )
            check_type(
                argname="argument action_token_generated_by_user_lifespan",
                value=action_token_generated_by_user_lifespan,
                expected_type=type_hints["action_token_generated_by_user_lifespan"],
            )
            check_type(
                argname="argument admin_theme",
                value=admin_theme,
                expected_type=type_hints["admin_theme"],
            )
            check_type(
                argname="argument attributes",
                value=attributes,
                expected_type=type_hints["attributes"],
            )
            check_type(
                argname="argument browser_flow",
                value=browser_flow,
                expected_type=type_hints["browser_flow"],
            )
            check_type(
                argname="argument client_authentication_flow",
                value=client_authentication_flow,
                expected_type=type_hints["client_authentication_flow"],
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
                argname="argument default_default_client_scopes",
                value=default_default_client_scopes,
                expected_type=type_hints["default_default_client_scopes"],
            )
            check_type(
                argname="argument default_optional_client_scopes",
                value=default_optional_client_scopes,
                expected_type=type_hints["default_optional_client_scopes"],
            )
            check_type(
                argname="argument default_signature_algorithm",
                value=default_signature_algorithm,
                expected_type=type_hints["default_signature_algorithm"],
            )
            check_type(
                argname="argument direct_grant_flow",
                value=direct_grant_flow,
                expected_type=type_hints["direct_grant_flow"],
            )
            check_type(
                argname="argument display_name",
                value=display_name,
                expected_type=type_hints["display_name"],
            )
            check_type(
                argname="argument display_name_html",
                value=display_name_html,
                expected_type=type_hints["display_name_html"],
            )
            check_type(
                argname="argument docker_authentication_flow",
                value=docker_authentication_flow,
                expected_type=type_hints["docker_authentication_flow"],
            )
            check_type(
                argname="argument duplicate_emails_allowed",
                value=duplicate_emails_allowed,
                expected_type=type_hints["duplicate_emails_allowed"],
            )
            check_type(
                argname="argument edit_username_allowed",
                value=edit_username_allowed,
                expected_type=type_hints["edit_username_allowed"],
            )
            check_type(
                argname="argument email_theme",
                value=email_theme,
                expected_type=type_hints["email_theme"],
            )
            check_type(
                argname="argument enabled",
                value=enabled,
                expected_type=type_hints["enabled"],
            )
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(
                argname="argument internal_id",
                value=internal_id,
                expected_type=type_hints["internal_id"],
            )
            check_type(
                argname="argument internationalization",
                value=internationalization,
                expected_type=type_hints["internationalization"],
            )
            check_type(
                argname="argument login_theme",
                value=login_theme,
                expected_type=type_hints["login_theme"],
            )
            check_type(
                argname="argument login_with_email_allowed",
                value=login_with_email_allowed,
                expected_type=type_hints["login_with_email_allowed"],
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
                argname="argument offline_session_idle_timeout",
                value=offline_session_idle_timeout,
                expected_type=type_hints["offline_session_idle_timeout"],
            )
            check_type(
                argname="argument offline_session_max_lifespan",
                value=offline_session_max_lifespan,
                expected_type=type_hints["offline_session_max_lifespan"],
            )
            check_type(
                argname="argument offline_session_max_lifespan_enabled",
                value=offline_session_max_lifespan_enabled,
                expected_type=type_hints["offline_session_max_lifespan_enabled"],
            )
            check_type(
                argname="argument otp_policy",
                value=otp_policy,
                expected_type=type_hints["otp_policy"],
            )
            check_type(
                argname="argument password_policy",
                value=password_policy,
                expected_type=type_hints["password_policy"],
            )
            check_type(
                argname="argument refresh_token_max_reuse",
                value=refresh_token_max_reuse,
                expected_type=type_hints["refresh_token_max_reuse"],
            )
            check_type(
                argname="argument registration_allowed",
                value=registration_allowed,
                expected_type=type_hints["registration_allowed"],
            )
            check_type(
                argname="argument registration_email_as_username",
                value=registration_email_as_username,
                expected_type=type_hints["registration_email_as_username"],
            )
            check_type(
                argname="argument registration_flow",
                value=registration_flow,
                expected_type=type_hints["registration_flow"],
            )
            check_type(
                argname="argument remember_me",
                value=remember_me,
                expected_type=type_hints["remember_me"],
            )
            check_type(
                argname="argument reset_credentials_flow",
                value=reset_credentials_flow,
                expected_type=type_hints["reset_credentials_flow"],
            )
            check_type(
                argname="argument reset_password_allowed",
                value=reset_password_allowed,
                expected_type=type_hints["reset_password_allowed"],
            )
            check_type(
                argname="argument revoke_refresh_token",
                value=revoke_refresh_token,
                expected_type=type_hints["revoke_refresh_token"],
            )
            check_type(
                argname="argument security_defenses",
                value=security_defenses,
                expected_type=type_hints["security_defenses"],
            )
            check_type(
                argname="argument smtp_server",
                value=smtp_server,
                expected_type=type_hints["smtp_server"],
            )
            check_type(
                argname="argument ssl_required",
                value=ssl_required,
                expected_type=type_hints["ssl_required"],
            )
            check_type(
                argname="argument sso_session_idle_timeout",
                value=sso_session_idle_timeout,
                expected_type=type_hints["sso_session_idle_timeout"],
            )
            check_type(
                argname="argument sso_session_idle_timeout_remember_me",
                value=sso_session_idle_timeout_remember_me,
                expected_type=type_hints["sso_session_idle_timeout_remember_me"],
            )
            check_type(
                argname="argument sso_session_max_lifespan",
                value=sso_session_max_lifespan,
                expected_type=type_hints["sso_session_max_lifespan"],
            )
            check_type(
                argname="argument sso_session_max_lifespan_remember_me",
                value=sso_session_max_lifespan_remember_me,
                expected_type=type_hints["sso_session_max_lifespan_remember_me"],
            )
            check_type(
                argname="argument user_managed_access",
                value=user_managed_access,
                expected_type=type_hints["user_managed_access"],
            )
            check_type(
                argname="argument verify_email",
                value=verify_email,
                expected_type=type_hints["verify_email"],
            )
            check_type(
                argname="argument web_authn_passwordless_policy",
                value=web_authn_passwordless_policy,
                expected_type=type_hints["web_authn_passwordless_policy"],
            )
            check_type(
                argname="argument web_authn_policy",
                value=web_authn_policy,
                expected_type=type_hints["web_authn_policy"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
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
        if access_code_lifespan is not None:
            self._values["access_code_lifespan"] = access_code_lifespan
        if access_code_lifespan_login is not None:
            self._values["access_code_lifespan_login"] = access_code_lifespan_login
        if access_code_lifespan_user_action is not None:
            self._values[
                "access_code_lifespan_user_action"
            ] = access_code_lifespan_user_action
        if access_token_lifespan is not None:
            self._values["access_token_lifespan"] = access_token_lifespan
        if access_token_lifespan_for_implicit_flow is not None:
            self._values[
                "access_token_lifespan_for_implicit_flow"
            ] = access_token_lifespan_for_implicit_flow
        if account_theme is not None:
            self._values["account_theme"] = account_theme
        if action_token_generated_by_admin_lifespan is not None:
            self._values[
                "action_token_generated_by_admin_lifespan"
            ] = action_token_generated_by_admin_lifespan
        if action_token_generated_by_user_lifespan is not None:
            self._values[
                "action_token_generated_by_user_lifespan"
            ] = action_token_generated_by_user_lifespan
        if admin_theme is not None:
            self._values["admin_theme"] = admin_theme
        if attributes is not None:
            self._values["attributes"] = attributes
        if browser_flow is not None:
            self._values["browser_flow"] = browser_flow
        if client_authentication_flow is not None:
            self._values["client_authentication_flow"] = client_authentication_flow
        if client_session_idle_timeout is not None:
            self._values["client_session_idle_timeout"] = client_session_idle_timeout
        if client_session_max_lifespan is not None:
            self._values["client_session_max_lifespan"] = client_session_max_lifespan
        if default_default_client_scopes is not None:
            self._values[
                "default_default_client_scopes"
            ] = default_default_client_scopes
        if default_optional_client_scopes is not None:
            self._values[
                "default_optional_client_scopes"
            ] = default_optional_client_scopes
        if default_signature_algorithm is not None:
            self._values["default_signature_algorithm"] = default_signature_algorithm
        if direct_grant_flow is not None:
            self._values["direct_grant_flow"] = direct_grant_flow
        if display_name is not None:
            self._values["display_name"] = display_name
        if display_name_html is not None:
            self._values["display_name_html"] = display_name_html
        if docker_authentication_flow is not None:
            self._values["docker_authentication_flow"] = docker_authentication_flow
        if duplicate_emails_allowed is not None:
            self._values["duplicate_emails_allowed"] = duplicate_emails_allowed
        if edit_username_allowed is not None:
            self._values["edit_username_allowed"] = edit_username_allowed
        if email_theme is not None:
            self._values["email_theme"] = email_theme
        if enabled is not None:
            self._values["enabled"] = enabled
        if id is not None:
            self._values["id"] = id
        if internal_id is not None:
            self._values["internal_id"] = internal_id
        if internationalization is not None:
            self._values["internationalization"] = internationalization
        if login_theme is not None:
            self._values["login_theme"] = login_theme
        if login_with_email_allowed is not None:
            self._values["login_with_email_allowed"] = login_with_email_allowed
        if oauth2_device_code_lifespan is not None:
            self._values["oauth2_device_code_lifespan"] = oauth2_device_code_lifespan
        if oauth2_device_polling_interval is not None:
            self._values[
                "oauth2_device_polling_interval"
            ] = oauth2_device_polling_interval
        if offline_session_idle_timeout is not None:
            self._values["offline_session_idle_timeout"] = offline_session_idle_timeout
        if offline_session_max_lifespan is not None:
            self._values["offline_session_max_lifespan"] = offline_session_max_lifespan
        if offline_session_max_lifespan_enabled is not None:
            self._values[
                "offline_session_max_lifespan_enabled"
            ] = offline_session_max_lifespan_enabled
        if otp_policy is not None:
            self._values["otp_policy"] = otp_policy
        if password_policy is not None:
            self._values["password_policy"] = password_policy
        if refresh_token_max_reuse is not None:
            self._values["refresh_token_max_reuse"] = refresh_token_max_reuse
        if registration_allowed is not None:
            self._values["registration_allowed"] = registration_allowed
        if registration_email_as_username is not None:
            self._values[
                "registration_email_as_username"
            ] = registration_email_as_username
        if registration_flow is not None:
            self._values["registration_flow"] = registration_flow
        if remember_me is not None:
            self._values["remember_me"] = remember_me
        if reset_credentials_flow is not None:
            self._values["reset_credentials_flow"] = reset_credentials_flow
        if reset_password_allowed is not None:
            self._values["reset_password_allowed"] = reset_password_allowed
        if revoke_refresh_token is not None:
            self._values["revoke_refresh_token"] = revoke_refresh_token
        if security_defenses is not None:
            self._values["security_defenses"] = security_defenses
        if smtp_server is not None:
            self._values["smtp_server"] = smtp_server
        if ssl_required is not None:
            self._values["ssl_required"] = ssl_required
        if sso_session_idle_timeout is not None:
            self._values["sso_session_idle_timeout"] = sso_session_idle_timeout
        if sso_session_idle_timeout_remember_me is not None:
            self._values[
                "sso_session_idle_timeout_remember_me"
            ] = sso_session_idle_timeout_remember_me
        if sso_session_max_lifespan is not None:
            self._values["sso_session_max_lifespan"] = sso_session_max_lifespan
        if sso_session_max_lifespan_remember_me is not None:
            self._values[
                "sso_session_max_lifespan_remember_me"
            ] = sso_session_max_lifespan_remember_me
        if user_managed_access is not None:
            self._values["user_managed_access"] = user_managed_access
        if verify_email is not None:
            self._values["verify_email"] = verify_email
        if web_authn_passwordless_policy is not None:
            self._values[
                "web_authn_passwordless_policy"
            ] = web_authn_passwordless_policy
        if web_authn_policy is not None:
            self._values["web_authn_policy"] = web_authn_policy

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
    def realm(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#realm Realm#realm}."""
        result = self._values.get("realm")
        assert result is not None, "Required property 'realm' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_code_lifespan(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#access_code_lifespan Realm#access_code_lifespan}."""
        result = self._values.get("access_code_lifespan")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def access_code_lifespan_login(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#access_code_lifespan_login Realm#access_code_lifespan_login}."""
        result = self._values.get("access_code_lifespan_login")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def access_code_lifespan_user_action(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#access_code_lifespan_user_action Realm#access_code_lifespan_user_action}."""
        result = self._values.get("access_code_lifespan_user_action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def access_token_lifespan(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#access_token_lifespan Realm#access_token_lifespan}."""
        result = self._values.get("access_token_lifespan")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def access_token_lifespan_for_implicit_flow(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#access_token_lifespan_for_implicit_flow Realm#access_token_lifespan_for_implicit_flow}."""
        result = self._values.get("access_token_lifespan_for_implicit_flow")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def account_theme(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#account_theme Realm#account_theme}."""
        result = self._values.get("account_theme")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def action_token_generated_by_admin_lifespan(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#action_token_generated_by_admin_lifespan Realm#action_token_generated_by_admin_lifespan}."""
        result = self._values.get("action_token_generated_by_admin_lifespan")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def action_token_generated_by_user_lifespan(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#action_token_generated_by_user_lifespan Realm#action_token_generated_by_user_lifespan}."""
        result = self._values.get("action_token_generated_by_user_lifespan")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def admin_theme(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#admin_theme Realm#admin_theme}."""
        result = self._values.get("admin_theme")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def attributes(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#attributes Realm#attributes}."""
        result = self._values.get("attributes")
        return typing.cast(
            typing.Optional[typing.Mapping[builtins.str, builtins.str]], result
        )

    @builtins.property
    def browser_flow(self) -> typing.Optional[builtins.str]:
        """Which flow should be used for BrowserFlow.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#browser_flow Realm#browser_flow}
        """
        result = self._values.get("browser_flow")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_authentication_flow(self) -> typing.Optional[builtins.str]:
        """Which flow should be used for ClientAuthenticationFlow.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#client_authentication_flow Realm#client_authentication_flow}
        """
        result = self._values.get("client_authentication_flow")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_session_idle_timeout(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#client_session_idle_timeout Realm#client_session_idle_timeout}."""
        result = self._values.get("client_session_idle_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_session_max_lifespan(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#client_session_max_lifespan Realm#client_session_max_lifespan}."""
        result = self._values.get("client_session_max_lifespan")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_default_client_scopes(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#default_default_client_scopes Realm#default_default_client_scopes}."""
        result = self._values.get("default_default_client_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def default_optional_client_scopes(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#default_optional_client_scopes Realm#default_optional_client_scopes}."""
        result = self._values.get("default_optional_client_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def default_signature_algorithm(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#default_signature_algorithm Realm#default_signature_algorithm}."""
        result = self._values.get("default_signature_algorithm")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def direct_grant_flow(self) -> typing.Optional[builtins.str]:
        """Which flow should be used for DirectGrantFlow.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#direct_grant_flow Realm#direct_grant_flow}
        """
        result = self._values.get("direct_grant_flow")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#display_name Realm#display_name}."""
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_name_html(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#display_name_html Realm#display_name_html}."""
        result = self._values.get("display_name_html")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def docker_authentication_flow(self) -> typing.Optional[builtins.str]:
        """Which flow should be used for DockerAuthenticationFlow.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#docker_authentication_flow Realm#docker_authentication_flow}
        """
        result = self._values.get("docker_authentication_flow")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def duplicate_emails_allowed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#duplicate_emails_allowed Realm#duplicate_emails_allowed}."""
        result = self._values.get("duplicate_emails_allowed")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def edit_username_allowed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#edit_username_allowed Realm#edit_username_allowed}."""
        result = self._values.get("edit_username_allowed")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def email_theme(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#email_theme Realm#email_theme}."""
        result = self._values.get("email_theme")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#enabled Realm#enabled}."""
        result = self._values.get("enabled")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#id Realm#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def internal_id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#internal_id Realm#internal_id}."""
        result = self._values.get("internal_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def internationalization(self) -> typing.Optional["RealmInternationalization"]:
        """internationalization block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#internationalization Realm#internationalization}
        """
        result = self._values.get("internationalization")
        return typing.cast(typing.Optional["RealmInternationalization"], result)

    @builtins.property
    def login_theme(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#login_theme Realm#login_theme}."""
        result = self._values.get("login_theme")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def login_with_email_allowed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#login_with_email_allowed Realm#login_with_email_allowed}."""
        result = self._values.get("login_with_email_allowed")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def oauth2_device_code_lifespan(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#oauth2_device_code_lifespan Realm#oauth2_device_code_lifespan}."""
        result = self._values.get("oauth2_device_code_lifespan")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oauth2_device_polling_interval(self) -> typing.Optional[jsii.Number]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#oauth2_device_polling_interval Realm#oauth2_device_polling_interval}."""
        result = self._values.get("oauth2_device_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def offline_session_idle_timeout(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#offline_session_idle_timeout Realm#offline_session_idle_timeout}."""
        result = self._values.get("offline_session_idle_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def offline_session_max_lifespan(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#offline_session_max_lifespan Realm#offline_session_max_lifespan}."""
        result = self._values.get("offline_session_max_lifespan")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def offline_session_max_lifespan_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#offline_session_max_lifespan_enabled Realm#offline_session_max_lifespan_enabled}."""
        result = self._values.get("offline_session_max_lifespan_enabled")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def otp_policy(self) -> typing.Optional["RealmOtpPolicy"]:
        """otp_policy block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#otp_policy Realm#otp_policy}
        """
        result = self._values.get("otp_policy")
        return typing.cast(typing.Optional["RealmOtpPolicy"], result)

    @builtins.property
    def password_policy(self) -> typing.Optional[builtins.str]:
        """String that represents the passwordPolicies that are in place.

        Each policy is separated with " and ". Supported policies can be found in the server-info providers page. example: "upperCase(1) and length(8) and forceExpiredPasswordChange(365) and notUsername(undefined)"

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#password_policy Realm#password_policy}
        """
        result = self._values.get("password_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def refresh_token_max_reuse(self) -> typing.Optional[jsii.Number]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#refresh_token_max_reuse Realm#refresh_token_max_reuse}."""
        result = self._values.get("refresh_token_max_reuse")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def registration_allowed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#registration_allowed Realm#registration_allowed}."""
        result = self._values.get("registration_allowed")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def registration_email_as_username(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#registration_email_as_username Realm#registration_email_as_username}."""
        result = self._values.get("registration_email_as_username")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def registration_flow(self) -> typing.Optional[builtins.str]:
        """Which flow should be used for RegistrationFlow.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#registration_flow Realm#registration_flow}
        """
        result = self._values.get("registration_flow")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def remember_me(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#remember_me Realm#remember_me}."""
        result = self._values.get("remember_me")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def reset_credentials_flow(self) -> typing.Optional[builtins.str]:
        """Which flow should be used for ResetCredentialsFlow.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#reset_credentials_flow Realm#reset_credentials_flow}
        """
        result = self._values.get("reset_credentials_flow")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def reset_password_allowed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#reset_password_allowed Realm#reset_password_allowed}."""
        result = self._values.get("reset_password_allowed")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def revoke_refresh_token(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#revoke_refresh_token Realm#revoke_refresh_token}."""
        result = self._values.get("revoke_refresh_token")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def security_defenses(self) -> typing.Optional["RealmSecurityDefenses"]:
        """security_defenses block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#security_defenses Realm#security_defenses}
        """
        result = self._values.get("security_defenses")
        return typing.cast(typing.Optional["RealmSecurityDefenses"], result)

    @builtins.property
    def smtp_server(self) -> typing.Optional["RealmSmtpServer"]:
        """smtp_server block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#smtp_server Realm#smtp_server}
        """
        result = self._values.get("smtp_server")
        return typing.cast(typing.Optional["RealmSmtpServer"], result)

    @builtins.property
    def ssl_required(self) -> typing.Optional[builtins.str]:
        """SSL Required: Values can be 'none', 'external' or 'all'.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#ssl_required Realm#ssl_required}
        """
        result = self._values.get("ssl_required")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sso_session_idle_timeout(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#sso_session_idle_timeout Realm#sso_session_idle_timeout}."""
        result = self._values.get("sso_session_idle_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sso_session_idle_timeout_remember_me(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#sso_session_idle_timeout_remember_me Realm#sso_session_idle_timeout_remember_me}."""
        result = self._values.get("sso_session_idle_timeout_remember_me")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sso_session_max_lifespan(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#sso_session_max_lifespan Realm#sso_session_max_lifespan}."""
        result = self._values.get("sso_session_max_lifespan")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sso_session_max_lifespan_remember_me(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#sso_session_max_lifespan_remember_me Realm#sso_session_max_lifespan_remember_me}."""
        result = self._values.get("sso_session_max_lifespan_remember_me")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_managed_access(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#user_managed_access Realm#user_managed_access}."""
        result = self._values.get("user_managed_access")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def verify_email(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#verify_email Realm#verify_email}."""
        result = self._values.get("verify_email")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def web_authn_passwordless_policy(
        self,
    ) -> typing.Optional["RealmWebAuthnPasswordlessPolicy"]:
        """web_authn_passwordless_policy block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#web_authn_passwordless_policy Realm#web_authn_passwordless_policy}
        """
        result = self._values.get("web_authn_passwordless_policy")
        return typing.cast(typing.Optional["RealmWebAuthnPasswordlessPolicy"], result)

    @builtins.property
    def web_authn_policy(self) -> typing.Optional["RealmWebAuthnPolicy"]:
        """web_authn_policy block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#web_authn_policy Realm#web_authn_policy}
        """
        result = self._values.get("web_authn_policy")
        return typing.cast(typing.Optional["RealmWebAuthnPolicy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RealmConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="keycloak.realm.RealmInternationalization",
    jsii_struct_bases=[],
    name_mapping={
        "default_locale": "defaultLocale",
        "supported_locales": "supportedLocales",
    },
)
class RealmInternationalization:
    def __init__(
        self,
        *,
        default_locale: builtins.str,
        supported_locales: typing.Sequence[builtins.str],
    ) -> None:
        """
        :param default_locale: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#default_locale Realm#default_locale}.
        :param supported_locales: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#supported_locales Realm#supported_locales}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__6dd4f6627bd28ee20348ba444f579346e718e203c4db223fc0f0d8093b48de6c
            )
            check_type(
                argname="argument default_locale",
                value=default_locale,
                expected_type=type_hints["default_locale"],
            )
            check_type(
                argname="argument supported_locales",
                value=supported_locales,
                expected_type=type_hints["supported_locales"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "default_locale": default_locale,
            "supported_locales": supported_locales,
        }

    @builtins.property
    def default_locale(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#default_locale Realm#default_locale}."""
        result = self._values.get("default_locale")
        assert result is not None, "Required property 'default_locale' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def supported_locales(self) -> typing.List[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#supported_locales Realm#supported_locales}."""
        result = self._values.get("supported_locales")
        assert result is not None, "Required property 'supported_locales' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RealmInternationalization(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RealmInternationalizationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.realm.RealmInternationalizationOutputReference",
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
                _typecheckingstub__0a7f1f5f64c7b0647913ccb1c5abe3db7bd5fe4460dc1cff7277ef0176478652
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

    @builtins.property
    @jsii.member(jsii_name="defaultLocaleInput")
    def default_locale_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "defaultLocaleInput")
        )

    @builtins.property
    @jsii.member(jsii_name="supportedLocalesInput")
    def supported_locales_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]],
            jsii.get(self, "supportedLocalesInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="defaultLocale")
    def default_locale(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultLocale"))

    @default_locale.setter
    def default_locale(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__83420ba5444da2f7de889e34c0d687fbd5e9c4c4379361f9a2b99f6c15afa44e
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "defaultLocale", value)

    @builtins.property
    @jsii.member(jsii_name="supportedLocales")
    def supported_locales(self) -> typing.List[builtins.str]:
        return typing.cast(
            typing.List[builtins.str], jsii.get(self, "supportedLocales")
        )

    @supported_locales.setter
    def supported_locales(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__11e9cd95a413d1ab7c02fb6013cb2c9ce6c80a282f221a2584246fdfc29639a0
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "supportedLocales", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RealmInternationalization]:
        return typing.cast(
            typing.Optional[RealmInternationalization], jsii.get(self, "internalValue")
        )

    @internal_value.setter
    def internal_value(self, value: typing.Optional[RealmInternationalization]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__cd0951b936206e6e3c06e89bf37f021a7cc6ecabab58f0d4388b9356f9399a89
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="keycloak.realm.RealmOtpPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "algorithm": "algorithm",
        "digits": "digits",
        "initial_counter": "initialCounter",
        "look_ahead_window": "lookAheadWindow",
        "period": "period",
        "type": "type",
    },
)
class RealmOtpPolicy:
    def __init__(
        self,
        *,
        algorithm: typing.Optional[builtins.str] = None,
        digits: typing.Optional[jsii.Number] = None,
        initial_counter: typing.Optional[jsii.Number] = None,
        look_ahead_window: typing.Optional[jsii.Number] = None,
        period: typing.Optional[jsii.Number] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param algorithm: What hashing algorithm should be used to generate the OTP. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#algorithm Realm#algorithm}
        :param digits: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#digits Realm#digits}.
        :param initial_counter: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#initial_counter Realm#initial_counter}.
        :param look_ahead_window: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#look_ahead_window Realm#look_ahead_window}.
        :param period: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#period Realm#period}.
        :param type: OTP Type, totp for Time-Based One Time Password or hotp for counter base one time password. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#type Realm#type}
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__f3a18dd93751c6a28d5a2bb2ac56e4ffd65f0ce17e536d1f0c121a7f43af42ac
            )
            check_type(
                argname="argument algorithm",
                value=algorithm,
                expected_type=type_hints["algorithm"],
            )
            check_type(
                argname="argument digits",
                value=digits,
                expected_type=type_hints["digits"],
            )
            check_type(
                argname="argument initial_counter",
                value=initial_counter,
                expected_type=type_hints["initial_counter"],
            )
            check_type(
                argname="argument look_ahead_window",
                value=look_ahead_window,
                expected_type=type_hints["look_ahead_window"],
            )
            check_type(
                argname="argument period",
                value=period,
                expected_type=type_hints["period"],
            )
            check_type(
                argname="argument type", value=type, expected_type=type_hints["type"]
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if algorithm is not None:
            self._values["algorithm"] = algorithm
        if digits is not None:
            self._values["digits"] = digits
        if initial_counter is not None:
            self._values["initial_counter"] = initial_counter
        if look_ahead_window is not None:
            self._values["look_ahead_window"] = look_ahead_window
        if period is not None:
            self._values["period"] = period
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def algorithm(self) -> typing.Optional[builtins.str]:
        """What hashing algorithm should be used to generate the OTP.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#algorithm Realm#algorithm}
        """
        result = self._values.get("algorithm")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def digits(self) -> typing.Optional[jsii.Number]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#digits Realm#digits}."""
        result = self._values.get("digits")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def initial_counter(self) -> typing.Optional[jsii.Number]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#initial_counter Realm#initial_counter}."""
        result = self._values.get("initial_counter")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def look_ahead_window(self) -> typing.Optional[jsii.Number]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#look_ahead_window Realm#look_ahead_window}."""
        result = self._values.get("look_ahead_window")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def period(self) -> typing.Optional[jsii.Number]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#period Realm#period}."""
        result = self._values.get("period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        """OTP Type, totp for Time-Based One Time Password or hotp for counter base one time password.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#type Realm#type}
        """
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RealmOtpPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RealmOtpPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.realm.RealmOtpPolicyOutputReference",
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
                _typecheckingstub__f658acb205f2034438bc37d3c668102e9462f2ee8691c0d8c5835dd8d8d284f8
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

    @jsii.member(jsii_name="resetAlgorithm")
    def reset_algorithm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlgorithm", []))

    @jsii.member(jsii_name="resetDigits")
    def reset_digits(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDigits", []))

    @jsii.member(jsii_name="resetInitialCounter")
    def reset_initial_counter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitialCounter", []))

    @jsii.member(jsii_name="resetLookAheadWindow")
    def reset_look_ahead_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLookAheadWindow", []))

    @jsii.member(jsii_name="resetPeriod")
    def reset_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeriod", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="algorithmInput")
    def algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "algorithmInput")
        )

    @builtins.property
    @jsii.member(jsii_name="digitsInput")
    def digits_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "digitsInput"))

    @builtins.property
    @jsii.member(jsii_name="initialCounterInput")
    def initial_counter_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(
            typing.Optional[jsii.Number], jsii.get(self, "initialCounterInput")
        )

    @builtins.property
    @jsii.member(jsii_name="lookAheadWindowInput")
    def look_ahead_window_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(
            typing.Optional[jsii.Number], jsii.get(self, "lookAheadWindowInput")
        )

    @builtins.property
    @jsii.member(jsii_name="periodInput")
    def period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "periodInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="algorithm")
    def algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "algorithm"))

    @algorithm.setter
    def algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__22dcc86babcb116596c32a7d968fc4fce32357eba6b4d557e35bb6381b7a8caf
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "algorithm", value)

    @builtins.property
    @jsii.member(jsii_name="digits")
    def digits(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "digits"))

    @digits.setter
    def digits(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__82b460c603a445f76df73699063253ae69ce9a09292be3e2ef27c119d7155e76
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "digits", value)

    @builtins.property
    @jsii.member(jsii_name="initialCounter")
    def initial_counter(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "initialCounter"))

    @initial_counter.setter
    def initial_counter(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__e7982e0f96117b343c40eef2a2d7c7048b513ed7b7a018e8c4c5322d2bdd314c
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "initialCounter", value)

    @builtins.property
    @jsii.member(jsii_name="lookAheadWindow")
    def look_ahead_window(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lookAheadWindow"))

    @look_ahead_window.setter
    def look_ahead_window(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__8556587d3e94e2cbffe30e773af1079b4fa99e84f3332f0a26959dcae5a0b55a
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "lookAheadWindow", value)

    @builtins.property
    @jsii.member(jsii_name="period")
    def period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "period"))

    @period.setter
    def period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__cc4346e29f3801b10901daec645d74fb0c8c1f0b84fe50aa26cfdc64d1253331
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "period", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a0739bf7ef32ff3e15a516a0ee91ab5508340fa329ab50f5a5bbcb885e989cb3
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RealmOtpPolicy]:
        return typing.cast(
            typing.Optional[RealmOtpPolicy], jsii.get(self, "internalValue")
        )

    @internal_value.setter
    def internal_value(self, value: typing.Optional[RealmOtpPolicy]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a09ee5bae6721a9951ca4f248aff4c5889b030b90e2750c298969c71dabf27d7
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="keycloak.realm.RealmSecurityDefenses",
    jsii_struct_bases=[],
    name_mapping={
        "brute_force_detection": "bruteForceDetection",
        "headers": "headers",
    },
)
class RealmSecurityDefenses:
    def __init__(
        self,
        *,
        brute_force_detection: typing.Optional[
            typing.Union[
                "RealmSecurityDefensesBruteForceDetection",
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        headers: typing.Optional[
            typing.Union[
                "RealmSecurityDefensesHeaders", typing.Dict[builtins.str, typing.Any]
            ]
        ] = None,
    ) -> None:
        """
        :param brute_force_detection: brute_force_detection block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#brute_force_detection Realm#brute_force_detection}
        :param headers: headers block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#headers Realm#headers}
        """
        if isinstance(brute_force_detection, dict):
            brute_force_detection = RealmSecurityDefensesBruteForceDetection(
                **brute_force_detection
            )
        if isinstance(headers, dict):
            headers = RealmSecurityDefensesHeaders(**headers)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d6679f0e896343b2f8cc320f20c130e6396ecf73e9d7e6483ddb2d2f4669be09
            )
            check_type(
                argname="argument brute_force_detection",
                value=brute_force_detection,
                expected_type=type_hints["brute_force_detection"],
            )
            check_type(
                argname="argument headers",
                value=headers,
                expected_type=type_hints["headers"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if brute_force_detection is not None:
            self._values["brute_force_detection"] = brute_force_detection
        if headers is not None:
            self._values["headers"] = headers

    @builtins.property
    def brute_force_detection(
        self,
    ) -> typing.Optional["RealmSecurityDefensesBruteForceDetection"]:
        """brute_force_detection block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#brute_force_detection Realm#brute_force_detection}
        """
        result = self._values.get("brute_force_detection")
        return typing.cast(
            typing.Optional["RealmSecurityDefensesBruteForceDetection"], result
        )

    @builtins.property
    def headers(self) -> typing.Optional["RealmSecurityDefensesHeaders"]:
        """headers block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#headers Realm#headers}
        """
        result = self._values.get("headers")
        return typing.cast(typing.Optional["RealmSecurityDefensesHeaders"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RealmSecurityDefenses(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="keycloak.realm.RealmSecurityDefensesBruteForceDetection",
    jsii_struct_bases=[],
    name_mapping={
        "failure_reset_time_seconds": "failureResetTimeSeconds",
        "max_failure_wait_seconds": "maxFailureWaitSeconds",
        "max_login_failures": "maxLoginFailures",
        "minimum_quick_login_wait_seconds": "minimumQuickLoginWaitSeconds",
        "permanent_lockout": "permanentLockout",
        "quick_login_check_milli_seconds": "quickLoginCheckMilliSeconds",
        "wait_increment_seconds": "waitIncrementSeconds",
    },
)
class RealmSecurityDefensesBruteForceDetection:
    def __init__(
        self,
        *,
        failure_reset_time_seconds: typing.Optional[jsii.Number] = None,
        max_failure_wait_seconds: typing.Optional[jsii.Number] = None,
        max_login_failures: typing.Optional[jsii.Number] = None,
        minimum_quick_login_wait_seconds: typing.Optional[jsii.Number] = None,
        permanent_lockout: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        quick_login_check_milli_seconds: typing.Optional[jsii.Number] = None,
        wait_increment_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        """
        :param failure_reset_time_seconds: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#failure_reset_time_seconds Realm#failure_reset_time_seconds}.
        :param max_failure_wait_seconds: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#max_failure_wait_seconds Realm#max_failure_wait_seconds}.
        :param max_login_failures: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#max_login_failures Realm#max_login_failures}.
        :param minimum_quick_login_wait_seconds: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#minimum_quick_login_wait_seconds Realm#minimum_quick_login_wait_seconds}.
        :param permanent_lockout: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#permanent_lockout Realm#permanent_lockout}.
        :param quick_login_check_milli_seconds: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#quick_login_check_milli_seconds Realm#quick_login_check_milli_seconds}.
        :param wait_increment_seconds: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#wait_increment_seconds Realm#wait_increment_seconds}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__ef5bd84bf8b5c8d7c82a4688f46abdc996d1c4fadc6316825c3f7a356e3e2db0
            )
            check_type(
                argname="argument failure_reset_time_seconds",
                value=failure_reset_time_seconds,
                expected_type=type_hints["failure_reset_time_seconds"],
            )
            check_type(
                argname="argument max_failure_wait_seconds",
                value=max_failure_wait_seconds,
                expected_type=type_hints["max_failure_wait_seconds"],
            )
            check_type(
                argname="argument max_login_failures",
                value=max_login_failures,
                expected_type=type_hints["max_login_failures"],
            )
            check_type(
                argname="argument minimum_quick_login_wait_seconds",
                value=minimum_quick_login_wait_seconds,
                expected_type=type_hints["minimum_quick_login_wait_seconds"],
            )
            check_type(
                argname="argument permanent_lockout",
                value=permanent_lockout,
                expected_type=type_hints["permanent_lockout"],
            )
            check_type(
                argname="argument quick_login_check_milli_seconds",
                value=quick_login_check_milli_seconds,
                expected_type=type_hints["quick_login_check_milli_seconds"],
            )
            check_type(
                argname="argument wait_increment_seconds",
                value=wait_increment_seconds,
                expected_type=type_hints["wait_increment_seconds"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if failure_reset_time_seconds is not None:
            self._values["failure_reset_time_seconds"] = failure_reset_time_seconds
        if max_failure_wait_seconds is not None:
            self._values["max_failure_wait_seconds"] = max_failure_wait_seconds
        if max_login_failures is not None:
            self._values["max_login_failures"] = max_login_failures
        if minimum_quick_login_wait_seconds is not None:
            self._values[
                "minimum_quick_login_wait_seconds"
            ] = minimum_quick_login_wait_seconds
        if permanent_lockout is not None:
            self._values["permanent_lockout"] = permanent_lockout
        if quick_login_check_milli_seconds is not None:
            self._values[
                "quick_login_check_milli_seconds"
            ] = quick_login_check_milli_seconds
        if wait_increment_seconds is not None:
            self._values["wait_increment_seconds"] = wait_increment_seconds

    @builtins.property
    def failure_reset_time_seconds(self) -> typing.Optional[jsii.Number]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#failure_reset_time_seconds Realm#failure_reset_time_seconds}."""
        result = self._values.get("failure_reset_time_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_failure_wait_seconds(self) -> typing.Optional[jsii.Number]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#max_failure_wait_seconds Realm#max_failure_wait_seconds}."""
        result = self._values.get("max_failure_wait_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_login_failures(self) -> typing.Optional[jsii.Number]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#max_login_failures Realm#max_login_failures}."""
        result = self._values.get("max_login_failures")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def minimum_quick_login_wait_seconds(self) -> typing.Optional[jsii.Number]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#minimum_quick_login_wait_seconds Realm#minimum_quick_login_wait_seconds}."""
        result = self._values.get("minimum_quick_login_wait_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def permanent_lockout(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#permanent_lockout Realm#permanent_lockout}."""
        result = self._values.get("permanent_lockout")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def quick_login_check_milli_seconds(self) -> typing.Optional[jsii.Number]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#quick_login_check_milli_seconds Realm#quick_login_check_milli_seconds}."""
        result = self._values.get("quick_login_check_milli_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def wait_increment_seconds(self) -> typing.Optional[jsii.Number]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#wait_increment_seconds Realm#wait_increment_seconds}."""
        result = self._values.get("wait_increment_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RealmSecurityDefensesBruteForceDetection(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RealmSecurityDefensesBruteForceDetectionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.realm.RealmSecurityDefensesBruteForceDetectionOutputReference",
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
                _typecheckingstub__2fa67aa3a74f13e605249752f3a507f52ccaf4d4b29d3442fa0350bcae78b879
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

    @jsii.member(jsii_name="resetFailureResetTimeSeconds")
    def reset_failure_reset_time_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailureResetTimeSeconds", []))

    @jsii.member(jsii_name="resetMaxFailureWaitSeconds")
    def reset_max_failure_wait_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxFailureWaitSeconds", []))

    @jsii.member(jsii_name="resetMaxLoginFailures")
    def reset_max_login_failures(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxLoginFailures", []))

    @jsii.member(jsii_name="resetMinimumQuickLoginWaitSeconds")
    def reset_minimum_quick_login_wait_seconds(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetMinimumQuickLoginWaitSeconds", [])
        )

    @jsii.member(jsii_name="resetPermanentLockout")
    def reset_permanent_lockout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPermanentLockout", []))

    @jsii.member(jsii_name="resetQuickLoginCheckMilliSeconds")
    def reset_quick_login_check_milli_seconds(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetQuickLoginCheckMilliSeconds", [])
        )

    @jsii.member(jsii_name="resetWaitIncrementSeconds")
    def reset_wait_increment_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitIncrementSeconds", []))

    @builtins.property
    @jsii.member(jsii_name="failureResetTimeSecondsInput")
    def failure_reset_time_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(
            typing.Optional[jsii.Number], jsii.get(self, "failureResetTimeSecondsInput")
        )

    @builtins.property
    @jsii.member(jsii_name="maxFailureWaitSecondsInput")
    def max_failure_wait_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(
            typing.Optional[jsii.Number], jsii.get(self, "maxFailureWaitSecondsInput")
        )

    @builtins.property
    @jsii.member(jsii_name="maxLoginFailuresInput")
    def max_login_failures_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(
            typing.Optional[jsii.Number], jsii.get(self, "maxLoginFailuresInput")
        )

    @builtins.property
    @jsii.member(jsii_name="minimumQuickLoginWaitSecondsInput")
    def minimum_quick_login_wait_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(
            typing.Optional[jsii.Number],
            jsii.get(self, "minimumQuickLoginWaitSecondsInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="permanentLockoutInput")
    def permanent_lockout_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "permanentLockoutInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="quickLoginCheckMilliSecondsInput")
    def quick_login_check_milli_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(
            typing.Optional[jsii.Number],
            jsii.get(self, "quickLoginCheckMilliSecondsInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="waitIncrementSecondsInput")
    def wait_increment_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(
            typing.Optional[jsii.Number], jsii.get(self, "waitIncrementSecondsInput")
        )

    @builtins.property
    @jsii.member(jsii_name="failureResetTimeSeconds")
    def failure_reset_time_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "failureResetTimeSeconds"))

    @failure_reset_time_seconds.setter
    def failure_reset_time_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__afb545db1f8766c0500bb529c2ab1ba1705eae342de5faecb3f8f6ef679ab352
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "failureResetTimeSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="maxFailureWaitSeconds")
    def max_failure_wait_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxFailureWaitSeconds"))

    @max_failure_wait_seconds.setter
    def max_failure_wait_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__9cc2cb48c6af028b066d10c10b2f098fb9d7f22b1903b11f8ce8ce38fbeb89a0
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "maxFailureWaitSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="maxLoginFailures")
    def max_login_failures(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxLoginFailures"))

    @max_login_failures.setter
    def max_login_failures(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__34c2a121d92d6a6bcf7eb8e1cb660bbcb15ecf9cd1d8f79b689a012c7fbd7f22
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "maxLoginFailures", value)

    @builtins.property
    @jsii.member(jsii_name="minimumQuickLoginWaitSeconds")
    def minimum_quick_login_wait_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minimumQuickLoginWaitSeconds"))

    @minimum_quick_login_wait_seconds.setter
    def minimum_quick_login_wait_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d606effd4bdec899fe55fb7dedce9f3ef672cd43d192effb1badcdc49de4afc4
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "minimumQuickLoginWaitSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="permanentLockout")
    def permanent_lockout(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "permanentLockout"),
        )

    @permanent_lockout.setter
    def permanent_lockout(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__62bc4f7f1c5e95cc3458b752a85ed886adadefa4f79f1294cfe9936aeaa30e69
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "permanentLockout", value)

    @builtins.property
    @jsii.member(jsii_name="quickLoginCheckMilliSeconds")
    def quick_login_check_milli_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "quickLoginCheckMilliSeconds"))

    @quick_login_check_milli_seconds.setter
    def quick_login_check_milli_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__9bdf137380e1add889ad07dc9723eda73280dd9eb8a877570d5a6dc43952d38a
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "quickLoginCheckMilliSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="waitIncrementSeconds")
    def wait_increment_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "waitIncrementSeconds"))

    @wait_increment_seconds.setter
    def wait_increment_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__6791ef3a74d47fb619ddc189c1bfab787779adf80c599e1a8e4556689b3c1dff
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "waitIncrementSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[RealmSecurityDefensesBruteForceDetection]:
        return typing.cast(
            typing.Optional[RealmSecurityDefensesBruteForceDetection],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[RealmSecurityDefensesBruteForceDetection],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__85097f0da85805cfbd5a6dc654368abf27a1b898dfaab752cdbc7d1dd1d13af7
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="keycloak.realm.RealmSecurityDefensesHeaders",
    jsii_struct_bases=[],
    name_mapping={
        "content_security_policy": "contentSecurityPolicy",
        "content_security_policy_report_only": "contentSecurityPolicyReportOnly",
        "strict_transport_security": "strictTransportSecurity",
        "x_content_type_options": "xContentTypeOptions",
        "x_frame_options": "xFrameOptions",
        "x_robots_tag": "xRobotsTag",
        "x_xss_protection": "xXssProtection",
    },
)
class RealmSecurityDefensesHeaders:
    def __init__(
        self,
        *,
        content_security_policy: typing.Optional[builtins.str] = None,
        content_security_policy_report_only: typing.Optional[builtins.str] = None,
        strict_transport_security: typing.Optional[builtins.str] = None,
        x_content_type_options: typing.Optional[builtins.str] = None,
        x_frame_options: typing.Optional[builtins.str] = None,
        x_robots_tag: typing.Optional[builtins.str] = None,
        x_xss_protection: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param content_security_policy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#content_security_policy Realm#content_security_policy}.
        :param content_security_policy_report_only: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#content_security_policy_report_only Realm#content_security_policy_report_only}.
        :param strict_transport_security: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#strict_transport_security Realm#strict_transport_security}.
        :param x_content_type_options: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#x_content_type_options Realm#x_content_type_options}.
        :param x_frame_options: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#x_frame_options Realm#x_frame_options}.
        :param x_robots_tag: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#x_robots_tag Realm#x_robots_tag}.
        :param x_xss_protection: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#x_xss_protection Realm#x_xss_protection}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__4fa14a9260df05ead6519b88636257662e99e7c6532f7ece64fec4661e63ec26
            )
            check_type(
                argname="argument content_security_policy",
                value=content_security_policy,
                expected_type=type_hints["content_security_policy"],
            )
            check_type(
                argname="argument content_security_policy_report_only",
                value=content_security_policy_report_only,
                expected_type=type_hints["content_security_policy_report_only"],
            )
            check_type(
                argname="argument strict_transport_security",
                value=strict_transport_security,
                expected_type=type_hints["strict_transport_security"],
            )
            check_type(
                argname="argument x_content_type_options",
                value=x_content_type_options,
                expected_type=type_hints["x_content_type_options"],
            )
            check_type(
                argname="argument x_frame_options",
                value=x_frame_options,
                expected_type=type_hints["x_frame_options"],
            )
            check_type(
                argname="argument x_robots_tag",
                value=x_robots_tag,
                expected_type=type_hints["x_robots_tag"],
            )
            check_type(
                argname="argument x_xss_protection",
                value=x_xss_protection,
                expected_type=type_hints["x_xss_protection"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if content_security_policy is not None:
            self._values["content_security_policy"] = content_security_policy
        if content_security_policy_report_only is not None:
            self._values[
                "content_security_policy_report_only"
            ] = content_security_policy_report_only
        if strict_transport_security is not None:
            self._values["strict_transport_security"] = strict_transport_security
        if x_content_type_options is not None:
            self._values["x_content_type_options"] = x_content_type_options
        if x_frame_options is not None:
            self._values["x_frame_options"] = x_frame_options
        if x_robots_tag is not None:
            self._values["x_robots_tag"] = x_robots_tag
        if x_xss_protection is not None:
            self._values["x_xss_protection"] = x_xss_protection

    @builtins.property
    def content_security_policy(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#content_security_policy Realm#content_security_policy}."""
        result = self._values.get("content_security_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_security_policy_report_only(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#content_security_policy_report_only Realm#content_security_policy_report_only}."""
        result = self._values.get("content_security_policy_report_only")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def strict_transport_security(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#strict_transport_security Realm#strict_transport_security}."""
        result = self._values.get("strict_transport_security")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def x_content_type_options(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#x_content_type_options Realm#x_content_type_options}."""
        result = self._values.get("x_content_type_options")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def x_frame_options(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#x_frame_options Realm#x_frame_options}."""
        result = self._values.get("x_frame_options")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def x_robots_tag(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#x_robots_tag Realm#x_robots_tag}."""
        result = self._values.get("x_robots_tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def x_xss_protection(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#x_xss_protection Realm#x_xss_protection}."""
        result = self._values.get("x_xss_protection")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RealmSecurityDefensesHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RealmSecurityDefensesHeadersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.realm.RealmSecurityDefensesHeadersOutputReference",
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
                _typecheckingstub__6741714819ca4186bfcd6f98b1a0df6d66919b1f01bc08ff53e3c0b3a884f301
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

    @jsii.member(jsii_name="resetContentSecurityPolicy")
    def reset_content_security_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentSecurityPolicy", []))

    @jsii.member(jsii_name="resetContentSecurityPolicyReportOnly")
    def reset_content_security_policy_report_only(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetContentSecurityPolicyReportOnly", [])
        )

    @jsii.member(jsii_name="resetStrictTransportSecurity")
    def reset_strict_transport_security(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStrictTransportSecurity", []))

    @jsii.member(jsii_name="resetXContentTypeOptions")
    def reset_x_content_type_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetXContentTypeOptions", []))

    @jsii.member(jsii_name="resetXFrameOptions")
    def reset_x_frame_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetXFrameOptions", []))

    @jsii.member(jsii_name="resetXRobotsTag")
    def reset_x_robots_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetXRobotsTag", []))

    @jsii.member(jsii_name="resetXXssProtection")
    def reset_x_xss_protection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetXXssProtection", []))

    @builtins.property
    @jsii.member(jsii_name="contentSecurityPolicyInput")
    def content_security_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "contentSecurityPolicyInput")
        )

    @builtins.property
    @jsii.member(jsii_name="contentSecurityPolicyReportOnlyInput")
    def content_security_policy_report_only_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "contentSecurityPolicyReportOnlyInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="strictTransportSecurityInput")
    def strict_transport_security_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "strictTransportSecurityInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="xContentTypeOptionsInput")
    def x_content_type_options_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "xContentTypeOptionsInput")
        )

    @builtins.property
    @jsii.member(jsii_name="xFrameOptionsInput")
    def x_frame_options_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "xFrameOptionsInput")
        )

    @builtins.property
    @jsii.member(jsii_name="xRobotsTagInput")
    def x_robots_tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "xRobotsTagInput")
        )

    @builtins.property
    @jsii.member(jsii_name="xXssProtectionInput")
    def x_xss_protection_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "xXssProtectionInput")
        )

    @builtins.property
    @jsii.member(jsii_name="contentSecurityPolicy")
    def content_security_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentSecurityPolicy"))

    @content_security_policy.setter
    def content_security_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__e4ee15fd3270196fc84b88245748c7b96d9e5ebccb07ec928678d6c7d7f01607
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "contentSecurityPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="contentSecurityPolicyReportOnly")
    def content_security_policy_report_only(self) -> builtins.str:
        return typing.cast(
            builtins.str, jsii.get(self, "contentSecurityPolicyReportOnly")
        )

    @content_security_policy_report_only.setter
    def content_security_policy_report_only(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d4afa19c885394bdfa6c8c554fa327789d1cf392ae4f2231109c6575207be015
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "contentSecurityPolicyReportOnly", value)

    @builtins.property
    @jsii.member(jsii_name="strictTransportSecurity")
    def strict_transport_security(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "strictTransportSecurity"))

    @strict_transport_security.setter
    def strict_transport_security(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__534cd2bb5c6936edb819647e86911072aa7eefaf6f14c7c1ed8253ec9c5c73b3
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "strictTransportSecurity", value)

    @builtins.property
    @jsii.member(jsii_name="xContentTypeOptions")
    def x_content_type_options(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "xContentTypeOptions"))

    @x_content_type_options.setter
    def x_content_type_options(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__6ae6f69bf72d5707a20d25006c05592a103c3ad053b470879fba844b57a189f0
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "xContentTypeOptions", value)

    @builtins.property
    @jsii.member(jsii_name="xFrameOptions")
    def x_frame_options(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "xFrameOptions"))

    @x_frame_options.setter
    def x_frame_options(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__69438a514d9779a20cdb1a1de32c427ac6bd2349b61bed5bb85b9702bc56dbd1
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "xFrameOptions", value)

    @builtins.property
    @jsii.member(jsii_name="xRobotsTag")
    def x_robots_tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "xRobotsTag"))

    @x_robots_tag.setter
    def x_robots_tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__76f19d42c183a803cb4a592022a5b153729a0c7eb3c9d252c7f778b984613a64
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "xRobotsTag", value)

    @builtins.property
    @jsii.member(jsii_name="xXssProtection")
    def x_xss_protection(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "xXssProtection"))

    @x_xss_protection.setter
    def x_xss_protection(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__c8f0d1ee62a84cfcad410eaa3ec74fc81d96a7ce46abbbc854f3fde2c6171280
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "xXssProtection", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RealmSecurityDefensesHeaders]:
        return typing.cast(
            typing.Optional[RealmSecurityDefensesHeaders],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[RealmSecurityDefensesHeaders],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__9973ae0a5607bda6bda2981219cf4443b8631f9b6c8f23f53abb0f237d876667
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


class RealmSecurityDefensesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.realm.RealmSecurityDefensesOutputReference",
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
                _typecheckingstub__53b0fa7b057855b8992dc8e300d2b51d5edcca55c44d59ede5e761fa4c2c3106
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

    @jsii.member(jsii_name="putBruteForceDetection")
    def put_brute_force_detection(
        self,
        *,
        failure_reset_time_seconds: typing.Optional[jsii.Number] = None,
        max_failure_wait_seconds: typing.Optional[jsii.Number] = None,
        max_login_failures: typing.Optional[jsii.Number] = None,
        minimum_quick_login_wait_seconds: typing.Optional[jsii.Number] = None,
        permanent_lockout: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        quick_login_check_milli_seconds: typing.Optional[jsii.Number] = None,
        wait_increment_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        """
        :param failure_reset_time_seconds: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#failure_reset_time_seconds Realm#failure_reset_time_seconds}.
        :param max_failure_wait_seconds: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#max_failure_wait_seconds Realm#max_failure_wait_seconds}.
        :param max_login_failures: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#max_login_failures Realm#max_login_failures}.
        :param minimum_quick_login_wait_seconds: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#minimum_quick_login_wait_seconds Realm#minimum_quick_login_wait_seconds}.
        :param permanent_lockout: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#permanent_lockout Realm#permanent_lockout}.
        :param quick_login_check_milli_seconds: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#quick_login_check_milli_seconds Realm#quick_login_check_milli_seconds}.
        :param wait_increment_seconds: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#wait_increment_seconds Realm#wait_increment_seconds}.
        """
        value = RealmSecurityDefensesBruteForceDetection(
            failure_reset_time_seconds=failure_reset_time_seconds,
            max_failure_wait_seconds=max_failure_wait_seconds,
            max_login_failures=max_login_failures,
            minimum_quick_login_wait_seconds=minimum_quick_login_wait_seconds,
            permanent_lockout=permanent_lockout,
            quick_login_check_milli_seconds=quick_login_check_milli_seconds,
            wait_increment_seconds=wait_increment_seconds,
        )

        return typing.cast(None, jsii.invoke(self, "putBruteForceDetection", [value]))

    @jsii.member(jsii_name="putHeaders")
    def put_headers(
        self,
        *,
        content_security_policy: typing.Optional[builtins.str] = None,
        content_security_policy_report_only: typing.Optional[builtins.str] = None,
        strict_transport_security: typing.Optional[builtins.str] = None,
        x_content_type_options: typing.Optional[builtins.str] = None,
        x_frame_options: typing.Optional[builtins.str] = None,
        x_robots_tag: typing.Optional[builtins.str] = None,
        x_xss_protection: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param content_security_policy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#content_security_policy Realm#content_security_policy}.
        :param content_security_policy_report_only: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#content_security_policy_report_only Realm#content_security_policy_report_only}.
        :param strict_transport_security: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#strict_transport_security Realm#strict_transport_security}.
        :param x_content_type_options: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#x_content_type_options Realm#x_content_type_options}.
        :param x_frame_options: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#x_frame_options Realm#x_frame_options}.
        :param x_robots_tag: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#x_robots_tag Realm#x_robots_tag}.
        :param x_xss_protection: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#x_xss_protection Realm#x_xss_protection}.
        """
        value = RealmSecurityDefensesHeaders(
            content_security_policy=content_security_policy,
            content_security_policy_report_only=content_security_policy_report_only,
            strict_transport_security=strict_transport_security,
            x_content_type_options=x_content_type_options,
            x_frame_options=x_frame_options,
            x_robots_tag=x_robots_tag,
            x_xss_protection=x_xss_protection,
        )

        return typing.cast(None, jsii.invoke(self, "putHeaders", [value]))

    @jsii.member(jsii_name="resetBruteForceDetection")
    def reset_brute_force_detection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBruteForceDetection", []))

    @jsii.member(jsii_name="resetHeaders")
    def reset_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaders", []))

    @builtins.property
    @jsii.member(jsii_name="bruteForceDetection")
    def brute_force_detection(
        self,
    ) -> RealmSecurityDefensesBruteForceDetectionOutputReference:
        return typing.cast(
            RealmSecurityDefensesBruteForceDetectionOutputReference,
            jsii.get(self, "bruteForceDetection"),
        )

    @builtins.property
    @jsii.member(jsii_name="headers")
    def headers(self) -> RealmSecurityDefensesHeadersOutputReference:
        return typing.cast(
            RealmSecurityDefensesHeadersOutputReference, jsii.get(self, "headers")
        )

    @builtins.property
    @jsii.member(jsii_name="bruteForceDetectionInput")
    def brute_force_detection_input(
        self,
    ) -> typing.Optional[RealmSecurityDefensesBruteForceDetection]:
        return typing.cast(
            typing.Optional[RealmSecurityDefensesBruteForceDetection],
            jsii.get(self, "bruteForceDetectionInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="headersInput")
    def headers_input(self) -> typing.Optional[RealmSecurityDefensesHeaders]:
        return typing.cast(
            typing.Optional[RealmSecurityDefensesHeaders],
            jsii.get(self, "headersInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RealmSecurityDefenses]:
        return typing.cast(
            typing.Optional[RealmSecurityDefenses], jsii.get(self, "internalValue")
        )

    @internal_value.setter
    def internal_value(self, value: typing.Optional[RealmSecurityDefenses]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__f5a6f94637c2e90f1c80bdc3e411c0f592ab4134568fa605c1381b4e288bfd74
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="keycloak.realm.RealmSmtpServer",
    jsii_struct_bases=[],
    name_mapping={
        "from_": "from",
        "host": "host",
        "auth": "auth",
        "envelope_from": "envelopeFrom",
        "from_display_name": "fromDisplayName",
        "port": "port",
        "reply_to": "replyTo",
        "reply_to_display_name": "replyToDisplayName",
        "ssl": "ssl",
        "starttls": "starttls",
    },
)
class RealmSmtpServer:
    def __init__(
        self,
        *,
        from_: builtins.str,
        host: builtins.str,
        auth: typing.Optional[
            typing.Union["RealmSmtpServerAuth", typing.Dict[builtins.str, typing.Any]]
        ] = None,
        envelope_from: typing.Optional[builtins.str] = None,
        from_display_name: typing.Optional[builtins.str] = None,
        port: typing.Optional[builtins.str] = None,
        reply_to: typing.Optional[builtins.str] = None,
        reply_to_display_name: typing.Optional[builtins.str] = None,
        ssl: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        starttls: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
    ) -> None:
        """
        :param from_: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#from Realm#from}.
        :param host: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#host Realm#host}.
        :param auth: auth block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#auth Realm#auth}
        :param envelope_from: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#envelope_from Realm#envelope_from}.
        :param from_display_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#from_display_name Realm#from_display_name}.
        :param port: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#port Realm#port}.
        :param reply_to: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#reply_to Realm#reply_to}.
        :param reply_to_display_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#reply_to_display_name Realm#reply_to_display_name}.
        :param ssl: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#ssl Realm#ssl}.
        :param starttls: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#starttls Realm#starttls}.
        """
        if isinstance(auth, dict):
            auth = RealmSmtpServerAuth(**auth)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__020a95d653ec80b514b6858618290075cbd70cf9efa6e3fa7d5b45e6171ee29b
            )
            check_type(
                argname="argument from_", value=from_, expected_type=type_hints["from_"]
            )
            check_type(
                argname="argument host", value=host, expected_type=type_hints["host"]
            )
            check_type(
                argname="argument auth", value=auth, expected_type=type_hints["auth"]
            )
            check_type(
                argname="argument envelope_from",
                value=envelope_from,
                expected_type=type_hints["envelope_from"],
            )
            check_type(
                argname="argument from_display_name",
                value=from_display_name,
                expected_type=type_hints["from_display_name"],
            )
            check_type(
                argname="argument port", value=port, expected_type=type_hints["port"]
            )
            check_type(
                argname="argument reply_to",
                value=reply_to,
                expected_type=type_hints["reply_to"],
            )
            check_type(
                argname="argument reply_to_display_name",
                value=reply_to_display_name,
                expected_type=type_hints["reply_to_display_name"],
            )
            check_type(
                argname="argument ssl", value=ssl, expected_type=type_hints["ssl"]
            )
            check_type(
                argname="argument starttls",
                value=starttls,
                expected_type=type_hints["starttls"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "from_": from_,
            "host": host,
        }
        if auth is not None:
            self._values["auth"] = auth
        if envelope_from is not None:
            self._values["envelope_from"] = envelope_from
        if from_display_name is not None:
            self._values["from_display_name"] = from_display_name
        if port is not None:
            self._values["port"] = port
        if reply_to is not None:
            self._values["reply_to"] = reply_to
        if reply_to_display_name is not None:
            self._values["reply_to_display_name"] = reply_to_display_name
        if ssl is not None:
            self._values["ssl"] = ssl
        if starttls is not None:
            self._values["starttls"] = starttls

    @builtins.property
    def from_(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#from Realm#from}."""
        result = self._values.get("from_")
        assert result is not None, "Required property 'from_' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#host Realm#host}."""
        result = self._values.get("host")
        assert result is not None, "Required property 'host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auth(self) -> typing.Optional["RealmSmtpServerAuth"]:
        """auth block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#auth Realm#auth}
        """
        result = self._values.get("auth")
        return typing.cast(typing.Optional["RealmSmtpServerAuth"], result)

    @builtins.property
    def envelope_from(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#envelope_from Realm#envelope_from}."""
        result = self._values.get("envelope_from")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def from_display_name(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#from_display_name Realm#from_display_name}."""
        result = self._values.get("from_display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#port Realm#port}."""
        result = self._values.get("port")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def reply_to(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#reply_to Realm#reply_to}."""
        result = self._values.get("reply_to")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def reply_to_display_name(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#reply_to_display_name Realm#reply_to_display_name}."""
        result = self._values.get("reply_to_display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssl(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#ssl Realm#ssl}."""
        result = self._values.get("ssl")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def starttls(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#starttls Realm#starttls}."""
        result = self._values.get("starttls")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RealmSmtpServer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="keycloak.realm.RealmSmtpServerAuth",
    jsii_struct_bases=[],
    name_mapping={"password": "password", "username": "username"},
)
class RealmSmtpServerAuth:
    def __init__(self, *, password: builtins.str, username: builtins.str) -> None:
        """
        :param password: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#password Realm#password}.
        :param username: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#username Realm#username}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__3d33466dc7c6980f71c41b55c0f810061e3fd7eac15f09ff3bc15969465f511c
            )
            check_type(
                argname="argument password",
                value=password,
                expected_type=type_hints["password"],
            )
            check_type(
                argname="argument username",
                value=username,
                expected_type=type_hints["username"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "password": password,
            "username": username,
        }

    @builtins.property
    def password(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#password Realm#password}."""
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#username Realm#username}."""
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RealmSmtpServerAuth(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RealmSmtpServerAuthOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.realm.RealmSmtpServerAuthOutputReference",
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
                _typecheckingstub__85c131dfcedb6312f008a078e981f0212aded896f2e0837593c685e04e2a2b36
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

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "passwordInput")
        )

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "usernameInput")
        )

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__89f7191a92ca02489787c3b25a85c18c936cfede89567fb512e895e839a27be1
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__ec6087810323bf717edd0f0844f30945c2f5ec9f73433ae0b1357865be149313
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RealmSmtpServerAuth]:
        return typing.cast(
            typing.Optional[RealmSmtpServerAuth], jsii.get(self, "internalValue")
        )

    @internal_value.setter
    def internal_value(self, value: typing.Optional[RealmSmtpServerAuth]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__3370762a7f7ac4feaacb38bf35c9383bab9b2e54e995efb87e50fb33d2c4d83d
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


class RealmSmtpServerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.realm.RealmSmtpServerOutputReference",
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
                _typecheckingstub__ecdbfb28a26f3f484ac082a74598a4b498846a78f345973377d20a3ffd2f210b
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

    @jsii.member(jsii_name="putAuth")
    def put_auth(self, *, password: builtins.str, username: builtins.str) -> None:
        """
        :param password: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#password Realm#password}.
        :param username: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#username Realm#username}.
        """
        value = RealmSmtpServerAuth(password=password, username=username)

        return typing.cast(None, jsii.invoke(self, "putAuth", [value]))

    @jsii.member(jsii_name="resetAuth")
    def reset_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuth", []))

    @jsii.member(jsii_name="resetEnvelopeFrom")
    def reset_envelope_from(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnvelopeFrom", []))

    @jsii.member(jsii_name="resetFromDisplayName")
    def reset_from_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFromDisplayName", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetReplyTo")
    def reset_reply_to(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplyTo", []))

    @jsii.member(jsii_name="resetReplyToDisplayName")
    def reset_reply_to_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplyToDisplayName", []))

    @jsii.member(jsii_name="resetSsl")
    def reset_ssl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSsl", []))

    @jsii.member(jsii_name="resetStarttls")
    def reset_starttls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStarttls", []))

    @builtins.property
    @jsii.member(jsii_name="auth")
    def auth(self) -> RealmSmtpServerAuthOutputReference:
        return typing.cast(RealmSmtpServerAuthOutputReference, jsii.get(self, "auth"))

    @builtins.property
    @jsii.member(jsii_name="authInput")
    def auth_input(self) -> typing.Optional[RealmSmtpServerAuth]:
        return typing.cast(
            typing.Optional[RealmSmtpServerAuth], jsii.get(self, "authInput")
        )

    @builtins.property
    @jsii.member(jsii_name="envelopeFromInput")
    def envelope_from_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "envelopeFromInput")
        )

    @builtins.property
    @jsii.member(jsii_name="fromDisplayNameInput")
    def from_display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "fromDisplayNameInput")
        )

    @builtins.property
    @jsii.member(jsii_name="fromInput")
    def from_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fromInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="replyToDisplayNameInput")
    def reply_to_display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "replyToDisplayNameInput")
        )

    @builtins.property
    @jsii.member(jsii_name="replyToInput")
    def reply_to_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "replyToInput")
        )

    @builtins.property
    @jsii.member(jsii_name="sslInput")
    def ssl_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "sslInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="starttlsInput")
    def starttls_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "starttlsInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="envelopeFrom")
    def envelope_from(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "envelopeFrom"))

    @envelope_from.setter
    def envelope_from(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__7d730330a62129e0ca832459ecfa4cd355ed2a069c164f6420270f5e94a4410d
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "envelopeFrom", value)

    @builtins.property
    @jsii.member(jsii_name="from")
    def from_(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "from"))

    @from_.setter
    def from_(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__8ad957d393246c7368cc83b15dc4b21bbc5860fc88fd9aa3c4ed418611c62506
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "from", value)

    @builtins.property
    @jsii.member(jsii_name="fromDisplayName")
    def from_display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fromDisplayName"))

    @from_display_name.setter
    def from_display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__446226912c77b2da81b763fbcca8bc1733fd29510b009f97a24b54253dfec97d
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "fromDisplayName", value)

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__91633f39b7ab215b26c9fb57addeb5aff9984872d321ec2c7bf204088887a602
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "port"))

    @port.setter
    def port(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__2f7e0758f5f7f962c726d5afc7cccd4370d662111fd82f0e66af1ae5f4670039
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="replyTo")
    def reply_to(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replyTo"))

    @reply_to.setter
    def reply_to(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__9d0c64568c00bca2a33f624a2514028b77ccb2c95ac8855759910564ad8e4f0b
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "replyTo", value)

    @builtins.property
    @jsii.member(jsii_name="replyToDisplayName")
    def reply_to_display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replyToDisplayName"))

    @reply_to_display_name.setter
    def reply_to_display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__6856f53dc29f77a7f016644f39f036dd1e06bfa6b6e7e932c9aa3775013b3557
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "replyToDisplayName", value)

    @builtins.property
    @jsii.member(jsii_name="ssl")
    def ssl(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "ssl"),
        )

    @ssl.setter
    def ssl(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d2f360f0ffb2d83cfb7449c3a85eef7d5c336a83998959cd64a0d972214616ce
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "ssl", value)

    @builtins.property
    @jsii.member(jsii_name="starttls")
    def starttls(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "starttls"),
        )

    @starttls.setter
    def starttls(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__ec6006e328612384216868a727008c8a84dc9ab46e7f029a52efc70b8339f86b
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "starttls", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RealmSmtpServer]:
        return typing.cast(
            typing.Optional[RealmSmtpServer], jsii.get(self, "internalValue")
        )

    @internal_value.setter
    def internal_value(self, value: typing.Optional[RealmSmtpServer]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__e230aa3b0bcd970737bfe1efee7627cfb2015ff4aad18162e2396deeb8523276
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="keycloak.realm.RealmWebAuthnPasswordlessPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "acceptable_aaguids": "acceptableAaguids",
        "attestation_conveyance_preference": "attestationConveyancePreference",
        "authenticator_attachment": "authenticatorAttachment",
        "avoid_same_authenticator_register": "avoidSameAuthenticatorRegister",
        "create_timeout": "createTimeout",
        "relying_party_entity_name": "relyingPartyEntityName",
        "relying_party_id": "relyingPartyId",
        "require_resident_key": "requireResidentKey",
        "signature_algorithms": "signatureAlgorithms",
        "user_verification_requirement": "userVerificationRequirement",
    },
)
class RealmWebAuthnPasswordlessPolicy:
    def __init__(
        self,
        *,
        acceptable_aaguids: typing.Optional[typing.Sequence[builtins.str]] = None,
        attestation_conveyance_preference: typing.Optional[builtins.str] = None,
        authenticator_attachment: typing.Optional[builtins.str] = None,
        avoid_same_authenticator_register: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        create_timeout: typing.Optional[jsii.Number] = None,
        relying_party_entity_name: typing.Optional[builtins.str] = None,
        relying_party_id: typing.Optional[builtins.str] = None,
        require_resident_key: typing.Optional[builtins.str] = None,
        signature_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        user_verification_requirement: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param acceptable_aaguids: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#acceptable_aaguids Realm#acceptable_aaguids}.
        :param attestation_conveyance_preference: Either none, indirect or direct. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#attestation_conveyance_preference Realm#attestation_conveyance_preference}
        :param authenticator_attachment: Either platform or cross-platform. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#authenticator_attachment Realm#authenticator_attachment}
        :param avoid_same_authenticator_register: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#avoid_same_authenticator_register Realm#avoid_same_authenticator_register}.
        :param create_timeout: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#create_timeout Realm#create_timeout}.
        :param relying_party_entity_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#relying_party_entity_name Realm#relying_party_entity_name}.
        :param relying_party_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#relying_party_id Realm#relying_party_id}.
        :param require_resident_key: Either Yes or No. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#require_resident_key Realm#require_resident_key}
        :param signature_algorithms: Keycloak lists ES256, ES384, ES512, RS256, RS384, RS512, RS1 at the time of writing. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#signature_algorithms Realm#signature_algorithms}
        :param user_verification_requirement: Either required, preferred or discouraged. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#user_verification_requirement Realm#user_verification_requirement}
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__30fec3e38de1efe6f1de806c6550317a07c434fff2e896bc5f51051375a1dee5
            )
            check_type(
                argname="argument acceptable_aaguids",
                value=acceptable_aaguids,
                expected_type=type_hints["acceptable_aaguids"],
            )
            check_type(
                argname="argument attestation_conveyance_preference",
                value=attestation_conveyance_preference,
                expected_type=type_hints["attestation_conveyance_preference"],
            )
            check_type(
                argname="argument authenticator_attachment",
                value=authenticator_attachment,
                expected_type=type_hints["authenticator_attachment"],
            )
            check_type(
                argname="argument avoid_same_authenticator_register",
                value=avoid_same_authenticator_register,
                expected_type=type_hints["avoid_same_authenticator_register"],
            )
            check_type(
                argname="argument create_timeout",
                value=create_timeout,
                expected_type=type_hints["create_timeout"],
            )
            check_type(
                argname="argument relying_party_entity_name",
                value=relying_party_entity_name,
                expected_type=type_hints["relying_party_entity_name"],
            )
            check_type(
                argname="argument relying_party_id",
                value=relying_party_id,
                expected_type=type_hints["relying_party_id"],
            )
            check_type(
                argname="argument require_resident_key",
                value=require_resident_key,
                expected_type=type_hints["require_resident_key"],
            )
            check_type(
                argname="argument signature_algorithms",
                value=signature_algorithms,
                expected_type=type_hints["signature_algorithms"],
            )
            check_type(
                argname="argument user_verification_requirement",
                value=user_verification_requirement,
                expected_type=type_hints["user_verification_requirement"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if acceptable_aaguids is not None:
            self._values["acceptable_aaguids"] = acceptable_aaguids
        if attestation_conveyance_preference is not None:
            self._values[
                "attestation_conveyance_preference"
            ] = attestation_conveyance_preference
        if authenticator_attachment is not None:
            self._values["authenticator_attachment"] = authenticator_attachment
        if avoid_same_authenticator_register is not None:
            self._values[
                "avoid_same_authenticator_register"
            ] = avoid_same_authenticator_register
        if create_timeout is not None:
            self._values["create_timeout"] = create_timeout
        if relying_party_entity_name is not None:
            self._values["relying_party_entity_name"] = relying_party_entity_name
        if relying_party_id is not None:
            self._values["relying_party_id"] = relying_party_id
        if require_resident_key is not None:
            self._values["require_resident_key"] = require_resident_key
        if signature_algorithms is not None:
            self._values["signature_algorithms"] = signature_algorithms
        if user_verification_requirement is not None:
            self._values[
                "user_verification_requirement"
            ] = user_verification_requirement

    @builtins.property
    def acceptable_aaguids(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#acceptable_aaguids Realm#acceptable_aaguids}."""
        result = self._values.get("acceptable_aaguids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def attestation_conveyance_preference(self) -> typing.Optional[builtins.str]:
        """Either none, indirect or direct.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#attestation_conveyance_preference Realm#attestation_conveyance_preference}
        """
        result = self._values.get("attestation_conveyance_preference")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def authenticator_attachment(self) -> typing.Optional[builtins.str]:
        """Either platform or cross-platform.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#authenticator_attachment Realm#authenticator_attachment}
        """
        result = self._values.get("authenticator_attachment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def avoid_same_authenticator_register(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#avoid_same_authenticator_register Realm#avoid_same_authenticator_register}."""
        result = self._values.get("avoid_same_authenticator_register")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def create_timeout(self) -> typing.Optional[jsii.Number]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#create_timeout Realm#create_timeout}."""
        result = self._values.get("create_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def relying_party_entity_name(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#relying_party_entity_name Realm#relying_party_entity_name}."""
        result = self._values.get("relying_party_entity_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def relying_party_id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#relying_party_id Realm#relying_party_id}."""
        result = self._values.get("relying_party_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def require_resident_key(self) -> typing.Optional[builtins.str]:
        """Either Yes or No.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#require_resident_key Realm#require_resident_key}
        """
        result = self._values.get("require_resident_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def signature_algorithms(self) -> typing.Optional[typing.List[builtins.str]]:
        """Keycloak lists ES256, ES384, ES512, RS256, RS384, RS512, RS1 at the time of writing.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#signature_algorithms Realm#signature_algorithms}
        """
        result = self._values.get("signature_algorithms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def user_verification_requirement(self) -> typing.Optional[builtins.str]:
        """Either required, preferred or discouraged.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#user_verification_requirement Realm#user_verification_requirement}
        """
        result = self._values.get("user_verification_requirement")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RealmWebAuthnPasswordlessPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RealmWebAuthnPasswordlessPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.realm.RealmWebAuthnPasswordlessPolicyOutputReference",
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
                _typecheckingstub__deb86a328d3f335535b31fe50040f5ca0c5094a32a6ac55bc5945ca1fce730cf
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

    @jsii.member(jsii_name="resetAcceptableAaguids")
    def reset_acceptable_aaguids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcceptableAaguids", []))

    @jsii.member(jsii_name="resetAttestationConveyancePreference")
    def reset_attestation_conveyance_preference(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetAttestationConveyancePreference", [])
        )

    @jsii.member(jsii_name="resetAuthenticatorAttachment")
    def reset_authenticator_attachment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthenticatorAttachment", []))

    @jsii.member(jsii_name="resetAvoidSameAuthenticatorRegister")
    def reset_avoid_same_authenticator_register(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetAvoidSameAuthenticatorRegister", [])
        )

    @jsii.member(jsii_name="resetCreateTimeout")
    def reset_create_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreateTimeout", []))

    @jsii.member(jsii_name="resetRelyingPartyEntityName")
    def reset_relying_party_entity_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRelyingPartyEntityName", []))

    @jsii.member(jsii_name="resetRelyingPartyId")
    def reset_relying_party_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRelyingPartyId", []))

    @jsii.member(jsii_name="resetRequireResidentKey")
    def reset_require_resident_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequireResidentKey", []))

    @jsii.member(jsii_name="resetSignatureAlgorithms")
    def reset_signature_algorithms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSignatureAlgorithms", []))

    @jsii.member(jsii_name="resetUserVerificationRequirement")
    def reset_user_verification_requirement(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetUserVerificationRequirement", [])
        )

    @builtins.property
    @jsii.member(jsii_name="acceptableAaguidsInput")
    def acceptable_aaguids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]],
            jsii.get(self, "acceptableAaguidsInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="attestationConveyancePreferenceInput")
    def attestation_conveyance_preference_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "attestationConveyancePreferenceInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="authenticatorAttachmentInput")
    def authenticator_attachment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "authenticatorAttachmentInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="avoidSameAuthenticatorRegisterInput")
    def avoid_same_authenticator_register_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "avoidSameAuthenticatorRegisterInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="createTimeoutInput")
    def create_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(
            typing.Optional[jsii.Number], jsii.get(self, "createTimeoutInput")
        )

    @builtins.property
    @jsii.member(jsii_name="relyingPartyEntityNameInput")
    def relying_party_entity_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "relyingPartyEntityNameInput")
        )

    @builtins.property
    @jsii.member(jsii_name="relyingPartyIdInput")
    def relying_party_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "relyingPartyIdInput")
        )

    @builtins.property
    @jsii.member(jsii_name="requireResidentKeyInput")
    def require_resident_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "requireResidentKeyInput")
        )

    @builtins.property
    @jsii.member(jsii_name="signatureAlgorithmsInput")
    def signature_algorithms_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]],
            jsii.get(self, "signatureAlgorithmsInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="userVerificationRequirementInput")
    def user_verification_requirement_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "userVerificationRequirementInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="acceptableAaguids")
    def acceptable_aaguids(self) -> typing.List[builtins.str]:
        return typing.cast(
            typing.List[builtins.str], jsii.get(self, "acceptableAaguids")
        )

    @acceptable_aaguids.setter
    def acceptable_aaguids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__048c87fbbb85898db23bfdde8645adfa93502cafba399957555141d3e16ea1a4
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "acceptableAaguids", value)

    @builtins.property
    @jsii.member(jsii_name="attestationConveyancePreference")
    def attestation_conveyance_preference(self) -> builtins.str:
        return typing.cast(
            builtins.str, jsii.get(self, "attestationConveyancePreference")
        )

    @attestation_conveyance_preference.setter
    def attestation_conveyance_preference(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__da72a7ec661129918889f5deea4d0d7ffdc7ddc2ec9ecde6f9c8e6315932dc54
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "attestationConveyancePreference", value)

    @builtins.property
    @jsii.member(jsii_name="authenticatorAttachment")
    def authenticator_attachment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authenticatorAttachment"))

    @authenticator_attachment.setter
    def authenticator_attachment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__12d80f004451c67665b3b38e9b01c3cc9bb38fcac77ee4653b12c63e8940bb54
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "authenticatorAttachment", value)

    @builtins.property
    @jsii.member(jsii_name="avoidSameAuthenticatorRegister")
    def avoid_same_authenticator_register(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "avoidSameAuthenticatorRegister"),
        )

    @avoid_same_authenticator_register.setter
    def avoid_same_authenticator_register(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__571a3164b83fde44c4dcaa206bba11ffe8938a836ae7d1dcc555888667f82a03
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "avoidSameAuthenticatorRegister", value)

    @builtins.property
    @jsii.member(jsii_name="createTimeout")
    def create_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "createTimeout"))

    @create_timeout.setter
    def create_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__c07ec26eab715c461bf9bc8a2f97fef638f4f3a6f5994736a2cd3e8ed01bdb6b
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "createTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="relyingPartyEntityName")
    def relying_party_entity_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "relyingPartyEntityName"))

    @relying_party_entity_name.setter
    def relying_party_entity_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__dc376acfe3e0862e6fd9ebb98a39a159277d237f7c4e655781948109675f29c2
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "relyingPartyEntityName", value)

    @builtins.property
    @jsii.member(jsii_name="relyingPartyId")
    def relying_party_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "relyingPartyId"))

    @relying_party_id.setter
    def relying_party_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__e124481f20ee9e574494df4394546d3d2eb59d85482967b5cc1d64568fe8deef
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "relyingPartyId", value)

    @builtins.property
    @jsii.member(jsii_name="requireResidentKey")
    def require_resident_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "requireResidentKey"))

    @require_resident_key.setter
    def require_resident_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__bc2cef981fde163dacec75e73d7dc4fd6a918b78cbc6413de0418160a41dece8
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "requireResidentKey", value)

    @builtins.property
    @jsii.member(jsii_name="signatureAlgorithms")
    def signature_algorithms(self) -> typing.List[builtins.str]:
        return typing.cast(
            typing.List[builtins.str], jsii.get(self, "signatureAlgorithms")
        )

    @signature_algorithms.setter
    def signature_algorithms(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d3ef744dff9584a0a70596412224eb47a603fcadb956eaee471aa73fba6b6396
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "signatureAlgorithms", value)

    @builtins.property
    @jsii.member(jsii_name="userVerificationRequirement")
    def user_verification_requirement(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userVerificationRequirement"))

    @user_verification_requirement.setter
    def user_verification_requirement(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__550b55e677b0f1dd22bd398ed8c07e285889c298af5b1198d00722604b28e516
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "userVerificationRequirement", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RealmWebAuthnPasswordlessPolicy]:
        return typing.cast(
            typing.Optional[RealmWebAuthnPasswordlessPolicy],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[RealmWebAuthnPasswordlessPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__037167ccd38b36d2134e62900016250b11da3f62e2fa893977e339843a3b65f1
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="keycloak.realm.RealmWebAuthnPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "acceptable_aaguids": "acceptableAaguids",
        "attestation_conveyance_preference": "attestationConveyancePreference",
        "authenticator_attachment": "authenticatorAttachment",
        "avoid_same_authenticator_register": "avoidSameAuthenticatorRegister",
        "create_timeout": "createTimeout",
        "relying_party_entity_name": "relyingPartyEntityName",
        "relying_party_id": "relyingPartyId",
        "require_resident_key": "requireResidentKey",
        "signature_algorithms": "signatureAlgorithms",
        "user_verification_requirement": "userVerificationRequirement",
    },
)
class RealmWebAuthnPolicy:
    def __init__(
        self,
        *,
        acceptable_aaguids: typing.Optional[typing.Sequence[builtins.str]] = None,
        attestation_conveyance_preference: typing.Optional[builtins.str] = None,
        authenticator_attachment: typing.Optional[builtins.str] = None,
        avoid_same_authenticator_register: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        create_timeout: typing.Optional[jsii.Number] = None,
        relying_party_entity_name: typing.Optional[builtins.str] = None,
        relying_party_id: typing.Optional[builtins.str] = None,
        require_resident_key: typing.Optional[builtins.str] = None,
        signature_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
        user_verification_requirement: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param acceptable_aaguids: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#acceptable_aaguids Realm#acceptable_aaguids}.
        :param attestation_conveyance_preference: Either none, indirect or direct. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#attestation_conveyance_preference Realm#attestation_conveyance_preference}
        :param authenticator_attachment: Either platform or cross-platform. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#authenticator_attachment Realm#authenticator_attachment}
        :param avoid_same_authenticator_register: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#avoid_same_authenticator_register Realm#avoid_same_authenticator_register}.
        :param create_timeout: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#create_timeout Realm#create_timeout}.
        :param relying_party_entity_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#relying_party_entity_name Realm#relying_party_entity_name}.
        :param relying_party_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#relying_party_id Realm#relying_party_id}.
        :param require_resident_key: Either Yes or No. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#require_resident_key Realm#require_resident_key}
        :param signature_algorithms: Keycloak lists ES256, ES384, ES512, RS256, RS384, RS512, RS1 at the time of writing. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#signature_algorithms Realm#signature_algorithms}
        :param user_verification_requirement: Either required, preferred or discouraged. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#user_verification_requirement Realm#user_verification_requirement}
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__2b5c469b147d061c08da6ff206dd726db54ba097ee834b26cd58e7415b837727
            )
            check_type(
                argname="argument acceptable_aaguids",
                value=acceptable_aaguids,
                expected_type=type_hints["acceptable_aaguids"],
            )
            check_type(
                argname="argument attestation_conveyance_preference",
                value=attestation_conveyance_preference,
                expected_type=type_hints["attestation_conveyance_preference"],
            )
            check_type(
                argname="argument authenticator_attachment",
                value=authenticator_attachment,
                expected_type=type_hints["authenticator_attachment"],
            )
            check_type(
                argname="argument avoid_same_authenticator_register",
                value=avoid_same_authenticator_register,
                expected_type=type_hints["avoid_same_authenticator_register"],
            )
            check_type(
                argname="argument create_timeout",
                value=create_timeout,
                expected_type=type_hints["create_timeout"],
            )
            check_type(
                argname="argument relying_party_entity_name",
                value=relying_party_entity_name,
                expected_type=type_hints["relying_party_entity_name"],
            )
            check_type(
                argname="argument relying_party_id",
                value=relying_party_id,
                expected_type=type_hints["relying_party_id"],
            )
            check_type(
                argname="argument require_resident_key",
                value=require_resident_key,
                expected_type=type_hints["require_resident_key"],
            )
            check_type(
                argname="argument signature_algorithms",
                value=signature_algorithms,
                expected_type=type_hints["signature_algorithms"],
            )
            check_type(
                argname="argument user_verification_requirement",
                value=user_verification_requirement,
                expected_type=type_hints["user_verification_requirement"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if acceptable_aaguids is not None:
            self._values["acceptable_aaguids"] = acceptable_aaguids
        if attestation_conveyance_preference is not None:
            self._values[
                "attestation_conveyance_preference"
            ] = attestation_conveyance_preference
        if authenticator_attachment is not None:
            self._values["authenticator_attachment"] = authenticator_attachment
        if avoid_same_authenticator_register is not None:
            self._values[
                "avoid_same_authenticator_register"
            ] = avoid_same_authenticator_register
        if create_timeout is not None:
            self._values["create_timeout"] = create_timeout
        if relying_party_entity_name is not None:
            self._values["relying_party_entity_name"] = relying_party_entity_name
        if relying_party_id is not None:
            self._values["relying_party_id"] = relying_party_id
        if require_resident_key is not None:
            self._values["require_resident_key"] = require_resident_key
        if signature_algorithms is not None:
            self._values["signature_algorithms"] = signature_algorithms
        if user_verification_requirement is not None:
            self._values[
                "user_verification_requirement"
            ] = user_verification_requirement

    @builtins.property
    def acceptable_aaguids(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#acceptable_aaguids Realm#acceptable_aaguids}."""
        result = self._values.get("acceptable_aaguids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def attestation_conveyance_preference(self) -> typing.Optional[builtins.str]:
        """Either none, indirect or direct.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#attestation_conveyance_preference Realm#attestation_conveyance_preference}
        """
        result = self._values.get("attestation_conveyance_preference")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def authenticator_attachment(self) -> typing.Optional[builtins.str]:
        """Either platform or cross-platform.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#authenticator_attachment Realm#authenticator_attachment}
        """
        result = self._values.get("authenticator_attachment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def avoid_same_authenticator_register(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#avoid_same_authenticator_register Realm#avoid_same_authenticator_register}."""
        result = self._values.get("avoid_same_authenticator_register")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def create_timeout(self) -> typing.Optional[jsii.Number]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#create_timeout Realm#create_timeout}."""
        result = self._values.get("create_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def relying_party_entity_name(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#relying_party_entity_name Realm#relying_party_entity_name}."""
        result = self._values.get("relying_party_entity_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def relying_party_id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#relying_party_id Realm#relying_party_id}."""
        result = self._values.get("relying_party_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def require_resident_key(self) -> typing.Optional[builtins.str]:
        """Either Yes or No.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#require_resident_key Realm#require_resident_key}
        """
        result = self._values.get("require_resident_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def signature_algorithms(self) -> typing.Optional[typing.List[builtins.str]]:
        """Keycloak lists ES256, ES384, ES512, RS256, RS384, RS512, RS1 at the time of writing.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#signature_algorithms Realm#signature_algorithms}
        """
        result = self._values.get("signature_algorithms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def user_verification_requirement(self) -> typing.Optional[builtins.str]:
        """Either required, preferred or discouraged.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm#user_verification_requirement Realm#user_verification_requirement}
        """
        result = self._values.get("user_verification_requirement")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RealmWebAuthnPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RealmWebAuthnPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.realm.RealmWebAuthnPolicyOutputReference",
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
                _typecheckingstub__4c6c3c080b60bcd327786e3f4907da59464020735316f69e96f705dacf7d45c8
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

    @jsii.member(jsii_name="resetAcceptableAaguids")
    def reset_acceptable_aaguids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcceptableAaguids", []))

    @jsii.member(jsii_name="resetAttestationConveyancePreference")
    def reset_attestation_conveyance_preference(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetAttestationConveyancePreference", [])
        )

    @jsii.member(jsii_name="resetAuthenticatorAttachment")
    def reset_authenticator_attachment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthenticatorAttachment", []))

    @jsii.member(jsii_name="resetAvoidSameAuthenticatorRegister")
    def reset_avoid_same_authenticator_register(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetAvoidSameAuthenticatorRegister", [])
        )

    @jsii.member(jsii_name="resetCreateTimeout")
    def reset_create_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreateTimeout", []))

    @jsii.member(jsii_name="resetRelyingPartyEntityName")
    def reset_relying_party_entity_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRelyingPartyEntityName", []))

    @jsii.member(jsii_name="resetRelyingPartyId")
    def reset_relying_party_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRelyingPartyId", []))

    @jsii.member(jsii_name="resetRequireResidentKey")
    def reset_require_resident_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequireResidentKey", []))

    @jsii.member(jsii_name="resetSignatureAlgorithms")
    def reset_signature_algorithms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSignatureAlgorithms", []))

    @jsii.member(jsii_name="resetUserVerificationRequirement")
    def reset_user_verification_requirement(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetUserVerificationRequirement", [])
        )

    @builtins.property
    @jsii.member(jsii_name="acceptableAaguidsInput")
    def acceptable_aaguids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]],
            jsii.get(self, "acceptableAaguidsInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="attestationConveyancePreferenceInput")
    def attestation_conveyance_preference_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "attestationConveyancePreferenceInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="authenticatorAttachmentInput")
    def authenticator_attachment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "authenticatorAttachmentInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="avoidSameAuthenticatorRegisterInput")
    def avoid_same_authenticator_register_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "avoidSameAuthenticatorRegisterInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="createTimeoutInput")
    def create_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(
            typing.Optional[jsii.Number], jsii.get(self, "createTimeoutInput")
        )

    @builtins.property
    @jsii.member(jsii_name="relyingPartyEntityNameInput")
    def relying_party_entity_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "relyingPartyEntityNameInput")
        )

    @builtins.property
    @jsii.member(jsii_name="relyingPartyIdInput")
    def relying_party_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "relyingPartyIdInput")
        )

    @builtins.property
    @jsii.member(jsii_name="requireResidentKeyInput")
    def require_resident_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "requireResidentKeyInput")
        )

    @builtins.property
    @jsii.member(jsii_name="signatureAlgorithmsInput")
    def signature_algorithms_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]],
            jsii.get(self, "signatureAlgorithmsInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="userVerificationRequirementInput")
    def user_verification_requirement_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "userVerificationRequirementInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="acceptableAaguids")
    def acceptable_aaguids(self) -> typing.List[builtins.str]:
        return typing.cast(
            typing.List[builtins.str], jsii.get(self, "acceptableAaguids")
        )

    @acceptable_aaguids.setter
    def acceptable_aaguids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__6b80eb4bebc91b4b1626c47217b5624e075628965100bdbb834b72b75821e984
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "acceptableAaguids", value)

    @builtins.property
    @jsii.member(jsii_name="attestationConveyancePreference")
    def attestation_conveyance_preference(self) -> builtins.str:
        return typing.cast(
            builtins.str, jsii.get(self, "attestationConveyancePreference")
        )

    @attestation_conveyance_preference.setter
    def attestation_conveyance_preference(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__5d2a6a6f18e8133f53104b5ee3c01668cbd89d5580e4ead1a7e2f2a9fcfddf3a
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "attestationConveyancePreference", value)

    @builtins.property
    @jsii.member(jsii_name="authenticatorAttachment")
    def authenticator_attachment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authenticatorAttachment"))

    @authenticator_attachment.setter
    def authenticator_attachment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__4c1df1c08a0308e50d6aff6b587b9bc4bc20c793af4c6e2820e09f42f968be07
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "authenticatorAttachment", value)

    @builtins.property
    @jsii.member(jsii_name="avoidSameAuthenticatorRegister")
    def avoid_same_authenticator_register(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "avoidSameAuthenticatorRegister"),
        )

    @avoid_same_authenticator_register.setter
    def avoid_same_authenticator_register(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__8caffd61f7dfd27bc53a259db891b9cd3175aca4febbf637dc0fe925f59a7b77
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "avoidSameAuthenticatorRegister", value)

    @builtins.property
    @jsii.member(jsii_name="createTimeout")
    def create_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "createTimeout"))

    @create_timeout.setter
    def create_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__304eb56a4278d5909e6126ab003fcbc71f00777c103b4a99dedb5a80d6b7931c
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "createTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="relyingPartyEntityName")
    def relying_party_entity_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "relyingPartyEntityName"))

    @relying_party_entity_name.setter
    def relying_party_entity_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__5aaeb7981ae4ad4f56c98e10858eea34be4d1ad44991112aa2141f36af39973e
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "relyingPartyEntityName", value)

    @builtins.property
    @jsii.member(jsii_name="relyingPartyId")
    def relying_party_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "relyingPartyId"))

    @relying_party_id.setter
    def relying_party_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__15fe3c45c395e1749ab2c1db75f418a99068a4c4f5df97400b6180f0e32a47ed
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "relyingPartyId", value)

    @builtins.property
    @jsii.member(jsii_name="requireResidentKey")
    def require_resident_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "requireResidentKey"))

    @require_resident_key.setter
    def require_resident_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__e051ba32ffb033ce4a1e55285aa0830ab4c62a64dfe1f230029bf2d9f1a11c1e
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "requireResidentKey", value)

    @builtins.property
    @jsii.member(jsii_name="signatureAlgorithms")
    def signature_algorithms(self) -> typing.List[builtins.str]:
        return typing.cast(
            typing.List[builtins.str], jsii.get(self, "signatureAlgorithms")
        )

    @signature_algorithms.setter
    def signature_algorithms(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b17f4b88923d004cd3cb22ecfb2bff8c1c451193f15127894edf522ca43c5966
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "signatureAlgorithms", value)

    @builtins.property
    @jsii.member(jsii_name="userVerificationRequirement")
    def user_verification_requirement(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userVerificationRequirement"))

    @user_verification_requirement.setter
    def user_verification_requirement(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__42929530138d1f8e36c48ba65bc015d2b452cccce7c0391ffeec9d783ee7bf40
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "userVerificationRequirement", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RealmWebAuthnPolicy]:
        return typing.cast(
            typing.Optional[RealmWebAuthnPolicy], jsii.get(self, "internalValue")
        )

    @internal_value.setter
    def internal_value(self, value: typing.Optional[RealmWebAuthnPolicy]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__42b1ac7f5591d8c906fce9127039c3e286a0f00145f03ace678807a049bc79ea
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


__all__ = [
    "Realm",
    "RealmConfig",
    "RealmInternationalization",
    "RealmInternationalizationOutputReference",
    "RealmOtpPolicy",
    "RealmOtpPolicyOutputReference",
    "RealmSecurityDefenses",
    "RealmSecurityDefensesBruteForceDetection",
    "RealmSecurityDefensesBruteForceDetectionOutputReference",
    "RealmSecurityDefensesHeaders",
    "RealmSecurityDefensesHeadersOutputReference",
    "RealmSecurityDefensesOutputReference",
    "RealmSmtpServer",
    "RealmSmtpServerAuth",
    "RealmSmtpServerAuthOutputReference",
    "RealmSmtpServerOutputReference",
    "RealmWebAuthnPasswordlessPolicy",
    "RealmWebAuthnPasswordlessPolicyOutputReference",
    "RealmWebAuthnPolicy",
    "RealmWebAuthnPolicyOutputReference",
]

publication.publish()


def _typecheckingstub__3884c9ca449eb14a5003cf4a9e6dd8be906cad1cc4bce9dc8927112aab746bff(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    realm: builtins.str,
    access_code_lifespan: typing.Optional[builtins.str] = None,
    access_code_lifespan_login: typing.Optional[builtins.str] = None,
    access_code_lifespan_user_action: typing.Optional[builtins.str] = None,
    access_token_lifespan: typing.Optional[builtins.str] = None,
    access_token_lifespan_for_implicit_flow: typing.Optional[builtins.str] = None,
    account_theme: typing.Optional[builtins.str] = None,
    action_token_generated_by_admin_lifespan: typing.Optional[builtins.str] = None,
    action_token_generated_by_user_lifespan: typing.Optional[builtins.str] = None,
    admin_theme: typing.Optional[builtins.str] = None,
    attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    browser_flow: typing.Optional[builtins.str] = None,
    client_authentication_flow: typing.Optional[builtins.str] = None,
    client_session_idle_timeout: typing.Optional[builtins.str] = None,
    client_session_max_lifespan: typing.Optional[builtins.str] = None,
    default_default_client_scopes: typing.Optional[
        typing.Sequence[builtins.str]
    ] = None,
    default_optional_client_scopes: typing.Optional[
        typing.Sequence[builtins.str]
    ] = None,
    default_signature_algorithm: typing.Optional[builtins.str] = None,
    direct_grant_flow: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    display_name_html: typing.Optional[builtins.str] = None,
    docker_authentication_flow: typing.Optional[builtins.str] = None,
    duplicate_emails_allowed: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    edit_username_allowed: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    email_theme: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    id: typing.Optional[builtins.str] = None,
    internal_id: typing.Optional[builtins.str] = None,
    internationalization: typing.Optional[
        typing.Union[RealmInternationalization, typing.Dict[builtins.str, typing.Any]]
    ] = None,
    login_theme: typing.Optional[builtins.str] = None,
    login_with_email_allowed: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    oauth2_device_code_lifespan: typing.Optional[builtins.str] = None,
    oauth2_device_polling_interval: typing.Optional[jsii.Number] = None,
    offline_session_idle_timeout: typing.Optional[builtins.str] = None,
    offline_session_max_lifespan: typing.Optional[builtins.str] = None,
    offline_session_max_lifespan_enabled: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    otp_policy: typing.Optional[
        typing.Union[RealmOtpPolicy, typing.Dict[builtins.str, typing.Any]]
    ] = None,
    password_policy: typing.Optional[builtins.str] = None,
    refresh_token_max_reuse: typing.Optional[jsii.Number] = None,
    registration_allowed: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    registration_email_as_username: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    registration_flow: typing.Optional[builtins.str] = None,
    remember_me: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    reset_credentials_flow: typing.Optional[builtins.str] = None,
    reset_password_allowed: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    revoke_refresh_token: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    security_defenses: typing.Optional[
        typing.Union[RealmSecurityDefenses, typing.Dict[builtins.str, typing.Any]]
    ] = None,
    smtp_server: typing.Optional[
        typing.Union[RealmSmtpServer, typing.Dict[builtins.str, typing.Any]]
    ] = None,
    ssl_required: typing.Optional[builtins.str] = None,
    sso_session_idle_timeout: typing.Optional[builtins.str] = None,
    sso_session_idle_timeout_remember_me: typing.Optional[builtins.str] = None,
    sso_session_max_lifespan: typing.Optional[builtins.str] = None,
    sso_session_max_lifespan_remember_me: typing.Optional[builtins.str] = None,
    user_managed_access: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    verify_email: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    web_authn_passwordless_policy: typing.Optional[
        typing.Union[
            RealmWebAuthnPasswordlessPolicy, typing.Dict[builtins.str, typing.Any]
        ]
    ] = None,
    web_authn_policy: typing.Optional[
        typing.Union[RealmWebAuthnPolicy, typing.Dict[builtins.str, typing.Any]]
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


def _typecheckingstub__4efff962e4bd300f374e414a220e9d866949f903bca2e248ac330ef95bdaebfe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__86e316ca73cd9630d38187e69d67cd95e11cf4a1e77d5de54c71d9b17e2d3bc7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ec9320a12ae161db794450a3921ec2efabaf1a43cd5388ef666d332c621ed876(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d5ec6b81495fd42e38b2c2fb0bfdf6ea441333b905f996f8e24a0aada769da2c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__db4ee232a0635d41812a7d5c35ae9ab0e005ed62826004b46c0e93fc62f225eb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b83590f5078715338f047a5b6dd38a8a06994070b4d90dbb7b602cc540176c1d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__47f68b1d0bc4a48746793c9152307b61e626a993e81cde2262c8478869ceea75(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a7b44e8dd5cdac65963743fba935a4b904d2446995792e28852035da7c0e18a4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__2a4fd3f52a8d5f0296d732c68e62e19fd3718bca08032ced2a32954501c4f91f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e1b3cb4b6cda8d217ec50331f039a2e8082024f76ebfd7f82ac6ca5fe790a5af(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d9b45f952efc5f43c46890bcc417f4f50aae588e97886317ff6db60707b9376c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__fb9259639782ba4f95809a3b43467fe3669a8077384ee4f622668d3e7fcdd801(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b671e68bdc74504f61f72c63dc2895eda0e901cfb173c5c9dfd7364e7383ad11(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__391a826fefc8eaf8a4aced7d829f2899fff625bf2a305df859a8701447ad6e9c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d26a828a4c4d30f00392d9208746de7dc26f09a8cb48f174b90434fba969106c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8015412d14543cfc1494322d20f962dee3b491bc36dd2cbdf8ece717b7ef1e7e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__db2c4f995dc204d42c1416213895f9a8b739f0750757438e2e95b6f355d560b1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__5a780941836b54d3fd9557a7cf6377c7ce206babbd72edbbd45d84b21512337f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__bdcc88b646f345f19db9b382d600d62b3ccfc70a2ed47372119bbfb67f688f9c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__80789a7175c3ec01c637bb3a7952156c6db63b5199cbe9a1aa92d2b8bfe59935(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__29ef7d9b2e4f1a93c4b917ce928e7328570f89eb82b6ea7a1a88e18f6e9d9243(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a26862e4a2007c2c1e0316b7ce79ad2a02fa112feed9ef3e882a6ce72e424756(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__caa421a139755aeb9c8975d5d324b1ead9d2b73f959dce9845b772ddd2275bb0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3dabdd7b04eaf76bdb10de9c7603523681d25f90faec63f7f6f326ed42399672(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__60b55c532ab0a8770d0b03a6bcb226f956d74c8c2a06266a052f6e17f15b4d77(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d4773891b72ecc0d05c2713e857ddcb8b3c8912c55cb1525faf39360961b08c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b160919c6b300e9b23e6aefeb7a5a93c131505f31cdc0207ca769d258a52bfa1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3a423024e3c28e3333258ba58cd26fae5bcf8e416207e21d40dc1113c92958c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3573a19e26ea0f2d1b94269ce06afc13117ea6790053b316ddd4709b9a022257(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d66bc4eba8def70dd798430e5c8a162c575ad5fc6ff03c28bde2aac8c6f1a202(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__071b008188bc5347eec40ca8552bf64586f5b5fadeab0b5e9c0349757e752f3b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a778fcb47fbba7095b9894be5fbb8a41cefb396d0c8f04e635d3b78f8ba8b5b5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d6632f60953ec77de327b82fc8e2558299b55451b5174ded8784c0b59b0a6f79(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7b66b1a999513e1630443529ab2cd80c6ae73606c4d14bc514818a58f1ec716e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d8c02a71cc8b4f38d86d88d09240feecdae71c26f0ff04ced2491a67c6ba8558(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__2c8aad4a7e393c01bef949b1a5e7909fae6a35e328dd0762757826268792b9b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__494523c218ae47b190e3443e34fd6c7a6bc91a03965bb1a9cc0305ddf37154ae(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__29346830421cb5a106f84d810ed52aec6f25b7d11a366b316afcf38f4a8dd086(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__62afce0efa55d2cea1123911b06ca8c64ad28bd47d25d0ae63573218e391f2a6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__2e09dbcca9be5ea274fd0b8d40908be00ff6ced221b0bbd040a5fcb38059b390(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__daa614f5432bb09427b0f97ad3e7272708534a11b6f4a2d6a89e00c84dae1985(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__248e0c9aade6ee6a877068d57935f2a9802e873ce9c8b55c2c6c6c3acfda3e01(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__bf69e0f0b12a90dc2a50116c58849d86acad201d92a22e51d729a5f755901e8a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f51a8645decd8f777be02ffe9b32beb76758818168c1a76d835a12c76e6b72ac(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__550a66edbf13bb4be7b8f4279b3e3d6eb95b2d79ab2c416216b2d4007bed3da7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0cc04ba50537f9687df4b40ea30ef0bb92f275d2b610aab08e1670169d0e9490(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7fd08b9cfebdad9aa94805b012ed9ae17625536e27c5b2589a41862ae232ecf0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__511a507599a9c1e044fd95b9f31b71579b29c3202556991c67f75543d64bca6b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__dc6978ae6cfe8c776bd581acd4b7c9f3dfc25f41152e7941f01d2e2125520da0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1de33be22bcec879f3ba3d72f715d4748381e0632e812857f61f1ab864c3d7ac(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9d97db664249b19e0087c1e8b9b4dab4e90760e5d1fe0189e12b58042c2570d6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f805730adb3685af83d5cf884414d8f42c4dfadb884bbbd7a9e1fd9c9a630b19(
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
    realm: builtins.str,
    access_code_lifespan: typing.Optional[builtins.str] = None,
    access_code_lifespan_login: typing.Optional[builtins.str] = None,
    access_code_lifespan_user_action: typing.Optional[builtins.str] = None,
    access_token_lifespan: typing.Optional[builtins.str] = None,
    access_token_lifespan_for_implicit_flow: typing.Optional[builtins.str] = None,
    account_theme: typing.Optional[builtins.str] = None,
    action_token_generated_by_admin_lifespan: typing.Optional[builtins.str] = None,
    action_token_generated_by_user_lifespan: typing.Optional[builtins.str] = None,
    admin_theme: typing.Optional[builtins.str] = None,
    attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    browser_flow: typing.Optional[builtins.str] = None,
    client_authentication_flow: typing.Optional[builtins.str] = None,
    client_session_idle_timeout: typing.Optional[builtins.str] = None,
    client_session_max_lifespan: typing.Optional[builtins.str] = None,
    default_default_client_scopes: typing.Optional[
        typing.Sequence[builtins.str]
    ] = None,
    default_optional_client_scopes: typing.Optional[
        typing.Sequence[builtins.str]
    ] = None,
    default_signature_algorithm: typing.Optional[builtins.str] = None,
    direct_grant_flow: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    display_name_html: typing.Optional[builtins.str] = None,
    docker_authentication_flow: typing.Optional[builtins.str] = None,
    duplicate_emails_allowed: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    edit_username_allowed: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    email_theme: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    id: typing.Optional[builtins.str] = None,
    internal_id: typing.Optional[builtins.str] = None,
    internationalization: typing.Optional[
        typing.Union[RealmInternationalization, typing.Dict[builtins.str, typing.Any]]
    ] = None,
    login_theme: typing.Optional[builtins.str] = None,
    login_with_email_allowed: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    oauth2_device_code_lifespan: typing.Optional[builtins.str] = None,
    oauth2_device_polling_interval: typing.Optional[jsii.Number] = None,
    offline_session_idle_timeout: typing.Optional[builtins.str] = None,
    offline_session_max_lifespan: typing.Optional[builtins.str] = None,
    offline_session_max_lifespan_enabled: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    otp_policy: typing.Optional[
        typing.Union[RealmOtpPolicy, typing.Dict[builtins.str, typing.Any]]
    ] = None,
    password_policy: typing.Optional[builtins.str] = None,
    refresh_token_max_reuse: typing.Optional[jsii.Number] = None,
    registration_allowed: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    registration_email_as_username: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    registration_flow: typing.Optional[builtins.str] = None,
    remember_me: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    reset_credentials_flow: typing.Optional[builtins.str] = None,
    reset_password_allowed: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    revoke_refresh_token: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    security_defenses: typing.Optional[
        typing.Union[RealmSecurityDefenses, typing.Dict[builtins.str, typing.Any]]
    ] = None,
    smtp_server: typing.Optional[
        typing.Union[RealmSmtpServer, typing.Dict[builtins.str, typing.Any]]
    ] = None,
    ssl_required: typing.Optional[builtins.str] = None,
    sso_session_idle_timeout: typing.Optional[builtins.str] = None,
    sso_session_idle_timeout_remember_me: typing.Optional[builtins.str] = None,
    sso_session_max_lifespan: typing.Optional[builtins.str] = None,
    sso_session_max_lifespan_remember_me: typing.Optional[builtins.str] = None,
    user_managed_access: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    verify_email: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    web_authn_passwordless_policy: typing.Optional[
        typing.Union[
            RealmWebAuthnPasswordlessPolicy, typing.Dict[builtins.str, typing.Any]
        ]
    ] = None,
    web_authn_policy: typing.Optional[
        typing.Union[RealmWebAuthnPolicy, typing.Dict[builtins.str, typing.Any]]
    ] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6dd4f6627bd28ee20348ba444f579346e718e203c4db223fc0f0d8093b48de6c(
    *,
    default_locale: builtins.str,
    supported_locales: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0a7f1f5f64c7b0647913ccb1c5abe3db7bd5fe4460dc1cff7277ef0176478652(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__83420ba5444da2f7de889e34c0d687fbd5e9c4c4379361f9a2b99f6c15afa44e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__11e9cd95a413d1ab7c02fb6013cb2c9ce6c80a282f221a2584246fdfc29639a0(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__cd0951b936206e6e3c06e89bf37f021a7cc6ecabab58f0d4388b9356f9399a89(
    value: typing.Optional[RealmInternationalization],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f3a18dd93751c6a28d5a2bb2ac56e4ffd65f0ce17e536d1f0c121a7f43af42ac(
    *,
    algorithm: typing.Optional[builtins.str] = None,
    digits: typing.Optional[jsii.Number] = None,
    initial_counter: typing.Optional[jsii.Number] = None,
    look_ahead_window: typing.Optional[jsii.Number] = None,
    period: typing.Optional[jsii.Number] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f658acb205f2034438bc37d3c668102e9462f2ee8691c0d8c5835dd8d8d284f8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__22dcc86babcb116596c32a7d968fc4fce32357eba6b4d557e35bb6381b7a8caf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__82b460c603a445f76df73699063253ae69ce9a09292be3e2ef27c119d7155e76(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e7982e0f96117b343c40eef2a2d7c7048b513ed7b7a018e8c4c5322d2bdd314c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8556587d3e94e2cbffe30e773af1079b4fa99e84f3332f0a26959dcae5a0b55a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__cc4346e29f3801b10901daec645d74fb0c8c1f0b84fe50aa26cfdc64d1253331(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a0739bf7ef32ff3e15a516a0ee91ab5508340fa329ab50f5a5bbcb885e989cb3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a09ee5bae6721a9951ca4f248aff4c5889b030b90e2750c298969c71dabf27d7(
    value: typing.Optional[RealmOtpPolicy],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d6679f0e896343b2f8cc320f20c130e6396ecf73e9d7e6483ddb2d2f4669be09(
    *,
    brute_force_detection: typing.Optional[
        typing.Union[
            RealmSecurityDefensesBruteForceDetection,
            typing.Dict[builtins.str, typing.Any],
        ]
    ] = None,
    headers: typing.Optional[
        typing.Union[
            RealmSecurityDefensesHeaders, typing.Dict[builtins.str, typing.Any]
        ]
    ] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ef5bd84bf8b5c8d7c82a4688f46abdc996d1c4fadc6316825c3f7a356e3e2db0(
    *,
    failure_reset_time_seconds: typing.Optional[jsii.Number] = None,
    max_failure_wait_seconds: typing.Optional[jsii.Number] = None,
    max_login_failures: typing.Optional[jsii.Number] = None,
    minimum_quick_login_wait_seconds: typing.Optional[jsii.Number] = None,
    permanent_lockout: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    quick_login_check_milli_seconds: typing.Optional[jsii.Number] = None,
    wait_increment_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__2fa67aa3a74f13e605249752f3a507f52ccaf4d4b29d3442fa0350bcae78b879(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__afb545db1f8766c0500bb529c2ab1ba1705eae342de5faecb3f8f6ef679ab352(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9cc2cb48c6af028b066d10c10b2f098fb9d7f22b1903b11f8ce8ce38fbeb89a0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__34c2a121d92d6a6bcf7eb8e1cb660bbcb15ecf9cd1d8f79b689a012c7fbd7f22(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d606effd4bdec899fe55fb7dedce9f3ef672cd43d192effb1badcdc49de4afc4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__62bc4f7f1c5e95cc3458b752a85ed886adadefa4f79f1294cfe9936aeaa30e69(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9bdf137380e1add889ad07dc9723eda73280dd9eb8a877570d5a6dc43952d38a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6791ef3a74d47fb619ddc189c1bfab787779adf80c599e1a8e4556689b3c1dff(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__85097f0da85805cfbd5a6dc654368abf27a1b898dfaab752cdbc7d1dd1d13af7(
    value: typing.Optional[RealmSecurityDefensesBruteForceDetection],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4fa14a9260df05ead6519b88636257662e99e7c6532f7ece64fec4661e63ec26(
    *,
    content_security_policy: typing.Optional[builtins.str] = None,
    content_security_policy_report_only: typing.Optional[builtins.str] = None,
    strict_transport_security: typing.Optional[builtins.str] = None,
    x_content_type_options: typing.Optional[builtins.str] = None,
    x_frame_options: typing.Optional[builtins.str] = None,
    x_robots_tag: typing.Optional[builtins.str] = None,
    x_xss_protection: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6741714819ca4186bfcd6f98b1a0df6d66919b1f01bc08ff53e3c0b3a884f301(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e4ee15fd3270196fc84b88245748c7b96d9e5ebccb07ec928678d6c7d7f01607(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d4afa19c885394bdfa6c8c554fa327789d1cf392ae4f2231109c6575207be015(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__534cd2bb5c6936edb819647e86911072aa7eefaf6f14c7c1ed8253ec9c5c73b3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6ae6f69bf72d5707a20d25006c05592a103c3ad053b470879fba844b57a189f0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__69438a514d9779a20cdb1a1de32c427ac6bd2349b61bed5bb85b9702bc56dbd1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__76f19d42c183a803cb4a592022a5b153729a0c7eb3c9d252c7f778b984613a64(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c8f0d1ee62a84cfcad410eaa3ec74fc81d96a7ce46abbbc854f3fde2c6171280(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9973ae0a5607bda6bda2981219cf4443b8631f9b6c8f23f53abb0f237d876667(
    value: typing.Optional[RealmSecurityDefensesHeaders],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__53b0fa7b057855b8992dc8e300d2b51d5edcca55c44d59ede5e761fa4c2c3106(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f5a6f94637c2e90f1c80bdc3e411c0f592ab4134568fa605c1381b4e288bfd74(
    value: typing.Optional[RealmSecurityDefenses],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__020a95d653ec80b514b6858618290075cbd70cf9efa6e3fa7d5b45e6171ee29b(
    *,
    from_: builtins.str,
    host: builtins.str,
    auth: typing.Optional[
        typing.Union[RealmSmtpServerAuth, typing.Dict[builtins.str, typing.Any]]
    ] = None,
    envelope_from: typing.Optional[builtins.str] = None,
    from_display_name: typing.Optional[builtins.str] = None,
    port: typing.Optional[builtins.str] = None,
    reply_to: typing.Optional[builtins.str] = None,
    reply_to_display_name: typing.Optional[builtins.str] = None,
    ssl: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    starttls: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3d33466dc7c6980f71c41b55c0f810061e3fd7eac15f09ff3bc15969465f511c(
    *,
    password: builtins.str,
    username: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__85c131dfcedb6312f008a078e981f0212aded896f2e0837593c685e04e2a2b36(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__89f7191a92ca02489787c3b25a85c18c936cfede89567fb512e895e839a27be1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ec6087810323bf717edd0f0844f30945c2f5ec9f73433ae0b1357865be149313(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3370762a7f7ac4feaacb38bf35c9383bab9b2e54e995efb87e50fb33d2c4d83d(
    value: typing.Optional[RealmSmtpServerAuth],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ecdbfb28a26f3f484ac082a74598a4b498846a78f345973377d20a3ffd2f210b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7d730330a62129e0ca832459ecfa4cd355ed2a069c164f6420270f5e94a4410d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8ad957d393246c7368cc83b15dc4b21bbc5860fc88fd9aa3c4ed418611c62506(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__446226912c77b2da81b763fbcca8bc1733fd29510b009f97a24b54253dfec97d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__91633f39b7ab215b26c9fb57addeb5aff9984872d321ec2c7bf204088887a602(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__2f7e0758f5f7f962c726d5afc7cccd4370d662111fd82f0e66af1ae5f4670039(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9d0c64568c00bca2a33f624a2514028b77ccb2c95ac8855759910564ad8e4f0b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6856f53dc29f77a7f016644f39f036dd1e06bfa6b6e7e932c9aa3775013b3557(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d2f360f0ffb2d83cfb7449c3a85eef7d5c336a83998959cd64a0d972214616ce(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ec6006e328612384216868a727008c8a84dc9ab46e7f029a52efc70b8339f86b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e230aa3b0bcd970737bfe1efee7627cfb2015ff4aad18162e2396deeb8523276(
    value: typing.Optional[RealmSmtpServer],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__30fec3e38de1efe6f1de806c6550317a07c434fff2e896bc5f51051375a1dee5(
    *,
    acceptable_aaguids: typing.Optional[typing.Sequence[builtins.str]] = None,
    attestation_conveyance_preference: typing.Optional[builtins.str] = None,
    authenticator_attachment: typing.Optional[builtins.str] = None,
    avoid_same_authenticator_register: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    create_timeout: typing.Optional[jsii.Number] = None,
    relying_party_entity_name: typing.Optional[builtins.str] = None,
    relying_party_id: typing.Optional[builtins.str] = None,
    require_resident_key: typing.Optional[builtins.str] = None,
    signature_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
    user_verification_requirement: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__deb86a328d3f335535b31fe50040f5ca0c5094a32a6ac55bc5945ca1fce730cf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__048c87fbbb85898db23bfdde8645adfa93502cafba399957555141d3e16ea1a4(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__da72a7ec661129918889f5deea4d0d7ffdc7ddc2ec9ecde6f9c8e6315932dc54(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__12d80f004451c67665b3b38e9b01c3cc9bb38fcac77ee4653b12c63e8940bb54(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__571a3164b83fde44c4dcaa206bba11ffe8938a836ae7d1dcc555888667f82a03(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c07ec26eab715c461bf9bc8a2f97fef638f4f3a6f5994736a2cd3e8ed01bdb6b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__dc376acfe3e0862e6fd9ebb98a39a159277d237f7c4e655781948109675f29c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e124481f20ee9e574494df4394546d3d2eb59d85482967b5cc1d64568fe8deef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__bc2cef981fde163dacec75e73d7dc4fd6a918b78cbc6413de0418160a41dece8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d3ef744dff9584a0a70596412224eb47a603fcadb956eaee471aa73fba6b6396(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__550b55e677b0f1dd22bd398ed8c07e285889c298af5b1198d00722604b28e516(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__037167ccd38b36d2134e62900016250b11da3f62e2fa893977e339843a3b65f1(
    value: typing.Optional[RealmWebAuthnPasswordlessPolicy],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__2b5c469b147d061c08da6ff206dd726db54ba097ee834b26cd58e7415b837727(
    *,
    acceptable_aaguids: typing.Optional[typing.Sequence[builtins.str]] = None,
    attestation_conveyance_preference: typing.Optional[builtins.str] = None,
    authenticator_attachment: typing.Optional[builtins.str] = None,
    avoid_same_authenticator_register: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    create_timeout: typing.Optional[jsii.Number] = None,
    relying_party_entity_name: typing.Optional[builtins.str] = None,
    relying_party_id: typing.Optional[builtins.str] = None,
    require_resident_key: typing.Optional[builtins.str] = None,
    signature_algorithms: typing.Optional[typing.Sequence[builtins.str]] = None,
    user_verification_requirement: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4c6c3c080b60bcd327786e3f4907da59464020735316f69e96f705dacf7d45c8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6b80eb4bebc91b4b1626c47217b5624e075628965100bdbb834b72b75821e984(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__5d2a6a6f18e8133f53104b5ee3c01668cbd89d5580e4ead1a7e2f2a9fcfddf3a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4c1df1c08a0308e50d6aff6b587b9bc4bc20c793af4c6e2820e09f42f968be07(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8caffd61f7dfd27bc53a259db891b9cd3175aca4febbf637dc0fe925f59a7b77(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__304eb56a4278d5909e6126ab003fcbc71f00777c103b4a99dedb5a80d6b7931c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__5aaeb7981ae4ad4f56c98e10858eea34be4d1ad44991112aa2141f36af39973e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__15fe3c45c395e1749ab2c1db75f418a99068a4c4f5df97400b6180f0e32a47ed(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e051ba32ffb033ce4a1e55285aa0830ab4c62a64dfe1f230029bf2d9f1a11c1e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b17f4b88923d004cd3cb22ecfb2bff8c1c451193f15127894edf522ca43c5966(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__42929530138d1f8e36c48ba65bc015d2b452cccce7c0391ffeec9d783ee7bf40(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__42b1ac7f5591d8c906fce9127039c3e286a0f00145f03ace678807a049bc79ea(
    value: typing.Optional[RealmWebAuthnPolicy],
) -> None:
    """Type checking stubs"""
    pass
