"""
# `keycloak_ldap_role_mapper`

Refer to the Terraform Registory for docs: [`keycloak_ldap_role_mapper`](https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper).
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


class LdapRoleMapper(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.ldapRoleMapper.LdapRoleMapper",
):
    """Represents a {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper keycloak_ldap_role_mapper}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        ldap_roles_dn: builtins.str,
        ldap_user_federation_id: builtins.str,
        membership_ldap_attribute: builtins.str,
        membership_user_ldap_attribute: builtins.str,
        name: builtins.str,
        realm_id: builtins.str,
        role_name_ldap_attribute: builtins.str,
        role_object_classes: typing.Sequence[builtins.str],
        client_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        memberof_ldap_attribute: typing.Optional[builtins.str] = None,
        membership_attribute_type: typing.Optional[builtins.str] = None,
        mode: typing.Optional[builtins.str] = None,
        roles_ldap_filter: typing.Optional[builtins.str] = None,
        use_realm_roles_mapping: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        user_roles_retrieve_strategy: typing.Optional[builtins.str] = None,
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
        """Create a new {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper keycloak_ldap_role_mapper} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param ldap_roles_dn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#ldap_roles_dn LdapRoleMapper#ldap_roles_dn}.
        :param ldap_user_federation_id: The ldap user federation provider to attach this mapper to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#ldap_user_federation_id LdapRoleMapper#ldap_user_federation_id}
        :param membership_ldap_attribute: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#membership_ldap_attribute LdapRoleMapper#membership_ldap_attribute}.
        :param membership_user_ldap_attribute: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#membership_user_ldap_attribute LdapRoleMapper#membership_user_ldap_attribute}.
        :param name: Display name of the mapper when displayed in the console. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#name LdapRoleMapper#name}
        :param realm_id: The realm in which the ldap user federation provider exists. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#realm_id LdapRoleMapper#realm_id}
        :param role_name_ldap_attribute: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#role_name_ldap_attribute LdapRoleMapper#role_name_ldap_attribute}.
        :param role_object_classes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#role_object_classes LdapRoleMapper#role_object_classes}.
        :param client_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#client_id LdapRoleMapper#client_id}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#id LdapRoleMapper#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param memberof_ldap_attribute: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#memberof_ldap_attribute LdapRoleMapper#memberof_ldap_attribute}.
        :param membership_attribute_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#membership_attribute_type LdapRoleMapper#membership_attribute_type}.
        :param mode: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#mode LdapRoleMapper#mode}.
        :param roles_ldap_filter: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#roles_ldap_filter LdapRoleMapper#roles_ldap_filter}.
        :param use_realm_roles_mapping: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#use_realm_roles_mapping LdapRoleMapper#use_realm_roles_mapping}.
        :param user_roles_retrieve_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#user_roles_retrieve_strategy LdapRoleMapper#user_roles_retrieve_strategy}.
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
                _typecheckingstub__58e794209f56c731d7e06981fec386808f6e5f5f95f9901a828cae7f5341b097
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(
                argname="argument id_", value=id_, expected_type=type_hints["id_"]
            )
        config = LdapRoleMapperConfig(
            ldap_roles_dn=ldap_roles_dn,
            ldap_user_federation_id=ldap_user_federation_id,
            membership_ldap_attribute=membership_ldap_attribute,
            membership_user_ldap_attribute=membership_user_ldap_attribute,
            name=name,
            realm_id=realm_id,
            role_name_ldap_attribute=role_name_ldap_attribute,
            role_object_classes=role_object_classes,
            client_id=client_id,
            id=id,
            memberof_ldap_attribute=memberof_ldap_attribute,
            membership_attribute_type=membership_attribute_type,
            mode=mode,
            roles_ldap_filter=roles_ldap_filter,
            use_realm_roles_mapping=use_realm_roles_mapping,
            user_roles_retrieve_strategy=user_roles_retrieve_strategy,
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

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMemberofLdapAttribute")
    def reset_memberof_ldap_attribute(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemberofLdapAttribute", []))

    @jsii.member(jsii_name="resetMembershipAttributeType")
    def reset_membership_attribute_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMembershipAttributeType", []))

    @jsii.member(jsii_name="resetMode")
    def reset_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMode", []))

    @jsii.member(jsii_name="resetRolesLdapFilter")
    def reset_roles_ldap_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRolesLdapFilter", []))

    @jsii.member(jsii_name="resetUseRealmRolesMapping")
    def reset_use_realm_roles_mapping(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseRealmRolesMapping", []))

    @jsii.member(jsii_name="resetUserRolesRetrieveStrategy")
    def reset_user_roles_retrieve_strategy(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetUserRolesRetrieveStrategy", [])
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
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "clientIdInput")
        )

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ldapRolesDnInput")
    def ldap_roles_dn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "ldapRolesDnInput")
        )

    @builtins.property
    @jsii.member(jsii_name="ldapUserFederationIdInput")
    def ldap_user_federation_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "ldapUserFederationIdInput")
        )

    @builtins.property
    @jsii.member(jsii_name="memberofLdapAttributeInput")
    def memberof_ldap_attribute_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "memberofLdapAttributeInput")
        )

    @builtins.property
    @jsii.member(jsii_name="membershipAttributeTypeInput")
    def membership_attribute_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "membershipAttributeTypeInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="membershipLdapAttributeInput")
    def membership_ldap_attribute_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "membershipLdapAttributeInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="membershipUserLdapAttributeInput")
    def membership_user_ldap_attribute_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "membershipUserLdapAttributeInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

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
    @jsii.member(jsii_name="roleNameLdapAttributeInput")
    def role_name_ldap_attribute_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "roleNameLdapAttributeInput")
        )

    @builtins.property
    @jsii.member(jsii_name="roleObjectClassesInput")
    def role_object_classes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]],
            jsii.get(self, "roleObjectClassesInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="rolesLdapFilterInput")
    def roles_ldap_filter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "rolesLdapFilterInput")
        )

    @builtins.property
    @jsii.member(jsii_name="useRealmRolesMappingInput")
    def use_realm_roles_mapping_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "useRealmRolesMappingInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="userRolesRetrieveStrategyInput")
    def user_roles_retrieve_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "userRolesRetrieveStrategyInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__35f792ba9d38fbf9f45b133df6af310a121253361da4000cf5ffe80d87f92ed1
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__3dd7247474738a7c571123f6097a9cc249ad299fe1a7bde24deef786084bd2f7
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ldapRolesDn")
    def ldap_roles_dn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ldapRolesDn"))

    @ldap_roles_dn.setter
    def ldap_roles_dn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__8c4fb80c2ff0ac699bf5ccf322dc4ea8c8a82add2d6942e1b01dff431d62ff84
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "ldapRolesDn", value)

    @builtins.property
    @jsii.member(jsii_name="ldapUserFederationId")
    def ldap_user_federation_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ldapUserFederationId"))

    @ldap_user_federation_id.setter
    def ldap_user_federation_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__5a653795a9f38ac2789d6d0e67418ecee50ee6114973d3fecb8772a218e238af
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "ldapUserFederationId", value)

    @builtins.property
    @jsii.member(jsii_name="memberofLdapAttribute")
    def memberof_ldap_attribute(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "memberofLdapAttribute"))

    @memberof_ldap_attribute.setter
    def memberof_ldap_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d32abb01988bae45562dacb1969621bbc735a12f440adebfb3f07555faabbe66
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "memberofLdapAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="membershipAttributeType")
    def membership_attribute_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "membershipAttributeType"))

    @membership_attribute_type.setter
    def membership_attribute_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__13fa66e5fbe8052c2bd389d0ffcc5eaac082d6e21f1197a946563a004f3719e9
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "membershipAttributeType", value)

    @builtins.property
    @jsii.member(jsii_name="membershipLdapAttribute")
    def membership_ldap_attribute(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "membershipLdapAttribute"))

    @membership_ldap_attribute.setter
    def membership_ldap_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d815f829fb31bb9d2135e508ddb834b3b2d64183fa08a5e8216c5768c0521cf2
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "membershipLdapAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="membershipUserLdapAttribute")
    def membership_user_ldap_attribute(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "membershipUserLdapAttribute"))

    @membership_user_ldap_attribute.setter
    def membership_user_ldap_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__7889902c919f6ae49e3a0cb261a3cb1074c328ce433d6cac210e69c5cb5575c3
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "membershipUserLdapAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__8526e041ed7533690146d86bdbe654e0a2cb83e2f3d55c1b0b24dfeb5abdd25e
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__13a1cfd3c62058896f68804c91780da339b0048d412eab2dca5844f90a497f13
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
                _typecheckingstub__145726753519eb75e71c7650f1ec491132d3e77411b9a151433cc0df7407216d
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "realmId", value)

    @builtins.property
    @jsii.member(jsii_name="roleNameLdapAttribute")
    def role_name_ldap_attribute(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleNameLdapAttribute"))

    @role_name_ldap_attribute.setter
    def role_name_ldap_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b8f2a9284a71a9281eb4a6f8f4745b9502b3232c5e49480d5ab7e37587130559
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "roleNameLdapAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="roleObjectClasses")
    def role_object_classes(self) -> typing.List[builtins.str]:
        return typing.cast(
            typing.List[builtins.str], jsii.get(self, "roleObjectClasses")
        )

    @role_object_classes.setter
    def role_object_classes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a8378011b135d31794850b6c35b0048f7b4089ef6184d6fd98bd4f25c5598ce6
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "roleObjectClasses", value)

    @builtins.property
    @jsii.member(jsii_name="rolesLdapFilter")
    def roles_ldap_filter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rolesLdapFilter"))

    @roles_ldap_filter.setter
    def roles_ldap_filter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__68bc9ce1109f4d526c66df5542cb41bfed3f090abdce983b4535b6c988bbb764
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "rolesLdapFilter", value)

    @builtins.property
    @jsii.member(jsii_name="useRealmRolesMapping")
    def use_realm_roles_mapping(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "useRealmRolesMapping"),
        )

    @use_realm_roles_mapping.setter
    def use_realm_roles_mapping(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__294ec256e68b77bad2c7c2c76fa45189d000d454833b8602af6412b0032c2659
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "useRealmRolesMapping", value)

    @builtins.property
    @jsii.member(jsii_name="userRolesRetrieveStrategy")
    def user_roles_retrieve_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userRolesRetrieveStrategy"))

    @user_roles_retrieve_strategy.setter
    def user_roles_retrieve_strategy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a09343e296a32f672e94a69d1eaded3db73ed2de0175f502251a4596371d22dc
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "userRolesRetrieveStrategy", value)


@jsii.data_type(
    jsii_type="keycloak.ldapRoleMapper.LdapRoleMapperConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "ldap_roles_dn": "ldapRolesDn",
        "ldap_user_federation_id": "ldapUserFederationId",
        "membership_ldap_attribute": "membershipLdapAttribute",
        "membership_user_ldap_attribute": "membershipUserLdapAttribute",
        "name": "name",
        "realm_id": "realmId",
        "role_name_ldap_attribute": "roleNameLdapAttribute",
        "role_object_classes": "roleObjectClasses",
        "client_id": "clientId",
        "id": "id",
        "memberof_ldap_attribute": "memberofLdapAttribute",
        "membership_attribute_type": "membershipAttributeType",
        "mode": "mode",
        "roles_ldap_filter": "rolesLdapFilter",
        "use_realm_roles_mapping": "useRealmRolesMapping",
        "user_roles_retrieve_strategy": "userRolesRetrieveStrategy",
    },
)
class LdapRoleMapperConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        ldap_roles_dn: builtins.str,
        ldap_user_federation_id: builtins.str,
        membership_ldap_attribute: builtins.str,
        membership_user_ldap_attribute: builtins.str,
        name: builtins.str,
        realm_id: builtins.str,
        role_name_ldap_attribute: builtins.str,
        role_object_classes: typing.Sequence[builtins.str],
        client_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        memberof_ldap_attribute: typing.Optional[builtins.str] = None,
        membership_attribute_type: typing.Optional[builtins.str] = None,
        mode: typing.Optional[builtins.str] = None,
        roles_ldap_filter: typing.Optional[builtins.str] = None,
        use_realm_roles_mapping: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        user_roles_retrieve_strategy: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param connection:
        :param count:
        :param depends_on:
        :param for_each:
        :param lifecycle:
        :param provider:
        :param provisioners:
        :param ldap_roles_dn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#ldap_roles_dn LdapRoleMapper#ldap_roles_dn}.
        :param ldap_user_federation_id: The ldap user federation provider to attach this mapper to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#ldap_user_federation_id LdapRoleMapper#ldap_user_federation_id}
        :param membership_ldap_attribute: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#membership_ldap_attribute LdapRoleMapper#membership_ldap_attribute}.
        :param membership_user_ldap_attribute: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#membership_user_ldap_attribute LdapRoleMapper#membership_user_ldap_attribute}.
        :param name: Display name of the mapper when displayed in the console. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#name LdapRoleMapper#name}
        :param realm_id: The realm in which the ldap user federation provider exists. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#realm_id LdapRoleMapper#realm_id}
        :param role_name_ldap_attribute: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#role_name_ldap_attribute LdapRoleMapper#role_name_ldap_attribute}.
        :param role_object_classes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#role_object_classes LdapRoleMapper#role_object_classes}.
        :param client_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#client_id LdapRoleMapper#client_id}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#id LdapRoleMapper#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param memberof_ldap_attribute: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#memberof_ldap_attribute LdapRoleMapper#memberof_ldap_attribute}.
        :param membership_attribute_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#membership_attribute_type LdapRoleMapper#membership_attribute_type}.
        :param mode: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#mode LdapRoleMapper#mode}.
        :param roles_ldap_filter: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#roles_ldap_filter LdapRoleMapper#roles_ldap_filter}.
        :param use_realm_roles_mapping: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#use_realm_roles_mapping LdapRoleMapper#use_realm_roles_mapping}.
        :param user_roles_retrieve_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#user_roles_retrieve_strategy LdapRoleMapper#user_roles_retrieve_strategy}.
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__99b029a568f4d645468f08c89fa1ed6acdb9eebc39ce17ea9834a441f9f5fdbe
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
                argname="argument ldap_roles_dn",
                value=ldap_roles_dn,
                expected_type=type_hints["ldap_roles_dn"],
            )
            check_type(
                argname="argument ldap_user_federation_id",
                value=ldap_user_federation_id,
                expected_type=type_hints["ldap_user_federation_id"],
            )
            check_type(
                argname="argument membership_ldap_attribute",
                value=membership_ldap_attribute,
                expected_type=type_hints["membership_ldap_attribute"],
            )
            check_type(
                argname="argument membership_user_ldap_attribute",
                value=membership_user_ldap_attribute,
                expected_type=type_hints["membership_user_ldap_attribute"],
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
                argname="argument role_name_ldap_attribute",
                value=role_name_ldap_attribute,
                expected_type=type_hints["role_name_ldap_attribute"],
            )
            check_type(
                argname="argument role_object_classes",
                value=role_object_classes,
                expected_type=type_hints["role_object_classes"],
            )
            check_type(
                argname="argument client_id",
                value=client_id,
                expected_type=type_hints["client_id"],
            )
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(
                argname="argument memberof_ldap_attribute",
                value=memberof_ldap_attribute,
                expected_type=type_hints["memberof_ldap_attribute"],
            )
            check_type(
                argname="argument membership_attribute_type",
                value=membership_attribute_type,
                expected_type=type_hints["membership_attribute_type"],
            )
            check_type(
                argname="argument mode", value=mode, expected_type=type_hints["mode"]
            )
            check_type(
                argname="argument roles_ldap_filter",
                value=roles_ldap_filter,
                expected_type=type_hints["roles_ldap_filter"],
            )
            check_type(
                argname="argument use_realm_roles_mapping",
                value=use_realm_roles_mapping,
                expected_type=type_hints["use_realm_roles_mapping"],
            )
            check_type(
                argname="argument user_roles_retrieve_strategy",
                value=user_roles_retrieve_strategy,
                expected_type=type_hints["user_roles_retrieve_strategy"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ldap_roles_dn": ldap_roles_dn,
            "ldap_user_federation_id": ldap_user_federation_id,
            "membership_ldap_attribute": membership_ldap_attribute,
            "membership_user_ldap_attribute": membership_user_ldap_attribute,
            "name": name,
            "realm_id": realm_id,
            "role_name_ldap_attribute": role_name_ldap_attribute,
            "role_object_classes": role_object_classes,
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
        if id is not None:
            self._values["id"] = id
        if memberof_ldap_attribute is not None:
            self._values["memberof_ldap_attribute"] = memberof_ldap_attribute
        if membership_attribute_type is not None:
            self._values["membership_attribute_type"] = membership_attribute_type
        if mode is not None:
            self._values["mode"] = mode
        if roles_ldap_filter is not None:
            self._values["roles_ldap_filter"] = roles_ldap_filter
        if use_realm_roles_mapping is not None:
            self._values["use_realm_roles_mapping"] = use_realm_roles_mapping
        if user_roles_retrieve_strategy is not None:
            self._values["user_roles_retrieve_strategy"] = user_roles_retrieve_strategy

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
    def ldap_roles_dn(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#ldap_roles_dn LdapRoleMapper#ldap_roles_dn}."""
        result = self._values.get("ldap_roles_dn")
        assert result is not None, "Required property 'ldap_roles_dn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ldap_user_federation_id(self) -> builtins.str:
        """The ldap user federation provider to attach this mapper to.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#ldap_user_federation_id LdapRoleMapper#ldap_user_federation_id}
        """
        result = self._values.get("ldap_user_federation_id")
        assert (
            result is not None
        ), "Required property 'ldap_user_federation_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def membership_ldap_attribute(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#membership_ldap_attribute LdapRoleMapper#membership_ldap_attribute}."""
        result = self._values.get("membership_ldap_attribute")
        assert (
            result is not None
        ), "Required property 'membership_ldap_attribute' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def membership_user_ldap_attribute(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#membership_user_ldap_attribute LdapRoleMapper#membership_user_ldap_attribute}."""
        result = self._values.get("membership_user_ldap_attribute")
        assert (
            result is not None
        ), "Required property 'membership_user_ldap_attribute' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        """Display name of the mapper when displayed in the console.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#name LdapRoleMapper#name}
        """
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def realm_id(self) -> builtins.str:
        """The realm in which the ldap user federation provider exists.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#realm_id LdapRoleMapper#realm_id}
        """
        result = self._values.get("realm_id")
        assert result is not None, "Required property 'realm_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_name_ldap_attribute(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#role_name_ldap_attribute LdapRoleMapper#role_name_ldap_attribute}."""
        result = self._values.get("role_name_ldap_attribute")
        assert (
            result is not None
        ), "Required property 'role_name_ldap_attribute' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_object_classes(self) -> typing.List[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#role_object_classes LdapRoleMapper#role_object_classes}."""
        result = self._values.get("role_object_classes")
        assert result is not None, "Required property 'role_object_classes' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def client_id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#client_id LdapRoleMapper#client_id}."""
        result = self._values.get("client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#id LdapRoleMapper#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def memberof_ldap_attribute(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#memberof_ldap_attribute LdapRoleMapper#memberof_ldap_attribute}."""
        result = self._values.get("memberof_ldap_attribute")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def membership_attribute_type(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#membership_attribute_type LdapRoleMapper#membership_attribute_type}."""
        result = self._values.get("membership_attribute_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mode(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#mode LdapRoleMapper#mode}."""
        result = self._values.get("mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def roles_ldap_filter(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#roles_ldap_filter LdapRoleMapper#roles_ldap_filter}."""
        result = self._values.get("roles_ldap_filter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def use_realm_roles_mapping(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#use_realm_roles_mapping LdapRoleMapper#use_realm_roles_mapping}."""
        result = self._values.get("use_realm_roles_mapping")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def user_roles_retrieve_strategy(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_role_mapper#user_roles_retrieve_strategy LdapRoleMapper#user_roles_retrieve_strategy}."""
        result = self._values.get("user_roles_retrieve_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LdapRoleMapperConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "LdapRoleMapper",
    "LdapRoleMapperConfig",
]

publication.publish()


def _typecheckingstub__58e794209f56c731d7e06981fec386808f6e5f5f95f9901a828cae7f5341b097(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    ldap_roles_dn: builtins.str,
    ldap_user_federation_id: builtins.str,
    membership_ldap_attribute: builtins.str,
    membership_user_ldap_attribute: builtins.str,
    name: builtins.str,
    realm_id: builtins.str,
    role_name_ldap_attribute: builtins.str,
    role_object_classes: typing.Sequence[builtins.str],
    client_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    memberof_ldap_attribute: typing.Optional[builtins.str] = None,
    membership_attribute_type: typing.Optional[builtins.str] = None,
    mode: typing.Optional[builtins.str] = None,
    roles_ldap_filter: typing.Optional[builtins.str] = None,
    use_realm_roles_mapping: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    user_roles_retrieve_strategy: typing.Optional[builtins.str] = None,
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


def _typecheckingstub__35f792ba9d38fbf9f45b133df6af310a121253361da4000cf5ffe80d87f92ed1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3dd7247474738a7c571123f6097a9cc249ad299fe1a7bde24deef786084bd2f7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8c4fb80c2ff0ac699bf5ccf322dc4ea8c8a82add2d6942e1b01dff431d62ff84(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__5a653795a9f38ac2789d6d0e67418ecee50ee6114973d3fecb8772a218e238af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d32abb01988bae45562dacb1969621bbc735a12f440adebfb3f07555faabbe66(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__13fa66e5fbe8052c2bd389d0ffcc5eaac082d6e21f1197a946563a004f3719e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d815f829fb31bb9d2135e508ddb834b3b2d64183fa08a5e8216c5768c0521cf2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7889902c919f6ae49e3a0cb261a3cb1074c328ce433d6cac210e69c5cb5575c3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8526e041ed7533690146d86bdbe654e0a2cb83e2f3d55c1b0b24dfeb5abdd25e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__13a1cfd3c62058896f68804c91780da339b0048d412eab2dca5844f90a497f13(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__145726753519eb75e71c7650f1ec491132d3e77411b9a151433cc0df7407216d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b8f2a9284a71a9281eb4a6f8f4745b9502b3232c5e49480d5ab7e37587130559(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a8378011b135d31794850b6c35b0048f7b4089ef6184d6fd98bd4f25c5598ce6(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__68bc9ce1109f4d526c66df5542cb41bfed3f090abdce983b4535b6c988bbb764(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__294ec256e68b77bad2c7c2c76fa45189d000d454833b8602af6412b0032c2659(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a09343e296a32f672e94a69d1eaded3db73ed2de0175f502251a4596371d22dc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__99b029a568f4d645468f08c89fa1ed6acdb9eebc39ce17ea9834a441f9f5fdbe(
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
    ldap_roles_dn: builtins.str,
    ldap_user_federation_id: builtins.str,
    membership_ldap_attribute: builtins.str,
    membership_user_ldap_attribute: builtins.str,
    name: builtins.str,
    realm_id: builtins.str,
    role_name_ldap_attribute: builtins.str,
    role_object_classes: typing.Sequence[builtins.str],
    client_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    memberof_ldap_attribute: typing.Optional[builtins.str] = None,
    membership_attribute_type: typing.Optional[builtins.str] = None,
    mode: typing.Optional[builtins.str] = None,
    roles_ldap_filter: typing.Optional[builtins.str] = None,
    use_realm_roles_mapping: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    user_roles_retrieve_strategy: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
