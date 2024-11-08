'''
# `kubernetes_env`

Refer to the Terraform Registory for docs: [`kubernetes_env`](https://www.terraform.io/docs/providers/kubernetes/r/env).
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


class Env(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.env.Env",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/kubernetes/r/env kubernetes_env}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        api_version: builtins.str,
        container: builtins.str,
        env: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EnvEnv", typing.Dict[builtins.str, typing.Any]]]],
        kind: builtins.str,
        metadata: typing.Union["EnvMetadata", typing.Dict[builtins.str, typing.Any]],
        field_manager: typing.Optional[builtins.str] = None,
        force: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/kubernetes/r/env kubernetes_env} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param api_version: Resource API version. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#api_version Env#api_version}
        :param container: Name of the container for which we are updating the environment variables. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#container Env#container}
        :param env: env block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#env Env#env}
        :param kind: Resource Kind. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#kind Env#kind}
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#metadata Env#metadata}
        :param field_manager: Set the name of the field manager for the specified environment variables. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#field_manager Env#field_manager}
        :param force: Force overwriting environments that were created or edited outside of Terraform. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#force Env#force}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#id Env#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce7545d8f24c4b017b6f970baae0b57e90ae6c124a3b8f0bd59d315f4b315f44)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = EnvConfig(
            api_version=api_version,
            container=container,
            env=env,
            kind=kind,
            metadata=metadata,
            field_manager=field_manager,
            force=force,
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

    @jsii.member(jsii_name="putEnv")
    def put_env(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EnvEnv", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75687acb7d8866542f1b6c84918eb8b069ec69e3be42a0fd8b4754578f9be0f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEnv", [value]))

    @jsii.member(jsii_name="putMetadata")
    def put_metadata(
        self,
        *,
        name: builtins.str,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: The name of the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#name Env#name}
        :param namespace: The namespace of the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#namespace Env#namespace}
        '''
        value = EnvMetadata(name=name, namespace=namespace)

        return typing.cast(None, jsii.invoke(self, "putMetadata", [value]))

    @jsii.member(jsii_name="resetFieldManager")
    def reset_field_manager(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFieldManager", []))

    @jsii.member(jsii_name="resetForce")
    def reset_force(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForce", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="env")
    def env(self) -> "EnvEnvList":
        return typing.cast("EnvEnvList", jsii.get(self, "env"))

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> "EnvMetadataOutputReference":
        return typing.cast("EnvMetadataOutputReference", jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="apiVersionInput")
    def api_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="containerInput")
    def container_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerInput"))

    @builtins.property
    @jsii.member(jsii_name="envInput")
    def env_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EnvEnv"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EnvEnv"]]], jsii.get(self, "envInput"))

    @builtins.property
    @jsii.member(jsii_name="fieldManagerInput")
    def field_manager_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fieldManagerInput"))

    @builtins.property
    @jsii.member(jsii_name="forceInput")
    def force_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "forceInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(self) -> typing.Optional["EnvMetadata"]:
        return typing.cast(typing.Optional["EnvMetadata"], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="apiVersion")
    def api_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiVersion"))

    @api_version.setter
    def api_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c9ed293334491d47d68175cbaae71838f362d706f2125d0edea5f4f5de88d97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiVersion", value)

    @builtins.property
    @jsii.member(jsii_name="container")
    def container(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "container"))

    @container.setter
    def container(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38c1091906adeac526e5ad5d8868fa6f6a802b9e802cdc72fdb87817cb1bc0ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "container", value)

    @builtins.property
    @jsii.member(jsii_name="fieldManager")
    def field_manager(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fieldManager"))

    @field_manager.setter
    def field_manager(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__752b83c2428182bb9c80c6333ad6aa4bfad5d34ae0c3c67b4eb2c8f18630f588)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fieldManager", value)

    @builtins.property
    @jsii.member(jsii_name="force")
    def force(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "force"))

    @force.setter
    def force(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f140ed1a0d0e98d8f977d469137aa28e0c2494a6e3438f03314e9e747abe778)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "force", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f5024797c7c42d65398fba021c1cb6dd3347f522e5afd8dc340232341b56bb3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea66c4c2e601539d2f31f2abb84049a1e04ccb3b6fba878f474deabea23ec0af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)


@jsii.data_type(
    jsii_type="kubernetes.env.EnvConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "api_version": "apiVersion",
        "container": "container",
        "env": "env",
        "kind": "kind",
        "metadata": "metadata",
        "field_manager": "fieldManager",
        "force": "force",
        "id": "id",
    },
)
class EnvConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        api_version: builtins.str,
        container: builtins.str,
        env: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["EnvEnv", typing.Dict[builtins.str, typing.Any]]]],
        kind: builtins.str,
        metadata: typing.Union["EnvMetadata", typing.Dict[builtins.str, typing.Any]],
        field_manager: typing.Optional[builtins.str] = None,
        force: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param api_version: Resource API version. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#api_version Env#api_version}
        :param container: Name of the container for which we are updating the environment variables. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#container Env#container}
        :param env: env block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#env Env#env}
        :param kind: Resource Kind. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#kind Env#kind}
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#metadata Env#metadata}
        :param field_manager: Set the name of the field manager for the specified environment variables. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#field_manager Env#field_manager}
        :param force: Force overwriting environments that were created or edited outside of Terraform. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#force Env#force}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#id Env#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(metadata, dict):
            metadata = EnvMetadata(**metadata)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6aae9169754d123c6cd4902542bea4e43b56e0e6be01f33ad859f6eec1b2101)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument api_version", value=api_version, expected_type=type_hints["api_version"])
            check_type(argname="argument container", value=container, expected_type=type_hints["container"])
            check_type(argname="argument env", value=env, expected_type=type_hints["env"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument field_manager", value=field_manager, expected_type=type_hints["field_manager"])
            check_type(argname="argument force", value=force, expected_type=type_hints["force"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_version": api_version,
            "container": container,
            "env": env,
            "kind": kind,
            "metadata": metadata,
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
        if field_manager is not None:
            self._values["field_manager"] = field_manager
        if force is not None:
            self._values["force"] = force
        if id is not None:
            self._values["id"] = id

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
    def api_version(self) -> builtins.str:
        '''Resource API version.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#api_version Env#api_version}
        '''
        result = self._values.get("api_version")
        assert result is not None, "Required property 'api_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container(self) -> builtins.str:
        '''Name of the container for which we are updating the environment variables.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#container Env#container}
        '''
        result = self._values.get("container")
        assert result is not None, "Required property 'container' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def env(self) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EnvEnv"]]:
        '''env block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#env Env#env}
        '''
        result = self._values.get("env")
        assert result is not None, "Required property 'env' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["EnvEnv"]], result)

    @builtins.property
    def kind(self) -> builtins.str:
        '''Resource Kind.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#kind Env#kind}
        '''
        result = self._values.get("kind")
        assert result is not None, "Required property 'kind' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def metadata(self) -> "EnvMetadata":
        '''metadata block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#metadata Env#metadata}
        '''
        result = self._values.get("metadata")
        assert result is not None, "Required property 'metadata' is missing"
        return typing.cast("EnvMetadata", result)

    @builtins.property
    def field_manager(self) -> typing.Optional[builtins.str]:
        '''Set the name of the field manager for the specified environment variables.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#field_manager Env#field_manager}
        '''
        result = self._values.get("field_manager")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def force(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Force overwriting environments that were created or edited outside of Terraform.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#force Env#force}
        '''
        result = self._values.get("force")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#id Env#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.env.EnvEnv",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value", "value_from": "valueFrom"},
)
class EnvEnv:
    def __init__(
        self,
        *,
        name: builtins.str,
        value: typing.Optional[builtins.str] = None,
        value_from: typing.Optional[typing.Union["EnvEnvValueFrom", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param name: Name of the environment variable. Must be a C_IDENTIFIER. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#name Env#name}
        :param value: Variable references $(VAR_NAME) are expanded using the previous defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to "". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#value Env#value}
        :param value_from: value_from block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#value_from Env#value_from}
        '''
        if isinstance(value_from, dict):
            value_from = EnvEnvValueFrom(**value_from)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3c6b670cdd73a448f7a4a01fabf729e3149367b23b75c58d459596026700e3b)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument value_from", value=value_from, expected_type=type_hints["value_from"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if value is not None:
            self._values["value"] = value
        if value_from is not None:
            self._values["value_from"] = value_from

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the environment variable. Must be a C_IDENTIFIER.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#name Env#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Variable references $(VAR_NAME) are expanded using the previous defined environment variables in the container and any service environment variables.

        If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to "".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#value Env#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value_from(self) -> typing.Optional["EnvEnvValueFrom"]:
        '''value_from block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#value_from Env#value_from}
        '''
        result = self._values.get("value_from")
        return typing.cast(typing.Optional["EnvEnvValueFrom"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvEnv(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EnvEnvList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.env.EnvEnvList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__87dd6cc2ab6c8196dd9de1129f086c01608404a3693b392c9775dd0fbbb99683)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "EnvEnvOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dee89c5f56dc3941e41a8431bc861c1562f052c55afcf50585b5f83bc631e2a6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EnvEnvOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f74f93371108126757fd6162d595b2e08923f2bf341d27b333bffbae5794863)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5185b6deb4a96c358217ad081c4bb4244510b770887b401cbecfd3348f1d814b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b97fa42b53d5d0d0dd9f8afaaa4333b30adb9e635e50900f50368e43674e7517)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EnvEnv]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EnvEnv]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EnvEnv]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b16dbc9e0c0119cbc0e80669ea3c26d7de26a22517257442b8c9bdd6bc41abb1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EnvEnvOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.env.EnvEnvOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bb6069da1bd0f2256846600c88f1daff78ec991523da46e41e4e027b1df4609d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putValueFrom")
    def put_value_from(
        self,
        *,
        config_map_key_ref: typing.Optional[typing.Union["EnvEnvValueFromConfigMapKeyRef", typing.Dict[builtins.str, typing.Any]]] = None,
        field_ref: typing.Optional[typing.Union["EnvEnvValueFromFieldRef", typing.Dict[builtins.str, typing.Any]]] = None,
        resource_field_ref: typing.Optional[typing.Union["EnvEnvValueFromResourceFieldRef", typing.Dict[builtins.str, typing.Any]]] = None,
        secret_key_ref: typing.Optional[typing.Union["EnvEnvValueFromSecretKeyRef", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param config_map_key_ref: config_map_key_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#config_map_key_ref Env#config_map_key_ref}
        :param field_ref: field_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#field_ref Env#field_ref}
        :param resource_field_ref: resource_field_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#resource_field_ref Env#resource_field_ref}
        :param secret_key_ref: secret_key_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#secret_key_ref Env#secret_key_ref}
        '''
        value = EnvEnvValueFrom(
            config_map_key_ref=config_map_key_ref,
            field_ref=field_ref,
            resource_field_ref=resource_field_ref,
            secret_key_ref=secret_key_ref,
        )

        return typing.cast(None, jsii.invoke(self, "putValueFrom", [value]))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @jsii.member(jsii_name="resetValueFrom")
    def reset_value_from(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValueFrom", []))

    @builtins.property
    @jsii.member(jsii_name="valueFrom")
    def value_from(self) -> "EnvEnvValueFromOutputReference":
        return typing.cast("EnvEnvValueFromOutputReference", jsii.get(self, "valueFrom"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueFromInput")
    def value_from_input(self) -> typing.Optional["EnvEnvValueFrom"]:
        return typing.cast(typing.Optional["EnvEnvValueFrom"], jsii.get(self, "valueFromInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e899c5039be1a8a398b11fd1186f63f3a516db63b76b0bcb8d83b53b3e88ae3d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc17b10847d3b08f809b7df19e5963034c68bc08f8d15cf18d5a0e8f34e92b0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EnvEnv, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EnvEnv, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EnvEnv, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bfc6499eb904362fedf1603c8a1e095e4bb6f133d2cdc8799bcbe20a9a62f77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.env.EnvEnvValueFrom",
    jsii_struct_bases=[],
    name_mapping={
        "config_map_key_ref": "configMapKeyRef",
        "field_ref": "fieldRef",
        "resource_field_ref": "resourceFieldRef",
        "secret_key_ref": "secretKeyRef",
    },
)
class EnvEnvValueFrom:
    def __init__(
        self,
        *,
        config_map_key_ref: typing.Optional[typing.Union["EnvEnvValueFromConfigMapKeyRef", typing.Dict[builtins.str, typing.Any]]] = None,
        field_ref: typing.Optional[typing.Union["EnvEnvValueFromFieldRef", typing.Dict[builtins.str, typing.Any]]] = None,
        resource_field_ref: typing.Optional[typing.Union["EnvEnvValueFromResourceFieldRef", typing.Dict[builtins.str, typing.Any]]] = None,
        secret_key_ref: typing.Optional[typing.Union["EnvEnvValueFromSecretKeyRef", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param config_map_key_ref: config_map_key_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#config_map_key_ref Env#config_map_key_ref}
        :param field_ref: field_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#field_ref Env#field_ref}
        :param resource_field_ref: resource_field_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#resource_field_ref Env#resource_field_ref}
        :param secret_key_ref: secret_key_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#secret_key_ref Env#secret_key_ref}
        '''
        if isinstance(config_map_key_ref, dict):
            config_map_key_ref = EnvEnvValueFromConfigMapKeyRef(**config_map_key_ref)
        if isinstance(field_ref, dict):
            field_ref = EnvEnvValueFromFieldRef(**field_ref)
        if isinstance(resource_field_ref, dict):
            resource_field_ref = EnvEnvValueFromResourceFieldRef(**resource_field_ref)
        if isinstance(secret_key_ref, dict):
            secret_key_ref = EnvEnvValueFromSecretKeyRef(**secret_key_ref)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50f57e7d1adca1fa304f1573f48d48d3562fab2d18c2c9355844961b590514a6)
            check_type(argname="argument config_map_key_ref", value=config_map_key_ref, expected_type=type_hints["config_map_key_ref"])
            check_type(argname="argument field_ref", value=field_ref, expected_type=type_hints["field_ref"])
            check_type(argname="argument resource_field_ref", value=resource_field_ref, expected_type=type_hints["resource_field_ref"])
            check_type(argname="argument secret_key_ref", value=secret_key_ref, expected_type=type_hints["secret_key_ref"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if config_map_key_ref is not None:
            self._values["config_map_key_ref"] = config_map_key_ref
        if field_ref is not None:
            self._values["field_ref"] = field_ref
        if resource_field_ref is not None:
            self._values["resource_field_ref"] = resource_field_ref
        if secret_key_ref is not None:
            self._values["secret_key_ref"] = secret_key_ref

    @builtins.property
    def config_map_key_ref(self) -> typing.Optional["EnvEnvValueFromConfigMapKeyRef"]:
        '''config_map_key_ref block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#config_map_key_ref Env#config_map_key_ref}
        '''
        result = self._values.get("config_map_key_ref")
        return typing.cast(typing.Optional["EnvEnvValueFromConfigMapKeyRef"], result)

    @builtins.property
    def field_ref(self) -> typing.Optional["EnvEnvValueFromFieldRef"]:
        '''field_ref block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#field_ref Env#field_ref}
        '''
        result = self._values.get("field_ref")
        return typing.cast(typing.Optional["EnvEnvValueFromFieldRef"], result)

    @builtins.property
    def resource_field_ref(self) -> typing.Optional["EnvEnvValueFromResourceFieldRef"]:
        '''resource_field_ref block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#resource_field_ref Env#resource_field_ref}
        '''
        result = self._values.get("resource_field_ref")
        return typing.cast(typing.Optional["EnvEnvValueFromResourceFieldRef"], result)

    @builtins.property
    def secret_key_ref(self) -> typing.Optional["EnvEnvValueFromSecretKeyRef"]:
        '''secret_key_ref block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#secret_key_ref Env#secret_key_ref}
        '''
        result = self._values.get("secret_key_ref")
        return typing.cast(typing.Optional["EnvEnvValueFromSecretKeyRef"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvEnvValueFrom(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="kubernetes.env.EnvEnvValueFromConfigMapKeyRef",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "name": "name", "optional": "optional"},
)
class EnvEnvValueFromConfigMapKeyRef:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        optional: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param key: The key to select. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#key Env#key}
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#name Env#name}
        :param optional: Specify whether the ConfigMap or its key must be defined. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#optional Env#optional}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__890d6ddc23e73b60bc8d0c71c794fd21f80952f7263239b2ff663089280cdaee)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument optional", value=optional, expected_type=type_hints["optional"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if name is not None:
            self._values["name"] = name
        if optional is not None:
            self._values["optional"] = optional

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The key to select.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#key Env#key}
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#name Env#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def optional(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Specify whether the ConfigMap or its key must be defined.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#optional Env#optional}
        '''
        result = self._values.get("optional")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvEnvValueFromConfigMapKeyRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EnvEnvValueFromConfigMapKeyRefOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.env.EnvEnvValueFromConfigMapKeyRefOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e9a0a3fa09c0119a62ee48047728c021d38a538a1db603a310a520d3e2e4cf3f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetOptional")
    def reset_optional(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptional", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="optionalInput")
    def optional_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "optionalInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c540038fb4242cd44bcab7a5b938f9c7a1f6413534895b7413173750d13ed5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4963d6a5c3ac1564e02629e5ae163012eccccb496947355cdb4f75b6ae264a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="optional")
    def optional(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "optional"))

    @optional.setter
    def optional(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d77d4d96aa938a7f1f0c5f5cbd3049a265b7ab7a7fbf54e8f65cda15332cc5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "optional", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EnvEnvValueFromConfigMapKeyRef]:
        return typing.cast(typing.Optional[EnvEnvValueFromConfigMapKeyRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EnvEnvValueFromConfigMapKeyRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__090374ba7608b120585290f05fcd76e9ee225b0e51dc6fd20897bdf73eb427f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.env.EnvEnvValueFromFieldRef",
    jsii_struct_bases=[],
    name_mapping={"api_version": "apiVersion", "field_path": "fieldPath"},
)
class EnvEnvValueFromFieldRef:
    def __init__(
        self,
        *,
        api_version: typing.Optional[builtins.str] = None,
        field_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param api_version: Version of the schema the FieldPath is written in terms of, defaults to "v1". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#api_version Env#api_version}
        :param field_path: Path of the field to select in the specified API version. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#field_path Env#field_path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efb030d56d5b6a5fc159b705729561c69e7a6b3178712259351a9e1a4025de90)
            check_type(argname="argument api_version", value=api_version, expected_type=type_hints["api_version"])
            check_type(argname="argument field_path", value=field_path, expected_type=type_hints["field_path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if api_version is not None:
            self._values["api_version"] = api_version
        if field_path is not None:
            self._values["field_path"] = field_path

    @builtins.property
    def api_version(self) -> typing.Optional[builtins.str]:
        '''Version of the schema the FieldPath is written in terms of, defaults to "v1".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#api_version Env#api_version}
        '''
        result = self._values.get("api_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def field_path(self) -> typing.Optional[builtins.str]:
        '''Path of the field to select in the specified API version.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#field_path Env#field_path}
        '''
        result = self._values.get("field_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvEnvValueFromFieldRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EnvEnvValueFromFieldRefOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.env.EnvEnvValueFromFieldRefOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__071b171aa12c086cd955e6b1ed20ab9023bdb2ea1f36d4a8c78e4992e87e422f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetApiVersion")
    def reset_api_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiVersion", []))

    @jsii.member(jsii_name="resetFieldPath")
    def reset_field_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFieldPath", []))

    @builtins.property
    @jsii.member(jsii_name="apiVersionInput")
    def api_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="fieldPathInput")
    def field_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fieldPathInput"))

    @builtins.property
    @jsii.member(jsii_name="apiVersion")
    def api_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiVersion"))

    @api_version.setter
    def api_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b02a2f89903b368b106af426d3cc435e3d975c432cff251da50b0b1d547d870)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiVersion", value)

    @builtins.property
    @jsii.member(jsii_name="fieldPath")
    def field_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fieldPath"))

    @field_path.setter
    def field_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4472f2902d39d1ce999c9cc0c53647d71c23e629986ed004d6da83d768edf5f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fieldPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EnvEnvValueFromFieldRef]:
        return typing.cast(typing.Optional[EnvEnvValueFromFieldRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[EnvEnvValueFromFieldRef]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d6419a7911c3a1211c9847112afbe9686138b61fa9653a3b3d6a569c7cf8e19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EnvEnvValueFromOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.env.EnvEnvValueFromOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cd1597513043cc1d8a41f7a749e6e66a4b38f128ca5b9593efc809355bef6031)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putConfigMapKeyRef")
    def put_config_map_key_ref(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        optional: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param key: The key to select. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#key Env#key}
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#name Env#name}
        :param optional: Specify whether the ConfigMap or its key must be defined. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#optional Env#optional}
        '''
        value = EnvEnvValueFromConfigMapKeyRef(key=key, name=name, optional=optional)

        return typing.cast(None, jsii.invoke(self, "putConfigMapKeyRef", [value]))

    @jsii.member(jsii_name="putFieldRef")
    def put_field_ref(
        self,
        *,
        api_version: typing.Optional[builtins.str] = None,
        field_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param api_version: Version of the schema the FieldPath is written in terms of, defaults to "v1". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#api_version Env#api_version}
        :param field_path: Path of the field to select in the specified API version. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#field_path Env#field_path}
        '''
        value = EnvEnvValueFromFieldRef(api_version=api_version, field_path=field_path)

        return typing.cast(None, jsii.invoke(self, "putFieldRef", [value]))

    @jsii.member(jsii_name="putResourceFieldRef")
    def put_resource_field_ref(
        self,
        *,
        resource: builtins.str,
        container_name: typing.Optional[builtins.str] = None,
        divisor: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param resource: Resource to select. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#resource Env#resource}
        :param container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#container_name Env#container_name}.
        :param divisor: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#divisor Env#divisor}.
        '''
        value = EnvEnvValueFromResourceFieldRef(
            resource=resource, container_name=container_name, divisor=divisor
        )

        return typing.cast(None, jsii.invoke(self, "putResourceFieldRef", [value]))

    @jsii.member(jsii_name="putSecretKeyRef")
    def put_secret_key_ref(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        optional: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param key: The key of the secret to select from. Must be a valid secret key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#key Env#key}
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#name Env#name}
        :param optional: Specify whether the Secret or its key must be defined. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#optional Env#optional}
        '''
        value = EnvEnvValueFromSecretKeyRef(key=key, name=name, optional=optional)

        return typing.cast(None, jsii.invoke(self, "putSecretKeyRef", [value]))

    @jsii.member(jsii_name="resetConfigMapKeyRef")
    def reset_config_map_key_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigMapKeyRef", []))

    @jsii.member(jsii_name="resetFieldRef")
    def reset_field_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFieldRef", []))

    @jsii.member(jsii_name="resetResourceFieldRef")
    def reset_resource_field_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceFieldRef", []))

    @jsii.member(jsii_name="resetSecretKeyRef")
    def reset_secret_key_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretKeyRef", []))

    @builtins.property
    @jsii.member(jsii_name="configMapKeyRef")
    def config_map_key_ref(self) -> EnvEnvValueFromConfigMapKeyRefOutputReference:
        return typing.cast(EnvEnvValueFromConfigMapKeyRefOutputReference, jsii.get(self, "configMapKeyRef"))

    @builtins.property
    @jsii.member(jsii_name="fieldRef")
    def field_ref(self) -> EnvEnvValueFromFieldRefOutputReference:
        return typing.cast(EnvEnvValueFromFieldRefOutputReference, jsii.get(self, "fieldRef"))

    @builtins.property
    @jsii.member(jsii_name="resourceFieldRef")
    def resource_field_ref(self) -> "EnvEnvValueFromResourceFieldRefOutputReference":
        return typing.cast("EnvEnvValueFromResourceFieldRefOutputReference", jsii.get(self, "resourceFieldRef"))

    @builtins.property
    @jsii.member(jsii_name="secretKeyRef")
    def secret_key_ref(self) -> "EnvEnvValueFromSecretKeyRefOutputReference":
        return typing.cast("EnvEnvValueFromSecretKeyRefOutputReference", jsii.get(self, "secretKeyRef"))

    @builtins.property
    @jsii.member(jsii_name="configMapKeyRefInput")
    def config_map_key_ref_input(
        self,
    ) -> typing.Optional[EnvEnvValueFromConfigMapKeyRef]:
        return typing.cast(typing.Optional[EnvEnvValueFromConfigMapKeyRef], jsii.get(self, "configMapKeyRefInput"))

    @builtins.property
    @jsii.member(jsii_name="fieldRefInput")
    def field_ref_input(self) -> typing.Optional[EnvEnvValueFromFieldRef]:
        return typing.cast(typing.Optional[EnvEnvValueFromFieldRef], jsii.get(self, "fieldRefInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceFieldRefInput")
    def resource_field_ref_input(
        self,
    ) -> typing.Optional["EnvEnvValueFromResourceFieldRef"]:
        return typing.cast(typing.Optional["EnvEnvValueFromResourceFieldRef"], jsii.get(self, "resourceFieldRefInput"))

    @builtins.property
    @jsii.member(jsii_name="secretKeyRefInput")
    def secret_key_ref_input(self) -> typing.Optional["EnvEnvValueFromSecretKeyRef"]:
        return typing.cast(typing.Optional["EnvEnvValueFromSecretKeyRef"], jsii.get(self, "secretKeyRefInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EnvEnvValueFrom]:
        return typing.cast(typing.Optional[EnvEnvValueFrom], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[EnvEnvValueFrom]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d72c312d623018f7a50c45699f9c1834225da0b5ef18fc8fb86426421dd92f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.env.EnvEnvValueFromResourceFieldRef",
    jsii_struct_bases=[],
    name_mapping={
        "resource": "resource",
        "container_name": "containerName",
        "divisor": "divisor",
    },
)
class EnvEnvValueFromResourceFieldRef:
    def __init__(
        self,
        *,
        resource: builtins.str,
        container_name: typing.Optional[builtins.str] = None,
        divisor: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param resource: Resource to select. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#resource Env#resource}
        :param container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#container_name Env#container_name}.
        :param divisor: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#divisor Env#divisor}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__015ef5725459082319e92735609992e52b92eff598c57531f5806c8fd7df785f)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
            check_type(argname="argument container_name", value=container_name, expected_type=type_hints["container_name"])
            check_type(argname="argument divisor", value=divisor, expected_type=type_hints["divisor"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource": resource,
        }
        if container_name is not None:
            self._values["container_name"] = container_name
        if divisor is not None:
            self._values["divisor"] = divisor

    @builtins.property
    def resource(self) -> builtins.str:
        '''Resource to select.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#resource Env#resource}
        '''
        result = self._values.get("resource")
        assert result is not None, "Required property 'resource' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#container_name Env#container_name}.'''
        result = self._values.get("container_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def divisor(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#divisor Env#divisor}.'''
        result = self._values.get("divisor")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvEnvValueFromResourceFieldRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EnvEnvValueFromResourceFieldRefOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.env.EnvEnvValueFromResourceFieldRefOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__181037af62e8eed77128cbb31a69fe40a2f9d88fb2eaa292ecc002335f8d6e64)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetContainerName")
    def reset_container_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerName", []))

    @jsii.member(jsii_name="resetDivisor")
    def reset_divisor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDivisor", []))

    @builtins.property
    @jsii.member(jsii_name="containerNameInput")
    def container_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="divisorInput")
    def divisor_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "divisorInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceInput")
    def resource_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceInput"))

    @builtins.property
    @jsii.member(jsii_name="containerName")
    def container_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerName"))

    @container_name.setter
    def container_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c36974f000b3e306006ae5ab2b5ee62029834942cc2afca6947e437b47f6976)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerName", value)

    @builtins.property
    @jsii.member(jsii_name="divisor")
    def divisor(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "divisor"))

    @divisor.setter
    def divisor(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__429e8762968257ca4f8675a369b42f1e96266ef4bc6ca582b1cfb276db29c5ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "divisor", value)

    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resource"))

    @resource.setter
    def resource(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2de7dccecae4443af60e107513942a9e31383bb067038c9aecad27257f494428)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resource", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EnvEnvValueFromResourceFieldRef]:
        return typing.cast(typing.Optional[EnvEnvValueFromResourceFieldRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EnvEnvValueFromResourceFieldRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64ddee3edce785e0ff2926a46a9fa672fa314546476ed88bc3c32f2b8d66be10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.env.EnvEnvValueFromSecretKeyRef",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "name": "name", "optional": "optional"},
)
class EnvEnvValueFromSecretKeyRef:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        optional: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param key: The key of the secret to select from. Must be a valid secret key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#key Env#key}
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#name Env#name}
        :param optional: Specify whether the Secret or its key must be defined. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#optional Env#optional}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4fa7ce199550cb5f0774829377da44e3dad2880e001bad71c2e7027320eaa54)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument optional", value=optional, expected_type=type_hints["optional"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if name is not None:
            self._values["name"] = name
        if optional is not None:
            self._values["optional"] = optional

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The key of the secret to select from. Must be a valid secret key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#key Env#key}
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#name Env#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def optional(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Specify whether the Secret or its key must be defined.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#optional Env#optional}
        '''
        result = self._values.get("optional")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvEnvValueFromSecretKeyRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EnvEnvValueFromSecretKeyRefOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.env.EnvEnvValueFromSecretKeyRefOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2247c1e2931e84aaca4f367c8019c6f1eb2b6a67e728b61019284b79eeffc399)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetOptional")
    def reset_optional(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptional", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="optionalInput")
    def optional_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "optionalInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25a9b9f6d2402e1325518a0fb5d03621512fbb1bd5ca9880972010b232744d4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__501dff2ecc59aa7eb38e5c59bdf6a949144572a53bf647425ae24e9e7b632833)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="optional")
    def optional(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "optional"))

    @optional.setter
    def optional(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d4e70b1de0ffe703650d52d72050972d42e1dec58c6d84dfb58a8142d686713)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "optional", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EnvEnvValueFromSecretKeyRef]:
        return typing.cast(typing.Optional[EnvEnvValueFromSecretKeyRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EnvEnvValueFromSecretKeyRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__215481065880d5c93d41ffc0ed4713eb40a909d94eb5e38977f5ae3e04ecf6a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="kubernetes.env.EnvMetadata",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class EnvMetadata:
    def __init__(
        self,
        *,
        name: builtins.str,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: The name of the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#name Env#name}
        :param namespace: The namespace of the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#namespace Env#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87a08262ad9484983b5838752b26d88ae41482bc29b9c1b257ca9b0e9b1f9ffe)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#name Env#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The namespace of the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/env#namespace Env#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvMetadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EnvMetadataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="kubernetes.env.EnvMetadataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__66cddd8d1182a49bf921945b468f0650189f7a59cbfcafb6bd47953856700a96)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc7a80cbc8555c66d0a1dcc026555b4901396f7b543fce123c7d40a3fcf6a6d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82240b5cfe0f0f20d6bc0d864db65972ee843c3bfdef26b5a60c66ef8ceef6e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EnvMetadata]:
        return typing.cast(typing.Optional[EnvMetadata], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[EnvMetadata]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc80ef8542ce6c6c54657cc28fa16c5c4f921f418bd6ad7ab45749d877d57bbe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Env",
    "EnvConfig",
    "EnvEnv",
    "EnvEnvList",
    "EnvEnvOutputReference",
    "EnvEnvValueFrom",
    "EnvEnvValueFromConfigMapKeyRef",
    "EnvEnvValueFromConfigMapKeyRefOutputReference",
    "EnvEnvValueFromFieldRef",
    "EnvEnvValueFromFieldRefOutputReference",
    "EnvEnvValueFromOutputReference",
    "EnvEnvValueFromResourceFieldRef",
    "EnvEnvValueFromResourceFieldRefOutputReference",
    "EnvEnvValueFromSecretKeyRef",
    "EnvEnvValueFromSecretKeyRefOutputReference",
    "EnvMetadata",
    "EnvMetadataOutputReference",
]

publication.publish()

def _typecheckingstub__ce7545d8f24c4b017b6f970baae0b57e90ae6c124a3b8f0bd59d315f4b315f44(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    api_version: builtins.str,
    container: builtins.str,
    env: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EnvEnv, typing.Dict[builtins.str, typing.Any]]]],
    kind: builtins.str,
    metadata: typing.Union[EnvMetadata, typing.Dict[builtins.str, typing.Any]],
    field_manager: typing.Optional[builtins.str] = None,
    force: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__75687acb7d8866542f1b6c84918eb8b069ec69e3be42a0fd8b4754578f9be0f0(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EnvEnv, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c9ed293334491d47d68175cbaae71838f362d706f2125d0edea5f4f5de88d97(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38c1091906adeac526e5ad5d8868fa6f6a802b9e802cdc72fdb87817cb1bc0ec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__752b83c2428182bb9c80c6333ad6aa4bfad5d34ae0c3c67b4eb2c8f18630f588(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f140ed1a0d0e98d8f977d469137aa28e0c2494a6e3438f03314e9e747abe778(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f5024797c7c42d65398fba021c1cb6dd3347f522e5afd8dc340232341b56bb3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea66c4c2e601539d2f31f2abb84049a1e04ccb3b6fba878f474deabea23ec0af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6aae9169754d123c6cd4902542bea4e43b56e0e6be01f33ad859f6eec1b2101(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    api_version: builtins.str,
    container: builtins.str,
    env: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[EnvEnv, typing.Dict[builtins.str, typing.Any]]]],
    kind: builtins.str,
    metadata: typing.Union[EnvMetadata, typing.Dict[builtins.str, typing.Any]],
    field_manager: typing.Optional[builtins.str] = None,
    force: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3c6b670cdd73a448f7a4a01fabf729e3149367b23b75c58d459596026700e3b(
    *,
    name: builtins.str,
    value: typing.Optional[builtins.str] = None,
    value_from: typing.Optional[typing.Union[EnvEnvValueFrom, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87dd6cc2ab6c8196dd9de1129f086c01608404a3693b392c9775dd0fbbb99683(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dee89c5f56dc3941e41a8431bc861c1562f052c55afcf50585b5f83bc631e2a6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f74f93371108126757fd6162d595b2e08923f2bf341d27b333bffbae5794863(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5185b6deb4a96c358217ad081c4bb4244510b770887b401cbecfd3348f1d814b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b97fa42b53d5d0d0dd9f8afaaa4333b30adb9e635e50900f50368e43674e7517(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b16dbc9e0c0119cbc0e80669ea3c26d7de26a22517257442b8c9bdd6bc41abb1(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[EnvEnv]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb6069da1bd0f2256846600c88f1daff78ec991523da46e41e4e027b1df4609d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e899c5039be1a8a398b11fd1186f63f3a516db63b76b0bcb8d83b53b3e88ae3d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc17b10847d3b08f809b7df19e5963034c68bc08f8d15cf18d5a0e8f34e92b0b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bfc6499eb904362fedf1603c8a1e095e4bb6f133d2cdc8799bcbe20a9a62f77(
    value: typing.Optional[typing.Union[EnvEnv, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50f57e7d1adca1fa304f1573f48d48d3562fab2d18c2c9355844961b590514a6(
    *,
    config_map_key_ref: typing.Optional[typing.Union[EnvEnvValueFromConfigMapKeyRef, typing.Dict[builtins.str, typing.Any]]] = None,
    field_ref: typing.Optional[typing.Union[EnvEnvValueFromFieldRef, typing.Dict[builtins.str, typing.Any]]] = None,
    resource_field_ref: typing.Optional[typing.Union[EnvEnvValueFromResourceFieldRef, typing.Dict[builtins.str, typing.Any]]] = None,
    secret_key_ref: typing.Optional[typing.Union[EnvEnvValueFromSecretKeyRef, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__890d6ddc23e73b60bc8d0c71c794fd21f80952f7263239b2ff663089280cdaee(
    *,
    key: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    optional: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9a0a3fa09c0119a62ee48047728c021d38a538a1db603a310a520d3e2e4cf3f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c540038fb4242cd44bcab7a5b938f9c7a1f6413534895b7413173750d13ed5a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4963d6a5c3ac1564e02629e5ae163012eccccb496947355cdb4f75b6ae264a4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d77d4d96aa938a7f1f0c5f5cbd3049a265b7ab7a7fbf54e8f65cda15332cc5f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__090374ba7608b120585290f05fcd76e9ee225b0e51dc6fd20897bdf73eb427f7(
    value: typing.Optional[EnvEnvValueFromConfigMapKeyRef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efb030d56d5b6a5fc159b705729561c69e7a6b3178712259351a9e1a4025de90(
    *,
    api_version: typing.Optional[builtins.str] = None,
    field_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__071b171aa12c086cd955e6b1ed20ab9023bdb2ea1f36d4a8c78e4992e87e422f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b02a2f89903b368b106af426d3cc435e3d975c432cff251da50b0b1d547d870(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4472f2902d39d1ce999c9cc0c53647d71c23e629986ed004d6da83d768edf5f7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d6419a7911c3a1211c9847112afbe9686138b61fa9653a3b3d6a569c7cf8e19(
    value: typing.Optional[EnvEnvValueFromFieldRef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd1597513043cc1d8a41f7a749e6e66a4b38f128ca5b9593efc809355bef6031(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d72c312d623018f7a50c45699f9c1834225da0b5ef18fc8fb86426421dd92f7(
    value: typing.Optional[EnvEnvValueFrom],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__015ef5725459082319e92735609992e52b92eff598c57531f5806c8fd7df785f(
    *,
    resource: builtins.str,
    container_name: typing.Optional[builtins.str] = None,
    divisor: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__181037af62e8eed77128cbb31a69fe40a2f9d88fb2eaa292ecc002335f8d6e64(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c36974f000b3e306006ae5ab2b5ee62029834942cc2afca6947e437b47f6976(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__429e8762968257ca4f8675a369b42f1e96266ef4bc6ca582b1cfb276db29c5ea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2de7dccecae4443af60e107513942a9e31383bb067038c9aecad27257f494428(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64ddee3edce785e0ff2926a46a9fa672fa314546476ed88bc3c32f2b8d66be10(
    value: typing.Optional[EnvEnvValueFromResourceFieldRef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4fa7ce199550cb5f0774829377da44e3dad2880e001bad71c2e7027320eaa54(
    *,
    key: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    optional: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2247c1e2931e84aaca4f367c8019c6f1eb2b6a67e728b61019284b79eeffc399(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25a9b9f6d2402e1325518a0fb5d03621512fbb1bd5ca9880972010b232744d4d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__501dff2ecc59aa7eb38e5c59bdf6a949144572a53bf647425ae24e9e7b632833(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d4e70b1de0ffe703650d52d72050972d42e1dec58c6d84dfb58a8142d686713(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__215481065880d5c93d41ffc0ed4713eb40a909d94eb5e38977f5ae3e04ecf6a8(
    value: typing.Optional[EnvEnvValueFromSecretKeyRef],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87a08262ad9484983b5838752b26d88ae41482bc29b9c1b257ca9b0e9b1f9ffe(
    *,
    name: builtins.str,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66cddd8d1182a49bf921945b468f0650189f7a59cbfcafb6bd47953856700a96(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc7a80cbc8555c66d0a1dcc026555b4901396f7b543fce123c7d40a3fcf6a6d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82240b5cfe0f0f20d6bc0d864db65972ee843c3bfdef26b5a60c66ef8ceef6e5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc80ef8542ce6c6c54657cc28fa16c5c4f921f418bd6ad7ab45749d877d57bbe(
    value: typing.Optional[EnvMetadata],
) -> None:
    """Type checking stubs"""
    pass
