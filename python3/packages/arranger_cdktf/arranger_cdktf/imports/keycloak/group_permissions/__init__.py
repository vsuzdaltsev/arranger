"""
# `keycloak_group_permissions`

Refer to the Terraform Registory for docs: [`keycloak_group_permissions`](https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions).
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


class GroupPermissions(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.groupPermissions.GroupPermissions",
):
    """Represents a {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions keycloak_group_permissions}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        group_id: builtins.str,
        realm_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        manage_membership_scope: typing.Optional[
            typing.Union[
                "GroupPermissionsManageMembershipScope",
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        manage_members_scope: typing.Optional[
            typing.Union[
                "GroupPermissionsManageMembersScope",
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        manage_scope: typing.Optional[
            typing.Union[
                "GroupPermissionsManageScope", typing.Dict[builtins.str, typing.Any]
            ]
        ] = None,
        view_members_scope: typing.Optional[
            typing.Union[
                "GroupPermissionsViewMembersScope",
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        view_scope: typing.Optional[
            typing.Union[
                "GroupPermissionsViewScope", typing.Dict[builtins.str, typing.Any]
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
        """Create a new {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions keycloak_group_permissions} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param group_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#group_id GroupPermissions#group_id}.
        :param realm_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#realm_id GroupPermissions#realm_id}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#id GroupPermissions#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param manage_membership_scope: manage_membership_scope block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#manage_membership_scope GroupPermissions#manage_membership_scope}
        :param manage_members_scope: manage_members_scope block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#manage_members_scope GroupPermissions#manage_members_scope}
        :param manage_scope: manage_scope block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#manage_scope GroupPermissions#manage_scope}
        :param view_members_scope: view_members_scope block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#view_members_scope GroupPermissions#view_members_scope}
        :param view_scope: view_scope block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#view_scope GroupPermissions#view_scope}
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
                _typecheckingstub__38f6212cdc6d6d9861a129d2698e12468a3dcdb3acc23ef896109a1339746e3f
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(
                argname="argument id_", value=id_, expected_type=type_hints["id_"]
            )
        config = GroupPermissionsConfig(
            group_id=group_id,
            realm_id=realm_id,
            id=id,
            manage_membership_scope=manage_membership_scope,
            manage_members_scope=manage_members_scope,
            manage_scope=manage_scope,
            view_members_scope=view_members_scope,
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

    @jsii.member(jsii_name="putManageMembershipScope")
    def put_manage_membership_scope(
        self,
        *,
        decision_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#decision_strategy GroupPermissions#decision_strategy}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#description GroupPermissions#description}.
        :param policies: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#policies GroupPermissions#policies}.
        """
        value = GroupPermissionsManageMembershipScope(
            decision_strategy=decision_strategy,
            description=description,
            policies=policies,
        )

        return typing.cast(None, jsii.invoke(self, "putManageMembershipScope", [value]))

    @jsii.member(jsii_name="putManageMembersScope")
    def put_manage_members_scope(
        self,
        *,
        decision_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#decision_strategy GroupPermissions#decision_strategy}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#description GroupPermissions#description}.
        :param policies: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#policies GroupPermissions#policies}.
        """
        value = GroupPermissionsManageMembersScope(
            decision_strategy=decision_strategy,
            description=description,
            policies=policies,
        )

        return typing.cast(None, jsii.invoke(self, "putManageMembersScope", [value]))

    @jsii.member(jsii_name="putManageScope")
    def put_manage_scope(
        self,
        *,
        decision_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#decision_strategy GroupPermissions#decision_strategy}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#description GroupPermissions#description}.
        :param policies: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#policies GroupPermissions#policies}.
        """
        value = GroupPermissionsManageScope(
            decision_strategy=decision_strategy,
            description=description,
            policies=policies,
        )

        return typing.cast(None, jsii.invoke(self, "putManageScope", [value]))

    @jsii.member(jsii_name="putViewMembersScope")
    def put_view_members_scope(
        self,
        *,
        decision_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#decision_strategy GroupPermissions#decision_strategy}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#description GroupPermissions#description}.
        :param policies: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#policies GroupPermissions#policies}.
        """
        value = GroupPermissionsViewMembersScope(
            decision_strategy=decision_strategy,
            description=description,
            policies=policies,
        )

        return typing.cast(None, jsii.invoke(self, "putViewMembersScope", [value]))

    @jsii.member(jsii_name="putViewScope")
    def put_view_scope(
        self,
        *,
        decision_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#decision_strategy GroupPermissions#decision_strategy}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#description GroupPermissions#description}.
        :param policies: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#policies GroupPermissions#policies}.
        """
        value = GroupPermissionsViewScope(
            decision_strategy=decision_strategy,
            description=description,
            policies=policies,
        )

        return typing.cast(None, jsii.invoke(self, "putViewScope", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetManageMembershipScope")
    def reset_manage_membership_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManageMembershipScope", []))

    @jsii.member(jsii_name="resetManageMembersScope")
    def reset_manage_members_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManageMembersScope", []))

    @jsii.member(jsii_name="resetManageScope")
    def reset_manage_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManageScope", []))

    @jsii.member(jsii_name="resetViewMembersScope")
    def reset_view_members_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetViewMembersScope", []))

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
    @jsii.member(jsii_name="manageMembershipScope")
    def manage_membership_scope(
        self,
    ) -> "GroupPermissionsManageMembershipScopeOutputReference":
        return typing.cast(
            "GroupPermissionsManageMembershipScopeOutputReference",
            jsii.get(self, "manageMembershipScope"),
        )

    @builtins.property
    @jsii.member(jsii_name="manageMembersScope")
    def manage_members_scope(
        self,
    ) -> "GroupPermissionsManageMembersScopeOutputReference":
        return typing.cast(
            "GroupPermissionsManageMembersScopeOutputReference",
            jsii.get(self, "manageMembersScope"),
        )

    @builtins.property
    @jsii.member(jsii_name="manageScope")
    def manage_scope(self) -> "GroupPermissionsManageScopeOutputReference":
        return typing.cast(
            "GroupPermissionsManageScopeOutputReference", jsii.get(self, "manageScope")
        )

    @builtins.property
    @jsii.member(jsii_name="viewMembersScope")
    def view_members_scope(self) -> "GroupPermissionsViewMembersScopeOutputReference":
        return typing.cast(
            "GroupPermissionsViewMembersScopeOutputReference",
            jsii.get(self, "viewMembersScope"),
        )

    @builtins.property
    @jsii.member(jsii_name="viewScope")
    def view_scope(self) -> "GroupPermissionsViewScopeOutputReference":
        return typing.cast(
            "GroupPermissionsViewScopeOutputReference", jsii.get(self, "viewScope")
        )

    @builtins.property
    @jsii.member(jsii_name="groupIdInput")
    def group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "groupIdInput")
        )

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="manageMembershipScopeInput")
    def manage_membership_scope_input(
        self,
    ) -> typing.Optional["GroupPermissionsManageMembershipScope"]:
        return typing.cast(
            typing.Optional["GroupPermissionsManageMembershipScope"],
            jsii.get(self, "manageMembershipScopeInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="manageMembersScopeInput")
    def manage_members_scope_input(
        self,
    ) -> typing.Optional["GroupPermissionsManageMembersScope"]:
        return typing.cast(
            typing.Optional["GroupPermissionsManageMembersScope"],
            jsii.get(self, "manageMembersScopeInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="manageScopeInput")
    def manage_scope_input(self) -> typing.Optional["GroupPermissionsManageScope"]:
        return typing.cast(
            typing.Optional["GroupPermissionsManageScope"],
            jsii.get(self, "manageScopeInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="realmIdInput")
    def realm_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "realmIdInput")
        )

    @builtins.property
    @jsii.member(jsii_name="viewMembersScopeInput")
    def view_members_scope_input(
        self,
    ) -> typing.Optional["GroupPermissionsViewMembersScope"]:
        return typing.cast(
            typing.Optional["GroupPermissionsViewMembersScope"],
            jsii.get(self, "viewMembersScopeInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="viewScopeInput")
    def view_scope_input(self) -> typing.Optional["GroupPermissionsViewScope"]:
        return typing.cast(
            typing.Optional["GroupPermissionsViewScope"],
            jsii.get(self, "viewScopeInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="groupId")
    def group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupId"))

    @group_id.setter
    def group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__5174e4c6237692952f069b132dbb9313bdc19e7986f1fa32e725ad34ac9c8a80
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "groupId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__8651debafd6ae7690137b15d26315ad2486d98f6e09f3c8a6582b4a572f4fcf6
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
                _typecheckingstub__8555effdf7d77e54cb7e5f96a9249621bfaf6d5ec01cad07ce57e2c35effd94d
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "realmId", value)


@jsii.data_type(
    jsii_type="keycloak.groupPermissions.GroupPermissionsConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "group_id": "groupId",
        "realm_id": "realmId",
        "id": "id",
        "manage_membership_scope": "manageMembershipScope",
        "manage_members_scope": "manageMembersScope",
        "manage_scope": "manageScope",
        "view_members_scope": "viewMembersScope",
        "view_scope": "viewScope",
    },
)
class GroupPermissionsConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        group_id: builtins.str,
        realm_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        manage_membership_scope: typing.Optional[
            typing.Union[
                "GroupPermissionsManageMembershipScope",
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        manage_members_scope: typing.Optional[
            typing.Union[
                "GroupPermissionsManageMembersScope",
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        manage_scope: typing.Optional[
            typing.Union[
                "GroupPermissionsManageScope", typing.Dict[builtins.str, typing.Any]
            ]
        ] = None,
        view_members_scope: typing.Optional[
            typing.Union[
                "GroupPermissionsViewMembersScope",
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        view_scope: typing.Optional[
            typing.Union[
                "GroupPermissionsViewScope", typing.Dict[builtins.str, typing.Any]
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
        :param group_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#group_id GroupPermissions#group_id}.
        :param realm_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#realm_id GroupPermissions#realm_id}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#id GroupPermissions#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param manage_membership_scope: manage_membership_scope block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#manage_membership_scope GroupPermissions#manage_membership_scope}
        :param manage_members_scope: manage_members_scope block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#manage_members_scope GroupPermissions#manage_members_scope}
        :param manage_scope: manage_scope block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#manage_scope GroupPermissions#manage_scope}
        :param view_members_scope: view_members_scope block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#view_members_scope GroupPermissions#view_members_scope}
        :param view_scope: view_scope block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#view_scope GroupPermissions#view_scope}
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(manage_membership_scope, dict):
            manage_membership_scope = GroupPermissionsManageMembershipScope(
                **manage_membership_scope
            )
        if isinstance(manage_members_scope, dict):
            manage_members_scope = GroupPermissionsManageMembersScope(
                **manage_members_scope
            )
        if isinstance(manage_scope, dict):
            manage_scope = GroupPermissionsManageScope(**manage_scope)
        if isinstance(view_members_scope, dict):
            view_members_scope = GroupPermissionsViewMembersScope(**view_members_scope)
        if isinstance(view_scope, dict):
            view_scope = GroupPermissionsViewScope(**view_scope)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__740f4930faaf7edd52489c3dada6cd3aa496fee8c06fcc47cdcc389df65ecd21
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
                argname="argument group_id",
                value=group_id,
                expected_type=type_hints["group_id"],
            )
            check_type(
                argname="argument realm_id",
                value=realm_id,
                expected_type=type_hints["realm_id"],
            )
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(
                argname="argument manage_membership_scope",
                value=manage_membership_scope,
                expected_type=type_hints["manage_membership_scope"],
            )
            check_type(
                argname="argument manage_members_scope",
                value=manage_members_scope,
                expected_type=type_hints["manage_members_scope"],
            )
            check_type(
                argname="argument manage_scope",
                value=manage_scope,
                expected_type=type_hints["manage_scope"],
            )
            check_type(
                argname="argument view_members_scope",
                value=view_members_scope,
                expected_type=type_hints["view_members_scope"],
            )
            check_type(
                argname="argument view_scope",
                value=view_scope,
                expected_type=type_hints["view_scope"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "group_id": group_id,
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
        if manage_membership_scope is not None:
            self._values["manage_membership_scope"] = manage_membership_scope
        if manage_members_scope is not None:
            self._values["manage_members_scope"] = manage_members_scope
        if manage_scope is not None:
            self._values["manage_scope"] = manage_scope
        if view_members_scope is not None:
            self._values["view_members_scope"] = view_members_scope
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
    def group_id(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#group_id GroupPermissions#group_id}."""
        result = self._values.get("group_id")
        assert result is not None, "Required property 'group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def realm_id(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#realm_id GroupPermissions#realm_id}."""
        result = self._values.get("realm_id")
        assert result is not None, "Required property 'realm_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#id GroupPermissions#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def manage_membership_scope(
        self,
    ) -> typing.Optional["GroupPermissionsManageMembershipScope"]:
        """manage_membership_scope block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#manage_membership_scope GroupPermissions#manage_membership_scope}
        """
        result = self._values.get("manage_membership_scope")
        return typing.cast(
            typing.Optional["GroupPermissionsManageMembershipScope"], result
        )

    @builtins.property
    def manage_members_scope(
        self,
    ) -> typing.Optional["GroupPermissionsManageMembersScope"]:
        """manage_members_scope block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#manage_members_scope GroupPermissions#manage_members_scope}
        """
        result = self._values.get("manage_members_scope")
        return typing.cast(
            typing.Optional["GroupPermissionsManageMembersScope"], result
        )

    @builtins.property
    def manage_scope(self) -> typing.Optional["GroupPermissionsManageScope"]:
        """manage_scope block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#manage_scope GroupPermissions#manage_scope}
        """
        result = self._values.get("manage_scope")
        return typing.cast(typing.Optional["GroupPermissionsManageScope"], result)

    @builtins.property
    def view_members_scope(self) -> typing.Optional["GroupPermissionsViewMembersScope"]:
        """view_members_scope block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#view_members_scope GroupPermissions#view_members_scope}
        """
        result = self._values.get("view_members_scope")
        return typing.cast(typing.Optional["GroupPermissionsViewMembersScope"], result)

    @builtins.property
    def view_scope(self) -> typing.Optional["GroupPermissionsViewScope"]:
        """view_scope block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#view_scope GroupPermissions#view_scope}
        """
        result = self._values.get("view_scope")
        return typing.cast(typing.Optional["GroupPermissionsViewScope"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GroupPermissionsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="keycloak.groupPermissions.GroupPermissionsManageMembersScope",
    jsii_struct_bases=[],
    name_mapping={
        "decision_strategy": "decisionStrategy",
        "description": "description",
        "policies": "policies",
    },
)
class GroupPermissionsManageMembersScope:
    def __init__(
        self,
        *,
        decision_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#decision_strategy GroupPermissions#decision_strategy}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#description GroupPermissions#description}.
        :param policies: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#policies GroupPermissions#policies}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__3a38b6dbc0595eceae253a6898e7e3d327cd098dec24b734bc60adc392163953
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
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#decision_strategy GroupPermissions#decision_strategy}."""
        result = self._values.get("decision_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#description GroupPermissions#description}."""
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policies(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#policies GroupPermissions#policies}."""
        result = self._values.get("policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GroupPermissionsManageMembersScope(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GroupPermissionsManageMembersScopeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.groupPermissions.GroupPermissionsManageMembersScopeOutputReference",
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
                _typecheckingstub__50b0b61797dcf472b32f6972665e2d701840593316a721a3e1d9ad33a9f9411a
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
                _typecheckingstub__c14fd9cd8221b79aeeaaaf13f910e1bd9b26a751888d9bed4edf170a7c5d1b0d
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
                _typecheckingstub__36c116a7c6d2ac0d54c821d2132bb7c2ce5c9525d0746dcaaf3cc4b471bf4b9f
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
                _typecheckingstub__f67b33ac63b368f2c07aec8543e7f95b743fce12195a5f2bd5b0539f8e0a671e
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "policies", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GroupPermissionsManageMembersScope]:
        return typing.cast(
            typing.Optional[GroupPermissionsManageMembersScope],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GroupPermissionsManageMembersScope],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__85916ee1fb98c0e7edada7e4ed74a4fdda268a71f8a57c4c05067824c24c8799
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="keycloak.groupPermissions.GroupPermissionsManageMembershipScope",
    jsii_struct_bases=[],
    name_mapping={
        "decision_strategy": "decisionStrategy",
        "description": "description",
        "policies": "policies",
    },
)
class GroupPermissionsManageMembershipScope:
    def __init__(
        self,
        *,
        decision_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#decision_strategy GroupPermissions#decision_strategy}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#description GroupPermissions#description}.
        :param policies: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#policies GroupPermissions#policies}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__ea6b95d29a494bd0d815914ad907ef04e1c92696ced68e744fdc77df1aba08e2
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
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#decision_strategy GroupPermissions#decision_strategy}."""
        result = self._values.get("decision_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#description GroupPermissions#description}."""
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policies(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#policies GroupPermissions#policies}."""
        result = self._values.get("policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GroupPermissionsManageMembershipScope(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GroupPermissionsManageMembershipScopeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.groupPermissions.GroupPermissionsManageMembershipScopeOutputReference",
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
                _typecheckingstub__835ca507cb213759ff1d77fecf901a12b1a227bdf13c4a304c7b0642616b0887
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
                _typecheckingstub__ef8b8990f8f7f57121374e84d6d087193e4911b3ff18de32f6ef06abb4924484
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
                _typecheckingstub__7561a3961298e062a0dc8cf5abc27773dbc4b13cb6977eee51e2378ae88920d0
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
                _typecheckingstub__eb17140d341ff6ec2a47082ff9af2cd0dde4b19d9a5e4a528f792bb2915d9638
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "policies", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GroupPermissionsManageMembershipScope]:
        return typing.cast(
            typing.Optional[GroupPermissionsManageMembershipScope],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GroupPermissionsManageMembershipScope],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__e37dbcf184b2be3d59185ca6f4269baadc772280a6b8a7b919625b5f773b88cb
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="keycloak.groupPermissions.GroupPermissionsManageScope",
    jsii_struct_bases=[],
    name_mapping={
        "decision_strategy": "decisionStrategy",
        "description": "description",
        "policies": "policies",
    },
)
class GroupPermissionsManageScope:
    def __init__(
        self,
        *,
        decision_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#decision_strategy GroupPermissions#decision_strategy}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#description GroupPermissions#description}.
        :param policies: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#policies GroupPermissions#policies}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__4e9227529b363e7daea6b04ba3e5538aa34acb59626d2a7ec8f0edc702c8023b
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
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#decision_strategy GroupPermissions#decision_strategy}."""
        result = self._values.get("decision_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#description GroupPermissions#description}."""
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policies(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#policies GroupPermissions#policies}."""
        result = self._values.get("policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GroupPermissionsManageScope(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GroupPermissionsManageScopeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.groupPermissions.GroupPermissionsManageScopeOutputReference",
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
                _typecheckingstub__62bbf44efcbeebbc7b0f4d1bd1f4cde4b29f6ccf59112dbb04669d2619168348
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
                _typecheckingstub__8fa01dcf50cad1a69088305c48ea29cc42c93120884cd981068a8a1b0e459b11
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
                _typecheckingstub__ea74cf1ecc3c5dfbbea4444933abff657e03203ae94cb1f7d1d9178b9b0f8953
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
                _typecheckingstub__99de732d3be09b0c4e8eba2960e1d19dc80b1c13e12a2a89d7a924af35817bfc
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "policies", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GroupPermissionsManageScope]:
        return typing.cast(
            typing.Optional[GroupPermissionsManageScope],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GroupPermissionsManageScope],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d1bc335e361cdcff4e499fa2eb44938567d118c8034683424ff73295b261df93
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="keycloak.groupPermissions.GroupPermissionsViewMembersScope",
    jsii_struct_bases=[],
    name_mapping={
        "decision_strategy": "decisionStrategy",
        "description": "description",
        "policies": "policies",
    },
)
class GroupPermissionsViewMembersScope:
    def __init__(
        self,
        *,
        decision_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#decision_strategy GroupPermissions#decision_strategy}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#description GroupPermissions#description}.
        :param policies: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#policies GroupPermissions#policies}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__e7514b62ab43d6813a703908cbbc2ab759a350c918702fb59f56b04924b71b3a
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
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#decision_strategy GroupPermissions#decision_strategy}."""
        result = self._values.get("decision_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#description GroupPermissions#description}."""
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policies(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#policies GroupPermissions#policies}."""
        result = self._values.get("policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GroupPermissionsViewMembersScope(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GroupPermissionsViewMembersScopeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.groupPermissions.GroupPermissionsViewMembersScopeOutputReference",
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
                _typecheckingstub__9d511c6c5793782eded08f2ad63c4dc4a99f72c5f8442342e9ddfac541679e77
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
                _typecheckingstub__b97de5008ef760568bfe1703244ab9ac67b79a34823206bbe80eaecf6dbd40c9
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
                _typecheckingstub__e4cae361b9049dadabba91f31c3d4a7ba92a381201e37273f4eee85fd66d0321
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
                _typecheckingstub__aa18362791253a55870959ac4872e0b2b33a627749e585f266fd5d3c2ab7c304
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "policies", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GroupPermissionsViewMembersScope]:
        return typing.cast(
            typing.Optional[GroupPermissionsViewMembersScope],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GroupPermissionsViewMembersScope],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__0b8e3b0b805edb00c41a41e61b2c996e887edc5ed5672278767dff2755cef865
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="keycloak.groupPermissions.GroupPermissionsViewScope",
    jsii_struct_bases=[],
    name_mapping={
        "decision_strategy": "decisionStrategy",
        "description": "description",
        "policies": "policies",
    },
)
class GroupPermissionsViewScope:
    def __init__(
        self,
        *,
        decision_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#decision_strategy GroupPermissions#decision_strategy}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#description GroupPermissions#description}.
        :param policies: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#policies GroupPermissions#policies}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__1dcfd1d392ee00ae138d8dea7bf5a4e452e3e92b0a19f215c66a944936c89db0
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
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#decision_strategy GroupPermissions#decision_strategy}."""
        result = self._values.get("decision_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#description GroupPermissions#description}."""
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policies(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/group_permissions#policies GroupPermissions#policies}."""
        result = self._values.get("policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GroupPermissionsViewScope(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GroupPermissionsViewScopeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.groupPermissions.GroupPermissionsViewScopeOutputReference",
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
                _typecheckingstub__7839132ab90e5959b1bfeab035ff1b4ef0a3c59a54dcadc68cfc221094643c6d
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
                _typecheckingstub__1cd121a659f051b1014608a7369bdb87bdb2843ddf5bd0cc4db088870d00db00
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
                _typecheckingstub__ec8ed64c65f1edd385c2f9a936f9b09b6ad6a81260bd2783c2a1456a350a385e
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
                _typecheckingstub__3f0d519a3f350b24aa2f67819dad0ae8d48954797bf0a9c3267c6c44508500c8
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "policies", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GroupPermissionsViewScope]:
        return typing.cast(
            typing.Optional[GroupPermissionsViewScope], jsii.get(self, "internalValue")
        )

    @internal_value.setter
    def internal_value(self, value: typing.Optional[GroupPermissionsViewScope]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__5109b73baec3f15df19d6c6e2bc5441862d4af0f8f5dbcf5981f03e44bd09e9a
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


__all__ = [
    "GroupPermissions",
    "GroupPermissionsConfig",
    "GroupPermissionsManageMembersScope",
    "GroupPermissionsManageMembersScopeOutputReference",
    "GroupPermissionsManageMembershipScope",
    "GroupPermissionsManageMembershipScopeOutputReference",
    "GroupPermissionsManageScope",
    "GroupPermissionsManageScopeOutputReference",
    "GroupPermissionsViewMembersScope",
    "GroupPermissionsViewMembersScopeOutputReference",
    "GroupPermissionsViewScope",
    "GroupPermissionsViewScopeOutputReference",
]

publication.publish()


def _typecheckingstub__38f6212cdc6d6d9861a129d2698e12468a3dcdb3acc23ef896109a1339746e3f(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    group_id: builtins.str,
    realm_id: builtins.str,
    id: typing.Optional[builtins.str] = None,
    manage_membership_scope: typing.Optional[
        typing.Union[
            GroupPermissionsManageMembershipScope, typing.Dict[builtins.str, typing.Any]
        ]
    ] = None,
    manage_members_scope: typing.Optional[
        typing.Union[
            GroupPermissionsManageMembersScope, typing.Dict[builtins.str, typing.Any]
        ]
    ] = None,
    manage_scope: typing.Optional[
        typing.Union[GroupPermissionsManageScope, typing.Dict[builtins.str, typing.Any]]
    ] = None,
    view_members_scope: typing.Optional[
        typing.Union[
            GroupPermissionsViewMembersScope, typing.Dict[builtins.str, typing.Any]
        ]
    ] = None,
    view_scope: typing.Optional[
        typing.Union[GroupPermissionsViewScope, typing.Dict[builtins.str, typing.Any]]
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


def _typecheckingstub__5174e4c6237692952f069b132dbb9313bdc19e7986f1fa32e725ad34ac9c8a80(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8651debafd6ae7690137b15d26315ad2486d98f6e09f3c8a6582b4a572f4fcf6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8555effdf7d77e54cb7e5f96a9249621bfaf6d5ec01cad07ce57e2c35effd94d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__740f4930faaf7edd52489c3dada6cd3aa496fee8c06fcc47cdcc389df65ecd21(
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
    group_id: builtins.str,
    realm_id: builtins.str,
    id: typing.Optional[builtins.str] = None,
    manage_membership_scope: typing.Optional[
        typing.Union[
            GroupPermissionsManageMembershipScope, typing.Dict[builtins.str, typing.Any]
        ]
    ] = None,
    manage_members_scope: typing.Optional[
        typing.Union[
            GroupPermissionsManageMembersScope, typing.Dict[builtins.str, typing.Any]
        ]
    ] = None,
    manage_scope: typing.Optional[
        typing.Union[GroupPermissionsManageScope, typing.Dict[builtins.str, typing.Any]]
    ] = None,
    view_members_scope: typing.Optional[
        typing.Union[
            GroupPermissionsViewMembersScope, typing.Dict[builtins.str, typing.Any]
        ]
    ] = None,
    view_scope: typing.Optional[
        typing.Union[GroupPermissionsViewScope, typing.Dict[builtins.str, typing.Any]]
    ] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3a38b6dbc0595eceae253a6898e7e3d327cd098dec24b734bc60adc392163953(
    *,
    decision_strategy: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    policies: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__50b0b61797dcf472b32f6972665e2d701840593316a721a3e1d9ad33a9f9411a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c14fd9cd8221b79aeeaaaf13f910e1bd9b26a751888d9bed4edf170a7c5d1b0d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__36c116a7c6d2ac0d54c821d2132bb7c2ce5c9525d0746dcaaf3cc4b471bf4b9f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f67b33ac63b368f2c07aec8543e7f95b743fce12195a5f2bd5b0539f8e0a671e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__85916ee1fb98c0e7edada7e4ed74a4fdda268a71f8a57c4c05067824c24c8799(
    value: typing.Optional[GroupPermissionsManageMembersScope],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ea6b95d29a494bd0d815914ad907ef04e1c92696ced68e744fdc77df1aba08e2(
    *,
    decision_strategy: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    policies: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__835ca507cb213759ff1d77fecf901a12b1a227bdf13c4a304c7b0642616b0887(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ef8b8990f8f7f57121374e84d6d087193e4911b3ff18de32f6ef06abb4924484(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7561a3961298e062a0dc8cf5abc27773dbc4b13cb6977eee51e2378ae88920d0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__eb17140d341ff6ec2a47082ff9af2cd0dde4b19d9a5e4a528f792bb2915d9638(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e37dbcf184b2be3d59185ca6f4269baadc772280a6b8a7b919625b5f773b88cb(
    value: typing.Optional[GroupPermissionsManageMembershipScope],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4e9227529b363e7daea6b04ba3e5538aa34acb59626d2a7ec8f0edc702c8023b(
    *,
    decision_strategy: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    policies: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__62bbf44efcbeebbc7b0f4d1bd1f4cde4b29f6ccf59112dbb04669d2619168348(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8fa01dcf50cad1a69088305c48ea29cc42c93120884cd981068a8a1b0e459b11(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ea74cf1ecc3c5dfbbea4444933abff657e03203ae94cb1f7d1d9178b9b0f8953(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__99de732d3be09b0c4e8eba2960e1d19dc80b1c13e12a2a89d7a924af35817bfc(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d1bc335e361cdcff4e499fa2eb44938567d118c8034683424ff73295b261df93(
    value: typing.Optional[GroupPermissionsManageScope],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e7514b62ab43d6813a703908cbbc2ab759a350c918702fb59f56b04924b71b3a(
    *,
    decision_strategy: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    policies: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9d511c6c5793782eded08f2ad63c4dc4a99f72c5f8442342e9ddfac541679e77(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b97de5008ef760568bfe1703244ab9ac67b79a34823206bbe80eaecf6dbd40c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e4cae361b9049dadabba91f31c3d4a7ba92a381201e37273f4eee85fd66d0321(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__aa18362791253a55870959ac4872e0b2b33a627749e585f266fd5d3c2ab7c304(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0b8e3b0b805edb00c41a41e61b2c996e887edc5ed5672278767dff2755cef865(
    value: typing.Optional[GroupPermissionsViewMembersScope],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1dcfd1d392ee00ae138d8dea7bf5a4e452e3e92b0a19f215c66a944936c89db0(
    *,
    decision_strategy: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    policies: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7839132ab90e5959b1bfeab035ff1b4ef0a3c59a54dcadc68cfc221094643c6d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1cd121a659f051b1014608a7369bdb87bdb2843ddf5bd0cc4db088870d00db00(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ec8ed64c65f1edd385c2f9a936f9b09b6ad6a81260bd2783c2a1456a350a385e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3f0d519a3f350b24aa2f67819dad0ae8d48954797bf0a9c3267c6c44508500c8(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__5109b73baec3f15df19d6c6e2bc5441862d4af0f8f5dbcf5981f03e44bd09e9a(
    value: typing.Optional[GroupPermissionsViewScope],
) -> None:
    """Type checking stubs"""
    pass
