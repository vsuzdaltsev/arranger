"""
# `keycloak_attribute_to_role_identity_provider_mapper`

Refer to the Terraform Registory for docs: [`keycloak_attribute_to_role_identity_provider_mapper`](https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_to_role_identity_provider_mapper).
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


class AttributeToRoleIdentityProviderMapper(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.attributeToRoleIdentityProviderMapper.AttributeToRoleIdentityProviderMapper",
):
    """Represents a {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_to_role_identity_provider_mapper keycloak_attribute_to_role_identity_provider_mapper}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        identity_provider_alias: builtins.str,
        name: builtins.str,
        realm: builtins.str,
        role: builtins.str,
        attribute_friendly_name: typing.Optional[builtins.str] = None,
        attribute_name: typing.Optional[builtins.str] = None,
        attribute_value: typing.Optional[builtins.str] = None,
        claim_name: typing.Optional[builtins.str] = None,
        claim_value: typing.Optional[builtins.str] = None,
        extra_config: typing.Optional[
            typing.Mapping[builtins.str, builtins.str]
        ] = None,
        id: typing.Optional[builtins.str] = None,
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
        """Create a new {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_to_role_identity_provider_mapper keycloak_attribute_to_role_identity_provider_mapper} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param identity_provider_alias: IDP Alias. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_to_role_identity_provider_mapper#identity_provider_alias AttributeToRoleIdentityProviderMapper#identity_provider_alias}
        :param name: IDP Mapper Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_to_role_identity_provider_mapper#name AttributeToRoleIdentityProviderMapper#name}
        :param realm: Realm Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_to_role_identity_provider_mapper#realm AttributeToRoleIdentityProviderMapper#realm}
        :param role: Role Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_to_role_identity_provider_mapper#role AttributeToRoleIdentityProviderMapper#role}
        :param attribute_friendly_name: Attribute Friendly Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_to_role_identity_provider_mapper#attribute_friendly_name AttributeToRoleIdentityProviderMapper#attribute_friendly_name}
        :param attribute_name: Attribute Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_to_role_identity_provider_mapper#attribute_name AttributeToRoleIdentityProviderMapper#attribute_name}
        :param attribute_value: Attribute Value. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_to_role_identity_provider_mapper#attribute_value AttributeToRoleIdentityProviderMapper#attribute_value}
        :param claim_name: OIDC Claim Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_to_role_identity_provider_mapper#claim_name AttributeToRoleIdentityProviderMapper#claim_name}
        :param claim_value: OIDC Claim Value. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_to_role_identity_provider_mapper#claim_value AttributeToRoleIdentityProviderMapper#claim_value}
        :param extra_config: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_to_role_identity_provider_mapper#extra_config AttributeToRoleIdentityProviderMapper#extra_config}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_to_role_identity_provider_mapper#id AttributeToRoleIdentityProviderMapper#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
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
                _typecheckingstub__85f109c6921c191447285a15690d4aa42fe581c550dbc2f3074a2be18bf56d64
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(
                argname="argument id_", value=id_, expected_type=type_hints["id_"]
            )
        config = AttributeToRoleIdentityProviderMapperConfig(
            identity_provider_alias=identity_provider_alias,
            name=name,
            realm=realm,
            role=role,
            attribute_friendly_name=attribute_friendly_name,
            attribute_name=attribute_name,
            attribute_value=attribute_value,
            claim_name=claim_name,
            claim_value=claim_value,
            extra_config=extra_config,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetAttributeFriendlyName")
    def reset_attribute_friendly_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttributeFriendlyName", []))

    @jsii.member(jsii_name="resetAttributeName")
    def reset_attribute_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttributeName", []))

    @jsii.member(jsii_name="resetAttributeValue")
    def reset_attribute_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttributeValue", []))

    @jsii.member(jsii_name="resetClaimName")
    def reset_claim_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClaimName", []))

    @jsii.member(jsii_name="resetClaimValue")
    def reset_claim_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClaimValue", []))

    @jsii.member(jsii_name="resetExtraConfig")
    def reset_extra_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtraConfig", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    @jsii.member(jsii_name="attributeFriendlyNameInput")
    def attribute_friendly_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "attributeFriendlyNameInput")
        )

    @builtins.property
    @jsii.member(jsii_name="attributeNameInput")
    def attribute_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "attributeNameInput")
        )

    @builtins.property
    @jsii.member(jsii_name="attributeValueInput")
    def attribute_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "attributeValueInput")
        )

    @builtins.property
    @jsii.member(jsii_name="claimNameInput")
    def claim_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "claimNameInput")
        )

    @builtins.property
    @jsii.member(jsii_name="claimValueInput")
    def claim_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "claimValueInput")
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
    @jsii.member(jsii_name="identityProviderAliasInput")
    def identity_provider_alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "identityProviderAliasInput")
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
    @jsii.member(jsii_name="realmInput")
    def realm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "realmInput"))

    @builtins.property
    @jsii.member(jsii_name="roleInput")
    def role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleInput"))

    @builtins.property
    @jsii.member(jsii_name="attributeFriendlyName")
    def attribute_friendly_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attributeFriendlyName"))

    @attribute_friendly_name.setter
    def attribute_friendly_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__f3769caa271dc3f48b2b342839cb6429e335f9ba9ef6b72205d88fa8f74e6a6f
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "attributeFriendlyName", value)

    @builtins.property
    @jsii.member(jsii_name="attributeName")
    def attribute_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attributeName"))

    @attribute_name.setter
    def attribute_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__47884a32eafb27f1193d7b9a3a87f8ac834d994214fd5723568334e0897d387f
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "attributeName", value)

    @builtins.property
    @jsii.member(jsii_name="attributeValue")
    def attribute_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attributeValue"))

    @attribute_value.setter
    def attribute_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__1414eacb10326045f0dba365fb28134994ea72d112e0294ffac909cc335d44e5
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "attributeValue", value)

    @builtins.property
    @jsii.member(jsii_name="claimName")
    def claim_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "claimName"))

    @claim_name.setter
    def claim_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__6a5d3dbd8c489af41728b9af8b2cf0037e434d8ca978fd3f34329381f5d51015
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "claimName", value)

    @builtins.property
    @jsii.member(jsii_name="claimValue")
    def claim_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "claimValue"))

    @claim_value.setter
    def claim_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__39c53640fccbcf54385f74ede36453f12220be2801ae588558099907b74e1431
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "claimValue", value)

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
                _typecheckingstub__3b6db20d0e347fa34e930db6558ecf96a057fcf91b4d70977c619234858d3913
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
                _typecheckingstub__59d1f4196cc67bb3ba1cdeef0c5a1974db27da5a5abf3d6f26615dc5f1912f17
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="identityProviderAlias")
    def identity_provider_alias(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityProviderAlias"))

    @identity_provider_alias.setter
    def identity_provider_alias(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__be060e714f1c5c994c11055f0371e93d28324b324a583672b224780e06385eb2
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "identityProviderAlias", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__c4d7a5e967299926f910281b73f9ef0ea4d55943c429c9c320fcda197275d642
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="realm")
    def realm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "realm"))

    @realm.setter
    def realm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__4f069125de36c6510b0841d002a65bcd24f7e3fa321f42c68afc007dfae87ca3
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "realm", value)

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @role.setter
    def role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__4709f55adb0ccc8db257544d1152594b114e4cbc64baf6c579bfa85ec51e9366
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "role", value)


@jsii.data_type(
    jsii_type="keycloak.attributeToRoleIdentityProviderMapper.AttributeToRoleIdentityProviderMapperConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "identity_provider_alias": "identityProviderAlias",
        "name": "name",
        "realm": "realm",
        "role": "role",
        "attribute_friendly_name": "attributeFriendlyName",
        "attribute_name": "attributeName",
        "attribute_value": "attributeValue",
        "claim_name": "claimName",
        "claim_value": "claimValue",
        "extra_config": "extraConfig",
        "id": "id",
    },
)
class AttributeToRoleIdentityProviderMapperConfig(
    _cdktf_9a9027ec.TerraformMetaArguments,
):
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
        identity_provider_alias: builtins.str,
        name: builtins.str,
        realm: builtins.str,
        role: builtins.str,
        attribute_friendly_name: typing.Optional[builtins.str] = None,
        attribute_name: typing.Optional[builtins.str] = None,
        attribute_value: typing.Optional[builtins.str] = None,
        claim_name: typing.Optional[builtins.str] = None,
        claim_value: typing.Optional[builtins.str] = None,
        extra_config: typing.Optional[
            typing.Mapping[builtins.str, builtins.str]
        ] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param connection:
        :param count:
        :param depends_on:
        :param for_each:
        :param lifecycle:
        :param provider:
        :param provisioners:
        :param identity_provider_alias: IDP Alias. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_to_role_identity_provider_mapper#identity_provider_alias AttributeToRoleIdentityProviderMapper#identity_provider_alias}
        :param name: IDP Mapper Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_to_role_identity_provider_mapper#name AttributeToRoleIdentityProviderMapper#name}
        :param realm: Realm Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_to_role_identity_provider_mapper#realm AttributeToRoleIdentityProviderMapper#realm}
        :param role: Role Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_to_role_identity_provider_mapper#role AttributeToRoleIdentityProviderMapper#role}
        :param attribute_friendly_name: Attribute Friendly Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_to_role_identity_provider_mapper#attribute_friendly_name AttributeToRoleIdentityProviderMapper#attribute_friendly_name}
        :param attribute_name: Attribute Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_to_role_identity_provider_mapper#attribute_name AttributeToRoleIdentityProviderMapper#attribute_name}
        :param attribute_value: Attribute Value. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_to_role_identity_provider_mapper#attribute_value AttributeToRoleIdentityProviderMapper#attribute_value}
        :param claim_name: OIDC Claim Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_to_role_identity_provider_mapper#claim_name AttributeToRoleIdentityProviderMapper#claim_name}
        :param claim_value: OIDC Claim Value. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_to_role_identity_provider_mapper#claim_value AttributeToRoleIdentityProviderMapper#claim_value}
        :param extra_config: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_to_role_identity_provider_mapper#extra_config AttributeToRoleIdentityProviderMapper#extra_config}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_to_role_identity_provider_mapper#id AttributeToRoleIdentityProviderMapper#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__0c56f17d24cd32fe421df706ef61fcea8ed6712e82e885f02ae873490380e271
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
                argname="argument identity_provider_alias",
                value=identity_provider_alias,
                expected_type=type_hints["identity_provider_alias"],
            )
            check_type(
                argname="argument name", value=name, expected_type=type_hints["name"]
            )
            check_type(
                argname="argument realm", value=realm, expected_type=type_hints["realm"]
            )
            check_type(
                argname="argument role", value=role, expected_type=type_hints["role"]
            )
            check_type(
                argname="argument attribute_friendly_name",
                value=attribute_friendly_name,
                expected_type=type_hints["attribute_friendly_name"],
            )
            check_type(
                argname="argument attribute_name",
                value=attribute_name,
                expected_type=type_hints["attribute_name"],
            )
            check_type(
                argname="argument attribute_value",
                value=attribute_value,
                expected_type=type_hints["attribute_value"],
            )
            check_type(
                argname="argument claim_name",
                value=claim_name,
                expected_type=type_hints["claim_name"],
            )
            check_type(
                argname="argument claim_value",
                value=claim_value,
                expected_type=type_hints["claim_value"],
            )
            check_type(
                argname="argument extra_config",
                value=extra_config,
                expected_type=type_hints["extra_config"],
            )
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "identity_provider_alias": identity_provider_alias,
            "name": name,
            "realm": realm,
            "role": role,
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
        if attribute_friendly_name is not None:
            self._values["attribute_friendly_name"] = attribute_friendly_name
        if attribute_name is not None:
            self._values["attribute_name"] = attribute_name
        if attribute_value is not None:
            self._values["attribute_value"] = attribute_value
        if claim_name is not None:
            self._values["claim_name"] = claim_name
        if claim_value is not None:
            self._values["claim_value"] = claim_value
        if extra_config is not None:
            self._values["extra_config"] = extra_config
        if id is not None:
            self._values["id"] = id

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
    def identity_provider_alias(self) -> builtins.str:
        """IDP Alias.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_to_role_identity_provider_mapper#identity_provider_alias AttributeToRoleIdentityProviderMapper#identity_provider_alias}
        """
        result = self._values.get("identity_provider_alias")
        assert (
            result is not None
        ), "Required property 'identity_provider_alias' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        """IDP Mapper Name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_to_role_identity_provider_mapper#name AttributeToRoleIdentityProviderMapper#name}
        """
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def realm(self) -> builtins.str:
        """Realm Name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_to_role_identity_provider_mapper#realm AttributeToRoleIdentityProviderMapper#realm}
        """
        result = self._values.get("realm")
        assert result is not None, "Required property 'realm' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role(self) -> builtins.str:
        """Role Name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_to_role_identity_provider_mapper#role AttributeToRoleIdentityProviderMapper#role}
        """
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attribute_friendly_name(self) -> typing.Optional[builtins.str]:
        """Attribute Friendly Name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_to_role_identity_provider_mapper#attribute_friendly_name AttributeToRoleIdentityProviderMapper#attribute_friendly_name}
        """
        result = self._values.get("attribute_friendly_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def attribute_name(self) -> typing.Optional[builtins.str]:
        """Attribute Name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_to_role_identity_provider_mapper#attribute_name AttributeToRoleIdentityProviderMapper#attribute_name}
        """
        result = self._values.get("attribute_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def attribute_value(self) -> typing.Optional[builtins.str]:
        """Attribute Value.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_to_role_identity_provider_mapper#attribute_value AttributeToRoleIdentityProviderMapper#attribute_value}
        """
        result = self._values.get("attribute_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def claim_name(self) -> typing.Optional[builtins.str]:
        """OIDC Claim Name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_to_role_identity_provider_mapper#claim_name AttributeToRoleIdentityProviderMapper#claim_name}
        """
        result = self._values.get("claim_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def claim_value(self) -> typing.Optional[builtins.str]:
        """OIDC Claim Value.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_to_role_identity_provider_mapper#claim_value AttributeToRoleIdentityProviderMapper#claim_value}
        """
        result = self._values.get("claim_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extra_config(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_to_role_identity_provider_mapper#extra_config AttributeToRoleIdentityProviderMapper#extra_config}."""
        result = self._values.get("extra_config")
        return typing.cast(
            typing.Optional[typing.Mapping[builtins.str, builtins.str]], result
        )

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_to_role_identity_provider_mapper#id AttributeToRoleIdentityProviderMapper#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AttributeToRoleIdentityProviderMapperConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AttributeToRoleIdentityProviderMapper",
    "AttributeToRoleIdentityProviderMapperConfig",
]

publication.publish()


def _typecheckingstub__85f109c6921c191447285a15690d4aa42fe581c550dbc2f3074a2be18bf56d64(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    identity_provider_alias: builtins.str,
    name: builtins.str,
    realm: builtins.str,
    role: builtins.str,
    attribute_friendly_name: typing.Optional[builtins.str] = None,
    attribute_name: typing.Optional[builtins.str] = None,
    attribute_value: typing.Optional[builtins.str] = None,
    claim_name: typing.Optional[builtins.str] = None,
    claim_value: typing.Optional[builtins.str] = None,
    extra_config: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    id: typing.Optional[builtins.str] = None,
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


def _typecheckingstub__f3769caa271dc3f48b2b342839cb6429e335f9ba9ef6b72205d88fa8f74e6a6f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__47884a32eafb27f1193d7b9a3a87f8ac834d994214fd5723568334e0897d387f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1414eacb10326045f0dba365fb28134994ea72d112e0294ffac909cc335d44e5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6a5d3dbd8c489af41728b9af8b2cf0037e434d8ca978fd3f34329381f5d51015(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__39c53640fccbcf54385f74ede36453f12220be2801ae588558099907b74e1431(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3b6db20d0e347fa34e930db6558ecf96a057fcf91b4d70977c619234858d3913(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__59d1f4196cc67bb3ba1cdeef0c5a1974db27da5a5abf3d6f26615dc5f1912f17(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__be060e714f1c5c994c11055f0371e93d28324b324a583672b224780e06385eb2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c4d7a5e967299926f910281b73f9ef0ea4d55943c429c9c320fcda197275d642(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4f069125de36c6510b0841d002a65bcd24f7e3fa321f42c68afc007dfae87ca3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4709f55adb0ccc8db257544d1152594b114e4cbc64baf6c579bfa85ec51e9366(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0c56f17d24cd32fe421df706ef61fcea8ed6712e82e885f02ae873490380e271(
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
    identity_provider_alias: builtins.str,
    name: builtins.str,
    realm: builtins.str,
    role: builtins.str,
    attribute_friendly_name: typing.Optional[builtins.str] = None,
    attribute_name: typing.Optional[builtins.str] = None,
    attribute_value: typing.Optional[builtins.str] = None,
    claim_name: typing.Optional[builtins.str] = None,
    claim_value: typing.Optional[builtins.str] = None,
    extra_config: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
