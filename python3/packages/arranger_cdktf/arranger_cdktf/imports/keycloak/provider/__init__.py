"""
# `provider`

Refer to the Terraform Registory for docs: [`keycloak`](https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs).
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


class KeycloakProvider(
    _cdktf_9a9027ec.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.provider.KeycloakProvider",
):
    """Represents a {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs keycloak}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        client_id: builtins.str,
        url: builtins.str,
        additional_headers: typing.Optional[
            typing.Mapping[builtins.str, builtins.str]
        ] = None,
        alias: typing.Optional[builtins.str] = None,
        base_path: typing.Optional[builtins.str] = None,
        client_secret: typing.Optional[builtins.str] = None,
        client_timeout: typing.Optional[jsii.Number] = None,
        initial_login: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        password: typing.Optional[builtins.str] = None,
        realm: typing.Optional[builtins.str] = None,
        red_hat_sso: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        root_ca_certificate: typing.Optional[builtins.str] = None,
        tls_insecure_skip_verify: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        """Create a new {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs keycloak} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param client_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#client_id KeycloakProvider#client_id}.
        :param url: The base URL of the Keycloak instance, before ``/auth``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#url KeycloakProvider#url}
        :param additional_headers: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#additional_headers KeycloakProvider#additional_headers}.
        :param alias: Alias name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#alias KeycloakProvider#alias}
        :param base_path: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#base_path KeycloakProvider#base_path}.
        :param client_secret: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#client_secret KeycloakProvider#client_secret}.
        :param client_timeout: Timeout (in seconds) of the Keycloak client. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#client_timeout KeycloakProvider#client_timeout}
        :param initial_login: Whether or not to login to Keycloak instance on provider initialization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#initial_login KeycloakProvider#initial_login}
        :param password: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#password KeycloakProvider#password}.
        :param realm: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#realm KeycloakProvider#realm}.
        :param red_hat_sso: When true, the provider will treat the Keycloak instance as a Red Hat SSO server, specifically when parsing the version returned from the /serverinfo API endpoint. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#red_hat_sso KeycloakProvider#red_hat_sso}
        :param root_ca_certificate: Allows x509 calls using an unknown CA certificate (for development purposes). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#root_ca_certificate KeycloakProvider#root_ca_certificate}
        :param tls_insecure_skip_verify: Allows ignoring insecure certificates when set to true. Defaults to false. Disabling security check is dangerous and should be avoided. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#tls_insecure_skip_verify KeycloakProvider#tls_insecure_skip_verify}
        :param username: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#username KeycloakProvider#username}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__c2d01a976383beadc940b7f47720bec21ec9c08cb62299ba3edd17eac893a2d4
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = KeycloakProviderConfig(
            client_id=client_id,
            url=url,
            additional_headers=additional_headers,
            alias=alias,
            base_path=base_path,
            client_secret=client_secret,
            client_timeout=client_timeout,
            initial_login=initial_login,
            password=password,
            realm=realm,
            red_hat_sso=red_hat_sso,
            root_ca_certificate=root_ca_certificate,
            tls_insecure_skip_verify=tls_insecure_skip_verify,
            username=username,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAdditionalHeaders")
    def reset_additional_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalHeaders", []))

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetBasePath")
    def reset_base_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBasePath", []))

    @jsii.member(jsii_name="resetClientSecret")
    def reset_client_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientSecret", []))

    @jsii.member(jsii_name="resetClientTimeout")
    def reset_client_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientTimeout", []))

    @jsii.member(jsii_name="resetInitialLogin")
    def reset_initial_login(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitialLogin", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetRealm")
    def reset_realm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRealm", []))

    @jsii.member(jsii_name="resetRedHatSso")
    def reset_red_hat_sso(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedHatSso", []))

    @jsii.member(jsii_name="resetRootCaCertificate")
    def reset_root_ca_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootCaCertificate", []))

    @jsii.member(jsii_name="resetTlsInsecureSkipVerify")
    def reset_tls_insecure_skip_verify(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsInsecureSkipVerify", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

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
    @jsii.member(jsii_name="additionalHeadersInput")
    def additional_headers_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(
            typing.Optional[typing.Mapping[builtins.str, builtins.str]],
            jsii.get(self, "additionalHeadersInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="basePathInput")
    def base_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "basePathInput")
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
    @jsii.member(jsii_name="clientTimeoutInput")
    def client_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(
            typing.Optional[jsii.Number], jsii.get(self, "clientTimeoutInput")
        )

    @builtins.property
    @jsii.member(jsii_name="initialLoginInput")
    def initial_login_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "initialLoginInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "passwordInput")
        )

    @builtins.property
    @jsii.member(jsii_name="realmInput")
    def realm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "realmInput"))

    @builtins.property
    @jsii.member(jsii_name="redHatSsoInput")
    def red_hat_sso_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "redHatSsoInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="rootCaCertificateInput")
    def root_ca_certificate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "rootCaCertificateInput")
        )

    @builtins.property
    @jsii.member(jsii_name="tlsInsecureSkipVerifyInput")
    def tls_insecure_skip_verify_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "tlsInsecureSkipVerifyInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "usernameInput")
        )

    @builtins.property
    @jsii.member(jsii_name="additionalHeaders")
    def additional_headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(
            typing.Optional[typing.Mapping[builtins.str, builtins.str]],
            jsii.get(self, "additionalHeaders"),
        )

    @additional_headers.setter
    def additional_headers(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__2c7a31a7b46dbf29f6e39849afcdc4a637e7bb567fd339c64ce7fdf2c4306352
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "additionalHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__39f50082d7858a68cb049f4e43dcf7314ed9b12bf162c8a57d40b48965e286f5
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="basePath")
    def base_path(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "basePath"))

    @base_path.setter
    def base_path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__aee86a700d59a9701fa3071816ff7b18d433973ff52744db7b4852985bbbdeeb
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "basePath", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__bd01fb11f449334077a926696b8571504497dac597e4017f2aca978f6869f646
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "clientSecret")
        )

    @client_secret.setter
    def client_secret(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__dd91af398da5c60b5cb7c707aa3961e20b7b9a91b7d85d94f70490d553d91a47
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="clientTimeout")
    def client_timeout(self) -> typing.Optional[jsii.Number]:
        return typing.cast(
            typing.Optional[jsii.Number], jsii.get(self, "clientTimeout")
        )

    @client_timeout.setter
    def client_timeout(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__1a992d761058fbe6eb01cd9ce9cba50cfd80fa378986ec19b0fbad2543128602
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "clientTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="initialLogin")
    def initial_login(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "initialLogin"),
        )

    @initial_login.setter
    def initial_login(
        self,
        value: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__e016747635d56ce13981c74ddb9db1daf0e56d4c56f6b4f6249bad4d8db79a4c
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "initialLogin", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "password"))

    @password.setter
    def password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__927bf4145f4dd7ce0e0b5d3126b900a536040f0a3149ff1ff9500792553c80e1
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="realm")
    def realm(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "realm"))

    @realm.setter
    def realm(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__df11a7e292a3378b0fa480b74c67ffa002fbb3613ba0ebbf2e0d2ac018a77cb9
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "realm", value)

    @builtins.property
    @jsii.member(jsii_name="redHatSso")
    def red_hat_sso(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "redHatSso"),
        )

    @red_hat_sso.setter
    def red_hat_sso(
        self,
        value: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__2ecb2726d34cd1ef16a88a2966f8c89ae9b613dc75ad1b95b1bd229b37d2cac4
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "redHatSso", value)

    @builtins.property
    @jsii.member(jsii_name="rootCaCertificate")
    def root_ca_certificate(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "rootCaCertificate")
        )

    @root_ca_certificate.setter
    def root_ca_certificate(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__cddf936da5331bda041585e7c1674c8de9d984377862a6771f3a2db07d88eaa7
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "rootCaCertificate", value)

    @builtins.property
    @jsii.member(jsii_name="tlsInsecureSkipVerify")
    def tls_insecure_skip_verify(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "tlsInsecureSkipVerify"),
        )

    @tls_insecure_skip_verify.setter
    def tls_insecure_skip_verify(
        self,
        value: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__62f0789ba8bb525e5edc90de2d0a68554395bddbd0cc9371a905910daf188b24
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "tlsInsecureSkipVerify", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "url"))

    @url.setter
    def url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__1880ec6ca502460f339fd886d87288c82256a4faa19e742e4f9761531452c046
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "username"))

    @username.setter
    def username(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__8b57621c296120da0f1165f0af1345dfcd9e5ae4afeae01dbf948c485a4736f0
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "username", value)


@jsii.data_type(
    jsii_type="keycloak.provider.KeycloakProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "url": "url",
        "additional_headers": "additionalHeaders",
        "alias": "alias",
        "base_path": "basePath",
        "client_secret": "clientSecret",
        "client_timeout": "clientTimeout",
        "initial_login": "initialLogin",
        "password": "password",
        "realm": "realm",
        "red_hat_sso": "redHatSso",
        "root_ca_certificate": "rootCaCertificate",
        "tls_insecure_skip_verify": "tlsInsecureSkipVerify",
        "username": "username",
    },
)
class KeycloakProviderConfig:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        url: builtins.str,
        additional_headers: typing.Optional[
            typing.Mapping[builtins.str, builtins.str]
        ] = None,
        alias: typing.Optional[builtins.str] = None,
        base_path: typing.Optional[builtins.str] = None,
        client_secret: typing.Optional[builtins.str] = None,
        client_timeout: typing.Optional[jsii.Number] = None,
        initial_login: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        password: typing.Optional[builtins.str] = None,
        realm: typing.Optional[builtins.str] = None,
        red_hat_sso: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        root_ca_certificate: typing.Optional[builtins.str] = None,
        tls_insecure_skip_verify: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param client_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#client_id KeycloakProvider#client_id}.
        :param url: The base URL of the Keycloak instance, before ``/auth``. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#url KeycloakProvider#url}
        :param additional_headers: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#additional_headers KeycloakProvider#additional_headers}.
        :param alias: Alias name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#alias KeycloakProvider#alias}
        :param base_path: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#base_path KeycloakProvider#base_path}.
        :param client_secret: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#client_secret KeycloakProvider#client_secret}.
        :param client_timeout: Timeout (in seconds) of the Keycloak client. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#client_timeout KeycloakProvider#client_timeout}
        :param initial_login: Whether or not to login to Keycloak instance on provider initialization. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#initial_login KeycloakProvider#initial_login}
        :param password: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#password KeycloakProvider#password}.
        :param realm: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#realm KeycloakProvider#realm}.
        :param red_hat_sso: When true, the provider will treat the Keycloak instance as a Red Hat SSO server, specifically when parsing the version returned from the /serverinfo API endpoint. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#red_hat_sso KeycloakProvider#red_hat_sso}
        :param root_ca_certificate: Allows x509 calls using an unknown CA certificate (for development purposes). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#root_ca_certificate KeycloakProvider#root_ca_certificate}
        :param tls_insecure_skip_verify: Allows ignoring insecure certificates when set to true. Defaults to false. Disabling security check is dangerous and should be avoided. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#tls_insecure_skip_verify KeycloakProvider#tls_insecure_skip_verify}
        :param username: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#username KeycloakProvider#username}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__be7c2079e2423c9c545c578add2b41bf6fd3629f50fbfc690f38b0a48a52c54f
            )
            check_type(
                argname="argument client_id",
                value=client_id,
                expected_type=type_hints["client_id"],
            )
            check_type(
                argname="argument url", value=url, expected_type=type_hints["url"]
            )
            check_type(
                argname="argument additional_headers",
                value=additional_headers,
                expected_type=type_hints["additional_headers"],
            )
            check_type(
                argname="argument alias", value=alias, expected_type=type_hints["alias"]
            )
            check_type(
                argname="argument base_path",
                value=base_path,
                expected_type=type_hints["base_path"],
            )
            check_type(
                argname="argument client_secret",
                value=client_secret,
                expected_type=type_hints["client_secret"],
            )
            check_type(
                argname="argument client_timeout",
                value=client_timeout,
                expected_type=type_hints["client_timeout"],
            )
            check_type(
                argname="argument initial_login",
                value=initial_login,
                expected_type=type_hints["initial_login"],
            )
            check_type(
                argname="argument password",
                value=password,
                expected_type=type_hints["password"],
            )
            check_type(
                argname="argument realm", value=realm, expected_type=type_hints["realm"]
            )
            check_type(
                argname="argument red_hat_sso",
                value=red_hat_sso,
                expected_type=type_hints["red_hat_sso"],
            )
            check_type(
                argname="argument root_ca_certificate",
                value=root_ca_certificate,
                expected_type=type_hints["root_ca_certificate"],
            )
            check_type(
                argname="argument tls_insecure_skip_verify",
                value=tls_insecure_skip_verify,
                expected_type=type_hints["tls_insecure_skip_verify"],
            )
            check_type(
                argname="argument username",
                value=username,
                expected_type=type_hints["username"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_id": client_id,
            "url": url,
        }
        if additional_headers is not None:
            self._values["additional_headers"] = additional_headers
        if alias is not None:
            self._values["alias"] = alias
        if base_path is not None:
            self._values["base_path"] = base_path
        if client_secret is not None:
            self._values["client_secret"] = client_secret
        if client_timeout is not None:
            self._values["client_timeout"] = client_timeout
        if initial_login is not None:
            self._values["initial_login"] = initial_login
        if password is not None:
            self._values["password"] = password
        if realm is not None:
            self._values["realm"] = realm
        if red_hat_sso is not None:
            self._values["red_hat_sso"] = red_hat_sso
        if root_ca_certificate is not None:
            self._values["root_ca_certificate"] = root_ca_certificate
        if tls_insecure_skip_verify is not None:
            self._values["tls_insecure_skip_verify"] = tls_insecure_skip_verify
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def client_id(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#client_id KeycloakProvider#client_id}."""
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def url(self) -> builtins.str:
        """The base URL of the Keycloak instance, before ``/auth``.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#url KeycloakProvider#url}
        """
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#additional_headers KeycloakProvider#additional_headers}."""
        result = self._values.get("additional_headers")
        return typing.cast(
            typing.Optional[typing.Mapping[builtins.str, builtins.str]], result
        )

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        """Alias name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#alias KeycloakProvider#alias}
        """
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def base_path(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#base_path KeycloakProvider#base_path}."""
        result = self._values.get("base_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_secret(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#client_secret KeycloakProvider#client_secret}."""
        result = self._values.get("client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_timeout(self) -> typing.Optional[jsii.Number]:
        """Timeout (in seconds) of the Keycloak client.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#client_timeout KeycloakProvider#client_timeout}
        """
        result = self._values.get("client_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def initial_login(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Whether or not to login to Keycloak instance on provider initialization.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#initial_login KeycloakProvider#initial_login}
        """
        result = self._values.get("initial_login")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#password KeycloakProvider#password}."""
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def realm(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#realm KeycloakProvider#realm}."""
        result = self._values.get("realm")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def red_hat_sso(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """When true, the provider will treat the Keycloak instance as a Red Hat SSO server, specifically when parsing the version returned from the /serverinfo API endpoint.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#red_hat_sso KeycloakProvider#red_hat_sso}
        """
        result = self._values.get("red_hat_sso")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def root_ca_certificate(self) -> typing.Optional[builtins.str]:
        """Allows x509 calls using an unknown CA certificate (for development purposes).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#root_ca_certificate KeycloakProvider#root_ca_certificate}
        """
        result = self._values.get("root_ca_certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls_insecure_skip_verify(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Allows ignoring insecure certificates when set to true.

        Defaults to false. Disabling security check is dangerous and should be avoided.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#tls_insecure_skip_verify KeycloakProvider#tls_insecure_skip_verify}
        """
        result = self._values.get("tls_insecure_skip_verify")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs#username KeycloakProvider#username}."""
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeycloakProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "KeycloakProvider",
    "KeycloakProviderConfig",
]

publication.publish()


def _typecheckingstub__c2d01a976383beadc940b7f47720bec21ec9c08cb62299ba3edd17eac893a2d4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    client_id: builtins.str,
    url: builtins.str,
    additional_headers: typing.Optional[
        typing.Mapping[builtins.str, builtins.str]
    ] = None,
    alias: typing.Optional[builtins.str] = None,
    base_path: typing.Optional[builtins.str] = None,
    client_secret: typing.Optional[builtins.str] = None,
    client_timeout: typing.Optional[jsii.Number] = None,
    initial_login: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    password: typing.Optional[builtins.str] = None,
    realm: typing.Optional[builtins.str] = None,
    red_hat_sso: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    root_ca_certificate: typing.Optional[builtins.str] = None,
    tls_insecure_skip_verify: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__2c7a31a7b46dbf29f6e39849afcdc4a637e7bb567fd339c64ce7fdf2c4306352(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__39f50082d7858a68cb049f4e43dcf7314ed9b12bf162c8a57d40b48965e286f5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__aee86a700d59a9701fa3071816ff7b18d433973ff52744db7b4852985bbbdeeb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__bd01fb11f449334077a926696b8571504497dac597e4017f2aca978f6869f646(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__dd91af398da5c60b5cb7c707aa3961e20b7b9a91b7d85d94f70490d553d91a47(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1a992d761058fbe6eb01cd9ce9cba50cfd80fa378986ec19b0fbad2543128602(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e016747635d56ce13981c74ddb9db1daf0e56d4c56f6b4f6249bad4d8db79a4c(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__927bf4145f4dd7ce0e0b5d3126b900a536040f0a3149ff1ff9500792553c80e1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__df11a7e292a3378b0fa480b74c67ffa002fbb3613ba0ebbf2e0d2ac018a77cb9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__2ecb2726d34cd1ef16a88a2966f8c89ae9b613dc75ad1b95b1bd229b37d2cac4(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__cddf936da5331bda041585e7c1674c8de9d984377862a6771f3a2db07d88eaa7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__62f0789ba8bb525e5edc90de2d0a68554395bddbd0cc9371a905910daf188b24(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1880ec6ca502460f339fd886d87288c82256a4faa19e742e4f9761531452c046(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8b57621c296120da0f1165f0af1345dfcd9e5ae4afeae01dbf948c485a4736f0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__be7c2079e2423c9c545c578add2b41bf6fd3629f50fbfc690f38b0a48a52c54f(
    *,
    client_id: builtins.str,
    url: builtins.str,
    additional_headers: typing.Optional[
        typing.Mapping[builtins.str, builtins.str]
    ] = None,
    alias: typing.Optional[builtins.str] = None,
    base_path: typing.Optional[builtins.str] = None,
    client_secret: typing.Optional[builtins.str] = None,
    client_timeout: typing.Optional[jsii.Number] = None,
    initial_login: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    password: typing.Optional[builtins.str] = None,
    realm: typing.Optional[builtins.str] = None,
    red_hat_sso: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    root_ca_certificate: typing.Optional[builtins.str] = None,
    tls_insecure_skip_verify: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
