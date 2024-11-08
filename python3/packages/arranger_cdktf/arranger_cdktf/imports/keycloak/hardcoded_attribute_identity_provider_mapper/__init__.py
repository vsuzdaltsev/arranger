"""
# `keycloak_hardcoded_attribute_identity_provider_mapper`

Refer to the Terraform Registory for docs: [`keycloak_hardcoded_attribute_identity_provider_mapper`](https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/hardcoded_attribute_identity_provider_mapper).
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


class HardcodedAttributeIdentityProviderMapper(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.hardcodedAttributeIdentityProviderMapper.HardcodedAttributeIdentityProviderMapper",
):
    """Represents a {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/hardcoded_attribute_identity_provider_mapper keycloak_hardcoded_attribute_identity_provider_mapper}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        identity_provider_alias: builtins.str,
        name: builtins.str,
        realm: builtins.str,
        user_session: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        attribute_name: typing.Optional[builtins.str] = None,
        attribute_value: typing.Optional[builtins.str] = None,
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
        """Create a new {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/hardcoded_attribute_identity_provider_mapper keycloak_hardcoded_attribute_identity_provider_mapper} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param identity_provider_alias: IDP Alias. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/hardcoded_attribute_identity_provider_mapper#identity_provider_alias HardcodedAttributeIdentityProviderMapper#identity_provider_alias}
        :param name: IDP Mapper Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/hardcoded_attribute_identity_provider_mapper#name HardcodedAttributeIdentityProviderMapper#name}
        :param realm: Realm Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/hardcoded_attribute_identity_provider_mapper#realm HardcodedAttributeIdentityProviderMapper#realm}
        :param user_session: Is Attribute Related To a User Session. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/hardcoded_attribute_identity_provider_mapper#user_session HardcodedAttributeIdentityProviderMapper#user_session}
        :param attribute_name: OIDC Claim. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/hardcoded_attribute_identity_provider_mapper#attribute_name HardcodedAttributeIdentityProviderMapper#attribute_name}
        :param attribute_value: User Attribute. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/hardcoded_attribute_identity_provider_mapper#attribute_value HardcodedAttributeIdentityProviderMapper#attribute_value}
        :param extra_config: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/hardcoded_attribute_identity_provider_mapper#extra_config HardcodedAttributeIdentityProviderMapper#extra_config}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/hardcoded_attribute_identity_provider_mapper#id HardcodedAttributeIdentityProviderMapper#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
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
                _typecheckingstub__d67b2f42e53653e0193b9272feb09f2bcc10e27ac33f2cf4f8bfd63a942788ab
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(
                argname="argument id_", value=id_, expected_type=type_hints["id_"]
            )
        config = HardcodedAttributeIdentityProviderMapperConfig(
            identity_provider_alias=identity_provider_alias,
            name=name,
            realm=realm,
            user_session=user_session,
            attribute_name=attribute_name,
            attribute_value=attribute_value,
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

    @jsii.member(jsii_name="resetAttributeName")
    def reset_attribute_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttributeName", []))

    @jsii.member(jsii_name="resetAttributeValue")
    def reset_attribute_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttributeValue", []))

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
    @jsii.member(jsii_name="userSessionInput")
    def user_session_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "userSessionInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="attributeName")
    def attribute_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attributeName"))

    @attribute_name.setter
    def attribute_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__3783b128e7d5015506002e698b85a9cfddb4411822c522710e0f9f09a400361a
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
                _typecheckingstub__e394be2df8c4edfe71424c57f992b30a9fa6b4d3b84996b12e0b83612135fe7c
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "attributeValue", value)

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
                _typecheckingstub__9fd934f739956d1a223ee16d1dd609dd95f6907c8d6bb1c1d5a8142f8b21efcd
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
                _typecheckingstub__c723c2f47c86ace96ed03ae1feac2bc33f93fd451c7be9a7fd6c2f50866ce407
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
                _typecheckingstub__aa0dc82b05fe7410e00643794b7d1bc8d37e479429a17903eb317ffd59504739
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
                _typecheckingstub__2c68b67ed8973b1aa19f83453af91d0435284fb281a5e0f8a58c05480d8a1c2a
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
                _typecheckingstub__e24da05313851194b8974a8df7afb83f4f3dc32f510abee16d7831f9f3b17d8c
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "realm", value)

    @builtins.property
    @jsii.member(jsii_name="userSession")
    def user_session(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "userSession"),
        )

    @user_session.setter
    def user_session(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__708024fcabbf18905d6d741a14adde9db7d96ccb04ef1ee94ea46269e6250f09
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "userSession", value)


@jsii.data_type(
    jsii_type="keycloak.hardcodedAttributeIdentityProviderMapper.HardcodedAttributeIdentityProviderMapperConfig",
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
        "user_session": "userSession",
        "attribute_name": "attributeName",
        "attribute_value": "attributeValue",
        "extra_config": "extraConfig",
        "id": "id",
    },
)
class HardcodedAttributeIdentityProviderMapperConfig(
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
        user_session: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        attribute_name: typing.Optional[builtins.str] = None,
        attribute_value: typing.Optional[builtins.str] = None,
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
        :param identity_provider_alias: IDP Alias. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/hardcoded_attribute_identity_provider_mapper#identity_provider_alias HardcodedAttributeIdentityProviderMapper#identity_provider_alias}
        :param name: IDP Mapper Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/hardcoded_attribute_identity_provider_mapper#name HardcodedAttributeIdentityProviderMapper#name}
        :param realm: Realm Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/hardcoded_attribute_identity_provider_mapper#realm HardcodedAttributeIdentityProviderMapper#realm}
        :param user_session: Is Attribute Related To a User Session. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/hardcoded_attribute_identity_provider_mapper#user_session HardcodedAttributeIdentityProviderMapper#user_session}
        :param attribute_name: OIDC Claim. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/hardcoded_attribute_identity_provider_mapper#attribute_name HardcodedAttributeIdentityProviderMapper#attribute_name}
        :param attribute_value: User Attribute. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/hardcoded_attribute_identity_provider_mapper#attribute_value HardcodedAttributeIdentityProviderMapper#attribute_value}
        :param extra_config: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/hardcoded_attribute_identity_provider_mapper#extra_config HardcodedAttributeIdentityProviderMapper#extra_config}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/hardcoded_attribute_identity_provider_mapper#id HardcodedAttributeIdentityProviderMapper#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__4a5375c8272f21e49bbaf19df88807c4da6e60faf1424ea61960e21691142ca9
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
                argname="argument user_session",
                value=user_session,
                expected_type=type_hints["user_session"],
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
                argname="argument extra_config",
                value=extra_config,
                expected_type=type_hints["extra_config"],
            )
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "identity_provider_alias": identity_provider_alias,
            "name": name,
            "realm": realm,
            "user_session": user_session,
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
        if attribute_name is not None:
            self._values["attribute_name"] = attribute_name
        if attribute_value is not None:
            self._values["attribute_value"] = attribute_value
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/hardcoded_attribute_identity_provider_mapper#identity_provider_alias HardcodedAttributeIdentityProviderMapper#identity_provider_alias}
        """
        result = self._values.get("identity_provider_alias")
        assert (
            result is not None
        ), "Required property 'identity_provider_alias' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        """IDP Mapper Name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/hardcoded_attribute_identity_provider_mapper#name HardcodedAttributeIdentityProviderMapper#name}
        """
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def realm(self) -> builtins.str:
        """Realm Name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/hardcoded_attribute_identity_provider_mapper#realm HardcodedAttributeIdentityProviderMapper#realm}
        """
        result = self._values.get("realm")
        assert result is not None, "Required property 'realm' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_session(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        """Is Attribute Related To a User Session.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/hardcoded_attribute_identity_provider_mapper#user_session HardcodedAttributeIdentityProviderMapper#user_session}
        """
        result = self._values.get("user_session")
        assert result is not None, "Required property 'user_session' is missing"
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result
        )

    @builtins.property
    def attribute_name(self) -> typing.Optional[builtins.str]:
        """OIDC Claim.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/hardcoded_attribute_identity_provider_mapper#attribute_name HardcodedAttributeIdentityProviderMapper#attribute_name}
        """
        result = self._values.get("attribute_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def attribute_value(self) -> typing.Optional[builtins.str]:
        """User Attribute.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/hardcoded_attribute_identity_provider_mapper#attribute_value HardcodedAttributeIdentityProviderMapper#attribute_value}
        """
        result = self._values.get("attribute_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extra_config(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/hardcoded_attribute_identity_provider_mapper#extra_config HardcodedAttributeIdentityProviderMapper#extra_config}."""
        result = self._values.get("extra_config")
        return typing.cast(
            typing.Optional[typing.Mapping[builtins.str, builtins.str]], result
        )

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/hardcoded_attribute_identity_provider_mapper#id HardcodedAttributeIdentityProviderMapper#id}.

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
        return "HardcodedAttributeIdentityProviderMapperConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "HardcodedAttributeIdentityProviderMapper",
    "HardcodedAttributeIdentityProviderMapperConfig",
]

publication.publish()


def _typecheckingstub__d67b2f42e53653e0193b9272feb09f2bcc10e27ac33f2cf4f8bfd63a942788ab(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    identity_provider_alias: builtins.str,
    name: builtins.str,
    realm: builtins.str,
    user_session: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    attribute_name: typing.Optional[builtins.str] = None,
    attribute_value: typing.Optional[builtins.str] = None,
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


def _typecheckingstub__3783b128e7d5015506002e698b85a9cfddb4411822c522710e0f9f09a400361a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e394be2df8c4edfe71424c57f992b30a9fa6b4d3b84996b12e0b83612135fe7c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9fd934f739956d1a223ee16d1dd609dd95f6907c8d6bb1c1d5a8142f8b21efcd(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c723c2f47c86ace96ed03ae1feac2bc33f93fd451c7be9a7fd6c2f50866ce407(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__aa0dc82b05fe7410e00643794b7d1bc8d37e479429a17903eb317ffd59504739(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__2c68b67ed8973b1aa19f83453af91d0435284fb281a5e0f8a58c05480d8a1c2a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e24da05313851194b8974a8df7afb83f4f3dc32f510abee16d7831f9f3b17d8c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__708024fcabbf18905d6d741a14adde9db7d96ccb04ef1ee94ea46269e6250f09(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__4a5375c8272f21e49bbaf19df88807c4da6e60faf1424ea61960e21691142ca9(
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
    user_session: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    attribute_name: typing.Optional[builtins.str] = None,
    attribute_value: typing.Optional[builtins.str] = None,
    extra_config: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
