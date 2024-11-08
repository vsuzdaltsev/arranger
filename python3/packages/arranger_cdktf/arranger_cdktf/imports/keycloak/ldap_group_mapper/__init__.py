"""
# `keycloak_ldap_group_mapper`

Refer to the Terraform Registory for docs: [`keycloak_ldap_group_mapper`](https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper).
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


class LdapGroupMapper(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.ldapGroupMapper.LdapGroupMapper",
):
    """Represents a {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper keycloak_ldap_group_mapper}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        group_name_ldap_attribute: builtins.str,
        group_object_classes: typing.Sequence[builtins.str],
        ldap_groups_dn: builtins.str,
        ldap_user_federation_id: builtins.str,
        membership_ldap_attribute: builtins.str,
        membership_user_ldap_attribute: builtins.str,
        name: builtins.str,
        realm_id: builtins.str,
        drop_non_existing_groups_during_sync: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        groups_ldap_filter: typing.Optional[builtins.str] = None,
        groups_path: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ignore_missing_groups: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        mapped_group_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
        memberof_ldap_attribute: typing.Optional[builtins.str] = None,
        membership_attribute_type: typing.Optional[builtins.str] = None,
        mode: typing.Optional[builtins.str] = None,
        preserve_group_inheritance: typing.Optional[
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
        """Create a new {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper keycloak_ldap_group_mapper} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param group_name_ldap_attribute: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#group_name_ldap_attribute LdapGroupMapper#group_name_ldap_attribute}.
        :param group_object_classes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#group_object_classes LdapGroupMapper#group_object_classes}.
        :param ldap_groups_dn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#ldap_groups_dn LdapGroupMapper#ldap_groups_dn}.
        :param ldap_user_federation_id: The ldap user federation provider to attach this mapper to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#ldap_user_federation_id LdapGroupMapper#ldap_user_federation_id}
        :param membership_ldap_attribute: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#membership_ldap_attribute LdapGroupMapper#membership_ldap_attribute}.
        :param membership_user_ldap_attribute: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#membership_user_ldap_attribute LdapGroupMapper#membership_user_ldap_attribute}.
        :param name: Display name of the mapper when displayed in the console. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#name LdapGroupMapper#name}
        :param realm_id: The realm in which the ldap user federation provider exists. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#realm_id LdapGroupMapper#realm_id}
        :param drop_non_existing_groups_during_sync: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#drop_non_existing_groups_during_sync LdapGroupMapper#drop_non_existing_groups_during_sync}.
        :param groups_ldap_filter: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#groups_ldap_filter LdapGroupMapper#groups_ldap_filter}.
        :param groups_path: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#groups_path LdapGroupMapper#groups_path}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#id LdapGroupMapper#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ignore_missing_groups: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#ignore_missing_groups LdapGroupMapper#ignore_missing_groups}.
        :param mapped_group_attributes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#mapped_group_attributes LdapGroupMapper#mapped_group_attributes}.
        :param memberof_ldap_attribute: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#memberof_ldap_attribute LdapGroupMapper#memberof_ldap_attribute}.
        :param membership_attribute_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#membership_attribute_type LdapGroupMapper#membership_attribute_type}.
        :param mode: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#mode LdapGroupMapper#mode}.
        :param preserve_group_inheritance: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#preserve_group_inheritance LdapGroupMapper#preserve_group_inheritance}.
        :param user_roles_retrieve_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#user_roles_retrieve_strategy LdapGroupMapper#user_roles_retrieve_strategy}.
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
                _typecheckingstub__e4a27cd414511f5db012d27cdf08934bf0766e0cc119e96160dd239ad4e18bc9
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(
                argname="argument id_", value=id_, expected_type=type_hints["id_"]
            )
        config = LdapGroupMapperConfig(
            group_name_ldap_attribute=group_name_ldap_attribute,
            group_object_classes=group_object_classes,
            ldap_groups_dn=ldap_groups_dn,
            ldap_user_federation_id=ldap_user_federation_id,
            membership_ldap_attribute=membership_ldap_attribute,
            membership_user_ldap_attribute=membership_user_ldap_attribute,
            name=name,
            realm_id=realm_id,
            drop_non_existing_groups_during_sync=drop_non_existing_groups_during_sync,
            groups_ldap_filter=groups_ldap_filter,
            groups_path=groups_path,
            id=id,
            ignore_missing_groups=ignore_missing_groups,
            mapped_group_attributes=mapped_group_attributes,
            memberof_ldap_attribute=memberof_ldap_attribute,
            membership_attribute_type=membership_attribute_type,
            mode=mode,
            preserve_group_inheritance=preserve_group_inheritance,
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

    @jsii.member(jsii_name="resetDropNonExistingGroupsDuringSync")
    def reset_drop_non_existing_groups_during_sync(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetDropNonExistingGroupsDuringSync", [])
        )

    @jsii.member(jsii_name="resetGroupsLdapFilter")
    def reset_groups_ldap_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupsLdapFilter", []))

    @jsii.member(jsii_name="resetGroupsPath")
    def reset_groups_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupsPath", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIgnoreMissingGroups")
    def reset_ignore_missing_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreMissingGroups", []))

    @jsii.member(jsii_name="resetMappedGroupAttributes")
    def reset_mapped_group_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMappedGroupAttributes", []))

    @jsii.member(jsii_name="resetMemberofLdapAttribute")
    def reset_memberof_ldap_attribute(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemberofLdapAttribute", []))

    @jsii.member(jsii_name="resetMembershipAttributeType")
    def reset_membership_attribute_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMembershipAttributeType", []))

    @jsii.member(jsii_name="resetMode")
    def reset_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMode", []))

    @jsii.member(jsii_name="resetPreserveGroupInheritance")
    def reset_preserve_group_inheritance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreserveGroupInheritance", []))

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
    @jsii.member(jsii_name="dropNonExistingGroupsDuringSyncInput")
    def drop_non_existing_groups_during_sync_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "dropNonExistingGroupsDuringSyncInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="groupNameLdapAttributeInput")
    def group_name_ldap_attribute_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "groupNameLdapAttributeInput")
        )

    @builtins.property
    @jsii.member(jsii_name="groupObjectClassesInput")
    def group_object_classes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]],
            jsii.get(self, "groupObjectClassesInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="groupsLdapFilterInput")
    def groups_ldap_filter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "groupsLdapFilterInput")
        )

    @builtins.property
    @jsii.member(jsii_name="groupsPathInput")
    def groups_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "groupsPathInput")
        )

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreMissingGroupsInput")
    def ignore_missing_groups_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "ignoreMissingGroupsInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="ldapGroupsDnInput")
    def ldap_groups_dn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "ldapGroupsDnInput")
        )

    @builtins.property
    @jsii.member(jsii_name="ldapUserFederationIdInput")
    def ldap_user_federation_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "ldapUserFederationIdInput")
        )

    @builtins.property
    @jsii.member(jsii_name="mappedGroupAttributesInput")
    def mapped_group_attributes_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]],
            jsii.get(self, "mappedGroupAttributesInput"),
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
    @jsii.member(jsii_name="preserveGroupInheritanceInput")
    def preserve_group_inheritance_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "preserveGroupInheritanceInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="realmIdInput")
    def realm_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "realmIdInput")
        )

    @builtins.property
    @jsii.member(jsii_name="userRolesRetrieveStrategyInput")
    def user_roles_retrieve_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str],
            jsii.get(self, "userRolesRetrieveStrategyInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="dropNonExistingGroupsDuringSync")
    def drop_non_existing_groups_during_sync(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "dropNonExistingGroupsDuringSync"),
        )

    @drop_non_existing_groups_during_sync.setter
    def drop_non_existing_groups_during_sync(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__deecabdcdf8fa91c09b27a47f2697e719542622aabc9dc2f55e2405e3ca34a38
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "dropNonExistingGroupsDuringSync", value)

    @builtins.property
    @jsii.member(jsii_name="groupNameLdapAttribute")
    def group_name_ldap_attribute(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupNameLdapAttribute"))

    @group_name_ldap_attribute.setter
    def group_name_ldap_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__bd8698f4f36ef02e8261a509642a33f314c26c0f6013fd06c05130f0fb60b28d
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "groupNameLdapAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="groupObjectClasses")
    def group_object_classes(self) -> typing.List[builtins.str]:
        return typing.cast(
            typing.List[builtins.str], jsii.get(self, "groupObjectClasses")
        )

    @group_object_classes.setter
    def group_object_classes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__808990e30e6b4484d7a53b0986224875c709ffb4c222b77ea5ada2bc44bb1253
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "groupObjectClasses", value)

    @builtins.property
    @jsii.member(jsii_name="groupsLdapFilter")
    def groups_ldap_filter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupsLdapFilter"))

    @groups_ldap_filter.setter
    def groups_ldap_filter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__526437a4c88089132aa79479bd250001e5a8758ef8636de1b59bb1b929f20460
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "groupsLdapFilter", value)

    @builtins.property
    @jsii.member(jsii_name="groupsPath")
    def groups_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupsPath"))

    @groups_path.setter
    def groups_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__6490d3a797c277603810a7a54a962514a3a8eac938f1dbdeac8704b3a70a003f
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "groupsPath", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__5eb1ac666b8bbf2cc82f63abf7797f2772a3d186f93e481708faf216afa37fa1
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreMissingGroups")
    def ignore_missing_groups(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "ignoreMissingGroups"),
        )

    @ignore_missing_groups.setter
    def ignore_missing_groups(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__adf263f5109d50538c710e45b42f86420c7d30ed2c6d7828e78728d9e09ce016
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "ignoreMissingGroups", value)

    @builtins.property
    @jsii.member(jsii_name="ldapGroupsDn")
    def ldap_groups_dn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ldapGroupsDn"))

    @ldap_groups_dn.setter
    def ldap_groups_dn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__02b344d17640627a5895e81ccefd71035aa3810e659f5495a8034d89d96b7b80
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "ldapGroupsDn", value)

    @builtins.property
    @jsii.member(jsii_name="ldapUserFederationId")
    def ldap_user_federation_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ldapUserFederationId"))

    @ldap_user_federation_id.setter
    def ldap_user_federation_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__9053dfe0683cbf3c4341420ca3e90e2b56ef7cf74ca6a8e3cbaef4b28e9a0ac9
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "ldapUserFederationId", value)

    @builtins.property
    @jsii.member(jsii_name="mappedGroupAttributes")
    def mapped_group_attributes(self) -> typing.List[builtins.str]:
        return typing.cast(
            typing.List[builtins.str], jsii.get(self, "mappedGroupAttributes")
        )

    @mapped_group_attributes.setter
    def mapped_group_attributes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d10cd1396f77a5d9db4fa269bf85c62fc9ac9287b91e0e0cd7208b4cce42893e
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "mappedGroupAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="memberofLdapAttribute")
    def memberof_ldap_attribute(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "memberofLdapAttribute"))

    @memberof_ldap_attribute.setter
    def memberof_ldap_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__95cd73f5d71dacf023a0b39881d3d9dcede0fafef86c438245f25742a94f6726
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
                _typecheckingstub__2d346b923965d34913c6593a336d7af643aa093397f702e633f6542a270ec545
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
                _typecheckingstub__5689cb6d472ff02dfc977bb6619f86dd143771dbdf911352b7541a56ae62fa81
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
                _typecheckingstub__e837bebba86d4c7398118b3b7884a72602c8507c5996cb59408a6b7778e1091a
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
                _typecheckingstub__113852227364576d9e36cb8b7b19a176f2678ef3087ad8faded061fa2c23c34d
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
                _typecheckingstub__67f82691f8179f315cf18f21471a48c8450be3c217ee06df8c51feaba709a253
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="preserveGroupInheritance")
    def preserve_group_inheritance(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "preserveGroupInheritance"),
        )

    @preserve_group_inheritance.setter
    def preserve_group_inheritance(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__017602c84b2a4b26d2146510bed39d97095932006b15652dcf4302b9ef4cd1ae
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "preserveGroupInheritance", value)

    @builtins.property
    @jsii.member(jsii_name="realmId")
    def realm_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "realmId"))

    @realm_id.setter
    def realm_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a4e9617b3c3d0bdd942915b4b3496241b33d243b948f1d1b94e22e483605786a
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "realmId", value)

    @builtins.property
    @jsii.member(jsii_name="userRolesRetrieveStrategy")
    def user_roles_retrieve_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userRolesRetrieveStrategy"))

    @user_roles_retrieve_strategy.setter
    def user_roles_retrieve_strategy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__12fbf9a8ec997a0cb3dad461a7f1230de4fea59eae047b25f87fa54bc605ba1b
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "userRolesRetrieveStrategy", value)


@jsii.data_type(
    jsii_type="keycloak.ldapGroupMapper.LdapGroupMapperConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "group_name_ldap_attribute": "groupNameLdapAttribute",
        "group_object_classes": "groupObjectClasses",
        "ldap_groups_dn": "ldapGroupsDn",
        "ldap_user_federation_id": "ldapUserFederationId",
        "membership_ldap_attribute": "membershipLdapAttribute",
        "membership_user_ldap_attribute": "membershipUserLdapAttribute",
        "name": "name",
        "realm_id": "realmId",
        "drop_non_existing_groups_during_sync": "dropNonExistingGroupsDuringSync",
        "groups_ldap_filter": "groupsLdapFilter",
        "groups_path": "groupsPath",
        "id": "id",
        "ignore_missing_groups": "ignoreMissingGroups",
        "mapped_group_attributes": "mappedGroupAttributes",
        "memberof_ldap_attribute": "memberofLdapAttribute",
        "membership_attribute_type": "membershipAttributeType",
        "mode": "mode",
        "preserve_group_inheritance": "preserveGroupInheritance",
        "user_roles_retrieve_strategy": "userRolesRetrieveStrategy",
    },
)
class LdapGroupMapperConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        group_name_ldap_attribute: builtins.str,
        group_object_classes: typing.Sequence[builtins.str],
        ldap_groups_dn: builtins.str,
        ldap_user_federation_id: builtins.str,
        membership_ldap_attribute: builtins.str,
        membership_user_ldap_attribute: builtins.str,
        name: builtins.str,
        realm_id: builtins.str,
        drop_non_existing_groups_during_sync: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        groups_ldap_filter: typing.Optional[builtins.str] = None,
        groups_path: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ignore_missing_groups: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        mapped_group_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
        memberof_ldap_attribute: typing.Optional[builtins.str] = None,
        membership_attribute_type: typing.Optional[builtins.str] = None,
        mode: typing.Optional[builtins.str] = None,
        preserve_group_inheritance: typing.Optional[
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
        :param group_name_ldap_attribute: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#group_name_ldap_attribute LdapGroupMapper#group_name_ldap_attribute}.
        :param group_object_classes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#group_object_classes LdapGroupMapper#group_object_classes}.
        :param ldap_groups_dn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#ldap_groups_dn LdapGroupMapper#ldap_groups_dn}.
        :param ldap_user_federation_id: The ldap user federation provider to attach this mapper to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#ldap_user_federation_id LdapGroupMapper#ldap_user_federation_id}
        :param membership_ldap_attribute: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#membership_ldap_attribute LdapGroupMapper#membership_ldap_attribute}.
        :param membership_user_ldap_attribute: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#membership_user_ldap_attribute LdapGroupMapper#membership_user_ldap_attribute}.
        :param name: Display name of the mapper when displayed in the console. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#name LdapGroupMapper#name}
        :param realm_id: The realm in which the ldap user federation provider exists. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#realm_id LdapGroupMapper#realm_id}
        :param drop_non_existing_groups_during_sync: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#drop_non_existing_groups_during_sync LdapGroupMapper#drop_non_existing_groups_during_sync}.
        :param groups_ldap_filter: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#groups_ldap_filter LdapGroupMapper#groups_ldap_filter}.
        :param groups_path: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#groups_path LdapGroupMapper#groups_path}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#id LdapGroupMapper#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ignore_missing_groups: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#ignore_missing_groups LdapGroupMapper#ignore_missing_groups}.
        :param mapped_group_attributes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#mapped_group_attributes LdapGroupMapper#mapped_group_attributes}.
        :param memberof_ldap_attribute: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#memberof_ldap_attribute LdapGroupMapper#memberof_ldap_attribute}.
        :param membership_attribute_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#membership_attribute_type LdapGroupMapper#membership_attribute_type}.
        :param mode: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#mode LdapGroupMapper#mode}.
        :param preserve_group_inheritance: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#preserve_group_inheritance LdapGroupMapper#preserve_group_inheritance}.
        :param user_roles_retrieve_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#user_roles_retrieve_strategy LdapGroupMapper#user_roles_retrieve_strategy}.
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a185002c2093e507ecfe97918646dce1053a26ee4682ceddc07c6875f0c1ad2f
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
                argname="argument group_name_ldap_attribute",
                value=group_name_ldap_attribute,
                expected_type=type_hints["group_name_ldap_attribute"],
            )
            check_type(
                argname="argument group_object_classes",
                value=group_object_classes,
                expected_type=type_hints["group_object_classes"],
            )
            check_type(
                argname="argument ldap_groups_dn",
                value=ldap_groups_dn,
                expected_type=type_hints["ldap_groups_dn"],
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
                argname="argument drop_non_existing_groups_during_sync",
                value=drop_non_existing_groups_during_sync,
                expected_type=type_hints["drop_non_existing_groups_during_sync"],
            )
            check_type(
                argname="argument groups_ldap_filter",
                value=groups_ldap_filter,
                expected_type=type_hints["groups_ldap_filter"],
            )
            check_type(
                argname="argument groups_path",
                value=groups_path,
                expected_type=type_hints["groups_path"],
            )
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(
                argname="argument ignore_missing_groups",
                value=ignore_missing_groups,
                expected_type=type_hints["ignore_missing_groups"],
            )
            check_type(
                argname="argument mapped_group_attributes",
                value=mapped_group_attributes,
                expected_type=type_hints["mapped_group_attributes"],
            )
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
                argname="argument preserve_group_inheritance",
                value=preserve_group_inheritance,
                expected_type=type_hints["preserve_group_inheritance"],
            )
            check_type(
                argname="argument user_roles_retrieve_strategy",
                value=user_roles_retrieve_strategy,
                expected_type=type_hints["user_roles_retrieve_strategy"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "group_name_ldap_attribute": group_name_ldap_attribute,
            "group_object_classes": group_object_classes,
            "ldap_groups_dn": ldap_groups_dn,
            "ldap_user_federation_id": ldap_user_federation_id,
            "membership_ldap_attribute": membership_ldap_attribute,
            "membership_user_ldap_attribute": membership_user_ldap_attribute,
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
        if drop_non_existing_groups_during_sync is not None:
            self._values[
                "drop_non_existing_groups_during_sync"
            ] = drop_non_existing_groups_during_sync
        if groups_ldap_filter is not None:
            self._values["groups_ldap_filter"] = groups_ldap_filter
        if groups_path is not None:
            self._values["groups_path"] = groups_path
        if id is not None:
            self._values["id"] = id
        if ignore_missing_groups is not None:
            self._values["ignore_missing_groups"] = ignore_missing_groups
        if mapped_group_attributes is not None:
            self._values["mapped_group_attributes"] = mapped_group_attributes
        if memberof_ldap_attribute is not None:
            self._values["memberof_ldap_attribute"] = memberof_ldap_attribute
        if membership_attribute_type is not None:
            self._values["membership_attribute_type"] = membership_attribute_type
        if mode is not None:
            self._values["mode"] = mode
        if preserve_group_inheritance is not None:
            self._values["preserve_group_inheritance"] = preserve_group_inheritance
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
    def group_name_ldap_attribute(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#group_name_ldap_attribute LdapGroupMapper#group_name_ldap_attribute}."""
        result = self._values.get("group_name_ldap_attribute")
        assert (
            result is not None
        ), "Required property 'group_name_ldap_attribute' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_object_classes(self) -> typing.List[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#group_object_classes LdapGroupMapper#group_object_classes}."""
        result = self._values.get("group_object_classes")
        assert result is not None, "Required property 'group_object_classes' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def ldap_groups_dn(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#ldap_groups_dn LdapGroupMapper#ldap_groups_dn}."""
        result = self._values.get("ldap_groups_dn")
        assert result is not None, "Required property 'ldap_groups_dn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ldap_user_federation_id(self) -> builtins.str:
        """The ldap user federation provider to attach this mapper to.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#ldap_user_federation_id LdapGroupMapper#ldap_user_federation_id}
        """
        result = self._values.get("ldap_user_federation_id")
        assert (
            result is not None
        ), "Required property 'ldap_user_federation_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def membership_ldap_attribute(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#membership_ldap_attribute LdapGroupMapper#membership_ldap_attribute}."""
        result = self._values.get("membership_ldap_attribute")
        assert (
            result is not None
        ), "Required property 'membership_ldap_attribute' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def membership_user_ldap_attribute(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#membership_user_ldap_attribute LdapGroupMapper#membership_user_ldap_attribute}."""
        result = self._values.get("membership_user_ldap_attribute")
        assert (
            result is not None
        ), "Required property 'membership_user_ldap_attribute' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        """Display name of the mapper when displayed in the console.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#name LdapGroupMapper#name}
        """
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def realm_id(self) -> builtins.str:
        """The realm in which the ldap user federation provider exists.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#realm_id LdapGroupMapper#realm_id}
        """
        result = self._values.get("realm_id")
        assert result is not None, "Required property 'realm_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def drop_non_existing_groups_during_sync(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#drop_non_existing_groups_during_sync LdapGroupMapper#drop_non_existing_groups_during_sync}."""
        result = self._values.get("drop_non_existing_groups_during_sync")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def groups_ldap_filter(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#groups_ldap_filter LdapGroupMapper#groups_ldap_filter}."""
        result = self._values.get("groups_ldap_filter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def groups_path(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#groups_path LdapGroupMapper#groups_path}."""
        result = self._values.get("groups_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#id LdapGroupMapper#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ignore_missing_groups(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#ignore_missing_groups LdapGroupMapper#ignore_missing_groups}."""
        result = self._values.get("ignore_missing_groups")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def mapped_group_attributes(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#mapped_group_attributes LdapGroupMapper#mapped_group_attributes}."""
        result = self._values.get("mapped_group_attributes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def memberof_ldap_attribute(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#memberof_ldap_attribute LdapGroupMapper#memberof_ldap_attribute}."""
        result = self._values.get("memberof_ldap_attribute")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def membership_attribute_type(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#membership_attribute_type LdapGroupMapper#membership_attribute_type}."""
        result = self._values.get("membership_attribute_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mode(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#mode LdapGroupMapper#mode}."""
        result = self._values.get("mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preserve_group_inheritance(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#preserve_group_inheritance LdapGroupMapper#preserve_group_inheritance}."""
        result = self._values.get("preserve_group_inheritance")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def user_roles_retrieve_strategy(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_group_mapper#user_roles_retrieve_strategy LdapGroupMapper#user_roles_retrieve_strategy}."""
        result = self._values.get("user_roles_retrieve_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LdapGroupMapperConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "LdapGroupMapper",
    "LdapGroupMapperConfig",
]

publication.publish()


def _typecheckingstub__e4a27cd414511f5db012d27cdf08934bf0766e0cc119e96160dd239ad4e18bc9(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    group_name_ldap_attribute: builtins.str,
    group_object_classes: typing.Sequence[builtins.str],
    ldap_groups_dn: builtins.str,
    ldap_user_federation_id: builtins.str,
    membership_ldap_attribute: builtins.str,
    membership_user_ldap_attribute: builtins.str,
    name: builtins.str,
    realm_id: builtins.str,
    drop_non_existing_groups_during_sync: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    groups_ldap_filter: typing.Optional[builtins.str] = None,
    groups_path: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    ignore_missing_groups: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    mapped_group_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
    memberof_ldap_attribute: typing.Optional[builtins.str] = None,
    membership_attribute_type: typing.Optional[builtins.str] = None,
    mode: typing.Optional[builtins.str] = None,
    preserve_group_inheritance: typing.Optional[
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


def _typecheckingstub__deecabdcdf8fa91c09b27a47f2697e719542622aabc9dc2f55e2405e3ca34a38(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__bd8698f4f36ef02e8261a509642a33f314c26c0f6013fd06c05130f0fb60b28d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__808990e30e6b4484d7a53b0986224875c709ffb4c222b77ea5ada2bc44bb1253(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__526437a4c88089132aa79479bd250001e5a8758ef8636de1b59bb1b929f20460(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6490d3a797c277603810a7a54a962514a3a8eac938f1dbdeac8704b3a70a003f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__5eb1ac666b8bbf2cc82f63abf7797f2772a3d186f93e481708faf216afa37fa1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__adf263f5109d50538c710e45b42f86420c7d30ed2c6d7828e78728d9e09ce016(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__02b344d17640627a5895e81ccefd71035aa3810e659f5495a8034d89d96b7b80(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9053dfe0683cbf3c4341420ca3e90e2b56ef7cf74ca6a8e3cbaef4b28e9a0ac9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d10cd1396f77a5d9db4fa269bf85c62fc9ac9287b91e0e0cd7208b4cce42893e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__95cd73f5d71dacf023a0b39881d3d9dcede0fafef86c438245f25742a94f6726(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__2d346b923965d34913c6593a336d7af643aa093397f702e633f6542a270ec545(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__5689cb6d472ff02dfc977bb6619f86dd143771dbdf911352b7541a56ae62fa81(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e837bebba86d4c7398118b3b7884a72602c8507c5996cb59408a6b7778e1091a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__113852227364576d9e36cb8b7b19a176f2678ef3087ad8faded061fa2c23c34d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__67f82691f8179f315cf18f21471a48c8450be3c217ee06df8c51feaba709a253(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__017602c84b2a4b26d2146510bed39d97095932006b15652dcf4302b9ef4cd1ae(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a4e9617b3c3d0bdd942915b4b3496241b33d243b948f1d1b94e22e483605786a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__12fbf9a8ec997a0cb3dad461a7f1230de4fea59eae047b25f87fa54bc605ba1b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a185002c2093e507ecfe97918646dce1053a26ee4682ceddc07c6875f0c1ad2f(
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
    group_name_ldap_attribute: builtins.str,
    group_object_classes: typing.Sequence[builtins.str],
    ldap_groups_dn: builtins.str,
    ldap_user_federation_id: builtins.str,
    membership_ldap_attribute: builtins.str,
    membership_user_ldap_attribute: builtins.str,
    name: builtins.str,
    realm_id: builtins.str,
    drop_non_existing_groups_during_sync: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    groups_ldap_filter: typing.Optional[builtins.str] = None,
    groups_path: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    ignore_missing_groups: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    mapped_group_attributes: typing.Optional[typing.Sequence[builtins.str]] = None,
    memberof_ldap_attribute: typing.Optional[builtins.str] = None,
    membership_attribute_type: typing.Optional[builtins.str] = None,
    mode: typing.Optional[builtins.str] = None,
    preserve_group_inheritance: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    user_roles_retrieve_strategy: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
