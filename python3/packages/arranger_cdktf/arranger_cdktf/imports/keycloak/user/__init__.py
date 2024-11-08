"""
# `keycloak_user`

Refer to the Terraform Registory for docs: [`keycloak_user`](https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user).
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


class User(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.user.User",
):
    """Represents a {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user keycloak_user}."""

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        realm_id: builtins.str,
        username: builtins.str,
        attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        email: typing.Optional[builtins.str] = None,
        email_verified: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        enabled: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        federated_identity: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable,
                typing.Sequence[
                    typing.Union[
                        "UserFederatedIdentity", typing.Dict[builtins.str, typing.Any]
                    ]
                ],
            ]
        ] = None,
        first_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        initial_password: typing.Optional[
            typing.Union["UserInitialPassword", typing.Dict[builtins.str, typing.Any]]
        ] = None,
        last_name: typing.Optional[builtins.str] = None,
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
        """Create a new {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user keycloak_user} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param realm_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#realm_id User#realm_id}.
        :param username: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#username User#username}.
        :param attributes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#attributes User#attributes}.
        :param email: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#email User#email}.
        :param email_verified: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#email_verified User#email_verified}.
        :param enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#enabled User#enabled}.
        :param federated_identity: federated_identity block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#federated_identity User#federated_identity}
        :param first_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#first_name User#first_name}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#id User#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param initial_password: initial_password block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#initial_password User#initial_password}
        :param last_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#last_name User#last_name}.
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
                _typecheckingstub__07be2110e46b48f2588be32dfd17abc600e0e8446154c1217593b15ca27d7f9e
            )
            check_type(
                argname="argument scope", value=scope, expected_type=type_hints["scope"]
            )
            check_type(
                argname="argument id_", value=id_, expected_type=type_hints["id_"]
            )
        config = UserConfig(
            realm_id=realm_id,
            username=username,
            attributes=attributes,
            email=email,
            email_verified=email_verified,
            enabled=enabled,
            federated_identity=federated_identity,
            first_name=first_name,
            id=id,
            initial_password=initial_password,
            last_name=last_name,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putFederatedIdentity")
    def put_federated_identity(
        self,
        value: typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    "UserFederatedIdentity", typing.Dict[builtins.str, typing.Any]
                ]
            ],
        ],
    ) -> None:
        """
        :param value: -
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__6cd189b61456cae2c2b7fa7ea2edc08a8fc5d96dab180baae4cde659b1f2e9ab
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        return typing.cast(None, jsii.invoke(self, "putFederatedIdentity", [value]))

    @jsii.member(jsii_name="putInitialPassword")
    def put_initial_password(
        self,
        *,
        value: builtins.str,
        temporary: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
    ) -> None:
        """
        :param value: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#value User#value}.
        :param temporary: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#temporary User#temporary}.
        """
        value_ = UserInitialPassword(value=value, temporary=temporary)

        return typing.cast(None, jsii.invoke(self, "putInitialPassword", [value_]))

    @jsii.member(jsii_name="resetAttributes")
    def reset_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttributes", []))

    @jsii.member(jsii_name="resetEmail")
    def reset_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmail", []))

    @jsii.member(jsii_name="resetEmailVerified")
    def reset_email_verified(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailVerified", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetFederatedIdentity")
    def reset_federated_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFederatedIdentity", []))

    @jsii.member(jsii_name="resetFirstName")
    def reset_first_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirstName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInitialPassword")
    def reset_initial_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitialPassword", []))

    @jsii.member(jsii_name="resetLastName")
    def reset_last_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLastName", []))

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
    @jsii.member(jsii_name="federatedIdentity")
    def federated_identity(self) -> "UserFederatedIdentityList":
        return typing.cast(
            "UserFederatedIdentityList", jsii.get(self, "federatedIdentity")
        )

    @builtins.property
    @jsii.member(jsii_name="initialPassword")
    def initial_password(self) -> "UserInitialPasswordOutputReference":
        return typing.cast(
            "UserInitialPasswordOutputReference", jsii.get(self, "initialPassword")
        )

    @builtins.property
    @jsii.member(jsii_name="attributesInput")
    def attributes_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(
            typing.Optional[typing.Mapping[builtins.str, builtins.str]],
            jsii.get(self, "attributesInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="emailVerifiedInput")
    def email_verified_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "emailVerifiedInput"),
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
    @jsii.member(jsii_name="federatedIdentityInput")
    def federated_identity_input(
        self,
    ) -> typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["UserFederatedIdentity"]]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable, typing.List["UserFederatedIdentity"]
                ]
            ],
            jsii.get(self, "federatedIdentityInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="firstNameInput")
    def first_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "firstNameInput")
        )

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="initialPasswordInput")
    def initial_password_input(self) -> typing.Optional["UserInitialPassword"]:
        return typing.cast(
            typing.Optional["UserInitialPassword"],
            jsii.get(self, "initialPasswordInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="lastNameInput")
    def last_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "lastNameInput")
        )

    @builtins.property
    @jsii.member(jsii_name="realmIdInput")
    def realm_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "realmIdInput")
        )

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "usernameInput")
        )

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(
            typing.Mapping[builtins.str, builtins.str], jsii.get(self, "attributes")
        )

    @attributes.setter
    def attributes(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__fc583523ebedc8230feb4b0482f670d149618b695afc064c22040bb2d318e101
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "attributes", value)

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @email.setter
    def email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__b2d5a71464889ad342b72dbf79d0a30bc11cb9ddd05aa4c702eac2699a9c5d12
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="emailVerified")
    def email_verified(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "emailVerified"),
        )

    @email_verified.setter
    def email_verified(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__1d04a50e9a69dae726a5573658543b2b299895666b40622ff8d1d5959c6c05ca
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "emailVerified", value)

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
                _typecheckingstub__da01d47f50cd94941f1a495935fd41c70bea241f867ce81d78d1b4b6e8635ccc
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="firstName")
    def first_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firstName"))

    @first_name.setter
    def first_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__8b54f9a36fae2a4d63213dc40c972358998854646ae027d734609b730368a719
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "firstName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__3bf385a4c20de1355af2e559e4dfd3ab61f84724890204e48c1027f3467740a6
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="lastName")
    def last_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastName"))

    @last_name.setter
    def last_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__ba13e3a3566c415cc1c7510510bfa90c650b4f969744a8fec10da07f6d20fd08
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "lastName", value)

    @builtins.property
    @jsii.member(jsii_name="realmId")
    def realm_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "realmId"))

    @realm_id.setter
    def realm_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__358e1f02d97127a21e9033112d08be8023553a5d77b29ef52b9f46b8851a2eaf
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "realmId", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__7a5d5a9e3528ce70f5d81c30d2173b43fe46cdf7d3a21e4646fca7329f43dd7b
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "username", value)


@jsii.data_type(
    jsii_type="keycloak.user.UserConfig",
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
        "username": "username",
        "attributes": "attributes",
        "email": "email",
        "email_verified": "emailVerified",
        "enabled": "enabled",
        "federated_identity": "federatedIdentity",
        "first_name": "firstName",
        "id": "id",
        "initial_password": "initialPassword",
        "last_name": "lastName",
    },
)
class UserConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        username: builtins.str,
        attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        email: typing.Optional[builtins.str] = None,
        email_verified: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        enabled: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
        federated_identity: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable,
                typing.Sequence[
                    typing.Union[
                        "UserFederatedIdentity", typing.Dict[builtins.str, typing.Any]
                    ]
                ],
            ]
        ] = None,
        first_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        initial_password: typing.Optional[
            typing.Union["UserInitialPassword", typing.Dict[builtins.str, typing.Any]]
        ] = None,
        last_name: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param connection:
        :param count:
        :param depends_on:
        :param for_each:
        :param lifecycle:
        :param provider:
        :param provisioners:
        :param realm_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#realm_id User#realm_id}.
        :param username: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#username User#username}.
        :param attributes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#attributes User#attributes}.
        :param email: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#email User#email}.
        :param email_verified: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#email_verified User#email_verified}.
        :param enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#enabled User#enabled}.
        :param federated_identity: federated_identity block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#federated_identity User#federated_identity}
        :param first_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#first_name User#first_name}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#id User#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param initial_password: initial_password block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#initial_password User#initial_password}
        :param last_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#last_name User#last_name}.
        """
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(initial_password, dict):
            initial_password = UserInitialPassword(**initial_password)
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__6d02061955edf4e0f99b79a692d72b7560eecb1a3ef266eb5886b46a72b2f5e5
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
                argname="argument username",
                value=username,
                expected_type=type_hints["username"],
            )
            check_type(
                argname="argument attributes",
                value=attributes,
                expected_type=type_hints["attributes"],
            )
            check_type(
                argname="argument email", value=email, expected_type=type_hints["email"]
            )
            check_type(
                argname="argument email_verified",
                value=email_verified,
                expected_type=type_hints["email_verified"],
            )
            check_type(
                argname="argument enabled",
                value=enabled,
                expected_type=type_hints["enabled"],
            )
            check_type(
                argname="argument federated_identity",
                value=federated_identity,
                expected_type=type_hints["federated_identity"],
            )
            check_type(
                argname="argument first_name",
                value=first_name,
                expected_type=type_hints["first_name"],
            )
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(
                argname="argument initial_password",
                value=initial_password,
                expected_type=type_hints["initial_password"],
            )
            check_type(
                argname="argument last_name",
                value=last_name,
                expected_type=type_hints["last_name"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "realm_id": realm_id,
            "username": username,
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
        if attributes is not None:
            self._values["attributes"] = attributes
        if email is not None:
            self._values["email"] = email
        if email_verified is not None:
            self._values["email_verified"] = email_verified
        if enabled is not None:
            self._values["enabled"] = enabled
        if federated_identity is not None:
            self._values["federated_identity"] = federated_identity
        if first_name is not None:
            self._values["first_name"] = first_name
        if id is not None:
            self._values["id"] = id
        if initial_password is not None:
            self._values["initial_password"] = initial_password
        if last_name is not None:
            self._values["last_name"] = last_name

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
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#realm_id User#realm_id}."""
        result = self._values.get("realm_id")
        assert result is not None, "Required property 'realm_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#username User#username}."""
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attributes(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#attributes User#attributes}."""
        result = self._values.get("attributes")
        return typing.cast(
            typing.Optional[typing.Mapping[builtins.str, builtins.str]], result
        )

    @builtins.property
    def email(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#email User#email}."""
        result = self._values.get("email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def email_verified(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#email_verified User#email_verified}."""
        result = self._values.get("email_verified")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#enabled User#enabled}."""
        result = self._values.get("enabled")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    @builtins.property
    def federated_identity(
        self,
    ) -> typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["UserFederatedIdentity"]]
    ]:
        """federated_identity block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#federated_identity User#federated_identity}
        """
        result = self._values.get("federated_identity")
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable, typing.List["UserFederatedIdentity"]
                ]
            ],
            result,
        )

    @builtins.property
    def first_name(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#first_name User#first_name}."""
        result = self._values.get("first_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#id User#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        """
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def initial_password(self) -> typing.Optional["UserInitialPassword"]:
        """initial_password block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#initial_password User#initial_password}
        """
        result = self._values.get("initial_password")
        return typing.cast(typing.Optional["UserInitialPassword"], result)

    @builtins.property
    def last_name(self) -> typing.Optional[builtins.str]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#last_name User#last_name}."""
        result = self._values.get("last_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="keycloak.user.UserFederatedIdentity",
    jsii_struct_bases=[],
    name_mapping={
        "identity_provider": "identityProvider",
        "user_id": "userId",
        "user_name": "userName",
    },
)
class UserFederatedIdentity:
    def __init__(
        self,
        *,
        identity_provider: builtins.str,
        user_id: builtins.str,
        user_name: builtins.str,
    ) -> None:
        """
        :param identity_provider: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#identity_provider User#identity_provider}.
        :param user_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#user_id User#user_id}.
        :param user_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#user_name User#user_name}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__f7b171db1f1c13323cd06044681ed1b444231c708f53bdb72a9b3421a0ba2c38
            )
            check_type(
                argname="argument identity_provider",
                value=identity_provider,
                expected_type=type_hints["identity_provider"],
            )
            check_type(
                argname="argument user_id",
                value=user_id,
                expected_type=type_hints["user_id"],
            )
            check_type(
                argname="argument user_name",
                value=user_name,
                expected_type=type_hints["user_name"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "identity_provider": identity_provider,
            "user_id": user_id,
            "user_name": user_name,
        }

    @builtins.property
    def identity_provider(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#identity_provider User#identity_provider}."""
        result = self._values.get("identity_provider")
        assert result is not None, "Required property 'identity_provider' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_id(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#user_id User#user_id}."""
        result = self._values.get("user_id")
        assert result is not None, "Required property 'user_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_name(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#user_name User#user_name}."""
        result = self._values.get("user_name")
        assert result is not None, "Required property 'user_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserFederatedIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class UserFederatedIdentityList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.user.UserFederatedIdentityList",
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
                _typecheckingstub__863b9474d9620ac3194d182a6f9ff495932562e91ffeb6cf6a31dbb6457fb3c3
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
    def get(self, index: jsii.Number) -> "UserFederatedIdentityOutputReference":
        """
        :param index: the index of the item to return.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__dc8d412c36f555d3d57d5cbf8007f9cdf35887e661f817c17b44fdacc574be9b
            )
            check_type(
                argname="argument index", value=index, expected_type=type_hints["index"]
            )
        return typing.cast(
            "UserFederatedIdentityOutputReference", jsii.invoke(self, "get", [index])
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
                _typecheckingstub__baab1e15c0e1172bf2089afbd9b1d603032383e97a2b952fe7b1e4acdcd98b8b
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
                _typecheckingstub__bb41d37d62a06e3be1693758d9369d6926da68733b00ed326a4e3026c68c5767
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
                _typecheckingstub__759ca2a359dac523fc1443fe7579a332910c8b65a0875bf9324bc65ab17c5601
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
        typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[UserFederatedIdentity]]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[
                    _cdktf_9a9027ec.IResolvable, typing.List[UserFederatedIdentity]
                ]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[
                _cdktf_9a9027ec.IResolvable, typing.List[UserFederatedIdentity]
            ]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__9ffca735b714216790740d8f112495ee530b4ed1709568c71e0983a2542908f6
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


class UserFederatedIdentityOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.user.UserFederatedIdentityOutputReference",
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
                _typecheckingstub__cb899fd2d2329b797acfa2419a6cc016459e04ea8695fb37e2b6447069370df6
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

    @builtins.property
    @jsii.member(jsii_name="identityProviderInput")
    def identity_provider_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "identityProviderInput")
        )

    @builtins.property
    @jsii.member(jsii_name="userIdInput")
    def user_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userIdInput"))

    @builtins.property
    @jsii.member(jsii_name="userNameInput")
    def user_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(
            typing.Optional[builtins.str], jsii.get(self, "userNameInput")
        )

    @builtins.property
    @jsii.member(jsii_name="identityProvider")
    def identity_provider(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityProvider"))

    @identity_provider.setter
    def identity_provider(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__88638c1f3b2f4a5cd7be0dca731a85a8dbdc315973c3ed3a57a203fee51d4e22
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "identityProvider", value)

    @builtins.property
    @jsii.member(jsii_name="userId")
    def user_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userId"))

    @user_id.setter
    def user_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__f2fe04178a824a578dbff50670fd6f53de45bb01bb19f14f746720c970670490
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "userId", value)

    @builtins.property
    @jsii.member(jsii_name="userName")
    def user_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userName"))

    @user_name.setter
    def user_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__5ca804b612ed43d6a84781c788ffd7ac92709bf85427b55f9699afd0f8e6b0eb
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "userName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, UserFederatedIdentity]
    ]:
        return typing.cast(
            typing.Optional[
                typing.Union[_cdktf_9a9027ec.IResolvable, UserFederatedIdentity]
            ],
            jsii.get(self, "internalValue"),
        )

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[
            typing.Union[_cdktf_9a9027ec.IResolvable, UserFederatedIdentity]
        ],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__fb056b577e958689a439475c46ac7485b557676ab692ded84f590e2c14785575
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="keycloak.user.UserInitialPassword",
    jsii_struct_bases=[],
    name_mapping={"value": "value", "temporary": "temporary"},
)
class UserInitialPassword:
    def __init__(
        self,
        *,
        value: builtins.str,
        temporary: typing.Optional[
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
        ] = None,
    ) -> None:
        """
        :param value: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#value User#value}.
        :param temporary: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#temporary User#temporary}.
        """
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__1ac1905e063e394a686b4261d37d88934048da03fab260872ec34bb7cb83ce71
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
            check_type(
                argname="argument temporary",
                value=temporary,
                expected_type=type_hints["temporary"],
            )
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "value": value,
        }
        if temporary is not None:
            self._values["temporary"] = temporary

    @builtins.property
    def value(self) -> builtins.str:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#value User#value}."""
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def temporary(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        """Docs at Terraform Registry: {@link https://registry.terraform.io/providers/mrparkers/keycloak/4.3.1/docs/resources/user#temporary User#temporary}."""
        result = self._values.get("temporary")
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            result,
        )

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserInitialPassword(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class UserInitialPasswordOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="keycloak.user.UserInitialPasswordOutputReference",
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
                _typecheckingstub__e046af26d09df802bcaac9762a6bf1fa7a03b889bc01213905bdd707a4ddad12
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

    @jsii.member(jsii_name="resetTemporary")
    def reset_temporary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTemporary", []))

    @builtins.property
    @jsii.member(jsii_name="temporaryInput")
    def temporary_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(
            typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
            jsii.get(self, "temporaryInput"),
        )

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="temporary")
    def temporary(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(
            typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
            jsii.get(self, "temporary"),
        )

    @temporary.setter
    def temporary(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__3ee829681946b696c600f234b8be49524158d3197398c28c5dae607e6dcd6553
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "temporary", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__27a74911d6c6b655aaab63c14394fd94b92e0e37956b8290f89652d5d5b662b3
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[UserInitialPassword]:
        return typing.cast(
            typing.Optional[UserInitialPassword], jsii.get(self, "internalValue")
        )

    @internal_value.setter
    def internal_value(self, value: typing.Optional[UserInitialPassword]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(
                _typecheckingstub__7da9aeeb7d795d232acc5182bcd6c0f2af102385da32a840e515566cfed7c55b
            )
            check_type(
                argname="argument value", value=value, expected_type=type_hints["value"]
            )
        jsii.set(self, "internalValue", value)


__all__ = [
    "User",
    "UserConfig",
    "UserFederatedIdentity",
    "UserFederatedIdentityList",
    "UserFederatedIdentityOutputReference",
    "UserInitialPassword",
    "UserInitialPasswordOutputReference",
]

publication.publish()


def _typecheckingstub__07be2110e46b48f2588be32dfd17abc600e0e8446154c1217593b15ca27d7f9e(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    realm_id: builtins.str,
    username: builtins.str,
    attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    email: typing.Optional[builtins.str] = None,
    email_verified: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    enabled: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    federated_identity: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    UserFederatedIdentity, typing.Dict[builtins.str, typing.Any]
                ]
            ],
        ]
    ] = None,
    first_name: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    initial_password: typing.Optional[
        typing.Union[UserInitialPassword, typing.Dict[builtins.str, typing.Any]]
    ] = None,
    last_name: typing.Optional[builtins.str] = None,
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


def _typecheckingstub__6cd189b61456cae2c2b7fa7ea2edc08a8fc5d96dab180baae4cde659b1f2e9ab(
    value: typing.Union[
        _cdktf_9a9027ec.IResolvable,
        typing.Sequence[
            typing.Union[UserFederatedIdentity, typing.Dict[builtins.str, typing.Any]]
        ],
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__fc583523ebedc8230feb4b0482f670d149618b695afc064c22040bb2d318e101(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__b2d5a71464889ad342b72dbf79d0a30bc11cb9ddd05aa4c702eac2699a9c5d12(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1d04a50e9a69dae726a5573658543b2b299895666b40622ff8d1d5959c6c05ca(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__da01d47f50cd94941f1a495935fd41c70bea241f867ce81d78d1b4b6e8635ccc(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__8b54f9a36fae2a4d63213dc40c972358998854646ae027d734609b730368a719(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3bf385a4c20de1355af2e559e4dfd3ab61f84724890204e48c1027f3467740a6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__ba13e3a3566c415cc1c7510510bfa90c650b4f969744a8fec10da07f6d20fd08(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__358e1f02d97127a21e9033112d08be8023553a5d77b29ef52b9f46b8851a2eaf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7a5d5a9e3528ce70f5d81c30d2173b43fe46cdf7d3a21e4646fca7329f43dd7b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__6d02061955edf4e0f99b79a692d72b7560eecb1a3ef266eb5886b46a72b2f5e5(
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
    username: builtins.str,
    attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    email: typing.Optional[builtins.str] = None,
    email_verified: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    enabled: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
    federated_identity: typing.Optional[
        typing.Union[
            _cdktf_9a9027ec.IResolvable,
            typing.Sequence[
                typing.Union[
                    UserFederatedIdentity, typing.Dict[builtins.str, typing.Any]
                ]
            ],
        ]
    ] = None,
    first_name: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    initial_password: typing.Optional[
        typing.Union[UserInitialPassword, typing.Dict[builtins.str, typing.Any]]
    ] = None,
    last_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f7b171db1f1c13323cd06044681ed1b444231c708f53bdb72a9b3421a0ba2c38(
    *,
    identity_provider: builtins.str,
    user_id: builtins.str,
    user_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__863b9474d9620ac3194d182a6f9ff495932562e91ffeb6cf6a31dbb6457fb3c3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__dc8d412c36f555d3d57d5cbf8007f9cdf35887e661f817c17b44fdacc574be9b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__baab1e15c0e1172bf2089afbd9b1d603032383e97a2b952fe7b1e4acdcd98b8b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__bb41d37d62a06e3be1693758d9369d6926da68733b00ed326a4e3026c68c5767(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__759ca2a359dac523fc1443fe7579a332910c8b65a0875bf9324bc65ab17c5601(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__9ffca735b714216790740d8f112495ee530b4ed1709568c71e0983a2542908f6(
    value: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[UserFederatedIdentity]]
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__cb899fd2d2329b797acfa2419a6cc016459e04ea8695fb37e2b6447069370df6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__88638c1f3b2f4a5cd7be0dca731a85a8dbdc315973c3ed3a57a203fee51d4e22(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__f2fe04178a824a578dbff50670fd6f53de45bb01bb19f14f746720c970670490(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__5ca804b612ed43d6a84781c788ffd7ac92709bf85427b55f9699afd0f8e6b0eb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__fb056b577e958689a439475c46ac7485b557676ab692ded84f590e2c14785575(
    value: typing.Optional[
        typing.Union[_cdktf_9a9027ec.IResolvable, UserFederatedIdentity]
    ],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__1ac1905e063e394a686b4261d37d88934048da03fab260872ec34bb7cb83ce71(
    *,
    value: builtins.str,
    temporary: typing.Optional[
        typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]
    ] = None,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__e046af26d09df802bcaac9762a6bf1fa7a03b889bc01213905bdd707a4ddad12(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__3ee829681946b696c600f234b8be49524158d3197398c28c5dae607e6dcd6553(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__27a74911d6c6b655aaab63c14394fd94b92e0e37956b8290f89652d5d5b662b3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass


def _typecheckingstub__7da9aeeb7d795d232acc5182bcd6c0f2af102385da32a840e515566cfed7c55b(
    value: typing.Optional[UserInitialPassword],
) -> None:
    """Type checking stubs"""
    pass
