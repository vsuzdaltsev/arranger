"""
# `keycloak_saml_client`

Refer to the Terraform Registory for docs: [`keycloak_saml_client`](https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client).
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


class SamlClient(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.samlClient.SamlClient",
):
    """Represents a {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client keycloak_saml_client}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        client_id: builtins.str,
        realm_id: builtins.str,
        assertion_consumer_post_url: typing.Optional[builtins.str] = None,
        assertion_consumer_redirect_url: typing.Optional[builtins.str] = None,
        authentication_flow_binding_overrides: typing.Optional[
            typing.Union[
                "SamlClientAuthenticationFlowBindingOverrides",
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        base_url: typing.Optional[builtins.str] = None,
        canonicalization_method: typing.Optional[builtins.str] = None,
        client_signature_required: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        encrypt_assertions: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        encryption_certificate: typing.Optional[builtins.str] = None,
        extra_config: typing.Optional[
            typing.Mapping[builtins.str, builtins.str]
        ] = None,
        force_name_id_format: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        force_post_binding: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        front_channel_logout: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        full_scope_allowed: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        id: typing.Optional[builtins.str] = None,
        idp_initiated_sso_relay_state: typing.Optional[builtins.str] = None,
        idp_initiated_sso_url_name: typing.Optional[builtins.str] = None,
        include_authn_statement: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        login_theme: typing.Optional[builtins.str] = None,
        logout_service_post_binding_url: typing.Optional[builtins.str] = None,
        logout_service_redirect_binding_url: typing.Optional[builtins.str] = None,
        master_saml_processing_url: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        name_id_format: typing.Optional[builtins.str] = None,
        root_url: typing.Optional[builtins.str] = None,
        sign_assertions: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        signature_algorithm: typing.Optional[builtins.str] = None,
        signature_key_name: typing.Optional[builtins.str] = None,
        sign_documents: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        signing_certificate: typing.Optional[builtins.str] = None,
        signing_private_key: typing.Optional[builtins.str] = None,
        valid_redirect_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
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
        """Create a new {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client keycloak_saml_client} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param client_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#client_id SamlClient#client_id}.
        :param realm_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#realm_id SamlClient#realm_id}.
        :param assertion_consumer_post_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#assertion_consumer_post_url SamlClient#assertion_consumer_post_url}.
        :param assertion_consumer_redirect_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#assertion_consumer_redirect_url SamlClient#assertion_consumer_redirect_url}.
        :param authentication_flow_binding_overrides: authentication_flow_binding_overrides block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#authentication_flow_binding_overrides SamlClient#authentication_flow_binding_overrides}
        :param base_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#base_url SamlClient#base_url}.
        :param canonicalization_method: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#canonicalization_method SamlClient#canonicalization_method}.
        :param client_signature_required: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#client_signature_required SamlClient#client_signature_required}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#description SamlClient#description}.
        :param enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#enabled SamlClient#enabled}.
        :param encrypt_assertions: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#encrypt_assertions SamlClient#encrypt_assertions}.
        :param encryption_certificate: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#encryption_certificate SamlClient#encryption_certificate}.
        :param extra_config: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#extra_config SamlClient#extra_config}.
        :param force_name_id_format: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#force_name_id_format SamlClient#force_name_id_format}.
        :param force_post_binding: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#force_post_binding SamlClient#force_post_binding}.
        :param front_channel_logout: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#front_channel_logout SamlClient#front_channel_logout}.
        :param full_scope_allowed: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#full_scope_allowed SamlClient#full_scope_allowed}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#id SamlClient#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param idp_initiated_sso_relay_state: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#idp_initiated_sso_relay_state SamlClient#idp_initiated_sso_relay_state}.
        :param idp_initiated_sso_url_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#idp_initiated_sso_url_name SamlClient#idp_initiated_sso_url_name}.
        :param include_authn_statement: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#include_authn_statement SamlClient#include_authn_statement}.
        :param login_theme: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#login_theme SamlClient#login_theme}.
        :param logout_service_post_binding_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#logout_service_post_binding_url SamlClient#logout_service_post_binding_url}.
        :param logout_service_redirect_binding_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#logout_service_redirect_binding_url SamlClient#logout_service_redirect_binding_url}.
        :param master_saml_processing_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#master_saml_processing_url SamlClient#master_saml_processing_url}.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#name SamlClient#name}.
        :param name_id_format: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#name_id_format SamlClient#name_id_format}.
        :param root_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#root_url SamlClient#root_url}.
        :param sign_assertions: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#sign_assertions SamlClient#sign_assertions}.
        :param signature_algorithm: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#signature_algorithm SamlClient#signature_algorithm}.
        :param signature_key_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#signature_key_name SamlClient#signature_key_name}.
        :param sign_documents: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#sign_documents SamlClient#sign_documents}.
        :param signing_certificate: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#signing_certificate SamlClient#signing_certificate}.
        :param signing_private_key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#signing_private_key SamlClient#signing_private_key}.
        :param valid_redirect_uris: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#valid_redirect_uris SamlClient#valid_redirect_uris}.
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
                _typecheckingstub__08b441a8e8453afef5418c091c41c9cecac62a5fddba783b8c676935ff028967
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(
                argname="argument id_", value=id_, expected_type=type_hints["id_"]
            )
        config = SamlClientConfig(
            client_id=client_id,
            realm_id=realm_id,
            assertion_consumer_post_url=assertion_consumer_post_url,
            assertion_consumer_redirect_url=assertion_consumer_redirect_url,
            authentication_flow_binding_overrides=authentication_flow_binding_overrides,
            base_url=base_url,
            canonicalization_method=canonicalization_method,
            client_signature_required=client_signature_required,
            description=description,
            enabled=enabled,
            encrypt_assertions=encrypt_assertions,
            encryption_certificate=encryption_certificate,
            extra_config=extra_config,
            force_name_id_format=force_name_id_format,
            force_post_binding=force_post_binding,
            front_channel_logout=front_channel_logout,
            full_scope_allowed=full_scope_allowed,
            id=id,
            idp_initiated_sso_relay_state=idp_initiated_sso_relay_state,
            idp_initiated_sso_url_name=idp_initiated_sso_url_name,
            include_authn_statement=include_authn_statement,
            login_theme=login_theme,
            logout_service_post_binding_url=logout_service_post_binding_url,
            logout_service_redirect_binding_url=logout_service_redirect_binding_url,
            master_saml_processing_url=master_saml_processing_url,
            name=name,
            name_id_format=name_id_format,
            root_url=root_url,
            sign_assertions=sign_assertions,
            signature_algorithm=signature_algorithm,
            signature_key_name=signature_key_name,
            sign_documents=sign_documents,
            signing_certificate=signing_certificate,
            signing_private_key=signing_private_key,
            valid_redirect_uris=valid_redirect_uris,
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
        :param browser_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#browser_id SamlClient#browser_id}.
        :param direct_grant_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#direct_grant_id SamlClient#direct_grant_id}.
        """
        value = SamlClientAuthenticationFlowBindingOverrides(
            browser_id=browser_id, direct_grant_id=direct_grant_id
        )

        return typing.cast(
            None, jsii.invoke(self, "putAuthenticationFlowBindingOverrides", [value])
        )

    @jsii.member(jsii_name="resetAssertionConsumerPostUrl")
    def reset_assertion_consumer_post_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssertionConsumerPostUrl", []))

    @jsii.member(jsii_name="resetAssertionConsumerRedirectUrl")
    def reset_assertion_consumer_redirect_url(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetAssertionConsumerRedirectUrl", [])
        )

    @jsii.member(jsii_name="resetAuthenticationFlowBindingOverrides")
    def reset_authentication_flow_binding_overrides(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetAuthenticationFlowBindingOverrides", [])
        )

    @jsii.member(jsii_name="resetBaseUrl")
    def reset_base_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBaseUrl", []))

    @jsii.member(jsii_name="resetCanonicalizationMethod")
    def reset_canonicalization_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCanonicalizationMethod", []))

    @jsii.member(jsii_name="resetClientSignatureRequired")
    def reset_client_signature_required(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientSignatureRequired", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetEncryptAssertions")
    def reset_encrypt_assertions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptAssertions", []))

    @jsii.member(jsii_name="resetEncryptionCertificate")
    def reset_encryption_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionCertificate", []))

    @jsii.member(jsii_name="resetExtraConfig")
    def reset_extra_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtraConfig", []))

    @jsii.member(jsii_name="resetForceNameIdFormat")
    def reset_force_name_id_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceNameIdFormat", []))

    @jsii.member(jsii_name="resetForcePostBinding")
    def reset_force_post_binding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForcePostBinding", []))

    @jsii.member(jsii_name="resetFrontChannelLogout")
    def reset_front_channel_logout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFrontChannelLogout", []))

    @jsii.member(jsii_name="resetFullScopeAllowed")
    def reset_full_scope_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFullScopeAllowed", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdpInitiatedSsoRelayState")
    def reset_idp_initiated_sso_relay_state(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetIdpInitiatedSsoRelayState", [])
        )

    @jsii.member(jsii_name="resetIdpInitiatedSsoUrlName")
    def reset_idp_initiated_sso_url_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdpInitiatedSsoUrlName", []))

    @jsii.member(jsii_name="resetIncludeAuthnStatement")
    def reset_include_authn_statement(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeAuthnStatement", []))

    @jsii.member(jsii_name="resetLoginTheme")
    def reset_login_theme(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoginTheme", []))

    @jsii.member(jsii_name="resetLogoutServicePostBindingUrl")
    def reset_logout_service_post_binding_url(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetLogoutServicePostBindingUrl", [])
        )

    @jsii.member(jsii_name="resetLogoutServiceRedirectBindingUrl")
    def reset_logout_service_redirect_binding_url(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetLogoutServiceRedirectBindingUrl", [])
        )

    @jsii.member(jsii_name="resetMasterSamlProcessingUrl")
    def reset_master_saml_processing_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMasterSamlProcessingUrl", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNameIdFormat")
    def reset_name_id_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNameIdFormat", []))

    @jsii.member(jsii_name="resetRootUrl")
    def reset_root_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootUrl", []))

    @jsii.member(jsii_name="resetSignAssertions")
    def reset_sign_assertions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSignAssertions", []))

    @jsii.member(jsii_name="resetSignatureAlgorithm")
    def reset_signature_algorithm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSignatureAlgorithm", []))

    @jsii.member(jsii_name="resetSignatureKeyName")
    def reset_signature_key_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSignatureKeyName", []))

    @jsii.member(jsii_name="resetSignDocuments")
    def reset_sign_documents(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSignDocuments", []))

    @jsii.member(jsii_name="resetSigningCertificate")
    def reset_signing_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSigningCertificate", []))

    @jsii.member(jsii_name="resetSigningPrivateKey")
    def reset_signing_private_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSigningPrivateKey", []))

    @jsii.member(jsii_name="resetValidRedirectUris")
    def reset_valid_redirect_uris(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValidRedirectUris", []))

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
    ) -> "SamlClientAuthenticationFlowBindingOverridesOutputReference":
        return typing.cast(
            "SamlClientAuthenticationFlowBindingOverridesOutputReference",
            jsii.get(self, "authenticationFlowBindingOverrides"),
        )

    @builtins.property
    @jsii.member(jsii_name="encryptionCertificateSha1")
    def encryption_certificate_sha1(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptionCertificateSha1"))

    @builtins.property
    @jsii.member(jsii_name="signingCertificateSha1")
    def signing_certificate_sha1(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signingCertificateSha1"))

    @builtins.property
    @jsii.member(jsii_name="signingPrivateKeySha1")
    def signing_private_key_sha1(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signingPrivateKeySha1"))

    @builtins.property
    @jsii.member(jsii_name="assertionConsumerPostUrlInput")
    def assertion_consumer_post_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "assertionConsumerPostUrlInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="assertionConsumerRedirectUrlInput")
    def assertion_consumer_redirect_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "assertionConsumerRedirectUrlInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="authenticationFlowBindingOverridesInput")
    def authentication_flow_binding_overrides_input(
        self,
    ) -> typing.Optional["SamlClientAuthenticationFlowBindingOverrides"]:
        return typing.cast(
            typing.Optional["SamlClientAuthenticationFlowBindingOverrides"],
            jsii.get(self, "authenticationFlowBindingOverridesInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="baseUrlInput")
    def base_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "baseUrlInput")
        )

    @builtins.property
    @jsii.member(jsii_name="canonicalizationMethodInput")
    def canonicalization_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "canonicalizationMethodInput")
        )

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "clientIdInput")
        )

    @builtins.property
    @jsii.member(jsii_name="clientSignatureRequiredInput")
    def client_signature_required_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "clientSignatureRequiredInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "descriptionInput")
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
    @jsii.member(jsii_name="encryptAssertionsInput")
    def encrypt_assertions_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "encryptAssertionsInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="encryptionCertificateInput")
    def encryption_certificate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "encryptionCertificateInput")
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
    @jsii.member(jsii_name="forceNameIdFormatInput")
    def force_name_id_format_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "forceNameIdFormatInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="forcePostBindingInput")
    def force_post_binding_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "forcePostBindingInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="frontChannelLogoutInput")
    def front_channel_logout_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "frontChannelLogoutInput"),
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
    @jsii.member(jsii_name="idpInitiatedSsoRelayStateInput")
    def idp_initiated_sso_relay_state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "idpInitiatedSsoRelayStateInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="idpInitiatedSsoUrlNameInput")
    def idp_initiated_sso_url_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "idpInitiatedSsoUrlNameInput")
        )

    @builtins.property
    @jsii.member(jsii_name="includeAuthnStatementInput")
    def include_authn_statement_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "includeAuthnStatementInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="loginThemeInput")
    def login_theme_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "loginThemeInput")
        )

    @builtins.property
    @jsii.member(jsii_name="logoutServicePostBindingUrlInput")
    def logout_service_post_binding_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "logoutServicePostBindingUrlInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="logoutServiceRedirectBindingUrlInput")
    def logout_service_redirect_binding_url_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "logoutServiceRedirectBindingUrlInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="masterSamlProcessingUrlInput")
    def master_saml_processing_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "masterSamlProcessingUrlInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="nameIdFormatInput")
    def name_id_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "nameIdFormatInput")
        )

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

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
    @jsii.member(jsii_name="signAssertionsInput")
    def sign_assertions_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "signAssertionsInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="signatureAlgorithmInput")
    def signature_algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "signatureAlgorithmInput")
        )

    @builtins.property
    @jsii.member(jsii_name="signatureKeyNameInput")
    def signature_key_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "signatureKeyNameInput")
        )

    @builtins.property
    @jsii.member(jsii_name="signDocumentsInput")
    def sign_documents_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "signDocumentsInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="signingCertificateInput")
    def signing_certificate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "signingCertificateInput")
        )

    @builtins.property
    @jsii.member(jsii_name="signingPrivateKeyInput")
    def signing_private_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "signingPrivateKeyInput")
        )

    @builtins.property
    @jsii.member(jsii_name="validRedirectUrisInput")
    def valid_redirect_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]],
            jsii.get(self, "validRedirectUrisInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="assertionConsumerPostUrl")
    def assertion_consumer_post_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "assertionConsumerPostUrl"))

    @assertion_consumer_post_url.setter
    def assertion_consumer_post_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__c9a60d05dd674ae3a183b347683413ab46c434e4c6aca5e4016e03c8f4e46aaa
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "assertionConsumerPostUrl", value)

    @builtins.property
    @jsii.member(jsii_name="assertionConsumerRedirectUrl")
    def assertion_consumer_redirect_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "assertionConsumerRedirectUrl"))

    @assertion_consumer_redirect_url.setter
    def assertion_consumer_redirect_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__9fa262e12e0090d8e57744604a189ed5e1fc9d5b707b513d4d5b3119bc10d70b
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "assertionConsumerRedirectUrl", value)

    @builtins.property
    @jsii.member(jsii_name="baseUrl")
    def base_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "baseUrl"))

    @base_url.setter
    def base_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a490941bfd183a4c2eb320ce33ee100c4559e88f383f027aa55fe3059d87c255
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "baseUrl", value)

    @builtins.property
    @jsii.member(jsii_name="canonicalizationMethod")
    def canonicalization_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "canonicalizationMethod"))

    @canonicalization_method.setter
    def canonicalization_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__07cf523b878d713abf3471c3b4ecd365cdcc7d8edd262b69a53277ee3deddfcc
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "canonicalizationMethod", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__7f78460700755961a5708febe5d4f01873945aa84e4b21f7e76844b4c8d84f91
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSignatureRequired")
    def client_signature_required(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "clientSignatureRequired"),
        )

    @client_signature_required.setter
    def client_signature_required(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__e4b56cd868ab1adf1b2809de841d16d3d0180df53b365c702de5e6cc70294325
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "clientSignatureRequired", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__09f19a076d07466889e04cc705b8c6708bc4f29ed2eb6011e4b554c8d480e109
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "description", value)

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
                _typecheckingstub__9d5b50bc3b5f6423b963c6eb3124d7fc4f4996a977506d3293faaf6f28143537
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="encryptAssertions")
    def encrypt_assertions(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "encryptAssertions"),
        )

    @encrypt_assertions.setter
    def encrypt_assertions(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__c11001ebe587445436473ce0ae973c938c756a2d6fae55153734e7fe1444555c
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "encryptAssertions", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionCertificate")
    def encryption_certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptionCertificate"))

    @encryption_certificate.setter
    def encryption_certificate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__e2f6982c1c20b03416de3ead06a3a96f2ccd88740ebb571f8df6a2a54b58e8df
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "encryptionCertificate", value)

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
                _typecheckingstub__c1ace4ef8115089a45a9a11c89cb76b2194776cbbd197219c7608a9e36036711
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "extraConfig", value)

    @builtins.property
    @jsii.member(jsii_name="forceNameIdFormat")
    def force_name_id_format(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "forceNameIdFormat"),
        )

    @force_name_id_format.setter
    def force_name_id_format(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__cd3825c540ac52fbb18b8493d16306f810c67d3f2e76903e7c4d7e8a7135940c
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "forceNameIdFormat", value)

    @builtins.property
    @jsii.member(jsii_name="forcePostBinding")
    def force_post_binding(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "forcePostBinding"),
        )

    @force_post_binding.setter
    def force_post_binding(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__8b531389d6f19d8a40081f520022ef6daed02841b8a0e367024b5c4cbef058f6
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "forcePostBinding", value)

    @builtins.property
    @jsii.member(jsii_name="frontChannelLogout")
    def front_channel_logout(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "frontChannelLogout"),
        )

    @front_channel_logout.setter
    def front_channel_logout(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__6251b5561f302bbf2107682c9baaa7956ea606a1f669c14078d5bc595bfbd643
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "frontChannelLogout", value)

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
                _typecheckingstub__3f9ee25d5e81d22eb3824129da4db68f94b919fb39a69b2956782b74f3124c27
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
                _typecheckingstub__7b346d20bf78d3c135ead9d5dfdeef94b86636aaa87aef2ad1603d76fa030652
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="idpInitiatedSsoRelayState")
    def idp_initiated_sso_relay_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "idpInitiatedSsoRelayState"))

    @idp_initiated_sso_relay_state.setter
    def idp_initiated_sso_relay_state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__0ba36e67f1dc80df02e5cc898070a40b8a0adae6135095623826523e4535568c
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "idpInitiatedSsoRelayState", value)

    @builtins.property
    @jsii.member(jsii_name="idpInitiatedSsoUrlName")
    def idp_initiated_sso_url_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "idpInitiatedSsoUrlName"))

    @idp_initiated_sso_url_name.setter
    def idp_initiated_sso_url_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__aef12f14893495c68bab38573de50e7f510e68ab351e71beec8b1cda54657e1c
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "idpInitiatedSsoUrlName", value)

    @builtins.property
    @jsii.member(jsii_name="includeAuthnStatement")
    def include_authn_statement(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "includeAuthnStatement"),
        )

    @include_authn_statement.setter
    def include_authn_statement(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__bafecc3c41637f9f2ecd2879af3c728a1f67402074355de16f28731faf043d9a
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "includeAuthnStatement", value)

    @builtins.property
    @jsii.member(jsii_name="loginTheme")
    def login_theme(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loginTheme"))

    @login_theme.setter
    def login_theme(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__72fec20de99ec41b53524d5c4b072c7e1c7c4346ab562fbaae4df4846c0cc8c6
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "loginTheme", value)

    @builtins.property
    @jsii.member(jsii_name="logoutServicePostBindingUrl")
    def logout_service_post_binding_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logoutServicePostBindingUrl"))

    @logout_service_post_binding_url.setter
    def logout_service_post_binding_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__3665b2e7a1036f087f172d4226dd0a6d68cde386b1704f40f4176183ea8fe4d4
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "logoutServicePostBindingUrl", value)

    @builtins.property
    @jsii.member(jsii_name="logoutServiceRedirectBindingUrl")
    def logout_service_redirect_binding_url(self) -> builtins.str:
        return typing.cast(
            builtins.str, jsii.get(self, "logoutServiceRedirectBindingUrl")
        )

    @logout_service_redirect_binding_url.setter
    def logout_service_redirect_binding_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__2b51403fb4016a3f343d819fbd56540477153f8774c1aaca9546bbc8269000b1
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "logoutServiceRedirectBindingUrl", value)

    @builtins.property
    @jsii.member(jsii_name="masterSamlProcessingUrl")
    def master_saml_processing_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "masterSamlProcessingUrl"))

    @master_saml_processing_url.setter
    def master_saml_processing_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__e42116a6ff8814f6dbbdc624f46fb2cd6bfc6e75f4293b3535d1c49aab0788dc
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "masterSamlProcessingUrl", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__6d80bf8b6cb82d707221fd8a072da4c9bece8add0ec113ff934b0870999214d7
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="nameIdFormat")
    def name_id_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nameIdFormat"))

    @name_id_format.setter
    def name_id_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__bb62271e007756755c8de4033f833e482f18a2fb4443f34e7fad53465a25abf8
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "nameIdFormat", value)

    @builtins.property
    @jsii.member(jsii_name="realmId")
    def realm_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "realmId"))

    @realm_id.setter
    def realm_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__8f43a551557b2d349ec2e77636a3896b71342aabaef882ec1c8e308039bd5e21
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
                _typecheckingstub__83f71e0a49caa40c2d53ecdd4058f402fa7e4776dcf506d3abf3d8419183d4af
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "rootUrl", value)

    @builtins.property
    @jsii.member(jsii_name="signAssertions")
    def sign_assertions(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "signAssertions"),
        )

    @sign_assertions.setter
    def sign_assertions(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__43f824ed8aa6a2741c1cdf8aae7ab7eab216e7847326df43f002016bbe5b61eb
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "signAssertions", value)

    @builtins.property
    @jsii.member(jsii_name="signatureAlgorithm")
    def signature_algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signatureAlgorithm"))

    @signature_algorithm.setter
    def signature_algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__0a4d583f25571a9fa8a4105509bf6440bef34f20561020a3da7f24e79fb3cef1
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "signatureAlgorithm", value)

    @builtins.property
    @jsii.member(jsii_name="signatureKeyName")
    def signature_key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signatureKeyName"))

    @signature_key_name.setter
    def signature_key_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__f1b84bf6aec8dee7bfe24903b9c3fd2b025d157dc4132b48119266fa827e85c6
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "signatureKeyName", value)

    @builtins.property
    @jsii.member(jsii_name="signDocuments")
    def sign_documents(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "signDocuments"),
        )

    @sign_documents.setter
    def sign_documents(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__ef556c6f8a72dddf87bb6d8144040124fdcd73d4812184db6c8e426b351f4486
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "signDocuments", value)

    @builtins.property
    @jsii.member(jsii_name="signingCertificate")
    def signing_certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signingCertificate"))

    @signing_certificate.setter
    def signing_certificate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__379b38c80fbef47385d40f262f14eb46b75fc155ee30717d82ff26cb773904fb
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "signingCertificate", value)

    @builtins.property
    @jsii.member(jsii_name="signingPrivateKey")
    def signing_private_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signingPrivateKey"))

    @signing_private_key.setter
    def signing_private_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__8d0b5abff4d7115995616b6a1a20acd17ff9b9d30e66c687716a4c75240f3a80
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "signingPrivateKey", value)

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
                _typecheckingstub__739d871486a57e7c25b17857dc79a0fe460079f84fa869805db2c20d272e9387
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "validRedirectUris", value)


@jsii.data_type(
    jsii_type="keycloak.samlClient.SamlClientAuthenticationFlowBindingOverrides",
    jsii_struct_bases=[],
    name_mapping={"browser_id": "browserId", "direct_grant_id": "directGrantId"},
)
class SamlClientAuthenticationFlowBindingOverrides:
    def __init__(
        self,
        *,
        browser_id: typing.Optional[builtins.str] = None,
        direct_grant_id: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param browser_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#browser_id SamlClient#browser_id}.
        :param direct_grant_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#direct_grant_id SamlClient#direct_grant_id}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d5fe979020ade3c1f3e25a50954fb5513e3feadcc3461ffb1100733c68dafc23
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
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#browser_id SamlClient#browser_id}."""
        result = self._values.get("browser_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def direct_grant_id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#direct_grant_id SamlClient#direct_grant_id}."""
        result = self._values.get("direct_grant_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SamlClientAuthenticationFlowBindingOverrides(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SamlClientAuthenticationFlowBindingOverridesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.samlClient.SamlClientAuthenticationFlowBindingOverridesOutputReference",
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
                _typecheckingstub__eaf20a85a25f3078945735d519344501708439cdc14aa5ec70e6c128d953ef0b
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
                _typecheckingstub__e11faf659a57824f03a9e5712e195e1f1cc8414f55eb9c6af0990d56845a7e54
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
                _typecheckingstub__77bd9eaea08b93f0dbfb9e7443fefae9daf1a47cd6d9395cadd7668482c3fdbe
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "directGrantId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SamlClientAuthenticationFlowBindingOverrides]:
        return typing.cast(
            typing.Optional[SamlClientAuthenticationFlowBindingOverrides],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SamlClientAuthenticationFlowBindingOverrides],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d9a86ef32d7714a10ff90f23856309178a08c38806b5a7a466dae66e79ea086d
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="keycloak.samlClient.SamlClientConfig",
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
        "assertion_consumer_post_url": "assertionConsumerPostUrl",
        "assertion_consumer_redirect_url": "assertionConsumerRedirectUrl",
        "authentication_flow_binding_overrides": "authenticationFlowBindingOverrides",
        "base_url": "baseUrl",
        "canonicalization_method": "canonicalizationMethod",
        "client_signature_required": "clientSignatureRequired",
        "description": "description",
        "enabled": "enabled",
        "encrypt_assertions": "encryptAssertions",
        "encryption_certificate": "encryptionCertificate",
        "extra_config": "extraConfig",
        "force_name_id_format": "forceNameIdFormat",
        "force_post_binding": "forcePostBinding",
        "front_channel_logout": "frontChannelLogout",
        "full_scope_allowed": "fullScopeAllowed",
        "id": "id",
        "idp_initiated_sso_relay_state": "idpInitiatedSsoRelayState",
        "idp_initiated_sso_url_name": "idpInitiatedSsoUrlName",
        "include_authn_statement": "includeAuthnStatement",
        "login_theme": "loginTheme",
        "logout_service_post_binding_url": "logoutServicePostBindingUrl",
        "logout_service_redirect_binding_url": "logoutServiceRedirectBindingUrl",
        "master_saml_processing_url": "masterSamlProcessingUrl",
        "name": "name",
        "name_id_format": "nameIdFormat",
        "root_url": "rootUrl",
        "sign_assertions": "signAssertions",
        "signature_algorithm": "signatureAlgorithm",
        "signature_key_name": "signatureKeyName",
        "sign_documents": "signDocuments",
        "signing_certificate": "signingCertificate",
        "signing_private_key": "signingPrivateKey",
        "valid_redirect_uris": "validRedirectUris",
    },
)
class SamlClientConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        assertion_consumer_post_url: typing.Optional[builtins.str] = None,
        assertion_consumer_redirect_url: typing.Optional[builtins.str] = None,
        authentication_flow_binding_overrides: typing.Optional[
            typing.Union[
                SamlClientAuthenticationFlowBindingOverrides,
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        base_url: typing.Optional[builtins.str] = None,
        canonicalization_method: typing.Optional[builtins.str] = None,
        client_signature_required: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        encrypt_assertions: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        encryption_certificate: typing.Optional[builtins.str] = None,
        extra_config: typing.Optional[
            typing.Mapping[builtins.str, builtins.str]
        ] = None,
        force_name_id_format: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        force_post_binding: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        front_channel_logout: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        full_scope_allowed: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        id: typing.Optional[builtins.str] = None,
        idp_initiated_sso_relay_state: typing.Optional[builtins.str] = None,
        idp_initiated_sso_url_name: typing.Optional[builtins.str] = None,
        include_authn_statement: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        login_theme: typing.Optional[builtins.str] = None,
        logout_service_post_binding_url: typing.Optional[builtins.str] = None,
        logout_service_redirect_binding_url: typing.Optional[builtins.str] = None,
        master_saml_processing_url: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        name_id_format: typing.Optional[builtins.str] = None,
        root_url: typing.Optional[builtins.str] = None,
        sign_assertions: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        signature_algorithm: typing.Optional[builtins.str] = None,
        signature_key_name: typing.Optional[builtins.str] = None,
        sign_documents: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        signing_certificate: typing.Optional[builtins.str] = None,
        signing_private_key: typing.Optional[builtins.str] = None,
        valid_redirect_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param connection:
        :param count:
        :param depends_on:
        :param for_each:
        :param lifecycle:
        :param provider:
        :param provisioners:
        :param client_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#client_id SamlClient#client_id}.
        :param realm_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#realm_id SamlClient#realm_id}.
        :param assertion_consumer_post_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#assertion_consumer_post_url SamlClient#assertion_consumer_post_url}.
        :param assertion_consumer_redirect_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#assertion_consumer_redirect_url SamlClient#assertion_consumer_redirect_url}.
        :param authentication_flow_binding_overrides: authentication_flow_binding_overrides block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#authentication_flow_binding_overrides SamlClient#authentication_flow_binding_overrides}
        :param base_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#base_url SamlClient#base_url}.
        :param canonicalization_method: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#canonicalization_method SamlClient#canonicalization_method}.
        :param client_signature_required: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#client_signature_required SamlClient#client_signature_required}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#description SamlClient#description}.
        :param enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#enabled SamlClient#enabled}.
        :param encrypt_assertions: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#encrypt_assertions SamlClient#encrypt_assertions}.
        :param encryption_certificate: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#encryption_certificate SamlClient#encryption_certificate}.
        :param extra_config: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#extra_config SamlClient#extra_config}.
        :param force_name_id_format: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#force_name_id_format SamlClient#force_name_id_format}.
        :param force_post_binding: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#force_post_binding SamlClient#force_post_binding}.
        :param front_channel_logout: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#front_channel_logout SamlClient#front_channel_logout}.
        :param full_scope_allowed: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#full_scope_allowed SamlClient#full_scope_allowed}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#id SamlClient#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param idp_initiated_sso_relay_state: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#idp_initiated_sso_relay_state SamlClient#idp_initiated_sso_relay_state}.
        :param idp_initiated_sso_url_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#idp_initiated_sso_url_name SamlClient#idp_initiated_sso_url_name}.
        :param include_authn_statement: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#include_authn_statement SamlClient#include_authn_statement}.
        :param login_theme: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#login_theme SamlClient#login_theme}.
        :param logout_service_post_binding_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#logout_service_post_binding_url SamlClient#logout_service_post_binding_url}.
        :param logout_service_redirect_binding_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#logout_service_redirect_binding_url SamlClient#logout_service_redirect_binding_url}.
        :param master_saml_processing_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#master_saml_processing_url SamlClient#master_saml_processing_url}.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#name SamlClient#name}.
        :param name_id_format: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#name_id_format SamlClient#name_id_format}.
        :param root_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#root_url SamlClient#root_url}.
        :param sign_assertions: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#sign_assertions SamlClient#sign_assertions}.
        :param signature_algorithm: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#signature_algorithm SamlClient#signature_algorithm}.
        :param signature_key_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#signature_key_name SamlClient#signature_key_name}.
        :param sign_documents: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#sign_documents SamlClient#sign_documents}.
        :param signing_certificate: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#signing_certificate SamlClient#signing_certificate}.
        :param signing_private_key: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#signing_private_key SamlClient#signing_private_key}.
        :param valid_redirect_uris: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#valid_redirect_uris SamlClient#valid_redirect_uris}.
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(authentication_flow_binding_overrides, dict):
            authentication_flow_binding_overrides = (
                SamlClientAuthenticationFlowBindingOverrides(
                    **authentication_flow_binding_overrides
                )
            )
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__e2d862ca0df36108e3e5a88e83c5e9ec7559515446862b1b9bf212aa12c8601d
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
                argname="argument assertion_consumer_post_url",
                value=assertion_consumer_post_url,
                expected_type=type_hints["assertion_consumer_post_url"],
            )
            check_type(
                argname="argument assertion_consumer_redirect_url",
                value=assertion_consumer_redirect_url,
                expected_type=type_hints["assertion_consumer_redirect_url"],
            )
            check_type(
                argname="argument authentication_flow_binding_overrides",
                value=authentication_flow_binding_overrides,
                expected_type=type_hints["authentication_flow_binding_overrides"],
            )
            check_type(
                argname="argument base_url",
                value=base_url,
                expected_type=type_hints["base_url"],
            )
            check_type(
                argname="argument canonicalization_method",
                value=canonicalization_method,
                expected_type=type_hints["canonicalization_method"],
            )
            check_type(
                argname="argument client_signature_required",
                value=client_signature_required,
                expected_type=type_hints["client_signature_required"],
            )
            check_type(
                argname="argument description",
                value=description,
                expected_type=type_hints["description"],
            )
            check_type(
                argname="argument enabled",
                value=enabled,
                expected_type=type_hints["enabled"],
            )
            check_type(
                argname="argument encrypt_assertions",
                value=encrypt_assertions,
                expected_type=type_hints["encrypt_assertions"],
            )
            check_type(
                argname="argument encryption_certificate",
                value=encryption_certificate,
                expected_type=type_hints["encryption_certificate"],
            )
            check_type(
                argname="argument extra_config",
                value=extra_config,
                expected_type=type_hints["extra_config"],
            )
            check_type(
                argname="argument force_name_id_format",
                value=force_name_id_format,
                expected_type=type_hints["force_name_id_format"],
            )
            check_type(
                argname="argument force_post_binding",
                value=force_post_binding,
                expected_type=type_hints["force_post_binding"],
            )
            check_type(
                argname="argument front_channel_logout",
                value=front_channel_logout,
                expected_type=type_hints["front_channel_logout"],
            )
            check_type(
                argname="argument full_scope_allowed",
                value=full_scope_allowed,
                expected_type=type_hints["full_scope_allowed"],
            )
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(
                argname="argument idp_initiated_sso_relay_state",
                value=idp_initiated_sso_relay_state,
                expected_type=type_hints["idp_initiated_sso_relay_state"],
            )
            check_type(
                argname="argument idp_initiated_sso_url_name",
                value=idp_initiated_sso_url_name,
                expected_type=type_hints["idp_initiated_sso_url_name"],
            )
            check_type(
                argname="argument include_authn_statement",
                value=include_authn_statement,
                expected_type=type_hints["include_authn_statement"],
            )
            check_type(
                argname="argument login_theme",
                value=login_theme,
                expected_type=type_hints["login_theme"],
            )
            check_type(
                argname="argument logout_service_post_binding_url",
                value=logout_service_post_binding_url,
                expected_type=type_hints["logout_service_post_binding_url"],
            )
            check_type(
                argname="argument logout_service_redirect_binding_url",
                value=logout_service_redirect_binding_url,
                expected_type=type_hints["logout_service_redirect_binding_url"],
            )
            check_type(
                argname="argument master_saml_processing_url",
                value=master_saml_processing_url,
                expected_type=type_hints["master_saml_processing_url"],
            )
            check_type(
                argname="argument name", value=name, expected_type=type_hints["name"]
            )
            check_type(
                argname="argument name_id_format",
                value=name_id_format,
                expected_type=type_hints["name_id_format"],
            )
            check_type(
                argname="argument root_url",
                value=root_url,
                expected_type=type_hints["root_url"],
            )
            check_type(
                argname="argument sign_assertions",
                value=sign_assertions,
                expected_type=type_hints["sign_assertions"],
            )
            check_type(
                argname="argument signature_algorithm",
                value=signature_algorithm,
                expected_type=type_hints["signature_algorithm"],
            )
            check_type(
                argname="argument signature_key_name",
                value=signature_key_name,
                expected_type=type_hints["signature_key_name"],
            )
            check_type(
                argname="argument sign_documents",
                value=sign_documents,
                expected_type=type_hints["sign_documents"],
            )
            check_type(
                argname="argument signing_certificate",
                value=signing_certificate,
                expected_type=type_hints["signing_certificate"],
            )
            check_type(
                argname="argument signing_private_key",
                value=signing_private_key,
                expected_type=type_hints["signing_private_key"],
            )
            check_type(
                argname="argument valid_redirect_uris",
                value=valid_redirect_uris,
                expected_type=type_hints["valid_redirect_uris"],
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
        if assertion_consumer_post_url is not None:
            self._values["assertion_consumer_post_url"] = assertion_consumer_post_url
        if assertion_consumer_redirect_url is not None:
            self._values[
                "assertion_consumer_redirect_url"
            ] = assertion_consumer_redirect_url
        if authentication_flow_binding_overrides is not None:
            self._values[
                "authentication_flow_binding_overrides"
            ] = authentication_flow_binding_overrides
        if base_url is not None:
            self._values["base_url"] = base_url
        if canonicalization_method is not None:
            self._values["canonicalization_method"] = canonicalization_method
        if client_signature_required is not None:
            self._values["client_signature_required"] = client_signature_required
        if description is not None:
            self._values["description"] = description
        if enabled is not None:
            self._values["enabled"] = enabled
        if encrypt_assertions is not None:
            self._values["encrypt_assertions"] = encrypt_assertions
        if encryption_certificate is not None:
            self._values["encryption_certificate"] = encryption_certificate
        if extra_config is not None:
            self._values["extra_config"] = extra_config
        if force_name_id_format is not None:
            self._values["force_name_id_format"] = force_name_id_format
        if force_post_binding is not None:
            self._values["force_post_binding"] = force_post_binding
        if front_channel_logout is not None:
            self._values["front_channel_logout"] = front_channel_logout
        if full_scope_allowed is not None:
            self._values["full_scope_allowed"] = full_scope_allowed
        if id is not None:
            self._values["id"] = id
        if idp_initiated_sso_relay_state is not None:
            self._values[
                "idp_initiated_sso_relay_state"
            ] = idp_initiated_sso_relay_state
        if idp_initiated_sso_url_name is not None:
            self._values["idp_initiated_sso_url_name"] = idp_initiated_sso_url_name
        if include_authn_statement is not None:
            self._values["include_authn_statement"] = include_authn_statement
        if login_theme is not None:
            self._values["login_theme"] = login_theme
        if logout_service_post_binding_url is not None:
            self._values[
                "logout_service_post_binding_url"
            ] = logout_service_post_binding_url
        if logout_service_redirect_binding_url is not None:
            self._values[
                "logout_service_redirect_binding_url"
            ] = logout_service_redirect_binding_url
        if master_saml_processing_url is not None:
            self._values["master_saml_processing_url"] = master_saml_processing_url
        if name is not None:
            self._values["name"] = name
        if name_id_format is not None:
            self._values["name_id_format"] = name_id_format
        if root_url is not None:
            self._values["root_url"] = root_url
        if sign_assertions is not None:
            self._values["sign_assertions"] = sign_assertions
        if signature_algorithm is not None:
            self._values["signature_algorithm"] = signature_algorithm
        if signature_key_name is not None:
            self._values["signature_key_name"] = signature_key_name
        if sign_documents is not None:
            self._values["sign_documents"] = sign_documents
        if signing_certificate is not None:
            self._values["signing_certificate"] = signing_certificate
        if signing_private_key is not None:
            self._values["signing_private_key"] = signing_private_key
        if valid_redirect_uris is not None:
            self._values["valid_redirect_uris"] = valid_redirect_uris

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
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#client_id SamlClient#client_id}."""
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def realm_id(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#realm_id SamlClient#realm_id}."""
        result = self._values.get("realm_id")
        assert result is not None, "Required property 'realm_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def assertion_consumer_post_url(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#assertion_consumer_post_url SamlClient#assertion_consumer_post_url}."""
        result = self._values.get("assertion_consumer_post_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def assertion_consumer_redirect_url(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#assertion_consumer_redirect_url SamlClient#assertion_consumer_redirect_url}."""
        result = self._values.get("assertion_consumer_redirect_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def authentication_flow_binding_overrides(
        self,
    ) -> typing.Optional[SamlClientAuthenticationFlowBindingOverrides]:
        """authentication_flow_binding_overrides block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#authentication_flow_binding_overrides SamlClient#authentication_flow_binding_overrides}
        """
        result = self._values.get("authentication_flow_binding_overrides")
        return typing.cast(
            typing.Optional[SamlClientAuthenticationFlowBindingOverrides], result
        )

    @builtins.property
    def base_url(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#base_url SamlClient#base_url}."""
        result = self._values.get("base_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def canonicalization_method(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#canonicalization_method SamlClient#canonicalization_method}."""
        result = self._values.get("canonicalization_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_signature_required(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#client_signature_required SamlClient#client_signature_required}."""
        result = self._values.get("client_signature_required")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#description SamlClient#description}."""
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#enabled SamlClient#enabled}."""
        result = self._values.get("enabled")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def encrypt_assertions(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#encrypt_assertions SamlClient#encrypt_assertions}."""
        result = self._values.get("encrypt_assertions")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def encryption_certificate(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#encryption_certificate SamlClient#encryption_certificate}."""
        result = self._values.get("encryption_certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extra_config(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#extra_config SamlClient#extra_config}."""
        result = self._values.get("extra_config")
        return typing.cast(
            typing.Optional[typing.Mapping[builtins.str, builtins.str]], result
        )

    @builtins.property
    def force_name_id_format(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#force_name_id_format SamlClient#force_name_id_format}."""
        result = self._values.get("force_name_id_format")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def force_post_binding(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#force_post_binding SamlClient#force_post_binding}."""
        result = self._values.get("force_post_binding")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def front_channel_logout(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#front_channel_logout SamlClient#front_channel_logout}."""
        result = self._values.get("front_channel_logout")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def full_scope_allowed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#full_scope_allowed SamlClient#full_scope_allowed}."""
        result = self._values.get("full_scope_allowed")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#id SamlClient#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def idp_initiated_sso_relay_state(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#idp_initiated_sso_relay_state SamlClient#idp_initiated_sso_relay_state}."""
        result = self._values.get("idp_initiated_sso_relay_state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def idp_initiated_sso_url_name(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#idp_initiated_sso_url_name SamlClient#idp_initiated_sso_url_name}."""
        result = self._values.get("idp_initiated_sso_url_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def include_authn_statement(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#include_authn_statement SamlClient#include_authn_statement}."""
        result = self._values.get("include_authn_statement")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def login_theme(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#login_theme SamlClient#login_theme}."""
        result = self._values.get("login_theme")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logout_service_post_binding_url(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#logout_service_post_binding_url SamlClient#logout_service_post_binding_url}."""
        result = self._values.get("logout_service_post_binding_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logout_service_redirect_binding_url(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#logout_service_redirect_binding_url SamlClient#logout_service_redirect_binding_url}."""
        result = self._values.get("logout_service_redirect_binding_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def master_saml_processing_url(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#master_saml_processing_url SamlClient#master_saml_processing_url}."""
        result = self._values.get("master_saml_processing_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#name SamlClient#name}."""
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name_id_format(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#name_id_format SamlClient#name_id_format}."""
        result = self._values.get("name_id_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def root_url(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#root_url SamlClient#root_url}."""
        result = self._values.get("root_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sign_assertions(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#sign_assertions SamlClient#sign_assertions}."""
        result = self._values.get("sign_assertions")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def signature_algorithm(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#signature_algorithm SamlClient#signature_algorithm}."""
        result = self._values.get("signature_algorithm")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def signature_key_name(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#signature_key_name SamlClient#signature_key_name}."""
        result = self._values.get("signature_key_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sign_documents(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#sign_documents SamlClient#sign_documents}."""
        result = self._values.get("sign_documents")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def signing_certificate(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#signing_certificate SamlClient#signing_certificate}."""
        result = self._values.get("signing_certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def signing_private_key(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#signing_private_key SamlClient#signing_private_key}."""
        result = self._values.get("signing_private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def valid_redirect_uris(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_client#valid_redirect_uris SamlClient#valid_redirect_uris}."""
        result = self._values.get("valid_redirect_uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SamlClientConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "SamlClient",
    "SamlClientAuthenticationFlowBindingOverrides",
    "SamlClientAuthenticationFlowBindingOverridesOutputReference",
    "SamlClientConfig",
]

publication.publish()


def _typecheckingstub__08b441a8e8453afef5418c091c41c9cecac62a5fddba783b8c676935ff028967(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    client_id: builtins.str,
    realm_id: builtins.str,
    assertion_consumer_post_url: typing.Optional[builtins.str] = None,
    assertion_consumer_redirect_url: typing.Optional[builtins.str] = None,
    authentication_flow_binding_overrides: typing.Optional[
        typing.Union[
            SamlClientAuthenticationFlowBindingOverrides,
            typing.Dict[builtins.str, typing.Any],
        ]
    ] = None,
    base_url: typing.Optional[builtins.str] = None,
    canonicalization_method: typing.Optional[builtins.str] = None,
    client_signature_required: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    description: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    encrypt_assertions: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    encryption_certificate: typing.Optional[builtins.str] = None,
    extra_config: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    force_name_id_format: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    force_post_binding: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    front_channel_logout: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    full_scope_allowed: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    id: typing.Optional[builtins.str] = None,
    idp_initiated_sso_relay_state: typing.Optional[builtins.str] = None,
    idp_initiated_sso_url_name: typing.Optional[builtins.str] = None,
    include_authn_statement: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    login_theme: typing.Optional[builtins.str] = None,
    logout_service_post_binding_url: typing.Optional[builtins.str] = None,
    logout_service_redirect_binding_url: typing.Optional[builtins.str] = None,
    master_saml_processing_url: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    name_id_format: typing.Optional[builtins.str] = None,
    root_url: typing.Optional[builtins.str] = None,
    sign_assertions: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    signature_algorithm: typing.Optional[builtins.str] = None,
    signature_key_name: typing.Optional[builtins.str] = None,
    sign_documents: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    signing_certificate: typing.Optional[builtins.str] = None,
    signing_private_key: typing.Optional[builtins.str] = None,
    valid_redirect_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
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


def _typecheckingstub__c9a60d05dd674ae3a183b347683413ab46c434e4c6aca5e4016e03c8f4e46aaa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9fa262e12e0090d8e57744604a189ed5e1fc9d5b707b513d4d5b3119bc10d70b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a490941bfd183a4c2eb320ce33ee100c4559e88f383f027aa55fe3059d87c255(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__07cf523b878d713abf3471c3b4ecd365cdcc7d8edd262b69a53277ee3deddfcc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7f78460700755961a5708febe5d4f01873945aa84e4b21f7e76844b4c8d84f91(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e4b56cd868ab1adf1b2809de841d16d3d0180df53b365c702de5e6cc70294325(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__09f19a076d07466889e04cc705b8c6708bc4f29ed2eb6011e4b554c8d480e109(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9d5b50bc3b5f6423b963c6eb3124d7fc4f4996a977506d3293faaf6f28143537(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c11001ebe587445436473ce0ae973c938c756a2d6fae55153734e7fe1444555c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e2f6982c1c20b03416de3ead06a3a96f2ccd88740ebb571f8df6a2a54b58e8df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c1ace4ef8115089a45a9a11c89cb76b2194776cbbd197219c7608a9e36036711(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__cd3825c540ac52fbb18b8493d16306f810c67d3f2e76903e7c4d7e8a7135940c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8b531389d6f19d8a40081f520022ef6daed02841b8a0e367024b5c4cbef058f6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6251b5561f302bbf2107682c9baaa7956ea606a1f669c14078d5bc595bfbd643(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3f9ee25d5e81d22eb3824129da4db68f94b919fb39a69b2956782b74f3124c27(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7b346d20bf78d3c135ead9d5dfdeef94b86636aaa87aef2ad1603d76fa030652(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0ba36e67f1dc80df02e5cc898070a40b8a0adae6135095623826523e4535568c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__aef12f14893495c68bab38573de50e7f510e68ab351e71beec8b1cda54657e1c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__bafecc3c41637f9f2ecd2879af3c728a1f67402074355de16f28731faf043d9a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__72fec20de99ec41b53524d5c4b072c7e1c7c4346ab562fbaae4df4846c0cc8c6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3665b2e7a1036f087f172d4226dd0a6d68cde386b1704f40f4176183ea8fe4d4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__2b51403fb4016a3f343d819fbd56540477153f8774c1aaca9546bbc8269000b1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e42116a6ff8814f6dbbdc624f46fb2cd6bfc6e75f4293b3535d1c49aab0788dc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6d80bf8b6cb82d707221fd8a072da4c9bece8add0ec113ff934b0870999214d7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__bb62271e007756755c8de4033f833e482f18a2fb4443f34e7fad53465a25abf8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8f43a551557b2d349ec2e77636a3896b71342aabaef882ec1c8e308039bd5e21(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__83f71e0a49caa40c2d53ecdd4058f402fa7e4776dcf506d3abf3d8419183d4af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__43f824ed8aa6a2741c1cdf8aae7ab7eab216e7847326df43f002016bbe5b61eb(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0a4d583f25571a9fa8a4105509bf6440bef34f20561020a3da7f24e79fb3cef1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f1b84bf6aec8dee7bfe24903b9c3fd2b025d157dc4132b48119266fa827e85c6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ef556c6f8a72dddf87bb6d8144040124fdcd73d4812184db6c8e426b351f4486(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__379b38c80fbef47385d40f262f14eb46b75fc155ee30717d82ff26cb773904fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8d0b5abff4d7115995616b6a1a20acd17ff9b9d30e66c687716a4c75240f3a80(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__739d871486a57e7c25b17857dc79a0fe460079f84fa869805db2c20d272e9387(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d5fe979020ade3c1f3e25a50954fb5513e3feadcc3461ffb1100733c68dafc23(
    *,
    browser_id: typing.Optional[builtins.str] = None,
    direct_grant_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__eaf20a85a25f3078945735d519344501708439cdc14aa5ec70e6c128d953ef0b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e11faf659a57824f03a9e5712e195e1f1cc8414f55eb9c6af0990d56845a7e54(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__77bd9eaea08b93f0dbfb9e7443fefae9daf1a47cd6d9395cadd7668482c3fdbe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d9a86ef32d7714a10ff90f23856309178a08c38806b5a7a466dae66e79ea086d(
    value: typing.Optional[SamlClientAuthenticationFlowBindingOverrides],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e2d862ca0df36108e3e5a88e83c5e9ec7559515446862b1b9bf212aa12c8601d(
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
    assertion_consumer_post_url: typing.Optional[builtins.str] = None,
    assertion_consumer_redirect_url: typing.Optional[builtins.str] = None,
    authentication_flow_binding_overrides: typing.Optional[
        typing.Union[
            SamlClientAuthenticationFlowBindingOverrides,
            typing.Dict[builtins.str, typing.Any],
        ]
    ] = None,
    base_url: typing.Optional[builtins.str] = None,
    canonicalization_method: typing.Optional[builtins.str] = None,
    client_signature_required: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    description: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    encrypt_assertions: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    encryption_certificate: typing.Optional[builtins.str] = None,
    extra_config: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    force_name_id_format: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    force_post_binding: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    front_channel_logout: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    full_scope_allowed: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    id: typing.Optional[builtins.str] = None,
    idp_initiated_sso_relay_state: typing.Optional[builtins.str] = None,
    idp_initiated_sso_url_name: typing.Optional[builtins.str] = None,
    include_authn_statement: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    login_theme: typing.Optional[builtins.str] = None,
    logout_service_post_binding_url: typing.Optional[builtins.str] = None,
    logout_service_redirect_binding_url: typing.Optional[builtins.str] = None,
    master_saml_processing_url: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    name_id_format: typing.Optional[builtins.str] = None,
    root_url: typing.Optional[builtins.str] = None,
    sign_assertions: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    signature_algorithm: typing.Optional[builtins.str] = None,
    signature_key_name: typing.Optional[builtins.str] = None,
    sign_documents: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    signing_certificate: typing.Optional[builtins.str] = None,
    signing_private_key: typing.Optional[builtins.str] = None,
    valid_redirect_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
