"""
# `keycloak_openid_audience_resolve_protocol_mapper`

Refer to the Terraform Registory for docs: [`keycloak_openid_audience_resolve_protocol_mapper`](https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_audience_resolve_protocol_mapper).
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


class OpenidAudienceResolveProtocolMapper(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.openidAudienceResolveProtocolMapper.OpenidAudienceResolveProtocolMapper",
):
    """Represents a {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_audience_resolve_protocol_mapper keycloak_openid_audience_resolve_protocol_mapper}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        realm_id: builtins.str,
        client_id: typing.Optional[builtins.str] = None,
        client_scope_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
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
        """Create a new {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_audience_resolve_protocol_mapper keycloak_openid_audience_resolve_protocol_mapper} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param realm_id: The realm id where the associated client or client scope exists. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_audience_resolve_protocol_mapper#realm_id OpenidAudienceResolveProtocolMapper#realm_id}
        :param client_id: The mapper's associated client. Cannot be used at the same time as client_scope_id. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_audience_resolve_protocol_mapper#client_id OpenidAudienceResolveProtocolMapper#client_id}
        :param client_scope_id: The mapper's associated client scope. Cannot be used at the same time as client_id. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_audience_resolve_protocol_mapper#client_scope_id OpenidAudienceResolveProtocolMapper#client_scope_id}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_audience_resolve_protocol_mapper#id OpenidAudienceResolveProtocolMapper#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: A human-friendly name that will appear in the Keycloak console. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_audience_resolve_protocol_mapper#name OpenidAudienceResolveProtocolMapper#name}
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
                _typecheckingstub__2bab18d70f04d381d2245b7c90f355f5c3cb4ad01d7f47ba6daf40e48721c65a
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(
                argname="argument id_", value=id_, expected_type=type_hints["id_"]
            )
        config = OpenidAudienceResolveProtocolMapperConfig(
            realm_id=realm_id,
            client_id=client_id,
            client_scope_id=client_scope_id,
            id=id,
            name=name,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetClientId")
    def reset_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientId", []))

    @jsii.member(jsii_name="resetClientScopeId")
    def reset_client_scope_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientScopeId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

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
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "clientIdInput")
        )

    @builtins.property
    @jsii.member(jsii_name="clientScopeIdInput")
    def client_scope_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "clientScopeIdInput")
        )

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

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
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__3fbcf3ae5b1aed599e25379007603aa65ec2a0c1654aef8ca9f0ba9fdafc0b07
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientScopeId")
    def client_scope_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientScopeId"))

    @client_scope_id.setter
    def client_scope_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__42411c19b8c1ce9b39e383325e4f4396280d3113283737e462c25b3389938fc3
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "clientScopeId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__77b88ad219b0687c2f33a9ba048c8e31ccb95c53b5ece91eae90edfd1825f8f3
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__80a193a12391524363119fcc64d354b8f48a259df2fa9ec48294a07ea5057775
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="realmId")
    def realm_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "realmId"))

    @realm_id.setter
    def realm_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__793fcbbe6b7752002fa42f89facc2045933aa11faee41b7dc6be33e92acd86b0
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "realmId", value)


@jsii.data_type(
    jsii_type="keycloak.openidAudienceResolveProtocolMapper.OpenidAudienceResolveProtocolMapperConfig",
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
        "client_id": "clientId",
        "client_scope_id": "clientScopeId",
        "id": "id",
        "name": "name",
    },
)
class OpenidAudienceResolveProtocolMapperConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        client_id: typing.Optional[builtins.str] = None,
        client_scope_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param connection:
        :param count:
        :param depends_on:
        :param for_each:
        :param lifecycle:
        :param provider:
        :param provisioners:
        :param realm_id: The realm id where the associated client or client scope exists. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_audience_resolve_protocol_mapper#realm_id OpenidAudienceResolveProtocolMapper#realm_id}
        :param client_id: The mapper's associated client. Cannot be used at the same time as client_scope_id. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_audience_resolve_protocol_mapper#client_id OpenidAudienceResolveProtocolMapper#client_id}
        :param client_scope_id: The mapper's associated client scope. Cannot be used at the same time as client_id. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_audience_resolve_protocol_mapper#client_scope_id OpenidAudienceResolveProtocolMapper#client_scope_id}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_audience_resolve_protocol_mapper#id OpenidAudienceResolveProtocolMapper#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: A human-friendly name that will appear in the Keycloak console. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_audience_resolve_protocol_mapper#name OpenidAudienceResolveProtocolMapper#name}
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__87d39fc1005f429ec4877b2e502389ec0d128b8be23642bb85edfb691ef0fd88
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
                argname="argument client_id",
                value=client_id,
                expected_type=type_hints["client_id"],
            )
            check_type(
                argname="argument client_scope_id",
                value=client_scope_id,
                expected_type=type_hints["client_scope_id"],
            )
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(
                argname="argument name", value=name, expected_type=type_hints["name"]
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
        if client_id is not None:
            self._values["client_id"] = client_id
        if client_scope_id is not None:
            self._values["client_scope_id"] = client_scope_id
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

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
        """The realm id where the associated client or client scope exists.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_audience_resolve_protocol_mapper#realm_id OpenidAudienceResolveProtocolMapper#realm_id}
        """
        result = self._values.get("realm_id")
        assert result is not None, "Required property 'realm_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_id(self) -> typing.Optional[builtins.str]:
        """The mapper's associated client. Cannot be used at the same time as client_scope_id.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_audience_resolve_protocol_mapper#client_id OpenidAudienceResolveProtocolMapper#client_id}
        """
        result = self._values.get("client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_scope_id(self) -> typing.Optional[builtins.str]:
        """The mapper's associated client scope. Cannot be used at the same time as client_id.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_audience_resolve_protocol_mapper#client_scope_id OpenidAudienceResolveProtocolMapper#client_scope_id}
        """
        result = self._values.get("client_scope_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_audience_resolve_protocol_mapper#id OpenidAudienceResolveProtocolMapper#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        """A human-friendly name that will appear in the Keycloak console.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_audience_resolve_protocol_mapper#name OpenidAudienceResolveProtocolMapper#name}
        """
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpenidAudienceResolveProtocolMapperConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "OpenidAudienceResolveProtocolMapper",
    "OpenidAudienceResolveProtocolMapperConfig",
]

publication.publish()


def _typecheckingstub__2bab18d70f04d381d2245b7c90f355f5c3cb4ad01d7f47ba6daf40e48721c65a(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    realm_id: builtins.str,
    client_id: typing.Optional[builtins.str] = None,
    client_scope_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
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


def _typecheckingstub__3fbcf3ae5b1aed599e25379007603aa65ec2a0c1654aef8ca9f0ba9fdafc0b07(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__42411c19b8c1ce9b39e383325e4f4396280d3113283737e462c25b3389938fc3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__77b88ad219b0687c2f33a9ba048c8e31ccb95c53b5ece91eae90edfd1825f8f3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__80a193a12391524363119fcc64d354b8f48a259df2fa9ec48294a07ea5057775(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__793fcbbe6b7752002fa42f89facc2045933aa11faee41b7dc6be33e92acd86b0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__87d39fc1005f429ec4877b2e502389ec0d128b8be23642bb85edfb691ef0fd88(
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
    client_id: typing.Optional[builtins.str] = None,
    client_scope_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
