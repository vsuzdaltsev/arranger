"""
# `keycloak_openid_user_realm_role_protocol_mapper`

Refer to the Terraform Registory for docs: [`keycloak_openid_user_realm_role_protocol_mapper`](https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper).
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


class OpenidUserRealmRoleProtocolMapper(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.openidUserRealmRoleProtocolMapper.OpenidUserRealmRoleProtocolMapper",
):
    """Represents a {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper keycloak_openid_user_realm_role_protocol_mapper}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        claim_name: builtins.str,
        name: builtins.str,
        realm_id: builtins.str,
        add_to_access_token: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        add_to_id_token: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        add_to_userinfo: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        claim_value_type: typing.Optional[builtins.str] = None,
        client_id: typing.Optional[builtins.str] = None,
        client_scope_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        multivalued: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        realm_role_prefix: typing.Optional[builtins.str] = None,
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
        """Create a new {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper keycloak_openid_user_realm_role_protocol_mapper} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param claim_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper#claim_name OpenidUserRealmRoleProtocolMapper#claim_name}.
        :param name: A human-friendly name that will appear in the Keycloak console. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper#name OpenidUserRealmRoleProtocolMapper#name}
        :param realm_id: The realm id where the associated client or client scope exists. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper#realm_id OpenidUserRealmRoleProtocolMapper#realm_id}
        :param add_to_access_token: Indicates if the attribute should be a claim in the access token. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper#add_to_access_token OpenidUserRealmRoleProtocolMapper#add_to_access_token}
        :param add_to_id_token: Indicates if the attribute should be a claim in the id token. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper#add_to_id_token OpenidUserRealmRoleProtocolMapper#add_to_id_token}
        :param add_to_userinfo: Indicates if the attribute should appear in the userinfo response body. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper#add_to_userinfo OpenidUserRealmRoleProtocolMapper#add_to_userinfo}
        :param claim_value_type: Claim type used when serializing tokens. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper#claim_value_type OpenidUserRealmRoleProtocolMapper#claim_value_type}
        :param client_id: The mapper's associated client. Cannot be used at the same time as client_scope_id. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper#client_id OpenidUserRealmRoleProtocolMapper#client_id}
        :param client_scope_id: The mapper's associated client scope. Cannot be used at the same time as client_id. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper#client_scope_id OpenidUserRealmRoleProtocolMapper#client_scope_id}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper#id OpenidUserRealmRoleProtocolMapper#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param multivalued: Indicates whether this attribute is a single value or an array of values. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper#multivalued OpenidUserRealmRoleProtocolMapper#multivalued}
        :param realm_role_prefix: Prefix that will be added to each realm role. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper#realm_role_prefix OpenidUserRealmRoleProtocolMapper#realm_role_prefix}
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
                _typecheckingstub__5c6005a97c17003a45e3d6124d95765f379182b6f0a74c6e475e6406357e945f
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(
                argname="argument id_", value=id_, expected_type=type_hints["id_"]
            )
        config = OpenidUserRealmRoleProtocolMapperConfig(
            claim_name=claim_name,
            name=name,
            realm_id=realm_id,
            add_to_access_token=add_to_access_token,
            add_to_id_token=add_to_id_token,
            add_to_userinfo=add_to_userinfo,
            claim_value_type=claim_value_type,
            client_id=client_id,
            client_scope_id=client_scope_id,
            id=id,
            multivalued=multivalued,
            realm_role_prefix=realm_role_prefix,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetAddToAccessToken")
    def reset_add_to_access_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddToAccessToken", []))

    @jsii.member(jsii_name="resetAddToIdToken")
    def reset_add_to_id_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddToIdToken", []))

    @jsii.member(jsii_name="resetAddToUserinfo")
    def reset_add_to_userinfo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddToUserinfo", []))

    @jsii.member(jsii_name="resetClaimValueType")
    def reset_claim_value_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClaimValueType", []))

    @jsii.member(jsii_name="resetClientId")
    def reset_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientId", []))

    @jsii.member(jsii_name="resetClientScopeId")
    def reset_client_scope_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientScopeId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMultivalued")
    def reset_multivalued(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMultivalued", []))

    @jsii.member(jsii_name="resetRealmRolePrefix")
    def reset_realm_role_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRealmRolePrefix", []))

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
    @jsii.member(jsii_name="addToAccessTokenInput")
    def add_to_access_token_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "addToAccessTokenInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="addToIdTokenInput")
    def add_to_id_token_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "addToIdTokenInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="addToUserinfoInput")
    def add_to_userinfo_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "addToUserinfoInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="claimNameInput")
    def claim_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "claimNameInput")
        )

    @builtins.property
    @jsii.member(jsii_name="claimValueTypeInput")
    def claim_value_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "claimValueTypeInput")
        )

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
    @jsii.member(jsii_name="multivaluedInput")
    def multivalued_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "multivaluedInput"),
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
    @jsii.member(jsii_name="realmRolePrefixInput")
    def realm_role_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "realmRolePrefixInput")
        )

    @builtins.property
    @jsii.member(jsii_name="addToAccessToken")
    def add_to_access_token(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "addToAccessToken"),
        )

    @add_to_access_token.setter
    def add_to_access_token(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__81f4a35942cf30a12cf78b9afb2e0dc61e9b9caaf6685b8d1dbaec247517fea6
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "addToAccessToken", value)

    @builtins.property
    @jsii.member(jsii_name="addToIdToken")
    def add_to_id_token(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "addToIdToken"),
        )

    @add_to_id_token.setter
    def add_to_id_token(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a2ad906a15c78222234f7e5f9e8d6f3fbe35283e025a1f67bce186c703093340
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "addToIdToken", value)

    @builtins.property
    @jsii.member(jsii_name="addToUserinfo")
    def add_to_userinfo(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "addToUserinfo"),
        )

    @add_to_userinfo.setter
    def add_to_userinfo(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__f7e120ace52dc9ef06bd9a261b189da52b4e2a1a35a53fe92332e5f92773cb6b
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "addToUserinfo", value)

    @builtins.property
    @jsii.member(jsii_name="claimName")
    def claim_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "claimName"))

    @claim_name.setter
    def claim_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__2e538b1382adee692ba606594447058b915580c900a75aec0da912e187cbe0de
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "claimName", value)

    @builtins.property
    @jsii.member(jsii_name="claimValueType")
    def claim_value_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "claimValueType"))

    @claim_value_type.setter
    def claim_value_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__6615983b412f2b83856333e1c87594ee24c5098ca4feba3cc0de3c4320b3dd1f
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "claimValueType", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a27d971bf328fe559431552d8f4b3d68f09c6f9a1b303094837049c9d0ec0433
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
                _typecheckingstub__df118b5c4fffd8b35f5a9e213cd1edd6220c7d7a27a5223d29599afc0161ebf2
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
                _typecheckingstub__3ee0c6a0bb6417eea8a5ad477393da5d8d8b867ff7919f4047b5d6f93a042cf3
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="multivalued")
    def multivalued(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "multivalued"),
        )

    @multivalued.setter
    def multivalued(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__1a197ef6f8fa2c6544c9522355388fb3ef56a698f13cf49683afeea81d17d810
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "multivalued", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__61cc992c3aa54eb9a39cacd8ed0e3d7c50884aa29a0caed0597297b0ebf62f53
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
                _typecheckingstub__fe1e00bea726577e9842c92b5b572075a1fedffb1c32a1fc3a54d9604b7e87b8
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "realmId", value)

    @builtins.property
    @jsii.member(jsii_name="realmRolePrefix")
    def realm_role_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "realmRolePrefix"))

    @realm_role_prefix.setter
    def realm_role_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__f0349ee82408dc556f54690a01f0c9121cb1dd37b8a4b1d7eb89e2fea0f4ce05
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "realmRolePrefix", value)


@jsii.data_type(
    jsii_type="keycloak.openidUserRealmRoleProtocolMapper.OpenidUserRealmRoleProtocolMapperConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "claim_name": "claimName",
        "name": "name",
        "realm_id": "realmId",
        "add_to_access_token": "addToAccessToken",
        "add_to_id_token": "addToIdToken",
        "add_to_userinfo": "addToUserinfo",
        "claim_value_type": "claimValueType",
        "client_id": "clientId",
        "client_scope_id": "clientScopeId",
        "id": "id",
        "multivalued": "multivalued",
        "realm_role_prefix": "realmRolePrefix",
    },
)
class OpenidUserRealmRoleProtocolMapperConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        claim_name: builtins.str,
        name: builtins.str,
        realm_id: builtins.str,
        add_to_access_token: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        add_to_id_token: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        add_to_userinfo: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        claim_value_type: typing.Optional[builtins.str] = None,
        client_id: typing.Optional[builtins.str] = None,
        client_scope_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        multivalued: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        realm_role_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param connection:
        :param count:
        :param depends_on:
        :param for_each:
        :param lifecycle:
        :param provider:
        :param provisioners:
        :param claim_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper#claim_name OpenidUserRealmRoleProtocolMapper#claim_name}.
        :param name: A human-friendly name that will appear in the Keycloak console. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper#name OpenidUserRealmRoleProtocolMapper#name}
        :param realm_id: The realm id where the associated client or client scope exists. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper#realm_id OpenidUserRealmRoleProtocolMapper#realm_id}
        :param add_to_access_token: Indicates if the attribute should be a claim in the access token. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper#add_to_access_token OpenidUserRealmRoleProtocolMapper#add_to_access_token}
        :param add_to_id_token: Indicates if the attribute should be a claim in the id token. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper#add_to_id_token OpenidUserRealmRoleProtocolMapper#add_to_id_token}
        :param add_to_userinfo: Indicates if the attribute should appear in the userinfo response body. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper#add_to_userinfo OpenidUserRealmRoleProtocolMapper#add_to_userinfo}
        :param claim_value_type: Claim type used when serializing tokens. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper#claim_value_type OpenidUserRealmRoleProtocolMapper#claim_value_type}
        :param client_id: The mapper's associated client. Cannot be used at the same time as client_scope_id. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper#client_id OpenidUserRealmRoleProtocolMapper#client_id}
        :param client_scope_id: The mapper's associated client scope. Cannot be used at the same time as client_id. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper#client_scope_id OpenidUserRealmRoleProtocolMapper#client_scope_id}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper#id OpenidUserRealmRoleProtocolMapper#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param multivalued: Indicates whether this attribute is a single value or an array of values. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper#multivalued OpenidUserRealmRoleProtocolMapper#multivalued}
        :param realm_role_prefix: Prefix that will be added to each realm role. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper#realm_role_prefix OpenidUserRealmRoleProtocolMapper#realm_role_prefix}
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__c524a264b79323bbfd2d52c17b986826e525e2a91ff0329f0d047ed4c95f00a7
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
                argname="argument claim_name",
                value=claim_name,
                expected_type=type_hints["claim_name"],
            )
            check_type(
                argname="argument name", value=name, expected_type=type_hints["name"]
            )
            check_type(
                argname="argument realm_id",
                value=realm_id,
                expected_type=type_hints["realm_id"],
            )
            check_type(
                argname="argument add_to_access_token",
                value=add_to_access_token,
                expected_type=type_hints["add_to_access_token"],
            )
            check_type(
                argname="argument add_to_id_token",
                value=add_to_id_token,
                expected_type=type_hints["add_to_id_token"],
            )
            check_type(
                argname="argument add_to_userinfo",
                value=add_to_userinfo,
                expected_type=type_hints["add_to_userinfo"],
            )
            check_type(
                argname="argument claim_value_type",
                value=claim_value_type,
                expected_type=type_hints["claim_value_type"],
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
                argname="argument multivalued",
                value=multivalued,
                expected_type=type_hints["multivalued"],
            )
            check_type(
                argname="argument realm_role_prefix",
                value=realm_role_prefix,
                expected_type=type_hints["realm_role_prefix"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "claim_name": claim_name,
            "name": name,
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
        if add_to_access_token is not None:
            self._values["add_to_access_token"] = add_to_access_token
        if add_to_id_token is not None:
            self._values["add_to_id_token"] = add_to_id_token
        if add_to_userinfo is not None:
            self._values["add_to_userinfo"] = add_to_userinfo
        if claim_value_type is not None:
            self._values["claim_value_type"] = claim_value_type
        if client_id is not None:
            self._values["client_id"] = client_id
        if client_scope_id is not None:
            self._values["client_scope_id"] = client_scope_id
        if id is not None:
            self._values["id"] = id
        if multivalued is not None:
            self._values["multivalued"] = multivalued
        if realm_role_prefix is not None:
            self._values["realm_role_prefix"] = realm_role_prefix

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
    def claim_name(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper#claim_name OpenidUserRealmRoleProtocolMapper#claim_name}."""
        result = self._values.get("claim_name")
        assert result is not None, "Required property 'claim_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        """A human-friendly name that will appear in the Keycloak console.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper#name OpenidUserRealmRoleProtocolMapper#name}
        """
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def realm_id(self) -> builtins.str:
        """The realm id where the associated client or client scope exists.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper#realm_id OpenidUserRealmRoleProtocolMapper#realm_id}
        """
        result = self._values.get("realm_id")
        assert result is not None, "Required property 'realm_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def add_to_access_token(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Indicates if the attribute should be a claim in the access token.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper#add_to_access_token OpenidUserRealmRoleProtocolMapper#add_to_access_token}
        """
        result = self._values.get("add_to_access_token")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def add_to_id_token(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Indicates if the attribute should be a claim in the id token.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper#add_to_id_token OpenidUserRealmRoleProtocolMapper#add_to_id_token}
        """
        result = self._values.get("add_to_id_token")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def add_to_userinfo(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Indicates if the attribute should appear in the userinfo response body.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper#add_to_userinfo OpenidUserRealmRoleProtocolMapper#add_to_userinfo}
        """
        result = self._values.get("add_to_userinfo")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def claim_value_type(self) -> typing.Optional[builtins.str]:
        """Claim type used when serializing tokens.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper#claim_value_type OpenidUserRealmRoleProtocolMapper#claim_value_type}
        """
        result = self._values.get("claim_value_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_id(self) -> typing.Optional[builtins.str]:
        """The mapper's associated client. Cannot be used at the same time as client_scope_id.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper#client_id OpenidUserRealmRoleProtocolMapper#client_id}
        """
        result = self._values.get("client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_scope_id(self) -> typing.Optional[builtins.str]:
        """The mapper's associated client scope. Cannot be used at the same time as client_id.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper#client_scope_id OpenidUserRealmRoleProtocolMapper#client_scope_id}
        """
        result = self._values.get("client_scope_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper#id OpenidUserRealmRoleProtocolMapper#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def multivalued(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Indicates whether this attribute is a single value or an array of values.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper#multivalued OpenidUserRealmRoleProtocolMapper#multivalued}
        """
        result = self._values.get("multivalued")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def realm_role_prefix(self) -> typing.Optional[builtins.str]:
        """Prefix that will be added to each realm role.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_user_realm_role_protocol_mapper#realm_role_prefix OpenidUserRealmRoleProtocolMapper#realm_role_prefix}
        """
        result = self._values.get("realm_role_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpenidUserRealmRoleProtocolMapperConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "OpenidUserRealmRoleProtocolMapper",
    "OpenidUserRealmRoleProtocolMapperConfig",
]

publication.publish()


def _typecheckingstub__5c6005a97c17003a45e3d6124d95765f379182b6f0a74c6e475e6406357e945f(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    claim_name: builtins.str,
    name: builtins.str,
    realm_id: builtins.str,
    add_to_access_token: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    add_to_id_token: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    add_to_userinfo: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    claim_value_type: typing.Optional[builtins.str] = None,
    client_id: typing.Optional[builtins.str] = None,
    client_scope_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    multivalued: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    realm_role_prefix: typing.Optional[builtins.str] = None,
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


def _typecheckingstub__81f4a35942cf30a12cf78b9afb2e0dc61e9b9caaf6685b8d1dbaec247517fea6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a2ad906a15c78222234f7e5f9e8d6f3fbe35283e025a1f67bce186c703093340(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f7e120ace52dc9ef06bd9a261b189da52b4e2a1a35a53fe92332e5f92773cb6b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__2e538b1382adee692ba606594447058b915580c900a75aec0da912e187cbe0de(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6615983b412f2b83856333e1c87594ee24c5098ca4feba3cc0de3c4320b3dd1f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a27d971bf328fe559431552d8f4b3d68f09c6f9a1b303094837049c9d0ec0433(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__df118b5c4fffd8b35f5a9e213cd1edd6220c7d7a27a5223d29599afc0161ebf2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3ee0c6a0bb6417eea8a5ad477393da5d8d8b867ff7919f4047b5d6f93a042cf3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1a197ef6f8fa2c6544c9522355388fb3ef56a698f13cf49683afeea81d17d810(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__61cc992c3aa54eb9a39cacd8ed0e3d7c50884aa29a0caed0597297b0ebf62f53(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__fe1e00bea726577e9842c92b5b572075a1fedffb1c32a1fc3a54d9604b7e87b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f0349ee82408dc556f54690a01f0c9121cb1dd37b8a4b1d7eb89e2fea0f4ce05(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c524a264b79323bbfd2d52c17b986826e525e2a91ff0329f0d047ed4c95f00a7(
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
    claim_name: builtins.str,
    name: builtins.str,
    realm_id: builtins.str,
    add_to_access_token: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    add_to_id_token: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    add_to_userinfo: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    claim_value_type: typing.Optional[builtins.str] = None,
    client_id: typing.Optional[builtins.str] = None,
    client_scope_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    multivalued: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    realm_role_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
