"""
# `data_keycloak_realm`

Refer to the Terraform Registory for docs: [`data_keycloak_realm`](https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm).
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


class DataKeycloakRealm(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.dataKeycloakRealm.DataKeycloakRealm",
):
    """Represents a {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm keycloak_realm}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        realm: builtins.str,
        attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        default_default_client_scopes: typing.Optional[
            typing.Sequence[builtins.str]
        ] = None,
        default_optional_client_scopes: typing.Optional[
            typing.Sequence[builtins.str]
        ] = None,
        display_name_html: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        internationalization: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable,
                typing.Sequence[
                    typing.Union[
                        "DataKeycloakRealmInternationalization",
                        typing.Dict[builtins.str, typing.Any],
                    ]
                ],
            ]
        ] = None,
        otp_policy: typing.Optional[
            typing.Union[
                "DataKeycloakRealmOtpPolicy", typing.Dict[builtins.str, typing.Any]
            ]
        ] = None,
        security_defenses: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable,
                typing.Sequence[
                    typing.Union[
                        "DataKeycloakRealmSecurityDefenses",
                        typing.Dict[builtins.str, typing.Any],
                    ]
                ],
            ]
        ] = None,
        smtp_server: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable,
                typing.Sequence[
                    typing.Union[
                        "DataKeycloakRealmSmtpServer",
                        typing.Dict[builtins.str, typing.Any],
                    ]
                ],
            ]
        ] = None,
        web_authn_passwordless_policy: typing.Optional[
            typing.Union[
                "DataKeycloakRealmWebAuthnPasswordlessPolicy",
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        web_authn_policy: typing.Optional[
            typing.Union[
                "DataKeycloakRealmWebAuthnPolicy", typing.Dict[builtins.str, typing.Any]
            ]
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
        """Create a new {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm keycloak_realm} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param realm: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#realm DataKeycloakRealm#realm}.
        :param attributes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#attributes DataKeycloakRealm#attributes}.
        :param default_default_client_scopes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#default_default_client_scopes DataKeycloakRealm#default_default_client_scopes}.
        :param default_optional_client_scopes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#default_optional_client_scopes DataKeycloakRealm#default_optional_client_scopes}.
        :param display_name_html: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#display_name_html DataKeycloakRealm#display_name_html}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#id DataKeycloakRealm#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param internationalization: internationalization block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#internationalization DataKeycloakRealm#internationalization}
        :param otp_policy: otp_policy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#otp_policy DataKeycloakRealm#otp_policy}
        :param security_defenses: security_defenses block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#security_defenses DataKeycloakRealm#security_defenses}
        :param smtp_server: smtp_server block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#smtp_server DataKeycloakRealm#smtp_server}
        :param web_authn_passwordless_policy: web_authn_passwordless_policy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#web_authn_passwordless_policy DataKeycloakRealm#web_authn_passwordless_policy}
        :param web_authn_policy: web_authn_policy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#web_authn_policy DataKeycloakRealm#web_authn_policy}
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
                _typecheckingstub__c9d6615c6488c13aa54ccc170a52a626100cdd5bf9b8bdb435544a9be69c4219
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(
                argname="argument id_", value=id_, expected_type=type_hints["id_"]
            )
        config = DataKeycloakRealmConfig(
            realm=realm,
            attributes=attributes,
            default_default_client_scopes=default_default_client_scopes,
            default_optional_client_scopes=default_optional_client_scopes,
            display_name_html=display_name_html,
            id=id,
            internationalization=internationalization,
            otp_policy=otp_policy,
            security_defenses=security_defenses,
            smtp_server=smtp_server,
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
        value: typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    "DataKeycloakRealmInternationalization",
                    typing.Dict[builtins.str, typing.Any],
                ]
            ],
        ],
    ) -> None:
        """
        :param value: -
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__fc844c7114c8893d9ae65ac56796e3a6b3732d31f270efde8aa2b90171341c53
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        return typing.cast(None, jsii.invoke(self, "putInternationalization", [value]))

    @jsii.member(jsii_name="putOtpPolicy")
    def put_otp_policy(self) -> None:
        value = DataKeycloakRealmOtpPolicy()

        return typing.cast(None, jsii.invoke(self, "putOtpPolicy", [value]))

    @jsii.member(jsii_name="putSecurityDefenses")
    def put_security_defenses(
        self,
        value: typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    "DataKeycloakRealmSecurityDefenses",
                    typing.Dict[builtins.str, typing.Any],
                ]
            ],
        ],
    ) -> None:
        """
        :param value: -
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__2d886d7ad6afec0644ad24dad0ed2e54008b5b8ed05429b228ca8f89f1f36792
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        return typing.cast(None, jsii.invoke(self, "putSecurityDefenses", [value]))

    @jsii.member(jsii_name="putSmtpServer")
    def put_smtp_server(
        self,
        value: typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    "DataKeycloakRealmSmtpServer", typing.Dict[builtins.str, typing.Any]
                ]
            ],
        ],
    ) -> None:
        """
        :param value: -
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__37648ab3a9b72fc767782d6b81e1e585a8df75e50cea40642ab7bc57a38f794a
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        return typing.cast(None, jsii.invoke(self, "putSmtpServer", [value]))

    @jsii.member(jsii_name="putWebAuthnPasswordlessPolicy")
    def put_web_authn_passwordless_policy(self) -> None:
        value = DataKeycloakRealmWebAuthnPasswordlessPolicy()

        return typing.cast(
            None, jsii.invoke(self, "putWebAuthnPasswordlessPolicy", [value])
        )

    @jsii.member(jsii_name="putWebAuthnPolicy")
    def put_web_authn_policy(self) -> None:
        value = DataKeycloakRealmWebAuthnPolicy()

        return typing.cast(None, jsii.invoke(self, "putWebAuthnPolicy", [value]))

    @jsii.member(jsii_name="resetAttributes")
    def reset_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttributes", []))

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

    @jsii.member(jsii_name="resetDisplayNameHtml")
    def reset_display_name_html(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayNameHtml", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInternationalization")
    def reset_internationalization(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInternationalization", []))

    @jsii.member(jsii_name="resetOtpPolicy")
    def reset_otp_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOtpPolicy", []))

    @jsii.member(jsii_name="resetSecurityDefenses")
    def reset_security_defenses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityDefenses", []))

    @jsii.member(jsii_name="resetSmtpServer")
    def reset_smtp_server(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSmtpServer", []))

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
    @jsii.member(jsii_name="accessCodeLifespan")
    def access_code_lifespan(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessCodeLifespan"))

    @builtins.property
    @jsii.member(jsii_name="accessCodeLifespanLogin")
    def access_code_lifespan_login(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessCodeLifespanLogin"))

    @builtins.property
    @jsii.member(jsii_name="accessCodeLifespanUserAction")
    def access_code_lifespan_user_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessCodeLifespanUserAction"))

    @builtins.property
    @jsii.member(jsii_name="accessTokenLifespan")
    def access_token_lifespan(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessTokenLifespan"))

    @builtins.property
    @jsii.member(jsii_name="accessTokenLifespanForImplicitFlow")
    def access_token_lifespan_for_implicit_flow(self) -> builtins.str:
        return typing.cast(
            builtins.str, jsii.get(self, "accessTokenLifespanForImplicitFlow")
        )

    @builtins.property
    @jsii.member(jsii_name="accountTheme")
    def account_theme(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountTheme"))

    @builtins.property
    @jsii.member(jsii_name="actionTokenGeneratedByAdminLifespan")
    def action_token_generated_by_admin_lifespan(self) -> builtins.str:
        return typing.cast(
            builtins.str, jsii.get(self, "actionTokenGeneratedByAdminLifespan")
        )

    @builtins.property
    @jsii.member(jsii_name="actionTokenGeneratedByUserLifespan")
    def action_token_generated_by_user_lifespan(self) -> builtins.str:
        return typing.cast(
            builtins.str, jsii.get(self, "actionTokenGeneratedByUserLifespan")
        )

    @builtins.property
    @jsii.member(jsii_name="adminTheme")
    def admin_theme(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adminTheme"))

    @builtins.property
    @jsii.member(jsii_name="browserFlow")
    def browser_flow(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "browserFlow"))

    @builtins.property
    @jsii.member(jsii_name="clientAuthenticationFlow")
    def client_authentication_flow(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientAuthenticationFlow"))

    @builtins.property
    @jsii.member(jsii_name="clientSessionIdleTimeout")
    def client_session_idle_timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSessionIdleTimeout"))

    @builtins.property
    @jsii.member(jsii_name="clientSessionMaxLifespan")
    def client_session_max_lifespan(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSessionMaxLifespan"))

    @builtins.property
    @jsii.member(jsii_name="defaultSignatureAlgorithm")
    def default_signature_algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultSignatureAlgorithm"))

    @builtins.property
    @jsii.member(jsii_name="directGrantFlow")
    def direct_grant_flow(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directGrantFlow"))

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @builtins.property
    @jsii.member(jsii_name="dockerAuthenticationFlow")
    def docker_authentication_flow(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dockerAuthenticationFlow"))

    @builtins.property
    @jsii.member(jsii_name="duplicateEmailsAllowed")
    def duplicate_emails_allowed(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(
            _cdktf_9a9027ec.IResolvable, jsii.get(self, "duplicateEmailsAllowed")
        )

    @builtins.property
    @jsii.member(jsii_name="editUsernameAllowed")
    def edit_username_allowed(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(
            _cdktf_9a9027ec.IResolvable, jsii.get(self, "editUsernameAllowed")
        )

    @builtins.property
    @jsii.member(jsii_name="emailTheme")
    def email_theme(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emailTheme"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "enabled"))

    @builtins.property
    @jsii.member(jsii_name="internalId")
    def internal_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "internalId"))

    @builtins.property
    @jsii.member(jsii_name="internationalization")
    def internationalization(self) -> "DataKeycloakRealmInternationalizationList":
        return typing.cast(
            "DataKeycloakRealmInternationalizationList",
            jsii.get(self, "internationalization"),
        )

    @builtins.property
    @jsii.member(jsii_name="loginTheme")
    def login_theme(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loginTheme"))

    @builtins.property
    @jsii.member(jsii_name="loginWithEmailAllowed")
    def login_with_email_allowed(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(
            _cdktf_9a9027ec.IResolvable, jsii.get(self, "loginWithEmailAllowed")
        )

    @builtins.property
    @jsii.member(jsii_name="oauth2DeviceCodeLifespan")
    def oauth2_device_code_lifespan(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oauth2DeviceCodeLifespan"))

    @builtins.property
    @jsii.member(jsii_name="oauth2DevicePollingInterval")
    def oauth2_device_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "oauth2DevicePollingInterval"))

    @builtins.property
    @jsii.member(jsii_name="offlineSessionIdleTimeout")
    def offline_session_idle_timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "offlineSessionIdleTimeout"))

    @builtins.property
    @jsii.member(jsii_name="offlineSessionMaxLifespan")
    def offline_session_max_lifespan(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "offlineSessionMaxLifespan"))

    @builtins.property
    @jsii.member(jsii_name="offlineSessionMaxLifespanEnabled")
    def offline_session_max_lifespan_enabled(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(
            _cdktf_9a9027ec.IResolvable,
            jsii.get(self, "offlineSessionMaxLifespanEnabled"),
        )

    @builtins.property
    @jsii.member(jsii_name="otpPolicy")
    def otp_policy(self) -> "DataKeycloakRealmOtpPolicyOutputReference":
        return typing.cast(
            "DataKeycloakRealmOtpPolicyOutputReference", jsii.get(self, "otpPolicy")
        )

    @builtins.property
    @jsii.member(jsii_name="passwordPolicy")
    def password_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "passwordPolicy"))

    @builtins.property
    @jsii.member(jsii_name="refreshTokenMaxReuse")
    def refresh_token_max_reuse(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "refreshTokenMaxReuse"))

    @builtins.property
    @jsii.member(jsii_name="registrationAllowed")
    def registration_allowed(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(
            _cdktf_9a9027ec.IResolvable, jsii.get(self, "registrationAllowed")
        )

    @builtins.property
    @jsii.member(jsii_name="registrationEmailAsUsername")
    def registration_email_as_username(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(
            _cdktf_9a9027ec.IResolvable, jsii.get(self, "registrationEmailAsUsername")
        )

    @builtins.property
    @jsii.member(jsii_name="registrationFlow")
    def registration_flow(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "registrationFlow"))

    @builtins.property
    @jsii.member(jsii_name="rememberMe")
    def remember_me(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "rememberMe"))

    @builtins.property
    @jsii.member(jsii_name="resetCredentialsFlow")
    def reset_credentials_flow(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resetCredentialsFlow"))

    @builtins.property
    @jsii.member(jsii_name="resetPasswordAllowed")
    def reset_password_allowed(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(
            _cdktf_9a9027ec.IResolvable, jsii.get(self, "resetPasswordAllowed")
        )

    @builtins.property
    @jsii.member(jsii_name="revokeRefreshToken")
    def revoke_refresh_token(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(
            _cdktf_9a9027ec.IResolvable, jsii.get(self, "revokeRefreshToken")
        )

    @builtins.property
    @jsii.member(jsii_name="securityDefenses")
    def security_defenses(self) -> "DataKeycloakRealmSecurityDefensesList":
        return typing.cast(
            "DataKeycloakRealmSecurityDefensesList", jsii.get(self, "securityDefenses")
        )

    @builtins.property
    @jsii.member(jsii_name="smtpServer")
    def smtp_server(self) -> "DataKeycloakRealmSmtpServerList":
        return typing.cast(
            "DataKeycloakRealmSmtpServerList", jsii.get(self, "smtpServer")
        )

    @builtins.property
    @jsii.member(jsii_name="sslRequired")
    def ssl_required(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslRequired"))

    @builtins.property
    @jsii.member(jsii_name="ssoSessionIdleTimeout")
    def sso_session_idle_timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ssoSessionIdleTimeout"))

    @builtins.property
    @jsii.member(jsii_name="ssoSessionIdleTimeoutRememberMe")
    def sso_session_idle_timeout_remember_me(self) -> builtins.str:
        return typing.cast(
            builtins.str, jsii.get(self, "ssoSessionIdleTimeoutRememberMe")
        )

    @builtins.property
    @jsii.member(jsii_name="ssoSessionMaxLifespan")
    def sso_session_max_lifespan(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ssoSessionMaxLifespan"))

    @builtins.property
    @jsii.member(jsii_name="ssoSessionMaxLifespanRememberMe")
    def sso_session_max_lifespan_remember_me(self) -> builtins.str:
        return typing.cast(
            builtins.str, jsii.get(self, "ssoSessionMaxLifespanRememberMe")
        )

    @builtins.property
    @jsii.member(jsii_name="userManagedAccess")
    def user_managed_access(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(
            _cdktf_9a9027ec.IResolvable, jsii.get(self, "userManagedAccess")
        )

    @builtins.property
    @jsii.member(jsii_name="verifyEmail")
    def verify_email(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "verifyEmail"))

    @builtins.property
    @jsii.member(jsii_name="webAuthnPasswordlessPolicy")
    def web_authn_passwordless_policy(
        self,
    ) -> "DataKeycloakRealmWebAuthnPasswordlessPolicyOutputReference":
        return typing.cast(
            "DataKeycloakRealmWebAuthnPasswordlessPolicyOutputReference",
            jsii.get(self, "webAuthnPasswordlessPolicy"),
        )

    @builtins.property
    @jsii.member(jsii_name="webAuthnPolicy")
    def web_authn_policy(self) -> "DataKeycloakRealmWebAuthnPolicyOutputReference":
        return typing.cast(
            "DataKeycloakRealmWebAuthnPolicyOutputReference",
            jsii.get(self, "webAuthnPolicy"),
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
    @jsii.member(jsii_name="displayNameHtmlInput")
    def display_name_html_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "displayNameHtmlInput")
        )

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="internationalizationInput")
    def internationalization_input(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.List["DataKeycloakRealmInternationalization"],
        ]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable,
                    typing.List["DataKeycloakRealmInternationalization"],
                ]
            ],
            jsii.get(self, "internationalizationInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="otpPolicyInput")
    def otp_policy_input(self) -> typing.Optional["DataKeycloakRealmOtpPolicy"]:
        return typing.cast(
            typing.Optional["DataKeycloakRealmOtpPolicy"],
            jsii.get(self, "otpPolicyInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="realmInput")
    def realm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "realmInput"))

    @builtins.property
    @jsii.member(jsii_name="securityDefensesInput")
    def security_defenses_input(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.List["DataKeycloakRealmSecurityDefenses"],
        ]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable,
                    typing.List["DataKeycloakRealmSecurityDefenses"],
                ]
            ],
            jsii.get(self, "securityDefensesInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="smtpServerInput")
    def smtp_server_input(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable, typing.List["DataKeycloakRealmSmtpServer"]
        ]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable,
                    typing.List["DataKeycloakRealmSmtpServer"],
                ]
            ],
            jsii.get(self, "smtpServerInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="webAuthnPasswordlessPolicyInput")
    def web_authn_passwordless_policy_input(
        self,
    ) -> typing.Optional["DataKeycloakRealmWebAuthnPasswordlessPolicy"]:
        return typing.cast(
            typing.Optional["DataKeycloakRealmWebAuthnPasswordlessPolicy"],
            jsii.get(self, "webAuthnPasswordlessPolicyInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="webAuthnPolicyInput")
    def web_authn_policy_input(
        self,
    ) -> typing.Optional["DataKeycloakRealmWebAuthnPolicy"]:
        return typing.cast(
            typing.Optional["DataKeycloakRealmWebAuthnPolicy"],
            jsii.get(self, "webAuthnPolicyInput"),
        )

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
                _typecheckingstub__2fcb602cfaf917d55d45a9383a34d717703c7b723e5b68fb444681cb6c36a8d0
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "attributes", value)

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
                _typecheckingstub__ba40794978551bd660eea8a01b0422ba031c15e9e868f2200c255c9e1b4bfc47
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
                _typecheckingstub__14372f8ac324772e1f3910ccbe6fa6e04b340fd4e53f881fc01edb1e4f478244
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "defaultOptionalClientScopes", value)

    @builtins.property
    @jsii.member(jsii_name="displayNameHtml")
    def display_name_html(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayNameHtml"))

    @display_name_html.setter
    def display_name_html(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__bf487c8ac839bcfd34b6946efc0254a032d0c8cc14914c10c867e0d5e61c83e8
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "displayNameHtml", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__33cb741c68705accb42c7d0cf91c93a847c2cdebaf83ec654bc071e6ca8b93ad
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="realm")
    def realm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "realm"))

    @realm.setter
    def realm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__4793cf564c6c8679a07df4db6d4c7b4cccd28d048816ac7e47ac7860b97cbaad
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "realm", value)


@jsii.data_type(
    jsii_type="keycloak.dataKeycloakRealm.DataKeycloakRealmConfig",
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
        "attributes": "attributes",
        "default_default_client_scopes": "defaultDefaultClientScopes",
        "default_optional_client_scopes": "defaultOptionalClientScopes",
        "display_name_html": "displayNameHtml",
        "id": "id",
        "internationalization": "internationalization",
        "otp_policy": "otpPolicy",
        "security_defenses": "securityDefenses",
        "smtp_server": "smtpServer",
        "web_authn_passwordless_policy": "webAuthnPasswordlessPolicy",
        "web_authn_policy": "webAuthnPolicy",
    },
)
class DataKeycloakRealmConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        default_default_client_scopes: typing.Optional[
            typing.Sequence[builtins.str]
        ] = None,
        default_optional_client_scopes: typing.Optional[
            typing.Sequence[builtins.str]
        ] = None,
        display_name_html: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        internationalization: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable,
                typing.Sequence[
                    typing.Union[
                        "DataKeycloakRealmInternationalization",
                        typing.Dict[builtins.str, typing.Any],
                    ]
                ],
            ]
        ] = None,
        otp_policy: typing.Optional[
            typing.Union[
                "DataKeycloakRealmOtpPolicy", typing.Dict[builtins.str, typing.Any]
            ]
        ] = None,
        security_defenses: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable,
                typing.Sequence[
                    typing.Union[
                        "DataKeycloakRealmSecurityDefenses",
                        typing.Dict[builtins.str, typing.Any],
                    ]
                ],
            ]
        ] = None,
        smtp_server: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable,
                typing.Sequence[
                    typing.Union[
                        "DataKeycloakRealmSmtpServer",
                        typing.Dict[builtins.str, typing.Any],
                    ]
                ],
            ]
        ] = None,
        web_authn_passwordless_policy: typing.Optional[
            typing.Union[
                "DataKeycloakRealmWebAuthnPasswordlessPolicy",
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        web_authn_policy: typing.Optional[
            typing.Union[
                "DataKeycloakRealmWebAuthnPolicy", typing.Dict[builtins.str, typing.Any]
            ]
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
        :param realm: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#realm DataKeycloakRealm#realm}.
        :param attributes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#attributes DataKeycloakRealm#attributes}.
        :param default_default_client_scopes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#default_default_client_scopes DataKeycloakRealm#default_default_client_scopes}.
        :param default_optional_client_scopes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#default_optional_client_scopes DataKeycloakRealm#default_optional_client_scopes}.
        :param display_name_html: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#display_name_html DataKeycloakRealm#display_name_html}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#id DataKeycloakRealm#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param internationalization: internationalization block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#internationalization DataKeycloakRealm#internationalization}
        :param otp_policy: otp_policy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#otp_policy DataKeycloakRealm#otp_policy}
        :param security_defenses: security_defenses block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#security_defenses DataKeycloakRealm#security_defenses}
        :param smtp_server: smtp_server block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#smtp_server DataKeycloakRealm#smtp_server}
        :param web_authn_passwordless_policy: web_authn_passwordless_policy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#web_authn_passwordless_policy DataKeycloakRealm#web_authn_passwordless_policy}
        :param web_authn_policy: web_authn_policy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#web_authn_policy DataKeycloakRealm#web_authn_policy}
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(otp_policy, dict):
            otp_policy = DataKeycloakRealmOtpPolicy(**otp_policy)
        if isinstance(web_authn_passwordless_policy, dict):
            web_authn_passwordless_policy = DataKeycloakRealmWebAuthnPasswordlessPolicy(
                **web_authn_passwordless_policy
            )
        if isinstance(web_authn_policy, dict):
            web_authn_policy = DataKeycloakRealmWebAuthnPolicy(**web_authn_policy)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__7297e11b08e4dc237eb3d38b4021880b3b51fac6f716e412a693c32b7dd6ad6a
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
                argname="argument attributes",
                value=attributes,
                expected_type=type_hints["attributes"],
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
                argname="argument display_name_html",
                value=display_name_html,
                expected_type=type_hints["display_name_html"],
            )
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(
                argname="argument internationalization",
                value=internationalization,
                expected_type=type_hints["internationalization"],
            )
            check_type(
                argname="argument otp_policy",
                value=otp_policy,
                expected_type=type_hints["otp_policy"],
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
        if attributes is not None:
            self._values["attributes"] = attributes
        if default_default_client_scopes is not None:
            self._values[
                "default_default_client_scopes"
            ] = default_default_client_scopes
        if default_optional_client_scopes is not None:
            self._values[
                "default_optional_client_scopes"
            ] = default_optional_client_scopes
        if display_name_html is not None:
            self._values["display_name_html"] = display_name_html
        if id is not None:
            self._values["id"] = id
        if internationalization is not None:
            self._values["internationalization"] = internationalization
        if otp_policy is not None:
            self._values["otp_policy"] = otp_policy
        if security_defenses is not None:
            self._values["security_defenses"] = security_defenses
        if smtp_server is not None:
            self._values["smtp_server"] = smtp_server
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
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#realm DataKeycloakRealm#realm}."""
        result = self._values.get("realm")
        assert result is not None, "Required property 'realm' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attributes(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#attributes DataKeycloakRealm#attributes}."""
        result = self._values.get("attributes")
        return typing.cast(
            typing.Optional[typing.Mapping[builtins.str, builtins.str]], result
        )

    @builtins.property
    def default_default_client_scopes(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#default_default_client_scopes DataKeycloakRealm#default_default_client_scopes}."""
        result = self._values.get("default_default_client_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def default_optional_client_scopes(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#default_optional_client_scopes DataKeycloakRealm#default_optional_client_scopes}."""
        result = self._values.get("default_optional_client_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def display_name_html(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#display_name_html DataKeycloakRealm#display_name_html}."""
        result = self._values.get("display_name_html")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#id DataKeycloakRealm#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def internationalization(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.List["DataKeycloakRealmInternationalization"],
        ]
    ]:
        """internationalization block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#internationalization DataKeycloakRealm#internationalization}
        """
        result = self._values.get("internationalization")
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable,
                    typing.List["DataKeycloakRealmInternationalization"],
                ]
            ],
            result,
        )

    @builtins.property
    def otp_policy(self) -> typing.Optional["DataKeycloakRealmOtpPolicy"]:
        """otp_policy block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#otp_policy DataKeycloakRealm#otp_policy}
        """
        result = self._values.get("otp_policy")
        return typing.cast(typing.Optional["DataKeycloakRealmOtpPolicy"], result)

    @builtins.property
    def security_defenses(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.List["DataKeycloakRealmSecurityDefenses"],
        ]
    ]:
        """security_defenses block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#security_defenses DataKeycloakRealm#security_defenses}
        """
        result = self._values.get("security_defenses")
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable,
                    typing.List["DataKeycloakRealmSecurityDefenses"],
                ]
            ],
            result,
        )

    @builtins.property
    def smtp_server(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable, typing.List["DataKeycloakRealmSmtpServer"]
        ]
    ]:
        """smtp_server block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#smtp_server DataKeycloakRealm#smtp_server}
        """
        result = self._values.get("smtp_server")
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable,
                    typing.List["DataKeycloakRealmSmtpServer"],
                ]
            ],
            result,
        )

    @builtins.property
    def web_authn_passwordless_policy(
        self,
    ) -> typing.Optional["DataKeycloakRealmWebAuthnPasswordlessPolicy"]:
        """web_authn_passwordless_policy block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#web_authn_passwordless_policy DataKeycloakRealm#web_authn_passwordless_policy}
        """
        result = self._values.get("web_authn_passwordless_policy")
        return typing.cast(
            typing.Optional["DataKeycloakRealmWebAuthnPasswordlessPolicy"], result
        )

    @builtins.property
    def web_authn_policy(self) -> typing.Optional["DataKeycloakRealmWebAuthnPolicy"]:
        """web_authn_policy block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#web_authn_policy DataKeycloakRealm#web_authn_policy}
        """
        result = self._values.get("web_authn_policy")
        return typing.cast(typing.Optional["DataKeycloakRealmWebAuthnPolicy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKeycloakRealmConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="keycloak.dataKeycloakRealm.DataKeycloakRealmInternationalization",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataKeycloakRealmInternationalization:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKeycloakRealmInternationalization(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKeycloakRealmInternationalizationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.dataKeycloakRealm.DataKeycloakRealmInternationalizationList",
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
                _typecheckingstub__1f93181d7cdc84e5855e1b7aad266e31ccf014ec644f4d2c828efdf76a9c7c4f
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
    ) -> "DataKeycloakRealmInternationalizationOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__2e1d262dca5bd387633650a837d144b0f378e5aaa78dab665e0ffe2e07233cfa
            )
            check_type(
                argname="argument index", value=index, expected_type=type_hints["index"]
            )
        return typing.cast(
            "DataKeycloakRealmInternationalizationOutputReference",
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
                _typecheckingstub__f5bfb0408b2bd1a52af1ee51cf036345edac3bd562cefd0451ae03039f6d64a1
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
                _typecheckingstub__03b9c988402afd041796088c3f80a7add6685f766e0a71bb2e7bff324874f9cd
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
                _typecheckingstub__ae26c1f82c6a40cf2a5c37a1553e506b8bda03632e999a9df8e47363d9fdc52e
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.List[DataKeycloakRealmInternationalization],
        ]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable,
                    typing.List[DataKeycloakRealmInternationalization],
                ]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable,
                typing.List[DataKeycloakRealmInternationalization],
            ]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a13910ee8f46a36acd7eb10bd524a8cd011107e5d550fd71fb370ebdcdbb49ec
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


class DataKeycloakRealmInternationalizationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.dataKeycloakRealm.DataKeycloakRealmInternationalizationOutputReference",
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
                _typecheckingstub__9bb656b2eb86c1c5977ec255dfc9d4229bcaa7fe9756da59be5f8de1ca7c865a
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
    @jsii.member(jsii_name="defaultLocale")
    def default_locale(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultLocale"))

    @builtins.property
    @jsii.member(jsii_name="supportedLocales")
    def supported_locales(self) -> typing.List[builtins.str]:
        return typing.cast(
            typing.List[builtins.str], jsii.get(self, "supportedLocales")
        )

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, DataKeycloakRealmInternationalization]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable, DataKeycloakRealmInternationalization
                ]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable, DataKeycloakRealmInternationalization
            ]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__5b46c0b511d4c17b33a170b5a0a8eeff5787e53f4b274497381c64960c8a539b
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="keycloak.dataKeycloakRealm.DataKeycloakRealmOtpPolicy",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataKeycloakRealmOtpPolicy:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKeycloakRealmOtpPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKeycloakRealmOtpPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.dataKeycloakRealm.DataKeycloakRealmOtpPolicyOutputReference",
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
                _typecheckingstub__85ffb84f5c563f843786e14b380f1f0067fcb2fcd6da67ba378f4fb9186274a2
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
    @jsii.member(jsii_name="algorithm")
    def algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "algorithm"))

    @builtins.property
    @jsii.member(jsii_name="digits")
    def digits(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "digits"))

    @builtins.property
    @jsii.member(jsii_name="initialCounter")
    def initial_counter(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "initialCounter"))

    @builtins.property
    @jsii.member(jsii_name="lookAheadWindow")
    def look_ahead_window(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lookAheadWindow"))

    @builtins.property
    @jsii.member(jsii_name="period")
    def period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "period"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataKeycloakRealmOtpPolicy]:
        return typing.cast(
            typing.Optional[DataKeycloakRealmOtpPolicy], jsii.get(self, "internalValue")
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKeycloakRealmOtpPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__8220be0cf02d4ef2c475cbf3c7d88c62be3391e0b7a52a3ca812018ae14916fe
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="keycloak.dataKeycloakRealm.DataKeycloakRealmSecurityDefenses",
    jsii_struct_bases=[],
    name_mapping={
        "brute_force_detection": "bruteForceDetection",
        "headers": "headers",
    },
)
class DataKeycloakRealmSecurityDefenses:
    def __init__(
        self,
        *,
        brute_force_detection: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable,
                typing.Sequence[
                    typing.Union[
                        "DataKeycloakRealmSecurityDefensesBruteForceDetection",
                        typing.Dict[builtins.str, typing.Any],
                    ]
                ],
            ]
        ] = None,
        headers: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable,
                typing.Sequence[
                    typing.Union[
                        "DataKeycloakRealmSecurityDefensesHeaders",
                        typing.Dict[builtins.str, typing.Any],
                    ]
                ],
            ]
        ] = None,
    ) -> None:
        """
        :param brute_force_detection: brute_force_detection block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#brute_force_detection DataKeycloakRealm#brute_force_detection}
        :param headers: headers block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#headers DataKeycloakRealm#headers}
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__0345a1a6325c1cf653d5f7182c8b50f7eb2c27013422c62df07ee4ed60d7dd21
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
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.List["DataKeycloakRealmSecurityDefensesBruteForceDetection"],
        ]
    ]:
        """brute_force_detection block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#brute_force_detection DataKeycloakRealm#brute_force_detection}
        """
        result = self._values.get("brute_force_detection")
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable,
                    typing.List["DataKeycloakRealmSecurityDefensesBruteForceDetection"],
                ]
            ],
            result,
        )

    @builtins.property
    def headers(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.List["DataKeycloakRealmSecurityDefensesHeaders"],
        ]
    ]:
        """headers block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#headers DataKeycloakRealm#headers}
        """
        result = self._values.get("headers")
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable,
                    typing.List["DataKeycloakRealmSecurityDefensesHeaders"],
                ]
            ],
            result,
        )

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKeycloakRealmSecurityDefenses(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="keycloak.dataKeycloakRealm.DataKeycloakRealmSecurityDefensesBruteForceDetection",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataKeycloakRealmSecurityDefensesBruteForceDetection:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKeycloakRealmSecurityDefensesBruteForceDetection(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKeycloakRealmSecurityDefensesBruteForceDetectionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.dataKeycloakRealm.DataKeycloakRealmSecurityDefensesBruteForceDetectionList",
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
                _typecheckingstub__e64aa82c20f4c054b06d89f1f3f6d1efdf7703eaf23ecbf6badf1e0c03e70850
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
    ) -> "DataKeycloakRealmSecurityDefensesBruteForceDetectionOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__147a090ffc6b881af8f7cc4ded88fcc3723162897a0bca42926d5c2ac839aa34
            )
            check_type(
                argname="argument index", value=index, expected_type=type_hints["index"]
            )
        return typing.cast(
            "DataKeycloakRealmSecurityDefensesBruteForceDetectionOutputReference",
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
                _typecheckingstub__9b0934c8a71d86462530c85024c1736a30199ec9e0e6b16505fb1ee44836794b
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
                _typecheckingstub__ecb698810358038da3b28c4d0c1199ecf214e06059b65a8982913b6b295e204c
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
                _typecheckingstub__525765b0332357b016503165017c5f336a9df9dee775cbdcbbdeb57fbd59d5b5
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.List[DataKeycloakRealmSecurityDefensesBruteForceDetection],
        ]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable,
                    typing.List[DataKeycloakRealmSecurityDefensesBruteForceDetection],
                ]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable,
                typing.List[DataKeycloakRealmSecurityDefensesBruteForceDetection],
            ]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__0e4d7d8857c0d1f6d3347d6e72d30baeeb738661dbb9cb0ed2a805fc91c086e5
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


class DataKeycloakRealmSecurityDefensesBruteForceDetectionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.dataKeycloakRealm.DataKeycloakRealmSecurityDefensesBruteForceDetectionOutputReference",
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
                _typecheckingstub__f0a07422957ecabaed4fe6b59af7e4657e9182f8961db7597af8306c72c35824
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
    @jsii.member(jsii_name="failureResetTimeSeconds")
    def failure_reset_time_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "failureResetTimeSeconds"))

    @builtins.property
    @jsii.member(jsii_name="maxFailureWaitSeconds")
    def max_failure_wait_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxFailureWaitSeconds"))

    @builtins.property
    @jsii.member(jsii_name="maxLoginFailures")
    def max_login_failures(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxLoginFailures"))

    @builtins.property
    @jsii.member(jsii_name="minimumQuickLoginWaitSeconds")
    def minimum_quick_login_wait_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minimumQuickLoginWaitSeconds"))

    @builtins.property
    @jsii.member(jsii_name="permanentLockout")
    def permanent_lockout(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(
            _cdktf_9a9027ec.IResolvable, jsii.get(self, "permanentLockout")
        )

    @builtins.property
    @jsii.member(jsii_name="quickLoginCheckMilliSeconds")
    def quick_login_check_milli_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "quickLoginCheckMilliSeconds"))

    @builtins.property
    @jsii.member(jsii_name="waitIncrementSeconds")
    def wait_increment_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "waitIncrementSeconds"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            DataKeycloakRealmSecurityDefensesBruteForceDetection,
        ]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable,
                    DataKeycloakRealmSecurityDefensesBruteForceDetection,
                ]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable,
                DataKeycloakRealmSecurityDefensesBruteForceDetection,
            ]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__0db1e2e2ace8bba3cfa9196e8be192190d6b85cb18e90982d06b0eb0a609fb69
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="keycloak.dataKeycloakRealm.DataKeycloakRealmSecurityDefensesHeaders",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataKeycloakRealmSecurityDefensesHeaders:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKeycloakRealmSecurityDefensesHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKeycloakRealmSecurityDefensesHeadersList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.dataKeycloakRealm.DataKeycloakRealmSecurityDefensesHeadersList",
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
                _typecheckingstub__8a6011f492979e13b996e4dcfed55f8315c104c84452769fe8e0393d06c141d5
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
    ) -> "DataKeycloakRealmSecurityDefensesHeadersOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__3e006510e492646fde7563ff1721864ab69bc1dc88dcf987fa73ebde8969cda7
            )
            check_type(
                argname="argument index", value=index, expected_type=type_hints["index"]
            )
        return typing.cast(
            "DataKeycloakRealmSecurityDefensesHeadersOutputReference",
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
                _typecheckingstub__eea27d552c0a3292b06048b773f07c0c8607fd7583c7d3d862a420c2a8e6bce6
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
                _typecheckingstub__01536ef6872c9814baf1fefcafaa5612f1e006c6d4aaf1ba48dd925ff7d3696c
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
                _typecheckingstub__fb144b446dafbb1923af5351bee3def80e00f90a7cb9f9f178f7f64e82383404
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.List[DataKeycloakRealmSecurityDefensesHeaders],
        ]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable,
                    typing.List[DataKeycloakRealmSecurityDefensesHeaders],
                ]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable,
                typing.List[DataKeycloakRealmSecurityDefensesHeaders],
            ]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__223eb251cca348f95a09cc29d1b4860d448771efbd896fad7442ccd279fdd315
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


class DataKeycloakRealmSecurityDefensesHeadersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.dataKeycloakRealm.DataKeycloakRealmSecurityDefensesHeadersOutputReference",
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
                _typecheckingstub__e0872fb1ebb77c40a39e3ed3c1d329018f57eba947ec32d42bc87261c5658f97
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
    @jsii.member(jsii_name="contentSecurityPolicy")
    def content_security_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentSecurityPolicy"))

    @builtins.property
    @jsii.member(jsii_name="contentSecurityPolicyReportOnly")
    def content_security_policy_report_only(self) -> builtins.str:
        return typing.cast(
            builtins.str, jsii.get(self, "contentSecurityPolicyReportOnly")
        )

    @builtins.property
    @jsii.member(jsii_name="strictTransportSecurity")
    def strict_transport_security(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "strictTransportSecurity"))

    @builtins.property
    @jsii.member(jsii_name="xContentTypeOptions")
    def x_content_type_options(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "xContentTypeOptions"))

    @builtins.property
    @jsii.member(jsii_name="xFrameOptions")
    def x_frame_options(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "xFrameOptions"))

    @builtins.property
    @jsii.member(jsii_name="xRobotsTag")
    def x_robots_tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "xRobotsTag"))

    @builtins.property
    @jsii.member(jsii_name="xXssProtection")
    def x_xss_protection(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "xXssProtection"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable, DataKeycloakRealmSecurityDefensesHeaders
        ]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable,
                    DataKeycloakRealmSecurityDefensesHeaders,
                ]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable, DataKeycloakRealmSecurityDefensesHeaders
            ]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__7e4d4687953ae967a85b63c39e0b3d94ff5e296a2f2f2c946866a05c45d3ec36
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


class DataKeycloakRealmSecurityDefensesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.dataKeycloakRealm.DataKeycloakRealmSecurityDefensesList",
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
                _typecheckingstub__b10796ddecb5fd3469d0a355f37ab7fbc0bda71ed6ad929add36de209a8448cd
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
    ) -> "DataKeycloakRealmSecurityDefensesOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__2f2f8945b5672c5c7102b60677d69e4789a6bc4d523b1f007c47fb81ec3be044
            )
            check_type(
                argname="argument index", value=index, expected_type=type_hints["index"]
            )
        return typing.cast(
            "DataKeycloakRealmSecurityDefensesOutputReference",
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
                _typecheckingstub__8286f0652ca21a2f661dcaaeef6a920020d373f4c07697571ecf90d110215095
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
                _typecheckingstub__9c5bdb2ac4a12fa2bbbe2251ff83728b3258d564a676c1b8e32a80e889fd8ddb
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
                _typecheckingstub__022a1a9e77a00e66de674db9f4d8b5a360c483e40add02a38157272ef6971913
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable, typing.List[DataKeycloakRealmSecurityDefenses]
        ]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable,
                    typing.List[DataKeycloakRealmSecurityDefenses],
                ]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable,
                typing.List[DataKeycloakRealmSecurityDefenses],
            ]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__af1b9cd14d1f9c68e194dc4132fb50dc66683bfdb86ce96676300b3dfb72fb0b
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


class DataKeycloakRealmSecurityDefensesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.dataKeycloakRealm.DataKeycloakRealmSecurityDefensesOutputReference",
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
                _typecheckingstub__31d799d351864f3221d9161ce573f73bda9eec5f5e2326b454f6bad52d8c9ab3
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

    @jsii.member(jsii_name="putBruteForceDetection")
    def put_brute_force_detection(
        self,
        value: typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    DataKeycloakRealmSecurityDefensesBruteForceDetection,
                    typing.Dict[builtins.str, typing.Any],
                ]
            ],
        ],
    ) -> None:
        """
        :param value: -
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__56873da6086dfb7d3af0cc7c84a2030ffadea22cfeaa2196e5ad94b2bd396865
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        return typing.cast(None, jsii.invoke(self, "putBruteForceDetection", [value]))

    @jsii.member(jsii_name="putHeaders")
    def put_headers(
        self,
        value: typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    DataKeycloakRealmSecurityDefensesHeaders,
                    typing.Dict[builtins.str, typing.Any],
                ]
            ],
        ],
    ) -> None:
        """
        :param value: -
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__ac86b4b4cd1a9444b70c048b9889738d3c578a2118e1ac184d0546b59cf3da47
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
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
    ) -> DataKeycloakRealmSecurityDefensesBruteForceDetectionList:
        return typing.cast(
            DataKeycloakRealmSecurityDefensesBruteForceDetectionList,
            jsii.get(self, "bruteForceDetection"),
        )

    @builtins.property
    @jsii.member(jsii_name="headers")
    def headers(self) -> DataKeycloakRealmSecurityDefensesHeadersList:
        return typing.cast(
            DataKeycloakRealmSecurityDefensesHeadersList, jsii.get(self, "headers")
        )

    @builtins.property
    @jsii.member(jsii_name="bruteForceDetectionInput")
    def brute_force_detection_input(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.List[DataKeycloakRealmSecurityDefensesBruteForceDetection],
        ]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable,
                    typing.List[DataKeycloakRealmSecurityDefensesBruteForceDetection],
                ]
            ],
            jsii.get(self, "bruteForceDetectionInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="headersInput")
    def headers_input(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.List[DataKeycloakRealmSecurityDefensesHeaders],
        ]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable,
                    typing.List[DataKeycloakRealmSecurityDefensesHeaders],
                ]
            ],
            jsii.get(self, "headersInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, DataKeycloakRealmSecurityDefenses]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable, DataKeycloakRealmSecurityDefenses
                ]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, DataKeycloakRealmSecurityDefenses]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__cee275d043514eeee3178f291736db60c0bf1f409757cb8c9efe124bf5e2e334
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="keycloak.dataKeycloakRealm.DataKeycloakRealmSmtpServer",
    jsii_struct_bases=[],
    name_mapping={"auth": "auth"},
)
class DataKeycloakRealmSmtpServer:
    def __init__(
        self,
        *,
        auth: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable,
                typing.Sequence[
                    typing.Union[
                        "DataKeycloakRealmSmtpServerAuth",
                        typing.Dict[builtins.str, typing.Any],
                    ]
                ],
            ]
        ] = None,
    ) -> None:
        """
        :param auth: auth block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#auth DataKeycloakRealm#auth}
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__ec7b49d64d74a70bde2276c40c665928b188ac47779c34cd4d095df1aeb97e21
            )
            check_type(
                argname="argument auth", value=auth, expected_type=type_hints["auth"]
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if auth is not None:
            self._values["auth"] = auth

    @builtins.property
    def auth(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable, typing.List["DataKeycloakRealmSmtpServerAuth"]
        ]
    ]:
        """auth block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/data-sources/realm#auth DataKeycloakRealm#auth}
        """
        result = self._values.get("auth")
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable,
                    typing.List["DataKeycloakRealmSmtpServerAuth"],
                ]
            ],
            result,
        )

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKeycloakRealmSmtpServer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="keycloak.dataKeycloakRealm.DataKeycloakRealmSmtpServerAuth",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataKeycloakRealmSmtpServerAuth:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKeycloakRealmSmtpServerAuth(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKeycloakRealmSmtpServerAuthList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.dataKeycloakRealm.DataKeycloakRealmSmtpServerAuthList",
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
                _typecheckingstub__39793921034d27304527349c183f0743164cc1acbd659e95b803ec113bd6f6e8
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
    ) -> "DataKeycloakRealmSmtpServerAuthOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__23cf1543b8b7d0467cbf76e7c2ded4737fdeca8933e4c5a0f6ef463b581d8975
            )
            check_type(
                argname="argument index", value=index, expected_type=type_hints["index"]
            )
        return typing.cast(
            "DataKeycloakRealmSmtpServerAuthOutputReference",
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
                _typecheckingstub__95738b0cfc83eeef4149edb74c94eb3d7f77ab3d317ad1daf3bb2bbb29209770
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
                _typecheckingstub__319da60ac97642b049c953de1e842c9117d6a62ae63b8ba7a81e591f8172393b
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
                _typecheckingstub__80c7f414f0e349ce093057d97b6866c6293c226213af5b6d677e2c58f1f8f347
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable, typing.List[DataKeycloakRealmSmtpServerAuth]
        ]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable,
                    typing.List[DataKeycloakRealmSmtpServerAuth],
                ]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable,
                typing.List[DataKeycloakRealmSmtpServerAuth],
            ]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__c569deba1bdb84ddd1e747d2200faff8bfb1f56420890f4fe0a4b365c5b0a52e
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


class DataKeycloakRealmSmtpServerAuthOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.dataKeycloakRealm.DataKeycloakRealmSmtpServerAuthOutputReference",
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
                _typecheckingstub__4a42f7bf713a0572ef10c328d887cf847a64ba0425d42246b3414e7e234f6337
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
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, DataKeycloakRealmSmtpServerAuth]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable, DataKeycloakRealmSmtpServerAuth
                ]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, DataKeycloakRealmSmtpServerAuth]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__803f469896b19fc1b923aba79720ac7d408bec15d05ff8e0cd9aeabc63848dc7
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


class DataKeycloakRealmSmtpServerList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.dataKeycloakRealm.DataKeycloakRealmSmtpServerList",
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
                _typecheckingstub__ff3ceb424443bd77c325d16c75b3e311f3ff5af686d43158b747552bdca8746e
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
    def get(self, index: jsii.Number) -> "DataKeycloakRealmSmtpServerOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__f51a763bf9420e4a6b6594bf340dad64019a82e5075475d5123b314008ba474b
            )
            check_type(
                argname="argument index", value=index, expected_type=type_hints["index"]
            )
        return typing.cast(
            "DataKeycloakRealmSmtpServerOutputReference",
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
                _typecheckingstub__b0142065cc658ecbb4be6d075a5c26e8bfaff549513b468ba317cbbf7a473d05
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
                _typecheckingstub__716ca3f48d9405943bd9cf4aa559567f0dec2bccd2c64cd9027da54ed2d6536e
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
                _typecheckingstub__20efa2527717b3f98f5ef9f3fcb0731177c41b69d721f24c8d614ed6ff006134
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable, typing.List[DataKeycloakRealmSmtpServer]
        ]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable,
                    typing.List[DataKeycloakRealmSmtpServer],
                ]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable, typing.List[DataKeycloakRealmSmtpServer]
            ]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__154889b80837092229c52cf3d2a6decf07210270d9fc5e34e7dbb28b94953446
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


class DataKeycloakRealmSmtpServerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.dataKeycloakRealm.DataKeycloakRealmSmtpServerOutputReference",
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
                _typecheckingstub__55c2d552b68328cbfba4fb1eca892ec6577ca6d55cbedc2555fa2aefa683a2f6
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

    @jsii.member(jsii_name="putAuth")
    def put_auth(
        self,
        value: typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    DataKeycloakRealmSmtpServerAuth,
                    typing.Dict[builtins.str, typing.Any],
                ]
            ],
        ],
    ) -> None:
        """
        :param value: -
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__6e6471bcfc7fe074ad8fbc7920bd05c8d0435fcd8f18bc3da4dd61df563f1fe8
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        return typing.cast(None, jsii.invoke(self, "putAuth", [value]))

    @jsii.member(jsii_name="resetAuth")
    def reset_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuth", []))

    @builtins.property
    @jsii.member(jsii_name="auth")
    def auth(self) -> DataKeycloakRealmSmtpServerAuthList:
        return typing.cast(DataKeycloakRealmSmtpServerAuthList, jsii.get(self, "auth"))

    @builtins.property
    @jsii.member(jsii_name="envelopeFrom")
    def envelope_from(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "envelopeFrom"))

    @builtins.property
    @jsii.member(jsii_name="from")
    def from_(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "from"))

    @builtins.property
    @jsii.member(jsii_name="fromDisplayName")
    def from_display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fromDisplayName"))

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "port"))

    @builtins.property
    @jsii.member(jsii_name="replyTo")
    def reply_to(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replyTo"))

    @builtins.property
    @jsii.member(jsii_name="replyToDisplayName")
    def reply_to_display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replyToDisplayName"))

    @builtins.property
    @jsii.member(jsii_name="ssl")
    def ssl(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "ssl"))

    @builtins.property
    @jsii.member(jsii_name="starttls")
    def starttls(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "starttls"))

    @builtins.property
    @jsii.member(jsii_name="authInput")
    def auth_input(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable, typing.List[DataKeycloakRealmSmtpServerAuth]
        ]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable,
                    typing.List[DataKeycloakRealmSmtpServerAuth],
                ]
            ],
            jsii.get(self, "authInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, DataKeycloakRealmSmtpServer]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[_cdktf_9a9027ec.IResolvable, DataKeycloakRealmSmtpServer]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, DataKeycloakRealmSmtpServer]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d61915b17fb4a9cc2e24c9cd81e1acd84b04944792fea9b5904f1731af78810d
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="keycloak.dataKeycloakRealm.DataKeycloakRealmWebAuthnPasswordlessPolicy",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataKeycloakRealmWebAuthnPasswordlessPolicy:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKeycloakRealmWebAuthnPasswordlessPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKeycloakRealmWebAuthnPasswordlessPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.dataKeycloakRealm.DataKeycloakRealmWebAuthnPasswordlessPolicyOutputReference",
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
                _typecheckingstub__72c015e1598c47c12185b368fbc16b90bffde5f8182cff789c2e05d6a97072d0
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
    @jsii.member(jsii_name="acceptableAaguids")
    def acceptable_aaguids(self) -> typing.List[builtins.str]:
        return typing.cast(
            typing.List[builtins.str], jsii.get(self, "acceptableAaguids")
        )

    @builtins.property
    @jsii.member(jsii_name="attestationConveyancePreference")
    def attestation_conveyance_preference(self) -> builtins.str:
        return typing.cast(
            builtins.str, jsii.get(self, "attestationConveyancePreference")
        )

    @builtins.property
    @jsii.member(jsii_name="authenticatorAttachment")
    def authenticator_attachment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authenticatorAttachment"))

    @builtins.property
    @jsii.member(jsii_name="avoidSameAuthenticatorRegister")
    def avoid_same_authenticator_register(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(
            _cdktf_9a9027ec.IResolvable,
            jsii.get(self, "avoidSameAuthenticatorRegister"),
        )

    @builtins.property
    @jsii.member(jsii_name="createTimeout")
    def create_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "createTimeout"))

    @builtins.property
    @jsii.member(jsii_name="relyingPartyEntityName")
    def relying_party_entity_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "relyingPartyEntityName"))

    @builtins.property
    @jsii.member(jsii_name="relyingPartyId")
    def relying_party_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "relyingPartyId"))

    @builtins.property
    @jsii.member(jsii_name="requireResidentKey")
    def require_resident_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "requireResidentKey"))

    @builtins.property
    @jsii.member(jsii_name="signatureAlgorithms")
    def signature_algorithms(self) -> typing.List[builtins.str]:
        return typing.cast(
            typing.List[builtins.str], jsii.get(self, "signatureAlgorithms")
        )

    @builtins.property
    @jsii.member(jsii_name="userVerificationRequirement")
    def user_verification_requirement(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userVerificationRequirement"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataKeycloakRealmWebAuthnPasswordlessPolicy]:
        return typing.cast(
            typing.Optional[DataKeycloakRealmWebAuthnPasswordlessPolicy],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKeycloakRealmWebAuthnPasswordlessPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__944aff65ec826567419c6ae97dbec8d4c67ceed355160df2c0ecd6cfeb7056cb
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="keycloak.dataKeycloakRealm.DataKeycloakRealmWebAuthnPolicy",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataKeycloakRealmWebAuthnPolicy:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataKeycloakRealmWebAuthnPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataKeycloakRealmWebAuthnPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.dataKeycloakRealm.DataKeycloakRealmWebAuthnPolicyOutputReference",
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
                _typecheckingstub__ad5ade617d5643cadfffbe930643637f4b1b1ee54ac0d6a5658fddc5501500f4
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
    @jsii.member(jsii_name="acceptableAaguids")
    def acceptable_aaguids(self) -> typing.List[builtins.str]:
        return typing.cast(
            typing.List[builtins.str], jsii.get(self, "acceptableAaguids")
        )

    @builtins.property
    @jsii.member(jsii_name="attestationConveyancePreference")
    def attestation_conveyance_preference(self) -> builtins.str:
        return typing.cast(
            builtins.str, jsii.get(self, "attestationConveyancePreference")
        )

    @builtins.property
    @jsii.member(jsii_name="authenticatorAttachment")
    def authenticator_attachment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authenticatorAttachment"))

    @builtins.property
    @jsii.member(jsii_name="avoidSameAuthenticatorRegister")
    def avoid_same_authenticator_register(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(
            _cdktf_9a9027ec.IResolvable,
            jsii.get(self, "avoidSameAuthenticatorRegister"),
        )

    @builtins.property
    @jsii.member(jsii_name="createTimeout")
    def create_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "createTimeout"))

    @builtins.property
    @jsii.member(jsii_name="relyingPartyEntityName")
    def relying_party_entity_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "relyingPartyEntityName"))

    @builtins.property
    @jsii.member(jsii_name="relyingPartyId")
    def relying_party_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "relyingPartyId"))

    @builtins.property
    @jsii.member(jsii_name="requireResidentKey")
    def require_resident_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "requireResidentKey"))

    @builtins.property
    @jsii.member(jsii_name="signatureAlgorithms")
    def signature_algorithms(self) -> typing.List[builtins.str]:
        return typing.cast(
            typing.List[builtins.str], jsii.get(self, "signatureAlgorithms")
        )

    @builtins.property
    @jsii.member(jsii_name="userVerificationRequirement")
    def user_verification_requirement(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userVerificationRequirement"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataKeycloakRealmWebAuthnPolicy]:
        return typing.cast(
            typing.Optional[DataKeycloakRealmWebAuthnPolicy],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataKeycloakRealmWebAuthnPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__28c65b1772966d242f221740a2f58b77c7fd1d21b54943641aa3af46b1570f49
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataKeycloakRealm",
    "DataKeycloakRealmConfig",
    "DataKeycloakRealmInternationalization",
    "DataKeycloakRealmInternationalizationList",
    "DataKeycloakRealmInternationalizationOutputReference",
    "DataKeycloakRealmOtpPolicy",
    "DataKeycloakRealmOtpPolicyOutputReference",
    "DataKeycloakRealmSecurityDefenses",
    "DataKeycloakRealmSecurityDefensesBruteForceDetection",
    "DataKeycloakRealmSecurityDefensesBruteForceDetectionList",
    "DataKeycloakRealmSecurityDefensesBruteForceDetectionOutputReference",
    "DataKeycloakRealmSecurityDefensesHeaders",
    "DataKeycloakRealmSecurityDefensesHeadersList",
    "DataKeycloakRealmSecurityDefensesHeadersOutputReference",
    "DataKeycloakRealmSecurityDefensesList",
    "DataKeycloakRealmSecurityDefensesOutputReference",
    "DataKeycloakRealmSmtpServer",
    "DataKeycloakRealmSmtpServerAuth",
    "DataKeycloakRealmSmtpServerAuthList",
    "DataKeycloakRealmSmtpServerAuthOutputReference",
    "DataKeycloakRealmSmtpServerList",
    "DataKeycloakRealmSmtpServerOutputReference",
    "DataKeycloakRealmWebAuthnPasswordlessPolicy",
    "DataKeycloakRealmWebAuthnPasswordlessPolicyOutputReference",
    "DataKeycloakRealmWebAuthnPolicy",
    "DataKeycloakRealmWebAuthnPolicyOutputReference",
]

publication.publish()


def _typecheckingstub__c9d6615c6488c13aa54ccc170a52a626100cdd5bf9b8bdb435544a9be69c4219(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    realm: builtins.str,
    attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    default_default_client_scopes: typing.Optional[
        typing.Sequence[builtins.str]
    ] = None,
    default_optional_client_scopes: typing.Optional[
        typing.Sequence[builtins.str]
    ] = None,
    display_name_html: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    internationalization: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    DataKeycloakRealmInternationalization,
                    typing.Dict[builtins.str, typing.Any],
                ]
            ],
        ]
    ] = None,
    otp_policy: typing.Optional[
        typing.Union[DataKeycloakRealmOtpPolicy, typing.Dict[builtins.str, typing.Any]]
    ] = None,
    security_defenses: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    DataKeycloakRealmSecurityDefenses,
                    typing.Dict[builtins.str, typing.Any],
                ]
            ],
        ]
    ] = None,
    smtp_server: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    DataKeycloakRealmSmtpServer, typing.Dict[builtins.str, typing.Any]
                ]
            ],
        ]
    ] = None,
    web_authn_passwordless_policy: typing.Optional[
        typing.Union[
            DataKeycloakRealmWebAuthnPasswordlessPolicy,
            typing.Dict[builtins.str, typing.Any],
        ]
    ] = None,
    web_authn_policy: typing.Optional[
        typing.Union[
            DataKeycloakRealmWebAuthnPolicy, typing.Dict[builtins.str, typing.Any]
        ]
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


def _typecheckingstub__fc844c7114c8893d9ae65ac56796e3a6b3732d31f270efde8aa2b90171341c53(
    value: typing.Union[
        _cdktf_9a9027ec.IResolvable,
        typing.Sequence[
            typing.Union[
                DataKeycloakRealmInternationalization,
                typing.Dict[builtins.str, typing.Any],
            ]
        ],
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__2d886d7ad6afec0644ad24dad0ed2e54008b5b8ed05429b228ca8f89f1f36792(
    value: typing.Union[
        _cdktf_9a9027ec.IResolvable,
        typing.Sequence[
            typing.Union[
                DataKeycloakRealmSecurityDefenses, typing.Dict[builtins.str, typing.Any]
            ]
        ],
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__37648ab3a9b72fc767782d6b81e1e585a8df75e50cea40642ab7bc57a38f794a(
    value: typing.Union[
        _cdktf_9a9027ec.IResolvable,
        typing.Sequence[
            typing.Union[
                DataKeycloakRealmSmtpServer, typing.Dict[builtins.str, typing.Any]
            ]
        ],
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__2fcb602cfaf917d55d45a9383a34d717703c7b723e5b68fb444681cb6c36a8d0(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ba40794978551bd660eea8a01b0422ba031c15e9e868f2200c255c9e1b4bfc47(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__14372f8ac324772e1f3910ccbe6fa6e04b340fd4e53f881fc01edb1e4f478244(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__bf487c8ac839bcfd34b6946efc0254a032d0c8cc14914c10c867e0d5e61c83e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__33cb741c68705accb42c7d0cf91c93a847c2cdebaf83ec654bc071e6ca8b93ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4793cf564c6c8679a07df4db6d4c7b4cccd28d048816ac7e47ac7860b97cbaad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7297e11b08e4dc237eb3d38b4021880b3b51fac6f716e412a693c32b7dd6ad6a(
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
    attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    default_default_client_scopes: typing.Optional[
        typing.Sequence[builtins.str]
    ] = None,
    default_optional_client_scopes: typing.Optional[
        typing.Sequence[builtins.str]
    ] = None,
    display_name_html: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    internationalization: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    DataKeycloakRealmInternationalization,
                    typing.Dict[builtins.str, typing.Any],
                ]
            ],
        ]
    ] = None,
    otp_policy: typing.Optional[
        typing.Union[DataKeycloakRealmOtpPolicy, typing.Dict[builtins.str, typing.Any]]
    ] = None,
    security_defenses: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    DataKeycloakRealmSecurityDefenses,
                    typing.Dict[builtins.str, typing.Any],
                ]
            ],
        ]
    ] = None,
    smtp_server: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    DataKeycloakRealmSmtpServer, typing.Dict[builtins.str, typing.Any]
                ]
            ],
        ]
    ] = None,
    web_authn_passwordless_policy: typing.Optional[
        typing.Union[
            DataKeycloakRealmWebAuthnPasswordlessPolicy,
            typing.Dict[builtins.str, typing.Any],
        ]
    ] = None,
    web_authn_policy: typing.Optional[
        typing.Union[
            DataKeycloakRealmWebAuthnPolicy, typing.Dict[builtins.str, typing.Any]
        ]
    ] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1f93181d7cdc84e5855e1b7aad266e31ccf014ec644f4d2c828efdf76a9c7c4f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__2e1d262dca5bd387633650a837d144b0f378e5aaa78dab665e0ffe2e07233cfa(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f5bfb0408b2bd1a52af1ee51cf036345edac3bd562cefd0451ae03039f6d64a1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__03b9c988402afd041796088c3f80a7add6685f766e0a71bb2e7bff324874f9cd(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ae26c1f82c6a40cf2a5c37a1553e506b8bda03632e999a9df8e47363d9fdc52e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a13910ee8f46a36acd7eb10bd524a8cd011107e5d550fd71fb370ebdcdbb49ec(
    value: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.List[DataKeycloakRealmInternationalization],
        ]
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9bb656b2eb86c1c5977ec255dfc9d4229bcaa7fe9756da59be5f8de1ca7c865a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__5b46c0b511d4c17b33a170b5a0a8eeff5787e53f4b274497381c64960c8a539b(
    value: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, DataKeycloakRealmInternationalization]
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__85ffb84f5c563f843786e14b380f1f0067fcb2fcd6da67ba378f4fb9186274a2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8220be0cf02d4ef2c475cbf3c7d88c62be3391e0b7a52a3ca812018ae14916fe(
    value: typing.Optional[DataKeycloakRealmOtpPolicy],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0345a1a6325c1cf653d5f7182c8b50f7eb2c27013422c62df07ee4ed60d7dd21(
    *,
    brute_force_detection: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    DataKeycloakRealmSecurityDefensesBruteForceDetection,
                    typing.Dict[builtins.str, typing.Any],
                ]
            ],
        ]
    ] = None,
    headers: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    DataKeycloakRealmSecurityDefensesHeaders,
                    typing.Dict[builtins.str, typing.Any],
                ]
            ],
        ]
    ] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e64aa82c20f4c054b06d89f1f3f6d1efdf7703eaf23ecbf6badf1e0c03e70850(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__147a090ffc6b881af8f7cc4ded88fcc3723162897a0bca42926d5c2ac839aa34(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9b0934c8a71d86462530c85024c1736a30199ec9e0e6b16505fb1ee44836794b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ecb698810358038da3b28c4d0c1199ecf214e06059b65a8982913b6b295e204c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__525765b0332357b016503165017c5f336a9df9dee775cbdcbbdeb57fbd59d5b5(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0e4d7d8857c0d1f6d3347d6e72d30baeeb738661dbb9cb0ed2a805fc91c086e5(
    value: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.List[DataKeycloakRealmSecurityDefensesBruteForceDetection],
        ]
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f0a07422957ecabaed4fe6b59af7e4657e9182f8961db7597af8306c72c35824(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0db1e2e2ace8bba3cfa9196e8be192190d6b85cb18e90982d06b0eb0a609fb69(
    value: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            DataKeycloakRealmSecurityDefensesBruteForceDetection,
        ]
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8a6011f492979e13b996e4dcfed55f8315c104c84452769fe8e0393d06c141d5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3e006510e492646fde7563ff1721864ab69bc1dc88dcf987fa73ebde8969cda7(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__eea27d552c0a3292b06048b773f07c0c8607fd7583c7d3d862a420c2a8e6bce6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__01536ef6872c9814baf1fefcafaa5612f1e006c6d4aaf1ba48dd925ff7d3696c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__fb144b446dafbb1923af5351bee3def80e00f90a7cb9f9f178f7f64e82383404(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__223eb251cca348f95a09cc29d1b4860d448771efbd896fad7442ccd279fdd315(
    value: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.List[DataKeycloakRealmSecurityDefensesHeaders],
        ]
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e0872fb1ebb77c40a39e3ed3c1d329018f57eba947ec32d42bc87261c5658f97(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7e4d4687953ae967a85b63c39e0b3d94ff5e296a2f2f2c946866a05c45d3ec36(
    value: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable, DataKeycloakRealmSecurityDefensesHeaders
        ]
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b10796ddecb5fd3469d0a355f37ab7fbc0bda71ed6ad929add36de209a8448cd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__2f2f8945b5672c5c7102b60677d69e4789a6bc4d523b1f007c47fb81ec3be044(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8286f0652ca21a2f661dcaaeef6a920020d373f4c07697571ecf90d110215095(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9c5bdb2ac4a12fa2bbbe2251ff83728b3258d564a676c1b8e32a80e889fd8ddb(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__022a1a9e77a00e66de674db9f4d8b5a360c483e40add02a38157272ef6971913(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__af1b9cd14d1f9c68e194dc4132fb50dc66683bfdb86ce96676300b3dfb72fb0b(
    value: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable, typing.List[DataKeycloakRealmSecurityDefenses]
        ]
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__31d799d351864f3221d9161ce573f73bda9eec5f5e2326b454f6bad52d8c9ab3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__56873da6086dfb7d3af0cc7c84a2030ffadea22cfeaa2196e5ad94b2bd396865(
    value: typing.Union[
        _cdktf_9a9027ec.IResolvable,
        typing.Sequence[
            typing.Union[
                DataKeycloakRealmSecurityDefensesBruteForceDetection,
                typing.Dict[builtins.str, typing.Any],
            ]
        ],
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ac86b4b4cd1a9444b70c048b9889738d3c578a2118e1ac184d0546b59cf3da47(
    value: typing.Union[
        _cdktf_9a9027ec.IResolvable,
        typing.Sequence[
            typing.Union[
                DataKeycloakRealmSecurityDefensesHeaders,
                typing.Dict[builtins.str, typing.Any],
            ]
        ],
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__cee275d043514eeee3178f291736db60c0bf1f409757cb8c9efe124bf5e2e334(
    value: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, DataKeycloakRealmSecurityDefenses]
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ec7b49d64d74a70bde2276c40c665928b188ac47779c34cd4d095df1aeb97e21(
    *,
    auth: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    DataKeycloakRealmSmtpServerAuth,
                    typing.Dict[builtins.str, typing.Any],
                ]
            ],
        ]
    ] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__39793921034d27304527349c183f0743164cc1acbd659e95b803ec113bd6f6e8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__23cf1543b8b7d0467cbf76e7c2ded4737fdeca8933e4c5a0f6ef463b581d8975(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__95738b0cfc83eeef4149edb74c94eb3d7f77ab3d317ad1daf3bb2bbb29209770(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__319da60ac97642b049c953de1e842c9117d6a62ae63b8ba7a81e591f8172393b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__80c7f414f0e349ce093057d97b6866c6293c226213af5b6d677e2c58f1f8f347(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c569deba1bdb84ddd1e747d2200faff8bfb1f56420890f4fe0a4b365c5b0a52e(
    value: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable, typing.List[DataKeycloakRealmSmtpServerAuth]
        ]
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4a42f7bf713a0572ef10c328d887cf847a64ba0425d42246b3414e7e234f6337(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__803f469896b19fc1b923aba79720ac7d408bec15d05ff8e0cd9aeabc63848dc7(
    value: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, DataKeycloakRealmSmtpServerAuth]
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ff3ceb424443bd77c325d16c75b3e311f3ff5af686d43158b747552bdca8746e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f51a763bf9420e4a6b6594bf340dad64019a82e5075475d5123b314008ba474b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b0142065cc658ecbb4be6d075a5c26e8bfaff549513b468ba317cbbf7a473d05(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__716ca3f48d9405943bd9cf4aa559567f0dec2bccd2c64cd9027da54ed2d6536e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__20efa2527717b3f98f5ef9f3fcb0731177c41b69d721f24c8d614ed6ff006134(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__154889b80837092229c52cf3d2a6decf07210270d9fc5e34e7dbb28b94953446(
    value: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable, typing.List[DataKeycloakRealmSmtpServer]
        ]
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__55c2d552b68328cbfba4fb1eca892ec6577ca6d55cbedc2555fa2aefa683a2f6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6e6471bcfc7fe074ad8fbc7920bd05c8d0435fcd8f18bc3da4dd61df563f1fe8(
    value: typing.Union[
        _cdktf_9a9027ec.IResolvable,
        typing.Sequence[
            typing.Union[
                DataKeycloakRealmSmtpServerAuth, typing.Dict[builtins.str, typing.Any]
            ]
        ],
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d61915b17fb4a9cc2e24c9cd81e1acd84b04944792fea9b5904f1731af78810d(
    value: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, DataKeycloakRealmSmtpServer]
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__72c015e1598c47c12185b368fbc16b90bffde5f8182cff789c2e05d6a97072d0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__944aff65ec826567419c6ae97dbec8d4c67ceed355160df2c0ecd6cfeb7056cb(
    value: typing.Optional[DataKeycloakRealmWebAuthnPasswordlessPolicy],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ad5ade617d5643cadfffbe930643637f4b1b1ee54ac0d6a5658fddc5501500f4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__28c65b1772966d242f221740a2f58b77c7fd1d21b54943641aa3af46b1570f49(
    value: typing.Optional[DataKeycloakRealmWebAuthnPolicy],
) -> None:
    """Type checking stubs"""
    pass
