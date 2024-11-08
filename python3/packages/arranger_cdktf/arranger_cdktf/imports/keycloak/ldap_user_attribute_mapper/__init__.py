"""
# `keycloak_ldap_user_attribute_mapper`

Refer to the Terraform Registory for docs: [`keycloak_ldap_user_attribute_mapper`](https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_attribute_mapper).
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


class LdapUserAttributeMapper(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.ldapUserAttributeMapper.LdapUserAttributeMapper",
):
    """Represents a {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_attribute_mapper keycloak_ldap_user_attribute_mapper}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        ldap_attribute: builtins.str,
        ldap_user_federation_id: builtins.str,
        name: builtins.str,
        realm_id: builtins.str,
        user_model_attribute: builtins.str,
        always_read_value_from_ldap: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        attribute_default_value: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        is_binary_attribute: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        is_mandatory_in_ldap: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        read_only: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
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
        """Create a new {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_attribute_mapper keycloak_ldap_user_attribute_mapper} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param ldap_attribute: Name of the mapped attribute on LDAP object. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_attribute_mapper#ldap_attribute LdapUserAttributeMapper#ldap_attribute}
        :param ldap_user_federation_id: The ldap user federation provider to attach this mapper to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_attribute_mapper#ldap_user_federation_id LdapUserAttributeMapper#ldap_user_federation_id}
        :param name: Display name of the mapper when displayed in the console. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_attribute_mapper#name LdapUserAttributeMapper#name}
        :param realm_id: The realm in which the ldap user federation provider exists. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_attribute_mapper#realm_id LdapUserAttributeMapper#realm_id}
        :param user_model_attribute: Name of the UserModel property or attribute you want to map the LDAP attribute into. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_attribute_mapper#user_model_attribute LdapUserAttributeMapper#user_model_attribute}
        :param always_read_value_from_ldap: When true, the value fetched from LDAP will override the value stored in Keycloak. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_attribute_mapper#always_read_value_from_ldap LdapUserAttributeMapper#always_read_value_from_ldap}
        :param attribute_default_value: Default value to set in LDAP if is_mandatory_in_ldap and the value is empty. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_attribute_mapper#attribute_default_value LdapUserAttributeMapper#attribute_default_value}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_attribute_mapper#id LdapUserAttributeMapper#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param is_binary_attribute: Should be true for binary LDAP attributes. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_attribute_mapper#is_binary_attribute LdapUserAttributeMapper#is_binary_attribute}
        :param is_mandatory_in_ldap: When true, this attribute must exist in LDAP. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_attribute_mapper#is_mandatory_in_ldap LdapUserAttributeMapper#is_mandatory_in_ldap}
        :param read_only: When true, this attribute is not saved back to LDAP when the user attribute is updated in Keycloak. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_attribute_mapper#read_only LdapUserAttributeMapper#read_only}
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
                _typecheckingstub__3546ea878a42e9d28137eefcfb902be5a9ee484ecb1c7f0cec4d0549cd68affd
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(
                argname="argument id_", value=id_, expected_type=type_hints["id_"]
            )
        config = LdapUserAttributeMapperConfig(
            ldap_attribute=ldap_attribute,
            ldap_user_federation_id=ldap_user_federation_id,
            name=name,
            realm_id=realm_id,
            user_model_attribute=user_model_attribute,
            always_read_value_from_ldap=always_read_value_from_ldap,
            attribute_default_value=attribute_default_value,
            id=id,
            is_binary_attribute=is_binary_attribute,
            is_mandatory_in_ldap=is_mandatory_in_ldap,
            read_only=read_only,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetAlwaysReadValueFromLdap")
    def reset_always_read_value_from_ldap(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlwaysReadValueFromLdap", []))

    @jsii.member(jsii_name="resetAttributeDefaultValue")
    def reset_attribute_default_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttributeDefaultValue", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIsBinaryAttribute")
    def reset_is_binary_attribute(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsBinaryAttribute", []))

    @jsii.member(jsii_name="resetIsMandatoryInLdap")
    def reset_is_mandatory_in_ldap(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsMandatoryInLdap", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

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
    @jsii.member(jsii_name="alwaysReadValueFromLdapInput")
    def always_read_value_from_ldap_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "alwaysReadValueFromLdapInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="attributeDefaultValueInput")
    def attribute_default_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "attributeDefaultValueInput")
        )

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="isBinaryAttributeInput")
    def is_binary_attribute_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "isBinaryAttributeInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="isMandatoryInLdapInput")
    def is_mandatory_in_ldap_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "isMandatoryInLdapInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="ldapAttributeInput")
    def ldap_attribute_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "ldapAttributeInput")
        )

    @builtins.property
    @jsii.member(jsii_name="ldapUserFederationIdInput")
    def ldap_user_federation_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "ldapUserFederationIdInput")
        )

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "readOnlyInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="realmIdInput")
    def realm_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "realmIdInput")
        )

    @builtins.property
    @jsii.member(jsii_name="userModelAttributeInput")
    def user_model_attribute_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "userModelAttributeInput")
        )

    @builtins.property
    @jsii.member(jsii_name="alwaysReadValueFromLdap")
    def always_read_value_from_ldap(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "alwaysReadValueFromLdap"),
        )

    @always_read_value_from_ldap.setter
    def always_read_value_from_ldap(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__0beae0a929a0ce550843a0b6bbe19eecd3b9ab9b00f2a33e9377ddf14372b730
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "alwaysReadValueFromLdap", value)

    @builtins.property
    @jsii.member(jsii_name="attributeDefaultValue")
    def attribute_default_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attributeDefaultValue"))

    @attribute_default_value.setter
    def attribute_default_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__5f62f39168d2228ed0a7441d3c7e3957f55fbb8655a01c5d9efa0a2ed729e8bf
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "attributeDefaultValue", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__33fb948ba4ed0ae9fa58f2ec13416982209b30fea0a5f6b6871affedb56446e8
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="isBinaryAttribute")
    def is_binary_attribute(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "isBinaryAttribute"),
        )

    @is_binary_attribute.setter
    def is_binary_attribute(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__5a5b6aa33224460070ca5d4623c7d9f313e00f5a899dff9c08cb69173d33939f
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "isBinaryAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="isMandatoryInLdap")
    def is_mandatory_in_ldap(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "isMandatoryInLdap"),
        )

    @is_mandatory_in_ldap.setter
    def is_mandatory_in_ldap(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__8e8a854c51aa4d7972f6c333888efcc30f937ad5fa4dd450722e85eeda2baeec
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "isMandatoryInLdap", value)

    @builtins.property
    @jsii.member(jsii_name="ldapAttribute")
    def ldap_attribute(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ldapAttribute"))

    @ldap_attribute.setter
    def ldap_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__403fc6a824319aa8970b88ebffec16d0a441571bfc574ffa5bab39f186823926
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "ldapAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="ldapUserFederationId")
    def ldap_user_federation_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ldapUserFederationId"))

    @ldap_user_federation_id.setter
    def ldap_user_federation_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d0591a701585f37bacab498ccdc10931e6596bbb72ec3e8f661809cb0299c27d
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "ldapUserFederationId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__d94bc27dc94da8ae6ff4937edd52a88eb687f3d7635ae900714064a9ceb634e2
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "readOnly"),
        )

    @read_only.setter
    def read_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__17aba09ce1a64fdb12d0839ab73570feaba777224b0ef576fb21a01f21d6056e
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="realmId")
    def realm_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "realmId"))

    @realm_id.setter
    def realm_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__88aee33629e382a85aa40daf695f7ea38649e2673d26249fb5b6c6df316dbc88
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "realmId", value)

    @builtins.property
    @jsii.member(jsii_name="userModelAttribute")
    def user_model_attribute(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userModelAttribute"))

    @user_model_attribute.setter
    def user_model_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__387304eb68df18f98635f7e5c25b217db69499978322453f245bbd5c44df80f1
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "userModelAttribute", value)


@jsii.data_type(
    jsii_type="keycloak.ldapUserAttributeMapper.LdapUserAttributeMapperConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "ldap_attribute": "ldapAttribute",
        "ldap_user_federation_id": "ldapUserFederationId",
        "name": "name",
        "realm_id": "realmId",
        "user_model_attribute": "userModelAttribute",
        "always_read_value_from_ldap": "alwaysReadValueFromLdap",
        "attribute_default_value": "attributeDefaultValue",
        "id": "id",
        "is_binary_attribute": "isBinaryAttribute",
        "is_mandatory_in_ldap": "isMandatoryInLdap",
        "read_only": "readOnly",
    },
)
class LdapUserAttributeMapperConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        ldap_attribute: builtins.str,
        ldap_user_federation_id: builtins.str,
        name: builtins.str,
        realm_id: builtins.str,
        user_model_attribute: builtins.str,
        always_read_value_from_ldap: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        attribute_default_value: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        is_binary_attribute: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        is_mandatory_in_ldap: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        read_only: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
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
        :param ldap_attribute: Name of the mapped attribute on LDAP object. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_attribute_mapper#ldap_attribute LdapUserAttributeMapper#ldap_attribute}
        :param ldap_user_federation_id: The ldap user federation provider to attach this mapper to. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_attribute_mapper#ldap_user_federation_id LdapUserAttributeMapper#ldap_user_federation_id}
        :param name: Display name of the mapper when displayed in the console. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_attribute_mapper#name LdapUserAttributeMapper#name}
        :param realm_id: The realm in which the ldap user federation provider exists. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_attribute_mapper#realm_id LdapUserAttributeMapper#realm_id}
        :param user_model_attribute: Name of the UserModel property or attribute you want to map the LDAP attribute into. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_attribute_mapper#user_model_attribute LdapUserAttributeMapper#user_model_attribute}
        :param always_read_value_from_ldap: When true, the value fetched from LDAP will override the value stored in Keycloak. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_attribute_mapper#always_read_value_from_ldap LdapUserAttributeMapper#always_read_value_from_ldap}
        :param attribute_default_value: Default value to set in LDAP if is_mandatory_in_ldap and the value is empty. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_attribute_mapper#attribute_default_value LdapUserAttributeMapper#attribute_default_value}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_attribute_mapper#id LdapUserAttributeMapper#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param is_binary_attribute: Should be true for binary LDAP attributes. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_attribute_mapper#is_binary_attribute LdapUserAttributeMapper#is_binary_attribute}
        :param is_mandatory_in_ldap: When true, this attribute must exist in LDAP. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_attribute_mapper#is_mandatory_in_ldap LdapUserAttributeMapper#is_mandatory_in_ldap}
        :param read_only: When true, this attribute is not saved back to LDAP when the user attribute is updated in Keycloak. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_attribute_mapper#read_only LdapUserAttributeMapper#read_only}
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__266153d98aca76a3d4942851aec8dd67d22e423b6f1ab517471a4d887fe2592f
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
                argname="argument ldap_attribute",
                value=ldap_attribute,
                expected_type=type_hints["ldap_attribute"],
            )
            check_type(
                argname="argument ldap_user_federation_id",
                value=ldap_user_federation_id,
                expected_type=type_hints["ldap_user_federation_id"],
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
                argname="argument user_model_attribute",
                value=user_model_attribute,
                expected_type=type_hints["user_model_attribute"],
            )
            check_type(
                argname="argument always_read_value_from_ldap",
                value=always_read_value_from_ldap,
                expected_type=type_hints["always_read_value_from_ldap"],
            )
            check_type(
                argname="argument attribute_default_value",
                value=attribute_default_value,
                expected_type=type_hints["attribute_default_value"],
            )
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(
                argname="argument is_binary_attribute",
                value=is_binary_attribute,
                expected_type=type_hints["is_binary_attribute"],
            )
            check_type(
                argname="argument is_mandatory_in_ldap",
                value=is_mandatory_in_ldap,
                expected_type=type_hints["is_mandatory_in_ldap"],
            )
            check_type(
                argname="argument read_only",
                value=read_only,
                expected_type=type_hints["read_only"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ldap_attribute": ldap_attribute,
            "ldap_user_federation_id": ldap_user_federation_id,
            "name": name,
            "realm_id": realm_id,
            "user_model_attribute": user_model_attribute,
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
        if always_read_value_from_ldap is not None:
            self._values["always_read_value_from_ldap"] = always_read_value_from_ldap
        if attribute_default_value is not None:
            self._values["attribute_default_value"] = attribute_default_value
        if id is not None:
            self._values["id"] = id
        if is_binary_attribute is not None:
            self._values["is_binary_attribute"] = is_binary_attribute
        if is_mandatory_in_ldap is not None:
            self._values["is_mandatory_in_ldap"] = is_mandatory_in_ldap
        if read_only is not None:
            self._values["read_only"] = read_only

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
    def ldap_attribute(self) -> builtins.str:
        """Name of the mapped attribute on LDAP object.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_attribute_mapper#ldap_attribute LdapUserAttributeMapper#ldap_attribute}
        """
        result = self._values.get("ldap_attribute")
        assert result is not None, "Required property 'ldap_attribute' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ldap_user_federation_id(self) -> builtins.str:
        """The ldap user federation provider to attach this mapper to.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_attribute_mapper#ldap_user_federation_id LdapUserAttributeMapper#ldap_user_federation_id}
        """
        result = self._values.get("ldap_user_federation_id")
        assert (
            result is not None
        ), "Required property 'ldap_user_federation_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        """Display name of the mapper when displayed in the console.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_attribute_mapper#name LdapUserAttributeMapper#name}
        """
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def realm_id(self) -> builtins.str:
        """The realm in which the ldap user federation provider exists.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_attribute_mapper#realm_id LdapUserAttributeMapper#realm_id}
        """
        result = self._values.get("realm_id")
        assert result is not None, "Required property 'realm_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_model_attribute(self) -> builtins.str:
        """Name of the UserModel property or attribute you want to map the LDAP attribute into.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_attribute_mapper#user_model_attribute LdapUserAttributeMapper#user_model_attribute}
        """
        result = self._values.get("user_model_attribute")
        assert result is not None, "Required property 'user_model_attribute' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def always_read_value_from_ldap(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """When true, the value fetched from LDAP will override the value stored in Keycloak.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_attribute_mapper#always_read_value_from_ldap LdapUserAttributeMapper#always_read_value_from_ldap}
        """
        result = self._values.get("always_read_value_from_ldap")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def attribute_default_value(self) -> typing.Optional[builtins.str]:
        """Default value to set in LDAP if is_mandatory_in_ldap and the value is empty.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_attribute_mapper#attribute_default_value LdapUserAttributeMapper#attribute_default_value}
        """
        result = self._values.get("attribute_default_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_attribute_mapper#id LdapUserAttributeMapper#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_binary_attribute(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Should be true for binary LDAP attributes.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_attribute_mapper#is_binary_attribute LdapUserAttributeMapper#is_binary_attribute}
        """
        result = self._values.get("is_binary_attribute")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def is_mandatory_in_ldap(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """When true, this attribute must exist in LDAP.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_attribute_mapper#is_mandatory_in_ldap LdapUserAttributeMapper#is_mandatory_in_ldap}
        """
        result = self._values.get("is_mandatory_in_ldap")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """When true, this attribute is not saved back to LDAP when the user attribute is updated in Keycloak.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/ldap_user_attribute_mapper#read_only LdapUserAttributeMapper#read_only}
        """
        result = self._values.get("read_only")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LdapUserAttributeMapperConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "LdapUserAttributeMapper",
    "LdapUserAttributeMapperConfig",
]

publication.publish()


def _typecheckingstub__3546ea878a42e9d28137eefcfb902be5a9ee484ecb1c7f0cec4d0549cd68affd(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    ldap_attribute: builtins.str,
    ldap_user_federation_id: builtins.str,
    name: builtins.str,
    realm_id: builtins.str,
    user_model_attribute: builtins.str,
    always_read_value_from_ldap: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    attribute_default_value: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    is_binary_attribute: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    is_mandatory_in_ldap: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    read_only: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
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


def _typecheckingstub__0beae0a929a0ce550843a0b6bbe19eecd3b9ab9b00f2a33e9377ddf14372b730(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__5f62f39168d2228ed0a7441d3c7e3957f55fbb8655a01c5d9efa0a2ed729e8bf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__33fb948ba4ed0ae9fa58f2ec13416982209b30fea0a5f6b6871affedb56446e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__5a5b6aa33224460070ca5d4623c7d9f313e00f5a899dff9c08cb69173d33939f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8e8a854c51aa4d7972f6c333888efcc30f937ad5fa4dd450722e85eeda2baeec(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__403fc6a824319aa8970b88ebffec16d0a441571bfc574ffa5bab39f186823926(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d0591a701585f37bacab498ccdc10931e6596bbb72ec3e8f661809cb0299c27d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__d94bc27dc94da8ae6ff4937edd52a88eb687f3d7635ae900714064a9ceb634e2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__17aba09ce1a64fdb12d0839ab73570feaba777224b0ef576fb21a01f21d6056e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__88aee33629e382a85aa40daf695f7ea38649e2673d26249fb5b6c6df316dbc88(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__387304eb68df18f98635f7e5c25b217db69499978322453f245bbd5c44df80f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__266153d98aca76a3d4942851aec8dd67d22e423b6f1ab517471a4d887fe2592f(
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
    ldap_attribute: builtins.str,
    ldap_user_federation_id: builtins.str,
    name: builtins.str,
    realm_id: builtins.str,
    user_model_attribute: builtins.str,
    always_read_value_from_ldap: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    attribute_default_value: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    is_binary_attribute: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    is_mandatory_in_ldap: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    read_only: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
) -> None:
    """Type checking stubs"""
    pass
