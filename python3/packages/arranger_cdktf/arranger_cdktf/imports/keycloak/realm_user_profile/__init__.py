"""
# `keycloak_realm_user_profile`

Refer to the Terraform Registory for docs: [`keycloak_realm_user_profile`](https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile).
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


class RealmUserProfile(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.realmUserProfile.RealmUserProfile",
):
    """Represents a {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile keycloak_realm_user_profile}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        realm_id: builtins.str,
        attribute: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable,
                typing.Sequence[
                    typing.Union[
                        "RealmUserProfileAttribute",
                        typing.Dict[builtins.str, typing.Any],
                    ]
                ],
            ]
        ] = None,
        group: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable,
                typing.Sequence[
                    typing.Union[
                        "RealmUserProfileGroup", typing.Dict[builtins.str, typing.Any]
                    ]
                ],
            ]
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
        """Create a new {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile keycloak_realm_user_profile} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param realm_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#realm_id RealmUserProfile#realm_id}.
        :param attribute: attribute block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#attribute RealmUserProfile#attribute}
        :param group: group block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#group RealmUserProfile#group}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#id RealmUserProfile#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
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
                _typecheckingstub__4c3250fbf605ea943f02577fb306ffdbadf9898901ed41ca21bb2f55e877c19d
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(
                argname="argument id_", value=id_, expected_type=type_hints["id_"]
            )
        config = RealmUserProfileConfig(
            realm_id=realm_id,
            attribute=attribute,
            group=group,
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

    @jsii.member(jsii_name="putAttribute")
    def put_attribute(
        self,
        value: typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    "RealmUserProfileAttribute", typing.Dict[builtins.str, typing.Any]
                ]
            ],
        ],
    ) -> None:
        """
        :param value: -
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__135a2c156ff5407923a086afb78ca9e93b817aa92d4c4acf437dac0d27070700
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        return typing.cast(None, jsii.invoke(self, "putAttribute", [value]))

    @jsii.member(jsii_name="putGroup")
    def put_group(
        self,
        value: typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    "RealmUserProfileGroup", typing.Dict[builtins.str, typing.Any]
                ]
            ],
        ],
    ) -> None:
        """
        :param value: -
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d63fcc2aacfaa14d3f25c00141e610ccb0abb2e82eac610674773f4611b2ebb7
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        return typing.cast(None, jsii.invoke(self, "putGroup", [value]))

    @jsii.member(jsii_name="resetAttribute")
    def reset_attribute(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttribute", []))

    @jsii.member(jsii_name="resetGroup")
    def reset_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroup", []))

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
    @jsii.member(jsii_name="attribute")
    def attribute(self) -> "RealmUserProfileAttributeList":
        return typing.cast("RealmUserProfileAttributeList", jsii.get(self, "attribute"))

    @builtins.property
    @jsii.member(jsii_name="group")
    def group(self) -> "RealmUserProfileGroupList":
        return typing.cast("RealmUserProfileGroupList", jsii.get(self, "group"))

    @builtins.property
    @jsii.member(jsii_name="attributeInput")
    def attribute_input(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable, typing.List["RealmUserProfileAttribute"]
        ]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable,
                    typing.List["RealmUserProfileAttribute"],
                ]
            ],
            jsii.get(self, "attributeInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="groupInput")
    def group_input(
        self,
    ) -> typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RealmUserProfileGroup"]]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable, typing.List["RealmUserProfileGroup"]
                ]
            ],
            jsii.get(self, "groupInput"),
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
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__41af7b42b93bee02963bc3135e7c09a6886e0d989a56b0d7d6f3d2c994293d99
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
                _typecheckingstub__16edd449dd0b4f80d0ff15e356d5a4f3730c2df24a2649b9ba73bccbffbe175c
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "realmId", value)


@jsii.data_type(
    jsii_type="keycloak.realmUserProfile.RealmUserProfileAttribute",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "annotations": "annotations",
        "display_name": "displayName",
        "enabled_when_scope": "enabledWhenScope",
        "group": "group",
        "permissions": "permissions",
        "required_for_roles": "requiredForRoles",
        "required_for_scopes": "requiredForScopes",
        "validator": "validator",
    },
)
class RealmUserProfileAttribute:
    def __init__(
        self,
        *,
        name: builtins.str,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        display_name: typing.Optional[builtins.str] = None,
        enabled_when_scope: typing.Optional[typing.Sequence[builtins.str]] = None,
        group: typing.Optional[builtins.str] = None,
        permissions: typing.Optional[
            typing.Union[
                "RealmUserProfileAttributePermissions",
                typing.Dict[builtins.str, typing.Any],
            ]
        ] = None,
        required_for_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        required_for_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
        validator: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable,
                typing.Sequence[
                    typing.Union[
                        "RealmUserProfileAttributeValidator",
                        typing.Dict[builtins.str, typing.Any],
                    ]
                ],
            ]
        ] = None,
    ) -> None:
        """
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#name RealmUserProfile#name}.
        :param annotations: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#annotations RealmUserProfile#annotations}.
        :param display_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#display_name RealmUserProfile#display_name}.
        :param enabled_when_scope: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#enabled_when_scope RealmUserProfile#enabled_when_scope}.
        :param group: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#group RealmUserProfile#group}.
        :param permissions: permissions block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#permissions RealmUserProfile#permissions}
        :param required_for_roles: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#required_for_roles RealmUserProfile#required_for_roles}.
        :param required_for_scopes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#required_for_scopes RealmUserProfile#required_for_scopes}.
        :param validator: validator block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#validator RealmUserProfile#validator}
        """
        if isinstance(permissions, dict):
            permissions = RealmUserProfileAttributePermissions(**permissions)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__6d2f2dce1318d6e9759c9c429a21fe25d093437b34a4fbdac7a616d4be60bd28
            )
            check_type(
                argname="argument name", value=name, expected_type=type_hints["name"]
            )
            check_type(
                argname="argument annotations",
                value=annotations,
                expected_type=type_hints["annotations"],
            )
            check_type(
                argname="argument display_name",
                value=display_name,
                expected_type=type_hints["display_name"],
            )
            check_type(
                argname="argument enabled_when_scope",
                value=enabled_when_scope,
                expected_type=type_hints["enabled_when_scope"],
            )
            check_type(
                argname="argument group", value=group, expected_type=type_hints["group"]
            )
            check_type(
                argname="argument permissions",
                value=permissions,
                expected_type=type_hints["permissions"],
            )
            check_type(
                argname="argument required_for_roles",
                value=required_for_roles,
                expected_type=type_hints["required_for_roles"],
            )
            check_type(
                argname="argument required_for_scopes",
                value=required_for_scopes,
                expected_type=type_hints["required_for_scopes"],
            )
            check_type(
                argname="argument validator",
                value=validator,
                expected_type=type_hints["validator"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if annotations is not None:
            self._values["annotations"] = annotations
        if display_name is not None:
            self._values["display_name"] = display_name
        if enabled_when_scope is not None:
            self._values["enabled_when_scope"] = enabled_when_scope
        if group is not None:
            self._values["group"] = group
        if permissions is not None:
            self._values["permissions"] = permissions
        if required_for_roles is not None:
            self._values["required_for_roles"] = required_for_roles
        if required_for_scopes is not None:
            self._values["required_for_scopes"] = required_for_scopes
        if validator is not None:
            self._values["validator"] = validator

    @builtins.property
    def name(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#name RealmUserProfile#name}."""
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#annotations RealmUserProfile#annotations}."""
        result = self._values.get("annotations")
        return typing.cast(
            typing.Optional[typing.Mapping[builtins.str, builtins.str]], result
        )

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#display_name RealmUserProfile#display_name}."""
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled_when_scope(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#enabled_when_scope RealmUserProfile#enabled_when_scope}."""
        result = self._values.get("enabled_when_scope")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def group(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#group RealmUserProfile#group}."""
        result = self._values.get("group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permissions(self) -> typing.Optional["RealmUserProfileAttributePermissions"]:
        """permissions block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#permissions RealmUserProfile#permissions}
        """
        result = self._values.get("permissions")
        return typing.cast(
            typing.Optional["RealmUserProfileAttributePermissions"], result
        )

    @builtins.property
    def required_for_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#required_for_roles RealmUserProfile#required_for_roles}."""
        result = self._values.get("required_for_roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def required_for_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#required_for_scopes RealmUserProfile#required_for_scopes}."""
        result = self._values.get("required_for_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def validator(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.List["RealmUserProfileAttributeValidator"],
        ]
    ]:
        """validator block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#validator RealmUserProfile#validator}
        """
        result = self._values.get("validator")
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable,
                    typing.List["RealmUserProfileAttributeValidator"],
                ]
            ],
            result,
        )

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RealmUserProfileAttribute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RealmUserProfileAttributeList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.realmUserProfile.RealmUserProfileAttributeList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__1b8a4c2616bf0f8817814a1b130909027555496af9bc5b109542ba5d4a7c615b
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
            check_type(
                argname="argument wraps_set",
                value=wraps_set,
                expected_type=type_hints["wraps_set"],
            )
        jsii.create(
            self.__class__, self, [terraform_resource, terraform_attribute, wraps_set]
        )

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "RealmUserProfileAttributeOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a180cec1a9a148b3d82383dff71ec7353fdad80a375f626caa8b516eb4ad239d
            )
            check_type(
                argname="argument index", value=index, expected_type=type_hints["index"]
            )
        return typing.cast(
            "RealmUserProfileAttributeOutputReference",
            jsii.invoke(self, "get", [index]),
        )

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        """The attribute on the parent resource this class is referencing."""
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__e47c57eb082e5a08306335cba1400da356c62d245cff42be8123b503cf3f6f12
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        """The parent resource."""
        return typing.cast(
            _cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource")
        )

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d1f869ccfcbd5ffdb4cf7d5ade14f6d925e96d0e38f07673c1e6f0e3b7b500ad
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        """whether the list is wrapping a set (will add tolist() to be able to access an item via an index)."""
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__e4dbc1056332dc0e83a731c90256d8e3b96e65d070f73b3062db651b7bef5320
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable, typing.List[RealmUserProfileAttribute]
        ]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable, typing.List[RealmUserProfileAttribute]
                ]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable, typing.List[RealmUserProfileAttribute]
            ]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__82a46129eb8d619bd2466dd9aec8b05a65d5a5b83c14a78287c95714a1898a8d
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


class RealmUserProfileAttributeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.realmUserProfile.RealmUserProfileAttributeOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__bbebac5ebabc1b73beaacaeae517503309d1120e651ba215bee52e35d8598347
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
            check_type(
                argname="argument complex_object_index",
                value=complex_object_index,
                expected_type=type_hints["complex_object_index"],
            )
            check_type(
                argname="argument complex_object_is_from_set",
                value=complex_object_is_from_set,
                expected_type=type_hints["complex_object_is_from_set"],
            )
        jsii.create(
            self.__class__,
            self,
            [
                terraform_resource,
                terraform_attribute,
                complex_object_index,
                complex_object_is_from_set,
            ],
        )

    @jsii.member(jsii_name="putPermissions")
    def put_permissions(
        self,
        *,
        edit: typing.Sequence[builtins.str],
        view: typing.Sequence[builtins.str],
    ) -> None:
        """
        :param edit: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#edit RealmUserProfile#edit}.
        :param view: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#view RealmUserProfile#view}.
        """
        value = RealmUserProfileAttributePermissions(edit=edit, view=view)

        return typing.cast(None, jsii.invoke(self, "putPermissions", [value]))

    @jsii.member(jsii_name="putValidator")
    def put_validator(
        self,
        value: typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    "RealmUserProfileAttributeValidator",
                    typing.Dict[builtins.str, typing.Any],
                ]
            ],
        ],
    ) -> None:
        """
        :param value: -
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a086e47d383955ef09839f3cdcef9fb694eeb71860ece3309fdc8f57ed3d2e21
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        return typing.cast(None, jsii.invoke(self, "putValidator", [value]))

    @jsii.member(jsii_name="resetAnnotations")
    def reset_annotations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnnotations", []))

    @jsii.member(jsii_name="resetDisplayName")
    def reset_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayName", []))

    @jsii.member(jsii_name="resetEnabledWhenScope")
    def reset_enabled_when_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabledWhenScope", []))

    @jsii.member(jsii_name="resetGroup")
    def reset_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroup", []))

    @jsii.member(jsii_name="resetPermissions")
    def reset_permissions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPermissions", []))

    @jsii.member(jsii_name="resetRequiredForRoles")
    def reset_required_for_roles(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequiredForRoles", []))

    @jsii.member(jsii_name="resetRequiredForScopes")
    def reset_required_for_scopes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequiredForScopes", []))

    @jsii.member(jsii_name="resetValidator")
    def reset_validator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValidator", []))

    @builtins.property
    @jsii.member(jsii_name="permissions")
    def permissions(self) -> "RealmUserProfileAttributePermissionsOutputReference":
        return typing.cast(
            "RealmUserProfileAttributePermissionsOutputReference",
            jsii.get(self, "permissions"),
        )

    @builtins.property
    @jsii.member(jsii_name="validator")
    def validator(self) -> "RealmUserProfileAttributeValidatorList":
        return typing.cast(
            "RealmUserProfileAttributeValidatorList", jsii.get(self, "validator")
        )

    @builtins.property
    @jsii.member(jsii_name="annotationsInput")
    def annotations_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(
            typing.Optional[typing.Mapping[builtins.str, builtins.str]],
            jsii.get(self, "annotationsInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "displayNameInput")
        )

    @builtins.property
    @jsii.member(jsii_name="enabledWhenScopeInput")
    def enabled_when_scope_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]],
            jsii.get(self, "enabledWhenScopeInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="groupInput")
    def group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="permissionsInput")
    def permissions_input(
        self,
    ) -> typing.Optional["RealmUserProfileAttributePermissions"]:
        return typing.cast(
            typing.Optional["RealmUserProfileAttributePermissions"],
            jsii.get(self, "permissionsInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="requiredForRolesInput")
    def required_for_roles_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]],
            jsii.get(self, "requiredForRolesInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="requiredForScopesInput")
    def required_for_scopes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]],
            jsii.get(self, "requiredForScopesInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="validatorInput")
    def validator_input(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.List["RealmUserProfileAttributeValidator"],
        ]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable,
                    typing.List["RealmUserProfileAttributeValidator"],
                ]
            ],
            jsii.get(self, "validatorInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="annotations")
    def annotations(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(
            typing.Mapping[builtins.str, builtins.str], jsii.get(self, "annotations")
        )

    @annotations.setter
    def annotations(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__40c9e7408ea317e749502a2d71de675608a277f2929149b79b2599a9e685f3e1
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__1eef879d63c0278dd0a6702ded655a26afdeee3709cbfd73bbb144ff7d42fc99
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="enabledWhenScope")
    def enabled_when_scope(self) -> typing.List[builtins.str]:
        return typing.cast(
            typing.List[builtins.str], jsii.get(self, "enabledWhenScope")
        )

    @enabled_when_scope.setter
    def enabled_when_scope(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__14487f05904dba3256ba4797e4d38d2736c35a6b33e0379a7a8b1166d084663c
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "enabledWhenScope", value)

    @builtins.property
    @jsii.member(jsii_name="group")
    def group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "group"))

    @group.setter
    def group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__063f89ab4ef5f28c6a17115ec7a1416a8ed113bdd7d82770d8614169ba48170b
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "group", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__6713b572ffe258366c0d95dbcec7d4f30019ab32959bff2772688eb3097917fd
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="requiredForRoles")
    def required_for_roles(self) -> typing.List[builtins.str]:
        return typing.cast(
            typing.List[builtins.str], jsii.get(self, "requiredForRoles")
        )

    @required_for_roles.setter
    def required_for_roles(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__0d5a157843cba5a4589535bb04615ba6064b212ca69b83e58dad5f2b6bb5e9e6
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "requiredForRoles", value)

    @builtins.property
    @jsii.member(jsii_name="requiredForScopes")
    def required_for_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(
            typing.List[builtins.str], jsii.get(self, "requiredForScopes")
        )

    @required_for_scopes.setter
    def required_for_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__5f6144b1cf0d97b68734297cca32b2fe5526aec066fc301d6823489d73af8a86
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "requiredForScopes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, RealmUserProfileAttribute]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[_cdktf_9a9027ec.IResolvable, RealmUserProfileAttribute]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, RealmUserProfileAttribute]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__8023e5fe73b10720846d1b84479270c0e95e312d0b98abaf96ef75fa1766e874
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="keycloak.realmUserProfile.RealmUserProfileAttributePermissions",
    jsii_struct_bases=[],
    name_mapping={"edit": "edit", "view": "view"},
)
class RealmUserProfileAttributePermissions:
    def __init__(
        self,
        *,
        edit: typing.Sequence[builtins.str],
        view: typing.Sequence[builtins.str],
    ) -> None:
        """
        :param edit: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#edit RealmUserProfile#edit}.
        :param view: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#view RealmUserProfile#view}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__40ab20d065858d4fcb07d851c7bbc52f9db63dd4d5dc5e5edf3ce5139ee564c2
            )
            check_type(
                argname="argument edit", value=edit, expected_type=type_hints["edit"]
            )
            check_type(
                argname="argument view", value=view, expected_type=type_hints["view"]
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "edit": edit,
            "view": view,
        }

    @builtins.property
    def edit(self) -> typing.List[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#edit RealmUserProfile#edit}."""
        result = self._values.get("edit")
        assert result is not None, "Required property 'edit' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def view(self) -> typing.List[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#view RealmUserProfile#view}."""
        result = self._values.get("view")
        assert result is not None, "Required property 'view' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RealmUserProfileAttributePermissions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RealmUserProfileAttributePermissionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.realmUserProfile.RealmUserProfileAttributePermissionsOutputReference",
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
                _typecheckingstub__3f9d7efde6aa7b32af1762230357e90c44e60352bb8c05ed24bbefa4ab7f0ca2
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

    @builtins.property
    @jsii.member(jsii_name="editInput")
    def edit_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]], jsii.get(self, "editInput")
        )

    @builtins.property
    @jsii.member(jsii_name="viewInput")
    def view_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(
            typing.Optional[typing.List[builtins.str]], jsii.get(self, "viewInput")
        )

    @builtins.property
    @jsii.member(jsii_name="edit")
    def edit(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "edit"))

    @edit.setter
    def edit(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__cfdfa56b2aa7952235602e6183a42136b5f0c3be2782f780bffa4945b518f837
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "edit", value)

    @builtins.property
    @jsii.member(jsii_name="view")
    def view(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "view"))

    @view.setter
    def view(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d59b0e0df293e353b02e6d8ff1c8d27dc9b5686c9d39b28a03978790ee61a416
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "view", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RealmUserProfileAttributePermissions]:
        return typing.cast(
            typing.Optional[RealmUserProfileAttributePermissions],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[RealmUserProfileAttributePermissions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__986d0338729529e35deb1ee70cb8d9e109a7e79b27f69571d0bd9044c6031d25
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="keycloak.realmUserProfile.RealmUserProfileAttributeValidator",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "config": "config"},
)
class RealmUserProfileAttributeValidator:
    def __init__(
        self,
        *,
        name: builtins.str,
        config: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        """
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#name RealmUserProfile#name}.
        :param config: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#config RealmUserProfile#config}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__00d66ff722ec12bf14e561539c9e0fd66931d3d7e89c9e6a2d5712cb73f8925e
            )
            check_type(
                argname="argument name", value=name, expected_type=type_hints["name"]
            )
            check_type(
                argname="argument config",
                value=config,
                expected_type=type_hints["config"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if config is not None:
            self._values["config"] = config

    @builtins.property
    def name(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#name RealmUserProfile#name}."""
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def config(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#config RealmUserProfile#config}."""
        result = self._values.get("config")
        return typing.cast(
            typing.Optional[typing.Mapping[builtins.str, builtins.str]], result
        )

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RealmUserProfileAttributeValidator(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RealmUserProfileAttributeValidatorList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.realmUserProfile.RealmUserProfileAttributeValidatorList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__90b7cb698609e68ed5763e635360ce4b4e7b285e7855cf87a9e15f363e3ddc17
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
            check_type(
                argname="argument wraps_set",
                value=wraps_set,
                expected_type=type_hints["wraps_set"],
            )
        jsii.create(
            self.__class__, self, [terraform_resource, terraform_attribute, wraps_set]
        )

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "RealmUserProfileAttributeValidatorOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d704fde626b7dc11a432522d2e234f5a41fca9365d5098589236809a82babf24
            )
            check_type(
                argname="argument index", value=index, expected_type=type_hints["index"]
            )
        return typing.cast(
            "RealmUserProfileAttributeValidatorOutputReference",
            jsii.invoke(self, "get", [index]),
        )

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        """The attribute on the parent resource this class is referencing."""
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__71e7611c0f2d6d2015cfce897b072d4ab143ed02106abd7545b9fbe2a4899392
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        """The parent resource."""
        return typing.cast(
            _cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource")
        )

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__faae8df8a1cbd302104d38de424ce8cdc445e617a2173df2bd84c9837d5c262c
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        """whether the list is wrapping a set (will add tolist() to be able to access an item via an index)."""
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__304c215f99e1b118a2366b6d48c22f803266c29a9d30d6fa64e96476035a5462
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable, typing.List[RealmUserProfileAttributeValidator]
        ]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable,
                    typing.List[RealmUserProfileAttributeValidator],
                ]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable,
                typing.List[RealmUserProfileAttributeValidator],
            ]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__abc632bff62b35a99b7a54eccf531696308a8f6f5f85df84f63ca7ffa903be2e
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


class RealmUserProfileAttributeValidatorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.realmUserProfile.RealmUserProfileAttributeValidatorOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__abdabec990f2a53c650928f1fc03fd7a0daeb0129255e1e5341f1fb6ec98cdc2
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
            check_type(
                argname="argument complex_object_index",
                value=complex_object_index,
                expected_type=type_hints["complex_object_index"],
            )
            check_type(
                argname="argument complex_object_is_from_set",
                value=complex_object_is_from_set,
                expected_type=type_hints["complex_object_is_from_set"],
            )
        jsii.create(
            self.__class__,
            self,
            [
                terraform_resource,
                terraform_attribute,
                complex_object_index,
                complex_object_is_from_set,
            ],
        )

    @jsii.member(jsii_name="resetConfig")
    def reset_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfig", []))

    @builtins.property
    @jsii.member(jsii_name="configInput")
    def config_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(
            typing.Optional[typing.Mapping[builtins.str, builtins.str]],
            jsii.get(self, "configInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="config")
    def config(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(
            typing.Mapping[builtins.str, builtins.str], jsii.get(self, "config")
        )

    @config.setter
    def config(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__7bbcf9cc575395116b99e7d330b89f8408ac39305585ac0515b4cf8058d61c94
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "config", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__5a869908a266a7592a8ad3fa7db003e254cafd7591089a10f4e72a640688db16
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, RealmUserProfileAttributeValidator]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable, RealmUserProfileAttributeValidator
                ]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable, RealmUserProfileAttributeValidator
            ]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__9e06be623fe1abd51e80ac8ad1bd5dd34de9e7f417a5cfcda19945a82193d48e
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="keycloak.realmUserProfile.RealmUserProfileConfig",
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
        "attribute": "attribute",
        "group": "group",
        "id": "id",
    },
)
class RealmUserProfileConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        attribute: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable,
                typing.Sequence[
                    typing.Union[
                        RealmUserProfileAttribute, typing.Dict[builtins.str, typing.Any]
                    ]
                ],
            ]
        ] = None,
        group: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable,
                typing.Sequence[
                    typing.Union[
                        "RealmUserProfileGroup", typing.Dict[builtins.str, typing.Any]
                    ]
                ],
            ]
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
        :param realm_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#realm_id RealmUserProfile#realm_id}.
        :param attribute: attribute block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#attribute RealmUserProfile#attribute}
        :param group: group block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#group RealmUserProfile#group}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#id RealmUserProfile#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__7616a1bb6a301f6c75a92f6e8b4b7975195d0f419da5ea7f8decf4370d513187
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
                argname="argument attribute",
                value=attribute,
                expected_type=type_hints["attribute"],
            )
            check_type(
                argname="argument group", value=group, expected_type=type_hints["group"]
            )
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
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
        if attribute is not None:
            self._values["attribute"] = attribute
        if group is not None:
            self._values["group"] = group
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
    def realm_id(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#realm_id RealmUserProfile#realm_id}."""
        result = self._values.get("realm_id")
        assert result is not None, "Required property 'realm_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attribute(
        self,
    ) -> typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable, typing.List[RealmUserProfileAttribute]
        ]
    ]:
        """attribute block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#attribute RealmUserProfile#attribute}
        """
        result = self._values.get("attribute")
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable, typing.List[RealmUserProfileAttribute]
                ]
            ],
            result,
        )

    @builtins.property
    def group(
        self,
    ) -> typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RealmUserProfileGroup"]]
    ]:
        """group block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#group RealmUserProfile#group}
        """
        result = self._values.get("group")
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable, typing.List["RealmUserProfileGroup"]
                ]
            ],
            result,
        )

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#id RealmUserProfile#id}.

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
        return "RealmUserProfileConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="keycloak.realmUserProfile.RealmUserProfileGroup",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "annotations": "annotations",
        "display_description": "displayDescription",
        "display_header": "displayHeader",
    },
)
class RealmUserProfileGroup:
    def __init__(
        self,
        *,
        name: builtins.str,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        display_description: typing.Optional[builtins.str] = None,
        display_header: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#name RealmUserProfile#name}.
        :param annotations: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#annotations RealmUserProfile#annotations}.
        :param display_description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#display_description RealmUserProfile#display_description}.
        :param display_header: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#display_header RealmUserProfile#display_header}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__5356202500e0105df66901115dd89d48a91ff964a59765e2a436307a298a694a
            )
            check_type(
                argname="argument name", value=name, expected_type=type_hints["name"]
            )
            check_type(
                argname="argument annotations",
                value=annotations,
                expected_type=type_hints["annotations"],
            )
            check_type(
                argname="argument display_description",
                value=display_description,
                expected_type=type_hints["display_description"],
            )
            check_type(
                argname="argument display_header",
                value=display_header,
                expected_type=type_hints["display_header"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if annotations is not None:
            self._values["annotations"] = annotations
        if display_description is not None:
            self._values["display_description"] = display_description
        if display_header is not None:
            self._values["display_header"] = display_header

    @builtins.property
    def name(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#name RealmUserProfile#name}."""
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#annotations RealmUserProfile#annotations}."""
        result = self._values.get("annotations")
        return typing.cast(
            typing.Optional[typing.Mapping[builtins.str, builtins.str]], result
        )

    @builtins.property
    def display_description(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#display_description RealmUserProfile#display_description}."""
        result = self._values.get("display_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_header(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_user_profile#display_header RealmUserProfile#display_header}."""
        result = self._values.get("display_header")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RealmUserProfileGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RealmUserProfileGroupList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.realmUserProfile.RealmUserProfileGroupList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a69d04b57e426d60d1184208b3137fa2dd7e40afb8b6e4bfcbe0e72b4759c9bc
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
            check_type(
                argname="argument wraps_set",
                value=wraps_set,
                expected_type=type_hints["wraps_set"],
            )
        jsii.create(
            self.__class__, self, [terraform_resource, terraform_attribute, wraps_set]
        )

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "RealmUserProfileGroupOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__51281a95104ad8d2f8716d2e438e8e808b5be91deb7c99f4f972d735029c0524
            )
            check_type(
                argname="argument index", value=index, expected_type=type_hints["index"]
            )
        return typing.cast(
            "RealmUserProfileGroupOutputReference", jsii.invoke(self, "get", [index])
        )

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        """The attribute on the parent resource this class is referencing."""
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__4a6fa135d4021cd8a4f6bea8977493e58dc39a4b4e4eb35ebd824ac1b68c7012
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        """The parent resource."""
        return typing.cast(
            _cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource")
        )

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__e1695eeda98e814035f379bce9ccd6063b54889e10445300fe2c881518710092
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        """whether the list is wrapping a set (will add tolist() to be able to access an item via an index)."""
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__2d6aaf607d4652ef56dbd400c7fdf090809e408df531a564390d135e9116b4c3
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RealmUserProfileGroup]]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable, typing.List[RealmUserProfileGroup]
                ]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable, typing.List[RealmUserProfileGroup]
            ]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__83baf1c46283aa49ff97de57d852daef9a50f8c543d11fb10b36d70b53201b55
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


class RealmUserProfileGroupOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.realmUserProfile.RealmUserProfileGroupOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        """
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__ddbfdee83e3927a493d747b7a090293fe42f444fef48559463f5b26f9b1237ae
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
            check_type(
                argname="argument complex_object_index",
                value=complex_object_index,
                expected_type=type_hints["complex_object_index"],
            )
            check_type(
                argname="argument complex_object_is_from_set",
                value=complex_object_is_from_set,
                expected_type=type_hints["complex_object_is_from_set"],
            )
        jsii.create(
            self.__class__,
            self,
            [
                terraform_resource,
                terraform_attribute,
                complex_object_index,
                complex_object_is_from_set,
            ],
        )

    @jsii.member(jsii_name="resetAnnotations")
    def reset_annotations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnnotations", []))

    @jsii.member(jsii_name="resetDisplayDescription")
    def reset_display_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayDescription", []))

    @jsii.member(jsii_name="resetDisplayHeader")
    def reset_display_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayHeader", []))

    @builtins.property
    @jsii.member(jsii_name="annotationsInput")
    def annotations_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(
            typing.Optional[typing.Mapping[builtins.str, builtins.str]],
            jsii.get(self, "annotationsInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="displayDescriptionInput")
    def display_description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "displayDescriptionInput")
        )

    @builtins.property
    @jsii.member(jsii_name="displayHeaderInput")
    def display_header_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "displayHeaderInput")
        )

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="annotations")
    def annotations(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(
            typing.Mapping[builtins.str, builtins.str], jsii.get(self, "annotations")
        )

    @annotations.setter
    def annotations(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__c926145a910f98a998512bf743cf160a121ef4336ca24e0fbcab521ced5c0e27
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="displayDescription")
    def display_description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayDescription"))

    @display_description.setter
    def display_description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__6be7efc36f7effd721a7d50da3b929fe99685bbd5e237fb1d9688996da3d1291
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "displayDescription", value)

    @builtins.property
    @jsii.member(jsii_name="displayHeader")
    def display_header(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayHeader"))

    @display_header.setter
    def display_header(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__ee8099d2b921b4614352a8103eea9d2cd1ce5478f177888929cb97a48136e114
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "displayHeader", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__def71e4527ed67d36b69d3640fd10af05b4d9e9168fe1c2d7653d6832fbe8101
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, RealmUserProfileGroup]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[_cdktf_9a9027ec.IResolvable, RealmUserProfileGroup]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, RealmUserProfileGroup]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b48d0cf0c3d28ad8e6f74fa52c5642dc92d88c756643d204adcdc96d365af788
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


__all__ = [
    "RealmUserProfile",
    "RealmUserProfileAttribute",
    "RealmUserProfileAttributeList",
    "RealmUserProfileAttributeOutputReference",
    "RealmUserProfileAttributePermissions",
    "RealmUserProfileAttributePermissionsOutputReference",
    "RealmUserProfileAttributeValidator",
    "RealmUserProfileAttributeValidatorList",
    "RealmUserProfileAttributeValidatorOutputReference",
    "RealmUserProfileConfig",
    "RealmUserProfileGroup",
    "RealmUserProfileGroupList",
    "RealmUserProfileGroupOutputReference",
]

publication.publish()


def _typecheckingstub__4c3250fbf605ea943f02577fb306ffdbadf9898901ed41ca21bb2f55e877c19d(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    realm_id: builtins.str,
    attribute: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    RealmUserProfileAttribute, typing.Dict[builtins.str, typing.Any]
                ]
            ],
        ]
    ] = None,
    group: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    RealmUserProfileGroup, typing.Dict[builtins.str, typing.Any]
                ]
            ],
        ]
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
    """Type checking stubs"""
    pass


def _typecheckingstub__135a2c156ff5407923a086afb78ca9e93b817aa92d4c4acf437dac0d27070700(
    value: typing.Union[
        _cdktf_9a9027ec.IResolvable,
        typing.Sequence[
            typing.Union[
                RealmUserProfileAttribute, typing.Dict[builtins.str, typing.Any]
            ]
        ],
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d63fcc2aacfaa14d3f25c00141e610ccb0abb2e82eac610674773f4611b2ebb7(
    value: typing.Union[
        _cdktf_9a9027ec.IResolvable,
        typing.Sequence[
            typing.Union[RealmUserProfileGroup, typing.Dict[builtins.str, typing.Any]]
        ],
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__41af7b42b93bee02963bc3135e7c09a6886e0d989a56b0d7d6f3d2c994293d99(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__16edd449dd0b4f80d0ff15e356d5a4f3730c2df24a2649b9ba73bccbffbe175c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6d2f2dce1318d6e9759c9c429a21fe25d093437b34a4fbdac7a616d4be60bd28(
    *,
    name: builtins.str,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    display_name: typing.Optional[builtins.str] = None,
    enabled_when_scope: typing.Optional[typing.Sequence[builtins.str]] = None,
    group: typing.Optional[builtins.str] = None,
    permissions: typing.Optional[
        typing.Union[
            RealmUserProfileAttributePermissions, typing.Dict[builtins.str, typing.Any]
        ]
    ] = None,
    required_for_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
    required_for_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    validator: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    RealmUserProfileAttributeValidator,
                    typing.Dict[builtins.str, typing.Any],
                ]
            ],
        ]
    ] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1b8a4c2616bf0f8817814a1b130909027555496af9bc5b109542ba5d4a7c615b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a180cec1a9a148b3d82383dff71ec7353fdad80a375f626caa8b516eb4ad239d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e47c57eb082e5a08306335cba1400da356c62d245cff42be8123b503cf3f6f12(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d1f869ccfcbd5ffdb4cf7d5ade14f6d925e96d0e38f07673c1e6f0e3b7b500ad(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e4dbc1056332dc0e83a731c90256d8e3b96e65d070f73b3062db651b7bef5320(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__82a46129eb8d619bd2466dd9aec8b05a65d5a5b83c14a78287c95714a1898a8d(
    value: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable, typing.List[RealmUserProfileAttribute]
        ]
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__bbebac5ebabc1b73beaacaeae517503309d1120e651ba215bee52e35d8598347(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a086e47d383955ef09839f3cdcef9fb694eeb71860ece3309fdc8f57ed3d2e21(
    value: typing.Union[
        _cdktf_9a9027ec.IResolvable,
        typing.Sequence[
            typing.Union[
                RealmUserProfileAttributeValidator,
                typing.Dict[builtins.str, typing.Any],
            ]
        ],
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__40c9e7408ea317e749502a2d71de675608a277f2929149b79b2599a9e685f3e1(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1eef879d63c0278dd0a6702ded655a26afdeee3709cbfd73bbb144ff7d42fc99(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__14487f05904dba3256ba4797e4d38d2736c35a6b33e0379a7a8b1166d084663c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__063f89ab4ef5f28c6a17115ec7a1416a8ed113bdd7d82770d8614169ba48170b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6713b572ffe258366c0d95dbcec7d4f30019ab32959bff2772688eb3097917fd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__0d5a157843cba5a4589535bb04615ba6064b212ca69b83e58dad5f2b6bb5e9e6(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__5f6144b1cf0d97b68734297cca32b2fe5526aec066fc301d6823489d73af8a86(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8023e5fe73b10720846d1b84479270c0e95e312d0b98abaf96ef75fa1766e874(
    value: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, RealmUserProfileAttribute]
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__40ab20d065858d4fcb07d851c7bbc52f9db63dd4d5dc5e5edf3ce5139ee564c2(
    *,
    edit: typing.Sequence[builtins.str],
    view: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3f9d7efde6aa7b32af1762230357e90c44e60352bb8c05ed24bbefa4ab7f0ca2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__cfdfa56b2aa7952235602e6183a42136b5f0c3be2782f780bffa4945b518f837(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d59b0e0df293e353b02e6d8ff1c8d27dc9b5686c9d39b28a03978790ee61a416(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__986d0338729529e35deb1ee70cb8d9e109a7e79b27f69571d0bd9044c6031d25(
    value: typing.Optional[RealmUserProfileAttributePermissions],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__00d66ff722ec12bf14e561539c9e0fd66931d3d7e89c9e6a2d5712cb73f8925e(
    *,
    name: builtins.str,
    config: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__90b7cb698609e68ed5763e635360ce4b4e7b285e7855cf87a9e15f363e3ddc17(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d704fde626b7dc11a432522d2e234f5a41fca9365d5098589236809a82babf24(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__71e7611c0f2d6d2015cfce897b072d4ab143ed02106abd7545b9fbe2a4899392(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__faae8df8a1cbd302104d38de424ce8cdc445e617a2173df2bd84c9837d5c262c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__304c215f99e1b118a2366b6d48c22f803266c29a9d30d6fa64e96476035a5462(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__abc632bff62b35a99b7a54eccf531696308a8f6f5f85df84f63ca7ffa903be2e(
    value: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable, typing.List[RealmUserProfileAttributeValidator]
        ]
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__abdabec990f2a53c650928f1fc03fd7a0daeb0129255e1e5341f1fb6ec98cdc2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7bbcf9cc575395116b99e7d330b89f8408ac39305585ac0515b4cf8058d61c94(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__5a869908a266a7592a8ad3fa7db003e254cafd7591089a10f4e72a640688db16(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9e06be623fe1abd51e80ac8ad1bd5dd34de9e7f417a5cfcda19945a82193d48e(
    value: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, RealmUserProfileAttributeValidator]
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7616a1bb6a301f6c75a92f6e8b4b7975195d0f419da5ea7f8decf4370d513187(
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
    attribute: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    RealmUserProfileAttribute, typing.Dict[builtins.str, typing.Any]
                ]
            ],
        ]
    ] = None,
    group: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    RealmUserProfileGroup, typing.Dict[builtins.str, typing.Any]
                ]
            ],
        ]
    ] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__5356202500e0105df66901115dd89d48a91ff964a59765e2a436307a298a694a(
    *,
    name: builtins.str,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    display_description: typing.Optional[builtins.str] = None,
    display_header: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a69d04b57e426d60d1184208b3137fa2dd7e40afb8b6e4bfcbe0e72b4759c9bc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__51281a95104ad8d2f8716d2e438e8e808b5be91deb7c99f4f972d735029c0524(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4a6fa135d4021cd8a4f6bea8977493e58dc39a4b4e4eb35ebd824ac1b68c7012(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e1695eeda98e814035f379bce9ccd6063b54889e10445300fe2c881518710092(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__2d6aaf607d4652ef56dbd400c7fdf090809e408df531a564390d135e9116b4c3(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__83baf1c46283aa49ff97de57d852daef9a50f8c543d11fb10b36d70b53201b55(
    value: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RealmUserProfileGroup]]
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ddbfdee83e3927a493d747b7a090293fe42f444fef48559463f5b26f9b1237ae(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c926145a910f98a998512bf743cf160a121ef4336ca24e0fbcab521ced5c0e27(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6be7efc36f7effd721a7d50da3b929fe99685bbd5e237fb1d9688996da3d1291(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ee8099d2b921b4614352a8103eea9d2cd1ce5478f177888929cb97a48136e114(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__def71e4527ed67d36b69d3640fd10af05b4d9e9168fe1c2d7653d6832fbe8101(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b48d0cf0c3d28ad8e6f74fa52c5642dc92d88c756643d204adcdc96d365af788(
    value: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, RealmUserProfileGroup]
    ],
) -> None:
    """Type checking stubs"""
    pass
