'''
# `aws_appmesh_virtual_node`

Refer to the Terraform Registory for docs: [`aws_appmesh_virtual_node`](https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node).
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


class AppmeshVirtualNode(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNode",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node aws_appmesh_virtual_node}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        mesh_name: builtins.str,
        name: builtins.str,
        spec: typing.Union["AppmeshVirtualNodeSpec", typing.Dict[builtins.str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        mesh_owner: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node aws_appmesh_virtual_node} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param mesh_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#mesh_name AppmeshVirtualNode#mesh_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#name AppmeshVirtualNode#name}.
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#spec AppmeshVirtualNode#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#id AppmeshVirtualNode#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mesh_owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#mesh_owner AppmeshVirtualNode#mesh_owner}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tags AppmeshVirtualNode#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tags_all AppmeshVirtualNode#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e24237a553776645ea72adc13270809d60e0872a07381576676bc1719cb52a8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AppmeshVirtualNodeConfig(
            mesh_name=mesh_name,
            name=name,
            spec=spec,
            id=id,
            mesh_owner=mesh_owner,
            tags=tags,
            tags_all=tags_all,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putSpec")
    def put_spec(
        self,
        *,
        backend: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AppmeshVirtualNodeSpecBackend", typing.Dict[builtins.str, typing.Any]]]]] = None,
        backend_defaults: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendDefaults", typing.Dict[builtins.str, typing.Any]]] = None,
        listener: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListener", typing.Dict[builtins.str, typing.Any]]] = None,
        logging: typing.Optional[typing.Union["AppmeshVirtualNodeSpecLogging", typing.Dict[builtins.str, typing.Any]]] = None,
        service_discovery: typing.Optional[typing.Union["AppmeshVirtualNodeSpecServiceDiscovery", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param backend: backend block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#backend AppmeshVirtualNode#backend}
        :param backend_defaults: backend_defaults block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#backend_defaults AppmeshVirtualNode#backend_defaults}
        :param listener: listener block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#listener AppmeshVirtualNode#listener}
        :param logging: logging block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#logging AppmeshVirtualNode#logging}
        :param service_discovery: service_discovery block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#service_discovery AppmeshVirtualNode#service_discovery}
        '''
        value = AppmeshVirtualNodeSpec(
            backend=backend,
            backend_defaults=backend_defaults,
            listener=listener,
            logging=logging,
            service_discovery=service_discovery,
        )

        return typing.cast(None, jsii.invoke(self, "putSpec", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMeshOwner")
    def reset_mesh_owner(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMeshOwner", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="createdDate")
    def created_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdDate"))

    @builtins.property
    @jsii.member(jsii_name="lastUpdatedDate")
    def last_updated_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastUpdatedDate"))

    @builtins.property
    @jsii.member(jsii_name="resourceOwner")
    def resource_owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceOwner"))

    @builtins.property
    @jsii.member(jsii_name="spec")
    def spec(self) -> "AppmeshVirtualNodeSpecOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecOutputReference", jsii.get(self, "spec"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="meshNameInput")
    def mesh_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "meshNameInput"))

    @builtins.property
    @jsii.member(jsii_name="meshOwnerInput")
    def mesh_owner_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "meshOwnerInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="specInput")
    def spec_input(self) -> typing.Optional["AppmeshVirtualNodeSpec"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpec"], jsii.get(self, "specInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsAllInput")
    def tags_all_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsAllInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__376443ffe264ee236e64919d013f6874ea9094294555962fbf5fd074838ddd1e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="meshName")
    def mesh_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "meshName"))

    @mesh_name.setter
    def mesh_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6806ef4dc04f4e79067780a6c797ac8cb5c29716fb9a73d4c3fa42d4f7894653)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "meshName", value)

    @builtins.property
    @jsii.member(jsii_name="meshOwner")
    def mesh_owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "meshOwner"))

    @mesh_owner.setter
    def mesh_owner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ba99551f9b79a7888c2fa275b9b34ca78291236597395428b41ffec128fd0a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "meshOwner", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec1b639d3a9b539b9ba914703902cf27fc4c47acdf324334105d1785380069a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70ea632be195dfc7499986a558e8b28525dbbd2c82bf723ab0bae8a2108506ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33831d2403ac911e94f304ca72aee107eb2918bcc2a299e7510786551366a58e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "mesh_name": "meshName",
        "name": "name",
        "spec": "spec",
        "id": "id",
        "mesh_owner": "meshOwner",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class AppmeshVirtualNodeConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        mesh_name: builtins.str,
        name: builtins.str,
        spec: typing.Union["AppmeshVirtualNodeSpec", typing.Dict[builtins.str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        mesh_owner: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param mesh_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#mesh_name AppmeshVirtualNode#mesh_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#name AppmeshVirtualNode#name}.
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#spec AppmeshVirtualNode#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#id AppmeshVirtualNode#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mesh_owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#mesh_owner AppmeshVirtualNode#mesh_owner}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tags AppmeshVirtualNode#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tags_all AppmeshVirtualNode#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(spec, dict):
            spec = AppmeshVirtualNodeSpec(**spec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aaa32f1a0be60eb1136a27db23ada0b3cbd0d2dbb838034972f70afc99d61150)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument mesh_name", value=mesh_name, expected_type=type_hints["mesh_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument spec", value=spec, expected_type=type_hints["spec"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument mesh_owner", value=mesh_owner, expected_type=type_hints["mesh_owner"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "mesh_name": mesh_name,
            "name": name,
            "spec": spec,
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
        if mesh_owner is not None:
            self._values["mesh_owner"] = mesh_owner
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all

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
    def mesh_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#mesh_name AppmeshVirtualNode#mesh_name}.'''
        result = self._values.get("mesh_name")
        assert result is not None, "Required property 'mesh_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#name AppmeshVirtualNode#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def spec(self) -> "AppmeshVirtualNodeSpec":
        '''spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#spec AppmeshVirtualNode#spec}
        '''
        result = self._values.get("spec")
        assert result is not None, "Required property 'spec' is missing"
        return typing.cast("AppmeshVirtualNodeSpec", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#id AppmeshVirtualNode#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mesh_owner(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#mesh_owner AppmeshVirtualNode#mesh_owner}.'''
        result = self._values.get("mesh_owner")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tags AppmeshVirtualNode#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tags_all AppmeshVirtualNode#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpec",
    jsii_struct_bases=[],
    name_mapping={
        "backend": "backend",
        "backend_defaults": "backendDefaults",
        "listener": "listener",
        "logging": "logging",
        "service_discovery": "serviceDiscovery",
    },
)
class AppmeshVirtualNodeSpec:
    def __init__(
        self,
        *,
        backend: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AppmeshVirtualNodeSpecBackend", typing.Dict[builtins.str, typing.Any]]]]] = None,
        backend_defaults: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendDefaults", typing.Dict[builtins.str, typing.Any]]] = None,
        listener: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListener", typing.Dict[builtins.str, typing.Any]]] = None,
        logging: typing.Optional[typing.Union["AppmeshVirtualNodeSpecLogging", typing.Dict[builtins.str, typing.Any]]] = None,
        service_discovery: typing.Optional[typing.Union["AppmeshVirtualNodeSpecServiceDiscovery", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param backend: backend block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#backend AppmeshVirtualNode#backend}
        :param backend_defaults: backend_defaults block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#backend_defaults AppmeshVirtualNode#backend_defaults}
        :param listener: listener block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#listener AppmeshVirtualNode#listener}
        :param logging: logging block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#logging AppmeshVirtualNode#logging}
        :param service_discovery: service_discovery block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#service_discovery AppmeshVirtualNode#service_discovery}
        '''
        if isinstance(backend_defaults, dict):
            backend_defaults = AppmeshVirtualNodeSpecBackendDefaults(**backend_defaults)
        if isinstance(listener, dict):
            listener = AppmeshVirtualNodeSpecListener(**listener)
        if isinstance(logging, dict):
            logging = AppmeshVirtualNodeSpecLogging(**logging)
        if isinstance(service_discovery, dict):
            service_discovery = AppmeshVirtualNodeSpecServiceDiscovery(**service_discovery)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0dc2b69e385cd93c86e408ca3a2933148ddeafe0e099d15b8210685f3b2e32cf)
            check_type(argname="argument backend", value=backend, expected_type=type_hints["backend"])
            check_type(argname="argument backend_defaults", value=backend_defaults, expected_type=type_hints["backend_defaults"])
            check_type(argname="argument listener", value=listener, expected_type=type_hints["listener"])
            check_type(argname="argument logging", value=logging, expected_type=type_hints["logging"])
            check_type(argname="argument service_discovery", value=service_discovery, expected_type=type_hints["service_discovery"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if backend is not None:
            self._values["backend"] = backend
        if backend_defaults is not None:
            self._values["backend_defaults"] = backend_defaults
        if listener is not None:
            self._values["listener"] = listener
        if logging is not None:
            self._values["logging"] = logging
        if service_discovery is not None:
            self._values["service_discovery"] = service_discovery

    @builtins.property
    def backend(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppmeshVirtualNodeSpecBackend"]]]:
        '''backend block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#backend AppmeshVirtualNode#backend}
        '''
        result = self._values.get("backend")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppmeshVirtualNodeSpecBackend"]]], result)

    @builtins.property
    def backend_defaults(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendDefaults"]:
        '''backend_defaults block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#backend_defaults AppmeshVirtualNode#backend_defaults}
        '''
        result = self._values.get("backend_defaults")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendDefaults"], result)

    @builtins.property
    def listener(self) -> typing.Optional["AppmeshVirtualNodeSpecListener"]:
        '''listener block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#listener AppmeshVirtualNode#listener}
        '''
        result = self._values.get("listener")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListener"], result)

    @builtins.property
    def logging(self) -> typing.Optional["AppmeshVirtualNodeSpecLogging"]:
        '''logging block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#logging AppmeshVirtualNode#logging}
        '''
        result = self._values.get("logging")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecLogging"], result)

    @builtins.property
    def service_discovery(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecServiceDiscovery"]:
        '''service_discovery block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#service_discovery AppmeshVirtualNode#service_discovery}
        '''
        result = self._values.get("service_discovery")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecServiceDiscovery"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackend",
    jsii_struct_bases=[],
    name_mapping={"virtual_service": "virtualService"},
)
class AppmeshVirtualNodeSpecBackend:
    def __init__(
        self,
        *,
        virtual_service: typing.Union["AppmeshVirtualNodeSpecBackendVirtualService", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param virtual_service: virtual_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#virtual_service AppmeshVirtualNode#virtual_service}
        '''
        if isinstance(virtual_service, dict):
            virtual_service = AppmeshVirtualNodeSpecBackendVirtualService(**virtual_service)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b25e1fbddd114621cf42865a7dea5371f65e9711b9b96723cfde7e3e789b0dc)
            check_type(argname="argument virtual_service", value=virtual_service, expected_type=type_hints["virtual_service"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "virtual_service": virtual_service,
        }

    @builtins.property
    def virtual_service(self) -> "AppmeshVirtualNodeSpecBackendVirtualService":
        '''virtual_service block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#virtual_service AppmeshVirtualNode#virtual_service}
        '''
        result = self._values.get("virtual_service")
        assert result is not None, "Required property 'virtual_service' is missing"
        return typing.cast("AppmeshVirtualNodeSpecBackendVirtualService", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackend(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaults",
    jsii_struct_bases=[],
    name_mapping={"client_policy": "clientPolicy"},
)
class AppmeshVirtualNodeSpecBackendDefaults:
    def __init__(
        self,
        *,
        client_policy: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param client_policy: client_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#client_policy AppmeshVirtualNode#client_policy}
        '''
        if isinstance(client_policy, dict):
            client_policy = AppmeshVirtualNodeSpecBackendDefaultsClientPolicy(**client_policy)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c16cd438aefb8370cd84a3a6c207dad9f351f9b858adf0d0ed213ab300baf06e)
            check_type(argname="argument client_policy", value=client_policy, expected_type=type_hints["client_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if client_policy is not None:
            self._values["client_policy"] = client_policy

    @builtins.property
    def client_policy(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicy"]:
        '''client_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#client_policy AppmeshVirtualNode#client_policy}
        '''
        result = self._values.get("client_policy")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendDefaults(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicy",
    jsii_struct_bases=[],
    name_mapping={"tls": "tls"},
)
class AppmeshVirtualNodeSpecBackendDefaultsClientPolicy:
    def __init__(
        self,
        *,
        tls: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTls", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param tls: tls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tls AppmeshVirtualNode#tls}
        '''
        if isinstance(tls, dict):
            tls = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTls(**tls)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd7f54e0da78b8468c14e4ce9cc9162b5d5365a485132d23ead903c0b6bbf295)
            check_type(argname="argument tls", value=tls, expected_type=type_hints["tls"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def tls(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTls"]:
        '''tls block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tls AppmeshVirtualNode#tls}
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTls"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendDefaultsClientPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d93a7312abb2ba928e3ad4d0726630bda6deecef109e4c775aab7ab35c3dea42)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTls")
    def put_tls(
        self,
        *,
        validation: typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidation", typing.Dict[builtins.str, typing.Any]],
        certificate: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificate", typing.Dict[builtins.str, typing.Any]]] = None,
        enforce: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ports: typing.Optional[typing.Sequence[jsii.Number]] = None,
    ) -> None:
        '''
        :param validation: validation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#validation AppmeshVirtualNode#validation}
        :param certificate: certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate AppmeshVirtualNode#certificate}
        :param enforce: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#enforce AppmeshVirtualNode#enforce}.
        :param ports: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#ports AppmeshVirtualNode#ports}.
        '''
        value = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTls(
            validation=validation,
            certificate=certificate,
            enforce=enforce,
            ports=ports,
        )

        return typing.cast(None, jsii.invoke(self, "putTls", [value]))

    @jsii.member(jsii_name="resetTls")
    def reset_tls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTls", []))

    @builtins.property
    @jsii.member(jsii_name="tls")
    def tls(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsOutputReference", jsii.get(self, "tls"))

    @builtins.property
    @jsii.member(jsii_name="tlsInput")
    def tls_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTls"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTls"], jsii.get(self, "tlsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicy]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9ce08fee2f9a504cf4071f9999d9476a7eb9fd2e67db7ff5011e7cdeef92a84)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTls",
    jsii_struct_bases=[],
    name_mapping={
        "validation": "validation",
        "certificate": "certificate",
        "enforce": "enforce",
        "ports": "ports",
    },
)
class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTls:
    def __init__(
        self,
        *,
        validation: typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidation", typing.Dict[builtins.str, typing.Any]],
        certificate: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificate", typing.Dict[builtins.str, typing.Any]]] = None,
        enforce: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ports: typing.Optional[typing.Sequence[jsii.Number]] = None,
    ) -> None:
        '''
        :param validation: validation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#validation AppmeshVirtualNode#validation}
        :param certificate: certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate AppmeshVirtualNode#certificate}
        :param enforce: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#enforce AppmeshVirtualNode#enforce}.
        :param ports: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#ports AppmeshVirtualNode#ports}.
        '''
        if isinstance(validation, dict):
            validation = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidation(**validation)
        if isinstance(certificate, dict):
            certificate = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificate(**certificate)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__deca6c77f7cee02bedd7f9d3ecc002ea27b15e30c71a3febbcea5a2679b06e24)
            check_type(argname="argument validation", value=validation, expected_type=type_hints["validation"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument enforce", value=enforce, expected_type=type_hints["enforce"])
            check_type(argname="argument ports", value=ports, expected_type=type_hints["ports"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "validation": validation,
        }
        if certificate is not None:
            self._values["certificate"] = certificate
        if enforce is not None:
            self._values["enforce"] = enforce
        if ports is not None:
            self._values["ports"] = ports

    @builtins.property
    def validation(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidation":
        '''validation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#validation AppmeshVirtualNode#validation}
        '''
        result = self._values.get("validation")
        assert result is not None, "Required property 'validation' is missing"
        return typing.cast("AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidation", result)

    @builtins.property
    def certificate(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificate"]:
        '''certificate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate AppmeshVirtualNode#certificate}
        '''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificate"], result)

    @builtins.property
    def enforce(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#enforce AppmeshVirtualNode#enforce}.'''
        result = self._values.get("enforce")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def ports(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#ports AppmeshVirtualNode#ports}.'''
        result = self._values.get("ports")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificate",
    jsii_struct_bases=[],
    name_mapping={"file": "file", "sds": "sds"},
)
class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificate:
    def __init__(
        self,
        *,
        file: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFile", typing.Dict[builtins.str, typing.Any]]] = None,
        sds: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSds", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        :param sds: sds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#sds AppmeshVirtualNode#sds}
        '''
        if isinstance(file, dict):
            file = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFile(**file)
        if isinstance(sds, dict):
            sds = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSds(**sds)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__419c3ab657431f23b613be2e2273e10967b3235d9b3997e0a8c95cddbb78039a)
            check_type(argname="argument file", value=file, expected_type=type_hints["file"])
            check_type(argname="argument sds", value=sds, expected_type=type_hints["sds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if file is not None:
            self._values["file"] = file
        if sds is not None:
            self._values["sds"] = sds

    @builtins.property
    def file(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFile"]:
        '''file block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        '''
        result = self._values.get("file")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFile"], result)

    @builtins.property
    def sds(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSds"]:
        '''sds block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#sds AppmeshVirtualNode#sds}
        '''
        result = self._values.get("sds")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSds"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFile",
    jsii_struct_bases=[],
    name_mapping={
        "certificate_chain": "certificateChain",
        "private_key": "privateKey",
    },
)
class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFile:
    def __init__(
        self,
        *,
        certificate_chain: builtins.str,
        private_key: builtins.str,
    ) -> None:
        '''
        :param certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_chain AppmeshVirtualNode#certificate_chain}.
        :param private_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#private_key AppmeshVirtualNode#private_key}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__faff23421fdf0e85f47d120c8d40816e4461b387becd54ae41187fbfb41e3d58)
            check_type(argname="argument certificate_chain", value=certificate_chain, expected_type=type_hints["certificate_chain"])
            check_type(argname="argument private_key", value=private_key, expected_type=type_hints["private_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_chain": certificate_chain,
            "private_key": private_key,
        }

    @builtins.property
    def certificate_chain(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_chain AppmeshVirtualNode#certificate_chain}.'''
        result = self._values.get("certificate_chain")
        assert result is not None, "Required property 'certificate_chain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def private_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#private_key AppmeshVirtualNode#private_key}.'''
        result = self._values.get("private_key")
        assert result is not None, "Required property 'private_key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFileOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFileOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__12363b31c8277cc8109549641d0d87ef5b50a6f2e2e68f70306e25a5f43d8256)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="certificateChainInput")
    def certificate_chain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateChainInput"))

    @builtins.property
    @jsii.member(jsii_name="privateKeyInput")
    def private_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateChain")
    def certificate_chain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateChain"))

    @certificate_chain.setter
    def certificate_chain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0549beaeb3adcf3cf4ad3e9fe4d222739782b4c2fbcd9166ef55ecde99730d94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateChain", value)

    @builtins.property
    @jsii.member(jsii_name="privateKey")
    def private_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateKey"))

    @private_key.setter
    def private_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d24506bc29bf51f6e3795ff57fcc6dacbb9c9d7865e7ffadb2e9055a9a3a546)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFile]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFile],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df95dd04c55f9aa6b00003cad82b9232ae8132c8d87ff9d191698e03e0e902d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b8a9c256a6f9915865d5374be1bcae5776ca29a8d07529f216f1de6532f3f9df)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putFile")
    def put_file(
        self,
        *,
        certificate_chain: builtins.str,
        private_key: builtins.str,
    ) -> None:
        '''
        :param certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_chain AppmeshVirtualNode#certificate_chain}.
        :param private_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#private_key AppmeshVirtualNode#private_key}.
        '''
        value = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFile(
            certificate_chain=certificate_chain, private_key=private_key
        )

        return typing.cast(None, jsii.invoke(self, "putFile", [value]))

    @jsii.member(jsii_name="putSds")
    def put_sds(self, *, secret_name: builtins.str) -> None:
        '''
        :param secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#secret_name AppmeshVirtualNode#secret_name}.
        '''
        value = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSds(
            secret_name=secret_name
        )

        return typing.cast(None, jsii.invoke(self, "putSds", [value]))

    @jsii.member(jsii_name="resetFile")
    def reset_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFile", []))

    @jsii.member(jsii_name="resetSds")
    def reset_sds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSds", []))

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(
        self,
    ) -> AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFileOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFileOutputReference, jsii.get(self, "file"))

    @builtins.property
    @jsii.member(jsii_name="sds")
    def sds(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSdsOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSdsOutputReference", jsii.get(self, "sds"))

    @builtins.property
    @jsii.member(jsii_name="fileInput")
    def file_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFile]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFile], jsii.get(self, "fileInput"))

    @builtins.property
    @jsii.member(jsii_name="sdsInput")
    def sds_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSds"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSds"], jsii.get(self, "sdsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificate]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificate],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8f1ee0d7e8ea9ba1769439de6c73cc389e55e0cc75c5fb9b0de078325d3b3e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSds",
    jsii_struct_bases=[],
    name_mapping={"secret_name": "secretName"},
)
class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSds:
    def __init__(self, *, secret_name: builtins.str) -> None:
        '''
        :param secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#secret_name AppmeshVirtualNode#secret_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3e1448ba5d1c2efbd92983bd6e9d7e9f5715a5535ca04cd8b608f082e992f13)
            check_type(argname="argument secret_name", value=secret_name, expected_type=type_hints["secret_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "secret_name": secret_name,
        }

    @builtins.property
    def secret_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#secret_name AppmeshVirtualNode#secret_name}.'''
        result = self._values.get("secret_name")
        assert result is not None, "Required property 'secret_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSdsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSdsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__84ad6973eb46dcc3b3cb863975e33f3f1e9c1cf7b6296ca6c91f4c648d4972f4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="secretNameInput")
    def secret_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretNameInput"))

    @builtins.property
    @jsii.member(jsii_name="secretName")
    def secret_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretName"))

    @secret_name.setter
    def secret_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd0800bac838fd5f1bbe1a3cb48609dab2b9768ca00998e1c5295e0f2b6259f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSds]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSds], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSds],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28bb040a45e4ed08fbf0aa3242a49d59812384868f4c7c8d8d6a84ce20488e41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b70e774e436da4f5672b3f5d52596c36ace03276efbf48dcaad13fd30517cfab)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCertificate")
    def put_certificate(
        self,
        *,
        file: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFile, typing.Dict[builtins.str, typing.Any]]] = None,
        sds: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSds, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        :param sds: sds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#sds AppmeshVirtualNode#sds}
        '''
        value = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificate(
            file=file, sds=sds
        )

        return typing.cast(None, jsii.invoke(self, "putCertificate", [value]))

    @jsii.member(jsii_name="putValidation")
    def put_validation(
        self,
        *,
        trust: typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrust", typing.Dict[builtins.str, typing.Any]],
        subject_alternative_names: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param trust: trust block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#trust AppmeshVirtualNode#trust}
        :param subject_alternative_names: subject_alternative_names block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#subject_alternative_names AppmeshVirtualNode#subject_alternative_names}
        '''
        value = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidation(
            trust=trust, subject_alternative_names=subject_alternative_names
        )

        return typing.cast(None, jsii.invoke(self, "putValidation", [value]))

    @jsii.member(jsii_name="resetCertificate")
    def reset_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificate", []))

    @jsii.member(jsii_name="resetEnforce")
    def reset_enforce(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnforce", []))

    @jsii.member(jsii_name="resetPorts")
    def reset_ports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPorts", []))

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(
        self,
    ) -> AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateOutputReference, jsii.get(self, "certificate"))

    @builtins.property
    @jsii.member(jsii_name="validation")
    def validation(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationOutputReference", jsii.get(self, "validation"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificate]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificate], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="enforceInput")
    def enforce_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enforceInput"))

    @builtins.property
    @jsii.member(jsii_name="portsInput")
    def ports_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "portsInput"))

    @builtins.property
    @jsii.member(jsii_name="validationInput")
    def validation_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidation"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidation"], jsii.get(self, "validationInput"))

    @builtins.property
    @jsii.member(jsii_name="enforce")
    def enforce(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enforce"))

    @enforce.setter
    def enforce(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd563475c7d3fb279c4a30f9f1b419097db7ef50e6764dd6339525d7f593e4b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enforce", value)

    @builtins.property
    @jsii.member(jsii_name="ports")
    def ports(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "ports"))

    @ports.setter
    def ports(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c395233f9e749ee993984d5d4ca14997c9c0b334b2385586ab844db98df8ba1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ports", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTls]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTls], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTls],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23546870b4e33a5679fa187ae8a2354bc70df467c3433338daf9eb725c9cee27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidation",
    jsii_struct_bases=[],
    name_mapping={
        "trust": "trust",
        "subject_alternative_names": "subjectAlternativeNames",
    },
)
class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidation:
    def __init__(
        self,
        *,
        trust: typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrust", typing.Dict[builtins.str, typing.Any]],
        subject_alternative_names: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param trust: trust block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#trust AppmeshVirtualNode#trust}
        :param subject_alternative_names: subject_alternative_names block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#subject_alternative_names AppmeshVirtualNode#subject_alternative_names}
        '''
        if isinstance(trust, dict):
            trust = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrust(**trust)
        if isinstance(subject_alternative_names, dict):
            subject_alternative_names = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames(**subject_alternative_names)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__613cde633eb5a8f249557a8d39723b7ad38cedce41d082be6c074ff9dd6d49ea)
            check_type(argname="argument trust", value=trust, expected_type=type_hints["trust"])
            check_type(argname="argument subject_alternative_names", value=subject_alternative_names, expected_type=type_hints["subject_alternative_names"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "trust": trust,
        }
        if subject_alternative_names is not None:
            self._values["subject_alternative_names"] = subject_alternative_names

    @builtins.property
    def trust(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrust":
        '''trust block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#trust AppmeshVirtualNode#trust}
        '''
        result = self._values.get("trust")
        assert result is not None, "Required property 'trust' is missing"
        return typing.cast("AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrust", result)

    @builtins.property
    def subject_alternative_names(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames"]:
        '''subject_alternative_names block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#subject_alternative_names AppmeshVirtualNode#subject_alternative_names}
        '''
        result = self._values.get("subject_alternative_names")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__174152230f9fc68aed459448bf0e95b8a8876688fbc9c92bf213c65adc28570b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSubjectAlternativeNames")
    def put_subject_alternative_names(
        self,
        *,
        match: typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#match AppmeshVirtualNode#match}
        '''
        value = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames(
            match=match
        )

        return typing.cast(None, jsii.invoke(self, "putSubjectAlternativeNames", [value]))

    @jsii.member(jsii_name="putTrust")
    def put_trust(
        self,
        *,
        acm: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcm", typing.Dict[builtins.str, typing.Any]]] = None,
        file: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFile", typing.Dict[builtins.str, typing.Any]]] = None,
        sds: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSds", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param acm: acm block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#acm AppmeshVirtualNode#acm}
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        :param sds: sds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#sds AppmeshVirtualNode#sds}
        '''
        value = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrust(
            acm=acm, file=file, sds=sds
        )

        return typing.cast(None, jsii.invoke(self, "putTrust", [value]))

    @jsii.member(jsii_name="resetSubjectAlternativeNames")
    def reset_subject_alternative_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubjectAlternativeNames", []))

    @builtins.property
    @jsii.member(jsii_name="subjectAlternativeNames")
    def subject_alternative_names(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesOutputReference", jsii.get(self, "subjectAlternativeNames"))

    @builtins.property
    @jsii.member(jsii_name="trust")
    def trust(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustOutputReference", jsii.get(self, "trust"))

    @builtins.property
    @jsii.member(jsii_name="subjectAlternativeNamesInput")
    def subject_alternative_names_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames"], jsii.get(self, "subjectAlternativeNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="trustInput")
    def trust_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrust"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrust"], jsii.get(self, "trustInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidation]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6846e980204e2905d62acf2636a2c37cba894b19259fbf1b69bee7764470a042)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames",
    jsii_struct_bases=[],
    name_mapping={"match": "match"},
)
class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames:
    def __init__(
        self,
        *,
        match: typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#match AppmeshVirtualNode#match}
        '''
        if isinstance(match, dict):
            match = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch(**match)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__518ebaf25f9df5e7981cac53664ada8b22be42e02ecff70301555b800ec8b60d)
            check_type(argname="argument match", value=match, expected_type=type_hints["match"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "match": match,
        }

    @builtins.property
    def match(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch":
        '''match block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#match AppmeshVirtualNode#match}
        '''
        result = self._values.get("match")
        assert result is not None, "Required property 'match' is missing"
        return typing.cast("AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch",
    jsii_struct_bases=[],
    name_mapping={"exact": "exact"},
)
class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch:
    def __init__(self, *, exact: typing.Sequence[builtins.str]) -> None:
        '''
        :param exact: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#exact AppmeshVirtualNode#exact}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34ccd1cf0cfcbae2fe1fd4300a37d9c415298e6374cc06b49d83b5b7d8ddc570)
            check_type(argname="argument exact", value=exact, expected_type=type_hints["exact"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "exact": exact,
        }

    @builtins.property
    def exact(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#exact AppmeshVirtualNode#exact}.'''
        result = self._values.get("exact")
        assert result is not None, "Required property 'exact' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatchOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatchOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__16e62587caa1308c02b8d8b221ad7171666d54b04d917fc0b2d1510f82613d70)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="exactInput")
    def exact_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "exactInput"))

    @builtins.property
    @jsii.member(jsii_name="exact")
    def exact(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exact"))

    @exact.setter
    def exact(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__600d8b4ce868ec7961e6b603d9289dd9dc18cd5c10d72b65de5a334246da4769)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exact", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40c3d791f7209561b6f447985b4b87745f3be89b1674d449abc6cfa749999204)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0fe33ce30292d10e8e5e46d2155052fd0ebde4536c95bc9d42c0d5cc8cce559e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMatch")
    def put_match(self, *, exact: typing.Sequence[builtins.str]) -> None:
        '''
        :param exact: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#exact AppmeshVirtualNode#exact}.
        '''
        value = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch(
            exact=exact
        )

        return typing.cast(None, jsii.invoke(self, "putMatch", [value]))

    @builtins.property
    @jsii.member(jsii_name="match")
    def match(
        self,
    ) -> AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatchOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatchOutputReference, jsii.get(self, "match"))

    @builtins.property
    @jsii.member(jsii_name="matchInput")
    def match_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch], jsii.get(self, "matchInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7fca7e59c27d158ea9b12d45f12e7c043c3d226804534b470eeaf38a722f5a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrust",
    jsii_struct_bases=[],
    name_mapping={"acm": "acm", "file": "file", "sds": "sds"},
)
class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrust:
    def __init__(
        self,
        *,
        acm: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcm", typing.Dict[builtins.str, typing.Any]]] = None,
        file: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFile", typing.Dict[builtins.str, typing.Any]]] = None,
        sds: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSds", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param acm: acm block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#acm AppmeshVirtualNode#acm}
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        :param sds: sds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#sds AppmeshVirtualNode#sds}
        '''
        if isinstance(acm, dict):
            acm = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcm(**acm)
        if isinstance(file, dict):
            file = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFile(**file)
        if isinstance(sds, dict):
            sds = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSds(**sds)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e3b24ba41c33cf00127d58032757922c8d11b510bdede95fc319863349529ae)
            check_type(argname="argument acm", value=acm, expected_type=type_hints["acm"])
            check_type(argname="argument file", value=file, expected_type=type_hints["file"])
            check_type(argname="argument sds", value=sds, expected_type=type_hints["sds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if acm is not None:
            self._values["acm"] = acm
        if file is not None:
            self._values["file"] = file
        if sds is not None:
            self._values["sds"] = sds

    @builtins.property
    def acm(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcm"]:
        '''acm block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#acm AppmeshVirtualNode#acm}
        '''
        result = self._values.get("acm")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcm"], result)

    @builtins.property
    def file(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFile"]:
        '''file block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        '''
        result = self._values.get("file")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFile"], result)

    @builtins.property
    def sds(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSds"]:
        '''sds block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#sds AppmeshVirtualNode#sds}
        '''
        result = self._values.get("sds")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSds"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrust(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcm",
    jsii_struct_bases=[],
    name_mapping={"certificate_authority_arns": "certificateAuthorityArns"},
)
class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcm:
    def __init__(
        self,
        *,
        certificate_authority_arns: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param certificate_authority_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_authority_arns AppmeshVirtualNode#certificate_authority_arns}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c60c69ed0922d8239dd35ba1641e22042eba28503e064b0c379cdbc3a4bdfebf)
            check_type(argname="argument certificate_authority_arns", value=certificate_authority_arns, expected_type=type_hints["certificate_authority_arns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_authority_arns": certificate_authority_arns,
        }

    @builtins.property
    def certificate_authority_arns(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_authority_arns AppmeshVirtualNode#certificate_authority_arns}.'''
        result = self._values.get("certificate_authority_arns")
        assert result is not None, "Required property 'certificate_authority_arns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcmOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcmOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c8ca7fa96eaa5f0fbc3b9913df7de16fde28f4d8aac12cced02fcd46533ceac9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="certificateAuthorityArnsInput")
    def certificate_authority_arns_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "certificateAuthorityArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateAuthorityArns")
    def certificate_authority_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "certificateAuthorityArns"))

    @certificate_authority_arns.setter
    def certificate_authority_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19fba7f6a527d8b5ea37df27ecbf82eb6c082974b98b0bfedd0d3d83d171049d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateAuthorityArns", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcm]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcm], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcm],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02fbe62b2d61edc364b147cae73b9d119fa97a7d583d2ef37f82e28fbf938e37)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFile",
    jsii_struct_bases=[],
    name_mapping={"certificate_chain": "certificateChain"},
)
class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFile:
    def __init__(self, *, certificate_chain: builtins.str) -> None:
        '''
        :param certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_chain AppmeshVirtualNode#certificate_chain}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7cefa59c6b95e87089b5f65a41a1876e0bba83c4632551464d774c726975757)
            check_type(argname="argument certificate_chain", value=certificate_chain, expected_type=type_hints["certificate_chain"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_chain": certificate_chain,
        }

    @builtins.property
    def certificate_chain(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_chain AppmeshVirtualNode#certificate_chain}.'''
        result = self._values.get("certificate_chain")
        assert result is not None, "Required property 'certificate_chain' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFileOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFileOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6648b4b75c5c04522aec68e68ceff585c060bdb85cafb42cb0a2ee3cc268c2f2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="certificateChainInput")
    def certificate_chain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateChainInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateChain")
    def certificate_chain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateChain"))

    @certificate_chain.setter
    def certificate_chain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa884aa872279347f0a30692f57ba4c9bb45034ad51c9dbb06864490564f3f52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateChain", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFile]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFile],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71ccc5ca17337e0a8f5179a77834bb0c17ffc2a4194db3b9b2a109dec1f83c17)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fb5c24537072e80d796cdc3f607759434e7677c3e361cbd05da8d317f880301d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAcm")
    def put_acm(
        self,
        *,
        certificate_authority_arns: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param certificate_authority_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_authority_arns AppmeshVirtualNode#certificate_authority_arns}.
        '''
        value = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcm(
            certificate_authority_arns=certificate_authority_arns
        )

        return typing.cast(None, jsii.invoke(self, "putAcm", [value]))

    @jsii.member(jsii_name="putFile")
    def put_file(self, *, certificate_chain: builtins.str) -> None:
        '''
        :param certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_chain AppmeshVirtualNode#certificate_chain}.
        '''
        value = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFile(
            certificate_chain=certificate_chain
        )

        return typing.cast(None, jsii.invoke(self, "putFile", [value]))

    @jsii.member(jsii_name="putSds")
    def put_sds(self, *, secret_name: builtins.str) -> None:
        '''
        :param secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#secret_name AppmeshVirtualNode#secret_name}.
        '''
        value = AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSds(
            secret_name=secret_name
        )

        return typing.cast(None, jsii.invoke(self, "putSds", [value]))

    @jsii.member(jsii_name="resetAcm")
    def reset_acm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcm", []))

    @jsii.member(jsii_name="resetFile")
    def reset_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFile", []))

    @jsii.member(jsii_name="resetSds")
    def reset_sds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSds", []))

    @builtins.property
    @jsii.member(jsii_name="acm")
    def acm(
        self,
    ) -> AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcmOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcmOutputReference, jsii.get(self, "acm"))

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(
        self,
    ) -> AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFileOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFileOutputReference, jsii.get(self, "file"))

    @builtins.property
    @jsii.member(jsii_name="sds")
    def sds(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSdsOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSdsOutputReference", jsii.get(self, "sds"))

    @builtins.property
    @jsii.member(jsii_name="acmInput")
    def acm_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcm]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcm], jsii.get(self, "acmInput"))

    @builtins.property
    @jsii.member(jsii_name="fileInput")
    def file_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFile]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFile], jsii.get(self, "fileInput"))

    @builtins.property
    @jsii.member(jsii_name="sdsInput")
    def sds_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSds"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSds"], jsii.get(self, "sdsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrust]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrust], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrust],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79cd95db611e9526d83ee9871a9bd75bad1c90bde2cafb561c49f4b86328b39f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSds",
    jsii_struct_bases=[],
    name_mapping={"secret_name": "secretName"},
)
class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSds:
    def __init__(self, *, secret_name: builtins.str) -> None:
        '''
        :param secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#secret_name AppmeshVirtualNode#secret_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5854b6a615c1389bbecc2dd478a527adc20a95558cd3268040cdaafcb150a980)
            check_type(argname="argument secret_name", value=secret_name, expected_type=type_hints["secret_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "secret_name": secret_name,
        }

    @builtins.property
    def secret_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#secret_name AppmeshVirtualNode#secret_name}.'''
        result = self._values.get("secret_name")
        assert result is not None, "Required property 'secret_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSdsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSdsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d68938e4d1de511677a858be93a69e5fa555149d1041d3b2cae281d00ecc1858)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="secretNameInput")
    def secret_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretNameInput"))

    @builtins.property
    @jsii.member(jsii_name="secretName")
    def secret_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretName"))

    @secret_name.setter
    def secret_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e71eb7913b88ce88326cac465ccfce908f304328d49df1987f28ccf3f92e5384)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSds]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSds], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSds],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__767917bd766878a2d766783b2f335bce1108023fadca259959bf80d08819905d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecBackendDefaultsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendDefaultsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ef79d63939e4eb6f57b5cbbd67cf7b883b28a2f492aa93d3087799fcfee40901)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putClientPolicy")
    def put_client_policy(
        self,
        *,
        tls: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTls, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param tls: tls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tls AppmeshVirtualNode#tls}
        '''
        value = AppmeshVirtualNodeSpecBackendDefaultsClientPolicy(tls=tls)

        return typing.cast(None, jsii.invoke(self, "putClientPolicy", [value]))

    @jsii.member(jsii_name="resetClientPolicy")
    def reset_client_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientPolicy", []))

    @builtins.property
    @jsii.member(jsii_name="clientPolicy")
    def client_policy(
        self,
    ) -> AppmeshVirtualNodeSpecBackendDefaultsClientPolicyOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecBackendDefaultsClientPolicyOutputReference, jsii.get(self, "clientPolicy"))

    @builtins.property
    @jsii.member(jsii_name="clientPolicyInput")
    def client_policy_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicy]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicy], jsii.get(self, "clientPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaults]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaults], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaults],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2144cfb211392b61c264086dced35c1b1a8066eac16fbdd039992ad68ed33052)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecBackendList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d9f2066ab328553280b7a63f8af425180976e382ec99c27a1c938e0e1b3b1628)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AppmeshVirtualNodeSpecBackendOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a82af33b75e2a9b5c87a649930dcb20ec83b45e30eeb3ef8f6ef0845a1cf5d1)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppmeshVirtualNodeSpecBackendOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__daa393838b753c47e81c474cd39afd85d0e9ee1b7872478a480b75ae608ffc7a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d607315274d589417fe8da49cf6b6900e49765148f9cd62811fd896384f92630)
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
            type_hints = typing.get_type_hints(_typecheckingstub__346cc334ad63289ff1eb077d5d5badf656e71000ff3ac5122868974bedcf9208)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshVirtualNodeSpecBackend]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshVirtualNodeSpecBackend]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshVirtualNodeSpecBackend]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__017867a72c1182e964ebf4351ca1725c70d5831495007dbf03806bf0abad0404)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecBackendOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1e67cbd98da146eed95ae170ee9e13a5893887dedc3848c26768a27f15834a45)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putVirtualService")
    def put_virtual_service(
        self,
        *,
        virtual_service_name: builtins.str,
        client_policy: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param virtual_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#virtual_service_name AppmeshVirtualNode#virtual_service_name}.
        :param client_policy: client_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#client_policy AppmeshVirtualNode#client_policy}
        '''
        value = AppmeshVirtualNodeSpecBackendVirtualService(
            virtual_service_name=virtual_service_name, client_policy=client_policy
        )

        return typing.cast(None, jsii.invoke(self, "putVirtualService", [value]))

    @builtins.property
    @jsii.member(jsii_name="virtualService")
    def virtual_service(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendVirtualServiceOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecBackendVirtualServiceOutputReference", jsii.get(self, "virtualService"))

    @builtins.property
    @jsii.member(jsii_name="virtualServiceInput")
    def virtual_service_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendVirtualService"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendVirtualService"], jsii.get(self, "virtualServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackend, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackend, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackend, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0158ef87edc7de8257fd7ce2d85cbb450cdf58349b75e9b9c9e03bb5348a80d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualService",
    jsii_struct_bases=[],
    name_mapping={
        "virtual_service_name": "virtualServiceName",
        "client_policy": "clientPolicy",
    },
)
class AppmeshVirtualNodeSpecBackendVirtualService:
    def __init__(
        self,
        *,
        virtual_service_name: builtins.str,
        client_policy: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param virtual_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#virtual_service_name AppmeshVirtualNode#virtual_service_name}.
        :param client_policy: client_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#client_policy AppmeshVirtualNode#client_policy}
        '''
        if isinstance(client_policy, dict):
            client_policy = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicy(**client_policy)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b6feff43f72e0e59badcc959d1cf720fcd97572cf2096df6cd1cd05fa5b4217)
            check_type(argname="argument virtual_service_name", value=virtual_service_name, expected_type=type_hints["virtual_service_name"])
            check_type(argname="argument client_policy", value=client_policy, expected_type=type_hints["client_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "virtual_service_name": virtual_service_name,
        }
        if client_policy is not None:
            self._values["client_policy"] = client_policy

    @builtins.property
    def virtual_service_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#virtual_service_name AppmeshVirtualNode#virtual_service_name}.'''
        result = self._values.get("virtual_service_name")
        assert result is not None, "Required property 'virtual_service_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_policy(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicy"]:
        '''client_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#client_policy AppmeshVirtualNode#client_policy}
        '''
        result = self._values.get("client_policy")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendVirtualService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicy",
    jsii_struct_bases=[],
    name_mapping={"tls": "tls"},
)
class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicy:
    def __init__(
        self,
        *,
        tls: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTls", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param tls: tls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tls AppmeshVirtualNode#tls}
        '''
        if isinstance(tls, dict):
            tls = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTls(**tls)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea585ffeafcbf8e2c4af5c3f94d411dece1877b8746c708b13027701bd608682)
            check_type(argname="argument tls", value=tls, expected_type=type_hints["tls"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def tls(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTls"]:
        '''tls block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tls AppmeshVirtualNode#tls}
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTls"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__92e8bd21c7a2958169937172140fc79407550a50d8ac29fcf3fc23a6c422fc9f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTls")
    def put_tls(
        self,
        *,
        validation: typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidation", typing.Dict[builtins.str, typing.Any]],
        certificate: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificate", typing.Dict[builtins.str, typing.Any]]] = None,
        enforce: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ports: typing.Optional[typing.Sequence[jsii.Number]] = None,
    ) -> None:
        '''
        :param validation: validation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#validation AppmeshVirtualNode#validation}
        :param certificate: certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate AppmeshVirtualNode#certificate}
        :param enforce: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#enforce AppmeshVirtualNode#enforce}.
        :param ports: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#ports AppmeshVirtualNode#ports}.
        '''
        value = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTls(
            validation=validation,
            certificate=certificate,
            enforce=enforce,
            ports=ports,
        )

        return typing.cast(None, jsii.invoke(self, "putTls", [value]))

    @jsii.member(jsii_name="resetTls")
    def reset_tls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTls", []))

    @builtins.property
    @jsii.member(jsii_name="tls")
    def tls(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsOutputReference", jsii.get(self, "tls"))

    @builtins.property
    @jsii.member(jsii_name="tlsInput")
    def tls_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTls"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTls"], jsii.get(self, "tlsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicy]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__778f370594515921ea6756b08cae694cfa1eec7ffa82037587c6dbbaa4ccd686)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTls",
    jsii_struct_bases=[],
    name_mapping={
        "validation": "validation",
        "certificate": "certificate",
        "enforce": "enforce",
        "ports": "ports",
    },
)
class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTls:
    def __init__(
        self,
        *,
        validation: typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidation", typing.Dict[builtins.str, typing.Any]],
        certificate: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificate", typing.Dict[builtins.str, typing.Any]]] = None,
        enforce: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ports: typing.Optional[typing.Sequence[jsii.Number]] = None,
    ) -> None:
        '''
        :param validation: validation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#validation AppmeshVirtualNode#validation}
        :param certificate: certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate AppmeshVirtualNode#certificate}
        :param enforce: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#enforce AppmeshVirtualNode#enforce}.
        :param ports: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#ports AppmeshVirtualNode#ports}.
        '''
        if isinstance(validation, dict):
            validation = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidation(**validation)
        if isinstance(certificate, dict):
            certificate = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificate(**certificate)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a65807754e12d6c89b12b41161a9d472c0066632959fd74145ea2473f0aae338)
            check_type(argname="argument validation", value=validation, expected_type=type_hints["validation"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument enforce", value=enforce, expected_type=type_hints["enforce"])
            check_type(argname="argument ports", value=ports, expected_type=type_hints["ports"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "validation": validation,
        }
        if certificate is not None:
            self._values["certificate"] = certificate
        if enforce is not None:
            self._values["enforce"] = enforce
        if ports is not None:
            self._values["ports"] = ports

    @builtins.property
    def validation(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidation":
        '''validation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#validation AppmeshVirtualNode#validation}
        '''
        result = self._values.get("validation")
        assert result is not None, "Required property 'validation' is missing"
        return typing.cast("AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidation", result)

    @builtins.property
    def certificate(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificate"]:
        '''certificate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate AppmeshVirtualNode#certificate}
        '''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificate"], result)

    @builtins.property
    def enforce(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#enforce AppmeshVirtualNode#enforce}.'''
        result = self._values.get("enforce")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def ports(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#ports AppmeshVirtualNode#ports}.'''
        result = self._values.get("ports")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificate",
    jsii_struct_bases=[],
    name_mapping={"file": "file", "sds": "sds"},
)
class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificate:
    def __init__(
        self,
        *,
        file: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFile", typing.Dict[builtins.str, typing.Any]]] = None,
        sds: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSds", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        :param sds: sds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#sds AppmeshVirtualNode#sds}
        '''
        if isinstance(file, dict):
            file = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFile(**file)
        if isinstance(sds, dict):
            sds = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSds(**sds)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2abc0adde22e41fdadda507f12df096693412e834d316c9c913f9056a293d712)
            check_type(argname="argument file", value=file, expected_type=type_hints["file"])
            check_type(argname="argument sds", value=sds, expected_type=type_hints["sds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if file is not None:
            self._values["file"] = file
        if sds is not None:
            self._values["sds"] = sds

    @builtins.property
    def file(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFile"]:
        '''file block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        '''
        result = self._values.get("file")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFile"], result)

    @builtins.property
    def sds(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSds"]:
        '''sds block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#sds AppmeshVirtualNode#sds}
        '''
        result = self._values.get("sds")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSds"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFile",
    jsii_struct_bases=[],
    name_mapping={
        "certificate_chain": "certificateChain",
        "private_key": "privateKey",
    },
)
class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFile:
    def __init__(
        self,
        *,
        certificate_chain: builtins.str,
        private_key: builtins.str,
    ) -> None:
        '''
        :param certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_chain AppmeshVirtualNode#certificate_chain}.
        :param private_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#private_key AppmeshVirtualNode#private_key}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4169ca82be30c92f7504ca32a0a06060b3528ff0539acad8ad8518f8249002ca)
            check_type(argname="argument certificate_chain", value=certificate_chain, expected_type=type_hints["certificate_chain"])
            check_type(argname="argument private_key", value=private_key, expected_type=type_hints["private_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_chain": certificate_chain,
            "private_key": private_key,
        }

    @builtins.property
    def certificate_chain(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_chain AppmeshVirtualNode#certificate_chain}.'''
        result = self._values.get("certificate_chain")
        assert result is not None, "Required property 'certificate_chain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def private_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#private_key AppmeshVirtualNode#private_key}.'''
        result = self._values.get("private_key")
        assert result is not None, "Required property 'private_key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFileOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFileOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__eaae8263b66002fdf67ed6bf67a1061ea1627b34119438e453494eceb3e44579)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="certificateChainInput")
    def certificate_chain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateChainInput"))

    @builtins.property
    @jsii.member(jsii_name="privateKeyInput")
    def private_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateChain")
    def certificate_chain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateChain"))

    @certificate_chain.setter
    def certificate_chain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f26f0a55111342cb281d39239d601b5af42cd2afb8dd6ece64f6638efc9f0a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateChain", value)

    @builtins.property
    @jsii.member(jsii_name="privateKey")
    def private_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateKey"))

    @private_key.setter
    def private_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c1b206abe7b755e0a0a370fe54686b214ebc4213c5c18a38904cb97bdcd90a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFile]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFile],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d91c6159d5c531d29c7afc85c5783c7db5e3fe631131535f7f7e85ca7af8bd9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4e11ceaa6493757d5219b228815029b41203838cacf8884e32245ff7a6f7afb9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putFile")
    def put_file(
        self,
        *,
        certificate_chain: builtins.str,
        private_key: builtins.str,
    ) -> None:
        '''
        :param certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_chain AppmeshVirtualNode#certificate_chain}.
        :param private_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#private_key AppmeshVirtualNode#private_key}.
        '''
        value = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFile(
            certificate_chain=certificate_chain, private_key=private_key
        )

        return typing.cast(None, jsii.invoke(self, "putFile", [value]))

    @jsii.member(jsii_name="putSds")
    def put_sds(self, *, secret_name: builtins.str) -> None:
        '''
        :param secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#secret_name AppmeshVirtualNode#secret_name}.
        '''
        value = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSds(
            secret_name=secret_name
        )

        return typing.cast(None, jsii.invoke(self, "putSds", [value]))

    @jsii.member(jsii_name="resetFile")
    def reset_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFile", []))

    @jsii.member(jsii_name="resetSds")
    def reset_sds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSds", []))

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(
        self,
    ) -> AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFileOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFileOutputReference, jsii.get(self, "file"))

    @builtins.property
    @jsii.member(jsii_name="sds")
    def sds(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSdsOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSdsOutputReference", jsii.get(self, "sds"))

    @builtins.property
    @jsii.member(jsii_name="fileInput")
    def file_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFile]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFile], jsii.get(self, "fileInput"))

    @builtins.property
    @jsii.member(jsii_name="sdsInput")
    def sds_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSds"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSds"], jsii.get(self, "sdsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificate]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificate],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78c76eef627a1c9691ff55885110fdd08b93482e197b48a5cf08027c3787e59a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSds",
    jsii_struct_bases=[],
    name_mapping={"secret_name": "secretName"},
)
class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSds:
    def __init__(self, *, secret_name: builtins.str) -> None:
        '''
        :param secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#secret_name AppmeshVirtualNode#secret_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7da6ac89676d351e9c212f46fea9ee84c71f9853dea96a9f9fd57b149218490f)
            check_type(argname="argument secret_name", value=secret_name, expected_type=type_hints["secret_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "secret_name": secret_name,
        }

    @builtins.property
    def secret_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#secret_name AppmeshVirtualNode#secret_name}.'''
        result = self._values.get("secret_name")
        assert result is not None, "Required property 'secret_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSdsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSdsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1177ea3c6178e23e64407d9737bbd19c033b8177e08852a8041e44681793906a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="secretNameInput")
    def secret_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretNameInput"))

    @builtins.property
    @jsii.member(jsii_name="secretName")
    def secret_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretName"))

    @secret_name.setter
    def secret_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ffd35944a6a4b1a0a68aa1d372c90cc0cb4da77e3b4d5521952d98001f123f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSds]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSds], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSds],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8f0b825e23d1992d4a5fd244d857cd4d89d25f0d20c7ad37f9a795157c4c7b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3747eeae074d89f8c1541463225e9fbe0762857c3f57c6a8a1f48505e9fdb33d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCertificate")
    def put_certificate(
        self,
        *,
        file: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFile, typing.Dict[builtins.str, typing.Any]]] = None,
        sds: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSds, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        :param sds: sds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#sds AppmeshVirtualNode#sds}
        '''
        value = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificate(
            file=file, sds=sds
        )

        return typing.cast(None, jsii.invoke(self, "putCertificate", [value]))

    @jsii.member(jsii_name="putValidation")
    def put_validation(
        self,
        *,
        trust: typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrust", typing.Dict[builtins.str, typing.Any]],
        subject_alternative_names: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNames", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param trust: trust block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#trust AppmeshVirtualNode#trust}
        :param subject_alternative_names: subject_alternative_names block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#subject_alternative_names AppmeshVirtualNode#subject_alternative_names}
        '''
        value = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidation(
            trust=trust, subject_alternative_names=subject_alternative_names
        )

        return typing.cast(None, jsii.invoke(self, "putValidation", [value]))

    @jsii.member(jsii_name="resetCertificate")
    def reset_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificate", []))

    @jsii.member(jsii_name="resetEnforce")
    def reset_enforce(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnforce", []))

    @jsii.member(jsii_name="resetPorts")
    def reset_ports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPorts", []))

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(
        self,
    ) -> AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateOutputReference, jsii.get(self, "certificate"))

    @builtins.property
    @jsii.member(jsii_name="validation")
    def validation(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationOutputReference", jsii.get(self, "validation"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificate]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificate], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="enforceInput")
    def enforce_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enforceInput"))

    @builtins.property
    @jsii.member(jsii_name="portsInput")
    def ports_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "portsInput"))

    @builtins.property
    @jsii.member(jsii_name="validationInput")
    def validation_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidation"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidation"], jsii.get(self, "validationInput"))

    @builtins.property
    @jsii.member(jsii_name="enforce")
    def enforce(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enforce"))

    @enforce.setter
    def enforce(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9972cb8f1779a692c7fb24feb9f6cb65f25a0ad93927b2d34e5a85b0b15412a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enforce", value)

    @builtins.property
    @jsii.member(jsii_name="ports")
    def ports(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "ports"))

    @ports.setter
    def ports(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71873f4554c9c2fb69bcd1b6a862997c4b166e7d7b64795d2c8c4e5dd676e3fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ports", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTls]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTls], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTls],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8fd65a0313b7d5196528838724970350ebadc696571702838367e7be2c359c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidation",
    jsii_struct_bases=[],
    name_mapping={
        "trust": "trust",
        "subject_alternative_names": "subjectAlternativeNames",
    },
)
class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidation:
    def __init__(
        self,
        *,
        trust: typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrust", typing.Dict[builtins.str, typing.Any]],
        subject_alternative_names: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNames", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param trust: trust block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#trust AppmeshVirtualNode#trust}
        :param subject_alternative_names: subject_alternative_names block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#subject_alternative_names AppmeshVirtualNode#subject_alternative_names}
        '''
        if isinstance(trust, dict):
            trust = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrust(**trust)
        if isinstance(subject_alternative_names, dict):
            subject_alternative_names = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNames(**subject_alternative_names)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__329fc992e79335380e1db2b6db2623f69135fff8eb604ba4a78f04e33bdd7425)
            check_type(argname="argument trust", value=trust, expected_type=type_hints["trust"])
            check_type(argname="argument subject_alternative_names", value=subject_alternative_names, expected_type=type_hints["subject_alternative_names"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "trust": trust,
        }
        if subject_alternative_names is not None:
            self._values["subject_alternative_names"] = subject_alternative_names

    @builtins.property
    def trust(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrust":
        '''trust block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#trust AppmeshVirtualNode#trust}
        '''
        result = self._values.get("trust")
        assert result is not None, "Required property 'trust' is missing"
        return typing.cast("AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrust", result)

    @builtins.property
    def subject_alternative_names(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNames"]:
        '''subject_alternative_names block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#subject_alternative_names AppmeshVirtualNode#subject_alternative_names}
        '''
        result = self._values.get("subject_alternative_names")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNames"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1e57b17ee50b339508ae480775006645bb7f4f152b51c0f6d8a1f85f73c88506)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSubjectAlternativeNames")
    def put_subject_alternative_names(
        self,
        *,
        match: typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatch", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#match AppmeshVirtualNode#match}
        '''
        value = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNames(
            match=match
        )

        return typing.cast(None, jsii.invoke(self, "putSubjectAlternativeNames", [value]))

    @jsii.member(jsii_name="putTrust")
    def put_trust(
        self,
        *,
        acm: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcm", typing.Dict[builtins.str, typing.Any]]] = None,
        file: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFile", typing.Dict[builtins.str, typing.Any]]] = None,
        sds: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSds", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param acm: acm block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#acm AppmeshVirtualNode#acm}
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        :param sds: sds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#sds AppmeshVirtualNode#sds}
        '''
        value = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrust(
            acm=acm, file=file, sds=sds
        )

        return typing.cast(None, jsii.invoke(self, "putTrust", [value]))

    @jsii.member(jsii_name="resetSubjectAlternativeNames")
    def reset_subject_alternative_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubjectAlternativeNames", []))

    @builtins.property
    @jsii.member(jsii_name="subjectAlternativeNames")
    def subject_alternative_names(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesOutputReference", jsii.get(self, "subjectAlternativeNames"))

    @builtins.property
    @jsii.member(jsii_name="trust")
    def trust(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustOutputReference", jsii.get(self, "trust"))

    @builtins.property
    @jsii.member(jsii_name="subjectAlternativeNamesInput")
    def subject_alternative_names_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNames"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNames"], jsii.get(self, "subjectAlternativeNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="trustInput")
    def trust_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrust"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrust"], jsii.get(self, "trustInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidation]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7db07fb841028e2fd04f975676d090c9537b594559c0890ba970b2b3fd16ab08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNames",
    jsii_struct_bases=[],
    name_mapping={"match": "match"},
)
class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNames:
    def __init__(
        self,
        *,
        match: typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatch", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#match AppmeshVirtualNode#match}
        '''
        if isinstance(match, dict):
            match = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatch(**match)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8ca11af5f31817aa0913eb96d6ba622bb1b3292c4029ec26656195227774cda)
            check_type(argname="argument match", value=match, expected_type=type_hints["match"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "match": match,
        }

    @builtins.property
    def match(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatch":
        '''match block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#match AppmeshVirtualNode#match}
        '''
        result = self._values.get("match")
        assert result is not None, "Required property 'match' is missing"
        return typing.cast("AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatch", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNames(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatch",
    jsii_struct_bases=[],
    name_mapping={"exact": "exact"},
)
class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatch:
    def __init__(self, *, exact: typing.Sequence[builtins.str]) -> None:
        '''
        :param exact: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#exact AppmeshVirtualNode#exact}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e53005a96b93f4c60f1edf62c7cc7d3f55b82d78b36912a377588ce29a3468df)
            check_type(argname="argument exact", value=exact, expected_type=type_hints["exact"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "exact": exact,
        }

    @builtins.property
    def exact(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#exact AppmeshVirtualNode#exact}.'''
        result = self._values.get("exact")
        assert result is not None, "Required property 'exact' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatchOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatchOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__056e1f9daad1e67d727a3d882cb860f92fa1fb544db78b5885eb497aea494ab9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="exactInput")
    def exact_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "exactInput"))

    @builtins.property
    @jsii.member(jsii_name="exact")
    def exact(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exact"))

    @exact.setter
    def exact(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1602616e04febc4ecda072dad2661dab25b6e4ad2a31be5bd266562ad750e2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exact", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatch]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatch],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64592cf3f232dd82576326dd3ceb640b8847131d5cc96428ca12ba73b0253bc2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__618fe04e56d4c892d8f3a69e80464fd1173b26241f8151453a622a5647d7bc58)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMatch")
    def put_match(self, *, exact: typing.Sequence[builtins.str]) -> None:
        '''
        :param exact: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#exact AppmeshVirtualNode#exact}.
        '''
        value = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatch(
            exact=exact
        )

        return typing.cast(None, jsii.invoke(self, "putMatch", [value]))

    @builtins.property
    @jsii.member(jsii_name="match")
    def match(
        self,
    ) -> AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatchOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatchOutputReference, jsii.get(self, "match"))

    @builtins.property
    @jsii.member(jsii_name="matchInput")
    def match_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatch]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatch], jsii.get(self, "matchInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNames]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNames], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNames],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4314046e85c755271482938fb562325c4ff840d98b779810f66475fc66e3505e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrust",
    jsii_struct_bases=[],
    name_mapping={"acm": "acm", "file": "file", "sds": "sds"},
)
class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrust:
    def __init__(
        self,
        *,
        acm: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcm", typing.Dict[builtins.str, typing.Any]]] = None,
        file: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFile", typing.Dict[builtins.str, typing.Any]]] = None,
        sds: typing.Optional[typing.Union["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSds", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param acm: acm block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#acm AppmeshVirtualNode#acm}
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        :param sds: sds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#sds AppmeshVirtualNode#sds}
        '''
        if isinstance(acm, dict):
            acm = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcm(**acm)
        if isinstance(file, dict):
            file = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFile(**file)
        if isinstance(sds, dict):
            sds = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSds(**sds)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad656554e842ee963076aa14d39bcb00ec3bee7bf9cd71373417dfac005208cf)
            check_type(argname="argument acm", value=acm, expected_type=type_hints["acm"])
            check_type(argname="argument file", value=file, expected_type=type_hints["file"])
            check_type(argname="argument sds", value=sds, expected_type=type_hints["sds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if acm is not None:
            self._values["acm"] = acm
        if file is not None:
            self._values["file"] = file
        if sds is not None:
            self._values["sds"] = sds

    @builtins.property
    def acm(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcm"]:
        '''acm block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#acm AppmeshVirtualNode#acm}
        '''
        result = self._values.get("acm")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcm"], result)

    @builtins.property
    def file(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFile"]:
        '''file block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        '''
        result = self._values.get("file")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFile"], result)

    @builtins.property
    def sds(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSds"]:
        '''sds block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#sds AppmeshVirtualNode#sds}
        '''
        result = self._values.get("sds")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSds"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrust(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcm",
    jsii_struct_bases=[],
    name_mapping={"certificate_authority_arns": "certificateAuthorityArns"},
)
class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcm:
    def __init__(
        self,
        *,
        certificate_authority_arns: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param certificate_authority_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_authority_arns AppmeshVirtualNode#certificate_authority_arns}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fad90b8a4e5f0974b537f3383373c8ef1f51c5d7ed7af1c26d4110b70f4f92b)
            check_type(argname="argument certificate_authority_arns", value=certificate_authority_arns, expected_type=type_hints["certificate_authority_arns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_authority_arns": certificate_authority_arns,
        }

    @builtins.property
    def certificate_authority_arns(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_authority_arns AppmeshVirtualNode#certificate_authority_arns}.'''
        result = self._values.get("certificate_authority_arns")
        assert result is not None, "Required property 'certificate_authority_arns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcmOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcmOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__59e01f33702693b31b70c22b44dd9c91d86094a3df87771f18bf2f94736f1fac)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="certificateAuthorityArnsInput")
    def certificate_authority_arns_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "certificateAuthorityArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateAuthorityArns")
    def certificate_authority_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "certificateAuthorityArns"))

    @certificate_authority_arns.setter
    def certificate_authority_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23f541ef640a474644535fb567fad202044f02fed18a2721587a030bfec400dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateAuthorityArns", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcm]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcm], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcm],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__211a30659db4dfe4789e91be3586db4881d298a7624b711edfcc3cd8823058f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFile",
    jsii_struct_bases=[],
    name_mapping={"certificate_chain": "certificateChain"},
)
class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFile:
    def __init__(self, *, certificate_chain: builtins.str) -> None:
        '''
        :param certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_chain AppmeshVirtualNode#certificate_chain}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6474310f3473fa93f607582a7b4fbc0ed9dec0e4a6553061f48aa0d27624d70)
            check_type(argname="argument certificate_chain", value=certificate_chain, expected_type=type_hints["certificate_chain"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_chain": certificate_chain,
        }

    @builtins.property
    def certificate_chain(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_chain AppmeshVirtualNode#certificate_chain}.'''
        result = self._values.get("certificate_chain")
        assert result is not None, "Required property 'certificate_chain' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFileOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFileOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4619ac1b9c6ee608caa9a4b3b9e28e0ab4a298f769dd397a11cff52dcd8eb829)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="certificateChainInput")
    def certificate_chain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateChainInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateChain")
    def certificate_chain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateChain"))

    @certificate_chain.setter
    def certificate_chain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d2edc13affe54bae3d71b71e121c58fa4d85244ce206cbbe7cb9ad22df7fd22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateChain", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFile]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFile],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c94f943018aa2f20a125f804ab45010efcce73c0287ba5263a9fb6f9e4292605)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5b776974142fd50e9610fe7b20a6e29a3ab5a526c6365e716c4965c40c1b0307)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAcm")
    def put_acm(
        self,
        *,
        certificate_authority_arns: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param certificate_authority_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_authority_arns AppmeshVirtualNode#certificate_authority_arns}.
        '''
        value = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcm(
            certificate_authority_arns=certificate_authority_arns
        )

        return typing.cast(None, jsii.invoke(self, "putAcm", [value]))

    @jsii.member(jsii_name="putFile")
    def put_file(self, *, certificate_chain: builtins.str) -> None:
        '''
        :param certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_chain AppmeshVirtualNode#certificate_chain}.
        '''
        value = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFile(
            certificate_chain=certificate_chain
        )

        return typing.cast(None, jsii.invoke(self, "putFile", [value]))

    @jsii.member(jsii_name="putSds")
    def put_sds(self, *, secret_name: builtins.str) -> None:
        '''
        :param secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#secret_name AppmeshVirtualNode#secret_name}.
        '''
        value = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSds(
            secret_name=secret_name
        )

        return typing.cast(None, jsii.invoke(self, "putSds", [value]))

    @jsii.member(jsii_name="resetAcm")
    def reset_acm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcm", []))

    @jsii.member(jsii_name="resetFile")
    def reset_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFile", []))

    @jsii.member(jsii_name="resetSds")
    def reset_sds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSds", []))

    @builtins.property
    @jsii.member(jsii_name="acm")
    def acm(
        self,
    ) -> AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcmOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcmOutputReference, jsii.get(self, "acm"))

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(
        self,
    ) -> AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFileOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFileOutputReference, jsii.get(self, "file"))

    @builtins.property
    @jsii.member(jsii_name="sds")
    def sds(
        self,
    ) -> "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSdsOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSdsOutputReference", jsii.get(self, "sds"))

    @builtins.property
    @jsii.member(jsii_name="acmInput")
    def acm_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcm]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcm], jsii.get(self, "acmInput"))

    @builtins.property
    @jsii.member(jsii_name="fileInput")
    def file_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFile]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFile], jsii.get(self, "fileInput"))

    @builtins.property
    @jsii.member(jsii_name="sdsInput")
    def sds_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSds"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSds"], jsii.get(self, "sdsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrust]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrust], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrust],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__280119688cd60f43831428e7c3699f6d8c7cf5396e867fb859a36dc3f56fb90b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSds",
    jsii_struct_bases=[],
    name_mapping={"secret_name": "secretName"},
)
class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSds:
    def __init__(self, *, secret_name: builtins.str) -> None:
        '''
        :param secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#secret_name AppmeshVirtualNode#secret_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be40365ee314fd0c2b1a2868b58801b9a18852e42d0e7a30d047608d5a9896af)
            check_type(argname="argument secret_name", value=secret_name, expected_type=type_hints["secret_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "secret_name": secret_name,
        }

    @builtins.property
    def secret_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#secret_name AppmeshVirtualNode#secret_name}.'''
        result = self._values.get("secret_name")
        assert result is not None, "Required property 'secret_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSdsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSdsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a870b7ed058da9f3174f04317fb6c492a52f5176393e00ee794789fc2be1e57e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="secretNameInput")
    def secret_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretNameInput"))

    @builtins.property
    @jsii.member(jsii_name="secretName")
    def secret_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretName"))

    @secret_name.setter
    def secret_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0510dcd63d253f3dcbb77c35b02f4afaa7feb2a828921c12e2a730216b6e6855)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSds]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSds], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSds],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dccc964a08ed7720f24f408576aee1aa966750879725330ea857a57813990c63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecBackendVirtualServiceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecBackendVirtualServiceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c628ffb2945e31f753831c69312575c8086d696709c672ae974e7376585747d8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putClientPolicy")
    def put_client_policy(
        self,
        *,
        tls: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTls, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param tls: tls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tls AppmeshVirtualNode#tls}
        '''
        value = AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicy(tls=tls)

        return typing.cast(None, jsii.invoke(self, "putClientPolicy", [value]))

    @jsii.member(jsii_name="resetClientPolicy")
    def reset_client_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientPolicy", []))

    @builtins.property
    @jsii.member(jsii_name="clientPolicy")
    def client_policy(
        self,
    ) -> AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyOutputReference, jsii.get(self, "clientPolicy"))

    @builtins.property
    @jsii.member(jsii_name="clientPolicyInput")
    def client_policy_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicy]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicy], jsii.get(self, "clientPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualServiceNameInput")
    def virtual_service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualServiceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualServiceName")
    def virtual_service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualServiceName"))

    @virtual_service_name.setter
    def virtual_service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c564deb28dbb3a750b711d9a74ab90730b229c8b714989e36aed0c18f3fdaf82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualServiceName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendVirtualService]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendVirtualService], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualService],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__183a98ecdf50c1b3586cbcc115925575d4bba17a563aa9607b4a707698a96d4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListener",
    jsii_struct_bases=[],
    name_mapping={
        "port_mapping": "portMapping",
        "connection_pool": "connectionPool",
        "health_check": "healthCheck",
        "outlier_detection": "outlierDetection",
        "timeout": "timeout",
        "tls": "tls",
    },
)
class AppmeshVirtualNodeSpecListener:
    def __init__(
        self,
        *,
        port_mapping: typing.Union["AppmeshVirtualNodeSpecListenerPortMapping", typing.Dict[builtins.str, typing.Any]],
        connection_pool: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerConnectionPool", typing.Dict[builtins.str, typing.Any]]] = None,
        health_check: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerHealthCheck", typing.Dict[builtins.str, typing.Any]]] = None,
        outlier_detection: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerOutlierDetection", typing.Dict[builtins.str, typing.Any]]] = None,
        timeout: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTimeout", typing.Dict[builtins.str, typing.Any]]] = None,
        tls: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTls", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param port_mapping: port_mapping block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#port_mapping AppmeshVirtualNode#port_mapping}
        :param connection_pool: connection_pool block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#connection_pool AppmeshVirtualNode#connection_pool}
        :param health_check: health_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#health_check AppmeshVirtualNode#health_check}
        :param outlier_detection: outlier_detection block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#outlier_detection AppmeshVirtualNode#outlier_detection}
        :param timeout: timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#timeout AppmeshVirtualNode#timeout}
        :param tls: tls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tls AppmeshVirtualNode#tls}
        '''
        if isinstance(port_mapping, dict):
            port_mapping = AppmeshVirtualNodeSpecListenerPortMapping(**port_mapping)
        if isinstance(connection_pool, dict):
            connection_pool = AppmeshVirtualNodeSpecListenerConnectionPool(**connection_pool)
        if isinstance(health_check, dict):
            health_check = AppmeshVirtualNodeSpecListenerHealthCheck(**health_check)
        if isinstance(outlier_detection, dict):
            outlier_detection = AppmeshVirtualNodeSpecListenerOutlierDetection(**outlier_detection)
        if isinstance(timeout, dict):
            timeout = AppmeshVirtualNodeSpecListenerTimeout(**timeout)
        if isinstance(tls, dict):
            tls = AppmeshVirtualNodeSpecListenerTls(**tls)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__299232a8b99ecf3ac75cd0db65816aca2b7e775bc63449a5247a2eedaa954f69)
            check_type(argname="argument port_mapping", value=port_mapping, expected_type=type_hints["port_mapping"])
            check_type(argname="argument connection_pool", value=connection_pool, expected_type=type_hints["connection_pool"])
            check_type(argname="argument health_check", value=health_check, expected_type=type_hints["health_check"])
            check_type(argname="argument outlier_detection", value=outlier_detection, expected_type=type_hints["outlier_detection"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument tls", value=tls, expected_type=type_hints["tls"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "port_mapping": port_mapping,
        }
        if connection_pool is not None:
            self._values["connection_pool"] = connection_pool
        if health_check is not None:
            self._values["health_check"] = health_check
        if outlier_detection is not None:
            self._values["outlier_detection"] = outlier_detection
        if timeout is not None:
            self._values["timeout"] = timeout
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def port_mapping(self) -> "AppmeshVirtualNodeSpecListenerPortMapping":
        '''port_mapping block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#port_mapping AppmeshVirtualNode#port_mapping}
        '''
        result = self._values.get("port_mapping")
        assert result is not None, "Required property 'port_mapping' is missing"
        return typing.cast("AppmeshVirtualNodeSpecListenerPortMapping", result)

    @builtins.property
    def connection_pool(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerConnectionPool"]:
        '''connection_pool block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#connection_pool AppmeshVirtualNode#connection_pool}
        '''
        result = self._values.get("connection_pool")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerConnectionPool"], result)

    @builtins.property
    def health_check(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerHealthCheck"]:
        '''health_check block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#health_check AppmeshVirtualNode#health_check}
        '''
        result = self._values.get("health_check")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerHealthCheck"], result)

    @builtins.property
    def outlier_detection(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerOutlierDetection"]:
        '''outlier_detection block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#outlier_detection AppmeshVirtualNode#outlier_detection}
        '''
        result = self._values.get("outlier_detection")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerOutlierDetection"], result)

    @builtins.property
    def timeout(self) -> typing.Optional["AppmeshVirtualNodeSpecListenerTimeout"]:
        '''timeout block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#timeout AppmeshVirtualNode#timeout}
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTimeout"], result)

    @builtins.property
    def tls(self) -> typing.Optional["AppmeshVirtualNodeSpecListenerTls"]:
        '''tls block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tls AppmeshVirtualNode#tls}
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTls"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListener(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerConnectionPool",
    jsii_struct_bases=[],
    name_mapping={"grpc": "grpc", "http": "http", "http2": "http2", "tcp": "tcp"},
)
class AppmeshVirtualNodeSpecListenerConnectionPool:
    def __init__(
        self,
        *,
        grpc: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerConnectionPoolGrpc", typing.Dict[builtins.str, typing.Any]]] = None,
        http: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerConnectionPoolHttp", typing.Dict[builtins.str, typing.Any]]] = None,
        http2: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerConnectionPoolHttp2", typing.Dict[builtins.str, typing.Any]]] = None,
        tcp: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerConnectionPoolTcp", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param grpc: grpc block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#grpc AppmeshVirtualNode#grpc}
        :param http: http block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#http AppmeshVirtualNode#http}
        :param http2: http2 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#http2 AppmeshVirtualNode#http2}
        :param tcp: tcp block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tcp AppmeshVirtualNode#tcp}
        '''
        if isinstance(grpc, dict):
            grpc = AppmeshVirtualNodeSpecListenerConnectionPoolGrpc(**grpc)
        if isinstance(http, dict):
            http = AppmeshVirtualNodeSpecListenerConnectionPoolHttp(**http)
        if isinstance(http2, dict):
            http2 = AppmeshVirtualNodeSpecListenerConnectionPoolHttp2(**http2)
        if isinstance(tcp, dict):
            tcp = AppmeshVirtualNodeSpecListenerConnectionPoolTcp(**tcp)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0911161d7ee89b0bb78441f34d900302b2b7c284c85cdd3786d3137bb8e4688)
            check_type(argname="argument grpc", value=grpc, expected_type=type_hints["grpc"])
            check_type(argname="argument http", value=http, expected_type=type_hints["http"])
            check_type(argname="argument http2", value=http2, expected_type=type_hints["http2"])
            check_type(argname="argument tcp", value=tcp, expected_type=type_hints["tcp"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if grpc is not None:
            self._values["grpc"] = grpc
        if http is not None:
            self._values["http"] = http
        if http2 is not None:
            self._values["http2"] = http2
        if tcp is not None:
            self._values["tcp"] = tcp

    @builtins.property
    def grpc(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerConnectionPoolGrpc"]:
        '''grpc block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#grpc AppmeshVirtualNode#grpc}
        '''
        result = self._values.get("grpc")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerConnectionPoolGrpc"], result)

    @builtins.property
    def http(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerConnectionPoolHttp"]:
        '''http block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#http AppmeshVirtualNode#http}
        '''
        result = self._values.get("http")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerConnectionPoolHttp"], result)

    @builtins.property
    def http2(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerConnectionPoolHttp2"]:
        '''http2 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#http2 AppmeshVirtualNode#http2}
        '''
        result = self._values.get("http2")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerConnectionPoolHttp2"], result)

    @builtins.property
    def tcp(self) -> typing.Optional["AppmeshVirtualNodeSpecListenerConnectionPoolTcp"]:
        '''tcp block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tcp AppmeshVirtualNode#tcp}
        '''
        result = self._values.get("tcp")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerConnectionPoolTcp"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerConnectionPool(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerConnectionPoolGrpc",
    jsii_struct_bases=[],
    name_mapping={"max_requests": "maxRequests"},
)
class AppmeshVirtualNodeSpecListenerConnectionPoolGrpc:
    def __init__(self, *, max_requests: jsii.Number) -> None:
        '''
        :param max_requests: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_requests AppmeshVirtualNode#max_requests}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6970d73a083c7f6fb6ab9bc89becfe9efb14478c9e60c0967a04bfbe465d427)
            check_type(argname="argument max_requests", value=max_requests, expected_type=type_hints["max_requests"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "max_requests": max_requests,
        }

    @builtins.property
    def max_requests(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_requests AppmeshVirtualNode#max_requests}.'''
        result = self._values.get("max_requests")
        assert result is not None, "Required property 'max_requests' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerConnectionPoolGrpc(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerConnectionPoolGrpcOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerConnectionPoolGrpcOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__eed41e82b0e970a5daab6391ad6939c372daafc0458ef3a5597004112644204f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="maxRequestsInput")
    def max_requests_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxRequestsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxRequests")
    def max_requests(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxRequests"))

    @max_requests.setter
    def max_requests(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5023e96e749022e74e965663c013aeef541a178995f95dd3e63c84023507cfb7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxRequests", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolGrpc]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolGrpc], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolGrpc],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__121dc3f4e80061fd757e41a7befd18f9baa9a3467182f1b0ed30ccb15db26bb0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerConnectionPoolHttp",
    jsii_struct_bases=[],
    name_mapping={
        "max_connections": "maxConnections",
        "max_pending_requests": "maxPendingRequests",
    },
)
class AppmeshVirtualNodeSpecListenerConnectionPoolHttp:
    def __init__(
        self,
        *,
        max_connections: jsii.Number,
        max_pending_requests: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_connections: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_connections AppmeshVirtualNode#max_connections}.
        :param max_pending_requests: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_pending_requests AppmeshVirtualNode#max_pending_requests}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a01b624511a7e649a532ede0c3ac6cfc07b45f50b8db85b59cbd8a2a1c0941df)
            check_type(argname="argument max_connections", value=max_connections, expected_type=type_hints["max_connections"])
            check_type(argname="argument max_pending_requests", value=max_pending_requests, expected_type=type_hints["max_pending_requests"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "max_connections": max_connections,
        }
        if max_pending_requests is not None:
            self._values["max_pending_requests"] = max_pending_requests

    @builtins.property
    def max_connections(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_connections AppmeshVirtualNode#max_connections}.'''
        result = self._values.get("max_connections")
        assert result is not None, "Required property 'max_connections' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def max_pending_requests(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_pending_requests AppmeshVirtualNode#max_pending_requests}.'''
        result = self._values.get("max_pending_requests")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerConnectionPoolHttp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerConnectionPoolHttp2",
    jsii_struct_bases=[],
    name_mapping={"max_requests": "maxRequests"},
)
class AppmeshVirtualNodeSpecListenerConnectionPoolHttp2:
    def __init__(self, *, max_requests: jsii.Number) -> None:
        '''
        :param max_requests: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_requests AppmeshVirtualNode#max_requests}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54c2cb1800a1f9b90d12bb4c8d721d18547398291fcc9d0480412212126cb8dd)
            check_type(argname="argument max_requests", value=max_requests, expected_type=type_hints["max_requests"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "max_requests": max_requests,
        }

    @builtins.property
    def max_requests(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_requests AppmeshVirtualNode#max_requests}.'''
        result = self._values.get("max_requests")
        assert result is not None, "Required property 'max_requests' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerConnectionPoolHttp2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerConnectionPoolHttp2OutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerConnectionPoolHttp2OutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4538053bb7581990396f9f241d77915b161d77e434b3a64031b2fb6f208695c4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="maxRequestsInput")
    def max_requests_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxRequestsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxRequests")
    def max_requests(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxRequests"))

    @max_requests.setter
    def max_requests(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3c457e175193ae78ebff2ab5381b72cc71709e3e6273646438407679916a4bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxRequests", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolHttp2]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolHttp2], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolHttp2],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8101bd085cb8d03e3442615d0423449718aaeefacf3ae077f74f49a35c317983)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecListenerConnectionPoolHttpOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerConnectionPoolHttpOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a7c7969ae3e220362a7bbf15285546ce394557b09a09a6e538710e0ac297b4dc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMaxPendingRequests")
    def reset_max_pending_requests(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxPendingRequests", []))

    @builtins.property
    @jsii.member(jsii_name="maxConnectionsInput")
    def max_connections_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConnectionsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxPendingRequestsInput")
    def max_pending_requests_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxPendingRequestsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConnections")
    def max_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConnections"))

    @max_connections.setter
    def max_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0580a605ddc2ece792a02a1bbe53770795144c2086ec17b342089ee837c973ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConnections", value)

    @builtins.property
    @jsii.member(jsii_name="maxPendingRequests")
    def max_pending_requests(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxPendingRequests"))

    @max_pending_requests.setter
    def max_pending_requests(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34c5f72a91107bc2265c31f009fa5a68c583f7f1d4af929e263aa6f985b9ad29)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxPendingRequests", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolHttp]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolHttp], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolHttp],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa8278a8aeb46e9548428e0753425fb1cba6a30e15c24aa02b4ca49b172d08be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecListenerConnectionPoolOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerConnectionPoolOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1edde56e92b3d3ea16ba2f0e03fcf310d57f036777ccf8cfecb80cda538e1e41)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putGrpc")
    def put_grpc(self, *, max_requests: jsii.Number) -> None:
        '''
        :param max_requests: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_requests AppmeshVirtualNode#max_requests}.
        '''
        value = AppmeshVirtualNodeSpecListenerConnectionPoolGrpc(
            max_requests=max_requests
        )

        return typing.cast(None, jsii.invoke(self, "putGrpc", [value]))

    @jsii.member(jsii_name="putHttp")
    def put_http(
        self,
        *,
        max_connections: jsii.Number,
        max_pending_requests: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_connections: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_connections AppmeshVirtualNode#max_connections}.
        :param max_pending_requests: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_pending_requests AppmeshVirtualNode#max_pending_requests}.
        '''
        value = AppmeshVirtualNodeSpecListenerConnectionPoolHttp(
            max_connections=max_connections, max_pending_requests=max_pending_requests
        )

        return typing.cast(None, jsii.invoke(self, "putHttp", [value]))

    @jsii.member(jsii_name="putHttp2")
    def put_http2(self, *, max_requests: jsii.Number) -> None:
        '''
        :param max_requests: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_requests AppmeshVirtualNode#max_requests}.
        '''
        value = AppmeshVirtualNodeSpecListenerConnectionPoolHttp2(
            max_requests=max_requests
        )

        return typing.cast(None, jsii.invoke(self, "putHttp2", [value]))

    @jsii.member(jsii_name="putTcp")
    def put_tcp(self, *, max_connections: jsii.Number) -> None:
        '''
        :param max_connections: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_connections AppmeshVirtualNode#max_connections}.
        '''
        value = AppmeshVirtualNodeSpecListenerConnectionPoolTcp(
            max_connections=max_connections
        )

        return typing.cast(None, jsii.invoke(self, "putTcp", [value]))

    @jsii.member(jsii_name="resetGrpc")
    def reset_grpc(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGrpc", []))

    @jsii.member(jsii_name="resetHttp")
    def reset_http(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttp", []))

    @jsii.member(jsii_name="resetHttp2")
    def reset_http2(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttp2", []))

    @jsii.member(jsii_name="resetTcp")
    def reset_tcp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTcp", []))

    @builtins.property
    @jsii.member(jsii_name="grpc")
    def grpc(self) -> AppmeshVirtualNodeSpecListenerConnectionPoolGrpcOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerConnectionPoolGrpcOutputReference, jsii.get(self, "grpc"))

    @builtins.property
    @jsii.member(jsii_name="http")
    def http(self) -> AppmeshVirtualNodeSpecListenerConnectionPoolHttpOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerConnectionPoolHttpOutputReference, jsii.get(self, "http"))

    @builtins.property
    @jsii.member(jsii_name="http2")
    def http2(self) -> AppmeshVirtualNodeSpecListenerConnectionPoolHttp2OutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerConnectionPoolHttp2OutputReference, jsii.get(self, "http2"))

    @builtins.property
    @jsii.member(jsii_name="tcp")
    def tcp(self) -> "AppmeshVirtualNodeSpecListenerConnectionPoolTcpOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecListenerConnectionPoolTcpOutputReference", jsii.get(self, "tcp"))

    @builtins.property
    @jsii.member(jsii_name="grpcInput")
    def grpc_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolGrpc]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolGrpc], jsii.get(self, "grpcInput"))

    @builtins.property
    @jsii.member(jsii_name="http2Input")
    def http2_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolHttp2]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolHttp2], jsii.get(self, "http2Input"))

    @builtins.property
    @jsii.member(jsii_name="httpInput")
    def http_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolHttp]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolHttp], jsii.get(self, "httpInput"))

    @builtins.property
    @jsii.member(jsii_name="tcpInput")
    def tcp_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerConnectionPoolTcp"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerConnectionPoolTcp"], jsii.get(self, "tcpInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPool]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPool], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aab5fc798a25053b3eaea3a3f8d23e2e6ee1899b29ed630f0de47f75259ac1a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerConnectionPoolTcp",
    jsii_struct_bases=[],
    name_mapping={"max_connections": "maxConnections"},
)
class AppmeshVirtualNodeSpecListenerConnectionPoolTcp:
    def __init__(self, *, max_connections: jsii.Number) -> None:
        '''
        :param max_connections: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_connections AppmeshVirtualNode#max_connections}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df53ed8c0924d8a9902edc19d091ed1289fd4f6ceb433783dc0db5528a0fa5a2)
            check_type(argname="argument max_connections", value=max_connections, expected_type=type_hints["max_connections"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "max_connections": max_connections,
        }

    @builtins.property
    def max_connections(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_connections AppmeshVirtualNode#max_connections}.'''
        result = self._values.get("max_connections")
        assert result is not None, "Required property 'max_connections' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerConnectionPoolTcp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerConnectionPoolTcpOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerConnectionPoolTcpOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d61c432b4edff9e418c07387436e23e1e1f8fa0bf3acc17e78da40872503b86d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="maxConnectionsInput")
    def max_connections_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConnectionsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConnections")
    def max_connections(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConnections"))

    @max_connections.setter
    def max_connections(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98c5afd2b8cf90bbc20a5a9f0a37469be2af29d12f54fa231d341be515b1ac33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConnections", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolTcp]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolTcp], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolTcp],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af9981797c73bce5da1804514a594e65a204e10ab17ef3724edb20c400a0e882)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerHealthCheck",
    jsii_struct_bases=[],
    name_mapping={
        "healthy_threshold": "healthyThreshold",
        "interval_millis": "intervalMillis",
        "protocol": "protocol",
        "timeout_millis": "timeoutMillis",
        "unhealthy_threshold": "unhealthyThreshold",
        "path": "path",
        "port": "port",
    },
)
class AppmeshVirtualNodeSpecListenerHealthCheck:
    def __init__(
        self,
        *,
        healthy_threshold: jsii.Number,
        interval_millis: jsii.Number,
        protocol: builtins.str,
        timeout_millis: jsii.Number,
        unhealthy_threshold: jsii.Number,
        path: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param healthy_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#healthy_threshold AppmeshVirtualNode#healthy_threshold}.
        :param interval_millis: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#interval_millis AppmeshVirtualNode#interval_millis}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#protocol AppmeshVirtualNode#protocol}.
        :param timeout_millis: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#timeout_millis AppmeshVirtualNode#timeout_millis}.
        :param unhealthy_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unhealthy_threshold AppmeshVirtualNode#unhealthy_threshold}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#path AppmeshVirtualNode#path}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#port AppmeshVirtualNode#port}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__618d044954c4a44ffd2a363bc1d1e9546cc72e3b0920bae3704b633d0876ec08)
            check_type(argname="argument healthy_threshold", value=healthy_threshold, expected_type=type_hints["healthy_threshold"])
            check_type(argname="argument interval_millis", value=interval_millis, expected_type=type_hints["interval_millis"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument timeout_millis", value=timeout_millis, expected_type=type_hints["timeout_millis"])
            check_type(argname="argument unhealthy_threshold", value=unhealthy_threshold, expected_type=type_hints["unhealthy_threshold"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "healthy_threshold": healthy_threshold,
            "interval_millis": interval_millis,
            "protocol": protocol,
            "timeout_millis": timeout_millis,
            "unhealthy_threshold": unhealthy_threshold,
        }
        if path is not None:
            self._values["path"] = path
        if port is not None:
            self._values["port"] = port

    @builtins.property
    def healthy_threshold(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#healthy_threshold AppmeshVirtualNode#healthy_threshold}.'''
        result = self._values.get("healthy_threshold")
        assert result is not None, "Required property 'healthy_threshold' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def interval_millis(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#interval_millis AppmeshVirtualNode#interval_millis}.'''
        result = self._values.get("interval_millis")
        assert result is not None, "Required property 'interval_millis' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#protocol AppmeshVirtualNode#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def timeout_millis(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#timeout_millis AppmeshVirtualNode#timeout_millis}.'''
        result = self._values.get("timeout_millis")
        assert result is not None, "Required property 'timeout_millis' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def unhealthy_threshold(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unhealthy_threshold AppmeshVirtualNode#unhealthy_threshold}.'''
        result = self._values.get("unhealthy_threshold")
        assert result is not None, "Required property 'unhealthy_threshold' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#path AppmeshVirtualNode#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#port AppmeshVirtualNode#port}.'''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerHealthCheck(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerHealthCheckOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerHealthCheckOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cb10f233040cabd31473ad81f0559ce792f182de0b212a48cbd9ceeca1b352b5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @builtins.property
    @jsii.member(jsii_name="healthyThresholdInput")
    def healthy_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "healthyThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalMillisInput")
    def interval_millis_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalMillisInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutMillisInput")
    def timeout_millis_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutMillisInput"))

    @builtins.property
    @jsii.member(jsii_name="unhealthyThresholdInput")
    def unhealthy_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "unhealthyThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="healthyThreshold")
    def healthy_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "healthyThreshold"))

    @healthy_threshold.setter
    def healthy_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d3f4e6cfdea4fc5a7e2b04cf9a59651fc29c77ce0652ccabddc8d14f25af193)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthyThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="intervalMillis")
    def interval_millis(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "intervalMillis"))

    @interval_millis.setter
    def interval_millis(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e7bbe24438ed6ab73ad95183b0f7a7093a13e1ce3c436845b1aa18ba8c9eda9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intervalMillis", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a42a4fd74b5d13c86d7bcff28f9551d09bd389a014556e6d51f00f2f4f5fee70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e00fc67a5ecd0e7877603b0da432500bf0ec6be6b5dedda8049af19e11f4a0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d61c898c214df52e89d285ff0ef481d1163bd76e4224ea8025c8b0042cbf389)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutMillis")
    def timeout_millis(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutMillis"))

    @timeout_millis.setter
    def timeout_millis(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7165aaf0e1002cb0df6ba33e30b529dd1028a9fd5946d55b617d11e887532573)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutMillis", value)

    @builtins.property
    @jsii.member(jsii_name="unhealthyThreshold")
    def unhealthy_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "unhealthyThreshold"))

    @unhealthy_threshold.setter
    def unhealthy_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54f6ad7be614b6a73fc3e21965b8731a12765b0ac5a6924cbb03d7381de37565)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unhealthyThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerHealthCheck]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerHealthCheck], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerHealthCheck],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__777b9299df96f92c649c596970cafe1eca63a43fad08722a62ae827365f6b414)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerOutlierDetection",
    jsii_struct_bases=[],
    name_mapping={
        "base_ejection_duration": "baseEjectionDuration",
        "interval": "interval",
        "max_ejection_percent": "maxEjectionPercent",
        "max_server_errors": "maxServerErrors",
    },
)
class AppmeshVirtualNodeSpecListenerOutlierDetection:
    def __init__(
        self,
        *,
        base_ejection_duration: typing.Union["AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDuration", typing.Dict[builtins.str, typing.Any]],
        interval: typing.Union["AppmeshVirtualNodeSpecListenerOutlierDetectionInterval", typing.Dict[builtins.str, typing.Any]],
        max_ejection_percent: jsii.Number,
        max_server_errors: jsii.Number,
    ) -> None:
        '''
        :param base_ejection_duration: base_ejection_duration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#base_ejection_duration AppmeshVirtualNode#base_ejection_duration}
        :param interval: interval block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#interval AppmeshVirtualNode#interval}
        :param max_ejection_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_ejection_percent AppmeshVirtualNode#max_ejection_percent}.
        :param max_server_errors: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_server_errors AppmeshVirtualNode#max_server_errors}.
        '''
        if isinstance(base_ejection_duration, dict):
            base_ejection_duration = AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDuration(**base_ejection_duration)
        if isinstance(interval, dict):
            interval = AppmeshVirtualNodeSpecListenerOutlierDetectionInterval(**interval)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__892c5d8ac210e5ad318b001c81ece41283348f3d9042e816d648efcb9684bbed)
            check_type(argname="argument base_ejection_duration", value=base_ejection_duration, expected_type=type_hints["base_ejection_duration"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument max_ejection_percent", value=max_ejection_percent, expected_type=type_hints["max_ejection_percent"])
            check_type(argname="argument max_server_errors", value=max_server_errors, expected_type=type_hints["max_server_errors"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "base_ejection_duration": base_ejection_duration,
            "interval": interval,
            "max_ejection_percent": max_ejection_percent,
            "max_server_errors": max_server_errors,
        }

    @builtins.property
    def base_ejection_duration(
        self,
    ) -> "AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDuration":
        '''base_ejection_duration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#base_ejection_duration AppmeshVirtualNode#base_ejection_duration}
        '''
        result = self._values.get("base_ejection_duration")
        assert result is not None, "Required property 'base_ejection_duration' is missing"
        return typing.cast("AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDuration", result)

    @builtins.property
    def interval(self) -> "AppmeshVirtualNodeSpecListenerOutlierDetectionInterval":
        '''interval block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#interval AppmeshVirtualNode#interval}
        '''
        result = self._values.get("interval")
        assert result is not None, "Required property 'interval' is missing"
        return typing.cast("AppmeshVirtualNodeSpecListenerOutlierDetectionInterval", result)

    @builtins.property
    def max_ejection_percent(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_ejection_percent AppmeshVirtualNode#max_ejection_percent}.'''
        result = self._values.get("max_ejection_percent")
        assert result is not None, "Required property 'max_ejection_percent' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def max_server_errors(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_server_errors AppmeshVirtualNode#max_server_errors}.'''
        result = self._values.get("max_server_errors")
        assert result is not None, "Required property 'max_server_errors' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerOutlierDetection(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDuration",
    jsii_struct_bases=[],
    name_mapping={"unit": "unit", "value": "value"},
)
class AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDuration:
    def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__592467e076dbe821cd8ee0dd475153c97e7b4356308f118f44e84fd476ff8680)
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "unit": unit,
            "value": value,
        }

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDuration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f3d22e22173b25ed2f5e1409e7e2f6ff35d5b39f117eea2bb36dc45d3eba46ae)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdc900165b3eaf92d1ac619f821c9a0d409a1cebcf3ca52a38473e07c39478d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7557e9dd5222bb42edcd91c6fe9d662722ce057550e6064c0e87711390c5db4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDuration]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDuration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDuration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d9518d10474b0f4342293f97f9f39fd860d0d8f52378ee019c2d8a8a644c52d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerOutlierDetectionInterval",
    jsii_struct_bases=[],
    name_mapping={"unit": "unit", "value": "value"},
)
class AppmeshVirtualNodeSpecListenerOutlierDetectionInterval:
    def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a05d002bed226c06a60eff669f2664a8d13886c1db5636c5bfc2c6e88e9ac9e)
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "unit": unit,
            "value": value,
        }

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerOutlierDetectionInterval(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerOutlierDetectionIntervalOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerOutlierDetectionIntervalOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__212b2a33840eaf822187f5c0ff1821e5ffa673cab6e1b4fba5514dbfa581855b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35a815d87b8e277417fbd37aee2cf49d49d9a8e1b439fb1a32a8b32ae5265e5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d73ac93f65df857700bd503254c42197386e80aea65893f140fe9742b43a2ed8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerOutlierDetectionInterval]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerOutlierDetectionInterval], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerOutlierDetectionInterval],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0109993a02c70ac5b0a6f40c062d1cf61162a992d9909f2e953c48e361cb6182)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecListenerOutlierDetectionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerOutlierDetectionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8ba83fb71e79f7c99eeff923e80f8e2852c87137aa4c7ca3c1d5477b4ca57393)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBaseEjectionDuration")
    def put_base_ejection_duration(
        self,
        *,
        unit: builtins.str,
        value: jsii.Number,
    ) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.
        '''
        value_ = AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDuration(
            unit=unit, value=value
        )

        return typing.cast(None, jsii.invoke(self, "putBaseEjectionDuration", [value_]))

    @jsii.member(jsii_name="putInterval")
    def put_interval(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.
        '''
        value_ = AppmeshVirtualNodeSpecListenerOutlierDetectionInterval(
            unit=unit, value=value
        )

        return typing.cast(None, jsii.invoke(self, "putInterval", [value_]))

    @builtins.property
    @jsii.member(jsii_name="baseEjectionDuration")
    def base_ejection_duration(
        self,
    ) -> AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDurationOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDurationOutputReference, jsii.get(self, "baseEjectionDuration"))

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(
        self,
    ) -> AppmeshVirtualNodeSpecListenerOutlierDetectionIntervalOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerOutlierDetectionIntervalOutputReference, jsii.get(self, "interval"))

    @builtins.property
    @jsii.member(jsii_name="baseEjectionDurationInput")
    def base_ejection_duration_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDuration]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDuration], jsii.get(self, "baseEjectionDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerOutlierDetectionInterval]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerOutlierDetectionInterval], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="maxEjectionPercentInput")
    def max_ejection_percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxEjectionPercentInput"))

    @builtins.property
    @jsii.member(jsii_name="maxServerErrorsInput")
    def max_server_errors_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxServerErrorsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxEjectionPercent")
    def max_ejection_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxEjectionPercent"))

    @max_ejection_percent.setter
    def max_ejection_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbfd8a168accf9a679e5b1f90f37ee1bd73a72a7347dcf56ae44c027cb904b70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxEjectionPercent", value)

    @builtins.property
    @jsii.member(jsii_name="maxServerErrors")
    def max_server_errors(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxServerErrors"))

    @max_server_errors.setter
    def max_server_errors(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6db75fba44bef3d1777590292f7abcbaf33ec1978b9c786dd84595a7cfab6025)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxServerErrors", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerOutlierDetection]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerOutlierDetection], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerOutlierDetection],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2eadf43b3fe456868847236f9d67289d8755dc5fc4e62c331a205e046d25b0b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecListenerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7ec88e01dfcb45a247349c2b280028cf7cadb962a7d708911aad5cef7cf2cc66)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putConnectionPool")
    def put_connection_pool(
        self,
        *,
        grpc: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerConnectionPoolGrpc, typing.Dict[builtins.str, typing.Any]]] = None,
        http: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerConnectionPoolHttp, typing.Dict[builtins.str, typing.Any]]] = None,
        http2: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerConnectionPoolHttp2, typing.Dict[builtins.str, typing.Any]]] = None,
        tcp: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerConnectionPoolTcp, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param grpc: grpc block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#grpc AppmeshVirtualNode#grpc}
        :param http: http block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#http AppmeshVirtualNode#http}
        :param http2: http2 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#http2 AppmeshVirtualNode#http2}
        :param tcp: tcp block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tcp AppmeshVirtualNode#tcp}
        '''
        value = AppmeshVirtualNodeSpecListenerConnectionPool(
            grpc=grpc, http=http, http2=http2, tcp=tcp
        )

        return typing.cast(None, jsii.invoke(self, "putConnectionPool", [value]))

    @jsii.member(jsii_name="putHealthCheck")
    def put_health_check(
        self,
        *,
        healthy_threshold: jsii.Number,
        interval_millis: jsii.Number,
        protocol: builtins.str,
        timeout_millis: jsii.Number,
        unhealthy_threshold: jsii.Number,
        path: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param healthy_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#healthy_threshold AppmeshVirtualNode#healthy_threshold}.
        :param interval_millis: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#interval_millis AppmeshVirtualNode#interval_millis}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#protocol AppmeshVirtualNode#protocol}.
        :param timeout_millis: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#timeout_millis AppmeshVirtualNode#timeout_millis}.
        :param unhealthy_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unhealthy_threshold AppmeshVirtualNode#unhealthy_threshold}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#path AppmeshVirtualNode#path}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#port AppmeshVirtualNode#port}.
        '''
        value = AppmeshVirtualNodeSpecListenerHealthCheck(
            healthy_threshold=healthy_threshold,
            interval_millis=interval_millis,
            protocol=protocol,
            timeout_millis=timeout_millis,
            unhealthy_threshold=unhealthy_threshold,
            path=path,
            port=port,
        )

        return typing.cast(None, jsii.invoke(self, "putHealthCheck", [value]))

    @jsii.member(jsii_name="putOutlierDetection")
    def put_outlier_detection(
        self,
        *,
        base_ejection_duration: typing.Union[AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDuration, typing.Dict[builtins.str, typing.Any]],
        interval: typing.Union[AppmeshVirtualNodeSpecListenerOutlierDetectionInterval, typing.Dict[builtins.str, typing.Any]],
        max_ejection_percent: jsii.Number,
        max_server_errors: jsii.Number,
    ) -> None:
        '''
        :param base_ejection_duration: base_ejection_duration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#base_ejection_duration AppmeshVirtualNode#base_ejection_duration}
        :param interval: interval block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#interval AppmeshVirtualNode#interval}
        :param max_ejection_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_ejection_percent AppmeshVirtualNode#max_ejection_percent}.
        :param max_server_errors: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#max_server_errors AppmeshVirtualNode#max_server_errors}.
        '''
        value = AppmeshVirtualNodeSpecListenerOutlierDetection(
            base_ejection_duration=base_ejection_duration,
            interval=interval,
            max_ejection_percent=max_ejection_percent,
            max_server_errors=max_server_errors,
        )

        return typing.cast(None, jsii.invoke(self, "putOutlierDetection", [value]))

    @jsii.member(jsii_name="putPortMapping")
    def put_port_mapping(self, *, port: jsii.Number, protocol: builtins.str) -> None:
        '''
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#port AppmeshVirtualNode#port}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#protocol AppmeshVirtualNode#protocol}.
        '''
        value = AppmeshVirtualNodeSpecListenerPortMapping(port=port, protocol=protocol)

        return typing.cast(None, jsii.invoke(self, "putPortMapping", [value]))

    @jsii.member(jsii_name="putTimeout")
    def put_timeout(
        self,
        *,
        grpc: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTimeoutGrpc", typing.Dict[builtins.str, typing.Any]]] = None,
        http: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTimeoutHttp", typing.Dict[builtins.str, typing.Any]]] = None,
        http2: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTimeoutHttp2", typing.Dict[builtins.str, typing.Any]]] = None,
        tcp: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTimeoutTcp", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param grpc: grpc block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#grpc AppmeshVirtualNode#grpc}
        :param http: http block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#http AppmeshVirtualNode#http}
        :param http2: http2 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#http2 AppmeshVirtualNode#http2}
        :param tcp: tcp block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tcp AppmeshVirtualNode#tcp}
        '''
        value = AppmeshVirtualNodeSpecListenerTimeout(
            grpc=grpc, http=http, http2=http2, tcp=tcp
        )

        return typing.cast(None, jsii.invoke(self, "putTimeout", [value]))

    @jsii.member(jsii_name="putTls")
    def put_tls(
        self,
        *,
        certificate: typing.Union["AppmeshVirtualNodeSpecListenerTlsCertificate", typing.Dict[builtins.str, typing.Any]],
        mode: builtins.str,
        validation: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTlsValidation", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param certificate: certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate AppmeshVirtualNode#certificate}
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#mode AppmeshVirtualNode#mode}.
        :param validation: validation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#validation AppmeshVirtualNode#validation}
        '''
        value = AppmeshVirtualNodeSpecListenerTls(
            certificate=certificate, mode=mode, validation=validation
        )

        return typing.cast(None, jsii.invoke(self, "putTls", [value]))

    @jsii.member(jsii_name="resetConnectionPool")
    def reset_connection_pool(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionPool", []))

    @jsii.member(jsii_name="resetHealthCheck")
    def reset_health_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheck", []))

    @jsii.member(jsii_name="resetOutlierDetection")
    def reset_outlier_detection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutlierDetection", []))

    @jsii.member(jsii_name="resetTimeout")
    def reset_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeout", []))

    @jsii.member(jsii_name="resetTls")
    def reset_tls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTls", []))

    @builtins.property
    @jsii.member(jsii_name="connectionPool")
    def connection_pool(
        self,
    ) -> AppmeshVirtualNodeSpecListenerConnectionPoolOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerConnectionPoolOutputReference, jsii.get(self, "connectionPool"))

    @builtins.property
    @jsii.member(jsii_name="healthCheck")
    def health_check(self) -> AppmeshVirtualNodeSpecListenerHealthCheckOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerHealthCheckOutputReference, jsii.get(self, "healthCheck"))

    @builtins.property
    @jsii.member(jsii_name="outlierDetection")
    def outlier_detection(
        self,
    ) -> AppmeshVirtualNodeSpecListenerOutlierDetectionOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerOutlierDetectionOutputReference, jsii.get(self, "outlierDetection"))

    @builtins.property
    @jsii.member(jsii_name="portMapping")
    def port_mapping(
        self,
    ) -> "AppmeshVirtualNodeSpecListenerPortMappingOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecListenerPortMappingOutputReference", jsii.get(self, "portMapping"))

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> "AppmeshVirtualNodeSpecListenerTimeoutOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecListenerTimeoutOutputReference", jsii.get(self, "timeout"))

    @builtins.property
    @jsii.member(jsii_name="tls")
    def tls(self) -> "AppmeshVirtualNodeSpecListenerTlsOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecListenerTlsOutputReference", jsii.get(self, "tls"))

    @builtins.property
    @jsii.member(jsii_name="connectionPoolInput")
    def connection_pool_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPool]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPool], jsii.get(self, "connectionPoolInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckInput")
    def health_check_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerHealthCheck]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerHealthCheck], jsii.get(self, "healthCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="outlierDetectionInput")
    def outlier_detection_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerOutlierDetection]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerOutlierDetection], jsii.get(self, "outlierDetectionInput"))

    @builtins.property
    @jsii.member(jsii_name="portMappingInput")
    def port_mapping_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerPortMapping"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerPortMapping"], jsii.get(self, "portMappingInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(self) -> typing.Optional["AppmeshVirtualNodeSpecListenerTimeout"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTimeout"], jsii.get(self, "timeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsInput")
    def tls_input(self) -> typing.Optional["AppmeshVirtualNodeSpecListenerTls"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTls"], jsii.get(self, "tlsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshVirtualNodeSpecListener]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListener], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListener],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e81712ee667195c3c1a11013fa41bd66cb816e5b1d0ef6a4303c40f6e67651a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerPortMapping",
    jsii_struct_bases=[],
    name_mapping={"port": "port", "protocol": "protocol"},
)
class AppmeshVirtualNodeSpecListenerPortMapping:
    def __init__(self, *, port: jsii.Number, protocol: builtins.str) -> None:
        '''
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#port AppmeshVirtualNode#port}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#protocol AppmeshVirtualNode#protocol}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da959cb4c20f7d276308c867058b13d9c35ee8d7b556b756283195b02a822c2e)
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "port": port,
            "protocol": protocol,
        }

    @builtins.property
    def port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#port AppmeshVirtualNode#port}.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#protocol AppmeshVirtualNode#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerPortMapping(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerPortMappingOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerPortMappingOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2267c0935efad8123d6d42b82cb036ecdf3f2a192a75e6bfbd83c7ba36f6b1a2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95854854c8d9d8cec9a30967d4d1447bed90e025ef6eb3377faf47d891ef058a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39879b5aa4281dfa5c0cecb633da653c339b51b87103cf3f49603397aa551908)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerPortMapping]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerPortMapping], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerPortMapping],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__942408529637d2a43dc327499a74ee123a051975545f6214633c24aba0c7252e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeout",
    jsii_struct_bases=[],
    name_mapping={"grpc": "grpc", "http": "http", "http2": "http2", "tcp": "tcp"},
)
class AppmeshVirtualNodeSpecListenerTimeout:
    def __init__(
        self,
        *,
        grpc: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTimeoutGrpc", typing.Dict[builtins.str, typing.Any]]] = None,
        http: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTimeoutHttp", typing.Dict[builtins.str, typing.Any]]] = None,
        http2: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTimeoutHttp2", typing.Dict[builtins.str, typing.Any]]] = None,
        tcp: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTimeoutTcp", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param grpc: grpc block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#grpc AppmeshVirtualNode#grpc}
        :param http: http block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#http AppmeshVirtualNode#http}
        :param http2: http2 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#http2 AppmeshVirtualNode#http2}
        :param tcp: tcp block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tcp AppmeshVirtualNode#tcp}
        '''
        if isinstance(grpc, dict):
            grpc = AppmeshVirtualNodeSpecListenerTimeoutGrpc(**grpc)
        if isinstance(http, dict):
            http = AppmeshVirtualNodeSpecListenerTimeoutHttp(**http)
        if isinstance(http2, dict):
            http2 = AppmeshVirtualNodeSpecListenerTimeoutHttp2(**http2)
        if isinstance(tcp, dict):
            tcp = AppmeshVirtualNodeSpecListenerTimeoutTcp(**tcp)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__331d71893c6a08fac53976bff60ec57e687c6dab22e0ac55bb2544112f16a7e4)
            check_type(argname="argument grpc", value=grpc, expected_type=type_hints["grpc"])
            check_type(argname="argument http", value=http, expected_type=type_hints["http"])
            check_type(argname="argument http2", value=http2, expected_type=type_hints["http2"])
            check_type(argname="argument tcp", value=tcp, expected_type=type_hints["tcp"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if grpc is not None:
            self._values["grpc"] = grpc
        if http is not None:
            self._values["http"] = http
        if http2 is not None:
            self._values["http2"] = http2
        if tcp is not None:
            self._values["tcp"] = tcp

    @builtins.property
    def grpc(self) -> typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutGrpc"]:
        '''grpc block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#grpc AppmeshVirtualNode#grpc}
        '''
        result = self._values.get("grpc")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutGrpc"], result)

    @builtins.property
    def http(self) -> typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutHttp"]:
        '''http block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#http AppmeshVirtualNode#http}
        '''
        result = self._values.get("http")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutHttp"], result)

    @builtins.property
    def http2(self) -> typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutHttp2"]:
        '''http2 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#http2 AppmeshVirtualNode#http2}
        '''
        result = self._values.get("http2")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutHttp2"], result)

    @builtins.property
    def tcp(self) -> typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutTcp"]:
        '''tcp block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tcp AppmeshVirtualNode#tcp}
        '''
        result = self._values.get("tcp")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutTcp"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTimeout(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutGrpc",
    jsii_struct_bases=[],
    name_mapping={"idle": "idle", "per_request": "perRequest"},
)
class AppmeshVirtualNodeSpecListenerTimeoutGrpc:
    def __init__(
        self,
        *,
        idle: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTimeoutGrpcIdle", typing.Dict[builtins.str, typing.Any]]] = None,
        per_request: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequest", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param idle: idle block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#idle AppmeshVirtualNode#idle}
        :param per_request: per_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#per_request AppmeshVirtualNode#per_request}
        '''
        if isinstance(idle, dict):
            idle = AppmeshVirtualNodeSpecListenerTimeoutGrpcIdle(**idle)
        if isinstance(per_request, dict):
            per_request = AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequest(**per_request)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21b83df330bc4d9ff3997b2faa5d08b23214499e099c732455e569f22c826502)
            check_type(argname="argument idle", value=idle, expected_type=type_hints["idle"])
            check_type(argname="argument per_request", value=per_request, expected_type=type_hints["per_request"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if idle is not None:
            self._values["idle"] = idle
        if per_request is not None:
            self._values["per_request"] = per_request

    @builtins.property
    def idle(self) -> typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutGrpcIdle"]:
        '''idle block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#idle AppmeshVirtualNode#idle}
        '''
        result = self._values.get("idle")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutGrpcIdle"], result)

    @builtins.property
    def per_request(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequest"]:
        '''per_request block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#per_request AppmeshVirtualNode#per_request}
        '''
        result = self._values.get("per_request")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequest"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTimeoutGrpc(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutGrpcIdle",
    jsii_struct_bases=[],
    name_mapping={"unit": "unit", "value": "value"},
)
class AppmeshVirtualNodeSpecListenerTimeoutGrpcIdle:
    def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3925e9fe9b27af327058539e7892f3fccc49338fe735fab973cbd736425b41dc)
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "unit": unit,
            "value": value,
        }

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTimeoutGrpcIdle(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerTimeoutGrpcIdleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutGrpcIdleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9630b6da97a65480f5c01effd22c05f54837f5a3637786f9f3e0159d1e0b51a1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21a5a7180236ef4420939cf9f2aa05d0b5a6e936f7e621d4fe9c882b96123f20)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa94c9315f22feda82c9ae0762c699c857351608f1fb3e7c08f79afb7f469b96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutGrpcIdle]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutGrpcIdle], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutGrpcIdle],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4f8b663b6b2d7817e2182e6209cd157ac8049f14c17cae86c1369a9711dd2b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecListenerTimeoutGrpcOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutGrpcOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5e112d1fa3f3da5469a371e440f6bdef8430d4e3521760ed4c1ec85f65372d34)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putIdle")
    def put_idle(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.
        '''
        value_ = AppmeshVirtualNodeSpecListenerTimeoutGrpcIdle(unit=unit, value=value)

        return typing.cast(None, jsii.invoke(self, "putIdle", [value_]))

    @jsii.member(jsii_name="putPerRequest")
    def put_per_request(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.
        '''
        value_ = AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequest(
            unit=unit, value=value
        )

        return typing.cast(None, jsii.invoke(self, "putPerRequest", [value_]))

    @jsii.member(jsii_name="resetIdle")
    def reset_idle(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdle", []))

    @jsii.member(jsii_name="resetPerRequest")
    def reset_per_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPerRequest", []))

    @builtins.property
    @jsii.member(jsii_name="idle")
    def idle(self) -> AppmeshVirtualNodeSpecListenerTimeoutGrpcIdleOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerTimeoutGrpcIdleOutputReference, jsii.get(self, "idle"))

    @builtins.property
    @jsii.member(jsii_name="perRequest")
    def per_request(
        self,
    ) -> "AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequestOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequestOutputReference", jsii.get(self, "perRequest"))

    @builtins.property
    @jsii.member(jsii_name="idleInput")
    def idle_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutGrpcIdle]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutGrpcIdle], jsii.get(self, "idleInput"))

    @builtins.property
    @jsii.member(jsii_name="perRequestInput")
    def per_request_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequest"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequest"], jsii.get(self, "perRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutGrpc]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutGrpc], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutGrpc],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8a5adfd306543f44633b1d8d593b4f41d10a225d44b895ea2fde885053f0c98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequest",
    jsii_struct_bases=[],
    name_mapping={"unit": "unit", "value": "value"},
)
class AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequest:
    def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be437169e9c73d751af2188652623f6bb356650103427cad9e6cec35acfe6fe4)
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "unit": unit,
            "value": value,
        }

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequestOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequestOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__daba591cc8de2929fd4fae7432ca0d1f2cb8b66bba5caa24061871afc1914cc7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d755b3b6a997da4f14d5a20dfb3812be91df7c41f884c48324a04f52ad64e9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bd8e75a9e80a489e8304a6c9d7fd3c95405426e07c99c5255c4d69abb7fd78a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequest]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequest],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__913cfe8c715783fa1d2b6b7bc07e043578d4d9872d2943a09ef78cce5fdd86bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutHttp",
    jsii_struct_bases=[],
    name_mapping={"idle": "idle", "per_request": "perRequest"},
)
class AppmeshVirtualNodeSpecListenerTimeoutHttp:
    def __init__(
        self,
        *,
        idle: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTimeoutHttpIdle", typing.Dict[builtins.str, typing.Any]]] = None,
        per_request: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequest", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param idle: idle block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#idle AppmeshVirtualNode#idle}
        :param per_request: per_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#per_request AppmeshVirtualNode#per_request}
        '''
        if isinstance(idle, dict):
            idle = AppmeshVirtualNodeSpecListenerTimeoutHttpIdle(**idle)
        if isinstance(per_request, dict):
            per_request = AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequest(**per_request)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6dc5c0b89a7d362fe6868667ad5ed45b312fcabae9ff6100266894092c5af74e)
            check_type(argname="argument idle", value=idle, expected_type=type_hints["idle"])
            check_type(argname="argument per_request", value=per_request, expected_type=type_hints["per_request"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if idle is not None:
            self._values["idle"] = idle
        if per_request is not None:
            self._values["per_request"] = per_request

    @builtins.property
    def idle(self) -> typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutHttpIdle"]:
        '''idle block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#idle AppmeshVirtualNode#idle}
        '''
        result = self._values.get("idle")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutHttpIdle"], result)

    @builtins.property
    def per_request(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequest"]:
        '''per_request block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#per_request AppmeshVirtualNode#per_request}
        '''
        result = self._values.get("per_request")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequest"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTimeoutHttp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutHttp2",
    jsii_struct_bases=[],
    name_mapping={"idle": "idle", "per_request": "perRequest"},
)
class AppmeshVirtualNodeSpecListenerTimeoutHttp2:
    def __init__(
        self,
        *,
        idle: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTimeoutHttp2Idle", typing.Dict[builtins.str, typing.Any]]] = None,
        per_request: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequest", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param idle: idle block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#idle AppmeshVirtualNode#idle}
        :param per_request: per_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#per_request AppmeshVirtualNode#per_request}
        '''
        if isinstance(idle, dict):
            idle = AppmeshVirtualNodeSpecListenerTimeoutHttp2Idle(**idle)
        if isinstance(per_request, dict):
            per_request = AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequest(**per_request)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4aed04cbfebfa19a5380f4787549ce9fb41d28a776321114370793d4bd74022b)
            check_type(argname="argument idle", value=idle, expected_type=type_hints["idle"])
            check_type(argname="argument per_request", value=per_request, expected_type=type_hints["per_request"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if idle is not None:
            self._values["idle"] = idle
        if per_request is not None:
            self._values["per_request"] = per_request

    @builtins.property
    def idle(self) -> typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutHttp2Idle"]:
        '''idle block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#idle AppmeshVirtualNode#idle}
        '''
        result = self._values.get("idle")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutHttp2Idle"], result)

    @builtins.property
    def per_request(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequest"]:
        '''per_request block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#per_request AppmeshVirtualNode#per_request}
        '''
        result = self._values.get("per_request")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequest"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTimeoutHttp2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutHttp2Idle",
    jsii_struct_bases=[],
    name_mapping={"unit": "unit", "value": "value"},
)
class AppmeshVirtualNodeSpecListenerTimeoutHttp2Idle:
    def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffbeb38214c3843a6a5ed727db7fe02dad4d3717c8a94a6768b96ef336f47ada)
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "unit": unit,
            "value": value,
        }

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTimeoutHttp2Idle(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerTimeoutHttp2IdleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutHttp2IdleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e228fd4796edd81738091ba6d3e19d2bb5feafe21eb23ae79e38c46e9b1b9186)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b40caa00a5e504db477330b222034e01e18754d184d68b33b3c47aee72ce48ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21bf9863e25598dcd1b897fc4ccf228540c1d664dc99146f8ac626c89543a5a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp2Idle]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp2Idle], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp2Idle],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3bbc108eea3462169406ae7db1a2d79939c98d08eb968a0ed2f7cfda26d5ba8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecListenerTimeoutHttp2OutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutHttp2OutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__aafc8e9dbaa953aab7fb35c55af6df69a0b938517701bb0fccd10d1ed87b5bad)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putIdle")
    def put_idle(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.
        '''
        value_ = AppmeshVirtualNodeSpecListenerTimeoutHttp2Idle(unit=unit, value=value)

        return typing.cast(None, jsii.invoke(self, "putIdle", [value_]))

    @jsii.member(jsii_name="putPerRequest")
    def put_per_request(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.
        '''
        value_ = AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequest(
            unit=unit, value=value
        )

        return typing.cast(None, jsii.invoke(self, "putPerRequest", [value_]))

    @jsii.member(jsii_name="resetIdle")
    def reset_idle(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdle", []))

    @jsii.member(jsii_name="resetPerRequest")
    def reset_per_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPerRequest", []))

    @builtins.property
    @jsii.member(jsii_name="idle")
    def idle(self) -> AppmeshVirtualNodeSpecListenerTimeoutHttp2IdleOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerTimeoutHttp2IdleOutputReference, jsii.get(self, "idle"))

    @builtins.property
    @jsii.member(jsii_name="perRequest")
    def per_request(
        self,
    ) -> "AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequestOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequestOutputReference", jsii.get(self, "perRequest"))

    @builtins.property
    @jsii.member(jsii_name="idleInput")
    def idle_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp2Idle]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp2Idle], jsii.get(self, "idleInput"))

    @builtins.property
    @jsii.member(jsii_name="perRequestInput")
    def per_request_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequest"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequest"], jsii.get(self, "perRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp2]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp2], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp2],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a82e772f4905ebefb1917d1b98cb4ce56dd5aeb180a697f9db0a6615627cad4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequest",
    jsii_struct_bases=[],
    name_mapping={"unit": "unit", "value": "value"},
)
class AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequest:
    def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3e4001653e57e08fcad1c8ad0cc431159f2c01cedc47cc557a1734e06576986)
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "unit": unit,
            "value": value,
        }

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequestOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequestOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__910f7cebe9585d7ef0af21f5422936702526490e8841c0e43de88624b0d37b71)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1b1083744cf200585370cb22e198e718f454b65ef59f54f89050754aba4baef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d18cfb41fb207a6ebf5a479002b150ed69c46ca9553b2ae12542098a25471402)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequest]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequest],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9eb09e947ebcb473b1f8a2d1752a98784a3d85d2b4b748d25ee9e84b0feb7e34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutHttpIdle",
    jsii_struct_bases=[],
    name_mapping={"unit": "unit", "value": "value"},
)
class AppmeshVirtualNodeSpecListenerTimeoutHttpIdle:
    def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23cc6562daf095a27f50aec46e222269d2455f87564f46c0bed179324e536644)
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "unit": unit,
            "value": value,
        }

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTimeoutHttpIdle(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerTimeoutHttpIdleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutHttpIdleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3f8cfd952f9aa30563edc9183f4659afa53d4c2055b8d938bd7035a0f394bc6b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__172a02bc4f98188e5a08bfaa557a4a4a3c6857c17158698c2570282ea6f92332)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebff2145817fbf3ec73b2a5fa7116ade23e6a17ca9051c87ce7ca5b688cd8e6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttpIdle]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttpIdle], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttpIdle],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8c3ea526cc377b9450ff75b1f5dca082597e8bdf6a6b1ae803b14597f752847)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecListenerTimeoutHttpOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutHttpOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d71e6f43d32b86abd953a2b33577e4dcbd4f7f90ffcf4680b3cd4e8430efd5f1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putIdle")
    def put_idle(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.
        '''
        value_ = AppmeshVirtualNodeSpecListenerTimeoutHttpIdle(unit=unit, value=value)

        return typing.cast(None, jsii.invoke(self, "putIdle", [value_]))

    @jsii.member(jsii_name="putPerRequest")
    def put_per_request(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.
        '''
        value_ = AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequest(
            unit=unit, value=value
        )

        return typing.cast(None, jsii.invoke(self, "putPerRequest", [value_]))

    @jsii.member(jsii_name="resetIdle")
    def reset_idle(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdle", []))

    @jsii.member(jsii_name="resetPerRequest")
    def reset_per_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPerRequest", []))

    @builtins.property
    @jsii.member(jsii_name="idle")
    def idle(self) -> AppmeshVirtualNodeSpecListenerTimeoutHttpIdleOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerTimeoutHttpIdleOutputReference, jsii.get(self, "idle"))

    @builtins.property
    @jsii.member(jsii_name="perRequest")
    def per_request(
        self,
    ) -> "AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequestOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequestOutputReference", jsii.get(self, "perRequest"))

    @builtins.property
    @jsii.member(jsii_name="idleInput")
    def idle_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttpIdle]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttpIdle], jsii.get(self, "idleInput"))

    @builtins.property
    @jsii.member(jsii_name="perRequestInput")
    def per_request_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequest"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequest"], jsii.get(self, "perRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb705ec69beafca92a7ffd72315dbc94665647ed4219cbad7a33f0ad6412c339)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequest",
    jsii_struct_bases=[],
    name_mapping={"unit": "unit", "value": "value"},
)
class AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequest:
    def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de37204f19629d58df5cee36535bde3f2101c83e0c4b39f1d7651da1c9b1878d)
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "unit": unit,
            "value": value,
        }

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequestOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequestOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__18f50f72e6a7fcd96cab1cb36ff41f6ab6e4039077bae9a7c3b0e56544c853c8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__beb3cd3332a9dccee21a454ea2596fb2ea7f0bd4a5a19dc6c1fe596be87461ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27fcd89cccf418a3f38349a4a202eb8719e5858c06a44144cce48c05f2fbda3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequest]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequest],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f67d06cd5584a510b8382f11ff241476533341cf26949a9fa7d5ac6c51f84f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecListenerTimeoutOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__90754faed3ef40bc8cb54c0581cf39507a2df9216907cee154748f9d3de2cfad)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putGrpc")
    def put_grpc(
        self,
        *,
        idle: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeoutGrpcIdle, typing.Dict[builtins.str, typing.Any]]] = None,
        per_request: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequest, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param idle: idle block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#idle AppmeshVirtualNode#idle}
        :param per_request: per_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#per_request AppmeshVirtualNode#per_request}
        '''
        value = AppmeshVirtualNodeSpecListenerTimeoutGrpc(
            idle=idle, per_request=per_request
        )

        return typing.cast(None, jsii.invoke(self, "putGrpc", [value]))

    @jsii.member(jsii_name="putHttp")
    def put_http(
        self,
        *,
        idle: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeoutHttpIdle, typing.Dict[builtins.str, typing.Any]]] = None,
        per_request: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequest, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param idle: idle block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#idle AppmeshVirtualNode#idle}
        :param per_request: per_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#per_request AppmeshVirtualNode#per_request}
        '''
        value = AppmeshVirtualNodeSpecListenerTimeoutHttp(
            idle=idle, per_request=per_request
        )

        return typing.cast(None, jsii.invoke(self, "putHttp", [value]))

    @jsii.member(jsii_name="putHttp2")
    def put_http2(
        self,
        *,
        idle: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeoutHttp2Idle, typing.Dict[builtins.str, typing.Any]]] = None,
        per_request: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequest, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param idle: idle block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#idle AppmeshVirtualNode#idle}
        :param per_request: per_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#per_request AppmeshVirtualNode#per_request}
        '''
        value = AppmeshVirtualNodeSpecListenerTimeoutHttp2(
            idle=idle, per_request=per_request
        )

        return typing.cast(None, jsii.invoke(self, "putHttp2", [value]))

    @jsii.member(jsii_name="putTcp")
    def put_tcp(
        self,
        *,
        idle: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTimeoutTcpIdle", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param idle: idle block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#idle AppmeshVirtualNode#idle}
        '''
        value = AppmeshVirtualNodeSpecListenerTimeoutTcp(idle=idle)

        return typing.cast(None, jsii.invoke(self, "putTcp", [value]))

    @jsii.member(jsii_name="resetGrpc")
    def reset_grpc(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGrpc", []))

    @jsii.member(jsii_name="resetHttp")
    def reset_http(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttp", []))

    @jsii.member(jsii_name="resetHttp2")
    def reset_http2(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttp2", []))

    @jsii.member(jsii_name="resetTcp")
    def reset_tcp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTcp", []))

    @builtins.property
    @jsii.member(jsii_name="grpc")
    def grpc(self) -> AppmeshVirtualNodeSpecListenerTimeoutGrpcOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerTimeoutGrpcOutputReference, jsii.get(self, "grpc"))

    @builtins.property
    @jsii.member(jsii_name="http")
    def http(self) -> AppmeshVirtualNodeSpecListenerTimeoutHttpOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerTimeoutHttpOutputReference, jsii.get(self, "http"))

    @builtins.property
    @jsii.member(jsii_name="http2")
    def http2(self) -> AppmeshVirtualNodeSpecListenerTimeoutHttp2OutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerTimeoutHttp2OutputReference, jsii.get(self, "http2"))

    @builtins.property
    @jsii.member(jsii_name="tcp")
    def tcp(self) -> "AppmeshVirtualNodeSpecListenerTimeoutTcpOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecListenerTimeoutTcpOutputReference", jsii.get(self, "tcp"))

    @builtins.property
    @jsii.member(jsii_name="grpcInput")
    def grpc_input(self) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutGrpc]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutGrpc], jsii.get(self, "grpcInput"))

    @builtins.property
    @jsii.member(jsii_name="http2Input")
    def http2_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp2]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp2], jsii.get(self, "http2Input"))

    @builtins.property
    @jsii.member(jsii_name="httpInput")
    def http_input(self) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp], jsii.get(self, "httpInput"))

    @builtins.property
    @jsii.member(jsii_name="tcpInput")
    def tcp_input(self) -> typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutTcp"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutTcp"], jsii.get(self, "tcpInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeout]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeout], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeout],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86fb0da156b8a5dffb441b7bf42b4cd9b8ca409d3edb555598b93025853a5642)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutTcp",
    jsii_struct_bases=[],
    name_mapping={"idle": "idle"},
)
class AppmeshVirtualNodeSpecListenerTimeoutTcp:
    def __init__(
        self,
        *,
        idle: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTimeoutTcpIdle", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param idle: idle block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#idle AppmeshVirtualNode#idle}
        '''
        if isinstance(idle, dict):
            idle = AppmeshVirtualNodeSpecListenerTimeoutTcpIdle(**idle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd5fb251e7bca83c1c83bfbdbfce7a2f6b6e9f9478b8286666ad90c866d909a6)
            check_type(argname="argument idle", value=idle, expected_type=type_hints["idle"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if idle is not None:
            self._values["idle"] = idle

    @builtins.property
    def idle(self) -> typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutTcpIdle"]:
        '''idle block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#idle AppmeshVirtualNode#idle}
        '''
        result = self._values.get("idle")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTimeoutTcpIdle"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTimeoutTcp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutTcpIdle",
    jsii_struct_bases=[],
    name_mapping={"unit": "unit", "value": "value"},
)
class AppmeshVirtualNodeSpecListenerTimeoutTcpIdle:
    def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bd575e546026eaaa1aada044e053271d5be7ec4e32f6d86c9762dcb106ad79f)
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "unit": unit,
            "value": value,
        }

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTimeoutTcpIdle(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerTimeoutTcpIdleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutTcpIdleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__19b8417311160af23e373a4721c34749588400fb0a06e28c1691b5e6a31babf2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fb8478c6b1827337b16dd6284f62535fd432d7ce22909030447cda93b5231f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b092fd473bbf8dd9333c6c39cbdee59c0eda6c731e4a57918006915a43f1349f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutTcpIdle]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutTcpIdle], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutTcpIdle],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebcf276bfab623e2086c23d7c19d0c6eed863b76d4cc188585d49d763dec576f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecListenerTimeoutTcpOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTimeoutTcpOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cf6c5c0d025da1ea5b4def659b544c837ae9c65a9ef8e6cf5e40118578965e95)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putIdle")
    def put_idle(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#unit AppmeshVirtualNode#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#value AppmeshVirtualNode#value}.
        '''
        value_ = AppmeshVirtualNodeSpecListenerTimeoutTcpIdle(unit=unit, value=value)

        return typing.cast(None, jsii.invoke(self, "putIdle", [value_]))

    @jsii.member(jsii_name="resetIdle")
    def reset_idle(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdle", []))

    @builtins.property
    @jsii.member(jsii_name="idle")
    def idle(self) -> AppmeshVirtualNodeSpecListenerTimeoutTcpIdleOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerTimeoutTcpIdleOutputReference, jsii.get(self, "idle"))

    @builtins.property
    @jsii.member(jsii_name="idleInput")
    def idle_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutTcpIdle]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutTcpIdle], jsii.get(self, "idleInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutTcp]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutTcp], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutTcp],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8c9deb5b9bbbdf3944d78b300d2f39ee347c012be9e1d63815acb8d5c157157)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTls",
    jsii_struct_bases=[],
    name_mapping={
        "certificate": "certificate",
        "mode": "mode",
        "validation": "validation",
    },
)
class AppmeshVirtualNodeSpecListenerTls:
    def __init__(
        self,
        *,
        certificate: typing.Union["AppmeshVirtualNodeSpecListenerTlsCertificate", typing.Dict[builtins.str, typing.Any]],
        mode: builtins.str,
        validation: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTlsValidation", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param certificate: certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate AppmeshVirtualNode#certificate}
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#mode AppmeshVirtualNode#mode}.
        :param validation: validation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#validation AppmeshVirtualNode#validation}
        '''
        if isinstance(certificate, dict):
            certificate = AppmeshVirtualNodeSpecListenerTlsCertificate(**certificate)
        if isinstance(validation, dict):
            validation = AppmeshVirtualNodeSpecListenerTlsValidation(**validation)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fe04259c75b8de83b8b9cef42026fa9473d79458739a64c8da5253eda93ce49)
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument validation", value=validation, expected_type=type_hints["validation"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate": certificate,
            "mode": mode,
        }
        if validation is not None:
            self._values["validation"] = validation

    @builtins.property
    def certificate(self) -> "AppmeshVirtualNodeSpecListenerTlsCertificate":
        '''certificate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate AppmeshVirtualNode#certificate}
        '''
        result = self._values.get("certificate")
        assert result is not None, "Required property 'certificate' is missing"
        return typing.cast("AppmeshVirtualNodeSpecListenerTlsCertificate", result)

    @builtins.property
    def mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#mode AppmeshVirtualNode#mode}.'''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def validation(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerTlsValidation"]:
        '''validation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#validation AppmeshVirtualNode#validation}
        '''
        result = self._values.get("validation")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTlsValidation"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsCertificate",
    jsii_struct_bases=[],
    name_mapping={"acm": "acm", "file": "file", "sds": "sds"},
)
class AppmeshVirtualNodeSpecListenerTlsCertificate:
    def __init__(
        self,
        *,
        acm: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTlsCertificateAcm", typing.Dict[builtins.str, typing.Any]]] = None,
        file: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTlsCertificateFile", typing.Dict[builtins.str, typing.Any]]] = None,
        sds: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTlsCertificateSds", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param acm: acm block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#acm AppmeshVirtualNode#acm}
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        :param sds: sds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#sds AppmeshVirtualNode#sds}
        '''
        if isinstance(acm, dict):
            acm = AppmeshVirtualNodeSpecListenerTlsCertificateAcm(**acm)
        if isinstance(file, dict):
            file = AppmeshVirtualNodeSpecListenerTlsCertificateFile(**file)
        if isinstance(sds, dict):
            sds = AppmeshVirtualNodeSpecListenerTlsCertificateSds(**sds)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e42dd54ccba59470424d9add59022ab897a77ddc5a623cb72c8795475120ec51)
            check_type(argname="argument acm", value=acm, expected_type=type_hints["acm"])
            check_type(argname="argument file", value=file, expected_type=type_hints["file"])
            check_type(argname="argument sds", value=sds, expected_type=type_hints["sds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if acm is not None:
            self._values["acm"] = acm
        if file is not None:
            self._values["file"] = file
        if sds is not None:
            self._values["sds"] = sds

    @builtins.property
    def acm(self) -> typing.Optional["AppmeshVirtualNodeSpecListenerTlsCertificateAcm"]:
        '''acm block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#acm AppmeshVirtualNode#acm}
        '''
        result = self._values.get("acm")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTlsCertificateAcm"], result)

    @builtins.property
    def file(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerTlsCertificateFile"]:
        '''file block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        '''
        result = self._values.get("file")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTlsCertificateFile"], result)

    @builtins.property
    def sds(self) -> typing.Optional["AppmeshVirtualNodeSpecListenerTlsCertificateSds"]:
        '''sds block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#sds AppmeshVirtualNode#sds}
        '''
        result = self._values.get("sds")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTlsCertificateSds"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTlsCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsCertificateAcm",
    jsii_struct_bases=[],
    name_mapping={"certificate_arn": "certificateArn"},
)
class AppmeshVirtualNodeSpecListenerTlsCertificateAcm:
    def __init__(self, *, certificate_arn: builtins.str) -> None:
        '''
        :param certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_arn AppmeshVirtualNode#certificate_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__954c93235e3a742f6b4cc1799f515332a776adbf49c198ed8003e8f2e3e8d660)
            check_type(argname="argument certificate_arn", value=certificate_arn, expected_type=type_hints["certificate_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_arn": certificate_arn,
        }

    @builtins.property
    def certificate_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_arn AppmeshVirtualNode#certificate_arn}.'''
        result = self._values.get("certificate_arn")
        assert result is not None, "Required property 'certificate_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTlsCertificateAcm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerTlsCertificateAcmOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsCertificateAcmOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9a4a0de40851a8af3cab79e7d90c5d914471ec94b6350c4134b746bb90a1a1cd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="certificateArnInput")
    def certificate_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateArnInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateArn")
    def certificate_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateArn"))

    @certificate_arn.setter
    def certificate_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4098c684b5110e10821b9dd2daeef518456fb04738dfd879d38e01b02b1e0cac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificateAcm]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificateAcm], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificateAcm],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2790a97dd2e1c85cb76d68c087a058a84c969cc447cd8cd5fffed28139e7239)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsCertificateFile",
    jsii_struct_bases=[],
    name_mapping={
        "certificate_chain": "certificateChain",
        "private_key": "privateKey",
    },
)
class AppmeshVirtualNodeSpecListenerTlsCertificateFile:
    def __init__(
        self,
        *,
        certificate_chain: builtins.str,
        private_key: builtins.str,
    ) -> None:
        '''
        :param certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_chain AppmeshVirtualNode#certificate_chain}.
        :param private_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#private_key AppmeshVirtualNode#private_key}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fc0a977e0dfdbc89e00bec39e6038440de97175f055b77a442584c001eb7cbc)
            check_type(argname="argument certificate_chain", value=certificate_chain, expected_type=type_hints["certificate_chain"])
            check_type(argname="argument private_key", value=private_key, expected_type=type_hints["private_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_chain": certificate_chain,
            "private_key": private_key,
        }

    @builtins.property
    def certificate_chain(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_chain AppmeshVirtualNode#certificate_chain}.'''
        result = self._values.get("certificate_chain")
        assert result is not None, "Required property 'certificate_chain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def private_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#private_key AppmeshVirtualNode#private_key}.'''
        result = self._values.get("private_key")
        assert result is not None, "Required property 'private_key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTlsCertificateFile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerTlsCertificateFileOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsCertificateFileOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bc545b3ee554b2c56fd383fb531a4e15c40aba9bd4ff21ee170de52b431363fa)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="certificateChainInput")
    def certificate_chain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateChainInput"))

    @builtins.property
    @jsii.member(jsii_name="privateKeyInput")
    def private_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateChain")
    def certificate_chain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateChain"))

    @certificate_chain.setter
    def certificate_chain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db0d53a7ccd1fc8d8cf3144c147ac98c61a09756878c3eaf963e2c8c43b5088d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateChain", value)

    @builtins.property
    @jsii.member(jsii_name="privateKey")
    def private_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateKey"))

    @private_key.setter
    def private_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adeb792498c1ae1c6b9917fe900ce74e5ec68fbf96a4a7250253ba283160e765)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificateFile]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificateFile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificateFile],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e4b167083b810b87e227e3229bbfe050df19116f86a2a24e2a6705c708fa516)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecListenerTlsCertificateOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsCertificateOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ebb75997ef10ff8aadb871bcabf70c1dad68ea1f13f0f5122f89a403eab43392)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAcm")
    def put_acm(self, *, certificate_arn: builtins.str) -> None:
        '''
        :param certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_arn AppmeshVirtualNode#certificate_arn}.
        '''
        value = AppmeshVirtualNodeSpecListenerTlsCertificateAcm(
            certificate_arn=certificate_arn
        )

        return typing.cast(None, jsii.invoke(self, "putAcm", [value]))

    @jsii.member(jsii_name="putFile")
    def put_file(
        self,
        *,
        certificate_chain: builtins.str,
        private_key: builtins.str,
    ) -> None:
        '''
        :param certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_chain AppmeshVirtualNode#certificate_chain}.
        :param private_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#private_key AppmeshVirtualNode#private_key}.
        '''
        value = AppmeshVirtualNodeSpecListenerTlsCertificateFile(
            certificate_chain=certificate_chain, private_key=private_key
        )

        return typing.cast(None, jsii.invoke(self, "putFile", [value]))

    @jsii.member(jsii_name="putSds")
    def put_sds(self, *, secret_name: builtins.str) -> None:
        '''
        :param secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#secret_name AppmeshVirtualNode#secret_name}.
        '''
        value = AppmeshVirtualNodeSpecListenerTlsCertificateSds(
            secret_name=secret_name
        )

        return typing.cast(None, jsii.invoke(self, "putSds", [value]))

    @jsii.member(jsii_name="resetAcm")
    def reset_acm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcm", []))

    @jsii.member(jsii_name="resetFile")
    def reset_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFile", []))

    @jsii.member(jsii_name="resetSds")
    def reset_sds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSds", []))

    @builtins.property
    @jsii.member(jsii_name="acm")
    def acm(self) -> AppmeshVirtualNodeSpecListenerTlsCertificateAcmOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerTlsCertificateAcmOutputReference, jsii.get(self, "acm"))

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(self) -> AppmeshVirtualNodeSpecListenerTlsCertificateFileOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerTlsCertificateFileOutputReference, jsii.get(self, "file"))

    @builtins.property
    @jsii.member(jsii_name="sds")
    def sds(self) -> "AppmeshVirtualNodeSpecListenerTlsCertificateSdsOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecListenerTlsCertificateSdsOutputReference", jsii.get(self, "sds"))

    @builtins.property
    @jsii.member(jsii_name="acmInput")
    def acm_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificateAcm]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificateAcm], jsii.get(self, "acmInput"))

    @builtins.property
    @jsii.member(jsii_name="fileInput")
    def file_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificateFile]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificateFile], jsii.get(self, "fileInput"))

    @builtins.property
    @jsii.member(jsii_name="sdsInput")
    def sds_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerTlsCertificateSds"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTlsCertificateSds"], jsii.get(self, "sdsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificate]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificate],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3af4739fd4ca955fec46283aa505635d428c1fedf6d22e17cbe985a957e0f6a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsCertificateSds",
    jsii_struct_bases=[],
    name_mapping={"secret_name": "secretName"},
)
class AppmeshVirtualNodeSpecListenerTlsCertificateSds:
    def __init__(self, *, secret_name: builtins.str) -> None:
        '''
        :param secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#secret_name AppmeshVirtualNode#secret_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3e56a0a1e0cba40719df7987ee2b40a6f3ca6394b119c2a9ee2008c071ba5fe)
            check_type(argname="argument secret_name", value=secret_name, expected_type=type_hints["secret_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "secret_name": secret_name,
        }

    @builtins.property
    def secret_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#secret_name AppmeshVirtualNode#secret_name}.'''
        result = self._values.get("secret_name")
        assert result is not None, "Required property 'secret_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTlsCertificateSds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerTlsCertificateSdsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsCertificateSdsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9d2fb404acc44640f80fadfefd8f5f989f2b0da68dbb59dee7b09017d77f1ea6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="secretNameInput")
    def secret_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretNameInput"))

    @builtins.property
    @jsii.member(jsii_name="secretName")
    def secret_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretName"))

    @secret_name.setter
    def secret_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58deef79cdb7bcbc2d98ad775d7033880fd18c56a19064d1396052c174b8dea9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificateSds]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificateSds], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificateSds],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f90e965bc6a408add9bfea5a89b4f77bf4753c8d7c999d780ac478587e0bb6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecListenerTlsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__af11cd6c2de43dcf0df038654cc123a9fd3db21606321e4384dbd37c50ca30f4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCertificate")
    def put_certificate(
        self,
        *,
        acm: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTlsCertificateAcm, typing.Dict[builtins.str, typing.Any]]] = None,
        file: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTlsCertificateFile, typing.Dict[builtins.str, typing.Any]]] = None,
        sds: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTlsCertificateSds, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param acm: acm block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#acm AppmeshVirtualNode#acm}
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        :param sds: sds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#sds AppmeshVirtualNode#sds}
        '''
        value = AppmeshVirtualNodeSpecListenerTlsCertificate(
            acm=acm, file=file, sds=sds
        )

        return typing.cast(None, jsii.invoke(self, "putCertificate", [value]))

    @jsii.member(jsii_name="putValidation")
    def put_validation(
        self,
        *,
        trust: typing.Union["AppmeshVirtualNodeSpecListenerTlsValidationTrust", typing.Dict[builtins.str, typing.Any]],
        subject_alternative_names: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNames", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param trust: trust block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#trust AppmeshVirtualNode#trust}
        :param subject_alternative_names: subject_alternative_names block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#subject_alternative_names AppmeshVirtualNode#subject_alternative_names}
        '''
        value = AppmeshVirtualNodeSpecListenerTlsValidation(
            trust=trust, subject_alternative_names=subject_alternative_names
        )

        return typing.cast(None, jsii.invoke(self, "putValidation", [value]))

    @jsii.member(jsii_name="resetValidation")
    def reset_validation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValidation", []))

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(
        self,
    ) -> AppmeshVirtualNodeSpecListenerTlsCertificateOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerTlsCertificateOutputReference, jsii.get(self, "certificate"))

    @builtins.property
    @jsii.member(jsii_name="validation")
    def validation(
        self,
    ) -> "AppmeshVirtualNodeSpecListenerTlsValidationOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecListenerTlsValidationOutputReference", jsii.get(self, "validation"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificate]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificate], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="validationInput")
    def validation_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerTlsValidation"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTlsValidation"], jsii.get(self, "validationInput"))

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7c081721cf99e58bec57ec52c619db99eb66a19508f996531154c6790a7780e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshVirtualNodeSpecListenerTls]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTls], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTls],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2345c49236266c61bdbaf96ca9187e218f51985232938b7c07636aa88fb388e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsValidation",
    jsii_struct_bases=[],
    name_mapping={
        "trust": "trust",
        "subject_alternative_names": "subjectAlternativeNames",
    },
)
class AppmeshVirtualNodeSpecListenerTlsValidation:
    def __init__(
        self,
        *,
        trust: typing.Union["AppmeshVirtualNodeSpecListenerTlsValidationTrust", typing.Dict[builtins.str, typing.Any]],
        subject_alternative_names: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNames", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param trust: trust block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#trust AppmeshVirtualNode#trust}
        :param subject_alternative_names: subject_alternative_names block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#subject_alternative_names AppmeshVirtualNode#subject_alternative_names}
        '''
        if isinstance(trust, dict):
            trust = AppmeshVirtualNodeSpecListenerTlsValidationTrust(**trust)
        if isinstance(subject_alternative_names, dict):
            subject_alternative_names = AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNames(**subject_alternative_names)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8879904a4ec0d347d3cacdfc5cbdfb323c0a44dfe6dc67cf2c228c2ece5104a2)
            check_type(argname="argument trust", value=trust, expected_type=type_hints["trust"])
            check_type(argname="argument subject_alternative_names", value=subject_alternative_names, expected_type=type_hints["subject_alternative_names"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "trust": trust,
        }
        if subject_alternative_names is not None:
            self._values["subject_alternative_names"] = subject_alternative_names

    @builtins.property
    def trust(self) -> "AppmeshVirtualNodeSpecListenerTlsValidationTrust":
        '''trust block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#trust AppmeshVirtualNode#trust}
        '''
        result = self._values.get("trust")
        assert result is not None, "Required property 'trust' is missing"
        return typing.cast("AppmeshVirtualNodeSpecListenerTlsValidationTrust", result)

    @builtins.property
    def subject_alternative_names(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNames"]:
        '''subject_alternative_names block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#subject_alternative_names AppmeshVirtualNode#subject_alternative_names}
        '''
        result = self._values.get("subject_alternative_names")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNames"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTlsValidation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerTlsValidationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsValidationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__893eb293bb4a18f1d02101912dcb4d56f2a0b2bfb71b190a1f4af93723a18f95)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSubjectAlternativeNames")
    def put_subject_alternative_names(
        self,
        *,
        match: typing.Union["AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatch", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#match AppmeshVirtualNode#match}
        '''
        value = AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNames(
            match=match
        )

        return typing.cast(None, jsii.invoke(self, "putSubjectAlternativeNames", [value]))

    @jsii.member(jsii_name="putTrust")
    def put_trust(
        self,
        *,
        file: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTlsValidationTrustFile", typing.Dict[builtins.str, typing.Any]]] = None,
        sds: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTlsValidationTrustSds", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        :param sds: sds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#sds AppmeshVirtualNode#sds}
        '''
        value = AppmeshVirtualNodeSpecListenerTlsValidationTrust(file=file, sds=sds)

        return typing.cast(None, jsii.invoke(self, "putTrust", [value]))

    @jsii.member(jsii_name="resetSubjectAlternativeNames")
    def reset_subject_alternative_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubjectAlternativeNames", []))

    @builtins.property
    @jsii.member(jsii_name="subjectAlternativeNames")
    def subject_alternative_names(
        self,
    ) -> "AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesOutputReference", jsii.get(self, "subjectAlternativeNames"))

    @builtins.property
    @jsii.member(jsii_name="trust")
    def trust(
        self,
    ) -> "AppmeshVirtualNodeSpecListenerTlsValidationTrustOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecListenerTlsValidationTrustOutputReference", jsii.get(self, "trust"))

    @builtins.property
    @jsii.member(jsii_name="subjectAlternativeNamesInput")
    def subject_alternative_names_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNames"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNames"], jsii.get(self, "subjectAlternativeNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="trustInput")
    def trust_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerTlsValidationTrust"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTlsValidationTrust"], jsii.get(self, "trustInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidation]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bde2f61d6b2f7c035bf06a6f646c6761aa7e1730da15574e0a6819510ebaa57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNames",
    jsii_struct_bases=[],
    name_mapping={"match": "match"},
)
class AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNames:
    def __init__(
        self,
        *,
        match: typing.Union["AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatch", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#match AppmeshVirtualNode#match}
        '''
        if isinstance(match, dict):
            match = AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatch(**match)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6aada447dfdb0819a302cdeae484a7b114df81d3b1cb22b7ddd7c00ec8c041d)
            check_type(argname="argument match", value=match, expected_type=type_hints["match"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "match": match,
        }

    @builtins.property
    def match(
        self,
    ) -> "AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatch":
        '''match block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#match AppmeshVirtualNode#match}
        '''
        result = self._values.get("match")
        assert result is not None, "Required property 'match' is missing"
        return typing.cast("AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatch", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNames(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatch",
    jsii_struct_bases=[],
    name_mapping={"exact": "exact"},
)
class AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatch:
    def __init__(self, *, exact: typing.Sequence[builtins.str]) -> None:
        '''
        :param exact: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#exact AppmeshVirtualNode#exact}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fe865528d320beaece5a85c0009a2005f941c322266a774fc021cb57485e93a)
            check_type(argname="argument exact", value=exact, expected_type=type_hints["exact"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "exact": exact,
        }

    @builtins.property
    def exact(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#exact AppmeshVirtualNode#exact}.'''
        result = self._values.get("exact")
        assert result is not None, "Required property 'exact' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatchOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatchOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c60984aab7a95b9d846479dd4cf265c9450b89018f60db196c2a7df6fa04e22c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="exactInput")
    def exact_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "exactInput"))

    @builtins.property
    @jsii.member(jsii_name="exact")
    def exact(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exact"))

    @exact.setter
    def exact(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42e30a0756c76f533f0d1c54587516e2c9bcfbaa3713d4a4b30846d68ea58218)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exact", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatch]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatch],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21b7fec44cf3b6721ed0add6e9bf59c51904a924f9b8d1764b992dd3d67c21fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__271fdc2d95a1d8e6cd63b8cbab4513586e844b56369d5e24dafeee39fd4d3b4b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMatch")
    def put_match(self, *, exact: typing.Sequence[builtins.str]) -> None:
        '''
        :param exact: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#exact AppmeshVirtualNode#exact}.
        '''
        value = AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatch(
            exact=exact
        )

        return typing.cast(None, jsii.invoke(self, "putMatch", [value]))

    @builtins.property
    @jsii.member(jsii_name="match")
    def match(
        self,
    ) -> AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatchOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatchOutputReference, jsii.get(self, "match"))

    @builtins.property
    @jsii.member(jsii_name="matchInput")
    def match_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatch]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatch], jsii.get(self, "matchInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNames]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNames], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNames],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6cff3ca8f3b4916245e817c5f9b89ccae3b7b10930d7ebb1c028048fbbfaa81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsValidationTrust",
    jsii_struct_bases=[],
    name_mapping={"file": "file", "sds": "sds"},
)
class AppmeshVirtualNodeSpecListenerTlsValidationTrust:
    def __init__(
        self,
        *,
        file: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTlsValidationTrustFile", typing.Dict[builtins.str, typing.Any]]] = None,
        sds: typing.Optional[typing.Union["AppmeshVirtualNodeSpecListenerTlsValidationTrustSds", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        :param sds: sds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#sds AppmeshVirtualNode#sds}
        '''
        if isinstance(file, dict):
            file = AppmeshVirtualNodeSpecListenerTlsValidationTrustFile(**file)
        if isinstance(sds, dict):
            sds = AppmeshVirtualNodeSpecListenerTlsValidationTrustSds(**sds)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96ce88dc38b06c41c06120cffb7219dbf367cd2fb2589396a51a3f8b482d809e)
            check_type(argname="argument file", value=file, expected_type=type_hints["file"])
            check_type(argname="argument sds", value=sds, expected_type=type_hints["sds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if file is not None:
            self._values["file"] = file
        if sds is not None:
            self._values["sds"] = sds

    @builtins.property
    def file(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerTlsValidationTrustFile"]:
        '''file block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        '''
        result = self._values.get("file")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTlsValidationTrustFile"], result)

    @builtins.property
    def sds(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerTlsValidationTrustSds"]:
        '''sds block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#sds AppmeshVirtualNode#sds}
        '''
        result = self._values.get("sds")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTlsValidationTrustSds"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTlsValidationTrust(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsValidationTrustFile",
    jsii_struct_bases=[],
    name_mapping={"certificate_chain": "certificateChain"},
)
class AppmeshVirtualNodeSpecListenerTlsValidationTrustFile:
    def __init__(self, *, certificate_chain: builtins.str) -> None:
        '''
        :param certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_chain AppmeshVirtualNode#certificate_chain}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5371d227c3248fe1187d5ea926fcd73839945f54c4553f959be5d1da36f48715)
            check_type(argname="argument certificate_chain", value=certificate_chain, expected_type=type_hints["certificate_chain"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_chain": certificate_chain,
        }

    @builtins.property
    def certificate_chain(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_chain AppmeshVirtualNode#certificate_chain}.'''
        result = self._values.get("certificate_chain")
        assert result is not None, "Required property 'certificate_chain' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTlsValidationTrustFile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerTlsValidationTrustFileOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsValidationTrustFileOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6a64829c69cdfffe41a57949b95313bbf652a52d99f244bd5be2a01b6da4bddd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="certificateChainInput")
    def certificate_chain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateChainInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateChain")
    def certificate_chain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateChain"))

    @certificate_chain.setter
    def certificate_chain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c1e2418bd69904577e5be41dabf46fd8b8230535f18b54c9e1eb73515d685b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateChain", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationTrustFile]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationTrustFile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationTrustFile],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57cc8c01f0a2d2a12489a9d42a55f2a51014623365c8157a6146fbc47c565027)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecListenerTlsValidationTrustOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsValidationTrustOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0cd18e1836ada60ca79725c835d931966bb8a21fae1549a7fe3a4ca661fe2aba)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putFile")
    def put_file(self, *, certificate_chain: builtins.str) -> None:
        '''
        :param certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#certificate_chain AppmeshVirtualNode#certificate_chain}.
        '''
        value = AppmeshVirtualNodeSpecListenerTlsValidationTrustFile(
            certificate_chain=certificate_chain
        )

        return typing.cast(None, jsii.invoke(self, "putFile", [value]))

    @jsii.member(jsii_name="putSds")
    def put_sds(self, *, secret_name: builtins.str) -> None:
        '''
        :param secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#secret_name AppmeshVirtualNode#secret_name}.
        '''
        value = AppmeshVirtualNodeSpecListenerTlsValidationTrustSds(
            secret_name=secret_name
        )

        return typing.cast(None, jsii.invoke(self, "putSds", [value]))

    @jsii.member(jsii_name="resetFile")
    def reset_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFile", []))

    @jsii.member(jsii_name="resetSds")
    def reset_sds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSds", []))

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(
        self,
    ) -> AppmeshVirtualNodeSpecListenerTlsValidationTrustFileOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerTlsValidationTrustFileOutputReference, jsii.get(self, "file"))

    @builtins.property
    @jsii.member(jsii_name="sds")
    def sds(
        self,
    ) -> "AppmeshVirtualNodeSpecListenerTlsValidationTrustSdsOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecListenerTlsValidationTrustSdsOutputReference", jsii.get(self, "sds"))

    @builtins.property
    @jsii.member(jsii_name="fileInput")
    def file_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationTrustFile]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationTrustFile], jsii.get(self, "fileInput"))

    @builtins.property
    @jsii.member(jsii_name="sdsInput")
    def sds_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecListenerTlsValidationTrustSds"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecListenerTlsValidationTrustSds"], jsii.get(self, "sdsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationTrust]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationTrust], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationTrust],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1ed0dd0c64af2399c771ee96d99d0fe400d8e72e0306d256cfa639e7c3a86e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsValidationTrustSds",
    jsii_struct_bases=[],
    name_mapping={"secret_name": "secretName"},
)
class AppmeshVirtualNodeSpecListenerTlsValidationTrustSds:
    def __init__(self, *, secret_name: builtins.str) -> None:
        '''
        :param secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#secret_name AppmeshVirtualNode#secret_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1ac5f6e72f9cef7929a164d1432886c9ede3a9a0a2fb2344db44d946276d238)
            check_type(argname="argument secret_name", value=secret_name, expected_type=type_hints["secret_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "secret_name": secret_name,
        }

    @builtins.property
    def secret_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#secret_name AppmeshVirtualNode#secret_name}.'''
        result = self._values.get("secret_name")
        assert result is not None, "Required property 'secret_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecListenerTlsValidationTrustSds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecListenerTlsValidationTrustSdsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecListenerTlsValidationTrustSdsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__40f96b814ceb7a3c26a1d2ee22f98c651dc563f1e669b8fa3b793982fa9f4435)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="secretNameInput")
    def secret_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretNameInput"))

    @builtins.property
    @jsii.member(jsii_name="secretName")
    def secret_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretName"))

    @secret_name.setter
    def secret_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee4bc1c94a7ced72479043dbc50413e13b5c277284add994bd2d38a9cf35f2df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationTrustSds]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationTrustSds], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationTrustSds],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__481f120d2d76802f1c235a4f368f5d92e11bab29105817ebae9d00ddece1d55a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecLogging",
    jsii_struct_bases=[],
    name_mapping={"access_log": "accessLog"},
)
class AppmeshVirtualNodeSpecLogging:
    def __init__(
        self,
        *,
        access_log: typing.Optional[typing.Union["AppmeshVirtualNodeSpecLoggingAccessLog", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param access_log: access_log block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#access_log AppmeshVirtualNode#access_log}
        '''
        if isinstance(access_log, dict):
            access_log = AppmeshVirtualNodeSpecLoggingAccessLog(**access_log)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f8ca2aea8d6f77b59580566af3a13fcc509efff59087729befc6e265fc27192)
            check_type(argname="argument access_log", value=access_log, expected_type=type_hints["access_log"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if access_log is not None:
            self._values["access_log"] = access_log

    @builtins.property
    def access_log(self) -> typing.Optional["AppmeshVirtualNodeSpecLoggingAccessLog"]:
        '''access_log block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#access_log AppmeshVirtualNode#access_log}
        '''
        result = self._values.get("access_log")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecLoggingAccessLog"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecLogging(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecLoggingAccessLog",
    jsii_struct_bases=[],
    name_mapping={"file": "file"},
)
class AppmeshVirtualNodeSpecLoggingAccessLog:
    def __init__(
        self,
        *,
        file: typing.Optional[typing.Union["AppmeshVirtualNodeSpecLoggingAccessLogFile", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        '''
        if isinstance(file, dict):
            file = AppmeshVirtualNodeSpecLoggingAccessLogFile(**file)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb86acce4a2fbcbeae42ff0019bce0be64e0bae961dca2a920fb50dedeabd48a)
            check_type(argname="argument file", value=file, expected_type=type_hints["file"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if file is not None:
            self._values["file"] = file

    @builtins.property
    def file(self) -> typing.Optional["AppmeshVirtualNodeSpecLoggingAccessLogFile"]:
        '''file block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        '''
        result = self._values.get("file")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecLoggingAccessLogFile"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecLoggingAccessLog(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecLoggingAccessLogFile",
    jsii_struct_bases=[],
    name_mapping={"path": "path"},
)
class AppmeshVirtualNodeSpecLoggingAccessLogFile:
    def __init__(self, *, path: builtins.str) -> None:
        '''
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#path AppmeshVirtualNode#path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be71a767791532003da7d81d97bc28d18c7f33f8661dbaed9130a845c64537fb)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "path": path,
        }

    @builtins.property
    def path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#path AppmeshVirtualNode#path}.'''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecLoggingAccessLogFile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecLoggingAccessLogFileOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecLoggingAccessLogFileOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e1ed98743bc06b687dcb1e437469f885b159e9098cecf166b51dbfb49a31b196)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7f42cb9b0a103c2b36eb943838ca9691917af5ee884c668879bafc40b9c73df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecLoggingAccessLogFile]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecLoggingAccessLogFile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecLoggingAccessLogFile],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8adb7285f4aab91bd31f2918881cc016b24becd9922c7b71a7cf9546793feca2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecLoggingAccessLogOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecLoggingAccessLogOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__44aaf70ce87958617409dd6b0ad993ffbf9f6f4092fdd82adb825f58ed5c10e4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putFile")
    def put_file(self, *, path: builtins.str) -> None:
        '''
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#path AppmeshVirtualNode#path}.
        '''
        value = AppmeshVirtualNodeSpecLoggingAccessLogFile(path=path)

        return typing.cast(None, jsii.invoke(self, "putFile", [value]))

    @jsii.member(jsii_name="resetFile")
    def reset_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFile", []))

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(self) -> AppmeshVirtualNodeSpecLoggingAccessLogFileOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecLoggingAccessLogFileOutputReference, jsii.get(self, "file"))

    @builtins.property
    @jsii.member(jsii_name="fileInput")
    def file_input(self) -> typing.Optional[AppmeshVirtualNodeSpecLoggingAccessLogFile]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecLoggingAccessLogFile], jsii.get(self, "fileInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshVirtualNodeSpecLoggingAccessLog]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecLoggingAccessLog], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecLoggingAccessLog],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a211a79e2c9f0261358ea4603cf2eccdb40f454701fa54faa37fd21249d5a47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecLoggingOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecLoggingOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__311534c9e3188fc760980cd8e0a28ec9461e097cdcc64f638b36f7623d3c9b8f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAccessLog")
    def put_access_log(
        self,
        *,
        file: typing.Optional[typing.Union[AppmeshVirtualNodeSpecLoggingAccessLogFile, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#file AppmeshVirtualNode#file}
        '''
        value = AppmeshVirtualNodeSpecLoggingAccessLog(file=file)

        return typing.cast(None, jsii.invoke(self, "putAccessLog", [value]))

    @jsii.member(jsii_name="resetAccessLog")
    def reset_access_log(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessLog", []))

    @builtins.property
    @jsii.member(jsii_name="accessLog")
    def access_log(self) -> AppmeshVirtualNodeSpecLoggingAccessLogOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecLoggingAccessLogOutputReference, jsii.get(self, "accessLog"))

    @builtins.property
    @jsii.member(jsii_name="accessLogInput")
    def access_log_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecLoggingAccessLog]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecLoggingAccessLog], jsii.get(self, "accessLogInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshVirtualNodeSpecLogging]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecLogging], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecLogging],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b6ff9a621b19824ee0ec0ee2d3b8d9a7d48aa22416e4618f2ae453c4040cef1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b25f89bc7a598744778cc818353c1977f96b33b53276e13f8a67f459fece3ad0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBackend")
    def put_backend(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppmeshVirtualNodeSpecBackend, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f7da9e3d273c6ae30de318e179b31a62637359a00f128fa135461599c6b4e68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBackend", [value]))

    @jsii.member(jsii_name="putBackendDefaults")
    def put_backend_defaults(
        self,
        *,
        client_policy: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendDefaultsClientPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param client_policy: client_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#client_policy AppmeshVirtualNode#client_policy}
        '''
        value = AppmeshVirtualNodeSpecBackendDefaults(client_policy=client_policy)

        return typing.cast(None, jsii.invoke(self, "putBackendDefaults", [value]))

    @jsii.member(jsii_name="putListener")
    def put_listener(
        self,
        *,
        port_mapping: typing.Union[AppmeshVirtualNodeSpecListenerPortMapping, typing.Dict[builtins.str, typing.Any]],
        connection_pool: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerConnectionPool, typing.Dict[builtins.str, typing.Any]]] = None,
        health_check: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerHealthCheck, typing.Dict[builtins.str, typing.Any]]] = None,
        outlier_detection: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerOutlierDetection, typing.Dict[builtins.str, typing.Any]]] = None,
        timeout: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeout, typing.Dict[builtins.str, typing.Any]]] = None,
        tls: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTls, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param port_mapping: port_mapping block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#port_mapping AppmeshVirtualNode#port_mapping}
        :param connection_pool: connection_pool block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#connection_pool AppmeshVirtualNode#connection_pool}
        :param health_check: health_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#health_check AppmeshVirtualNode#health_check}
        :param outlier_detection: outlier_detection block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#outlier_detection AppmeshVirtualNode#outlier_detection}
        :param timeout: timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#timeout AppmeshVirtualNode#timeout}
        :param tls: tls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#tls AppmeshVirtualNode#tls}
        '''
        value = AppmeshVirtualNodeSpecListener(
            port_mapping=port_mapping,
            connection_pool=connection_pool,
            health_check=health_check,
            outlier_detection=outlier_detection,
            timeout=timeout,
            tls=tls,
        )

        return typing.cast(None, jsii.invoke(self, "putListener", [value]))

    @jsii.member(jsii_name="putLogging")
    def put_logging(
        self,
        *,
        access_log: typing.Optional[typing.Union[AppmeshVirtualNodeSpecLoggingAccessLog, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param access_log: access_log block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#access_log AppmeshVirtualNode#access_log}
        '''
        value = AppmeshVirtualNodeSpecLogging(access_log=access_log)

        return typing.cast(None, jsii.invoke(self, "putLogging", [value]))

    @jsii.member(jsii_name="putServiceDiscovery")
    def put_service_discovery(
        self,
        *,
        aws_cloud_map: typing.Optional[typing.Union["AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMap", typing.Dict[builtins.str, typing.Any]]] = None,
        dns: typing.Optional[typing.Union["AppmeshVirtualNodeSpecServiceDiscoveryDns", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param aws_cloud_map: aws_cloud_map block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#aws_cloud_map AppmeshVirtualNode#aws_cloud_map}
        :param dns: dns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#dns AppmeshVirtualNode#dns}
        '''
        value = AppmeshVirtualNodeSpecServiceDiscovery(
            aws_cloud_map=aws_cloud_map, dns=dns
        )

        return typing.cast(None, jsii.invoke(self, "putServiceDiscovery", [value]))

    @jsii.member(jsii_name="resetBackend")
    def reset_backend(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackend", []))

    @jsii.member(jsii_name="resetBackendDefaults")
    def reset_backend_defaults(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackendDefaults", []))

    @jsii.member(jsii_name="resetListener")
    def reset_listener(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetListener", []))

    @jsii.member(jsii_name="resetLogging")
    def reset_logging(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogging", []))

    @jsii.member(jsii_name="resetServiceDiscovery")
    def reset_service_discovery(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceDiscovery", []))

    @builtins.property
    @jsii.member(jsii_name="backend")
    def backend(self) -> AppmeshVirtualNodeSpecBackendList:
        return typing.cast(AppmeshVirtualNodeSpecBackendList, jsii.get(self, "backend"))

    @builtins.property
    @jsii.member(jsii_name="backendDefaults")
    def backend_defaults(self) -> AppmeshVirtualNodeSpecBackendDefaultsOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecBackendDefaultsOutputReference, jsii.get(self, "backendDefaults"))

    @builtins.property
    @jsii.member(jsii_name="listener")
    def listener(self) -> AppmeshVirtualNodeSpecListenerOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecListenerOutputReference, jsii.get(self, "listener"))

    @builtins.property
    @jsii.member(jsii_name="logging")
    def logging(self) -> AppmeshVirtualNodeSpecLoggingOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecLoggingOutputReference, jsii.get(self, "logging"))

    @builtins.property
    @jsii.member(jsii_name="serviceDiscovery")
    def service_discovery(
        self,
    ) -> "AppmeshVirtualNodeSpecServiceDiscoveryOutputReference":
        return typing.cast("AppmeshVirtualNodeSpecServiceDiscoveryOutputReference", jsii.get(self, "serviceDiscovery"))

    @builtins.property
    @jsii.member(jsii_name="backendDefaultsInput")
    def backend_defaults_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecBackendDefaults]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecBackendDefaults], jsii.get(self, "backendDefaultsInput"))

    @builtins.property
    @jsii.member(jsii_name="backendInput")
    def backend_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshVirtualNodeSpecBackend]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshVirtualNodeSpecBackend]]], jsii.get(self, "backendInput"))

    @builtins.property
    @jsii.member(jsii_name="listenerInput")
    def listener_input(self) -> typing.Optional[AppmeshVirtualNodeSpecListener]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecListener], jsii.get(self, "listenerInput"))

    @builtins.property
    @jsii.member(jsii_name="loggingInput")
    def logging_input(self) -> typing.Optional[AppmeshVirtualNodeSpecLogging]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecLogging], jsii.get(self, "loggingInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceDiscoveryInput")
    def service_discovery_input(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecServiceDiscovery"]:
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecServiceDiscovery"], jsii.get(self, "serviceDiscoveryInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshVirtualNodeSpec]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppmeshVirtualNodeSpec]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c732fe52b65ab1eaabc61ddbdf04446bbe2084da9f07b78336f64109e5b7291e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecServiceDiscovery",
    jsii_struct_bases=[],
    name_mapping={"aws_cloud_map": "awsCloudMap", "dns": "dns"},
)
class AppmeshVirtualNodeSpecServiceDiscovery:
    def __init__(
        self,
        *,
        aws_cloud_map: typing.Optional[typing.Union["AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMap", typing.Dict[builtins.str, typing.Any]]] = None,
        dns: typing.Optional[typing.Union["AppmeshVirtualNodeSpecServiceDiscoveryDns", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param aws_cloud_map: aws_cloud_map block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#aws_cloud_map AppmeshVirtualNode#aws_cloud_map}
        :param dns: dns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#dns AppmeshVirtualNode#dns}
        '''
        if isinstance(aws_cloud_map, dict):
            aws_cloud_map = AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMap(**aws_cloud_map)
        if isinstance(dns, dict):
            dns = AppmeshVirtualNodeSpecServiceDiscoveryDns(**dns)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cb717e03fcd2dac42ab9a540e9e477ad68d15723c4bfdf513c912555a9b4e5a)
            check_type(argname="argument aws_cloud_map", value=aws_cloud_map, expected_type=type_hints["aws_cloud_map"])
            check_type(argname="argument dns", value=dns, expected_type=type_hints["dns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if aws_cloud_map is not None:
            self._values["aws_cloud_map"] = aws_cloud_map
        if dns is not None:
            self._values["dns"] = dns

    @builtins.property
    def aws_cloud_map(
        self,
    ) -> typing.Optional["AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMap"]:
        '''aws_cloud_map block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#aws_cloud_map AppmeshVirtualNode#aws_cloud_map}
        '''
        result = self._values.get("aws_cloud_map")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMap"], result)

    @builtins.property
    def dns(self) -> typing.Optional["AppmeshVirtualNodeSpecServiceDiscoveryDns"]:
        '''dns block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#dns AppmeshVirtualNode#dns}
        '''
        result = self._values.get("dns")
        return typing.cast(typing.Optional["AppmeshVirtualNodeSpecServiceDiscoveryDns"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecServiceDiscovery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMap",
    jsii_struct_bases=[],
    name_mapping={
        "namespace_name": "namespaceName",
        "service_name": "serviceName",
        "attributes": "attributes",
    },
)
class AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMap:
    def __init__(
        self,
        *,
        namespace_name: builtins.str,
        service_name: builtins.str,
        attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param namespace_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#namespace_name AppmeshVirtualNode#namespace_name}.
        :param service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#service_name AppmeshVirtualNode#service_name}.
        :param attributes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#attributes AppmeshVirtualNode#attributes}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffbace883b968f0ec3517e5ea33fefe43970d17a2ab47fd2ba11de102f577a61)
            check_type(argname="argument namespace_name", value=namespace_name, expected_type=type_hints["namespace_name"])
            check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
            check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "namespace_name": namespace_name,
            "service_name": service_name,
        }
        if attributes is not None:
            self._values["attributes"] = attributes

    @builtins.property
    def namespace_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#namespace_name AppmeshVirtualNode#namespace_name}.'''
        result = self._values.get("namespace_name")
        assert result is not None, "Required property 'namespace_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#service_name AppmeshVirtualNode#service_name}.'''
        result = self._values.get("service_name")
        assert result is not None, "Required property 'service_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attributes(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#attributes AppmeshVirtualNode#attributes}.'''
        result = self._values.get("attributes")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMap(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMapOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMapOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ae62403006c787db8a9d0731b02b5ad14b78e1d6b3e5cf983d1544154cb3b382)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAttributes")
    def reset_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAttributes", []))

    @builtins.property
    @jsii.member(jsii_name="attributesInput")
    def attributes_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "attributesInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceNameInput")
    def namespace_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceNameInput")
    def service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "attributes"))

    @attributes.setter
    def attributes(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43cbf020ed5732ca88916af6d979b7f3ccde969fc47bda77583ec707de22e9c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributes", value)

    @builtins.property
    @jsii.member(jsii_name="namespaceName")
    def namespace_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespaceName"))

    @namespace_name.setter
    def namespace_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9deba2a865b03ec4672bf2a6fee1b32a04abf64009d4023a9db3e03f70ce4507)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespaceName", value)

    @builtins.property
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceName"))

    @service_name.setter
    def service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9aa88cdeb799012402fcb60a65842f1db8735b7b3dae2649c34a05d0713050d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMap]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMap], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMap],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__337349fc333a761a537d2aa46c11a0fa26c929ef0654395f7c5d39e93b702abe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecServiceDiscoveryDns",
    jsii_struct_bases=[],
    name_mapping={"hostname": "hostname"},
)
class AppmeshVirtualNodeSpecServiceDiscoveryDns:
    def __init__(self, *, hostname: builtins.str) -> None:
        '''
        :param hostname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#hostname AppmeshVirtualNode#hostname}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9d6738de83205c77c082ad3500d82feef629d7ec470e2bfa5a4278b04d135ed)
            check_type(argname="argument hostname", value=hostname, expected_type=type_hints["hostname"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "hostname": hostname,
        }

    @builtins.property
    def hostname(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#hostname AppmeshVirtualNode#hostname}.'''
        result = self._values.get("hostname")
        assert result is not None, "Required property 'hostname' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualNodeSpecServiceDiscoveryDns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualNodeSpecServiceDiscoveryDnsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecServiceDiscoveryDnsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f8cfacf965609d3c9436f85aca5c78e8858545ad06bcaf00d6796f07f77bc614)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="hostnameInput")
    def hostname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostname"))

    @hostname.setter
    def hostname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5b656cc5f9bd0752580dc502397c27abdb2ba1d07f36baef202c5ad776641a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostname", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecServiceDiscoveryDns]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecServiceDiscoveryDns], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecServiceDiscoveryDns],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15b4b5d29d8c712affdea940b66accf9b5d1ccedb7b0584be8c8778d8956e105)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualNodeSpecServiceDiscoveryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualNode.AppmeshVirtualNodeSpecServiceDiscoveryOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6eda92c6b5bab71a15691f850aad3ec4b7280a43fc4b5c817f4b5ec54e786d6f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAwsCloudMap")
    def put_aws_cloud_map(
        self,
        *,
        namespace_name: builtins.str,
        service_name: builtins.str,
        attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param namespace_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#namespace_name AppmeshVirtualNode#namespace_name}.
        :param service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#service_name AppmeshVirtualNode#service_name}.
        :param attributes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#attributes AppmeshVirtualNode#attributes}.
        '''
        value = AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMap(
            namespace_name=namespace_name,
            service_name=service_name,
            attributes=attributes,
        )

        return typing.cast(None, jsii.invoke(self, "putAwsCloudMap", [value]))

    @jsii.member(jsii_name="putDns")
    def put_dns(self, *, hostname: builtins.str) -> None:
        '''
        :param hostname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_node#hostname AppmeshVirtualNode#hostname}.
        '''
        value = AppmeshVirtualNodeSpecServiceDiscoveryDns(hostname=hostname)

        return typing.cast(None, jsii.invoke(self, "putDns", [value]))

    @jsii.member(jsii_name="resetAwsCloudMap")
    def reset_aws_cloud_map(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsCloudMap", []))

    @jsii.member(jsii_name="resetDns")
    def reset_dns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDns", []))

    @builtins.property
    @jsii.member(jsii_name="awsCloudMap")
    def aws_cloud_map(
        self,
    ) -> AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMapOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMapOutputReference, jsii.get(self, "awsCloudMap"))

    @builtins.property
    @jsii.member(jsii_name="dns")
    def dns(self) -> AppmeshVirtualNodeSpecServiceDiscoveryDnsOutputReference:
        return typing.cast(AppmeshVirtualNodeSpecServiceDiscoveryDnsOutputReference, jsii.get(self, "dns"))

    @builtins.property
    @jsii.member(jsii_name="awsCloudMapInput")
    def aws_cloud_map_input(
        self,
    ) -> typing.Optional[AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMap]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMap], jsii.get(self, "awsCloudMapInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsInput")
    def dns_input(self) -> typing.Optional[AppmeshVirtualNodeSpecServiceDiscoveryDns]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecServiceDiscoveryDns], jsii.get(self, "dnsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshVirtualNodeSpecServiceDiscovery]:
        return typing.cast(typing.Optional[AppmeshVirtualNodeSpecServiceDiscovery], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualNodeSpecServiceDiscovery],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e85cc427616f072f8711b6142de3b1a279963bc57da22ba2438d11578056395b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AppmeshVirtualNode",
    "AppmeshVirtualNodeConfig",
    "AppmeshVirtualNodeSpec",
    "AppmeshVirtualNodeSpecBackend",
    "AppmeshVirtualNodeSpecBackendDefaults",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicy",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyOutputReference",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTls",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificate",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFile",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFileOutputReference",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateOutputReference",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSds",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSdsOutputReference",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsOutputReference",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidation",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationOutputReference",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatchOutputReference",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesOutputReference",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrust",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcm",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcmOutputReference",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFile",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFileOutputReference",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustOutputReference",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSds",
    "AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSdsOutputReference",
    "AppmeshVirtualNodeSpecBackendDefaultsOutputReference",
    "AppmeshVirtualNodeSpecBackendList",
    "AppmeshVirtualNodeSpecBackendOutputReference",
    "AppmeshVirtualNodeSpecBackendVirtualService",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicy",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyOutputReference",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTls",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificate",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFile",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFileOutputReference",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateOutputReference",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSds",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSdsOutputReference",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsOutputReference",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidation",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationOutputReference",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNames",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatch",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatchOutputReference",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesOutputReference",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrust",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcm",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcmOutputReference",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFile",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFileOutputReference",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustOutputReference",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSds",
    "AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSdsOutputReference",
    "AppmeshVirtualNodeSpecBackendVirtualServiceOutputReference",
    "AppmeshVirtualNodeSpecListener",
    "AppmeshVirtualNodeSpecListenerConnectionPool",
    "AppmeshVirtualNodeSpecListenerConnectionPoolGrpc",
    "AppmeshVirtualNodeSpecListenerConnectionPoolGrpcOutputReference",
    "AppmeshVirtualNodeSpecListenerConnectionPoolHttp",
    "AppmeshVirtualNodeSpecListenerConnectionPoolHttp2",
    "AppmeshVirtualNodeSpecListenerConnectionPoolHttp2OutputReference",
    "AppmeshVirtualNodeSpecListenerConnectionPoolHttpOutputReference",
    "AppmeshVirtualNodeSpecListenerConnectionPoolOutputReference",
    "AppmeshVirtualNodeSpecListenerConnectionPoolTcp",
    "AppmeshVirtualNodeSpecListenerConnectionPoolTcpOutputReference",
    "AppmeshVirtualNodeSpecListenerHealthCheck",
    "AppmeshVirtualNodeSpecListenerHealthCheckOutputReference",
    "AppmeshVirtualNodeSpecListenerOutlierDetection",
    "AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDuration",
    "AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDurationOutputReference",
    "AppmeshVirtualNodeSpecListenerOutlierDetectionInterval",
    "AppmeshVirtualNodeSpecListenerOutlierDetectionIntervalOutputReference",
    "AppmeshVirtualNodeSpecListenerOutlierDetectionOutputReference",
    "AppmeshVirtualNodeSpecListenerOutputReference",
    "AppmeshVirtualNodeSpecListenerPortMapping",
    "AppmeshVirtualNodeSpecListenerPortMappingOutputReference",
    "AppmeshVirtualNodeSpecListenerTimeout",
    "AppmeshVirtualNodeSpecListenerTimeoutGrpc",
    "AppmeshVirtualNodeSpecListenerTimeoutGrpcIdle",
    "AppmeshVirtualNodeSpecListenerTimeoutGrpcIdleOutputReference",
    "AppmeshVirtualNodeSpecListenerTimeoutGrpcOutputReference",
    "AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequest",
    "AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequestOutputReference",
    "AppmeshVirtualNodeSpecListenerTimeoutHttp",
    "AppmeshVirtualNodeSpecListenerTimeoutHttp2",
    "AppmeshVirtualNodeSpecListenerTimeoutHttp2Idle",
    "AppmeshVirtualNodeSpecListenerTimeoutHttp2IdleOutputReference",
    "AppmeshVirtualNodeSpecListenerTimeoutHttp2OutputReference",
    "AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequest",
    "AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequestOutputReference",
    "AppmeshVirtualNodeSpecListenerTimeoutHttpIdle",
    "AppmeshVirtualNodeSpecListenerTimeoutHttpIdleOutputReference",
    "AppmeshVirtualNodeSpecListenerTimeoutHttpOutputReference",
    "AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequest",
    "AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequestOutputReference",
    "AppmeshVirtualNodeSpecListenerTimeoutOutputReference",
    "AppmeshVirtualNodeSpecListenerTimeoutTcp",
    "AppmeshVirtualNodeSpecListenerTimeoutTcpIdle",
    "AppmeshVirtualNodeSpecListenerTimeoutTcpIdleOutputReference",
    "AppmeshVirtualNodeSpecListenerTimeoutTcpOutputReference",
    "AppmeshVirtualNodeSpecListenerTls",
    "AppmeshVirtualNodeSpecListenerTlsCertificate",
    "AppmeshVirtualNodeSpecListenerTlsCertificateAcm",
    "AppmeshVirtualNodeSpecListenerTlsCertificateAcmOutputReference",
    "AppmeshVirtualNodeSpecListenerTlsCertificateFile",
    "AppmeshVirtualNodeSpecListenerTlsCertificateFileOutputReference",
    "AppmeshVirtualNodeSpecListenerTlsCertificateOutputReference",
    "AppmeshVirtualNodeSpecListenerTlsCertificateSds",
    "AppmeshVirtualNodeSpecListenerTlsCertificateSdsOutputReference",
    "AppmeshVirtualNodeSpecListenerTlsOutputReference",
    "AppmeshVirtualNodeSpecListenerTlsValidation",
    "AppmeshVirtualNodeSpecListenerTlsValidationOutputReference",
    "AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNames",
    "AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatch",
    "AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatchOutputReference",
    "AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesOutputReference",
    "AppmeshVirtualNodeSpecListenerTlsValidationTrust",
    "AppmeshVirtualNodeSpecListenerTlsValidationTrustFile",
    "AppmeshVirtualNodeSpecListenerTlsValidationTrustFileOutputReference",
    "AppmeshVirtualNodeSpecListenerTlsValidationTrustOutputReference",
    "AppmeshVirtualNodeSpecListenerTlsValidationTrustSds",
    "AppmeshVirtualNodeSpecListenerTlsValidationTrustSdsOutputReference",
    "AppmeshVirtualNodeSpecLogging",
    "AppmeshVirtualNodeSpecLoggingAccessLog",
    "AppmeshVirtualNodeSpecLoggingAccessLogFile",
    "AppmeshVirtualNodeSpecLoggingAccessLogFileOutputReference",
    "AppmeshVirtualNodeSpecLoggingAccessLogOutputReference",
    "AppmeshVirtualNodeSpecLoggingOutputReference",
    "AppmeshVirtualNodeSpecOutputReference",
    "AppmeshVirtualNodeSpecServiceDiscovery",
    "AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMap",
    "AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMapOutputReference",
    "AppmeshVirtualNodeSpecServiceDiscoveryDns",
    "AppmeshVirtualNodeSpecServiceDiscoveryDnsOutputReference",
    "AppmeshVirtualNodeSpecServiceDiscoveryOutputReference",
]

publication.publish()

def _typecheckingstub__1e24237a553776645ea72adc13270809d60e0872a07381576676bc1719cb52a8(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    mesh_name: builtins.str,
    name: builtins.str,
    spec: typing.Union[AppmeshVirtualNodeSpec, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
    mesh_owner: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
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

def _typecheckingstub__376443ffe264ee236e64919d013f6874ea9094294555962fbf5fd074838ddd1e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6806ef4dc04f4e79067780a6c797ac8cb5c29716fb9a73d4c3fa42d4f7894653(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ba99551f9b79a7888c2fa275b9b34ca78291236597395428b41ffec128fd0a3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec1b639d3a9b539b9ba914703902cf27fc4c47acdf324334105d1785380069a3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70ea632be195dfc7499986a558e8b28525dbbd2c82bf723ab0bae8a2108506ba(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33831d2403ac911e94f304ca72aee107eb2918bcc2a299e7510786551366a58e(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aaa32f1a0be60eb1136a27db23ada0b3cbd0d2dbb838034972f70afc99d61150(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    mesh_name: builtins.str,
    name: builtins.str,
    spec: typing.Union[AppmeshVirtualNodeSpec, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
    mesh_owner: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dc2b69e385cd93c86e408ca3a2933148ddeafe0e099d15b8210685f3b2e32cf(
    *,
    backend: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppmeshVirtualNodeSpecBackend, typing.Dict[builtins.str, typing.Any]]]]] = None,
    backend_defaults: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendDefaults, typing.Dict[builtins.str, typing.Any]]] = None,
    listener: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListener, typing.Dict[builtins.str, typing.Any]]] = None,
    logging: typing.Optional[typing.Union[AppmeshVirtualNodeSpecLogging, typing.Dict[builtins.str, typing.Any]]] = None,
    service_discovery: typing.Optional[typing.Union[AppmeshVirtualNodeSpecServiceDiscovery, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b25e1fbddd114621cf42865a7dea5371f65e9711b9b96723cfde7e3e789b0dc(
    *,
    virtual_service: typing.Union[AppmeshVirtualNodeSpecBackendVirtualService, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c16cd438aefb8370cd84a3a6c207dad9f351f9b858adf0d0ed213ab300baf06e(
    *,
    client_policy: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendDefaultsClientPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd7f54e0da78b8468c14e4ce9cc9162b5d5365a485132d23ead903c0b6bbf295(
    *,
    tls: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTls, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d93a7312abb2ba928e3ad4d0726630bda6deecef109e4c775aab7ab35c3dea42(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9ce08fee2f9a504cf4071f9999d9476a7eb9fd2e67db7ff5011e7cdeef92a84(
    value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__deca6c77f7cee02bedd7f9d3ecc002ea27b15e30c71a3febbcea5a2679b06e24(
    *,
    validation: typing.Union[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidation, typing.Dict[builtins.str, typing.Any]],
    certificate: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificate, typing.Dict[builtins.str, typing.Any]]] = None,
    enforce: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ports: typing.Optional[typing.Sequence[jsii.Number]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__419c3ab657431f23b613be2e2273e10967b3235d9b3997e0a8c95cddbb78039a(
    *,
    file: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFile, typing.Dict[builtins.str, typing.Any]]] = None,
    sds: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSds, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__faff23421fdf0e85f47d120c8d40816e4461b387becd54ae41187fbfb41e3d58(
    *,
    certificate_chain: builtins.str,
    private_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12363b31c8277cc8109549641d0d87ef5b50a6f2e2e68f70306e25a5f43d8256(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0549beaeb3adcf3cf4ad3e9fe4d222739782b4c2fbcd9166ef55ecde99730d94(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d24506bc29bf51f6e3795ff57fcc6dacbb9c9d7865e7ffadb2e9055a9a3a546(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df95dd04c55f9aa6b00003cad82b9232ae8132c8d87ff9d191698e03e0e902d3(
    value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateFile],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8a9c256a6f9915865d5374be1bcae5776ca29a8d07529f216f1de6532f3f9df(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8f1ee0d7e8ea9ba1769439de6c73cc389e55e0cc75c5fb9b0de078325d3b3e8(
    value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificate],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3e1448ba5d1c2efbd92983bd6e9d7e9f5715a5535ca04cd8b608f082e992f13(
    *,
    secret_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84ad6973eb46dcc3b3cb863975e33f3f1e9c1cf7b6296ca6c91f4c648d4972f4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd0800bac838fd5f1bbe1a3cb48609dab2b9768ca00998e1c5295e0f2b6259f7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28bb040a45e4ed08fbf0aa3242a49d59812384868f4c7c8d8d6a84ce20488e41(
    value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsCertificateSds],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b70e774e436da4f5672b3f5d52596c36ace03276efbf48dcaad13fd30517cfab(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd563475c7d3fb279c4a30f9f1b419097db7ef50e6764dd6339525d7f593e4b1(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c395233f9e749ee993984d5d4ca14997c9c0b334b2385586ab844db98df8ba1(
    value: typing.List[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23546870b4e33a5679fa187ae8a2354bc70df467c3433338daf9eb725c9cee27(
    value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTls],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__613cde633eb5a8f249557a8d39723b7ad38cedce41d082be6c074ff9dd6d49ea(
    *,
    trust: typing.Union[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrust, typing.Dict[builtins.str, typing.Any]],
    subject_alternative_names: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__174152230f9fc68aed459448bf0e95b8a8876688fbc9c92bf213c65adc28570b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6846e980204e2905d62acf2636a2c37cba894b19259fbf1b69bee7764470a042(
    value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidation],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__518ebaf25f9df5e7981cac53664ada8b22be42e02ecff70301555b800ec8b60d(
    *,
    match: typing.Union[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34ccd1cf0cfcbae2fe1fd4300a37d9c415298e6374cc06b49d83b5b7d8ddc570(
    *,
    exact: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16e62587caa1308c02b8d8b221ad7171666d54b04d917fc0b2d1510f82613d70(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__600d8b4ce868ec7961e6b603d9289dd9dc18cd5c10d72b65de5a334246da4769(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40c3d791f7209561b6f447985b4b87745f3be89b1674d449abc6cfa749999204(
    value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fe33ce30292d10e8e5e46d2155052fd0ebde4536c95bc9d42c0d5cc8cce559e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7fca7e59c27d158ea9b12d45f12e7c043c3d226804534b470eeaf38a722f5a4(
    value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e3b24ba41c33cf00127d58032757922c8d11b510bdede95fc319863349529ae(
    *,
    acm: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcm, typing.Dict[builtins.str, typing.Any]]] = None,
    file: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFile, typing.Dict[builtins.str, typing.Any]]] = None,
    sds: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSds, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c60c69ed0922d8239dd35ba1641e22042eba28503e064b0c379cdbc3a4bdfebf(
    *,
    certificate_authority_arns: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8ca7fa96eaa5f0fbc3b9913df7de16fde28f4d8aac12cced02fcd46533ceac9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19fba7f6a527d8b5ea37df27ecbf82eb6c082974b98b0bfedd0d3d83d171049d(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02fbe62b2d61edc364b147cae73b9d119fa97a7d583d2ef37f82e28fbf938e37(
    value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustAcm],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7cefa59c6b95e87089b5f65a41a1876e0bba83c4632551464d774c726975757(
    *,
    certificate_chain: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6648b4b75c5c04522aec68e68ceff585c060bdb85cafb42cb0a2ee3cc268c2f2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa884aa872279347f0a30692f57ba4c9bb45034ad51c9dbb06864490564f3f52(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71ccc5ca17337e0a8f5179a77834bb0c17ffc2a4194db3b9b2a109dec1f83c17(
    value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustFile],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb5c24537072e80d796cdc3f607759434e7677c3e361cbd05da8d317f880301d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79cd95db611e9526d83ee9871a9bd75bad1c90bde2cafb561c49f4b86328b39f(
    value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrust],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5854b6a615c1389bbecc2dd478a527adc20a95558cd3268040cdaafcb150a980(
    *,
    secret_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d68938e4d1de511677a858be93a69e5fa555149d1041d3b2cae281d00ecc1858(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e71eb7913b88ce88326cac465ccfce908f304328d49df1987f28ccf3f92e5384(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__767917bd766878a2d766783b2f335bce1108023fadca259959bf80d08819905d(
    value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaultsClientPolicyTlsValidationTrustSds],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef79d63939e4eb6f57b5cbbd67cf7b883b28a2f492aa93d3087799fcfee40901(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2144cfb211392b61c264086dced35c1b1a8066eac16fbdd039992ad68ed33052(
    value: typing.Optional[AppmeshVirtualNodeSpecBackendDefaults],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9f2066ab328553280b7a63f8af425180976e382ec99c27a1c938e0e1b3b1628(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a82af33b75e2a9b5c87a649930dcb20ec83b45e30eeb3ef8f6ef0845a1cf5d1(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__daa393838b753c47e81c474cd39afd85d0e9ee1b7872478a480b75ae608ffc7a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d607315274d589417fe8da49cf6b6900e49765148f9cd62811fd896384f92630(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__346cc334ad63289ff1eb077d5d5badf656e71000ff3ac5122868974bedcf9208(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__017867a72c1182e964ebf4351ca1725c70d5831495007dbf03806bf0abad0404(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshVirtualNodeSpecBackend]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e67cbd98da146eed95ae170ee9e13a5893887dedc3848c26768a27f15834a45(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0158ef87edc7de8257fd7ce2d85cbb450cdf58349b75e9b9c9e03bb5348a80d3(
    value: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackend, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b6feff43f72e0e59badcc959d1cf720fcd97572cf2096df6cd1cd05fa5b4217(
    *,
    virtual_service_name: builtins.str,
    client_policy: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea585ffeafcbf8e2c4af5c3f94d411dece1877b8746c708b13027701bd608682(
    *,
    tls: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTls, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92e8bd21c7a2958169937172140fc79407550a50d8ac29fcf3fc23a6c422fc9f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__778f370594515921ea6756b08cae694cfa1eec7ffa82037587c6dbbaa4ccd686(
    value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a65807754e12d6c89b12b41161a9d472c0066632959fd74145ea2473f0aae338(
    *,
    validation: typing.Union[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidation, typing.Dict[builtins.str, typing.Any]],
    certificate: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificate, typing.Dict[builtins.str, typing.Any]]] = None,
    enforce: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ports: typing.Optional[typing.Sequence[jsii.Number]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2abc0adde22e41fdadda507f12df096693412e834d316c9c913f9056a293d712(
    *,
    file: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFile, typing.Dict[builtins.str, typing.Any]]] = None,
    sds: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSds, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4169ca82be30c92f7504ca32a0a06060b3528ff0539acad8ad8518f8249002ca(
    *,
    certificate_chain: builtins.str,
    private_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eaae8263b66002fdf67ed6bf67a1061ea1627b34119438e453494eceb3e44579(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f26f0a55111342cb281d39239d601b5af42cd2afb8dd6ece64f6638efc9f0a3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c1b206abe7b755e0a0a370fe54686b214ebc4213c5c18a38904cb97bdcd90a2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d91c6159d5c531d29c7afc85c5783c7db5e3fe631131535f7f7e85ca7af8bd9(
    value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateFile],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e11ceaa6493757d5219b228815029b41203838cacf8884e32245ff7a6f7afb9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78c76eef627a1c9691ff55885110fdd08b93482e197b48a5cf08027c3787e59a(
    value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificate],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7da6ac89676d351e9c212f46fea9ee84c71f9853dea96a9f9fd57b149218490f(
    *,
    secret_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1177ea3c6178e23e64407d9737bbd19c033b8177e08852a8041e44681793906a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ffd35944a6a4b1a0a68aa1d372c90cc0cb4da77e3b4d5521952d98001f123f3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8f0b825e23d1992d4a5fd244d857cd4d89d25f0d20c7ad37f9a795157c4c7b8(
    value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsCertificateSds],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3747eeae074d89f8c1541463225e9fbe0762857c3f57c6a8a1f48505e9fdb33d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9972cb8f1779a692c7fb24feb9f6cb65f25a0ad93927b2d34e5a85b0b15412a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71873f4554c9c2fb69bcd1b6a862997c4b166e7d7b64795d2c8c4e5dd676e3fe(
    value: typing.List[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8fd65a0313b7d5196528838724970350ebadc696571702838367e7be2c359c6(
    value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTls],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__329fc992e79335380e1db2b6db2623f69135fff8eb604ba4a78f04e33bdd7425(
    *,
    trust: typing.Union[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrust, typing.Dict[builtins.str, typing.Any]],
    subject_alternative_names: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNames, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e57b17ee50b339508ae480775006645bb7f4f152b51c0f6d8a1f85f73c88506(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7db07fb841028e2fd04f975676d090c9537b594559c0890ba970b2b3fd16ab08(
    value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidation],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8ca11af5f31817aa0913eb96d6ba622bb1b3292c4029ec26656195227774cda(
    *,
    match: typing.Union[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatch, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e53005a96b93f4c60f1edf62c7cc7d3f55b82d78b36912a377588ce29a3468df(
    *,
    exact: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__056e1f9daad1e67d727a3d882cb860f92fa1fb544db78b5885eb497aea494ab9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1602616e04febc4ecda072dad2661dab25b6e4ad2a31be5bd266562ad750e2b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64592cf3f232dd82576326dd3ceb640b8847131d5cc96428ca12ba73b0253bc2(
    value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNamesMatch],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__618fe04e56d4c892d8f3a69e80464fd1173b26241f8151453a622a5647d7bc58(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4314046e85c755271482938fb562325c4ff840d98b779810f66475fc66e3505e(
    value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationSubjectAlternativeNames],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad656554e842ee963076aa14d39bcb00ec3bee7bf9cd71373417dfac005208cf(
    *,
    acm: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcm, typing.Dict[builtins.str, typing.Any]]] = None,
    file: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFile, typing.Dict[builtins.str, typing.Any]]] = None,
    sds: typing.Optional[typing.Union[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSds, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fad90b8a4e5f0974b537f3383373c8ef1f51c5d7ed7af1c26d4110b70f4f92b(
    *,
    certificate_authority_arns: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59e01f33702693b31b70c22b44dd9c91d86094a3df87771f18bf2f94736f1fac(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23f541ef640a474644535fb567fad202044f02fed18a2721587a030bfec400dd(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__211a30659db4dfe4789e91be3586db4881d298a7624b711edfcc3cd8823058f3(
    value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustAcm],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6474310f3473fa93f607582a7b4fbc0ed9dec0e4a6553061f48aa0d27624d70(
    *,
    certificate_chain: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4619ac1b9c6ee608caa9a4b3b9e28e0ab4a298f769dd397a11cff52dcd8eb829(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d2edc13affe54bae3d71b71e121c58fa4d85244ce206cbbe7cb9ad22df7fd22(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c94f943018aa2f20a125f804ab45010efcce73c0287ba5263a9fb6f9e4292605(
    value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustFile],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b776974142fd50e9610fe7b20a6e29a3ab5a526c6365e716c4965c40c1b0307(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__280119688cd60f43831428e7c3699f6d8c7cf5396e867fb859a36dc3f56fb90b(
    value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrust],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be40365ee314fd0c2b1a2868b58801b9a18852e42d0e7a30d047608d5a9896af(
    *,
    secret_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a870b7ed058da9f3174f04317fb6c492a52f5176393e00ee794789fc2be1e57e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0510dcd63d253f3dcbb77c35b02f4afaa7feb2a828921c12e2a730216b6e6855(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dccc964a08ed7720f24f408576aee1aa966750879725330ea857a57813990c63(
    value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualServiceClientPolicyTlsValidationTrustSds],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c628ffb2945e31f753831c69312575c8086d696709c672ae974e7376585747d8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c564deb28dbb3a750b711d9a74ab90730b229c8b714989e36aed0c18f3fdaf82(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__183a98ecdf50c1b3586cbcc115925575d4bba17a563aa9607b4a707698a96d4e(
    value: typing.Optional[AppmeshVirtualNodeSpecBackendVirtualService],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__299232a8b99ecf3ac75cd0db65816aca2b7e775bc63449a5247a2eedaa954f69(
    *,
    port_mapping: typing.Union[AppmeshVirtualNodeSpecListenerPortMapping, typing.Dict[builtins.str, typing.Any]],
    connection_pool: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerConnectionPool, typing.Dict[builtins.str, typing.Any]]] = None,
    health_check: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerHealthCheck, typing.Dict[builtins.str, typing.Any]]] = None,
    outlier_detection: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerOutlierDetection, typing.Dict[builtins.str, typing.Any]]] = None,
    timeout: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeout, typing.Dict[builtins.str, typing.Any]]] = None,
    tls: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTls, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0911161d7ee89b0bb78441f34d900302b2b7c284c85cdd3786d3137bb8e4688(
    *,
    grpc: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerConnectionPoolGrpc, typing.Dict[builtins.str, typing.Any]]] = None,
    http: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerConnectionPoolHttp, typing.Dict[builtins.str, typing.Any]]] = None,
    http2: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerConnectionPoolHttp2, typing.Dict[builtins.str, typing.Any]]] = None,
    tcp: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerConnectionPoolTcp, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6970d73a083c7f6fb6ab9bc89becfe9efb14478c9e60c0967a04bfbe465d427(
    *,
    max_requests: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eed41e82b0e970a5daab6391ad6939c372daafc0458ef3a5597004112644204f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5023e96e749022e74e965663c013aeef541a178995f95dd3e63c84023507cfb7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__121dc3f4e80061fd757e41a7befd18f9baa9a3467182f1b0ed30ccb15db26bb0(
    value: typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolGrpc],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a01b624511a7e649a532ede0c3ac6cfc07b45f50b8db85b59cbd8a2a1c0941df(
    *,
    max_connections: jsii.Number,
    max_pending_requests: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54c2cb1800a1f9b90d12bb4c8d721d18547398291fcc9d0480412212126cb8dd(
    *,
    max_requests: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4538053bb7581990396f9f241d77915b161d77e434b3a64031b2fb6f208695c4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3c457e175193ae78ebff2ab5381b72cc71709e3e6273646438407679916a4bb(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8101bd085cb8d03e3442615d0423449718aaeefacf3ae077f74f49a35c317983(
    value: typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolHttp2],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7c7969ae3e220362a7bbf15285546ce394557b09a09a6e538710e0ac297b4dc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0580a605ddc2ece792a02a1bbe53770795144c2086ec17b342089ee837c973ef(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34c5f72a91107bc2265c31f009fa5a68c583f7f1d4af929e263aa6f985b9ad29(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa8278a8aeb46e9548428e0753425fb1cba6a30e15c24aa02b4ca49b172d08be(
    value: typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolHttp],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1edde56e92b3d3ea16ba2f0e03fcf310d57f036777ccf8cfecb80cda538e1e41(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aab5fc798a25053b3eaea3a3f8d23e2e6ee1899b29ed630f0de47f75259ac1a2(
    value: typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df53ed8c0924d8a9902edc19d091ed1289fd4f6ceb433783dc0db5528a0fa5a2(
    *,
    max_connections: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d61c432b4edff9e418c07387436e23e1e1f8fa0bf3acc17e78da40872503b86d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98c5afd2b8cf90bbc20a5a9f0a37469be2af29d12f54fa231d341be515b1ac33(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af9981797c73bce5da1804514a594e65a204e10ab17ef3724edb20c400a0e882(
    value: typing.Optional[AppmeshVirtualNodeSpecListenerConnectionPoolTcp],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__618d044954c4a44ffd2a363bc1d1e9546cc72e3b0920bae3704b633d0876ec08(
    *,
    healthy_threshold: jsii.Number,
    interval_millis: jsii.Number,
    protocol: builtins.str,
    timeout_millis: jsii.Number,
    unhealthy_threshold: jsii.Number,
    path: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb10f233040cabd31473ad81f0559ce792f182de0b212a48cbd9ceeca1b352b5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d3f4e6cfdea4fc5a7e2b04cf9a59651fc29c77ce0652ccabddc8d14f25af193(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e7bbe24438ed6ab73ad95183b0f7a7093a13e1ce3c436845b1aa18ba8c9eda9(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a42a4fd74b5d13c86d7bcff28f9551d09bd389a014556e6d51f00f2f4f5fee70(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e00fc67a5ecd0e7877603b0da432500bf0ec6be6b5dedda8049af19e11f4a0d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d61c898c214df52e89d285ff0ef481d1163bd76e4224ea8025c8b0042cbf389(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7165aaf0e1002cb0df6ba33e30b529dd1028a9fd5946d55b617d11e887532573(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54f6ad7be614b6a73fc3e21965b8731a12765b0ac5a6924cbb03d7381de37565(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__777b9299df96f92c649c596970cafe1eca63a43fad08722a62ae827365f6b414(
    value: typing.Optional[AppmeshVirtualNodeSpecListenerHealthCheck],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__892c5d8ac210e5ad318b001c81ece41283348f3d9042e816d648efcb9684bbed(
    *,
    base_ejection_duration: typing.Union[AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDuration, typing.Dict[builtins.str, typing.Any]],
    interval: typing.Union[AppmeshVirtualNodeSpecListenerOutlierDetectionInterval, typing.Dict[builtins.str, typing.Any]],
    max_ejection_percent: jsii.Number,
    max_server_errors: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__592467e076dbe821cd8ee0dd475153c97e7b4356308f118f44e84fd476ff8680(
    *,
    unit: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3d22e22173b25ed2f5e1409e7e2f6ff35d5b39f117eea2bb36dc45d3eba46ae(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdc900165b3eaf92d1ac619f821c9a0d409a1cebcf3ca52a38473e07c39478d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7557e9dd5222bb42edcd91c6fe9d662722ce057550e6064c0e87711390c5db4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d9518d10474b0f4342293f97f9f39fd860d0d8f52378ee019c2d8a8a644c52d(
    value: typing.Optional[AppmeshVirtualNodeSpecListenerOutlierDetectionBaseEjectionDuration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a05d002bed226c06a60eff669f2664a8d13886c1db5636c5bfc2c6e88e9ac9e(
    *,
    unit: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__212b2a33840eaf822187f5c0ff1821e5ffa673cab6e1b4fba5514dbfa581855b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35a815d87b8e277417fbd37aee2cf49d49d9a8e1b439fb1a32a8b32ae5265e5d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d73ac93f65df857700bd503254c42197386e80aea65893f140fe9742b43a2ed8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0109993a02c70ac5b0a6f40c062d1cf61162a992d9909f2e953c48e361cb6182(
    value: typing.Optional[AppmeshVirtualNodeSpecListenerOutlierDetectionInterval],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ba83fb71e79f7c99eeff923e80f8e2852c87137aa4c7ca3c1d5477b4ca57393(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbfd8a168accf9a679e5b1f90f37ee1bd73a72a7347dcf56ae44c027cb904b70(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6db75fba44bef3d1777590292f7abcbaf33ec1978b9c786dd84595a7cfab6025(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2eadf43b3fe456868847236f9d67289d8755dc5fc4e62c331a205e046d25b0b3(
    value: typing.Optional[AppmeshVirtualNodeSpecListenerOutlierDetection],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ec88e01dfcb45a247349c2b280028cf7cadb962a7d708911aad5cef7cf2cc66(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e81712ee667195c3c1a11013fa41bd66cb816e5b1d0ef6a4303c40f6e67651a2(
    value: typing.Optional[AppmeshVirtualNodeSpecListener],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da959cb4c20f7d276308c867058b13d9c35ee8d7b556b756283195b02a822c2e(
    *,
    port: jsii.Number,
    protocol: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2267c0935efad8123d6d42b82cb036ecdf3f2a192a75e6bfbd83c7ba36f6b1a2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95854854c8d9d8cec9a30967d4d1447bed90e025ef6eb3377faf47d891ef058a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39879b5aa4281dfa5c0cecb633da653c339b51b87103cf3f49603397aa551908(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__942408529637d2a43dc327499a74ee123a051975545f6214633c24aba0c7252e(
    value: typing.Optional[AppmeshVirtualNodeSpecListenerPortMapping],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__331d71893c6a08fac53976bff60ec57e687c6dab22e0ac55bb2544112f16a7e4(
    *,
    grpc: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeoutGrpc, typing.Dict[builtins.str, typing.Any]]] = None,
    http: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeoutHttp, typing.Dict[builtins.str, typing.Any]]] = None,
    http2: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeoutHttp2, typing.Dict[builtins.str, typing.Any]]] = None,
    tcp: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeoutTcp, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21b83df330bc4d9ff3997b2faa5d08b23214499e099c732455e569f22c826502(
    *,
    idle: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeoutGrpcIdle, typing.Dict[builtins.str, typing.Any]]] = None,
    per_request: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequest, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3925e9fe9b27af327058539e7892f3fccc49338fe735fab973cbd736425b41dc(
    *,
    unit: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9630b6da97a65480f5c01effd22c05f54837f5a3637786f9f3e0159d1e0b51a1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21a5a7180236ef4420939cf9f2aa05d0b5a6e936f7e621d4fe9c882b96123f20(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa94c9315f22feda82c9ae0762c699c857351608f1fb3e7c08f79afb7f469b96(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4f8b663b6b2d7817e2182e6209cd157ac8049f14c17cae86c1369a9711dd2b1(
    value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutGrpcIdle],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e112d1fa3f3da5469a371e440f6bdef8430d4e3521760ed4c1ec85f65372d34(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8a5adfd306543f44633b1d8d593b4f41d10a225d44b895ea2fde885053f0c98(
    value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutGrpc],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be437169e9c73d751af2188652623f6bb356650103427cad9e6cec35acfe6fe4(
    *,
    unit: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__daba591cc8de2929fd4fae7432ca0d1f2cb8b66bba5caa24061871afc1914cc7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d755b3b6a997da4f14d5a20dfb3812be91df7c41f884c48324a04f52ad64e9f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bd8e75a9e80a489e8304a6c9d7fd3c95405426e07c99c5255c4d69abb7fd78a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__913cfe8c715783fa1d2b6b7bc07e043578d4d9872d2943a09ef78cce5fdd86bd(
    value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutGrpcPerRequest],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6dc5c0b89a7d362fe6868667ad5ed45b312fcabae9ff6100266894092c5af74e(
    *,
    idle: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeoutHttpIdle, typing.Dict[builtins.str, typing.Any]]] = None,
    per_request: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequest, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4aed04cbfebfa19a5380f4787549ce9fb41d28a776321114370793d4bd74022b(
    *,
    idle: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeoutHttp2Idle, typing.Dict[builtins.str, typing.Any]]] = None,
    per_request: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequest, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffbeb38214c3843a6a5ed727db7fe02dad4d3717c8a94a6768b96ef336f47ada(
    *,
    unit: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e228fd4796edd81738091ba6d3e19d2bb5feafe21eb23ae79e38c46e9b1b9186(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b40caa00a5e504db477330b222034e01e18754d184d68b33b3c47aee72ce48ee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21bf9863e25598dcd1b897fc4ccf228540c1d664dc99146f8ac626c89543a5a6(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3bbc108eea3462169406ae7db1a2d79939c98d08eb968a0ed2f7cfda26d5ba8(
    value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp2Idle],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aafc8e9dbaa953aab7fb35c55af6df69a0b938517701bb0fccd10d1ed87b5bad(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a82e772f4905ebefb1917d1b98cb4ce56dd5aeb180a697f9db0a6615627cad4(
    value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp2],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3e4001653e57e08fcad1c8ad0cc431159f2c01cedc47cc557a1734e06576986(
    *,
    unit: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__910f7cebe9585d7ef0af21f5422936702526490e8841c0e43de88624b0d37b71(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1b1083744cf200585370cb22e198e718f454b65ef59f54f89050754aba4baef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d18cfb41fb207a6ebf5a479002b150ed69c46ca9553b2ae12542098a25471402(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9eb09e947ebcb473b1f8a2d1752a98784a3d85d2b4b748d25ee9e84b0feb7e34(
    value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp2PerRequest],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23cc6562daf095a27f50aec46e222269d2455f87564f46c0bed179324e536644(
    *,
    unit: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f8cfd952f9aa30563edc9183f4659afa53d4c2055b8d938bd7035a0f394bc6b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__172a02bc4f98188e5a08bfaa557a4a4a3c6857c17158698c2570282ea6f92332(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebff2145817fbf3ec73b2a5fa7116ade23e6a17ca9051c87ce7ca5b688cd8e6f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8c3ea526cc377b9450ff75b1f5dca082597e8bdf6a6b1ae803b14597f752847(
    value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttpIdle],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d71e6f43d32b86abd953a2b33577e4dcbd4f7f90ffcf4680b3cd4e8430efd5f1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb705ec69beafca92a7ffd72315dbc94665647ed4219cbad7a33f0ad6412c339(
    value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttp],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de37204f19629d58df5cee36535bde3f2101c83e0c4b39f1d7651da1c9b1878d(
    *,
    unit: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18f50f72e6a7fcd96cab1cb36ff41f6ab6e4039077bae9a7c3b0e56544c853c8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__beb3cd3332a9dccee21a454ea2596fb2ea7f0bd4a5a19dc6c1fe596be87461ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27fcd89cccf418a3f38349a4a202eb8719e5858c06a44144cce48c05f2fbda3a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f67d06cd5584a510b8382f11ff241476533341cf26949a9fa7d5ac6c51f84f9(
    value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutHttpPerRequest],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90754faed3ef40bc8cb54c0581cf39507a2df9216907cee154748f9d3de2cfad(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86fb0da156b8a5dffb441b7bf42b4cd9b8ca409d3edb555598b93025853a5642(
    value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeout],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd5fb251e7bca83c1c83bfbdbfce7a2f6b6e9f9478b8286666ad90c866d909a6(
    *,
    idle: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTimeoutTcpIdle, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bd575e546026eaaa1aada044e053271d5be7ec4e32f6d86c9762dcb106ad79f(
    *,
    unit: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19b8417311160af23e373a4721c34749588400fb0a06e28c1691b5e6a31babf2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fb8478c6b1827337b16dd6284f62535fd432d7ce22909030447cda93b5231f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b092fd473bbf8dd9333c6c39cbdee59c0eda6c731e4a57918006915a43f1349f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebcf276bfab623e2086c23d7c19d0c6eed863b76d4cc188585d49d763dec576f(
    value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutTcpIdle],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf6c5c0d025da1ea5b4def659b544c837ae9c65a9ef8e6cf5e40118578965e95(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8c9deb5b9bbbdf3944d78b300d2f39ee347c012be9e1d63815acb8d5c157157(
    value: typing.Optional[AppmeshVirtualNodeSpecListenerTimeoutTcp],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fe04259c75b8de83b8b9cef42026fa9473d79458739a64c8da5253eda93ce49(
    *,
    certificate: typing.Union[AppmeshVirtualNodeSpecListenerTlsCertificate, typing.Dict[builtins.str, typing.Any]],
    mode: builtins.str,
    validation: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTlsValidation, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e42dd54ccba59470424d9add59022ab897a77ddc5a623cb72c8795475120ec51(
    *,
    acm: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTlsCertificateAcm, typing.Dict[builtins.str, typing.Any]]] = None,
    file: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTlsCertificateFile, typing.Dict[builtins.str, typing.Any]]] = None,
    sds: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTlsCertificateSds, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__954c93235e3a742f6b4cc1799f515332a776adbf49c198ed8003e8f2e3e8d660(
    *,
    certificate_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a4a0de40851a8af3cab79e7d90c5d914471ec94b6350c4134b746bb90a1a1cd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4098c684b5110e10821b9dd2daeef518456fb04738dfd879d38e01b02b1e0cac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2790a97dd2e1c85cb76d68c087a058a84c969cc447cd8cd5fffed28139e7239(
    value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificateAcm],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fc0a977e0dfdbc89e00bec39e6038440de97175f055b77a442584c001eb7cbc(
    *,
    certificate_chain: builtins.str,
    private_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc545b3ee554b2c56fd383fb531a4e15c40aba9bd4ff21ee170de52b431363fa(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db0d53a7ccd1fc8d8cf3144c147ac98c61a09756878c3eaf963e2c8c43b5088d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adeb792498c1ae1c6b9917fe900ce74e5ec68fbf96a4a7250253ba283160e765(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e4b167083b810b87e227e3229bbfe050df19116f86a2a24e2a6705c708fa516(
    value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificateFile],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebb75997ef10ff8aadb871bcabf70c1dad68ea1f13f0f5122f89a403eab43392(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3af4739fd4ca955fec46283aa505635d428c1fedf6d22e17cbe985a957e0f6a0(
    value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificate],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3e56a0a1e0cba40719df7987ee2b40a6f3ca6394b119c2a9ee2008c071ba5fe(
    *,
    secret_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d2fb404acc44640f80fadfefd8f5f989f2b0da68dbb59dee7b09017d77f1ea6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58deef79cdb7bcbc2d98ad775d7033880fd18c56a19064d1396052c174b8dea9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f90e965bc6a408add9bfea5a89b4f77bf4753c8d7c999d780ac478587e0bb6e(
    value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsCertificateSds],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af11cd6c2de43dcf0df038654cc123a9fd3db21606321e4384dbd37c50ca30f4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7c081721cf99e58bec57ec52c619db99eb66a19508f996531154c6790a7780e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2345c49236266c61bdbaf96ca9187e218f51985232938b7c07636aa88fb388e(
    value: typing.Optional[AppmeshVirtualNodeSpecListenerTls],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8879904a4ec0d347d3cacdfc5cbdfb323c0a44dfe6dc67cf2c228c2ece5104a2(
    *,
    trust: typing.Union[AppmeshVirtualNodeSpecListenerTlsValidationTrust, typing.Dict[builtins.str, typing.Any]],
    subject_alternative_names: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNames, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__893eb293bb4a18f1d02101912dcb4d56f2a0b2bfb71b190a1f4af93723a18f95(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bde2f61d6b2f7c035bf06a6f646c6761aa7e1730da15574e0a6819510ebaa57(
    value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidation],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6aada447dfdb0819a302cdeae484a7b114df81d3b1cb22b7ddd7c00ec8c041d(
    *,
    match: typing.Union[AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatch, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fe865528d320beaece5a85c0009a2005f941c322266a774fc021cb57485e93a(
    *,
    exact: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c60984aab7a95b9d846479dd4cf265c9450b89018f60db196c2a7df6fa04e22c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42e30a0756c76f533f0d1c54587516e2c9bcfbaa3713d4a4b30846d68ea58218(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21b7fec44cf3b6721ed0add6e9bf59c51904a924f9b8d1764b992dd3d67c21fe(
    value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNamesMatch],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__271fdc2d95a1d8e6cd63b8cbab4513586e844b56369d5e24dafeee39fd4d3b4b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6cff3ca8f3b4916245e817c5f9b89ccae3b7b10930d7ebb1c028048fbbfaa81(
    value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationSubjectAlternativeNames],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96ce88dc38b06c41c06120cffb7219dbf367cd2fb2589396a51a3f8b482d809e(
    *,
    file: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTlsValidationTrustFile, typing.Dict[builtins.str, typing.Any]]] = None,
    sds: typing.Optional[typing.Union[AppmeshVirtualNodeSpecListenerTlsValidationTrustSds, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5371d227c3248fe1187d5ea926fcd73839945f54c4553f959be5d1da36f48715(
    *,
    certificate_chain: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a64829c69cdfffe41a57949b95313bbf652a52d99f244bd5be2a01b6da4bddd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c1e2418bd69904577e5be41dabf46fd8b8230535f18b54c9e1eb73515d685b4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57cc8c01f0a2d2a12489a9d42a55f2a51014623365c8157a6146fbc47c565027(
    value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationTrustFile],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cd18e1836ada60ca79725c835d931966bb8a21fae1549a7fe3a4ca661fe2aba(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1ed0dd0c64af2399c771ee96d99d0fe400d8e72e0306d256cfa639e7c3a86e6(
    value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationTrust],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1ac5f6e72f9cef7929a164d1432886c9ede3a9a0a2fb2344db44d946276d238(
    *,
    secret_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40f96b814ceb7a3c26a1d2ee22f98c651dc563f1e669b8fa3b793982fa9f4435(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee4bc1c94a7ced72479043dbc50413e13b5c277284add994bd2d38a9cf35f2df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__481f120d2d76802f1c235a4f368f5d92e11bab29105817ebae9d00ddece1d55a(
    value: typing.Optional[AppmeshVirtualNodeSpecListenerTlsValidationTrustSds],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f8ca2aea8d6f77b59580566af3a13fcc509efff59087729befc6e265fc27192(
    *,
    access_log: typing.Optional[typing.Union[AppmeshVirtualNodeSpecLoggingAccessLog, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb86acce4a2fbcbeae42ff0019bce0be64e0bae961dca2a920fb50dedeabd48a(
    *,
    file: typing.Optional[typing.Union[AppmeshVirtualNodeSpecLoggingAccessLogFile, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be71a767791532003da7d81d97bc28d18c7f33f8661dbaed9130a845c64537fb(
    *,
    path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1ed98743bc06b687dcb1e437469f885b159e9098cecf166b51dbfb49a31b196(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7f42cb9b0a103c2b36eb943838ca9691917af5ee884c668879bafc40b9c73df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8adb7285f4aab91bd31f2918881cc016b24becd9922c7b71a7cf9546793feca2(
    value: typing.Optional[AppmeshVirtualNodeSpecLoggingAccessLogFile],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44aaf70ce87958617409dd6b0ad993ffbf9f6f4092fdd82adb825f58ed5c10e4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a211a79e2c9f0261358ea4603cf2eccdb40f454701fa54faa37fd21249d5a47(
    value: typing.Optional[AppmeshVirtualNodeSpecLoggingAccessLog],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__311534c9e3188fc760980cd8e0a28ec9461e097cdcc64f638b36f7623d3c9b8f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b6ff9a621b19824ee0ec0ee2d3b8d9a7d48aa22416e4618f2ae453c4040cef1(
    value: typing.Optional[AppmeshVirtualNodeSpecLogging],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b25f89bc7a598744778cc818353c1977f96b33b53276e13f8a67f459fece3ad0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f7da9e3d273c6ae30de318e179b31a62637359a00f128fa135461599c6b4e68(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppmeshVirtualNodeSpecBackend, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c732fe52b65ab1eaabc61ddbdf04446bbe2084da9f07b78336f64109e5b7291e(
    value: typing.Optional[AppmeshVirtualNodeSpec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cb717e03fcd2dac42ab9a540e9e477ad68d15723c4bfdf513c912555a9b4e5a(
    *,
    aws_cloud_map: typing.Optional[typing.Union[AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMap, typing.Dict[builtins.str, typing.Any]]] = None,
    dns: typing.Optional[typing.Union[AppmeshVirtualNodeSpecServiceDiscoveryDns, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffbace883b968f0ec3517e5ea33fefe43970d17a2ab47fd2ba11de102f577a61(
    *,
    namespace_name: builtins.str,
    service_name: builtins.str,
    attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae62403006c787db8a9d0731b02b5ad14b78e1d6b3e5cf983d1544154cb3b382(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43cbf020ed5732ca88916af6d979b7f3ccde969fc47bda77583ec707de22e9c9(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9deba2a865b03ec4672bf2a6fee1b32a04abf64009d4023a9db3e03f70ce4507(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9aa88cdeb799012402fcb60a65842f1db8735b7b3dae2649c34a05d0713050d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__337349fc333a761a537d2aa46c11a0fa26c929ef0654395f7c5d39e93b702abe(
    value: typing.Optional[AppmeshVirtualNodeSpecServiceDiscoveryAwsCloudMap],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9d6738de83205c77c082ad3500d82feef629d7ec470e2bfa5a4278b04d135ed(
    *,
    hostname: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8cfacf965609d3c9436f85aca5c78e8858545ad06bcaf00d6796f07f77bc614(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5b656cc5f9bd0752580dc502397c27abdb2ba1d07f36baef202c5ad776641a0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15b4b5d29d8c712affdea940b66accf9b5d1ccedb7b0584be8c8778d8956e105(
    value: typing.Optional[AppmeshVirtualNodeSpecServiceDiscoveryDns],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6eda92c6b5bab71a15691f850aad3ec4b7280a43fc4b5c817f4b5ec54e786d6f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e85cc427616f072f8711b6142de3b1a279963bc57da22ba2438d11578056395b(
    value: typing.Optional[AppmeshVirtualNodeSpecServiceDiscovery],
) -> None:
    """Type checking stubs"""
    pass
