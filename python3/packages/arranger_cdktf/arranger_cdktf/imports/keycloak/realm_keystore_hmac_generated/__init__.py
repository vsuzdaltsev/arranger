"""
# `keycloak_realm_keystore_hmac_generated`

Refer to the Terraform Registory for docs: [`keycloak_realm_keystore_hmac_generated`](https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_keystore_hmac_generated).
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


class RealmKeystoreHmacGenerated(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.realmKeystoreHmacGenerated.RealmKeystoreHmacGenerated",
):
    """Represents a {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_keystore_hmac_generated keycloak_realm_keystore_hmac_generated}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        realm_id: builtins.str,
        active: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        algorithm: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        id: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        secret_size: typing.Optional[jsii.Number] = None,
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
        """Create a new {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_keystore_hmac_generated keycloak_realm_keystore_hmac_generated} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Display name of provider when linked in admin console. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_keystore_hmac_generated#name RealmKeystoreHmacGenerated#name}
        :param realm_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_keystore_hmac_generated#realm_id RealmKeystoreHmacGenerated#realm_id}.
        :param active: Set if the keys can be used for signing. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_keystore_hmac_generated#active RealmKeystoreHmacGenerated#active}
        :param algorithm: Intended algorithm for the key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_keystore_hmac_generated#algorithm RealmKeystoreHmacGenerated#algorithm}
        :param enabled: Set if the keys are enabled. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_keystore_hmac_generated#enabled RealmKeystoreHmacGenerated#enabled}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_keystore_hmac_generated#id RealmKeystoreHmacGenerated#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param priority: Priority for the provider. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_keystore_hmac_generated#priority RealmKeystoreHmacGenerated#priority}
        :param secret_size: Size in bytes for the generated secret. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_keystore_hmac_generated#secret_size RealmKeystoreHmacGenerated#secret_size}
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
                _typecheckingstub__1ba9c36045866f8706e216b3a43b428a28b7e1d1baa003db2b3f9f0a117a0b75
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(
                argname="argument id_", value=id_, expected_type=type_hints["id_"]
            )
        config = RealmKeystoreHmacGeneratedConfig(
            name=name,
            realm_id=realm_id,
            active=active,
            algorithm=algorithm,
            enabled=enabled,
            id=id,
            priority=priority,
            secret_size=secret_size,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetActive")
    def reset_active(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActive", []))

    @jsii.member(jsii_name="resetAlgorithm")
    def reset_algorithm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlgorithm", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetSecretSize")
    def reset_secret_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretSize", []))

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
    @jsii.member(jsii_name="activeInput")
    def active_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "activeInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="algorithmInput")
    def algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "algorithmInput")
        )

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "enabledInput"),
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
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(
            typing.Optional[jsii.Number], jsii.get(self, "priorityInput")
        )

    @builtins.property
    @jsii.member(jsii_name="realmIdInput")
    def realm_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "realmIdInput")
        )

    @builtins.property
    @jsii.member(jsii_name="secretSizeInput")
    def secret_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(
            typing.Optional[jsii.Number], jsii.get(self, "secretSizeInput")
        )

    @builtins.property
    @jsii.member(jsii_name="active")
    def active(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "active"),
        )

    @active.setter
    def active(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b56d003e0229f6e5ad8b0fa88ea55325731d0ee5c37e645b380c94d5a2f41c64
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "active", value)

    @builtins.property
    @jsii.member(jsii_name="algorithm")
    def algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "algorithm"))

    @algorithm.setter
    def algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__ac7ae132ca53f3fb78229301b0d07976bde8435a87f4ed6fb948f0c77d4d8c4a
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "algorithm", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "enabled"),
        )

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__e98fe01e31b04f1ee2f78c49e7f654a4209652d14a2c3ad0dcb98f3d7aa42ee6
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__7a98fb16a83e0385a915a62305a179c30d63989122cbdcc509bc0f5fd69692a6
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__295402b41778be19592c9300286718307753fa1e4b3d4ea85682087cc27ad46a
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__2fd0424cc6c6d083169984e4e3a8ba58b18cd40092f329748db80ff96cbf6023
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="realmId")
    def realm_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "realmId"))

    @realm_id.setter
    def realm_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__3c39fcd5ea6f65ea61e7d67506eeeae21c8bdf3bba3c91d14f21e5735860b0c1
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "realmId", value)

    @builtins.property
    @jsii.member(jsii_name="secretSize")
    def secret_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "secretSize"))

    @secret_size.setter
    def secret_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__554f986ef14601440fa9d927d6776e812fc2f49c1b4d2d9d545a8156ea2160d7
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "secretSize", value)


@jsii.data_type(
    jsii_type="keycloak.realmKeystoreHmacGenerated.RealmKeystoreHmacGeneratedConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "realm_id": "realmId",
        "active": "active",
        "algorithm": "algorithm",
        "enabled": "enabled",
        "id": "id",
        "priority": "priority",
        "secret_size": "secretSize",
    },
)
class RealmKeystoreHmacGeneratedConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        name: builtins.str,
        realm_id: builtins.str,
        active: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        algorithm: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        id: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        secret_size: typing.Optional[jsii.Number] = None,
    ) -> None:
        """
        :param connection:
        :param count:
        :param depends_on:
        :param for_each:
        :param lifecycle:
        :param provider:
        :param provisioners:
        :param name: Display name of provider when linked in admin console. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_keystore_hmac_generated#name RealmKeystoreHmacGenerated#name}
        :param realm_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_keystore_hmac_generated#realm_id RealmKeystoreHmacGenerated#realm_id}.
        :param active: Set if the keys can be used for signing. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_keystore_hmac_generated#active RealmKeystoreHmacGenerated#active}
        :param algorithm: Intended algorithm for the key. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_keystore_hmac_generated#algorithm RealmKeystoreHmacGenerated#algorithm}
        :param enabled: Set if the keys are enabled. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_keystore_hmac_generated#enabled RealmKeystoreHmacGenerated#enabled}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_keystore_hmac_generated#id RealmKeystoreHmacGenerated#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param priority: Priority for the provider. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_keystore_hmac_generated#priority RealmKeystoreHmacGenerated#priority}
        :param secret_size: Size in bytes for the generated secret. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_keystore_hmac_generated#secret_size RealmKeystoreHmacGenerated#secret_size}
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__58f1c773ace4b96860d469ab795462672f5c6047a8a439765c4a04e71991d958
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
                argname="argument name", value=name, expected_type=type_hints["name"]
            )
            check_type(
                argname="argument realm_id",
                value=realm_id,
                expected_type=type_hints["realm_id"],
            )
            check_type(
                argname="argument active",
                value=active,
                expected_type=type_hints["active"],
            )
            check_type(
                argname="argument algorithm",
                value=algorithm,
                expected_type=type_hints["algorithm"],
            )
            check_type(
                argname="argument enabled",
                value=enabled,
                expected_type=type_hints["enabled"],
            )
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(
                argname="argument priority",
                value=priority,
                expected_type=type_hints["priority"],
            )
            check_type(
                argname="argument secret_size",
                value=secret_size,
                expected_type=type_hints["secret_size"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
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
        if active is not None:
            self._values["active"] = active
        if algorithm is not None:
            self._values["algorithm"] = algorithm
        if enabled is not None:
            self._values["enabled"] = enabled
        if id is not None:
            self._values["id"] = id
        if priority is not None:
            self._values["priority"] = priority
        if secret_size is not None:
            self._values["secret_size"] = secret_size

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
    def name(self) -> builtins.str:
        """Display name of provider when linked in admin console.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_keystore_hmac_generated#name RealmKeystoreHmacGenerated#name}
        """
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def realm_id(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_keystore_hmac_generated#realm_id RealmKeystoreHmacGenerated#realm_id}."""
        result = self._values.get("realm_id")
        assert result is not None, "Required property 'realm_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def active(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Set if the keys can be used for signing.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_keystore_hmac_generated#active RealmKeystoreHmacGenerated#active}
        """
        result = self._values.get("active")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def algorithm(self) -> typing.Optional[builtins.str]:
        """Intended algorithm for the key.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_keystore_hmac_generated#algorithm RealmKeystoreHmacGenerated#algorithm}
        """
        result = self._values.get("algorithm")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Set if the keys are enabled.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_keystore_hmac_generated#enabled RealmKeystoreHmacGenerated#enabled}
        """
        result = self._values.get("enabled")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_keystore_hmac_generated#id RealmKeystoreHmacGenerated#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        """Priority for the provider.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_keystore_hmac_generated#priority RealmKeystoreHmacGenerated#priority}
        """
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def secret_size(self) -> typing.Optional[jsii.Number]:
        """Size in bytes for the generated secret.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/realm_keystore_hmac_generated#secret_size RealmKeystoreHmacGenerated#secret_size}
        """
        result = self._values.get("secret_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RealmKeystoreHmacGeneratedConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "RealmKeystoreHmacGenerated",
    "RealmKeystoreHmacGeneratedConfig",
]

publication.publish()


def _typecheckingstub__1ba9c36045866f8706e216b3a43b428a28b7e1d1baa003db2b3f9f0a117a0b75(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    realm_id: builtins.str,
    active: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    algorithm: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    id: typing.Optional[builtins.str] = None,
    priority: typing.Optional[jsii.Number] = None,
    secret_size: typing.Optional[jsii.Number] = None,
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


def _typecheckingstub__b56d003e0229f6e5ad8b0fa88ea55325731d0ee5c37e645b380c94d5a2f41c64(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ac7ae132ca53f3fb78229301b0d07976bde8435a87f4ed6fb948f0c77d4d8c4a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e98fe01e31b04f1ee2f78c49e7f654a4209652d14a2c3ad0dcb98f3d7aa42ee6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7a98fb16a83e0385a915a62305a179c30d63989122cbdcc509bc0f5fd69692a6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__295402b41778be19592c9300286718307753fa1e4b3d4ea85682087cc27ad46a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__2fd0424cc6c6d083169984e4e3a8ba58b18cd40092f329748db80ff96cbf6023(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3c39fcd5ea6f65ea61e7d67506eeeae21c8bdf3bba3c91d14f21e5735860b0c1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__554f986ef14601440fa9d927d6776e812fc2f49c1b4d2d9d545a8156ea2160d7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__58f1c773ace4b96860d469ab795462672f5c6047a8a439765c4a04e71991d958(
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
    name: builtins.str,
    realm_id: builtins.str,
    active: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    algorithm: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    id: typing.Optional[builtins.str] = None,
    priority: typing.Optional[jsii.Number] = None,
    secret_size: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass
