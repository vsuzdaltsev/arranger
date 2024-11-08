"""
# `keycloak_openid_client_permissions`

Refer to the Terraform Registory for docs: [`keycloak_openid_client_permissions`](https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions).
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


class OpenidClientPermissions(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.openidClientPermissions.OpenidClientPermissions",
):
    """Represents a {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions keycloak_openid_client_permissions}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        client_id: builtins.str,
        realm_id: builtins.str,
        configure_scope: typing.Optional[
            typing.Union[
                "OpenidClientPermissionsConfigureScope",
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        id: typing.Optional[builtins.str] = None,
        manage_scope: typing.Optional[
            typing.Union[
                "OpenidClientPermissionsManageScope",
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        map_roles_client_scope_scope: typing.Optional[
            typing.Union[
                "OpenidClientPermissionsMapRolesClientScopeScope",
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        map_roles_composite_scope: typing.Optional[
            typing.Union[
                "OpenidClientPermissionsMapRolesCompositeScope",
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        map_roles_scope: typing.Optional[
            typing.Union[
                "OpenidClientPermissionsMapRolesScope",
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        token_exchange_scope: typing.Optional[
            typing.Union[
                "OpenidClientPermissionsTokenExchangeScope",
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        view_scope: typing.Optional[
            typing.Union[
                "OpenidClientPermissionsViewScope",
                typing.Dict[builtins.str, typing.Any],
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
        """Create a new {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions keycloak_openid_client_permissions} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param client_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#client_id OpenidClientPermissions#client_id}.
        :param realm_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#realm_id OpenidClientPermissions#realm_id}.
        :param configure_scope: configure_scope block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#configure_scope OpenidClientPermissions#configure_scope}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#id OpenidClientPermissions#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param manage_scope: manage_scope block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#manage_scope OpenidClientPermissions#manage_scope}
        :param map_roles_client_scope_scope: map_roles_client_scope_scope block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#map_roles_client_scope_scope OpenidClientPermissions#map_roles_client_scope_scope}
        :param map_roles_composite_scope: map_roles_composite_scope block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#map_roles_composite_scope OpenidClientPermissions#map_roles_composite_scope}
        :param map_roles_scope: map_roles_scope block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#map_roles_scope OpenidClientPermissions#map_roles_scope}
        :param token_exchange_scope: token_exchange_scope block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#token_exchange_scope OpenidClientPermissions#token_exchange_scope}
        :param view_scope: view_scope block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#view_scope OpenidClientPermissions#view_scope}
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
                _typecheckingstub__dfa4654c4fe260e8089a1a8c59c8e955b00049a7409bb56888bfd19eefa1439e
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(
                argname="argument id_", value=id_, expected_type=type_hints["id_"]
            )
        config = OpenidClientPermissionsConfig(
            client_id=client_id,
            realm_id=realm_id,
            configure_scope=configure_scope,
            id=id,
            manage_scope=manage_scope,
            map_roles_client_scope_scope=map_roles_client_scope_scope,
            map_roles_composite_scope=map_roles_composite_scope,
            map_roles_scope=map_roles_scope,
            token_exchange_scope=token_exchange_scope,
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

    @jsii.member(jsii_name="putConfigureScope")
    def put_configure_scope(
        self,
        *,
        decision_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#decision_strategy OpenidClientPermissions#decision_strategy}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#description OpenidClientPermissions#description}.
        :param policies: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#policies OpenidClientPermissions#policies}.
        """
        value = OpenidClientPermissionsConfigureScope(
            decision_strategy=decision_strategy,
            description=description,
            policies=policies,
        )

        return typing.cast(None, jsii.invoke(self, "putConfigureScope", [value]))

    @jsii.member(jsii_name="putManageScope")
    def put_manage_scope(
        self,
        *,
        decision_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#decision_strategy OpenidClientPermissions#decision_strategy}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#description OpenidClientPermissions#description}.
        :param policies: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#policies OpenidClientPermissions#policies}.
        """
        value = OpenidClientPermissionsManageScope(
            decision_strategy=decision_strategy,
            description=description,
            policies=policies,
        )

        return typing.cast(None, jsii.invoke(self, "putManageScope", [value]))

    @jsii.member(jsii_name="putMapRolesClientScopeScope")
    def put_map_roles_client_scope_scope(
        self,
        *,
        decision_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#decision_strategy OpenidClientPermissions#decision_strategy}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#description OpenidClientPermissions#description}.
        :param policies: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#policies OpenidClientPermissions#policies}.
        """
        value = OpenidClientPermissionsMapRolesClientScopeScope(
            decision_strategy=decision_strategy,
            description=description,
            policies=policies,
        )

        return typing.cast(
            None, jsii.invoke(self, "putMapRolesClientScopeScope", [value])
        )

    @jsii.member(jsii_name="putMapRolesCompositeScope")
    def put_map_roles_composite_scope(
        self,
        *,
        decision_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#decision_strategy OpenidClientPermissions#decision_strategy}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#description OpenidClientPermissions#description}.
        :param policies: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#policies OpenidClientPermissions#policies}.
        """
        value = OpenidClientPermissionsMapRolesCompositeScope(
            decision_strategy=decision_strategy,
            description=description,
            policies=policies,
        )

        return typing.cast(
            None, jsii.invoke(self, "putMapRolesCompositeScope", [value])
        )

    @jsii.member(jsii_name="putMapRolesScope")
    def put_map_roles_scope(
        self,
        *,
        decision_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#decision_strategy OpenidClientPermissions#decision_strategy}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#description OpenidClientPermissions#description}.
        :param policies: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#policies OpenidClientPermissions#policies}.
        """
        value = OpenidClientPermissionsMapRolesScope(
            decision_strategy=decision_strategy,
            description=description,
            policies=policies,
        )

        return typing.cast(None, jsii.invoke(self, "putMapRolesScope", [value]))

    @jsii.member(jsii_name="putTokenExchangeScope")
    def put_token_exchange_scope(
        self,
        *,
        decision_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#decision_strategy OpenidClientPermissions#decision_strategy}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#description OpenidClientPermissions#description}.
        :param policies: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#policies OpenidClientPermissions#policies}.
        """
        value = OpenidClientPermissionsTokenExchangeScope(
            decision_strategy=decision_strategy,
            description=description,
            policies=policies,
        )

        return typing.cast(None, jsii.invoke(self, "putTokenExchangeScope", [value]))

    @jsii.member(jsii_name="putViewScope")
    def put_view_scope(
        self,
        *,
        decision_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#decision_strategy OpenidClientPermissions#decision_strategy}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#description OpenidClientPermissions#description}.
        :param policies: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#policies OpenidClientPermissions#policies}.
        """
        value = OpenidClientPermissionsViewScope(
            decision_strategy=decision_strategy,
            description=description,
            policies=policies,
        )

        return typing.cast(None, jsii.invoke(self, "putViewScope", [value]))

    @jsii.member(jsii_name="resetConfigureScope")
    def reset_configure_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigureScope", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetManageScope")
    def reset_manage_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManageScope", []))

    @jsii.member(jsii_name="resetMapRolesClientScopeScope")
    def reset_map_roles_client_scope_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMapRolesClientScopeScope", []))

    @jsii.member(jsii_name="resetMapRolesCompositeScope")
    def reset_map_roles_composite_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMapRolesCompositeScope", []))

    @jsii.member(jsii_name="resetMapRolesScope")
    def reset_map_roles_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMapRolesScope", []))

    @jsii.member(jsii_name="resetTokenExchangeScope")
    def reset_token_exchange_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenExchangeScope", []))

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
    @jsii.member(jsii_name="configureScope")
    def configure_scope(self) -> "OpenidClientPermissionsConfigureScopeOutputReference":
        return typing.cast(
            "OpenidClientPermissionsConfigureScopeOutputReference",
            jsii.get(self, "configureScope"),
        )

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "enabled"))

    @builtins.property
    @jsii.member(jsii_name="manageScope")
    def manage_scope(self) -> "OpenidClientPermissionsManageScopeOutputReference":
        return typing.cast(
            "OpenidClientPermissionsManageScopeOutputReference",
            jsii.get(self, "manageScope"),
        )

    @builtins.property
    @jsii.member(jsii_name="mapRolesClientScopeScope")
    def map_roles_client_scope_scope(
        self,
    ) -> "OpenidClientPermissionsMapRolesClientScopeScopeOutputReference":
        return typing.cast(
            "OpenidClientPermissionsMapRolesClientScopeScopeOutputReference",
            jsii.get(self, "mapRolesClientScopeScope"),
        )

    @builtins.property
    @jsii.member(jsii_name="mapRolesCompositeScope")
    def map_roles_composite_scope(
        self,
    ) -> "OpenidClientPermissionsMapRolesCompositeScopeOutputReference":
        return typing.cast(
            "OpenidClientPermissionsMapRolesCompositeScopeOutputReference",
            jsii.get(self, "mapRolesCompositeScope"),
        )

    @builtins.property
    @jsii.member(jsii_name="mapRolesScope")
    def map_roles_scope(self) -> "OpenidClientPermissionsMapRolesScopeOutputReference":
        return typing.cast(
            "OpenidClientPermissionsMapRolesScopeOutputReference",
            jsii.get(self, "mapRolesScope"),
        )

    @builtins.property
    @jsii.member(jsii_name="tokenExchangeScope")
    def token_exchange_scope(
        self,
    ) -> "OpenidClientPermissionsTokenExchangeScopeOutputReference":
        return typing.cast(
            "OpenidClientPermissionsTokenExchangeScopeOutputReference",
            jsii.get(self, "tokenExchangeScope"),
        )

    @builtins.property
    @jsii.member(jsii_name="viewScope")
    def view_scope(self) -> "OpenidClientPermissionsViewScopeOutputReference":
        return typing.cast(
            "OpenidClientPermissionsViewScopeOutputReference",
            jsii.get(self, "viewScope"),
        )

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "clientIdInput")
        )

    @builtins.property
    @jsii.member(jsii_name="configureScopeInput")
    def configure_scope_input(
        self,
    ) -> typing.Optional["OpenidClientPermissionsConfigureScope"]:
        return typing.cast(
            typing.Optional["OpenidClientPermissionsConfigureScope"],
            jsii.get(self, "configureScopeInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="manageScopeInput")
    def manage_scope_input(
        self,
    ) -> typing.Optional["OpenidClientPermissionsManageScope"]:
        return typing.cast(
            typing.Optional["OpenidClientPermissionsManageScope"],
            jsii.get(self, "manageScopeInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="mapRolesClientScopeScopeInput")
    def map_roles_client_scope_scope_input(
        self,
    ) -> typing.Optional["OpenidClientPermissionsMapRolesClientScopeScope"]:
        return typing.cast(
            typing.Optional["OpenidClientPermissionsMapRolesClientScopeScope"],
            jsii.get(self, "mapRolesClientScopeScopeInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="mapRolesCompositeScopeInput")
    def map_roles_composite_scope_input(
        self,
    ) -> typing.Optional["OpenidClientPermissionsMapRolesCompositeScope"]:
        return typing.cast(
            typing.Optional["OpenidClientPermissionsMapRolesCompositeScope"],
            jsii.get(self, "mapRolesCompositeScopeInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="mapRolesScopeInput")
    def map_roles_scope_input(
        self,
    ) -> typing.Optional["OpenidClientPermissionsMapRolesScope"]:
        return typing.cast(
            typing.Optional["OpenidClientPermissionsMapRolesScope"],
            jsii.get(self, "mapRolesScopeInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="realmIdInput")
    def realm_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "realmIdInput")
        )

    @builtins.property
    @jsii.member(jsii_name="tokenExchangeScopeInput")
    def token_exchange_scope_input(
        self,
    ) -> typing.Optional["OpenidClientPermissionsTokenExchangeScope"]:
        return typing.cast(
            typing.Optional["OpenidClientPermissionsTokenExchangeScope"],
            jsii.get(self, "tokenExchangeScopeInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="viewScopeInput")
    def view_scope_input(self) -> typing.Optional["OpenidClientPermissionsViewScope"]:
        return typing.cast(
            typing.Optional["OpenidClientPermissionsViewScope"],
            jsii.get(self, "viewScopeInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__c6446da29804b5c597b73c929f6fb2fe3b89e86f18bc2aaac12735d89505d3cb
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
                _typecheckingstub__fb1977ffa06357f83a6b3c4e1442deff191f0c29bb2843dfc389ab35f96f9345
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
                _typecheckingstub__2af61be61362f7624b102d7ea6be4d8fe1885716e3d04764897f4d0737fc580a
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "realmId", value)


@jsii.data_type(
    jsii_type="keycloak.openidClientPermissions.OpenidClientPermissionsConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "client_id": "clientId",
        "realm_id": "realmId",
        "configure_scope": "configureScope",
        "id": "id",
        "manage_scope": "manageScope",
        "map_roles_client_scope_scope": "mapRolesClientScopeScope",
        "map_roles_composite_scope": "mapRolesCompositeScope",
        "map_roles_scope": "mapRolesScope",
        "token_exchange_scope": "tokenExchangeScope",
        "view_scope": "viewScope",
    },
)
class OpenidClientPermissionsConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        client_id: builtins.str,
        realm_id: builtins.str,
        configure_scope: typing.Optional[
            typing.Union[
                "OpenidClientPermissionsConfigureScope",
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        id: typing.Optional[builtins.str] = None,
        manage_scope: typing.Optional[
            typing.Union[
                "OpenidClientPermissionsManageScope",
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        map_roles_client_scope_scope: typing.Optional[
            typing.Union[
                "OpenidClientPermissionsMapRolesClientScopeScope",
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        map_roles_composite_scope: typing.Optional[
            typing.Union[
                "OpenidClientPermissionsMapRolesCompositeScope",
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        map_roles_scope: typing.Optional[
            typing.Union[
                "OpenidClientPermissionsMapRolesScope",
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        token_exchange_scope: typing.Optional[
            typing.Union[
                "OpenidClientPermissionsTokenExchangeScope",
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        view_scope: typing.Optional[
            typing.Union[
                "OpenidClientPermissionsViewScope",
                typing.Dict[builtins.str, typing.Any],
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
        :param client_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#client_id OpenidClientPermissions#client_id}.
        :param realm_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#realm_id OpenidClientPermissions#realm_id}.
        :param configure_scope: configure_scope block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#configure_scope OpenidClientPermissions#configure_scope}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#id OpenidClientPermissions#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param manage_scope: manage_scope block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#manage_scope OpenidClientPermissions#manage_scope}
        :param map_roles_client_scope_scope: map_roles_client_scope_scope block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#map_roles_client_scope_scope OpenidClientPermissions#map_roles_client_scope_scope}
        :param map_roles_composite_scope: map_roles_composite_scope block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#map_roles_composite_scope OpenidClientPermissions#map_roles_composite_scope}
        :param map_roles_scope: map_roles_scope block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#map_roles_scope OpenidClientPermissions#map_roles_scope}
        :param token_exchange_scope: token_exchange_scope block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#token_exchange_scope OpenidClientPermissions#token_exchange_scope}
        :param view_scope: view_scope block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#view_scope OpenidClientPermissions#view_scope}
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(configure_scope, dict):
            configure_scope = OpenidClientPermissionsConfigureScope(**configure_scope)
        if isinstance(manage_scope, dict):
            manage_scope = OpenidClientPermissionsManageScope(**manage_scope)
        if isinstance(map_roles_client_scope_scope, dict):
            map_roles_client_scope_scope = (
                OpenidClientPermissionsMapRolesClientScopeScope(
                    **map_roles_client_scope_scope
                )
            )
        if isinstance(map_roles_composite_scope, dict):
            map_roles_composite_scope = OpenidClientPermissionsMapRolesCompositeScope(
                **map_roles_composite_scope
            )
        if isinstance(map_roles_scope, dict):
            map_roles_scope = OpenidClientPermissionsMapRolesScope(**map_roles_scope)
        if isinstance(token_exchange_scope, dict):
            token_exchange_scope = OpenidClientPermissionsTokenExchangeScope(
                **token_exchange_scope
            )
        if isinstance(view_scope, dict):
            view_scope = OpenidClientPermissionsViewScope(**view_scope)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__4e6e691a1b75b427f1b519f51290689cda5068b8acea9f93bc742451e5c16a9f
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
                argname="argument client_id",
                value=client_id,
                expected_type=type_hints["client_id"],
            )
            check_type(
                argname="argument realm_id",
                value=realm_id,
                expected_type=type_hints["realm_id"],
            )
            check_type(
                argname="argument configure_scope",
                value=configure_scope,
                expected_type=type_hints["configure_scope"],
            )
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(
                argname="argument manage_scope",
                value=manage_scope,
                expected_type=type_hints["manage_scope"],
            )
            check_type(
                argname="argument map_roles_client_scope_scope",
                value=map_roles_client_scope_scope,
                expected_type=type_hints["map_roles_client_scope_scope"],
            )
            check_type(
                argname="argument map_roles_composite_scope",
                value=map_roles_composite_scope,
                expected_type=type_hints["map_roles_composite_scope"],
            )
            check_type(
                argname="argument map_roles_scope",
                value=map_roles_scope,
                expected_type=type_hints["map_roles_scope"],
            )
            check_type(
                argname="argument token_exchange_scope",
                value=token_exchange_scope,
                expected_type=type_hints["token_exchange_scope"],
            )
            check_type(
                argname="argument view_scope",
                value=view_scope,
                expected_type=type_hints["view_scope"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_id": client_id,
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
        if configure_scope is not None:
            self._values["configure_scope"] = configure_scope
        if id is not None:
            self._values["id"] = id
        if manage_scope is not None:
            self._values["manage_scope"] = manage_scope
        if map_roles_client_scope_scope is not None:
            self._values["map_roles_client_scope_scope"] = map_roles_client_scope_scope
        if map_roles_composite_scope is not None:
            self._values["map_roles_composite_scope"] = map_roles_composite_scope
        if map_roles_scope is not None:
            self._values["map_roles_scope"] = map_roles_scope
        if token_exchange_scope is not None:
            self._values["token_exchange_scope"] = token_exchange_scope
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
    def client_id(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#client_id OpenidClientPermissions#client_id}."""
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def realm_id(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#realm_id OpenidClientPermissions#realm_id}."""
        result = self._values.get("realm_id")
        assert result is not None, "Required property 'realm_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configure_scope(
        self,
    ) -> typing.Optional["OpenidClientPermissionsConfigureScope"]:
        """configure_scope block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#configure_scope OpenidClientPermissions#configure_scope}
        """
        result = self._values.get("configure_scope")
        return typing.cast(
            typing.Optional["OpenidClientPermissionsConfigureScope"], result
        )

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#id OpenidClientPermissions#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def manage_scope(self) -> typing.Optional["OpenidClientPermissionsManageScope"]:
        """manage_scope block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#manage_scope OpenidClientPermissions#manage_scope}
        """
        result = self._values.get("manage_scope")
        return typing.cast(
            typing.Optional["OpenidClientPermissionsManageScope"], result
        )

    @builtins.property
    def map_roles_client_scope_scope(
        self,
    ) -> typing.Optional["OpenidClientPermissionsMapRolesClientScopeScope"]:
        """map_roles_client_scope_scope block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#map_roles_client_scope_scope OpenidClientPermissions#map_roles_client_scope_scope}
        """
        result = self._values.get("map_roles_client_scope_scope")
        return typing.cast(
            typing.Optional["OpenidClientPermissionsMapRolesClientScopeScope"], result
        )

    @builtins.property
    def map_roles_composite_scope(
        self,
    ) -> typing.Optional["OpenidClientPermissionsMapRolesCompositeScope"]:
        """map_roles_composite_scope block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#map_roles_composite_scope OpenidClientPermissions#map_roles_composite_scope}
        """
        result = self._values.get("map_roles_composite_scope")
        return typing.cast(
            typing.Optional["OpenidClientPermissionsMapRolesCompositeScope"], result
        )

    @builtins.property
    def map_roles_scope(
        self,
    ) -> typing.Optional["OpenidClientPermissionsMapRolesScope"]:
        """map_roles_scope block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#map_roles_scope OpenidClientPermissions#map_roles_scope}
        """
        result = self._values.get("map_roles_scope")
        return typing.cast(
            typing.Optional["OpenidClientPermissionsMapRolesScope"], result
        )

    @builtins.property
    def token_exchange_scope(
        self,
    ) -> typing.Optional["OpenidClientPermissionsTokenExchangeScope"]:
        """token_exchange_scope block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#token_exchange_scope OpenidClientPermissions#token_exchange_scope}
        """
        result = self._values.get("token_exchange_scope")
        return typing.cast(
            typing.Optional["OpenidClientPermissionsTokenExchangeScope"], result
        )

    @builtins.property
    def view_scope(self) -> typing.Optional["OpenidClientPermissionsViewScope"]:
        """view_scope block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#view_scope OpenidClientPermissions#view_scope}
        """
        result = self._values.get("view_scope")
        return typing.cast(typing.Optional["OpenidClientPermissionsViewScope"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpenidClientPermissionsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="keycloak.openidClientPermissions.OpenidClientPermissionsConfigureScope",
    jsii_struct_bases=[],
    name_mapping={
        "decision_strategy": "decisionStrategy",
        "description": "description",
        "policies": "policies",
    },
)
class OpenidClientPermissionsConfigureScope:
    def __init__(
        self,
        *,
        decision_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#decision_strategy OpenidClientPermissions#decision_strategy}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#description OpenidClientPermissions#description}.
        :param policies: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#policies OpenidClientPermissions#policies}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__05bc697b0e37abccb5a93d05c1ad26e5c3b47ca6f71f903285a5f014e70f5862
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
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#decision_strategy OpenidClientPermissions#decision_strategy}."""
        result = self._values.get("decision_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#description OpenidClientPermissions#description}."""
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policies(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#policies OpenidClientPermissions#policies}."""
        result = self._values.get("policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpenidClientPermissionsConfigureScope(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpenidClientPermissionsConfigureScopeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.openidClientPermissions.OpenidClientPermissionsConfigureScopeOutputReference",
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
                _typecheckingstub__7f1e6b5e9d8ce7daaff514bb685ba6f5edf8c1a39fbea9e6aad572d777ce4c31
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
                _typecheckingstub__a9bc22c7ab1f179e1dce66c607c86666f173ef10ddf8bf8b4145298d75136f85
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
                _typecheckingstub__1b695314ff2c6d9c32b776706e19d0e5b22e63d30b16d41457940a05a962cf4b
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
                _typecheckingstub__7a0c0addd99dc0cff7868048c17fb1a21b0967c828fe9e45c547867f386680d7
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "policies", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OpenidClientPermissionsConfigureScope]:
        return typing.cast(
            typing.Optional[OpenidClientPermissionsConfigureScope],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpenidClientPermissionsConfigureScope],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__80c288763fb647394662acdefeff2cfdc36e7dff86af5b811a3f3be4dcc45aa8
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="keycloak.openidClientPermissions.OpenidClientPermissionsManageScope",
    jsii_struct_bases=[],
    name_mapping={
        "decision_strategy": "decisionStrategy",
        "description": "description",
        "policies": "policies",
    },
)
class OpenidClientPermissionsManageScope:
    def __init__(
        self,
        *,
        decision_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#decision_strategy OpenidClientPermissions#decision_strategy}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#description OpenidClientPermissions#description}.
        :param policies: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#policies OpenidClientPermissions#policies}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b58a7fcc1545c550c7955e5dfe1fbc521bb0fc9fbf0215a6668ef5886cf30481
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
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#decision_strategy OpenidClientPermissions#decision_strategy}."""
        result = self._values.get("decision_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#description OpenidClientPermissions#description}."""
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policies(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#policies OpenidClientPermissions#policies}."""
        result = self._values.get("policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpenidClientPermissionsManageScope(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpenidClientPermissionsManageScopeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.openidClientPermissions.OpenidClientPermissionsManageScopeOutputReference",
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
                _typecheckingstub__17466e2ce1a394bc3d7a637db8c910971860ec06f0b8412d93359ab73a510bae
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
                _typecheckingstub__c107859ef8914e1c9d4003675b2cbb4ca1fe82aa06410179393b957faeb8c6fa
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
                _typecheckingstub__d8c9bf14971a9a91cce9e690ac0f03dbca72d877b83c26f200594ab7ea78f004
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
                _typecheckingstub__59ff8db1ee146c48da09cca62f0013821cc1c04cfa2d934a59cdc37fd92b4fa2
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "policies", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OpenidClientPermissionsManageScope]:
        return typing.cast(
            typing.Optional[OpenidClientPermissionsManageScope],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpenidClientPermissionsManageScope],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__4e11d271ec3b7f78455f3b76f57fcb26e712daa8f10065e4041c505c016dee3f
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="keycloak.openidClientPermissions.OpenidClientPermissionsMapRolesClientScopeScope",
    jsii_struct_bases=[],
    name_mapping={
        "decision_strategy": "decisionStrategy",
        "description": "description",
        "policies": "policies",
    },
)
class OpenidClientPermissionsMapRolesClientScopeScope:
    def __init__(
        self,
        *,
        decision_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#decision_strategy OpenidClientPermissions#decision_strategy}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#description OpenidClientPermissions#description}.
        :param policies: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#policies OpenidClientPermissions#policies}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__e1d581551ebe5edb33b977b66a6c6430104ce2c00c66a3d9f5ba8f177df1a27b
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
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#decision_strategy OpenidClientPermissions#decision_strategy}."""
        result = self._values.get("decision_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#description OpenidClientPermissions#description}."""
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policies(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#policies OpenidClientPermissions#policies}."""
        result = self._values.get("policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpenidClientPermissionsMapRolesClientScopeScope(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpenidClientPermissionsMapRolesClientScopeScopeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.openidClientPermissions.OpenidClientPermissionsMapRolesClientScopeScopeOutputReference",
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
                _typecheckingstub__201b275bfa64eabb4ec76703c0300c4878f8ce2d0971fbdb9851521538ecc2ad
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
                _typecheckingstub__27b0f4ddb55bab9f2f485c7ec6d203dd033cc955c6e1575cfbeb6ecb972a4a19
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
                _typecheckingstub__3d9b3a9a6d663c55f463df8fb51d1a8dad8760e4a19b9273188fbae45574330d
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
                _typecheckingstub__b7feda232662e2d92cd84955ed129e70bccdc1ef584348c9249bfcfdc3cf59da
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "policies", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OpenidClientPermissionsMapRolesClientScopeScope]:
        return typing.cast(
            typing.Optional[OpenidClientPermissionsMapRolesClientScopeScope],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpenidClientPermissionsMapRolesClientScopeScope],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__9558b09c4b93eb65d4009c62360c1b324623092f9ccb007442e047dff6469048
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="keycloak.openidClientPermissions.OpenidClientPermissionsMapRolesCompositeScope",
    jsii_struct_bases=[],
    name_mapping={
        "decision_strategy": "decisionStrategy",
        "description": "description",
        "policies": "policies",
    },
)
class OpenidClientPermissionsMapRolesCompositeScope:
    def __init__(
        self,
        *,
        decision_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#decision_strategy OpenidClientPermissions#decision_strategy}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#description OpenidClientPermissions#description}.
        :param policies: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#policies OpenidClientPermissions#policies}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__37458717bbe07c6ad40ea7faba129156897c2da46167fe815e4818d9f3433a26
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
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#decision_strategy OpenidClientPermissions#decision_strategy}."""
        result = self._values.get("decision_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#description OpenidClientPermissions#description}."""
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policies(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#policies OpenidClientPermissions#policies}."""
        result = self._values.get("policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpenidClientPermissionsMapRolesCompositeScope(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpenidClientPermissionsMapRolesCompositeScopeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.openidClientPermissions.OpenidClientPermissionsMapRolesCompositeScopeOutputReference",
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
                _typecheckingstub__9667c42bf2e6754f215abfd8096c110f87fdc470cd7398b913afad62842ad6d8
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
                _typecheckingstub__7dfbeb00bcb450113fd0d5e8ccc6798837b50ce96c2d8f3bd3e044bee2af3796
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
                _typecheckingstub__e3a338541d42c0d68756ebd4784148ceac6a137b002a7dcfca1d0b0e13bc21cb
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
                _typecheckingstub__f51b9687e18d5e3f89668bfd111eff73602f87becab7526938c96bd8737f018e
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "policies", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OpenidClientPermissionsMapRolesCompositeScope]:
        return typing.cast(
            typing.Optional[OpenidClientPermissionsMapRolesCompositeScope],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpenidClientPermissionsMapRolesCompositeScope],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__fa6e84d0efc8fbf12a5f84a9e2dea7880677b882da14795d99471b03ef4a7835
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="keycloak.openidClientPermissions.OpenidClientPermissionsMapRolesScope",
    jsii_struct_bases=[],
    name_mapping={
        "decision_strategy": "decisionStrategy",
        "description": "description",
        "policies": "policies",
    },
)
class OpenidClientPermissionsMapRolesScope:
    def __init__(
        self,
        *,
        decision_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#decision_strategy OpenidClientPermissions#decision_strategy}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#description OpenidClientPermissions#description}.
        :param policies: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#policies OpenidClientPermissions#policies}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__205626b58cf13234fd595d7b234468427d174fab606d556f75e042ccfacc8c25
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
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#decision_strategy OpenidClientPermissions#decision_strategy}."""
        result = self._values.get("decision_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#description OpenidClientPermissions#description}."""
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policies(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#policies OpenidClientPermissions#policies}."""
        result = self._values.get("policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpenidClientPermissionsMapRolesScope(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpenidClientPermissionsMapRolesScopeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.openidClientPermissions.OpenidClientPermissionsMapRolesScopeOutputReference",
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
                _typecheckingstub__87b3d09022d75ee20ad07eab301935fb00538a59e48497137797477e03b53adf
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
                _typecheckingstub__0f8dbc42f82286daf4c11f4f0cfa15c20b72e9d4a57c750038d161803f3f3d6a
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
                _typecheckingstub__16447aebfebc33bfecddbae3f7798364226319dfc540b2739f142ffda26c38f1
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
                _typecheckingstub__6e993871faf2368f373c0a8bfd0624113f0b8f38154f22138b8e9eed39ddc6ff
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "policies", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OpenidClientPermissionsMapRolesScope]:
        return typing.cast(
            typing.Optional[OpenidClientPermissionsMapRolesScope],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpenidClientPermissionsMapRolesScope],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__4a00907c6f9fee3b5f6b441e9a3a2391ee18497acd1e22a29491c12bd5a0424e
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="keycloak.openidClientPermissions.OpenidClientPermissionsTokenExchangeScope",
    jsii_struct_bases=[],
    name_mapping={
        "decision_strategy": "decisionStrategy",
        "description": "description",
        "policies": "policies",
    },
)
class OpenidClientPermissionsTokenExchangeScope:
    def __init__(
        self,
        *,
        decision_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#decision_strategy OpenidClientPermissions#decision_strategy}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#description OpenidClientPermissions#description}.
        :param policies: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#policies OpenidClientPermissions#policies}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__9f3332255634e55cd15a132f8a6d89a7f2313720e6db80d9a5228f8314687f3d
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
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#decision_strategy OpenidClientPermissions#decision_strategy}."""
        result = self._values.get("decision_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#description OpenidClientPermissions#description}."""
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policies(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#policies OpenidClientPermissions#policies}."""
        result = self._values.get("policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpenidClientPermissionsTokenExchangeScope(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpenidClientPermissionsTokenExchangeScopeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.openidClientPermissions.OpenidClientPermissionsTokenExchangeScopeOutputReference",
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
                _typecheckingstub__24e824712dbc00a9c9d08e7af91414278b66a6cd027640e19a180c3669233536
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
                _typecheckingstub__484ff7aaff1bcede9c05d65e8c2e812867b4a4095bd13b67e68bc92ae972e5e4
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
                _typecheckingstub__90db7968565cb9db4a654c844e2367ea04b49880c1bc02dcf5940ba0dcaaa082
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
                _typecheckingstub__c191cb2ad4d84d1c6a959636f3bec2e8b86d21ca44a309d8d9b6d59645a210f8
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "policies", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[OpenidClientPermissionsTokenExchangeScope]:
        return typing.cast(
            typing.Optional[OpenidClientPermissionsTokenExchangeScope],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpenidClientPermissionsTokenExchangeScope],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__eccda4fa08f723d1f7b00c15dc19310adb8148f1fdadd53033607818c6208125
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="keycloak.openidClientPermissions.OpenidClientPermissionsViewScope",
    jsii_struct_bases=[],
    name_mapping={
        "decision_strategy": "decisionStrategy",
        "description": "description",
        "policies": "policies",
    },
)
class OpenidClientPermissionsViewScope:
    def __init__(
        self,
        *,
        decision_strategy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        """
        :param decision_strategy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#decision_strategy OpenidClientPermissions#decision_strategy}.
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#description OpenidClientPermissions#description}.
        :param policies: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#policies OpenidClientPermissions#policies}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d5a6ba36d7573c2679da7caf376f0ab3e238381763b5ef27a4c17524435340c3
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
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#decision_strategy OpenidClientPermissions#decision_strategy}."""
        result = self._values.get("decision_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#description OpenidClientPermissions#description}."""
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policies(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/openid_client_permissions#policies OpenidClientPermissions#policies}."""
        result = self._values.get("policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpenidClientPermissionsViewScope(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpenidClientPermissionsViewScopeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.openidClientPermissions.OpenidClientPermissionsViewScopeOutputReference",
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
                _typecheckingstub__402429416b53a51b280517b271865666e0ad82a65378fe36621a220498aaa544
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
                _typecheckingstub__c0b922d79c1508d57f67a37af836acb0c0480e6fb565259920ce524cd3ba6052
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
                _typecheckingstub__48e0fe36d857c08f4f90c37dfbf0f141be3d5f2dc1082a8a3eaa9888b4918f34
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
                _typecheckingstub__0d3fb7a63771b4c9df6e3f4eef8d7cda0390600580a1a429a0c69fd5ef35acfd
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "policies", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OpenidClientPermissionsViewScope]:
        return typing.cast(
            typing.Optional[OpenidClientPermissionsViewScope],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OpenidClientPermissionsViewScope],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__760196cf1bd7bf60f00222452aa69445fb94f25b05f0c4e7bde415db19dd94e6
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


__all__ = [
    "OpenidClientPermissions",
    "OpenidClientPermissionsConfig",
    "OpenidClientPermissionsConfigureScope",
    "OpenidClientPermissionsConfigureScopeOutputReference",
    "OpenidClientPermissionsManageScope",
    "OpenidClientPermissionsManageScopeOutputReference",
    "OpenidClientPermissionsMapRolesClientScopeScope",
    "OpenidClientPermissionsMapRolesClientScopeScopeOutputReference",
    "OpenidClientPermissionsMapRolesCompositeScope",
    "OpenidClientPermissionsMapRolesCompositeScopeOutputReference",
    "OpenidClientPermissionsMapRolesScope",
    "OpenidClientPermissionsMapRolesScopeOutputReference",
    "OpenidClientPermissionsTokenExchangeScope",
    "OpenidClientPermissionsTokenExchangeScopeOutputReference",
    "OpenidClientPermissionsViewScope",
    "OpenidClientPermissionsViewScopeOutputReference",
]

publication.publish()


def _typecheckingstub__dfa4654c4fe260e8089a1a8c59c8e955b00049a7409bb56888bfd19eefa1439e(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    client_id: builtins.str,
    realm_id: builtins.str,
    configure_scope: typing.Optional[
        typing.Union[
            OpenidClientPermissionsConfigureScope, typing.Dict[builtins.str, typing.Any]
        ]
    ] = None,
    id: typing.Optional[builtins.str] = None,
    manage_scope: typing.Optional[
        typing.Union[
            OpenidClientPermissionsManageScope, typing.Dict[builtins.str, typing.Any]
        ]
    ] = None,
    map_roles_client_scope_scope: typing.Optional[
        typing.Union[
            OpenidClientPermissionsMapRolesClientScopeScope,
            typing.Dict[builtins.str, typing.Any],
        ]
    ] = None,
    map_roles_composite_scope: typing.Optional[
        typing.Union[
            OpenidClientPermissionsMapRolesCompositeScope,
            typing.Dict[builtins.str, typing.Any],
        ]
    ] = None,
    map_roles_scope: typing.Optional[
        typing.Union[
            OpenidClientPermissionsMapRolesScope, typing.Dict[builtins.str, typing.Any]
        ]
    ] = None,
    token_exchange_scope: typing.Optional[
        typing.Union[
            OpenidClientPermissionsTokenExchangeScope,
            typing.Dict[builtins.str, typing.Any],
        ]
    ] = None,
    view_scope: typing.Optional[
        typing.Union[
            OpenidClientPermissionsViewScope, typing.Dict[builtins.str, typing.Any]
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
    """Type checking stubs"""
    pass


def _typecheckingstub__c6446da29804b5c597b73c929f6fb2fe3b89e86f18bc2aaac12735d89505d3cb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__fb1977ffa06357f83a6b3c4e1442deff191f0c29bb2843dfc389ab35f96f9345(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__2af61be61362f7624b102d7ea6be4d8fe1885716e3d04764897f4d0737fc580a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4e6e691a1b75b427f1b519f51290689cda5068b8acea9f93bc742451e5c16a9f(
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
    client_id: builtins.str,
    realm_id: builtins.str,
    configure_scope: typing.Optional[
        typing.Union[
            OpenidClientPermissionsConfigureScope, typing.Dict[builtins.str, typing.Any]
        ]
    ] = None,
    id: typing.Optional[builtins.str] = None,
    manage_scope: typing.Optional[
        typing.Union[
            OpenidClientPermissionsManageScope, typing.Dict[builtins.str, typing.Any]
        ]
    ] = None,
    map_roles_client_scope_scope: typing.Optional[
        typing.Union[
            OpenidClientPermissionsMapRolesClientScopeScope,
            typing.Dict[builtins.str, typing.Any],
        ]
    ] = None,
    map_roles_composite_scope: typing.Optional[
        typing.Union[
            OpenidClientPermissionsMapRolesCompositeScope,
            typing.Dict[builtins.str, typing.Any],
        ]
    ] = None,
    map_roles_scope: typing.Optional[
        typing.Union[
            OpenidClientPermissionsMapRolesScope, typing.Dict[builtins.str, typing.Any]
        ]
    ] = None,
    token_exchange_scope: typing.Optional[
        typing.Union[
            OpenidClientPermissionsTokenExchangeScope,
            typing.Dict[builtins.str, typing.Any],
        ]
    ] = None,
    view_scope: typing.Optional[
        typing.Union[
            OpenidClientPermissionsViewScope, typing.Dict[builtins.str, typing.Any]
        ]
    ] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__05bc697b0e37abccb5a93d05c1ad26e5c3b47ca6f71f903285a5f014e70f5862(
    *,
    decision_strategy: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    policies: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7f1e6b5e9d8ce7daaff514bb685ba6f5edf8c1a39fbea9e6aad572d777ce4c31(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a9bc22c7ab1f179e1dce66c607c86666f173ef10ddf8bf8b4145298d75136f85(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1b695314ff2c6d9c32b776706e19d0e5b22e63d30b16d41457940a05a962cf4b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7a0c0addd99dc0cff7868048c17fb1a21b0967c828fe9e45c547867f386680d7(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__80c288763fb647394662acdefeff2cfdc36e7dff86af5b811a3f3be4dcc45aa8(
    value: typing.Optional[OpenidClientPermissionsConfigureScope],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b58a7fcc1545c550c7955e5dfe1fbc521bb0fc9fbf0215a6668ef5886cf30481(
    *,
    decision_strategy: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    policies: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__17466e2ce1a394bc3d7a637db8c910971860ec06f0b8412d93359ab73a510bae(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c107859ef8914e1c9d4003675b2cbb4ca1fe82aa06410179393b957faeb8c6fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d8c9bf14971a9a91cce9e690ac0f03dbca72d877b83c26f200594ab7ea78f004(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__59ff8db1ee146c48da09cca62f0013821cc1c04cfa2d934a59cdc37fd92b4fa2(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4e11d271ec3b7f78455f3b76f57fcb26e712daa8f10065e4041c505c016dee3f(
    value: typing.Optional[OpenidClientPermissionsManageScope],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e1d581551ebe5edb33b977b66a6c6430104ce2c00c66a3d9f5ba8f177df1a27b(
    *,
    decision_strategy: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    policies: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__201b275bfa64eabb4ec76703c0300c4878f8ce2d0971fbdb9851521538ecc2ad(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__27b0f4ddb55bab9f2f485c7ec6d203dd033cc955c6e1575cfbeb6ecb972a4a19(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3d9b3a9a6d663c55f463df8fb51d1a8dad8760e4a19b9273188fbae45574330d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b7feda232662e2d92cd84955ed129e70bccdc1ef584348c9249bfcfdc3cf59da(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9558b09c4b93eb65d4009c62360c1b324623092f9ccb007442e047dff6469048(
    value: typing.Optional[OpenidClientPermissionsMapRolesClientScopeScope],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__37458717bbe07c6ad40ea7faba129156897c2da46167fe815e4818d9f3433a26(
    *,
    decision_strategy: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    policies: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9667c42bf2e6754f215abfd8096c110f87fdc470cd7398b913afad62842ad6d8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7dfbeb00bcb450113fd0d5e8ccc6798837b50ce96c2d8f3bd3e044bee2af3796(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e3a338541d42c0d68756ebd4784148ceac6a137b002a7dcfca1d0b0e13bc21cb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f51b9687e18d5e3f89668bfd111eff73602f87becab7526938c96bd8737f018e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__fa6e84d0efc8fbf12a5f84a9e2dea7880677b882da14795d99471b03ef4a7835(
    value: typing.Optional[OpenidClientPermissionsMapRolesCompositeScope],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__205626b58cf13234fd595d7b234468427d174fab606d556f75e042ccfacc8c25(
    *,
    decision_strategy: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    policies: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__87b3d09022d75ee20ad07eab301935fb00538a59e48497137797477e03b53adf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0f8dbc42f82286daf4c11f4f0cfa15c20b72e9d4a57c750038d161803f3f3d6a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__16447aebfebc33bfecddbae3f7798364226319dfc540b2739f142ffda26c38f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6e993871faf2368f373c0a8bfd0624113f0b8f38154f22138b8e9eed39ddc6ff(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4a00907c6f9fee3b5f6b441e9a3a2391ee18497acd1e22a29491c12bd5a0424e(
    value: typing.Optional[OpenidClientPermissionsMapRolesScope],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9f3332255634e55cd15a132f8a6d89a7f2313720e6db80d9a5228f8314687f3d(
    *,
    decision_strategy: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    policies: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__24e824712dbc00a9c9d08e7af91414278b66a6cd027640e19a180c3669233536(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__484ff7aaff1bcede9c05d65e8c2e812867b4a4095bd13b67e68bc92ae972e5e4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__90db7968565cb9db4a654c844e2367ea04b49880c1bc02dcf5940ba0dcaaa082(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c191cb2ad4d84d1c6a959636f3bec2e8b86d21ca44a309d8d9b6d59645a210f8(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__eccda4fa08f723d1f7b00c15dc19310adb8148f1fdadd53033607818c6208125(
    value: typing.Optional[OpenidClientPermissionsTokenExchangeScope],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d5a6ba36d7573c2679da7caf376f0ab3e238381763b5ef27a4c17524435340c3(
    *,
    decision_strategy: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    policies: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__402429416b53a51b280517b271865666e0ad82a65378fe36621a220498aaa544(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c0b922d79c1508d57f67a37af836acb0c0480e6fb565259920ce524cd3ba6052(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__48e0fe36d857c08f4f90c37dfbf0f141be3d5f2dc1082a8a3eaa9888b4918f34(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0d3fb7a63771b4c9df6e3f4eef8d7cda0390600580a1a429a0c69fd5ef35acfd(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__760196cf1bd7bf60f00222452aa69445fb94f25b05f0c4e7bde415db19dd94e6(
    value: typing.Optional[OpenidClientPermissionsViewScope],
) -> None:
    """Type checking stubs"""
    pass
