"""
# `keycloak_attribute_importer_identity_provider_mapper`

Refer to the Terraform Registory for docs: [`keycloak_attribute_importer_identity_provider_mapper`](https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_importer_identity_provider_mapper).
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


class AttributeImporterIdentityProviderMapper(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.attributeImporterIdentityProviderMapper.AttributeImporterIdentityProviderMapper",
):
    """Represents a {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_importer_identity_provider_mapper keycloak_attribute_importer_identity_provider_mapper}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        identity_provider_alias: builtins.str,
        name: builtins.str,
        realm: builtins.str,
        user_attribute: builtins.str,
        attribute_friendly_name: typing.Optional[builtins.str] = None,
        attribute_name: typing.Optional[builtins.str] = None,
        claim_name: typing.Optional[builtins.str] = None,
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
        """Create a new {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_importer_identity_provider_mapper keycloak_attribute_importer_identity_provider_mapper} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param identity_provider_alias: IDP Alias. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_importer_identity_provider_mapper#identity_provider_alias AttributeImporterIdentityProviderMapper#identity_provider_alias}
        :param name: IDP Mapper Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_importer_identity_provider_mapper#name AttributeImporterIdentityProviderMapper#name}
        :param realm: Realm Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_importer_identity_provider_mapper#realm AttributeImporterIdentityProviderMapper#realm}
        :param user_attribute: User Attribute. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_importer_identity_provider_mapper#user_attribute AttributeImporterIdentityProviderMapper#user_attribute}
        :param attribute_friendly_name: Attribute Friendly Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_importer_identity_provider_mapper#attribute_friendly_name AttributeImporterIdentityProviderMapper#attribute_friendly_name}
        :param attribute_name: Attribute Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_importer_identity_provider_mapper#attribute_name AttributeImporterIdentityProviderMapper#attribute_name}
        :param claim_name: Claim Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_importer_identity_provider_mapper#claim_name AttributeImporterIdentityProviderMapper#claim_name}
        :param extra_config: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_importer_identity_provider_mapper#extra_config AttributeImporterIdentityProviderMapper#extra_config}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_importer_identity_provider_mapper#id AttributeImporterIdentityProviderMapper#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
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
                _typecheckingstub__050be39f01d4d0c64a8df3b22eeb90985a37cfa91b9ab46ff79d53fe2520481a
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(
                argname="argument id_", value=id_, expected_type=type_hints["id_"]
            )
        config = AttributeImporterIdentityProviderMapperConfig(
            identity_provider_alias=identity_provider_alias,
            name=name,
            realm=realm,
            user_attribute=user_attribute,
            attribute_friendly_name=attribute_friendly_name,
            attribute_name=attribute_name,
            claim_name=claim_name,
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

    @jsii.member(jsii_name="resetClaimName")
    def reset_claim_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClaimName", []))

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
    @jsii.member(jsii_name="claimNameInput")
    def claim_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "claimNameInput")
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
    @jsii.member(jsii_name="userAttributeInput")
    def user_attribute_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "userAttributeInput")
        )

    @builtins.property
    @jsii.member(jsii_name="attributeFriendlyName")
    def attribute_friendly_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attributeFriendlyName"))

    @attribute_friendly_name.setter
    def attribute_friendly_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__f7ac58735ffb65f14cf4417999866c6dd177d5948836a77c70d3b8d05529928e
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
                _typecheckingstub__fb0acc7c04ab059b7dd97f7a2e6d660416969442aab7f09d63bdb0a522cb3798
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "attributeName", value)

    @builtins.property
    @jsii.member(jsii_name="claimName")
    def claim_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "claimName"))

    @claim_name.setter
    def claim_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__01348939be9b875708097cc1810a51d404a0fb506b78b2cfe8a8a7bacb9bf5a9
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "claimName", value)

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
                _typecheckingstub__abad1c5ef8741e857b90b6298da9f27a3495f3df7e162700d33b2fb08e5c13c5
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
                _typecheckingstub__ec23024d7cff99eaa8f71e27a20393a23621dc039335a59ca2c5afd31f996b8d
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
                _typecheckingstub__41061dfff791de5773c105a0d21ad1840b645b0e44d2e1dbe9bb38709969e66d
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
                _typecheckingstub__68d6d84c4ab62ace81afcfedf7d3ff1e8bb1992a32c884203d125718c131ca2d
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
                _typecheckingstub__7200721205c2e475191e781b7cdd970b2aead3d36ea6ad46fae679ce0c2d9938
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "realm", value)

    @builtins.property
    @jsii.member(jsii_name="userAttribute")
    def user_attribute(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userAttribute"))

    @user_attribute.setter
    def user_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__c4a80ad7e39d5288d92f0c4a0d92b0268eb1e1537970707082881ebd5594f788
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "userAttribute", value)


@jsii.data_type(
    jsii_type="keycloak.attributeImporterIdentityProviderMapper.AttributeImporterIdentityProviderMapperConfig",
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
        "user_attribute": "userAttribute",
        "attribute_friendly_name": "attributeFriendlyName",
        "attribute_name": "attributeName",
        "claim_name": "claimName",
        "extra_config": "extraConfig",
        "id": "id",
    },
)
class AttributeImporterIdentityProviderMapperConfig(
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
        user_attribute: builtins.str,
        attribute_friendly_name: typing.Optional[builtins.str] = None,
        attribute_name: typing.Optional[builtins.str] = None,
        claim_name: typing.Optional[builtins.str] = None,
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
        :param identity_provider_alias: IDP Alias. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_importer_identity_provider_mapper#identity_provider_alias AttributeImporterIdentityProviderMapper#identity_provider_alias}
        :param name: IDP Mapper Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_importer_identity_provider_mapper#name AttributeImporterIdentityProviderMapper#name}
        :param realm: Realm Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_importer_identity_provider_mapper#realm AttributeImporterIdentityProviderMapper#realm}
        :param user_attribute: User Attribute. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_importer_identity_provider_mapper#user_attribute AttributeImporterIdentityProviderMapper#user_attribute}
        :param attribute_friendly_name: Attribute Friendly Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_importer_identity_provider_mapper#attribute_friendly_name AttributeImporterIdentityProviderMapper#attribute_friendly_name}
        :param attribute_name: Attribute Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_importer_identity_provider_mapper#attribute_name AttributeImporterIdentityProviderMapper#attribute_name}
        :param claim_name: Claim Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_importer_identity_provider_mapper#claim_name AttributeImporterIdentityProviderMapper#claim_name}
        :param extra_config: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_importer_identity_provider_mapper#extra_config AttributeImporterIdentityProviderMapper#extra_config}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_importer_identity_provider_mapper#id AttributeImporterIdentityProviderMapper#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__a2c7dfa1326815d2645cbd56d5786e796222fa5447187902daaa36cfa11dd0cc
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
                argname="argument user_attribute",
                value=user_attribute,
                expected_type=type_hints["user_attribute"],
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
                argname="argument claim_name",
                value=claim_name,
                expected_type=type_hints["claim_name"],
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
            "user_attribute": user_attribute,
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
        if claim_name is not None:
            self._values["claim_name"] = claim_name
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_importer_identity_provider_mapper#identity_provider_alias AttributeImporterIdentityProviderMapper#identity_provider_alias}
        """
        result = self._values.get("identity_provider_alias")
        assert (
            result is not None
        ), "Required property 'identity_provider_alias' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        """IDP Mapper Name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_importer_identity_provider_mapper#name AttributeImporterIdentityProviderMapper#name}
        """
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def realm(self) -> builtins.str:
        """Realm Name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_importer_identity_provider_mapper#realm AttributeImporterIdentityProviderMapper#realm}
        """
        result = self._values.get("realm")
        assert result is not None, "Required property 'realm' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_attribute(self) -> builtins.str:
        """User Attribute.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_importer_identity_provider_mapper#user_attribute AttributeImporterIdentityProviderMapper#user_attribute}
        """
        result = self._values.get("user_attribute")
        assert result is not None, "Required property 'user_attribute' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attribute_friendly_name(self) -> typing.Optional[builtins.str]:
        """Attribute Friendly Name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_importer_identity_provider_mapper#attribute_friendly_name AttributeImporterIdentityProviderMapper#attribute_friendly_name}
        """
        result = self._values.get("attribute_friendly_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def attribute_name(self) -> typing.Optional[builtins.str]:
        """Attribute Name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_importer_identity_provider_mapper#attribute_name AttributeImporterIdentityProviderMapper#attribute_name}
        """
        result = self._values.get("attribute_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def claim_name(self) -> typing.Optional[builtins.str]:
        """Claim Name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_importer_identity_provider_mapper#claim_name AttributeImporterIdentityProviderMapper#claim_name}
        """
        result = self._values.get("claim_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extra_config(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_importer_identity_provider_mapper#extra_config AttributeImporterIdentityProviderMapper#extra_config}."""
        result = self._values.get("extra_config")
        return typing.cast(
            typing.Optional[typing.Mapping[builtins.str, builtins.str]], result
        )

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/attribute_importer_identity_provider_mapper#id AttributeImporterIdentityProviderMapper#id}.

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
        return "AttributeImporterIdentityProviderMapperConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AttributeImporterIdentityProviderMapper",
    "AttributeImporterIdentityProviderMapperConfig",
]

publication.publish()


def _typecheckingstub__050be39f01d4d0c64a8df3b22eeb90985a37cfa91b9ab46ff79d53fe2520481a(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    identity_provider_alias: builtins.str,
    name: builtins.str,
    realm: builtins.str,
    user_attribute: builtins.str,
    attribute_friendly_name: typing.Optional[builtins.str] = None,
    attribute_name: typing.Optional[builtins.str] = None,
    claim_name: typing.Optional[builtins.str] = None,
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


def _typecheckingstub__f7ac58735ffb65f14cf4417999866c6dd177d5948836a77c70d3b8d05529928e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__fb0acc7c04ab059b7dd97f7a2e6d660416969442aab7f09d63bdb0a522cb3798(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__01348939be9b875708097cc1810a51d404a0fb506b78b2cfe8a8a7bacb9bf5a9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__abad1c5ef8741e857b90b6298da9f27a3495f3df7e162700d33b2fb08e5c13c5(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ec23024d7cff99eaa8f71e27a20393a23621dc039335a59ca2c5afd31f996b8d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__41061dfff791de5773c105a0d21ad1840b645b0e44d2e1dbe9bb38709969e66d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__68d6d84c4ab62ace81afcfedf7d3ff1e8bb1992a32c884203d125718c131ca2d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7200721205c2e475191e781b7cdd970b2aead3d36ea6ad46fae679ce0c2d9938(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__c4a80ad7e39d5288d92f0c4a0d92b0268eb1e1537970707082881ebd5594f788(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__a2c7dfa1326815d2645cbd56d5786e796222fa5447187902daaa36cfa11dd0cc(
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
    user_attribute: builtins.str,
    attribute_friendly_name: typing.Optional[builtins.str] = None,
    attribute_name: typing.Optional[builtins.str] = None,
    claim_name: typing.Optional[builtins.str] = None,
    extra_config: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
