'''
# `aws_transfer_access`

Refer to the Terraform Registory for docs: [`aws_transfer_access`](https://www.terraform.io/docs/providers/aws/r/transfer_access).
'''
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


class TransferAccess(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.transferAccess.TransferAccess",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/transfer_access aws_transfer_access}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        external_id: builtins.str,
        server_id: builtins.str,
        home_directory: typing.Optional[builtins.str] = None,
        home_directory_mappings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["TransferAccessHomeDirectoryMappings", typing.Dict[builtins.str, typing.Any]]]]] = None,
        home_directory_type: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        policy: typing.Optional[builtins.str] = None,
        posix_profile: typing.Optional[typing.Union["TransferAccessPosixProfile", typing.Dict[builtins.str, typing.Any]]] = None,
        role: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/transfer_access aws_transfer_access} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param external_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#external_id TransferAccess#external_id}.
        :param server_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#server_id TransferAccess#server_id}.
        :param home_directory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#home_directory TransferAccess#home_directory}.
        :param home_directory_mappings: home_directory_mappings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#home_directory_mappings TransferAccess#home_directory_mappings}
        :param home_directory_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#home_directory_type TransferAccess#home_directory_type}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#id TransferAccess#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#policy TransferAccess#policy}.
        :param posix_profile: posix_profile block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#posix_profile TransferAccess#posix_profile}
        :param role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#role TransferAccess#role}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48839d8ec10dfee3b140d6564b90ea342f401c33477cd8c3a66b5d5e492885aa)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = TransferAccessConfig(
            external_id=external_id,
            server_id=server_id,
            home_directory=home_directory,
            home_directory_mappings=home_directory_mappings,
            home_directory_type=home_directory_type,
            id=id,
            policy=policy,
            posix_profile=posix_profile,
            role=role,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putHomeDirectoryMappings")
    def put_home_directory_mappings(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["TransferAccessHomeDirectoryMappings", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8d22b958bdf1cd9f1b9f3983e97deac4d9f476aca71d09867a5ce6adc3d345e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHomeDirectoryMappings", [value]))

    @jsii.member(jsii_name="putPosixProfile")
    def put_posix_profile(
        self,
        *,
        gid: jsii.Number,
        uid: jsii.Number,
        secondary_gids: typing.Optional[typing.Sequence[jsii.Number]] = None,
    ) -> None:
        '''
        :param gid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#gid TransferAccess#gid}.
        :param uid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#uid TransferAccess#uid}.
        :param secondary_gids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#secondary_gids TransferAccess#secondary_gids}.
        '''
        value = TransferAccessPosixProfile(
            gid=gid, uid=uid, secondary_gids=secondary_gids
        )

        return typing.cast(None, jsii.invoke(self, "putPosixProfile", [value]))

    @jsii.member(jsii_name="resetHomeDirectory")
    def reset_home_directory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHomeDirectory", []))

    @jsii.member(jsii_name="resetHomeDirectoryMappings")
    def reset_home_directory_mappings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHomeDirectoryMappings", []))

    @jsii.member(jsii_name="resetHomeDirectoryType")
    def reset_home_directory_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHomeDirectoryType", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPolicy")
    def reset_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicy", []))

    @jsii.member(jsii_name="resetPosixProfile")
    def reset_posix_profile(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPosixProfile", []))

    @jsii.member(jsii_name="resetRole")
    def reset_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRole", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="homeDirectoryMappings")
    def home_directory_mappings(self) -> "TransferAccessHomeDirectoryMappingsList":
        return typing.cast("TransferAccessHomeDirectoryMappingsList", jsii.get(self, "homeDirectoryMappings"))

    @builtins.property
    @jsii.member(jsii_name="posixProfile")
    def posix_profile(self) -> "TransferAccessPosixProfileOutputReference":
        return typing.cast("TransferAccessPosixProfileOutputReference", jsii.get(self, "posixProfile"))

    @builtins.property
    @jsii.member(jsii_name="externalIdInput")
    def external_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "externalIdInput"))

    @builtins.property
    @jsii.member(jsii_name="homeDirectoryInput")
    def home_directory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "homeDirectoryInput"))

    @builtins.property
    @jsii.member(jsii_name="homeDirectoryMappingsInput")
    def home_directory_mappings_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["TransferAccessHomeDirectoryMappings"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["TransferAccessHomeDirectoryMappings"]]], jsii.get(self, "homeDirectoryMappingsInput"))

    @builtins.property
    @jsii.member(jsii_name="homeDirectoryTypeInput")
    def home_directory_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "homeDirectoryTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="policyInput")
    def policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyInput"))

    @builtins.property
    @jsii.member(jsii_name="posixProfileInput")
    def posix_profile_input(self) -> typing.Optional["TransferAccessPosixProfile"]:
        return typing.cast(typing.Optional["TransferAccessPosixProfile"], jsii.get(self, "posixProfileInput"))

    @builtins.property
    @jsii.member(jsii_name="roleInput")
    def role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleInput"))

    @builtins.property
    @jsii.member(jsii_name="serverIdInput")
    def server_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverIdInput"))

    @builtins.property
    @jsii.member(jsii_name="externalId")
    def external_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalId"))

    @external_id.setter
    def external_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e159265ab8740e82d4cd082eb6eb234de26b1ae69ad3c323f7c3de3629beac7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalId", value)

    @builtins.property
    @jsii.member(jsii_name="homeDirectory")
    def home_directory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "homeDirectory"))

    @home_directory.setter
    def home_directory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8c7a576f1ec0c0816b5e1face4b1a93ab1e58d900e28cddc9b4262708502c33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "homeDirectory", value)

    @builtins.property
    @jsii.member(jsii_name="homeDirectoryType")
    def home_directory_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "homeDirectoryType"))

    @home_directory_type.setter
    def home_directory_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6a1fa245330ade166d2ea1ba44abc94a967089c1292b0e1bbd3a48b20a23496)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "homeDirectoryType", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42ff9efd6ee99a598ba3d1b51cf73dd79d1ba49b978c4934389ca0a5d5e284b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policy"))

    @policy.setter
    def policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6f0165ce56775e796d580038ee6f6492b3eb2e11b1af6b9f16958f0c7da02ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policy", value)

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @role.setter
    def role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__514e5336dc8b68a8ec553695ac047fbbfd748eeea92cca100f2fc6964433ec00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "role", value)

    @builtins.property
    @jsii.member(jsii_name="serverId")
    def server_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverId"))

    @server_id.setter
    def server_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f734e6e64e90f574a6e9e79344480fcfabc7a825d654ed883a4896597f513234)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverId", value)


@jsii.data_type(
    jsii_type="aws.transferAccess.TransferAccessConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "external_id": "externalId",
        "server_id": "serverId",
        "home_directory": "homeDirectory",
        "home_directory_mappings": "homeDirectoryMappings",
        "home_directory_type": "homeDirectoryType",
        "id": "id",
        "policy": "policy",
        "posix_profile": "posixProfile",
        "role": "role",
    },
)
class TransferAccessConfig(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
        external_id: builtins.str,
        server_id: builtins.str,
        home_directory: typing.Optional[builtins.str] = None,
        home_directory_mappings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["TransferAccessHomeDirectoryMappings", typing.Dict[builtins.str, typing.Any]]]]] = None,
        home_directory_type: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        policy: typing.Optional[builtins.str] = None,
        posix_profile: typing.Optional[typing.Union["TransferAccessPosixProfile", typing.Dict[builtins.str, typing.Any]]] = None,
        role: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param external_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#external_id TransferAccess#external_id}.
        :param server_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#server_id TransferAccess#server_id}.
        :param home_directory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#home_directory TransferAccess#home_directory}.
        :param home_directory_mappings: home_directory_mappings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#home_directory_mappings TransferAccess#home_directory_mappings}
        :param home_directory_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#home_directory_type TransferAccess#home_directory_type}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#id TransferAccess#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#policy TransferAccess#policy}.
        :param posix_profile: posix_profile block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#posix_profile TransferAccess#posix_profile}
        :param role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#role TransferAccess#role}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(posix_profile, dict):
            posix_profile = TransferAccessPosixProfile(**posix_profile)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a47c87917f2cacc2d3a99536d9cdbec1be589f206df8c00733df3f4b80c3cfc)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument external_id", value=external_id, expected_type=type_hints["external_id"])
            check_type(argname="argument server_id", value=server_id, expected_type=type_hints["server_id"])
            check_type(argname="argument home_directory", value=home_directory, expected_type=type_hints["home_directory"])
            check_type(argname="argument home_directory_mappings", value=home_directory_mappings, expected_type=type_hints["home_directory_mappings"])
            check_type(argname="argument home_directory_type", value=home_directory_type, expected_type=type_hints["home_directory_type"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            check_type(argname="argument posix_profile", value=posix_profile, expected_type=type_hints["posix_profile"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "external_id": external_id,
            "server_id": server_id,
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
        if home_directory is not None:
            self._values["home_directory"] = home_directory
        if home_directory_mappings is not None:
            self._values["home_directory_mappings"] = home_directory_mappings
        if home_directory_type is not None:
            self._values["home_directory_type"] = home_directory_type
        if id is not None:
            self._values["id"] = id
        if policy is not None:
            self._values["policy"] = policy
        if posix_profile is not None:
            self._values["posix_profile"] = posix_profile
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]], result)

    @builtins.property
    def external_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#external_id TransferAccess#external_id}.'''
        result = self._values.get("external_id")
        assert result is not None, "Required property 'external_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def server_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#server_id TransferAccess#server_id}.'''
        result = self._values.get("server_id")
        assert result is not None, "Required property 'server_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def home_directory(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#home_directory TransferAccess#home_directory}.'''
        result = self._values.get("home_directory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def home_directory_mappings(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["TransferAccessHomeDirectoryMappings"]]]:
        '''home_directory_mappings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#home_directory_mappings TransferAccess#home_directory_mappings}
        '''
        result = self._values.get("home_directory_mappings")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["TransferAccessHomeDirectoryMappings"]]], result)

    @builtins.property
    def home_directory_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#home_directory_type TransferAccess#home_directory_type}.'''
        result = self._values.get("home_directory_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#id TransferAccess#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#policy TransferAccess#policy}.'''
        result = self._values.get("policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def posix_profile(self) -> typing.Optional["TransferAccessPosixProfile"]:
        '''posix_profile block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#posix_profile TransferAccess#posix_profile}
        '''
        result = self._values.get("posix_profile")
        return typing.cast(typing.Optional["TransferAccessPosixProfile"], result)

    @builtins.property
    def role(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#role TransferAccess#role}.'''
        result = self._values.get("role")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferAccessConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.transferAccess.TransferAccessHomeDirectoryMappings",
    jsii_struct_bases=[],
    name_mapping={"entry": "entry", "target": "target"},
)
class TransferAccessHomeDirectoryMappings:
    def __init__(self, *, entry: builtins.str, target: builtins.str) -> None:
        '''
        :param entry: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#entry TransferAccess#entry}.
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#target TransferAccess#target}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfb79ef04334f519bf745813232e7225a2b14c650d15ca990ef7c02a6f844ed4)
            check_type(argname="argument entry", value=entry, expected_type=type_hints["entry"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "entry": entry,
            "target": target,
        }

    @builtins.property
    def entry(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#entry TransferAccess#entry}.'''
        result = self._values.get("entry")
        assert result is not None, "Required property 'entry' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#target TransferAccess#target}.'''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferAccessHomeDirectoryMappings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TransferAccessHomeDirectoryMappingsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.transferAccess.TransferAccessHomeDirectoryMappingsList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf8c9182a9d51548fb4da7b85cdf9ac583b55cf1ddc0f82ca5727b49396c1149)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "TransferAccessHomeDirectoryMappingsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5cec472c91b979c7baee67f64513546fd7749de8fc809dfa920e857edb7230b9)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("TransferAccessHomeDirectoryMappingsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__522f681d23c5c8b3e914df86f472fc1f8f5fe9595a505f391097de60e038139b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af21ad86da9f230d01757feb91b573309bd39b4af57aa7ef01d381e5b30f6c95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3cd31a900d241ba37d3f2fdef0dee7e5867d17ee468fb791d62a2e5f963ec50)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[TransferAccessHomeDirectoryMappings]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[TransferAccessHomeDirectoryMappings]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[TransferAccessHomeDirectoryMappings]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30612b6932ebbc4e4e9a8db2a44d95ae1dc7f302bcdb1125c7438b0fb5e89dfa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class TransferAccessHomeDirectoryMappingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.transferAccess.TransferAccessHomeDirectoryMappingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d30948d27dbe7b453ba1d95dbc536404f71d4ec40642c8a0c8cfedc36ad1327c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="entryInput")
    def entry_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "entryInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="entry")
    def entry(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "entry"))

    @entry.setter
    def entry(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27a89d2a3dd909fab4d65cd1ce6e132f35f364a21b5a5dd28d887d7be92d9924)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entry", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92853b1bcd174e43c7bb0988cb841faeea4fbe9c948eae4702633c3727d36612)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[TransferAccessHomeDirectoryMappings, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[TransferAccessHomeDirectoryMappings, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[TransferAccessHomeDirectoryMappings, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83b182d247c321969e2cefcf275ee410be815106b12d5d523459027a33f38cec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.transferAccess.TransferAccessPosixProfile",
    jsii_struct_bases=[],
    name_mapping={"gid": "gid", "uid": "uid", "secondary_gids": "secondaryGids"},
)
class TransferAccessPosixProfile:
    def __init__(
        self,
        *,
        gid: jsii.Number,
        uid: jsii.Number,
        secondary_gids: typing.Optional[typing.Sequence[jsii.Number]] = None,
    ) -> None:
        '''
        :param gid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#gid TransferAccess#gid}.
        :param uid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#uid TransferAccess#uid}.
        :param secondary_gids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#secondary_gids TransferAccess#secondary_gids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff994f9133f727898d0c054550d6e25aada83e6fa2ec6ef68d36da5bf54bb0eb)
            check_type(argname="argument gid", value=gid, expected_type=type_hints["gid"])
            check_type(argname="argument uid", value=uid, expected_type=type_hints["uid"])
            check_type(argname="argument secondary_gids", value=secondary_gids, expected_type=type_hints["secondary_gids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "gid": gid,
            "uid": uid,
        }
        if secondary_gids is not None:
            self._values["secondary_gids"] = secondary_gids

    @builtins.property
    def gid(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#gid TransferAccess#gid}.'''
        result = self._values.get("gid")
        assert result is not None, "Required property 'gid' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def uid(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#uid TransferAccess#uid}.'''
        result = self._values.get("uid")
        assert result is not None, "Required property 'uid' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def secondary_gids(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/transfer_access#secondary_gids TransferAccess#secondary_gids}.'''
        result = self._values.get("secondary_gids")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransferAccessPosixProfile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TransferAccessPosixProfileOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.transferAccess.TransferAccessPosixProfileOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f555133474eb9aa78aec5df87a6858cd38f15ae151c0ffe5ff271dfb8e39e05b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetSecondaryGids")
    def reset_secondary_gids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecondaryGids", []))

    @builtins.property
    @jsii.member(jsii_name="gidInput")
    def gid_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "gidInput"))

    @builtins.property
    @jsii.member(jsii_name="secondaryGidsInput")
    def secondary_gids_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "secondaryGidsInput"))

    @builtins.property
    @jsii.member(jsii_name="uidInput")
    def uid_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "uidInput"))

    @builtins.property
    @jsii.member(jsii_name="gid")
    def gid(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "gid"))

    @gid.setter
    def gid(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aaddcfadc2922cea13689f7b5d2052fd5ce61e11f5a9d06744b439746a1499fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gid", value)

    @builtins.property
    @jsii.member(jsii_name="secondaryGids")
    def secondary_gids(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "secondaryGids"))

    @secondary_gids.setter
    def secondary_gids(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7c047dde0f87bacd0ebfe27cb693bf91b86ec438250a4c91fc728aec931ab21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secondaryGids", value)

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "uid"))

    @uid.setter
    def uid(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__704ece6ebff05620bed361f1923cd9a76ae328e7a0f7fc57327bdfb67f7b1a74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uid", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[TransferAccessPosixProfile]:
        return typing.cast(typing.Optional[TransferAccessPosixProfile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TransferAccessPosixProfile],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__577692432ce9cf45e1cff8485121e084887a8196c8e8498346430c6750502cda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "TransferAccess",
    "TransferAccessConfig",
    "TransferAccessHomeDirectoryMappings",
    "TransferAccessHomeDirectoryMappingsList",
    "TransferAccessHomeDirectoryMappingsOutputReference",
    "TransferAccessPosixProfile",
    "TransferAccessPosixProfileOutputReference",
]

publication.publish()

def _typecheckingstub__48839d8ec10dfee3b140d6564b90ea342f401c33477cd8c3a66b5d5e492885aa(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    external_id: builtins.str,
    server_id: builtins.str,
    home_directory: typing.Optional[builtins.str] = None,
    home_directory_mappings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[TransferAccessHomeDirectoryMappings, typing.Dict[builtins.str, typing.Any]]]]] = None,
    home_directory_type: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    policy: typing.Optional[builtins.str] = None,
    posix_profile: typing.Optional[typing.Union[TransferAccessPosixProfile, typing.Dict[builtins.str, typing.Any]]] = None,
    role: typing.Optional[builtins.str] = None,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8d22b958bdf1cd9f1b9f3983e97deac4d9f476aca71d09867a5ce6adc3d345e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[TransferAccessHomeDirectoryMappings, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e159265ab8740e82d4cd082eb6eb234de26b1ae69ad3c323f7c3de3629beac7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8c7a576f1ec0c0816b5e1face4b1a93ab1e58d900e28cddc9b4262708502c33(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6a1fa245330ade166d2ea1ba44abc94a967089c1292b0e1bbd3a48b20a23496(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42ff9efd6ee99a598ba3d1b51cf73dd79d1ba49b978c4934389ca0a5d5e284b4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6f0165ce56775e796d580038ee6f6492b3eb2e11b1af6b9f16958f0c7da02ca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__514e5336dc8b68a8ec553695ac047fbbfd748eeea92cca100f2fc6964433ec00(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f734e6e64e90f574a6e9e79344480fcfabc7a825d654ed883a4896597f513234(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a47c87917f2cacc2d3a99536d9cdbec1be589f206df8c00733df3f4b80c3cfc(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    external_id: builtins.str,
    server_id: builtins.str,
    home_directory: typing.Optional[builtins.str] = None,
    home_directory_mappings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[TransferAccessHomeDirectoryMappings, typing.Dict[builtins.str, typing.Any]]]]] = None,
    home_directory_type: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    policy: typing.Optional[builtins.str] = None,
    posix_profile: typing.Optional[typing.Union[TransferAccessPosixProfile, typing.Dict[builtins.str, typing.Any]]] = None,
    role: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfb79ef04334f519bf745813232e7225a2b14c650d15ca990ef7c02a6f844ed4(
    *,
    entry: builtins.str,
    target: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf8c9182a9d51548fb4da7b85cdf9ac583b55cf1ddc0f82ca5727b49396c1149(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cec472c91b979c7baee67f64513546fd7749de8fc809dfa920e857edb7230b9(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__522f681d23c5c8b3e914df86f472fc1f8f5fe9595a505f391097de60e038139b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af21ad86da9f230d01757feb91b573309bd39b4af57aa7ef01d381e5b30f6c95(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3cd31a900d241ba37d3f2fdef0dee7e5867d17ee468fb791d62a2e5f963ec50(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30612b6932ebbc4e4e9a8db2a44d95ae1dc7f302bcdb1125c7438b0fb5e89dfa(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[TransferAccessHomeDirectoryMappings]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d30948d27dbe7b453ba1d95dbc536404f71d4ec40642c8a0c8cfedc36ad1327c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27a89d2a3dd909fab4d65cd1ce6e132f35f364a21b5a5dd28d887d7be92d9924(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92853b1bcd174e43c7bb0988cb841faeea4fbe9c948eae4702633c3727d36612(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83b182d247c321969e2cefcf275ee410be815106b12d5d523459027a33f38cec(
    value: typing.Optional[typing.Union[TransferAccessHomeDirectoryMappings, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff994f9133f727898d0c054550d6e25aada83e6fa2ec6ef68d36da5bf54bb0eb(
    *,
    gid: jsii.Number,
    uid: jsii.Number,
    secondary_gids: typing.Optional[typing.Sequence[jsii.Number]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f555133474eb9aa78aec5df87a6858cd38f15ae151c0ffe5ff271dfb8e39e05b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aaddcfadc2922cea13689f7b5d2052fd5ce61e11f5a9d06744b439746a1499fd(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7c047dde0f87bacd0ebfe27cb693bf91b86ec438250a4c91fc728aec931ab21(
    value: typing.List[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__704ece6ebff05620bed361f1923cd9a76ae328e7a0f7fc57327bdfb67f7b1a74(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__577692432ce9cf45e1cff8485121e084887a8196c8e8498346430c6750502cda(
    value: typing.Optional[TransferAccessPosixProfile],
) -> None:
    """Type checking stubs"""
    pass
