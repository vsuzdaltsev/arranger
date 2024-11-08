"""
# `keycloak_authentication_bindings`

Refer to the Terraform Registory for docs: [`keycloak_authentication_bindings`](https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/authentication_bindings).
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


class AuthenticationBindings(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.authenticationBindings.AuthenticationBindings",
):
    """Represents a {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/authentication_bindings keycloak_authentication_bindings}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        realm_id: builtins.str,
        browser_flow: typing.Optional[builtins.str] = None,
        client_authentication_flow: typing.Optional[builtins.str] = None,
        direct_grant_flow: typing.Optional[builtins.str] = None,
        docker_authentication_flow: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        registration_flow: typing.Optional[builtins.str] = None,
        reset_credentials_flow: typing.Optional[builtins.str] = None,
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
        """Create a new {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/authentication_bindings keycloak_authentication_bindings} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param realm_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/authentication_bindings#realm_id AuthenticationBindings#realm_id}.
        :param browser_flow: Which flow should be used for BrowserFlow. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/authentication_bindings#browser_flow AuthenticationBindings#browser_flow}
        :param client_authentication_flow: Which flow should be used for ClientAuthenticationFlow. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/authentication_bindings#client_authentication_flow AuthenticationBindings#client_authentication_flow}
        :param direct_grant_flow: Which flow should be used for DirectGrantFlow. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/authentication_bindings#direct_grant_flow AuthenticationBindings#direct_grant_flow}
        :param docker_authentication_flow: Which flow should be used for DockerAuthenticationFlow. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/authentication_bindings#docker_authentication_flow AuthenticationBindings#docker_authentication_flow}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/authentication_bindings#id AuthenticationBindings#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param registration_flow: Which flow should be used for RegistrationFlow. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/authentication_bindings#registration_flow AuthenticationBindings#registration_flow}
        :param reset_credentials_flow: Which flow should be used for ResetCredentialsFlow. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/authentication_bindings#reset_credentials_flow AuthenticationBindings#reset_credentials_flow}
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
                _typecheckingstub__79c2c16b3d6f6f33a67ef9ff6730d76ce36cac6d8ac4c2467da74261f2e20d60
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(
                argname="argument id_", value=id_, expected_type=type_hints["id_"]
            )
        config = AuthenticationBindingsConfig(
            realm_id=realm_id,
            browser_flow=browser_flow,
            client_authentication_flow=client_authentication_flow,
            direct_grant_flow=direct_grant_flow,
            docker_authentication_flow=docker_authentication_flow,
            id=id,
            registration_flow=registration_flow,
            reset_credentials_flow=reset_credentials_flow,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetBrowserFlow")
    def reset_browser_flow(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBrowserFlow", []))

    @jsii.member(jsii_name="resetClientAuthenticationFlow")
    def reset_client_authentication_flow(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientAuthenticationFlow", []))

    @jsii.member(jsii_name="resetDirectGrantFlow")
    def reset_direct_grant_flow(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDirectGrantFlow", []))

    @jsii.member(jsii_name="resetDockerAuthenticationFlow")
    def reset_docker_authentication_flow(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDockerAuthenticationFlow", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetRegistrationFlow")
    def reset_registration_flow(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegistrationFlow", []))

    @jsii.member(jsii_name="resetResetCredentialsFlow")
    def reset_reset_credentials_flow(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResetCredentialsFlow", []))

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
    @jsii.member(jsii_name="directGrantFlowInput")
    def direct_grant_flow_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "directGrantFlowInput")
        )

    @builtins.property
    @jsii.member(jsii_name="dockerAuthenticationFlowInput")
    def docker_authentication_flow_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "dockerAuthenticationFlowInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="realmIdInput")
    def realm_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "realmIdInput")
        )

    @builtins.property
    @jsii.member(jsii_name="registrationFlowInput")
    def registration_flow_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "registrationFlowInput")
        )

    @builtins.property
    @jsii.member(jsii_name="resetCredentialsFlowInput")
    def reset_credentials_flow_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "resetCredentialsFlowInput")
        )

    @builtins.property
    @jsii.member(jsii_name="browserFlow")
    def browser_flow(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "browserFlow"))

    @browser_flow.setter
    def browser_flow(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__4abfb14690341bd293f58970338b3a848d127b3280c4f4d8a7f0a1ac70d02de5
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
                _typecheckingstub__5ac8f5f6f88ed0353ccf6e83e5081ded4bafb5012fe3c1d3c76a92b29961b2ed
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "clientAuthenticationFlow", value)

    @builtins.property
    @jsii.member(jsii_name="directGrantFlow")
    def direct_grant_flow(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directGrantFlow"))

    @direct_grant_flow.setter
    def direct_grant_flow(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__82f5711ed241b6a449cfd8609fbf083f28d2ca1ae15bf338f22243bca16646ef
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "directGrantFlow", value)

    @builtins.property
    @jsii.member(jsii_name="dockerAuthenticationFlow")
    def docker_authentication_flow(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dockerAuthenticationFlow"))

    @docker_authentication_flow.setter
    def docker_authentication_flow(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__c8edaa246235818391f7789f47cfcdba61155f3be4f7544f9c7838cdcc325447
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "dockerAuthenticationFlow", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__86ffc5c3c1edeab2b71e000af4f2f32511e965e862b786a7f1b41447f1ee0468
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="realmId")
    def realm_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "realmId"))

    @realm_id.setter
    def realm_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__0847cf249fc31db2a227a81454320a988ce558674d5f7266ae72cf6513774e30
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "realmId", value)

    @builtins.property
    @jsii.member(jsii_name="registrationFlow")
    def registration_flow(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "registrationFlow"))

    @registration_flow.setter
    def registration_flow(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__fadb37f6c1783b17b7d8b92721629f959b9f99bdfe6f18cfc2936a7da93c25e6
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "registrationFlow", value)

    @builtins.property
    @jsii.member(jsii_name="resetCredentialsFlow")
    def reset_credentials_flow(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resetCredentialsFlow"))

    @reset_credentials_flow.setter
    def reset_credentials_flow(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a6a51484daf3d734dc03cf93697d939f6cdd00f8fe7c68238ebb352931495d2a
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "resetCredentialsFlow", value)


@jsii.data_type(
    jsii_type="keycloak.authenticationBindings.AuthenticationBindingsConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "realm_id": "realmId",
        "browser_flow": "browserFlow",
        "client_authentication_flow": "clientAuthenticationFlow",
        "direct_grant_flow": "directGrantFlow",
        "docker_authentication_flow": "dockerAuthenticationFlow",
        "id": "id",
        "registration_flow": "registrationFlow",
        "reset_credentials_flow": "resetCredentialsFlow",
    },
)
class AuthenticationBindingsConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        realm_id: builtins.str,
        browser_flow: typing.Optional[builtins.str] = None,
        client_authentication_flow: typing.Optional[builtins.str] = None,
        direct_grant_flow: typing.Optional[builtins.str] = None,
        docker_authentication_flow: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        registration_flow: typing.Optional[builtins.str] = None,
        reset_credentials_flow: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param connection:
        :param count:
        :param depends_on:
        :param for_each:
        :param lifecycle:
        :param provider:
        :param provisioners:
        :param realm_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/authentication_bindings#realm_id AuthenticationBindings#realm_id}.
        :param browser_flow: Which flow should be used for BrowserFlow. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/authentication_bindings#browser_flow AuthenticationBindings#browser_flow}
        :param client_authentication_flow: Which flow should be used for ClientAuthenticationFlow. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/authentication_bindings#client_authentication_flow AuthenticationBindings#client_authentication_flow}
        :param direct_grant_flow: Which flow should be used for DirectGrantFlow. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/authentication_bindings#direct_grant_flow AuthenticationBindings#direct_grant_flow}
        :param docker_authentication_flow: Which flow should be used for DockerAuthenticationFlow. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/authentication_bindings#docker_authentication_flow AuthenticationBindings#docker_authentication_flow}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/authentication_bindings#id AuthenticationBindings#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param registration_flow: Which flow should be used for RegistrationFlow. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/authentication_bindings#registration_flow AuthenticationBindings#registration_flow}
        :param reset_credentials_flow: Which flow should be used for ResetCredentialsFlow. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/authentication_bindings#reset_credentials_flow AuthenticationBindings#reset_credentials_flow}
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__fbdddc74babe27e67df2dc19a0ca5d0d85076dae86c25ab1e3a5246fed403ec3
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
                argname="argument realm_id",
                value=realm_id,
                expected_type=type_hints["realm_id"],
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
                argname="argument direct_grant_flow",
                value=direct_grant_flow,
                expected_type=type_hints["direct_grant_flow"],
            )
            check_type(
                argname="argument docker_authentication_flow",
                value=docker_authentication_flow,
                expected_type=type_hints["docker_authentication_flow"],
            )
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(
                argname="argument registration_flow",
                value=registration_flow,
                expected_type=type_hints["registration_flow"],
            )
            check_type(
                argname="argument reset_credentials_flow",
                value=reset_credentials_flow,
                expected_type=type_hints["reset_credentials_flow"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
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
        if browser_flow is not None:
            self._values["browser_flow"] = browser_flow
        if client_authentication_flow is not None:
            self._values["client_authentication_flow"] = client_authentication_flow
        if direct_grant_flow is not None:
            self._values["direct_grant_flow"] = direct_grant_flow
        if docker_authentication_flow is not None:
            self._values["docker_authentication_flow"] = docker_authentication_flow
        if id is not None:
            self._values["id"] = id
        if registration_flow is not None:
            self._values["registration_flow"] = registration_flow
        if reset_credentials_flow is not None:
            self._values["reset_credentials_flow"] = reset_credentials_flow

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
    def realm_id(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/authentication_bindings#realm_id AuthenticationBindings#realm_id}."""
        result = self._values.get("realm_id")
        assert result is not None, "Required property 'realm_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def browser_flow(self) -> typing.Optional[builtins.str]:
        """Which flow should be used for BrowserFlow.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/authentication_bindings#browser_flow AuthenticationBindings#browser_flow}
        """
        result = self._values.get("browser_flow")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_authentication_flow(self) -> typing.Optional[builtins.str]:
        """Which flow should be used for ClientAuthenticationFlow.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/authentication_bindings#client_authentication_flow AuthenticationBindings#client_authentication_flow}
        """
        result = self._values.get("client_authentication_flow")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def direct_grant_flow(self) -> typing.Optional[builtins.str]:
        """Which flow should be used for DirectGrantFlow.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/authentication_bindings#direct_grant_flow AuthenticationBindings#direct_grant_flow}
        """
        result = self._values.get("direct_grant_flow")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def docker_authentication_flow(self) -> typing.Optional[builtins.str]:
        """Which flow should be used for DockerAuthenticationFlow.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/authentication_bindings#docker_authentication_flow AuthenticationBindings#docker_authentication_flow}
        """
        result = self._values.get("docker_authentication_flow")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/authentication_bindings#id AuthenticationBindings#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def registration_flow(self) -> typing.Optional[builtins.str]:
        """Which flow should be used for RegistrationFlow.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/authentication_bindings#registration_flow AuthenticationBindings#registration_flow}
        """
        result = self._values.get("registration_flow")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def reset_credentials_flow(self) -> typing.Optional[builtins.str]:
        """Which flow should be used for ResetCredentialsFlow.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/authentication_bindings#reset_credentials_flow AuthenticationBindings#reset_credentials_flow}
        """
        result = self._values.get("reset_credentials_flow")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthenticationBindingsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AuthenticationBindings",
    "AuthenticationBindingsConfig",
]

publication.publish()


def _typecheckingstub__79c2c16b3d6f6f33a67ef9ff6730d76ce36cac6d8ac4c2467da74261f2e20d60(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    realm_id: builtins.str,
    browser_flow: typing.Optional[builtins.str] = None,
    client_authentication_flow: typing.Optional[builtins.str] = None,
    direct_grant_flow: typing.Optional[builtins.str] = None,
    docker_authentication_flow: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    registration_flow: typing.Optional[builtins.str] = None,
    reset_credentials_flow: typing.Optional[builtins.str] = None,
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


def _typecheckingstub__4abfb14690341bd293f58970338b3a848d127b3280c4f4d8a7f0a1ac70d02de5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__5ac8f5f6f88ed0353ccf6e83e5081ded4bafb5012fe3c1d3c76a92b29961b2ed(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__82f5711ed241b6a449cfd8609fbf083f28d2ca1ae15bf338f22243bca16646ef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c8edaa246235818391f7789f47cfcdba61155f3be4f7544f9c7838cdcc325447(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__86ffc5c3c1edeab2b71e000af4f2f32511e965e862b786a7f1b41447f1ee0468(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0847cf249fc31db2a227a81454320a988ce558674d5f7266ae72cf6513774e30(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__fadb37f6c1783b17b7d8b92721629f959b9f99bdfe6f18cfc2936a7da93c25e6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a6a51484daf3d734dc03cf93697d939f6cdd00f8fe7c68238ebb352931495d2a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__fbdddc74babe27e67df2dc19a0ca5d0d85076dae86c25ab1e3a5246fed403ec3(
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
    realm_id: builtins.str,
    browser_flow: typing.Optional[builtins.str] = None,
    client_authentication_flow: typing.Optional[builtins.str] = None,
    direct_grant_flow: typing.Optional[builtins.str] = None,
    docker_authentication_flow: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    registration_flow: typing.Optional[builtins.str] = None,
    reset_credentials_flow: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
