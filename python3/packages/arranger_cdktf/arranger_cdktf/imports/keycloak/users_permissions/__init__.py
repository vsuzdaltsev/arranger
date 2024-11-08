"""
# `keycloak_users_permissions`

Refer to the Terraform Registory for docs: [`keycloak_users_permissions`](https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions).
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


class UsersPermissions(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.usersPermissions.UsersPermissions",
):
    """Represents a {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions keycloak_users_permissions}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        realm_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        impersonate_scope: typing.Optional[
            typing.Union[
                "UsersPermissionsImpersonateScope",
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        manage_group_membership_scope: typing.Optional[
            typing.Union[
                "UsersPermissionsManageGroupMembershipScope",
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        manage_scope: typing.Optional[
            typing.Union[
                "UsersPermissionsManageScope", typing.Dict[builtins.str, typing.Any]
            ]
        ] = None,
        map_roles_scope: typing.Optional[
            typing.Union[
                "UsersPermissionsMapRolesScope", typing.Dict[builtins.str, typing.Any]
            ]
        ] = None,
        user_impersonated_scope: typing.Optional[
            typing.Union[
                "UsersPermissionsUserImpersonatedScope",
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        view_scope: typing.Optional[
            typing.Union[
                "UsersPermissionsViewScope", typing.Dict[builtins.str, typing.Any]
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
        """Create a new {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions keycloak_users_permissions} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param realm_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#realm_id UsersPermissions#realm_id}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#id UsersPermissions#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param impersonate_scope: impersonate_scope block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#impersonate_scope UsersPermissions#impersonate_scope}
        :param manage_group_membership_scope: manage_group_membership_scope block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#manage_group_membership_scope UsersPermissions#manage_group_membership_scope}
        :param manage_scope: manage_scope block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#manage_scope UsersPermissions#manage_scope}
        :param map_roles_scope: map_roles_scope block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#map_roles_scope UsersPermissions#map_roles_scope}
        :param user_impersonated_scope: user_impersonated_scope block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#user_impersonated_scope UsersPermissions#user_impersonated_scope}
        :param view_scope: view_scope block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#view_scope UsersPermissions#view_scope}
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
                _typecheckingstub__bd1657c6a562d672dfaf8ba32f43d9c3c8b33e9b0e3dcb17f68bdfbf46d59bdd
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(
                argname="argument id_", value=id_, expected_type=type_hints["id_"]
            )
        config = UsersPermissionsConfig(
            realm_id=realm_id,
            id=id,
            impersonate_scope=impersonate_scope,
            manage_group_membership_scope=manage_group_membership_scope,
            manage_scope=manage_scope,
            map_roles_scope=map_roles_scope,
            user_impersonated_scope=user_impersonated_scope,
            view_scope=view_scope,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putImpersonateScope")
    def put_impersonate_scope(
        self,
        *,
        decision_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#decision_strategy UsersPermissions#decision_strategy}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#description UsersPermissions#description}.
        :param policies: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#policies UsersPermissions#policies}.
        """
        value = UsersPermissionsImpersonateScope(
            decision_strategy=decision_strategy,
            description=description,
            policies=policies,
        )

        return typing.cast(None, jsii.invoke(self, "putImpersonateScope", [value]))

    @jsii.member(jsii_name="putManageGroupMembershipScope")
    def put_manage_group_membership_scope(
        self,
        *,
        decision_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#decision_strategy UsersPermissions#decision_strategy}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#description UsersPermissions#description}.
        :param policies: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#policies UsersPermissions#policies}.
        """
        value = UsersPermissionsManageGroupMembershipScope(
            decision_strategy=decision_strategy,
            description=description,
            policies=policies,
        )

        return typing.cast(
            None, jsii.invoke(self, "putManageGroupMembershipScope", [value])
        )

    @jsii.member(jsii_name="putManageScope")
    def put_manage_scope(
        self,
        *,
        decision_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#decision_strategy UsersPermissions#decision_strategy}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#description UsersPermissions#description}.
        :param policies: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#policies UsersPermissions#policies}.
        """
        value = UsersPermissionsManageScope(
            decision_strategy=decision_strategy,
            description=description,
            policies=policies,
        )

        return typing.cast(None, jsii.invoke(self, "putManageScope", [value]))

    @jsii.member(jsii_name="putMapRolesScope")
    def put_map_roles_scope(
        self,
        *,
        decision_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#decision_strategy UsersPermissions#decision_strategy}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#description UsersPermissions#description}.
        :param policies: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#policies UsersPermissions#policies}.
        """
        value = UsersPermissionsMapRolesScope(
            decision_strategy=decision_strategy,
            description=description,
            policies=policies,
        )

        return typing.cast(None, jsii.invoke(self, "putMapRolesScope", [value]))

    @jsii.member(jsii_name="putUserImpersonatedScope")
    def put_user_impersonated_scope(
        self,
        *,
        decision_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#decision_strategy UsersPermissions#decision_strategy}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#description UsersPermissions#description}.
        :param policies: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#policies UsersPermissions#policies}.
        """
        value = UsersPermissionsUserImpersonatedScope(
            decision_strategy=decision_strategy,
            description=description,
            policies=policies,
        )

        return typing.cast(None, jsii.invoke(self, "putUserImpersonatedScope", [value]))

    @jsii.member(jsii_name="putViewScope")
    def put_view_scope(
        self,
        *,
        decision_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#decision_strategy UsersPermissions#decision_strategy}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#description UsersPermissions#description}.
        :param policies: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#policies UsersPermissions#policies}.
        """
        value = UsersPermissionsViewScope(
            decision_strategy=decision_strategy,
            description=description,
            policies=policies,
        )

        return typing.cast(None, jsii.invoke(self, "putViewScope", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetImpersonateScope")
    def reset_impersonate_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImpersonateScope", []))

    @jsii.member(jsii_name="resetManageGroupMembershipScope")
    def reset_manage_group_membership_scope(self) -> None:
        return typing.cast(
            None, jsii.invoke(self, "resetManageGroupMembershipScope", [])
        )

    @jsii.member(jsii_name="resetManageScope")
    def reset_manage_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManageScope", []))

    @jsii.member(jsii_name="resetMapRolesScope")
    def reset_map_roles_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMapRolesScope", []))

    @jsii.member(jsii_name="resetUserImpersonatedScope")
    def reset_user_impersonated_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserImpersonatedScope", []))

    @jsii.member(jsii_name="resetViewScope")
    def reset_view_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetViewScope", []))

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
    @jsii.member(jsii_name="authorizationResourceServerId")
    def authorization_resource_server_id(self) -> builtins.str:
        return typing.cast(
            builtins.str, jsii.get(self, "authorizationResourceServerId")
        )

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "enabled"))

    @builtins.property
    @jsii.member(jsii_name="impersonateScope")
    def impersonate_scope(self) -> "UsersPermissionsImpersonateScopeOutputReference":
        return typing.cast(
            "UsersPermissionsImpersonateScopeOutputReference",
            jsii.get(self, "impersonateScope"),
        )

    @builtins.property
    @jsii.member(jsii_name="manageGroupMembershipScope")
    def manage_group_membership_scope(
        self,
    ) -> "UsersPermissionsManageGroupMembershipScopeOutputReference":
        return typing.cast(
            "UsersPermissionsManageGroupMembershipScopeOutputReference",
            jsii.get(self, "manageGroupMembershipScope"),
        )

    @builtins.property
    @jsii.member(jsii_name="manageScope")
    def manage_scope(self) -> "UsersPermissionsManageScopeOutputReference":
        return typing.cast(
            "UsersPermissionsManageScopeOutputReference", jsii.get(self, "manageScope")
        )

    @builtins.property
    @jsii.member(jsii_name="mapRolesScope")
    def map_roles_scope(self) -> "UsersPermissionsMapRolesScopeOutputReference":
        return typing.cast(
            "UsersPermissionsMapRolesScopeOutputReference",
            jsii.get(self, "mapRolesScope"),
        )

    @builtins.property
    @jsii.member(jsii_name="userImpersonatedScope")
    def user_impersonated_scope(
        self,
    ) -> "UsersPermissionsUserImpersonatedScopeOutputReference":
        return typing.cast(
            "UsersPermissionsUserImpersonatedScopeOutputReference",
            jsii.get(self, "userImpersonatedScope"),
        )

    @builtins.property
    @jsii.member(jsii_name="viewScope")
    def view_scope(self) -> "UsersPermissionsViewScopeOutputReference":
        return typing.cast(
            "UsersPermissionsViewScopeOutputReference", jsii.get(self, "viewScope")
        )

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="impersonateScopeInput")
    def impersonate_scope_input(
        self,
    ) -> typing.Optional["UsersPermissionsImpersonateScope"]:
        return typing.cast(
            typing.Optional["UsersPermissionsImpersonateScope"],
            jsii.get(self, "impersonateScopeInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="manageGroupMembershipScopeInput")
    def manage_group_membership_scope_input(
        self,
    ) -> typing.Optional["UsersPermissionsManageGroupMembershipScope"]:
        return typing.cast(
            typing.Optional["UsersPermissionsManageGroupMembershipScope"],
            jsii.get(self, "manageGroupMembershipScopeInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="manageScopeInput")
    def manage_scope_input(self) -> typing.Optional["UsersPermissionsManageScope"]:
        return typing.cast(
            typing.Optional["UsersPermissionsManageScope"],
            jsii.get(self, "manageScopeInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="mapRolesScopeInput")
    def map_roles_scope_input(self) -> typing.Optional["UsersPermissionsMapRolesScope"]:
        return typing.cast(
            typing.Optional["UsersPermissionsMapRolesScope"],
            jsii.get(self, "mapRolesScopeInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="realmIdInput")
    def realm_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "realmIdInput")
        )

    @builtins.property
    @jsii.member(jsii_name="userImpersonatedScopeInput")
    def user_impersonated_scope_input(
        self,
    ) -> typing.Optional["UsersPermissionsUserImpersonatedScope"]:
        return typing.cast(
            typing.Optional["UsersPermissionsUserImpersonatedScope"],
            jsii.get(self, "userImpersonatedScopeInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="viewScopeInput")
    def view_scope_input(self) -> typing.Optional["UsersPermissionsViewScope"]:
        return typing.cast(
            typing.Optional["UsersPermissionsViewScope"],
            jsii.get(self, "viewScopeInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__76c10215b4ad309648d6969599bbbd216f9bb4e3770f5107d5d4b307731f4665
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
                _typecheckingstub__b993479f743088d584308ae4eede394cd9946dce71e7a98818872ece0eea0a30
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "realmId", value)


@jsii.data_type(
    jsii_type="keycloak.usersPermissions.UsersPermissionsConfig",
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
        "id": "id",
        "impersonate_scope": "impersonateScope",
        "manage_group_membership_scope": "manageGroupMembershipScope",
        "manage_scope": "manageScope",
        "map_roles_scope": "mapRolesScope",
        "user_impersonated_scope": "userImpersonatedScope",
        "view_scope": "viewScope",
    },
)
class UsersPermissionsConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        id: typing.Optional[builtins.str] = None,
        impersonate_scope: typing.Optional[
            typing.Union[
                "UsersPermissionsImpersonateScope",
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        manage_group_membership_scope: typing.Optional[
            typing.Union[
                "UsersPermissionsManageGroupMembershipScope",
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        manage_scope: typing.Optional[
            typing.Union[
                "UsersPermissionsManageScope", typing.Dict[builtins.str, typing.Any]
            ]
        ] = None,
        map_roles_scope: typing.Optional[
            typing.Union[
                "UsersPermissionsMapRolesScope", typing.Dict[builtins.str, typing.Any]
            ]
        ] = None,
        user_impersonated_scope: typing.Optional[
            typing.Union[
                "UsersPermissionsUserImpersonatedScope",
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        view_scope: typing.Optional[
            typing.Union[
                "UsersPermissionsViewScope", typing.Dict[builtins.str, typing.Any]
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
        :param realm_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#realm_id UsersPermissions#realm_id}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#id UsersPermissions#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param impersonate_scope: impersonate_scope block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#impersonate_scope UsersPermissions#impersonate_scope}
        :param manage_group_membership_scope: manage_group_membership_scope block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#manage_group_membership_scope UsersPermissions#manage_group_membership_scope}
        :param manage_scope: manage_scope block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#manage_scope UsersPermissions#manage_scope}
        :param map_roles_scope: map_roles_scope block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#map_roles_scope UsersPermissions#map_roles_scope}
        :param user_impersonated_scope: user_impersonated_scope block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#user_impersonated_scope UsersPermissions#user_impersonated_scope}
        :param view_scope: view_scope block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#view_scope UsersPermissions#view_scope}
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(impersonate_scope, dict):
            impersonate_scope = UsersPermissionsImpersonateScope(**impersonate_scope)
        if isinstance(manage_group_membership_scope, dict):
            manage_group_membership_scope = UsersPermissionsManageGroupMembershipScope(
                **manage_group_membership_scope
            )
        if isinstance(manage_scope, dict):
            manage_scope = UsersPermissionsManageScope(**manage_scope)
        if isinstance(map_roles_scope, dict):
            map_roles_scope = UsersPermissionsMapRolesScope(**map_roles_scope)
        if isinstance(user_impersonated_scope, dict):
            user_impersonated_scope = UsersPermissionsUserImpersonatedScope(
                **user_impersonated_scope
            )
        if isinstance(view_scope, dict):
            view_scope = UsersPermissionsViewScope(**view_scope)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__447c84f5e9847e1d42dcca058212a205b2f16f25ebf4e9745ec04588a4aa3a8d
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
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(
                argname="argument impersonate_scope",
                value=impersonate_scope,
                expected_type=type_hints["impersonate_scope"],
            )
            check_type(
                argname="argument manage_group_membership_scope",
                value=manage_group_membership_scope,
                expected_type=type_hints["manage_group_membership_scope"],
            )
            check_type(
                argname="argument manage_scope",
                value=manage_scope,
                expected_type=type_hints["manage_scope"],
            )
            check_type(
                argname="argument map_roles_scope",
                value=map_roles_scope,
                expected_type=type_hints["map_roles_scope"],
            )
            check_type(
                argname="argument user_impersonated_scope",
                value=user_impersonated_scope,
                expected_type=type_hints["user_impersonated_scope"],
            )
            check_type(
                argname="argument view_scope",
                value=view_scope,
                expected_type=type_hints["view_scope"],
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
        if id is not None:
            self._values["id"] = id
        if impersonate_scope is not None:
            self._values["impersonate_scope"] = impersonate_scope
        if manage_group_membership_scope is not None:
            self._values[
                "manage_group_membership_scope"
            ] = manage_group_membership_scope
        if manage_scope is not None:
            self._values["manage_scope"] = manage_scope
        if map_roles_scope is not None:
            self._values["map_roles_scope"] = map_roles_scope
        if user_impersonated_scope is not None:
            self._values["user_impersonated_scope"] = user_impersonated_scope
        if view_scope is not None:
            self._values["view_scope"] = view_scope

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
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#realm_id UsersPermissions#realm_id}."""
        result = self._values.get("realm_id")
        assert result is not None, "Required property 'realm_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#id UsersPermissions#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def impersonate_scope(self) -> typing.Optional["UsersPermissionsImpersonateScope"]:
        """impersonate_scope block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#impersonate_scope UsersPermissions#impersonate_scope}
        """
        result = self._values.get("impersonate_scope")
        return typing.cast(typing.Optional["UsersPermissionsImpersonateScope"], result)

    @builtins.property
    def manage_group_membership_scope(
        self,
    ) -> typing.Optional["UsersPermissionsManageGroupMembershipScope"]:
        """manage_group_membership_scope block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#manage_group_membership_scope UsersPermissions#manage_group_membership_scope}
        """
        result = self._values.get("manage_group_membership_scope")
        return typing.cast(
            typing.Optional["UsersPermissionsManageGroupMembershipScope"], result
        )

    @builtins.property
    def manage_scope(self) -> typing.Optional["UsersPermissionsManageScope"]:
        """manage_scope block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#manage_scope UsersPermissions#manage_scope}
        """
        result = self._values.get("manage_scope")
        return typing.cast(typing.Optional["UsersPermissionsManageScope"], result)

    @builtins.property
    def map_roles_scope(self) -> typing.Optional["UsersPermissionsMapRolesScope"]:
        """map_roles_scope block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#map_roles_scope UsersPermissions#map_roles_scope}
        """
        result = self._values.get("map_roles_scope")
        return typing.cast(typing.Optional["UsersPermissionsMapRolesScope"], result)

    @builtins.property
    def user_impersonated_scope(
        self,
    ) -> typing.Optional["UsersPermissionsUserImpersonatedScope"]:
        """user_impersonated_scope block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#user_impersonated_scope UsersPermissions#user_impersonated_scope}
        """
        result = self._values.get("user_impersonated_scope")
        return typing.cast(
            typing.Optional["UsersPermissionsUserImpersonatedScope"], result
        )

    @builtins.property
    def view_scope(self) -> typing.Optional["UsersPermissionsViewScope"]:
        """view_scope block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#view_scope UsersPermissions#view_scope}
        """
        result = self._values.get("view_scope")
        return typing.cast(typing.Optional["UsersPermissionsViewScope"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UsersPermissionsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="keycloak.usersPermissions.UsersPermissionsImpersonateScope",
    jsii_struct_bases=[],
    name_mapping={
        "decision_strategy": "decisionStrategy",
        "description": "description",
        "policies": "policies",
    },
)
class UsersPermissionsImpersonateScope:
    def __init__(
        self,
        *,
        decision_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#decision_strategy UsersPermissions#decision_strategy}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#description UsersPermissions#description}.
        :param policies: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#policies UsersPermissions#policies}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__48b37f85c9c01b01c5a2af390a5d6b7f700edc29b2b3849aa36321cb5b27d00c
            )
            check_type(
                argname="argument decision_strategy",
                value=decision_strategy,
                expected_type=type_hints["decision_strategy"],
            )
            check_type(
                argname="argument description",
                value=description,
                expected_type=type_hints["description"],
            )
            check_type(
                argname="argument policies",
                value=policies,
                expected_type=type_hints["policies"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if decision_strategy is not None:
            self._values["decision_strategy"] = decision_strategy
        if description is not None:
            self._values["description"] = description
        if policies is not None:
            self._values["policies"] = policies

    @builtins.property
    def decision_strategy(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#decision_strategy UsersPermissions#decision_strategy}."""
        result = self._values.get("decision_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#description UsersPermissions#description}."""
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policies(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#policies UsersPermissions#policies}."""
        result = self._values.get("policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UsersPermissionsImpersonateScope(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class UsersPermissionsImpersonateScopeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.usersPermissions.UsersPermissionsImpersonateScopeOutputReference",
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
                _typecheckingstub__f21b315c46adf2973dbfda760d48793e08519ff419dac78e602a4d0411105614
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

    @jsii.member(jsii_name="resetDecisionStrategy")
    def reset_decision_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDecisionStrategy", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetPolicies")
    def reset_policies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicies", []))

    @builtins.property
    @jsii.member(jsii_name="decisionStrategyInput")
    def decision_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "decisionStrategyInput")
        )

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "descriptionInput")
        )

    @builtins.property
    @jsii.member(jsii_name="policiesInput")
    def policies_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]], jsii.get(self, "policiesInput")
        )

    @builtins.property
    @jsii.member(jsii_name="decisionStrategy")
    def decision_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "decisionStrategy"))

    @decision_strategy.setter
    def decision_strategy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__12a509d13f62e74713866f4027d031da31996e1ff57319b1436bd6e7bdb17b85
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "decisionStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__0fb50c7854d979489c307500e77d9a01a5f1e7bf37288879cefc03ce54510ccc
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="policies")
    def policies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "policies"))

    @policies.setter
    def policies(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__e672857aa3f9814f4ba0b0e56f37efd28a9e0907a33fd18d9be5d6a1b1c64b56
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "policies", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[UsersPermissionsImpersonateScope]:
        return typing.cast(
            typing.Optional[UsersPermissionsImpersonateScope],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[UsersPermissionsImpersonateScope],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__990af648fe64fa6c2c52041670805cdd301b8a8f2ae1aec5e1db472613d007eb
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="keycloak.usersPermissions.UsersPermissionsManageGroupMembershipScope",
    jsii_struct_bases=[],
    name_mapping={
        "decision_strategy": "decisionStrategy",
        "description": "description",
        "policies": "policies",
    },
)
class UsersPermissionsManageGroupMembershipScope:
    def __init__(
        self,
        *,
        decision_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#decision_strategy UsersPermissions#decision_strategy}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#description UsersPermissions#description}.
        :param policies: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#policies UsersPermissions#policies}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d6a31e389b19236e50f8e7d10d249ace1f6343a4885a9e16b9c2974469e32fd1
            )
            check_type(
                argname="argument decision_strategy",
                value=decision_strategy,
                expected_type=type_hints["decision_strategy"],
            )
            check_type(
                argname="argument description",
                value=description,
                expected_type=type_hints["description"],
            )
            check_type(
                argname="argument policies",
                value=policies,
                expected_type=type_hints["policies"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if decision_strategy is not None:
            self._values["decision_strategy"] = decision_strategy
        if description is not None:
            self._values["description"] = description
        if policies is not None:
            self._values["policies"] = policies

    @builtins.property
    def decision_strategy(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#decision_strategy UsersPermissions#decision_strategy}."""
        result = self._values.get("decision_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#description UsersPermissions#description}."""
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policies(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#policies UsersPermissions#policies}."""
        result = self._values.get("policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UsersPermissionsManageGroupMembershipScope(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class UsersPermissionsManageGroupMembershipScopeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.usersPermissions.UsersPermissionsManageGroupMembershipScopeOutputReference",
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
                _typecheckingstub__988d4373585be4cb719b03defca86f6ef321edd045800c00fa99f7f2a9a22e54
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

    @jsii.member(jsii_name="resetDecisionStrategy")
    def reset_decision_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDecisionStrategy", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetPolicies")
    def reset_policies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicies", []))

    @builtins.property
    @jsii.member(jsii_name="decisionStrategyInput")
    def decision_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "decisionStrategyInput")
        )

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "descriptionInput")
        )

    @builtins.property
    @jsii.member(jsii_name="policiesInput")
    def policies_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]], jsii.get(self, "policiesInput")
        )

    @builtins.property
    @jsii.member(jsii_name="decisionStrategy")
    def decision_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "decisionStrategy"))

    @decision_strategy.setter
    def decision_strategy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__120633b4087c45d7237446d749ee3ef24292c73d7fda1817d9b0577c70ae5ef4
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "decisionStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__04dad1a566943e385143ecf1d437ea2b4a5c5fef6073ce83439d27812c4143aa
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="policies")
    def policies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "policies"))

    @policies.setter
    def policies(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__ee913fcd1a04496151d577b61a106f01c6cb87143bf2ecc8f87ddb0bf3ce8847
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "policies", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[UsersPermissionsManageGroupMembershipScope]:
        return typing.cast(
            typing.Optional[UsersPermissionsManageGroupMembershipScope],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[UsersPermissionsManageGroupMembershipScope],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__81ae768c4e9d05cf0aa0c03f91b7f5781c3ef47bc0493b30ae747aebce565248
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="keycloak.usersPermissions.UsersPermissionsManageScope",
    jsii_struct_bases=[],
    name_mapping={
        "decision_strategy": "decisionStrategy",
        "description": "description",
        "policies": "policies",
    },
)
class UsersPermissionsManageScope:
    def __init__(
        self,
        *,
        decision_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#decision_strategy UsersPermissions#decision_strategy}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#description UsersPermissions#description}.
        :param policies: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#policies UsersPermissions#policies}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__bbf69f8f9ed61234a8fee73650fe276d68df6688a883d7c4427b5efeddea435d
            )
            check_type(
                argname="argument decision_strategy",
                value=decision_strategy,
                expected_type=type_hints["decision_strategy"],
            )
            check_type(
                argname="argument description",
                value=description,
                expected_type=type_hints["description"],
            )
            check_type(
                argname="argument policies",
                value=policies,
                expected_type=type_hints["policies"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if decision_strategy is not None:
            self._values["decision_strategy"] = decision_strategy
        if description is not None:
            self._values["description"] = description
        if policies is not None:
            self._values["policies"] = policies

    @builtins.property
    def decision_strategy(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#decision_strategy UsersPermissions#decision_strategy}."""
        result = self._values.get("decision_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#description UsersPermissions#description}."""
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policies(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#policies UsersPermissions#policies}."""
        result = self._values.get("policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UsersPermissionsManageScope(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class UsersPermissionsManageScopeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.usersPermissions.UsersPermissionsManageScopeOutputReference",
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
                _typecheckingstub__5b8028ac7cf88f5b878d28bf7bcfa8736f335b9358bfa30897e5dd13632619bd
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

    @jsii.member(jsii_name="resetDecisionStrategy")
    def reset_decision_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDecisionStrategy", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetPolicies")
    def reset_policies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicies", []))

    @builtins.property
    @jsii.member(jsii_name="decisionStrategyInput")
    def decision_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "decisionStrategyInput")
        )

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "descriptionInput")
        )

    @builtins.property
    @jsii.member(jsii_name="policiesInput")
    def policies_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]], jsii.get(self, "policiesInput")
        )

    @builtins.property
    @jsii.member(jsii_name="decisionStrategy")
    def decision_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "decisionStrategy"))

    @decision_strategy.setter
    def decision_strategy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__1c889e9bc9352605e7fb3bb50290d956a9b5f26b33f239bfd612c8fe6550cf53
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "decisionStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__bc64938206f41dd14af2fb2a77c02566934499ffcf086e7464846946e35e33c7
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="policies")
    def policies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "policies"))

    @policies.setter
    def policies(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a921ac248c1c8b50bf21ada1e7402476dc2e82a9c58ebf496c5a51be9e970c1b
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "policies", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[UsersPermissionsManageScope]:
        return typing.cast(
            typing.Optional[UsersPermissionsManageScope],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[UsersPermissionsManageScope],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__99644c1e947eb4d7c45671c086aa0f45a532afe5b5d207360b93caa327ec0bef
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="keycloak.usersPermissions.UsersPermissionsMapRolesScope",
    jsii_struct_bases=[],
    name_mapping={
        "decision_strategy": "decisionStrategy",
        "description": "description",
        "policies": "policies",
    },
)
class UsersPermissionsMapRolesScope:
    def __init__(
        self,
        *,
        decision_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#decision_strategy UsersPermissions#decision_strategy}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#description UsersPermissions#description}.
        :param policies: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#policies UsersPermissions#policies}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__e9a40aa4fa19f30a7574affecc1f3b775a64ee7ad5bbca6775225d79f9dc0bbb
            )
            check_type(
                argname="argument decision_strategy",
                value=decision_strategy,
                expected_type=type_hints["decision_strategy"],
            )
            check_type(
                argname="argument description",
                value=description,
                expected_type=type_hints["description"],
            )
            check_type(
                argname="argument policies",
                value=policies,
                expected_type=type_hints["policies"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if decision_strategy is not None:
            self._values["decision_strategy"] = decision_strategy
        if description is not None:
            self._values["description"] = description
        if policies is not None:
            self._values["policies"] = policies

    @builtins.property
    def decision_strategy(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#decision_strategy UsersPermissions#decision_strategy}."""
        result = self._values.get("decision_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#description UsersPermissions#description}."""
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policies(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#policies UsersPermissions#policies}."""
        result = self._values.get("policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UsersPermissionsMapRolesScope(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class UsersPermissionsMapRolesScopeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.usersPermissions.UsersPermissionsMapRolesScopeOutputReference",
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
                _typecheckingstub__0e5a01704ad82a2f08d2c06689666947585aba1c2f805be30411784a39db7d19
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

    @jsii.member(jsii_name="resetDecisionStrategy")
    def reset_decision_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDecisionStrategy", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetPolicies")
    def reset_policies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicies", []))

    @builtins.property
    @jsii.member(jsii_name="decisionStrategyInput")
    def decision_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "decisionStrategyInput")
        )

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "descriptionInput")
        )

    @builtins.property
    @jsii.member(jsii_name="policiesInput")
    def policies_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]], jsii.get(self, "policiesInput")
        )

    @builtins.property
    @jsii.member(jsii_name="decisionStrategy")
    def decision_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "decisionStrategy"))

    @decision_strategy.setter
    def decision_strategy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__cd59b12525ba47ddbb717dadb5e746a797e3f7291a0c0494a5da45098a248fe1
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "decisionStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b7fbba099ce41d1b4c0b0dddb2349ba223bb6720f54fc02cab6185ad33cf5a00
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="policies")
    def policies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "policies"))

    @policies.setter
    def policies(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b990d4ecbca07c9e61faf6ba68ec039ee325d38fa27a986a54f059a2a06a2739
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "policies", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[UsersPermissionsMapRolesScope]:
        return typing.cast(
            typing.Optional[UsersPermissionsMapRolesScope],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[UsersPermissionsMapRolesScope],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b4be6695bb91e644921b8a324b3263e1d2efe2726670a2a9411afc74f9414c5f
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="keycloak.usersPermissions.UsersPermissionsUserImpersonatedScope",
    jsii_struct_bases=[],
    name_mapping={
        "decision_strategy": "decisionStrategy",
        "description": "description",
        "policies": "policies",
    },
)
class UsersPermissionsUserImpersonatedScope:
    def __init__(
        self,
        *,
        decision_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#decision_strategy UsersPermissions#decision_strategy}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#description UsersPermissions#description}.
        :param policies: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#policies UsersPermissions#policies}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__3ad266a40f0017e83f8763a263622387385dbbee2438251d0e230effe3c50abd
            )
            check_type(
                argname="argument decision_strategy",
                value=decision_strategy,
                expected_type=type_hints["decision_strategy"],
            )
            check_type(
                argname="argument description",
                value=description,
                expected_type=type_hints["description"],
            )
            check_type(
                argname="argument policies",
                value=policies,
                expected_type=type_hints["policies"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if decision_strategy is not None:
            self._values["decision_strategy"] = decision_strategy
        if description is not None:
            self._values["description"] = description
        if policies is not None:
            self._values["policies"] = policies

    @builtins.property
    def decision_strategy(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#decision_strategy UsersPermissions#decision_strategy}."""
        result = self._values.get("decision_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#description UsersPermissions#description}."""
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policies(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#policies UsersPermissions#policies}."""
        result = self._values.get("policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UsersPermissionsUserImpersonatedScope(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class UsersPermissionsUserImpersonatedScopeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.usersPermissions.UsersPermissionsUserImpersonatedScopeOutputReference",
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
                _typecheckingstub__c6f0909cb448463fc5b2791b23171dfdd39138fa54f8a70a8892e649dbc19428
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

    @jsii.member(jsii_name="resetDecisionStrategy")
    def reset_decision_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDecisionStrategy", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetPolicies")
    def reset_policies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicies", []))

    @builtins.property
    @jsii.member(jsii_name="decisionStrategyInput")
    def decision_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "decisionStrategyInput")
        )

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "descriptionInput")
        )

    @builtins.property
    @jsii.member(jsii_name="policiesInput")
    def policies_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]], jsii.get(self, "policiesInput")
        )

    @builtins.property
    @jsii.member(jsii_name="decisionStrategy")
    def decision_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "decisionStrategy"))

    @decision_strategy.setter
    def decision_strategy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__ffa0e6ea5f386926cf2f35a894b5da0c3c1049ce499ca17ec75b0bbfc5ab4ac2
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "decisionStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__99d149474bd314d90ddc7756fafff709f28d9d2ed3813acdf33ef336ddc63366
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="policies")
    def policies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "policies"))

    @policies.setter
    def policies(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d28e525266dc54673c33b7ece159162a1957bca661b5812eb8cbe8aec0901179
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "policies", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[UsersPermissionsUserImpersonatedScope]:
        return typing.cast(
            typing.Optional[UsersPermissionsUserImpersonatedScope],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[UsersPermissionsUserImpersonatedScope],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d224ce541da755981e609183bdb19dfdaafe79727856152d2326b27d2a92ff00
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="keycloak.usersPermissions.UsersPermissionsViewScope",
    jsii_struct_bases=[],
    name_mapping={
        "decision_strategy": "decisionStrategy",
        "description": "description",
        "policies": "policies",
    },
)
class UsersPermissionsViewScope:
    def __init__(
        self,
        *,
        decision_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#decision_strategy UsersPermissions#decision_strategy}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#description UsersPermissions#description}.
        :param policies: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#policies UsersPermissions#policies}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__6f63bad4f84f6b31eb3fbb582d42c7f68e1a6db8b7f59d3a8258122d91f756a5
            )
            check_type(
                argname="argument decision_strategy",
                value=decision_strategy,
                expected_type=type_hints["decision_strategy"],
            )
            check_type(
                argname="argument description",
                value=description,
                expected_type=type_hints["description"],
            )
            check_type(
                argname="argument policies",
                value=policies,
                expected_type=type_hints["policies"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if decision_strategy is not None:
            self._values["decision_strategy"] = decision_strategy
        if description is not None:
            self._values["description"] = description
        if policies is not None:
            self._values["policies"] = policies

    @builtins.property
    def decision_strategy(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#decision_strategy UsersPermissions#decision_strategy}."""
        result = self._values.get("decision_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#description UsersPermissions#description}."""
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policies(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/users_permissions#policies UsersPermissions#policies}."""
        result = self._values.get("policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UsersPermissionsViewScope(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class UsersPermissionsViewScopeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.usersPermissions.UsersPermissionsViewScopeOutputReference",
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
                _typecheckingstub__bdf9a75e232eb8e9de084200069342e86164c479e241c75a1c8e879384797735
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

    @jsii.member(jsii_name="resetDecisionStrategy")
    def reset_decision_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDecisionStrategy", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetPolicies")
    def reset_policies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicies", []))

    @builtins.property
    @jsii.member(jsii_name="decisionStrategyInput")
    def decision_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "decisionStrategyInput")
        )

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "descriptionInput")
        )

    @builtins.property
    @jsii.member(jsii_name="policiesInput")
    def policies_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]], jsii.get(self, "policiesInput")
        )

    @builtins.property
    @jsii.member(jsii_name="decisionStrategy")
    def decision_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "decisionStrategy"))

    @decision_strategy.setter
    def decision_strategy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__c1ce69af30664647ca070041c457ffb8ba1cc19863498c68df8307306b3719f1
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "decisionStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__e216f1af59d9686190e61d17c3c7d665c27b2f8dee9b2eee339b466acdd9d850
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="policies")
    def policies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "policies"))

    @policies.setter
    def policies(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__7917e57bcaa2b4b8cd3ad13f4149042686237ec9d36c1821b48f6656c22caf36
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "policies", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[UsersPermissionsViewScope]:
        return typing.cast(
            typing.Optional[UsersPermissionsViewScope], jsii.get(self, "internalValue")
        )

    @internal_value.setter
    def internal_value(self, value: typing.Optional[UsersPermissionsViewScope]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__0b6a28bf743b990723ac7c75064c1ae2f4cc6594e3153ef7ee4cb19b3bc4efec
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


__all__ = [
    "UsersPermissions",
    "UsersPermissionsConfig",
    "UsersPermissionsImpersonateScope",
    "UsersPermissionsImpersonateScopeOutputReference",
    "UsersPermissionsManageGroupMembershipScope",
    "UsersPermissionsManageGroupMembershipScopeOutputReference",
    "UsersPermissionsManageScope",
    "UsersPermissionsManageScopeOutputReference",
    "UsersPermissionsMapRolesScope",
    "UsersPermissionsMapRolesScopeOutputReference",
    "UsersPermissionsUserImpersonatedScope",
    "UsersPermissionsUserImpersonatedScopeOutputReference",
    "UsersPermissionsViewScope",
    "UsersPermissionsViewScopeOutputReference",
]

publication.publish()


def _typecheckingstub__bd1657c6a562d672dfaf8ba32f43d9c3c8b33e9b0e3dcb17f68bdfbf46d59bdd(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    realm_id: builtins.str,
    id: typing.Optional[builtins.str] = None,
    impersonate_scope: typing.Optional[
        typing.Union[
            UsersPermissionsImpersonateScope, typing.Dict[builtins.str, typing.Any]
        ]
    ] = None,
    manage_group_membership_scope: typing.Optional[
        typing.Union[
            UsersPermissionsManageGroupMembershipScope,
            typing.Dict[builtins.str, typing.Any],
        ]
    ] = None,
    manage_scope: typing.Optional[
        typing.Union[UsersPermissionsManageScope, typing.Dict[builtins.str, typing.Any]]
    ] = None,
    map_roles_scope: typing.Optional[
        typing.Union[
            UsersPermissionsMapRolesScope, typing.Dict[builtins.str, typing.Any]
        ]
    ] = None,
    user_impersonated_scope: typing.Optional[
        typing.Union[
            UsersPermissionsUserImpersonatedScope, typing.Dict[builtins.str, typing.Any]
        ]
    ] = None,
    view_scope: typing.Optional[
        typing.Union[UsersPermissionsViewScope, typing.Dict[builtins.str, typing.Any]]
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


def _typecheckingstub__76c10215b4ad309648d6969599bbbd216f9bb4e3770f5107d5d4b307731f4665(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b993479f743088d584308ae4eede394cd9946dce71e7a98818872ece0eea0a30(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__447c84f5e9847e1d42dcca058212a205b2f16f25ebf4e9745ec04588a4aa3a8d(
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
    id: typing.Optional[builtins.str] = None,
    impersonate_scope: typing.Optional[
        typing.Union[
            UsersPermissionsImpersonateScope, typing.Dict[builtins.str, typing.Any]
        ]
    ] = None,
    manage_group_membership_scope: typing.Optional[
        typing.Union[
            UsersPermissionsManageGroupMembershipScope,
            typing.Dict[builtins.str, typing.Any],
        ]
    ] = None,
    manage_scope: typing.Optional[
        typing.Union[UsersPermissionsManageScope, typing.Dict[builtins.str, typing.Any]]
    ] = None,
    map_roles_scope: typing.Optional[
        typing.Union[
            UsersPermissionsMapRolesScope, typing.Dict[builtins.str, typing.Any]
        ]
    ] = None,
    user_impersonated_scope: typing.Optional[
        typing.Union[
            UsersPermissionsUserImpersonatedScope, typing.Dict[builtins.str, typing.Any]
        ]
    ] = None,
    view_scope: typing.Optional[
        typing.Union[UsersPermissionsViewScope, typing.Dict[builtins.str, typing.Any]]
    ] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__48b37f85c9c01b01c5a2af390a5d6b7f700edc29b2b3849aa36321cb5b27d00c(
    *,
    decision_strategy: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    policies: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f21b315c46adf2973dbfda760d48793e08519ff419dac78e602a4d0411105614(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__12a509d13f62e74713866f4027d031da31996e1ff57319b1436bd6e7bdb17b85(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0fb50c7854d979489c307500e77d9a01a5f1e7bf37288879cefc03ce54510ccc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e672857aa3f9814f4ba0b0e56f37efd28a9e0907a33fd18d9be5d6a1b1c64b56(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__990af648fe64fa6c2c52041670805cdd301b8a8f2ae1aec5e1db472613d007eb(
    value: typing.Optional[UsersPermissionsImpersonateScope],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d6a31e389b19236e50f8e7d10d249ace1f6343a4885a9e16b9c2974469e32fd1(
    *,
    decision_strategy: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    policies: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__988d4373585be4cb719b03defca86f6ef321edd045800c00fa99f7f2a9a22e54(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__120633b4087c45d7237446d749ee3ef24292c73d7fda1817d9b0577c70ae5ef4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__04dad1a566943e385143ecf1d437ea2b4a5c5fef6073ce83439d27812c4143aa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ee913fcd1a04496151d577b61a106f01c6cb87143bf2ecc8f87ddb0bf3ce8847(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__81ae768c4e9d05cf0aa0c03f91b7f5781c3ef47bc0493b30ae747aebce565248(
    value: typing.Optional[UsersPermissionsManageGroupMembershipScope],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__bbf69f8f9ed61234a8fee73650fe276d68df6688a883d7c4427b5efeddea435d(
    *,
    decision_strategy: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    policies: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__5b8028ac7cf88f5b878d28bf7bcfa8736f335b9358bfa30897e5dd13632619bd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1c889e9bc9352605e7fb3bb50290d956a9b5f26b33f239bfd612c8fe6550cf53(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__bc64938206f41dd14af2fb2a77c02566934499ffcf086e7464846946e35e33c7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a921ac248c1c8b50bf21ada1e7402476dc2e82a9c58ebf496c5a51be9e970c1b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__99644c1e947eb4d7c45671c086aa0f45a532afe5b5d207360b93caa327ec0bef(
    value: typing.Optional[UsersPermissionsManageScope],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e9a40aa4fa19f30a7574affecc1f3b775a64ee7ad5bbca6775225d79f9dc0bbb(
    *,
    decision_strategy: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    policies: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0e5a01704ad82a2f08d2c06689666947585aba1c2f805be30411784a39db7d19(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__cd59b12525ba47ddbb717dadb5e746a797e3f7291a0c0494a5da45098a248fe1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b7fbba099ce41d1b4c0b0dddb2349ba223bb6720f54fc02cab6185ad33cf5a00(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b990d4ecbca07c9e61faf6ba68ec039ee325d38fa27a986a54f059a2a06a2739(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b4be6695bb91e644921b8a324b3263e1d2efe2726670a2a9411afc74f9414c5f(
    value: typing.Optional[UsersPermissionsMapRolesScope],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3ad266a40f0017e83f8763a263622387385dbbee2438251d0e230effe3c50abd(
    *,
    decision_strategy: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    policies: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c6f0909cb448463fc5b2791b23171dfdd39138fa54f8a70a8892e649dbc19428(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ffa0e6ea5f386926cf2f35a894b5da0c3c1049ce499ca17ec75b0bbfc5ab4ac2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__99d149474bd314d90ddc7756fafff709f28d9d2ed3813acdf33ef336ddc63366(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d28e525266dc54673c33b7ece159162a1957bca661b5812eb8cbe8aec0901179(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d224ce541da755981e609183bdb19dfdaafe79727856152d2326b27d2a92ff00(
    value: typing.Optional[UsersPermissionsUserImpersonatedScope],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6f63bad4f84f6b31eb3fbb582d42c7f68e1a6db8b7f59d3a8258122d91f756a5(
    *,
    decision_strategy: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    policies: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__bdf9a75e232eb8e9de084200069342e86164c479e241c75a1c8e879384797735(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c1ce69af30664647ca070041c457ffb8ba1cc19863498c68df8307306b3719f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e216f1af59d9686190e61d17c3c7d665c27b2f8dee9b2eee339b466acdd9d850(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7917e57bcaa2b4b8cd3ad13f4149042686237ec9d36c1821b48f6656c22caf36(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0b6a28bf743b990723ac7c75064c1ae2f4cc6594e3153ef7ee4cb19b3bc4efec(
    value: typing.Optional[UsersPermissionsViewScope],
) -> None:
    """Type checking stubs"""
    pass
