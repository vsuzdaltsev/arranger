"""
# `keycloak_saml_identity_provider`

Refer to the Terraform Registory for docs: [`keycloak_saml_identity_provider`](https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider).
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


class SamlIdentityProvider(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.samlIdentityProvider.SamlIdentityProvider",
):
    """Represents a {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider keycloak_saml_identity_provider}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        alias: builtins.str,
        entity_id: builtins.str,
        realm: builtins.str,
        single_sign_on_service_url: builtins.str,
        add_read_token_role_on_create: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        authenticate_by_default: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        authn_context_class_refs: typing.Optional[typing.Sequence[builtins.str]] = None,
        authn_context_comparison_type: typing.Optional[builtins.str] = None,
        authn_context_decl_refs: typing.Optional[typing.Sequence[builtins.str]] = None,
        backchannel_supported: typing.Optional[
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
        force_authn: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        gui_order: typing.Optional[builtins.str] = None,
        hide_on_login_page: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        id: typing.Optional[builtins.str] = None,
        link_only: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        login_hint: typing.Optional[builtins.str] = None,
        name_id_policy_format: typing.Optional[builtins.str] = None,
        post_binding_authn_request: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        post_binding_logout: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        post_binding_response: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        post_broker_login_flow_alias: typing.Optional[builtins.str] = None,
        principal_attribute: typing.Optional[builtins.str] = None,
        principal_type: typing.Optional[builtins.str] = None,
        provider_id: typing.Optional[builtins.str] = None,
        signature_algorithm: typing.Optional[builtins.str] = None,
        signing_certificate: typing.Optional[builtins.str] = None,
        single_logout_service_url: typing.Optional[builtins.str] = None,
        store_token: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        sync_mode: typing.Optional[builtins.str] = None,
        trust_email: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        validate_signature: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        want_assertions_encrypted: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        want_assertions_signed: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        xml_sign_key_info_key_name_transformer: typing.Optional[builtins.str] = None,
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
        """Create a new {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider keycloak_saml_identity_provider} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param alias: The alias uniquely identifies an identity provider and it is also used to build the redirect uri. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#alias SamlIdentityProvider#alias}
        :param entity_id: The Entity ID that will be used to uniquely identify this SAML Service Provider. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#entity_id SamlIdentityProvider#entity_id}
        :param realm: Realm Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#realm SamlIdentityProvider#realm}
        :param single_sign_on_service_url: SSO Logout URL. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#single_sign_on_service_url SamlIdentityProvider#single_sign_on_service_url}
        :param add_read_token_role_on_create: Enable/disable if new users can read any stored tokens. This assigns the broker.read-token role. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#add_read_token_role_on_create SamlIdentityProvider#add_read_token_role_on_create}
        :param authenticate_by_default: Enable/disable authenticate users by default. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#authenticate_by_default SamlIdentityProvider#authenticate_by_default}
        :param authn_context_class_refs: AuthnContext ClassRefs. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#authn_context_class_refs SamlIdentityProvider#authn_context_class_refs}
        :param authn_context_comparison_type: AuthnContext Comparison. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#authn_context_comparison_type SamlIdentityProvider#authn_context_comparison_type}
        :param authn_context_decl_refs: AuthnContext DeclRefs. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#authn_context_decl_refs SamlIdentityProvider#authn_context_decl_refs}
        :param backchannel_supported: Does the external IDP support backchannel logout? Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#backchannel_supported SamlIdentityProvider#backchannel_supported}
        :param display_name: Friendly name for Identity Providers. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#display_name SamlIdentityProvider#display_name}
        :param enabled: Enable/disable this identity provider. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#enabled SamlIdentityProvider#enabled}
        :param extra_config: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#extra_config SamlIdentityProvider#extra_config}.
        :param first_broker_login_flow_alias: Alias of authentication flow, which is triggered after first login with this identity provider. Term 'First Login' means that there is not yet existing Keycloak account linked with the authenticated identity provider account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#first_broker_login_flow_alias SamlIdentityProvider#first_broker_login_flow_alias}
        :param force_authn: Require Force Authn. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#force_authn SamlIdentityProvider#force_authn}
        :param gui_order: GUI Order. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#gui_order SamlIdentityProvider#gui_order}
        :param hide_on_login_page: Hide On Login Page. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#hide_on_login_page SamlIdentityProvider#hide_on_login_page}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#id SamlIdentityProvider#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param link_only: If true, users cannot log in through this provider. They can only link to this provider. This is useful if you don't want to allow login from the provider, but want to integrate with a provider Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#link_only SamlIdentityProvider#link_only}
        :param login_hint: Login Hint. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#login_hint SamlIdentityProvider#login_hint}
        :param name_id_policy_format: Name ID Policy Format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#name_id_policy_format SamlIdentityProvider#name_id_policy_format}
        :param post_binding_authn_request: Post Binding Authn Request. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#post_binding_authn_request SamlIdentityProvider#post_binding_authn_request}
        :param post_binding_logout: Post Binding Logout. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#post_binding_logout SamlIdentityProvider#post_binding_logout}
        :param post_binding_response: Post Binding Response. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#post_binding_response SamlIdentityProvider#post_binding_response}
        :param post_broker_login_flow_alias: Alias of authentication flow, which is triggered after each login with this identity provider. Useful if you want additional verification of each user authenticated with this identity provider (for example OTP). Leave this empty if you don't want any additional authenticators to be triggered after login with this identity provider. Also note, that authenticator implementations must assume that user is already set in ClientSession as identity provider already set it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#post_broker_login_flow_alias SamlIdentityProvider#post_broker_login_flow_alias}
        :param principal_attribute: Principal Attribute. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#principal_attribute SamlIdentityProvider#principal_attribute}
        :param principal_type: Principal Type. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#principal_type SamlIdentityProvider#principal_type}
        :param provider_id: provider id, is always saml, unless you have a custom implementation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#provider_id SamlIdentityProvider#provider_id}
        :param signature_algorithm: Signing Algorithm. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#signature_algorithm SamlIdentityProvider#signature_algorithm}
        :param signing_certificate: Signing Certificate. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#signing_certificate SamlIdentityProvider#signing_certificate}
        :param single_logout_service_url: Logout URL. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#single_logout_service_url SamlIdentityProvider#single_logout_service_url}
        :param store_token: Enable/disable if tokens must be stored after authenticating users. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#store_token SamlIdentityProvider#store_token}
        :param sync_mode: Sync Mode. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#sync_mode SamlIdentityProvider#sync_mode}
        :param trust_email: If enabled then email provided by this provider is not verified even if verification is enabled for the realm. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#trust_email SamlIdentityProvider#trust_email}
        :param validate_signature: Enable/disable signature validation of SAML responses. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#validate_signature SamlIdentityProvider#validate_signature}
        :param want_assertions_encrypted: Want Assertions Encrypted. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#want_assertions_encrypted SamlIdentityProvider#want_assertions_encrypted}
        :param want_assertions_signed: Want Assertions Signed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#want_assertions_signed SamlIdentityProvider#want_assertions_signed}
        :param xml_sign_key_info_key_name_transformer: Sign Key Transformer. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#xml_sign_key_info_key_name_transformer SamlIdentityProvider#xml_sign_key_info_key_name_transformer}
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
                _typecheckingstub__97f8a966aad9686073076b11caa4fdf9c68447ecb584a458c1704ac66c9d4453
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(
                argname="argument id_", value=id_, expected_type=type_hints["id_"]
            )
        config = SamlIdentityProviderConfig(
            alias=alias,
            entity_id=entity_id,
            realm=realm,
            single_sign_on_service_url=single_sign_on_service_url,
            add_read_token_role_on_create=add_read_token_role_on_create,
            authenticate_by_default=authenticate_by_default,
            authn_context_class_refs=authn_context_class_refs,
            authn_context_comparison_type=authn_context_comparison_type,
            authn_context_decl_refs=authn_context_decl_refs,
            backchannel_supported=backchannel_supported,
            display_name=display_name,
            enabled=enabled,
            extra_config=extra_config,
            first_broker_login_flow_alias=first_broker_login_flow_alias,
            force_authn=force_authn,
            gui_order=gui_order,
            hide_on_login_page=hide_on_login_page,
            id=id,
            link_only=link_only,
            login_hint=login_hint,
            name_id_policy_format=name_id_policy_format,
            post_binding_authn_request=post_binding_authn_request,
            post_binding_logout=post_binding_logout,
            post_binding_response=post_binding_response,
            post_broker_login_flow_alias=post_broker_login_flow_alias,
            principal_attribute=principal_attribute,
            principal_type=principal_type,
            provider_id=provider_id,
            signature_algorithm=signature_algorithm,
            signing_certificate=signing_certificate,
            single_logout_service_url=single_logout_service_url,
            store_token=store_token,
            sync_mode=sync_mode,
            trust_email=trust_email,
            validate_signature=validate_signature,
            want_assertions_encrypted=want_assertions_encrypted,
            want_assertions_signed=want_assertions_signed,
            xml_sign_key_info_key_name_transformer=xml_sign_key_info_key_name_transformer,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetAddReadTokenRoleOnCreate")
    def reset_add_read_token_role_on_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddReadTokenRoleOnCreate", []))

    @jsii.member(jsii_name="resetAuthenticateByDefault")
    def reset_authenticate_by_default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthenticateByDefault", []))

    @jsii.member(jsii_name="resetAuthnContextClassRefs")
    def reset_authn_context_class_refs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthnContextClassRefs", []))

    @jsii.member(jsii_name="resetAuthnContextComparisonType")
    def reset_authn_context_comparison_type(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetAuthnContextComparisonType", [])
        )

    @jsii.member(jsii_name="resetAuthnContextDeclRefs")
    def reset_authn_context_decl_refs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthnContextDeclRefs", []))

    @jsii.member(jsii_name="resetBackchannelSupported")
    def reset_backchannel_supported(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackchannelSupported", []))

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

    @jsii.member(jsii_name="resetForceAuthn")
    def reset_force_authn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceAuthn", []))

    @jsii.member(jsii_name="resetGuiOrder")
    def reset_gui_order(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGuiOrder", []))

    @jsii.member(jsii_name="resetHideOnLoginPage")
    def reset_hide_on_login_page(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHideOnLoginPage", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLinkOnly")
    def reset_link_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinkOnly", []))

    @jsii.member(jsii_name="resetLoginHint")
    def reset_login_hint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoginHint", []))

    @jsii.member(jsii_name="resetNameIdPolicyFormat")
    def reset_name_id_policy_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNameIdPolicyFormat", []))

    @jsii.member(jsii_name="resetPostBindingAuthnRequest")
    def reset_post_binding_authn_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPostBindingAuthnRequest", []))

    @jsii.member(jsii_name="resetPostBindingLogout")
    def reset_post_binding_logout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPostBindingLogout", []))

    @jsii.member(jsii_name="resetPostBindingResponse")
    def reset_post_binding_response(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPostBindingResponse", []))

    @jsii.member(jsii_name="resetPostBrokerLoginFlowAlias")
    def reset_post_broker_login_flow_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPostBrokerLoginFlowAlias", []))

    @jsii.member(jsii_name="resetPrincipalAttribute")
    def reset_principal_attribute(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrincipalAttribute", []))

    @jsii.member(jsii_name="resetPrincipalType")
    def reset_principal_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrincipalType", []))

    @jsii.member(jsii_name="resetProviderId")
    def reset_provider_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProviderId", []))

    @jsii.member(jsii_name="resetSignatureAlgorithm")
    def reset_signature_algorithm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSignatureAlgorithm", []))

    @jsii.member(jsii_name="resetSigningCertificate")
    def reset_signing_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSigningCertificate", []))

    @jsii.member(jsii_name="resetSingleLogoutServiceUrl")
    def reset_single_logout_service_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSingleLogoutServiceUrl", []))

    @jsii.member(jsii_name="resetStoreToken")
    def reset_store_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStoreToken", []))

    @jsii.member(jsii_name="resetSyncMode")
    def reset_sync_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSyncMode", []))

    @jsii.member(jsii_name="resetTrustEmail")
    def reset_trust_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrustEmail", []))

    @jsii.member(jsii_name="resetValidateSignature")
    def reset_validate_signature(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValidateSignature", []))

    @jsii.member(jsii_name="resetWantAssertionsEncrypted")
    def reset_want_assertions_encrypted(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWantAssertionsEncrypted", []))

    @jsii.member(jsii_name="resetWantAssertionsSigned")
    def reset_want_assertions_signed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWantAssertionsSigned", []))

    @jsii.member(jsii_name="resetXmlSignKeyInfoKeyNameTransformer")
    def reset_xml_sign_key_info_key_name_transformer(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetXmlSignKeyInfoKeyNameTransformer", [])
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
    @jsii.member(jsii_name="internalId")
    def internal_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "internalId"))

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
    @jsii.member(jsii_name="authnContextClassRefsInput")
    def authn_context_class_refs_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]],
            jsii.get(self, "authnContextClassRefsInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="authnContextComparisonTypeInput")
    def authn_context_comparison_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "authnContextComparisonTypeInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="authnContextDeclRefsInput")
    def authn_context_decl_refs_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]],
            jsii.get(self, "authnContextDeclRefsInput"),
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
    @jsii.member(jsii_name="entityIdInput")
    def entity_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "entityIdInput")
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
    @jsii.member(jsii_name="forceAuthnInput")
    def force_authn_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "forceAuthnInput"),
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
    @jsii.member(jsii_name="nameIdPolicyFormatInput")
    def name_id_policy_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "nameIdPolicyFormatInput")
        )

    @builtins.property
    @jsii.member(jsii_name="postBindingAuthnRequestInput")
    def post_binding_authn_request_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "postBindingAuthnRequestInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="postBindingLogoutInput")
    def post_binding_logout_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "postBindingLogoutInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="postBindingResponseInput")
    def post_binding_response_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "postBindingResponseInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="postBrokerLoginFlowAliasInput")
    def post_broker_login_flow_alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "postBrokerLoginFlowAliasInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="principalAttributeInput")
    def principal_attribute_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "principalAttributeInput")
        )

    @builtins.property
    @jsii.member(jsii_name="principalTypeInput")
    def principal_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "principalTypeInput")
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
    @jsii.member(jsii_name="signatureAlgorithmInput")
    def signature_algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "signatureAlgorithmInput")
        )

    @builtins.property
    @jsii.member(jsii_name="signingCertificateInput")
    def signing_certificate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "signingCertificateInput")
        )

    @builtins.property
    @jsii.member(jsii_name="singleLogoutServiceUrlInput")
    def single_logout_service_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "singleLogoutServiceUrlInput")
        )

    @builtins.property
    @jsii.member(jsii_name="singleSignOnServiceUrlInput")
    def single_sign_on_service_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "singleSignOnServiceUrlInput")
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
    @jsii.member(jsii_name="validateSignatureInput")
    def validate_signature_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "validateSignatureInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="wantAssertionsEncryptedInput")
    def want_assertions_encrypted_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "wantAssertionsEncryptedInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="wantAssertionsSignedInput")
    def want_assertions_signed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "wantAssertionsSignedInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="xmlSignKeyInfoKeyNameTransformerInput")
    def xml_sign_key_info_key_name_transformer_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "xmlSignKeyInfoKeyNameTransformerInput"),
        )

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
                _typecheckingstub__8b9dafb05ffc14c0dc3a12257f6966341fa469124958dbb9bdc96071088c8e22
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
                _typecheckingstub__f46b4774337e91ffb8ef2d33f089cdb1dc204c9bc61e7534b258f7204559587b
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
                _typecheckingstub__58feaf94ecb5b71c77b67d75c9a0ea705263ae6d2cd43d57913407c40d09a9d6
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "authenticateByDefault", value)

    @builtins.property
    @jsii.member(jsii_name="authnContextClassRefs")
    def authn_context_class_refs(self) -> typing.List[builtins.str]:
        return typing.cast(
            typing.List[builtins.str], jsii.get(self, "authnContextClassRefs")
        )

    @authn_context_class_refs.setter
    def authn_context_class_refs(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__ec9d82d8ffec731cb48903488f938bffa8f28c8831412edae28cd0279b8cbaee
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "authnContextClassRefs", value)

    @builtins.property
    @jsii.member(jsii_name="authnContextComparisonType")
    def authn_context_comparison_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authnContextComparisonType"))

    @authn_context_comparison_type.setter
    def authn_context_comparison_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__c35b56a3a77a078121b6ca5b7ea0c73aff72036d7702c955f538fe95e241c63e
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "authnContextComparisonType", value)

    @builtins.property
    @jsii.member(jsii_name="authnContextDeclRefs")
    def authn_context_decl_refs(self) -> typing.List[builtins.str]:
        return typing.cast(
            typing.List[builtins.str], jsii.get(self, "authnContextDeclRefs")
        )

    @authn_context_decl_refs.setter
    def authn_context_decl_refs(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__447f91590465a25c451ad141b82c7ffd78c842f14219002b82b7a5755a48cfe1
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "authnContextDeclRefs", value)

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
                _typecheckingstub__eb06edc7fedd9792b95c93c71c9c354fd62cbc0dd81af085140bbd52156516d0
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "backchannelSupported", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__49e142702873998d6c95547adcf1e8b133c583c0ebd51da0b88eccbd7e500c7e
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
                _typecheckingstub__8876bf5e9c676555d79ad5a6ffc1d196eb731d43413b9412d3915c25ffbca083
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="entityId")
    def entity_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "entityId"))

    @entity_id.setter
    def entity_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__ab30b114c0cd529b50f46ae5cdd94b744e3c8c0c060912064402b1f688e71436
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "entityId", value)

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
                _typecheckingstub__8c1e193074c83a719eb043cabef170f44a2908b565b69e586317044ed455b86a
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
                _typecheckingstub__65d18a3d71e07da6abaa1b8d477dbfb6f7c98746c02f0e8d30f353acf71fa35d
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "firstBrokerLoginFlowAlias", value)

    @builtins.property
    @jsii.member(jsii_name="forceAuthn")
    def force_authn(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "forceAuthn"),
        )

    @force_authn.setter
    def force_authn(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a2391d592852161c3215960245fd02ebbbf0e69161d00177d5306df7d48f120f
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "forceAuthn", value)

    @builtins.property
    @jsii.member(jsii_name="guiOrder")
    def gui_order(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "guiOrder"))

    @gui_order.setter
    def gui_order(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__3b4bde417847feb92114f89996958af8ee972359d1b525879c3bc206c36e0955
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
                _typecheckingstub__7cd7b3ec6ee3cd2e283594ed946070e580bf1a513921ccc2ee5881121bb61e33
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
                _typecheckingstub__444a70224691c022134631746a8c5ce4709c0e391a80cc60a893915d6471ff8c
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
                _typecheckingstub__d624f8d00dc1e8fb08f257148de8672a2c533f943a9a7ab755c9b56f01a628c9
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
                _typecheckingstub__f9ac548534be4312c30056a85926f9983ef338b8ce188ea97af4b0279ad19f18
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "loginHint", value)

    @builtins.property
    @jsii.member(jsii_name="nameIdPolicyFormat")
    def name_id_policy_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nameIdPolicyFormat"))

    @name_id_policy_format.setter
    def name_id_policy_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__ca2fd135009815a812338fbba84d200875254ba2aee440c2e2799aa36eb42448
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "nameIdPolicyFormat", value)

    @builtins.property
    @jsii.member(jsii_name="postBindingAuthnRequest")
    def post_binding_authn_request(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "postBindingAuthnRequest"),
        )

    @post_binding_authn_request.setter
    def post_binding_authn_request(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__e27ec219a10bd3d8cb66ec894971a05984d79401310ca539c85249cdb14f0ebc
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "postBindingAuthnRequest", value)

    @builtins.property
    @jsii.member(jsii_name="postBindingLogout")
    def post_binding_logout(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "postBindingLogout"),
        )

    @post_binding_logout.setter
    def post_binding_logout(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__df295788cf89133e3c9b2009496859a94fd8343615b189348cca1ff82d982e3f
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "postBindingLogout", value)

    @builtins.property
    @jsii.member(jsii_name="postBindingResponse")
    def post_binding_response(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "postBindingResponse"),
        )

    @post_binding_response.setter
    def post_binding_response(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__246514c1d14421f6c68259b2b7c43bc194ae63056afc9d09756bfcf1069b0e00
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "postBindingResponse", value)

    @builtins.property
    @jsii.member(jsii_name="postBrokerLoginFlowAlias")
    def post_broker_login_flow_alias(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "postBrokerLoginFlowAlias"))

    @post_broker_login_flow_alias.setter
    def post_broker_login_flow_alias(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__69251b1eb8798051ebd49bcc4d11e9ed172aeec4324e897236a6a732e281455e
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "postBrokerLoginFlowAlias", value)

    @builtins.property
    @jsii.member(jsii_name="principalAttribute")
    def principal_attribute(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "principalAttribute"))

    @principal_attribute.setter
    def principal_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__91dd594c3cdee7df03c9b09576d2fe5ee93963847d0c94ab899e9effd82bfc47
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "principalAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="principalType")
    def principal_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "principalType"))

    @principal_type.setter
    def principal_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__4e7f935f60f3f26a35dd8a59f2e0e0bf15393261f0640481b0bbffc97775a4f6
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "principalType", value)

    @builtins.property
    @jsii.member(jsii_name="providerId")
    def provider_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "providerId"))

    @provider_id.setter
    def provider_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__079138c8d22e7d610a45d5bc66f1d9e7382243970f6ed3a1e455aa4360c84358
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
                _typecheckingstub__d981cd37f273d10345827ca491b3fcdb53a10861d5d9052b71bf5f295223e4a0
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "realm", value)

    @builtins.property
    @jsii.member(jsii_name="signatureAlgorithm")
    def signature_algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signatureAlgorithm"))

    @signature_algorithm.setter
    def signature_algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__070c851a8e1a16e37df9f9159874ff2e793fa481aa4692126ff205b9eef13791
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "signatureAlgorithm", value)

    @builtins.property
    @jsii.member(jsii_name="signingCertificate")
    def signing_certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signingCertificate"))

    @signing_certificate.setter
    def signing_certificate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__ff2385671569d7c5e13de1aedc158d77bf3ff7f6ee9aec8cbb41211cf5dd80c1
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "signingCertificate", value)

    @builtins.property
    @jsii.member(jsii_name="singleLogoutServiceUrl")
    def single_logout_service_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "singleLogoutServiceUrl"))

    @single_logout_service_url.setter
    def single_logout_service_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__cbe82b67e93e1f99c2f572b2f4e9010536d1e81578573a98a1e68aaef108f489
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "singleLogoutServiceUrl", value)

    @builtins.property
    @jsii.member(jsii_name="singleSignOnServiceUrl")
    def single_sign_on_service_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "singleSignOnServiceUrl"))

    @single_sign_on_service_url.setter
    def single_sign_on_service_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__fed1c50c8cd596877d39d5debd39edc060fd27b4c493164586571a1f66359c71
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "singleSignOnServiceUrl", value)

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
                _typecheckingstub__616ed3af8ccff26b36cce5d290ecc790a833e9e596fcd78889b1cabd535817b2
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
                _typecheckingstub__04ab6a495606d7575a07e02ec662eeea4689b2f385308e42c0083e9d0385414f
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
                _typecheckingstub__d39af30df9f8af5009aab94e890dd2f92e47297f40ac05ca89df5465f4be17a7
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "trustEmail", value)

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
                _typecheckingstub__36f642006067e0d77b87edc72ad7f80a41b36aed07517fc533f2c6439b4b7c5f
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "validateSignature", value)

    @builtins.property
    @jsii.member(jsii_name="wantAssertionsEncrypted")
    def want_assertions_encrypted(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "wantAssertionsEncrypted"),
        )

    @want_assertions_encrypted.setter
    def want_assertions_encrypted(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__9a27e6a7ec792cd134c5598b3686ba178a972b7f1b9c8b47a8b46cba3657527d
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "wantAssertionsEncrypted", value)

    @builtins.property
    @jsii.member(jsii_name="wantAssertionsSigned")
    def want_assertions_signed(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "wantAssertionsSigned"),
        )

    @want_assertions_signed.setter
    def want_assertions_signed(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__49e018f8ed659d60ee172f532c50805ff942e42917a5a1cedcb83ab8230c3625
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "wantAssertionsSigned", value)

    @builtins.property
    @jsii.member(jsii_name="xmlSignKeyInfoKeyNameTransformer")
    def xml_sign_key_info_key_name_transformer(self) -> builtins.str:
        return typing.cast(
            builtins.str, jsii.get(self, "xmlSignKeyInfoKeyNameTransformer")
        )

    @xml_sign_key_info_key_name_transformer.setter
    def xml_sign_key_info_key_name_transformer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__916318ba031d47d05013df1f6018e8520850c049062c981433e832ca871e5f82
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "xmlSignKeyInfoKeyNameTransformer", value)


@jsii.data_type(
    jsii_type="keycloak.samlIdentityProvider.SamlIdentityProviderConfig",
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
        "entity_id": "entityId",
        "realm": "realm",
        "single_sign_on_service_url": "singleSignOnServiceUrl",
        "add_read_token_role_on_create": "addReadTokenRoleOnCreate",
        "authenticate_by_default": "authenticateByDefault",
        "authn_context_class_refs": "authnContextClassRefs",
        "authn_context_comparison_type": "authnContextComparisonType",
        "authn_context_decl_refs": "authnContextDeclRefs",
        "backchannel_supported": "backchannelSupported",
        "display_name": "displayName",
        "enabled": "enabled",
        "extra_config": "extraConfig",
        "first_broker_login_flow_alias": "firstBrokerLoginFlowAlias",
        "force_authn": "forceAuthn",
        "gui_order": "guiOrder",
        "hide_on_login_page": "hideOnLoginPage",
        "id": "id",
        "link_only": "linkOnly",
        "login_hint": "loginHint",
        "name_id_policy_format": "nameIdPolicyFormat",
        "post_binding_authn_request": "postBindingAuthnRequest",
        "post_binding_logout": "postBindingLogout",
        "post_binding_response": "postBindingResponse",
        "post_broker_login_flow_alias": "postBrokerLoginFlowAlias",
        "principal_attribute": "principalAttribute",
        "principal_type": "principalType",
        "provider_id": "providerId",
        "signature_algorithm": "signatureAlgorithm",
        "signing_certificate": "signingCertificate",
        "single_logout_service_url": "singleLogoutServiceUrl",
        "store_token": "storeToken",
        "sync_mode": "syncMode",
        "trust_email": "trustEmail",
        "validate_signature": "validateSignature",
        "want_assertions_encrypted": "wantAssertionsEncrypted",
        "want_assertions_signed": "wantAssertionsSigned",
        "xml_sign_key_info_key_name_transformer": "xmlSignKeyInfoKeyNameTransformer",
    },
)
class SamlIdentityProviderConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        entity_id: builtins.str,
        realm: builtins.str,
        single_sign_on_service_url: builtins.str,
        add_read_token_role_on_create: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        authenticate_by_default: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        authn_context_class_refs: typing.Optional[typing.Sequence[builtins.str]] = None,
        authn_context_comparison_type: typing.Optional[builtins.str] = None,
        authn_context_decl_refs: typing.Optional[typing.Sequence[builtins.str]] = None,
        backchannel_supported: typing.Optional[
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
        force_authn: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        gui_order: typing.Optional[builtins.str] = None,
        hide_on_login_page: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        id: typing.Optional[builtins.str] = None,
        link_only: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        login_hint: typing.Optional[builtins.str] = None,
        name_id_policy_format: typing.Optional[builtins.str] = None,
        post_binding_authn_request: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        post_binding_logout: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        post_binding_response: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        post_broker_login_flow_alias: typing.Optional[builtins.str] = None,
        principal_attribute: typing.Optional[builtins.str] = None,
        principal_type: typing.Optional[builtins.str] = None,
        provider_id: typing.Optional[builtins.str] = None,
        signature_algorithm: typing.Optional[builtins.str] = None,
        signing_certificate: typing.Optional[builtins.str] = None,
        single_logout_service_url: typing.Optional[builtins.str] = None,
        store_token: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        sync_mode: typing.Optional[builtins.str] = None,
        trust_email: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        validate_signature: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        want_assertions_encrypted: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        want_assertions_signed: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        xml_sign_key_info_key_name_transformer: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param connection:
        :param count:
        :param depends_on:
        :param for_each:
        :param lifecycle:
        :param provider:
        :param provisioners:
        :param alias: The alias uniquely identifies an identity provider and it is also used to build the redirect uri. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#alias SamlIdentityProvider#alias}
        :param entity_id: The Entity ID that will be used to uniquely identify this SAML Service Provider. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#entity_id SamlIdentityProvider#entity_id}
        :param realm: Realm Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#realm SamlIdentityProvider#realm}
        :param single_sign_on_service_url: SSO Logout URL. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#single_sign_on_service_url SamlIdentityProvider#single_sign_on_service_url}
        :param add_read_token_role_on_create: Enable/disable if new users can read any stored tokens. This assigns the broker.read-token role. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#add_read_token_role_on_create SamlIdentityProvider#add_read_token_role_on_create}
        :param authenticate_by_default: Enable/disable authenticate users by default. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#authenticate_by_default SamlIdentityProvider#authenticate_by_default}
        :param authn_context_class_refs: AuthnContext ClassRefs. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#authn_context_class_refs SamlIdentityProvider#authn_context_class_refs}
        :param authn_context_comparison_type: AuthnContext Comparison. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#authn_context_comparison_type SamlIdentityProvider#authn_context_comparison_type}
        :param authn_context_decl_refs: AuthnContext DeclRefs. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#authn_context_decl_refs SamlIdentityProvider#authn_context_decl_refs}
        :param backchannel_supported: Does the external IDP support backchannel logout? Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#backchannel_supported SamlIdentityProvider#backchannel_supported}
        :param display_name: Friendly name for Identity Providers. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#display_name SamlIdentityProvider#display_name}
        :param enabled: Enable/disable this identity provider. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#enabled SamlIdentityProvider#enabled}
        :param extra_config: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#extra_config SamlIdentityProvider#extra_config}.
        :param first_broker_login_flow_alias: Alias of authentication flow, which is triggered after first login with this identity provider. Term 'First Login' means that there is not yet existing Keycloak account linked with the authenticated identity provider account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#first_broker_login_flow_alias SamlIdentityProvider#first_broker_login_flow_alias}
        :param force_authn: Require Force Authn. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#force_authn SamlIdentityProvider#force_authn}
        :param gui_order: GUI Order. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#gui_order SamlIdentityProvider#gui_order}
        :param hide_on_login_page: Hide On Login Page. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#hide_on_login_page SamlIdentityProvider#hide_on_login_page}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#id SamlIdentityProvider#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param link_only: If true, users cannot log in through this provider. They can only link to this provider. This is useful if you don't want to allow login from the provider, but want to integrate with a provider Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#link_only SamlIdentityProvider#link_only}
        :param login_hint: Login Hint. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#login_hint SamlIdentityProvider#login_hint}
        :param name_id_policy_format: Name ID Policy Format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#name_id_policy_format SamlIdentityProvider#name_id_policy_format}
        :param post_binding_authn_request: Post Binding Authn Request. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#post_binding_authn_request SamlIdentityProvider#post_binding_authn_request}
        :param post_binding_logout: Post Binding Logout. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#post_binding_logout SamlIdentityProvider#post_binding_logout}
        :param post_binding_response: Post Binding Response. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#post_binding_response SamlIdentityProvider#post_binding_response}
        :param post_broker_login_flow_alias: Alias of authentication flow, which is triggered after each login with this identity provider. Useful if you want additional verification of each user authenticated with this identity provider (for example OTP). Leave this empty if you don't want any additional authenticators to be triggered after login with this identity provider. Also note, that authenticator implementations must assume that user is already set in ClientSession as identity provider already set it. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#post_broker_login_flow_alias SamlIdentityProvider#post_broker_login_flow_alias}
        :param principal_attribute: Principal Attribute. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#principal_attribute SamlIdentityProvider#principal_attribute}
        :param principal_type: Principal Type. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#principal_type SamlIdentityProvider#principal_type}
        :param provider_id: provider id, is always saml, unless you have a custom implementation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#provider_id SamlIdentityProvider#provider_id}
        :param signature_algorithm: Signing Algorithm. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#signature_algorithm SamlIdentityProvider#signature_algorithm}
        :param signing_certificate: Signing Certificate. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#signing_certificate SamlIdentityProvider#signing_certificate}
        :param single_logout_service_url: Logout URL. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#single_logout_service_url SamlIdentityProvider#single_logout_service_url}
        :param store_token: Enable/disable if tokens must be stored after authenticating users. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#store_token SamlIdentityProvider#store_token}
        :param sync_mode: Sync Mode. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#sync_mode SamlIdentityProvider#sync_mode}
        :param trust_email: If enabled then email provided by this provider is not verified even if verification is enabled for the realm. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#trust_email SamlIdentityProvider#trust_email}
        :param validate_signature: Enable/disable signature validation of SAML responses. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#validate_signature SamlIdentityProvider#validate_signature}
        :param want_assertions_encrypted: Want Assertions Encrypted. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#want_assertions_encrypted SamlIdentityProvider#want_assertions_encrypted}
        :param want_assertions_signed: Want Assertions Signed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#want_assertions_signed SamlIdentityProvider#want_assertions_signed}
        :param xml_sign_key_info_key_name_transformer: Sign Key Transformer. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#xml_sign_key_info_key_name_transformer SamlIdentityProvider#xml_sign_key_info_key_name_transformer}
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__6e6cb4ad1d88681d502c306000d9ee621d807f15950e89377353d17acd13c19b
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
                argname="argument entity_id",
                value=entity_id,
                expected_type=type_hints["entity_id"],
            )
            check_type(
                argname="argument realm", value=realm, expected_type=type_hints["realm"]
            )
            check_type(
                argname="argument single_sign_on_service_url",
                value=single_sign_on_service_url,
                expected_type=type_hints["single_sign_on_service_url"],
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
                argname="argument authn_context_class_refs",
                value=authn_context_class_refs,
                expected_type=type_hints["authn_context_class_refs"],
            )
            check_type(
                argname="argument authn_context_comparison_type",
                value=authn_context_comparison_type,
                expected_type=type_hints["authn_context_comparison_type"],
            )
            check_type(
                argname="argument authn_context_decl_refs",
                value=authn_context_decl_refs,
                expected_type=type_hints["authn_context_decl_refs"],
            )
            check_type(
                argname="argument backchannel_supported",
                value=backchannel_supported,
                expected_type=type_hints["backchannel_supported"],
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
                argname="argument force_authn",
                value=force_authn,
                expected_type=type_hints["force_authn"],
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
                argname="argument name_id_policy_format",
                value=name_id_policy_format,
                expected_type=type_hints["name_id_policy_format"],
            )
            check_type(
                argname="argument post_binding_authn_request",
                value=post_binding_authn_request,
                expected_type=type_hints["post_binding_authn_request"],
            )
            check_type(
                argname="argument post_binding_logout",
                value=post_binding_logout,
                expected_type=type_hints["post_binding_logout"],
            )
            check_type(
                argname="argument post_binding_response",
                value=post_binding_response,
                expected_type=type_hints["post_binding_response"],
            )
            check_type(
                argname="argument post_broker_login_flow_alias",
                value=post_broker_login_flow_alias,
                expected_type=type_hints["post_broker_login_flow_alias"],
            )
            check_type(
                argname="argument principal_attribute",
                value=principal_attribute,
                expected_type=type_hints["principal_attribute"],
            )
            check_type(
                argname="argument principal_type",
                value=principal_type,
                expected_type=type_hints["principal_type"],
            )
            check_type(
                argname="argument provider_id",
                value=provider_id,
                expected_type=type_hints["provider_id"],
            )
            check_type(
                argname="argument signature_algorithm",
                value=signature_algorithm,
                expected_type=type_hints["signature_algorithm"],
            )
            check_type(
                argname="argument signing_certificate",
                value=signing_certificate,
                expected_type=type_hints["signing_certificate"],
            )
            check_type(
                argname="argument single_logout_service_url",
                value=single_logout_service_url,
                expected_type=type_hints["single_logout_service_url"],
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
                argname="argument validate_signature",
                value=validate_signature,
                expected_type=type_hints["validate_signature"],
            )
            check_type(
                argname="argument want_assertions_encrypted",
                value=want_assertions_encrypted,
                expected_type=type_hints["want_assertions_encrypted"],
            )
            check_type(
                argname="argument want_assertions_signed",
                value=want_assertions_signed,
                expected_type=type_hints["want_assertions_signed"],
            )
            check_type(
                argname="argument xml_sign_key_info_key_name_transformer",
                value=xml_sign_key_info_key_name_transformer,
                expected_type=type_hints["xml_sign_key_info_key_name_transformer"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "alias": alias,
            "entity_id": entity_id,
            "realm": realm,
            "single_sign_on_service_url": single_sign_on_service_url,
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
        if add_read_token_role_on_create is not None:
            self._values[
                "add_read_token_role_on_create"
            ] = add_read_token_role_on_create
        if authenticate_by_default is not None:
            self._values["authenticate_by_default"] = authenticate_by_default
        if authn_context_class_refs is not None:
            self._values["authn_context_class_refs"] = authn_context_class_refs
        if authn_context_comparison_type is not None:
            self._values[
                "authn_context_comparison_type"
            ] = authn_context_comparison_type
        if authn_context_decl_refs is not None:
            self._values["authn_context_decl_refs"] = authn_context_decl_refs
        if backchannel_supported is not None:
            self._values["backchannel_supported"] = backchannel_supported
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
        if force_authn is not None:
            self._values["force_authn"] = force_authn
        if gui_order is not None:
            self._values["gui_order"] = gui_order
        if hide_on_login_page is not None:
            self._values["hide_on_login_page"] = hide_on_login_page
        if id is not None:
            self._values["id"] = id
        if link_only is not None:
            self._values["link_only"] = link_only
        if login_hint is not None:
            self._values["login_hint"] = login_hint
        if name_id_policy_format is not None:
            self._values["name_id_policy_format"] = name_id_policy_format
        if post_binding_authn_request is not None:
            self._values["post_binding_authn_request"] = post_binding_authn_request
        if post_binding_logout is not None:
            self._values["post_binding_logout"] = post_binding_logout
        if post_binding_response is not None:
            self._values["post_binding_response"] = post_binding_response
        if post_broker_login_flow_alias is not None:
            self._values["post_broker_login_flow_alias"] = post_broker_login_flow_alias
        if principal_attribute is not None:
            self._values["principal_attribute"] = principal_attribute
        if principal_type is not None:
            self._values["principal_type"] = principal_type
        if provider_id is not None:
            self._values["provider_id"] = provider_id
        if signature_algorithm is not None:
            self._values["signature_algorithm"] = signature_algorithm
        if signing_certificate is not None:
            self._values["signing_certificate"] = signing_certificate
        if single_logout_service_url is not None:
            self._values["single_logout_service_url"] = single_logout_service_url
        if store_token is not None:
            self._values["store_token"] = store_token
        if sync_mode is not None:
            self._values["sync_mode"] = sync_mode
        if trust_email is not None:
            self._values["trust_email"] = trust_email
        if validate_signature is not None:
            self._values["validate_signature"] = validate_signature
        if want_assertions_encrypted is not None:
            self._values["want_assertions_encrypted"] = want_assertions_encrypted
        if want_assertions_signed is not None:
            self._values["want_assertions_signed"] = want_assertions_signed
        if xml_sign_key_info_key_name_transformer is not None:
            self._values[
                "xml_sign_key_info_key_name_transformer"
            ] = xml_sign_key_info_key_name_transformer

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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#alias SamlIdentityProvider#alias}
        """
        result = self._values.get("alias")
        assert result is not None, "Required property 'alias' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def entity_id(self) -> builtins.str:
        """The Entity ID that will be used to uniquely identify this SAML Service Provider.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#entity_id SamlIdentityProvider#entity_id}
        """
        result = self._values.get("entity_id")
        assert result is not None, "Required property 'entity_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def realm(self) -> builtins.str:
        """Realm Name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#realm SamlIdentityProvider#realm}
        """
        result = self._values.get("realm")
        assert result is not None, "Required property 'realm' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def single_sign_on_service_url(self) -> builtins.str:
        """SSO Logout URL.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#single_sign_on_service_url SamlIdentityProvider#single_sign_on_service_url}
        """
        result = self._values.get("single_sign_on_service_url")
        assert (
            result is not None
        ), "Required property 'single_sign_on_service_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def add_read_token_role_on_create(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Enable/disable if new users can read any stored tokens. This assigns the broker.read-token role.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#add_read_token_role_on_create SamlIdentityProvider#add_read_token_role_on_create}
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#authenticate_by_default SamlIdentityProvider#authenticate_by_default}
        """
        result = self._values.get("authenticate_by_default")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def authn_context_class_refs(self) -> typing.Optional[typing.List[builtins.str]]:
        """AuthnContext ClassRefs.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#authn_context_class_refs SamlIdentityProvider#authn_context_class_refs}
        """
        result = self._values.get("authn_context_class_refs")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def authn_context_comparison_type(self) -> typing.Optional[builtins.str]:
        """AuthnContext Comparison.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#authn_context_comparison_type SamlIdentityProvider#authn_context_comparison_type}
        """
        result = self._values.get("authn_context_comparison_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def authn_context_decl_refs(self) -> typing.Optional[typing.List[builtins.str]]:
        """AuthnContext DeclRefs.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#authn_context_decl_refs SamlIdentityProvider#authn_context_decl_refs}
        """
        result = self._values.get("authn_context_decl_refs")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def backchannel_supported(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Does the external IDP support backchannel logout?

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#backchannel_supported SamlIdentityProvider#backchannel_supported}
        """
        result = self._values.get("backchannel_supported")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        """Friendly name for Identity Providers.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#display_name SamlIdentityProvider#display_name}
        """
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Enable/disable this identity provider.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#enabled SamlIdentityProvider#enabled}
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
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#extra_config SamlIdentityProvider#extra_config}."""
        result = self._values.get("extra_config")
        return typing.cast(
            typing.Optional[typing.Mapping[builtins.str, builtins.str]], result
        )

    @builtins.property
    def first_broker_login_flow_alias(self) -> typing.Optional[builtins.str]:
        """Alias of authentication flow, which is triggered after first login with this identity provider.

        Term 'First Login' means that there is not yet existing Keycloak account linked with the authenticated identity provider account.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#first_broker_login_flow_alias SamlIdentityProvider#first_broker_login_flow_alias}
        """
        result = self._values.get("first_broker_login_flow_alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def force_authn(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Require Force Authn.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#force_authn SamlIdentityProvider#force_authn}
        """
        result = self._values.get("force_authn")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def gui_order(self) -> typing.Optional[builtins.str]:
        """GUI Order.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#gui_order SamlIdentityProvider#gui_order}
        """
        result = self._values.get("gui_order")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hide_on_login_page(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Hide On Login Page.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#hide_on_login_page SamlIdentityProvider#hide_on_login_page}
        """
        result = self._values.get("hide_on_login_page")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#id SamlIdentityProvider#id}.

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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#link_only SamlIdentityProvider#link_only}
        """
        result = self._values.get("link_only")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def login_hint(self) -> typing.Optional[builtins.str]:
        """Login Hint.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#login_hint SamlIdentityProvider#login_hint}
        """
        result = self._values.get("login_hint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name_id_policy_format(self) -> typing.Optional[builtins.str]:
        """Name ID Policy Format.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#name_id_policy_format SamlIdentityProvider#name_id_policy_format}
        """
        result = self._values.get("name_id_policy_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def post_binding_authn_request(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Post Binding Authn Request.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#post_binding_authn_request SamlIdentityProvider#post_binding_authn_request}
        """
        result = self._values.get("post_binding_authn_request")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def post_binding_logout(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Post Binding Logout.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#post_binding_logout SamlIdentityProvider#post_binding_logout}
        """
        result = self._values.get("post_binding_logout")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def post_binding_response(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Post Binding Response.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#post_binding_response SamlIdentityProvider#post_binding_response}
        """
        result = self._values.get("post_binding_response")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def post_broker_login_flow_alias(self) -> typing.Optional[builtins.str]:
        """Alias of authentication flow, which is triggered after each login with this identity provider.

        Useful if you want additional verification of each user authenticated with this identity provider (for example OTP). Leave this empty if you don't want any additional authenticators to be triggered after login with this identity provider. Also note, that authenticator implementations must assume that user is already set in ClientSession as identity provider already set it.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#post_broker_login_flow_alias SamlIdentityProvider#post_broker_login_flow_alias}
        """
        result = self._values.get("post_broker_login_flow_alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def principal_attribute(self) -> typing.Optional[builtins.str]:
        """Principal Attribute.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#principal_attribute SamlIdentityProvider#principal_attribute}
        """
        result = self._values.get("principal_attribute")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def principal_type(self) -> typing.Optional[builtins.str]:
        """Principal Type.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#principal_type SamlIdentityProvider#principal_type}
        """
        result = self._values.get("principal_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provider_id(self) -> typing.Optional[builtins.str]:
        """provider id, is always saml, unless you have a custom implementation.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#provider_id SamlIdentityProvider#provider_id}
        """
        result = self._values.get("provider_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def signature_algorithm(self) -> typing.Optional[builtins.str]:
        """Signing Algorithm.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#signature_algorithm SamlIdentityProvider#signature_algorithm}
        """
        result = self._values.get("signature_algorithm")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def signing_certificate(self) -> typing.Optional[builtins.str]:
        """Signing Certificate.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#signing_certificate SamlIdentityProvider#signing_certificate}
        """
        result = self._values.get("signing_certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def single_logout_service_url(self) -> typing.Optional[builtins.str]:
        """Logout URL.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#single_logout_service_url SamlIdentityProvider#single_logout_service_url}
        """
        result = self._values.get("single_logout_service_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def store_token(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Enable/disable if tokens must be stored after authenticating users.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#store_token SamlIdentityProvider#store_token}
        """
        result = self._values.get("store_token")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def sync_mode(self) -> typing.Optional[builtins.str]:
        """Sync Mode.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#sync_mode SamlIdentityProvider#sync_mode}
        """
        result = self._values.get("sync_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def trust_email(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """If enabled then email provided by this provider is not verified even if verification is enabled for the realm.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#trust_email SamlIdentityProvider#trust_email}
        """
        result = self._values.get("trust_email")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def validate_signature(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Enable/disable signature validation of SAML responses.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#validate_signature SamlIdentityProvider#validate_signature}
        """
        result = self._values.get("validate_signature")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def want_assertions_encrypted(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Want Assertions Encrypted.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#want_assertions_encrypted SamlIdentityProvider#want_assertions_encrypted}
        """
        result = self._values.get("want_assertions_encrypted")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def want_assertions_signed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Want Assertions Signed.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#want_assertions_signed SamlIdentityProvider#want_assertions_signed}
        """
        result = self._values.get("want_assertions_signed")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def xml_sign_key_info_key_name_transformer(self) -> typing.Optional[builtins.str]:
        """Sign Key Transformer.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/saml_identity_provider#xml_sign_key_info_key_name_transformer SamlIdentityProvider#xml_sign_key_info_key_name_transformer}
        """
        result = self._values.get("xml_sign_key_info_key_name_transformer")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SamlIdentityProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "SamlIdentityProvider",
    "SamlIdentityProviderConfig",
]

publication.publish()


def _typecheckingstub__97f8a966aad9686073076b11caa4fdf9c68447ecb584a458c1704ac66c9d4453(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    alias: builtins.str,
    entity_id: builtins.str,
    realm: builtins.str,
    single_sign_on_service_url: builtins.str,
    add_read_token_role_on_create: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    authenticate_by_default: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    authn_context_class_refs: typing.Optional[typing.Sequence[builtins.str]] = None,
    authn_context_comparison_type: typing.Optional[builtins.str] = None,
    authn_context_decl_refs: typing.Optional[typing.Sequence[builtins.str]] = None,
    backchannel_supported: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    display_name: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    extra_config: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    first_broker_login_flow_alias: typing.Optional[builtins.str] = None,
    force_authn: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    gui_order: typing.Optional[builtins.str] = None,
    hide_on_login_page: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    id: typing.Optional[builtins.str] = None,
    link_only: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    login_hint: typing.Optional[builtins.str] = None,
    name_id_policy_format: typing.Optional[builtins.str] = None,
    post_binding_authn_request: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    post_binding_logout: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    post_binding_response: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    post_broker_login_flow_alias: typing.Optional[builtins.str] = None,
    principal_attribute: typing.Optional[builtins.str] = None,
    principal_type: typing.Optional[builtins.str] = None,
    provider_id: typing.Optional[builtins.str] = None,
    signature_algorithm: typing.Optional[builtins.str] = None,
    signing_certificate: typing.Optional[builtins.str] = None,
    single_logout_service_url: typing.Optional[builtins.str] = None,
    store_token: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    sync_mode: typing.Optional[builtins.str] = None,
    trust_email: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    validate_signature: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    want_assertions_encrypted: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    want_assertions_signed: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    xml_sign_key_info_key_name_transformer: typing.Optional[builtins.str] = None,
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


def _typecheckingstub__8b9dafb05ffc14c0dc3a12257f6966341fa469124958dbb9bdc96071088c8e22(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f46b4774337e91ffb8ef2d33f089cdb1dc204c9bc61e7534b258f7204559587b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__58feaf94ecb5b71c77b67d75c9a0ea705263ae6d2cd43d57913407c40d09a9d6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ec9d82d8ffec731cb48903488f938bffa8f28c8831412edae28cd0279b8cbaee(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c35b56a3a77a078121b6ca5b7ea0c73aff72036d7702c955f538fe95e241c63e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__447f91590465a25c451ad141b82c7ffd78c842f14219002b82b7a5755a48cfe1(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__eb06edc7fedd9792b95c93c71c9c354fd62cbc0dd81af085140bbd52156516d0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__49e142702873998d6c95547adcf1e8b133c583c0ebd51da0b88eccbd7e500c7e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8876bf5e9c676555d79ad5a6ffc1d196eb731d43413b9412d3915c25ffbca083(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ab30b114c0cd529b50f46ae5cdd94b744e3c8c0c060912064402b1f688e71436(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8c1e193074c83a719eb043cabef170f44a2908b565b69e586317044ed455b86a(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__65d18a3d71e07da6abaa1b8d477dbfb6f7c98746c02f0e8d30f353acf71fa35d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a2391d592852161c3215960245fd02ebbbf0e69161d00177d5306df7d48f120f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3b4bde417847feb92114f89996958af8ee972359d1b525879c3bc206c36e0955(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7cd7b3ec6ee3cd2e283594ed946070e580bf1a513921ccc2ee5881121bb61e33(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__444a70224691c022134631746a8c5ce4709c0e391a80cc60a893915d6471ff8c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d624f8d00dc1e8fb08f257148de8672a2c533f943a9a7ab755c9b56f01a628c9(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f9ac548534be4312c30056a85926f9983ef338b8ce188ea97af4b0279ad19f18(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ca2fd135009815a812338fbba84d200875254ba2aee440c2e2799aa36eb42448(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e27ec219a10bd3d8cb66ec894971a05984d79401310ca539c85249cdb14f0ebc(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__df295788cf89133e3c9b2009496859a94fd8343615b189348cca1ff82d982e3f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__246514c1d14421f6c68259b2b7c43bc194ae63056afc9d09756bfcf1069b0e00(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__69251b1eb8798051ebd49bcc4d11e9ed172aeec4324e897236a6a732e281455e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__91dd594c3cdee7df03c9b09576d2fe5ee93963847d0c94ab899e9effd82bfc47(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4e7f935f60f3f26a35dd8a59f2e0e0bf15393261f0640481b0bbffc97775a4f6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__079138c8d22e7d610a45d5bc66f1d9e7382243970f6ed3a1e455aa4360c84358(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d981cd37f273d10345827ca491b3fcdb53a10861d5d9052b71bf5f295223e4a0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__070c851a8e1a16e37df9f9159874ff2e793fa481aa4692126ff205b9eef13791(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ff2385671569d7c5e13de1aedc158d77bf3ff7f6ee9aec8cbb41211cf5dd80c1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__cbe82b67e93e1f99c2f572b2f4e9010536d1e81578573a98a1e68aaef108f489(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__fed1c50c8cd596877d39d5debd39edc060fd27b4c493164586571a1f66359c71(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__616ed3af8ccff26b36cce5d290ecc790a833e9e596fcd78889b1cabd535817b2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__04ab6a495606d7575a07e02ec662eeea4689b2f385308e42c0083e9d0385414f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d39af30df9f8af5009aab94e890dd2f92e47297f40ac05ca89df5465f4be17a7(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__36f642006067e0d77b87edc72ad7f80a41b36aed07517fc533f2c6439b4b7c5f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9a27e6a7ec792cd134c5598b3686ba178a972b7f1b9c8b47a8b46cba3657527d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__49e018f8ed659d60ee172f532c50805ff942e42917a5a1cedcb83ab8230c3625(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__916318ba031d47d05013df1f6018e8520850c049062c981433e832ca871e5f82(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6e6cb4ad1d88681d502c306000d9ee621d807f15950e89377353d17acd13c19b(
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
    entity_id: builtins.str,
    realm: builtins.str,
    single_sign_on_service_url: builtins.str,
    add_read_token_role_on_create: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    authenticate_by_default: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    authn_context_class_refs: typing.Optional[typing.Sequence[builtins.str]] = None,
    authn_context_comparison_type: typing.Optional[builtins.str] = None,
    authn_context_decl_refs: typing.Optional[typing.Sequence[builtins.str]] = None,
    backchannel_supported: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    display_name: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    extra_config: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    first_broker_login_flow_alias: typing.Optional[builtins.str] = None,
    force_authn: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    gui_order: typing.Optional[builtins.str] = None,
    hide_on_login_page: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    id: typing.Optional[builtins.str] = None,
    link_only: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    login_hint: typing.Optional[builtins.str] = None,
    name_id_policy_format: typing.Optional[builtins.str] = None,
    post_binding_authn_request: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    post_binding_logout: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    post_binding_response: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    post_broker_login_flow_alias: typing.Optional[builtins.str] = None,
    principal_attribute: typing.Optional[builtins.str] = None,
    principal_type: typing.Optional[builtins.str] = None,
    provider_id: typing.Optional[builtins.str] = None,
    signature_algorithm: typing.Optional[builtins.str] = None,
    signing_certificate: typing.Optional[builtins.str] = None,
    single_logout_service_url: typing.Optional[builtins.str] = None,
    store_token: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    sync_mode: typing.Optional[builtins.str] = None,
    trust_email: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    validate_signature: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    want_assertions_encrypted: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    want_assertions_signed: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    xml_sign_key_info_key_name_transformer: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
