'''
# `aws_appmesh_virtual_gateway`

Refer to the Terraform Registory for docs: [`aws_appmesh_virtual_gateway`](https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway).
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


class AppmeshVirtualGateway(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGateway",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway aws_appmesh_virtual_gateway}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        mesh_name: builtins.str,
        name: builtins.str,
        spec: typing.Union["AppmeshVirtualGatewaySpec", typing.Dict[builtins.str, typing.Any]],
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway aws_appmesh_virtual_gateway} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param mesh_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#mesh_name AppmeshVirtualGateway#mesh_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#name AppmeshVirtualGateway#name}.
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#spec AppmeshVirtualGateway#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#id AppmeshVirtualGateway#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mesh_owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#mesh_owner AppmeshVirtualGateway#mesh_owner}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#tags AppmeshVirtualGateway#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#tags_all AppmeshVirtualGateway#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9ffa1dfdc44237f563c7620b7e7a1d040fa5c8f576cb31a094d8d7a7eb37045)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AppmeshVirtualGatewayConfig(
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
        listener: typing.Union["AppmeshVirtualGatewaySpecListener", typing.Dict[builtins.str, typing.Any]],
        backend_defaults: typing.Optional[typing.Union["AppmeshVirtualGatewaySpecBackendDefaults", typing.Dict[builtins.str, typing.Any]]] = None,
        logging: typing.Optional[typing.Union["AppmeshVirtualGatewaySpecLogging", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param listener: listener block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#listener AppmeshVirtualGateway#listener}
        :param backend_defaults: backend_defaults block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#backend_defaults AppmeshVirtualGateway#backend_defaults}
        :param logging: logging block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#logging AppmeshVirtualGateway#logging}
        '''
        value = AppmeshVirtualGatewaySpec(
            listener=listener, backend_defaults=backend_defaults, logging=logging
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
    def spec(self) -> "AppmeshVirtualGatewaySpecOutputReference":
        return typing.cast("AppmeshVirtualGatewaySpecOutputReference", jsii.get(self, "spec"))

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
    def spec_input(self) -> typing.Optional["AppmeshVirtualGatewaySpec"]:
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpec"], jsii.get(self, "specInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__1f1bc027a25e53da46d10d13d95a76cfaa380ea876fb8c81e39ccd4fc089a893)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="meshName")
    def mesh_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "meshName"))

    @mesh_name.setter
    def mesh_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d03dac24f7459d0bd2790fd6791b7b5ab1278adf24ef829b39ab407771819ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "meshName", value)

    @builtins.property
    @jsii.member(jsii_name="meshOwner")
    def mesh_owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "meshOwner"))

    @mesh_owner.setter
    def mesh_owner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3029d42f2dd89ce9e3c73cdb798490ab8ecd7f7bf4f26e46d73e45f5c0f7861f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "meshOwner", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40e16538e8eb40992316e6491c68df7289128de7a8b4ffa5f28c59d8665f79a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d8a07597818f003edfd71aa4e654b6f2baa4a331bc5f3943d3e0e8f5402e90d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b1a837b2d6deeaa3536cd9fc7227b149e7f118565141d4afc41d1edcfde7cff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewayConfig",
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
class AppmeshVirtualGatewayConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        spec: typing.Union["AppmeshVirtualGatewaySpec", typing.Dict[builtins.str, typing.Any]],
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
        :param mesh_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#mesh_name AppmeshVirtualGateway#mesh_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#name AppmeshVirtualGateway#name}.
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#spec AppmeshVirtualGateway#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#id AppmeshVirtualGateway#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mesh_owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#mesh_owner AppmeshVirtualGateway#mesh_owner}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#tags AppmeshVirtualGateway#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#tags_all AppmeshVirtualGateway#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(spec, dict):
            spec = AppmeshVirtualGatewaySpec(**spec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f78d8a032e766325fde6d0826099df045709dfad853940ed5fc9a5be21498f60)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#mesh_name AppmeshVirtualGateway#mesh_name}.'''
        result = self._values.get("mesh_name")
        assert result is not None, "Required property 'mesh_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#name AppmeshVirtualGateway#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def spec(self) -> "AppmeshVirtualGatewaySpec":
        '''spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#spec AppmeshVirtualGateway#spec}
        '''
        result = self._values.get("spec")
        assert result is not None, "Required property 'spec' is missing"
        return typing.cast("AppmeshVirtualGatewaySpec", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#id AppmeshVirtualGateway#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mesh_owner(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#mesh_owner AppmeshVirtualGateway#mesh_owner}.'''
        result = self._values.get("mesh_owner")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#tags AppmeshVirtualGateway#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#tags_all AppmeshVirtualGateway#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualGatewayConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpec",
    jsii_struct_bases=[],
    name_mapping={
        "listener": "listener",
        "backend_defaults": "backendDefaults",
        "logging": "logging",
    },
)
class AppmeshVirtualGatewaySpec:
    def __init__(
        self,
        *,
        listener: typing.Union["AppmeshVirtualGatewaySpecListener", typing.Dict[builtins.str, typing.Any]],
        backend_defaults: typing.Optional[typing.Union["AppmeshVirtualGatewaySpecBackendDefaults", typing.Dict[builtins.str, typing.Any]]] = None,
        logging: typing.Optional[typing.Union["AppmeshVirtualGatewaySpecLogging", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param listener: listener block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#listener AppmeshVirtualGateway#listener}
        :param backend_defaults: backend_defaults block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#backend_defaults AppmeshVirtualGateway#backend_defaults}
        :param logging: logging block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#logging AppmeshVirtualGateway#logging}
        '''
        if isinstance(listener, dict):
            listener = AppmeshVirtualGatewaySpecListener(**listener)
        if isinstance(backend_defaults, dict):
            backend_defaults = AppmeshVirtualGatewaySpecBackendDefaults(**backend_defaults)
        if isinstance(logging, dict):
            logging = AppmeshVirtualGatewaySpecLogging(**logging)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0198859f5e2790d5f29a3c04079a95eff26c2aa29783ad639381709128e6ef8d)
            check_type(argname="argument listener", value=listener, expected_type=type_hints["listener"])
            check_type(argname="argument backend_defaults", value=backend_defaults, expected_type=type_hints["backend_defaults"])
            check_type(argname="argument logging", value=logging, expected_type=type_hints["logging"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "listener": listener,
        }
        if backend_defaults is not None:
            self._values["backend_defaults"] = backend_defaults
        if logging is not None:
            self._values["logging"] = logging

    @builtins.property
    def listener(self) -> "AppmeshVirtualGatewaySpecListener":
        '''listener block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#listener AppmeshVirtualGateway#listener}
        '''
        result = self._values.get("listener")
        assert result is not None, "Required property 'listener' is missing"
        return typing.cast("AppmeshVirtualGatewaySpecListener", result)

    @builtins.property
    def backend_defaults(
        self,
    ) -> typing.Optional["AppmeshVirtualGatewaySpecBackendDefaults"]:
        '''backend_defaults block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#backend_defaults AppmeshVirtualGateway#backend_defaults}
        '''
        result = self._values.get("backend_defaults")
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecBackendDefaults"], result)

    @builtins.property
    def logging(self) -> typing.Optional["AppmeshVirtualGatewaySpecLogging"]:
        '''logging block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#logging AppmeshVirtualGateway#logging}
        '''
        result = self._values.get("logging")
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecLogging"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualGatewaySpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecBackendDefaults",
    jsii_struct_bases=[],
    name_mapping={"client_policy": "clientPolicy"},
)
class AppmeshVirtualGatewaySpecBackendDefaults:
    def __init__(
        self,
        *,
        client_policy: typing.Optional[typing.Union["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param client_policy: client_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#client_policy AppmeshVirtualGateway#client_policy}
        '''
        if isinstance(client_policy, dict):
            client_policy = AppmeshVirtualGatewaySpecBackendDefaultsClientPolicy(**client_policy)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5caa35da86a439f032a42168cf94a159c9b0b7e61d9cd9934fe439cf99464d8c)
            check_type(argname="argument client_policy", value=client_policy, expected_type=type_hints["client_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if client_policy is not None:
            self._values["client_policy"] = client_policy

    @builtins.property
    def client_policy(
        self,
    ) -> typing.Optional["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicy"]:
        '''client_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#client_policy AppmeshVirtualGateway#client_policy}
        '''
        result = self._values.get("client_policy")
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualGatewaySpecBackendDefaults(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecBackendDefaultsClientPolicy",
    jsii_struct_bases=[],
    name_mapping={"tls": "tls"},
)
class AppmeshVirtualGatewaySpecBackendDefaultsClientPolicy:
    def __init__(
        self,
        *,
        tls: typing.Optional[typing.Union["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTls", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param tls: tls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#tls AppmeshVirtualGateway#tls}
        '''
        if isinstance(tls, dict):
            tls = AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTls(**tls)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69ab7ebf199caec9f24111ec54cd57a1e3f22df9b71541acf514a80c29fce811)
            check_type(argname="argument tls", value=tls, expected_type=type_hints["tls"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def tls(
        self,
    ) -> typing.Optional["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTls"]:
        '''tls block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#tls AppmeshVirtualGateway#tls}
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTls"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c26f30af9d50e5b2f4d65c4ad7ed772c647aaf3c615c3cb59118e2c50c4fc580)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTls")
    def put_tls(
        self,
        *,
        validation: typing.Union["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidation", typing.Dict[builtins.str, typing.Any]],
        certificate: typing.Optional[typing.Union["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificate", typing.Dict[builtins.str, typing.Any]]] = None,
        enforce: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ports: typing.Optional[typing.Sequence[jsii.Number]] = None,
    ) -> None:
        '''
        :param validation: validation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#validation AppmeshVirtualGateway#validation}
        :param certificate: certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#certificate AppmeshVirtualGateway#certificate}
        :param enforce: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#enforce AppmeshVirtualGateway#enforce}.
        :param ports: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#ports AppmeshVirtualGateway#ports}.
        '''
        value = AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTls(
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
    ) -> "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsOutputReference":
        return typing.cast("AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsOutputReference", jsii.get(self, "tls"))

    @builtins.property
    @jsii.member(jsii_name="tlsInput")
    def tls_input(
        self,
    ) -> typing.Optional["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTls"]:
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTls"], jsii.get(self, "tlsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicy]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d15c643f9b4d79d2c424b4c5b946dbb6488f6aa7d86ca4ca98d6ac70574881f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTls",
    jsii_struct_bases=[],
    name_mapping={
        "validation": "validation",
        "certificate": "certificate",
        "enforce": "enforce",
        "ports": "ports",
    },
)
class AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTls:
    def __init__(
        self,
        *,
        validation: typing.Union["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidation", typing.Dict[builtins.str, typing.Any]],
        certificate: typing.Optional[typing.Union["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificate", typing.Dict[builtins.str, typing.Any]]] = None,
        enforce: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ports: typing.Optional[typing.Sequence[jsii.Number]] = None,
    ) -> None:
        '''
        :param validation: validation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#validation AppmeshVirtualGateway#validation}
        :param certificate: certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#certificate AppmeshVirtualGateway#certificate}
        :param enforce: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#enforce AppmeshVirtualGateway#enforce}.
        :param ports: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#ports AppmeshVirtualGateway#ports}.
        '''
        if isinstance(validation, dict):
            validation = AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidation(**validation)
        if isinstance(certificate, dict):
            certificate = AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificate(**certificate)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8dabb3b51eee372da40def61ce455ec09fd65806b44c531e895f84f38e65cea)
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
    ) -> "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidation":
        '''validation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#validation AppmeshVirtualGateway#validation}
        '''
        result = self._values.get("validation")
        assert result is not None, "Required property 'validation' is missing"
        return typing.cast("AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidation", result)

    @builtins.property
    def certificate(
        self,
    ) -> typing.Optional["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificate"]:
        '''certificate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#certificate AppmeshVirtualGateway#certificate}
        '''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificate"], result)

    @builtins.property
    def enforce(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#enforce AppmeshVirtualGateway#enforce}.'''
        result = self._values.get("enforce")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def ports(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#ports AppmeshVirtualGateway#ports}.'''
        result = self._values.get("ports")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificate",
    jsii_struct_bases=[],
    name_mapping={"file": "file", "sds": "sds"},
)
class AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificate:
    def __init__(
        self,
        *,
        file: typing.Optional[typing.Union["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateFile", typing.Dict[builtins.str, typing.Any]]] = None,
        sds: typing.Optional[typing.Union["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateSds", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#file AppmeshVirtualGateway#file}
        :param sds: sds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#sds AppmeshVirtualGateway#sds}
        '''
        if isinstance(file, dict):
            file = AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateFile(**file)
        if isinstance(sds, dict):
            sds = AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateSds(**sds)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb25a68725043ebea80a695c2c4d99291c231d61b19e58e8d41fc623b14ad10c)
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
    ) -> typing.Optional["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateFile"]:
        '''file block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#file AppmeshVirtualGateway#file}
        '''
        result = self._values.get("file")
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateFile"], result)

    @builtins.property
    def sds(
        self,
    ) -> typing.Optional["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateSds"]:
        '''sds block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#sds AppmeshVirtualGateway#sds}
        '''
        result = self._values.get("sds")
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateSds"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateFile",
    jsii_struct_bases=[],
    name_mapping={
        "certificate_chain": "certificateChain",
        "private_key": "privateKey",
    },
)
class AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateFile:
    def __init__(
        self,
        *,
        certificate_chain: builtins.str,
        private_key: builtins.str,
    ) -> None:
        '''
        :param certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#certificate_chain AppmeshVirtualGateway#certificate_chain}.
        :param private_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#private_key AppmeshVirtualGateway#private_key}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d120bfa9070b38b3593401939b71b59a72a157da040b5963506d1c22b19f10d8)
            check_type(argname="argument certificate_chain", value=certificate_chain, expected_type=type_hints["certificate_chain"])
            check_type(argname="argument private_key", value=private_key, expected_type=type_hints["private_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_chain": certificate_chain,
            "private_key": private_key,
        }

    @builtins.property
    def certificate_chain(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#certificate_chain AppmeshVirtualGateway#certificate_chain}.'''
        result = self._values.get("certificate_chain")
        assert result is not None, "Required property 'certificate_chain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def private_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#private_key AppmeshVirtualGateway#private_key}.'''
        result = self._values.get("private_key")
        assert result is not None, "Required property 'private_key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateFile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateFileOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateFileOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__807fe590ae0839497ce1472cf81b877c9e32e673249a107622624e7036ac270e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__72dfcafa968bab8666b6683e58820d99ebcb05eb30676c57909efd9a98a01f9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateChain", value)

    @builtins.property
    @jsii.member(jsii_name="privateKey")
    def private_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateKey"))

    @private_key.setter
    def private_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__790cd9693d20eb312e0c5a986f4cd2cec8b4d9cd1c1366a59798acb440ac7527)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateFile]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateFile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateFile],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb9a488a7b66ceda41469636c76b932167f96f661f4bc15f3ab0032c6b8abd4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__088cd7062fdd1d26151b8789765a133b46b888c06d1d8b8b365d7b16f16d0ff2)
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
        :param certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#certificate_chain AppmeshVirtualGateway#certificate_chain}.
        :param private_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#private_key AppmeshVirtualGateway#private_key}.
        '''
        value = AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateFile(
            certificate_chain=certificate_chain, private_key=private_key
        )

        return typing.cast(None, jsii.invoke(self, "putFile", [value]))

    @jsii.member(jsii_name="putSds")
    def put_sds(self, *, secret_name: builtins.str) -> None:
        '''
        :param secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#secret_name AppmeshVirtualGateway#secret_name}.
        '''
        value = AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateSds(
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
    ) -> AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateFileOutputReference:
        return typing.cast(AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateFileOutputReference, jsii.get(self, "file"))

    @builtins.property
    @jsii.member(jsii_name="sds")
    def sds(
        self,
    ) -> "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateSdsOutputReference":
        return typing.cast("AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateSdsOutputReference", jsii.get(self, "sds"))

    @builtins.property
    @jsii.member(jsii_name="fileInput")
    def file_input(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateFile]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateFile], jsii.get(self, "fileInput"))

    @builtins.property
    @jsii.member(jsii_name="sdsInput")
    def sds_input(
        self,
    ) -> typing.Optional["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateSds"]:
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateSds"], jsii.get(self, "sdsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificate]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificate],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e084ce4310f490e7a0ef18ab7cde3cb24f05a52878dc06bb06bfd75143a41416)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateSds",
    jsii_struct_bases=[],
    name_mapping={"secret_name": "secretName"},
)
class AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateSds:
    def __init__(self, *, secret_name: builtins.str) -> None:
        '''
        :param secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#secret_name AppmeshVirtualGateway#secret_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5765ccf405d8c955d836b7f7d7d8924133a6a23b74ca84c75f7a8f28d9b6b7d)
            check_type(argname="argument secret_name", value=secret_name, expected_type=type_hints["secret_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "secret_name": secret_name,
        }

    @builtins.property
    def secret_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#secret_name AppmeshVirtualGateway#secret_name}.'''
        result = self._values.get("secret_name")
        assert result is not None, "Required property 'secret_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateSds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateSdsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateSdsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bd57019f6ca126f1335c7bc84eed11eb5731edf95866bd8e5bca51b8331b92bd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c29332a7e26404a02494487c3634dfd707192d701ec24ae85af84eafbe629551)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateSds]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateSds], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateSds],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cafa917f996b19b5fd7aa7432ed5c2d9bedbca7a6a0d1ff53bf049e1c9273ebd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__14ea9cbf47710fd8a34e2e04397a92c4024cdb60f5b653fa17064c39e0449f7f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCertificate")
    def put_certificate(
        self,
        *,
        file: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateFile, typing.Dict[builtins.str, typing.Any]]] = None,
        sds: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateSds, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#file AppmeshVirtualGateway#file}
        :param sds: sds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#sds AppmeshVirtualGateway#sds}
        '''
        value = AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificate(
            file=file, sds=sds
        )

        return typing.cast(None, jsii.invoke(self, "putCertificate", [value]))

    @jsii.member(jsii_name="putValidation")
    def put_validation(
        self,
        *,
        trust: typing.Union["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrust", typing.Dict[builtins.str, typing.Any]],
        subject_alternative_names: typing.Optional[typing.Union["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param trust: trust block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#trust AppmeshVirtualGateway#trust}
        :param subject_alternative_names: subject_alternative_names block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#subject_alternative_names AppmeshVirtualGateway#subject_alternative_names}
        '''
        value = AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidation(
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
    ) -> AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateOutputReference:
        return typing.cast(AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateOutputReference, jsii.get(self, "certificate"))

    @builtins.property
    @jsii.member(jsii_name="validation")
    def validation(
        self,
    ) -> "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationOutputReference":
        return typing.cast("AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationOutputReference", jsii.get(self, "validation"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificate]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificate], jsii.get(self, "certificateInput"))

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
    ) -> typing.Optional["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidation"]:
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidation"], jsii.get(self, "validationInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__f376b848c7a395501f63db4fabe11cf99ac7b8554a97e6b3959d1efe37c4d81d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enforce", value)

    @builtins.property
    @jsii.member(jsii_name="ports")
    def ports(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "ports"))

    @ports.setter
    def ports(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b94ebcc898dfe5ba215b78301905da4f6f35942aa50036c7828dd07b8bc1dc7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ports", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTls]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTls], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTls],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd9dd3db08cd92b898ca2546bd16cac10ffa3609e629ffa3b706f0140c4008d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidation",
    jsii_struct_bases=[],
    name_mapping={
        "trust": "trust",
        "subject_alternative_names": "subjectAlternativeNames",
    },
)
class AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidation:
    def __init__(
        self,
        *,
        trust: typing.Union["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrust", typing.Dict[builtins.str, typing.Any]],
        subject_alternative_names: typing.Optional[typing.Union["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param trust: trust block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#trust AppmeshVirtualGateway#trust}
        :param subject_alternative_names: subject_alternative_names block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#subject_alternative_names AppmeshVirtualGateway#subject_alternative_names}
        '''
        if isinstance(trust, dict):
            trust = AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrust(**trust)
        if isinstance(subject_alternative_names, dict):
            subject_alternative_names = AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames(**subject_alternative_names)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5e12f6a705c0dce4fd3ee33c66ce125af5894fd3728c5281b992917ef0cb608)
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
    ) -> "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrust":
        '''trust block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#trust AppmeshVirtualGateway#trust}
        '''
        result = self._values.get("trust")
        assert result is not None, "Required property 'trust' is missing"
        return typing.cast("AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrust", result)

    @builtins.property
    def subject_alternative_names(
        self,
    ) -> typing.Optional["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames"]:
        '''subject_alternative_names block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#subject_alternative_names AppmeshVirtualGateway#subject_alternative_names}
        '''
        result = self._values.get("subject_alternative_names")
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cb6fcf410532476b46a2423f54aa6f00d5ad1f24539e80e8f1939a13a5ad5f90)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSubjectAlternativeNames")
    def put_subject_alternative_names(
        self,
        *,
        match: typing.Union["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#match AppmeshVirtualGateway#match}
        '''
        value = AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames(
            match=match
        )

        return typing.cast(None, jsii.invoke(self, "putSubjectAlternativeNames", [value]))

    @jsii.member(jsii_name="putTrust")
    def put_trust(
        self,
        *,
        acm: typing.Optional[typing.Union["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustAcm", typing.Dict[builtins.str, typing.Any]]] = None,
        file: typing.Optional[typing.Union["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustFile", typing.Dict[builtins.str, typing.Any]]] = None,
        sds: typing.Optional[typing.Union["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustSds", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param acm: acm block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#acm AppmeshVirtualGateway#acm}
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#file AppmeshVirtualGateway#file}
        :param sds: sds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#sds AppmeshVirtualGateway#sds}
        '''
        value = AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrust(
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
    ) -> "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesOutputReference":
        return typing.cast("AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesOutputReference", jsii.get(self, "subjectAlternativeNames"))

    @builtins.property
    @jsii.member(jsii_name="trust")
    def trust(
        self,
    ) -> "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustOutputReference":
        return typing.cast("AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustOutputReference", jsii.get(self, "trust"))

    @builtins.property
    @jsii.member(jsii_name="subjectAlternativeNamesInput")
    def subject_alternative_names_input(
        self,
    ) -> typing.Optional["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames"]:
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames"], jsii.get(self, "subjectAlternativeNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="trustInput")
    def trust_input(
        self,
    ) -> typing.Optional["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrust"]:
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrust"], jsii.get(self, "trustInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidation]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29814ffe271b66bc94d1fbffead4bc692e3c81776e51765277e36c6f2e93aec9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames",
    jsii_struct_bases=[],
    name_mapping={"match": "match"},
)
class AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames:
    def __init__(
        self,
        *,
        match: typing.Union["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#match AppmeshVirtualGateway#match}
        '''
        if isinstance(match, dict):
            match = AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch(**match)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2aa75a7ae4ba4bc323dbc69ba483035a6e250cf5729c3485a9d5c80386899251)
            check_type(argname="argument match", value=match, expected_type=type_hints["match"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "match": match,
        }

    @builtins.property
    def match(
        self,
    ) -> "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch":
        '''match block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#match AppmeshVirtualGateway#match}
        '''
        result = self._values.get("match")
        assert result is not None, "Required property 'match' is missing"
        return typing.cast("AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch",
    jsii_struct_bases=[],
    name_mapping={"exact": "exact"},
)
class AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch:
    def __init__(self, *, exact: typing.Sequence[builtins.str]) -> None:
        '''
        :param exact: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#exact AppmeshVirtualGateway#exact}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bde2e6a498fca2ad46f82a0af53241beff0d38636dbeb1766101d92417b7f9f)
            check_type(argname="argument exact", value=exact, expected_type=type_hints["exact"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "exact": exact,
        }

    @builtins.property
    def exact(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#exact AppmeshVirtualGateway#exact}.'''
        result = self._values.get("exact")
        assert result is not None, "Required property 'exact' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatchOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatchOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__87e56eee3322688766bed44d72a6bfdbb539d53eff928104336f7ba9473c6b42)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1a44907e506d9d1cb4400a5be6165bfa1fd22c98dcd88b9595302a407cbf4fe3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exact", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b44e2b1b40bcead7b2ddb53cda170a736b2b6368ad3c5595068cd72876e5f3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0b79236a6abeab96a96c6154c192a8c15ecc91027a395ca22209400bbeb1dcd4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMatch")
    def put_match(self, *, exact: typing.Sequence[builtins.str]) -> None:
        '''
        :param exact: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#exact AppmeshVirtualGateway#exact}.
        '''
        value = AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch(
            exact=exact
        )

        return typing.cast(None, jsii.invoke(self, "putMatch", [value]))

    @builtins.property
    @jsii.member(jsii_name="match")
    def match(
        self,
    ) -> AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatchOutputReference:
        return typing.cast(AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatchOutputReference, jsii.get(self, "match"))

    @builtins.property
    @jsii.member(jsii_name="matchInput")
    def match_input(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch], jsii.get(self, "matchInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc293c54af82eab8fbccc58937b1a0a54b375286a95628d69337522549fba9b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrust",
    jsii_struct_bases=[],
    name_mapping={"acm": "acm", "file": "file", "sds": "sds"},
)
class AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrust:
    def __init__(
        self,
        *,
        acm: typing.Optional[typing.Union["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustAcm", typing.Dict[builtins.str, typing.Any]]] = None,
        file: typing.Optional[typing.Union["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustFile", typing.Dict[builtins.str, typing.Any]]] = None,
        sds: typing.Optional[typing.Union["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustSds", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param acm: acm block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#acm AppmeshVirtualGateway#acm}
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#file AppmeshVirtualGateway#file}
        :param sds: sds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#sds AppmeshVirtualGateway#sds}
        '''
        if isinstance(acm, dict):
            acm = AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustAcm(**acm)
        if isinstance(file, dict):
            file = AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustFile(**file)
        if isinstance(sds, dict):
            sds = AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustSds(**sds)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7cfe5c5db36f07ec1be90e0426516cba4e3c5065fbfd6717f21e406b77ec683)
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
    ) -> typing.Optional["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustAcm"]:
        '''acm block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#acm AppmeshVirtualGateway#acm}
        '''
        result = self._values.get("acm")
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustAcm"], result)

    @builtins.property
    def file(
        self,
    ) -> typing.Optional["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustFile"]:
        '''file block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#file AppmeshVirtualGateway#file}
        '''
        result = self._values.get("file")
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustFile"], result)

    @builtins.property
    def sds(
        self,
    ) -> typing.Optional["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustSds"]:
        '''sds block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#sds AppmeshVirtualGateway#sds}
        '''
        result = self._values.get("sds")
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustSds"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrust(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustAcm",
    jsii_struct_bases=[],
    name_mapping={"certificate_authority_arns": "certificateAuthorityArns"},
)
class AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustAcm:
    def __init__(
        self,
        *,
        certificate_authority_arns: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param certificate_authority_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#certificate_authority_arns AppmeshVirtualGateway#certificate_authority_arns}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b6b4b6360e32b60f300b435c01d99163e183bd5e171f81071c8a51d81cbedf3)
            check_type(argname="argument certificate_authority_arns", value=certificate_authority_arns, expected_type=type_hints["certificate_authority_arns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_authority_arns": certificate_authority_arns,
        }

    @builtins.property
    def certificate_authority_arns(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#certificate_authority_arns AppmeshVirtualGateway#certificate_authority_arns}.'''
        result = self._values.get("certificate_authority_arns")
        assert result is not None, "Required property 'certificate_authority_arns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustAcm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustAcmOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustAcmOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__101c5a07bf776a80d61e927a31f97d55049ee93ebf1a6109d4868ed84d34e64f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0039f8f8b7ab0eef4988ebf6f59099793e3644a1113542161538b75ea9fa45f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateAuthorityArns", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustAcm]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustAcm], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustAcm],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ac656b30c03084029a5b537fd9621ed49251ad50c92fd3529d684d0ea1d5259)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustFile",
    jsii_struct_bases=[],
    name_mapping={"certificate_chain": "certificateChain"},
)
class AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustFile:
    def __init__(self, *, certificate_chain: builtins.str) -> None:
        '''
        :param certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#certificate_chain AppmeshVirtualGateway#certificate_chain}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b0225f7bb3e2e59ea957b08d62928d890d498695d772734a6a67f71d811060d)
            check_type(argname="argument certificate_chain", value=certificate_chain, expected_type=type_hints["certificate_chain"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_chain": certificate_chain,
        }

    @builtins.property
    def certificate_chain(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#certificate_chain AppmeshVirtualGateway#certificate_chain}.'''
        result = self._values.get("certificate_chain")
        assert result is not None, "Required property 'certificate_chain' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustFile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustFileOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustFileOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__caf8c29d803acb0bf6dc17224d15d87fe0b4b10502fc220344356daf381306ea)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7b3645e5b544e0a70f40a9b56aa27fe18ef0aee7698b0669745c548be6c818fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateChain", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustFile]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustFile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustFile],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e191e7c47fb26e994894ff51e729004681c75ddcf243016c7987c9db98949880)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1f67ce5227bc58805f8f49bf00afb9ab280d23009f0e1b4a6509cb9307fc8103)
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
        :param certificate_authority_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#certificate_authority_arns AppmeshVirtualGateway#certificate_authority_arns}.
        '''
        value = AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustAcm(
            certificate_authority_arns=certificate_authority_arns
        )

        return typing.cast(None, jsii.invoke(self, "putAcm", [value]))

    @jsii.member(jsii_name="putFile")
    def put_file(self, *, certificate_chain: builtins.str) -> None:
        '''
        :param certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#certificate_chain AppmeshVirtualGateway#certificate_chain}.
        '''
        value = AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustFile(
            certificate_chain=certificate_chain
        )

        return typing.cast(None, jsii.invoke(self, "putFile", [value]))

    @jsii.member(jsii_name="putSds")
    def put_sds(self, *, secret_name: builtins.str) -> None:
        '''
        :param secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#secret_name AppmeshVirtualGateway#secret_name}.
        '''
        value = AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustSds(
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
    ) -> AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustAcmOutputReference:
        return typing.cast(AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustAcmOutputReference, jsii.get(self, "acm"))

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(
        self,
    ) -> AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustFileOutputReference:
        return typing.cast(AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustFileOutputReference, jsii.get(self, "file"))

    @builtins.property
    @jsii.member(jsii_name="sds")
    def sds(
        self,
    ) -> "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustSdsOutputReference":
        return typing.cast("AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustSdsOutputReference", jsii.get(self, "sds"))

    @builtins.property
    @jsii.member(jsii_name="acmInput")
    def acm_input(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustAcm]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustAcm], jsii.get(self, "acmInput"))

    @builtins.property
    @jsii.member(jsii_name="fileInput")
    def file_input(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustFile]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustFile], jsii.get(self, "fileInput"))

    @builtins.property
    @jsii.member(jsii_name="sdsInput")
    def sds_input(
        self,
    ) -> typing.Optional["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustSds"]:
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustSds"], jsii.get(self, "sdsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrust]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrust], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrust],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61b0225c2550022522b6348ebd594c8c446ff8c352394a58bd38dfb9f3ea4235)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustSds",
    jsii_struct_bases=[],
    name_mapping={"secret_name": "secretName"},
)
class AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustSds:
    def __init__(self, *, secret_name: builtins.str) -> None:
        '''
        :param secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#secret_name AppmeshVirtualGateway#secret_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8242aa7415f062e143839a71d715664ae19e9eb99b4c7aad9d00aea89a58629b)
            check_type(argname="argument secret_name", value=secret_name, expected_type=type_hints["secret_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "secret_name": secret_name,
        }

    @builtins.property
    def secret_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#secret_name AppmeshVirtualGateway#secret_name}.'''
        result = self._values.get("secret_name")
        assert result is not None, "Required property 'secret_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustSds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustSdsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustSdsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2df0199998bbcd697c05ba1ccae64302e92918263680b6b143d6b6dd19df7ba7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7d73c90a0f8b4ea072fcdd87c0aaaa6f32af106ef2227d4d6eb79c6a394a3c00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustSds]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustSds], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustSds],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35e062f3603ef142c6b250d2b734c744ea86b25231116e3b6d1de957470c66bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualGatewaySpecBackendDefaultsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecBackendDefaultsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__40ba99a787445d24cd3bc1910a93d0ec16adb62ad8c37208edd4f967ff02b427)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putClientPolicy")
    def put_client_policy(
        self,
        *,
        tls: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTls, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param tls: tls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#tls AppmeshVirtualGateway#tls}
        '''
        value = AppmeshVirtualGatewaySpecBackendDefaultsClientPolicy(tls=tls)

        return typing.cast(None, jsii.invoke(self, "putClientPolicy", [value]))

    @jsii.member(jsii_name="resetClientPolicy")
    def reset_client_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientPolicy", []))

    @builtins.property
    @jsii.member(jsii_name="clientPolicy")
    def client_policy(
        self,
    ) -> AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyOutputReference:
        return typing.cast(AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyOutputReference, jsii.get(self, "clientPolicy"))

    @builtins.property
    @jsii.member(jsii_name="clientPolicyInput")
    def client_policy_input(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicy]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicy], jsii.get(self, "clientPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecBackendDefaults]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecBackendDefaults], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualGatewaySpecBackendDefaults],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea6da4dbc3b2e4c43803b9bb5ec15fb19eeb8933976bde501b7f91ccacc1b74d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecListener",
    jsii_struct_bases=[],
    name_mapping={
        "port_mapping": "portMapping",
        "connection_pool": "connectionPool",
        "health_check": "healthCheck",
        "tls": "tls",
    },
)
class AppmeshVirtualGatewaySpecListener:
    def __init__(
        self,
        *,
        port_mapping: typing.Union["AppmeshVirtualGatewaySpecListenerPortMapping", typing.Dict[builtins.str, typing.Any]],
        connection_pool: typing.Optional[typing.Union["AppmeshVirtualGatewaySpecListenerConnectionPool", typing.Dict[builtins.str, typing.Any]]] = None,
        health_check: typing.Optional[typing.Union["AppmeshVirtualGatewaySpecListenerHealthCheck", typing.Dict[builtins.str, typing.Any]]] = None,
        tls: typing.Optional[typing.Union["AppmeshVirtualGatewaySpecListenerTls", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param port_mapping: port_mapping block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#port_mapping AppmeshVirtualGateway#port_mapping}
        :param connection_pool: connection_pool block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#connection_pool AppmeshVirtualGateway#connection_pool}
        :param health_check: health_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#health_check AppmeshVirtualGateway#health_check}
        :param tls: tls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#tls AppmeshVirtualGateway#tls}
        '''
        if isinstance(port_mapping, dict):
            port_mapping = AppmeshVirtualGatewaySpecListenerPortMapping(**port_mapping)
        if isinstance(connection_pool, dict):
            connection_pool = AppmeshVirtualGatewaySpecListenerConnectionPool(**connection_pool)
        if isinstance(health_check, dict):
            health_check = AppmeshVirtualGatewaySpecListenerHealthCheck(**health_check)
        if isinstance(tls, dict):
            tls = AppmeshVirtualGatewaySpecListenerTls(**tls)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e12c4676792fb05e812299033c8ef3e39a5983c0fdd227cdddbb5b7206a6df7d)
            check_type(argname="argument port_mapping", value=port_mapping, expected_type=type_hints["port_mapping"])
            check_type(argname="argument connection_pool", value=connection_pool, expected_type=type_hints["connection_pool"])
            check_type(argname="argument health_check", value=health_check, expected_type=type_hints["health_check"])
            check_type(argname="argument tls", value=tls, expected_type=type_hints["tls"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "port_mapping": port_mapping,
        }
        if connection_pool is not None:
            self._values["connection_pool"] = connection_pool
        if health_check is not None:
            self._values["health_check"] = health_check
        if tls is not None:
            self._values["tls"] = tls

    @builtins.property
    def port_mapping(self) -> "AppmeshVirtualGatewaySpecListenerPortMapping":
        '''port_mapping block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#port_mapping AppmeshVirtualGateway#port_mapping}
        '''
        result = self._values.get("port_mapping")
        assert result is not None, "Required property 'port_mapping' is missing"
        return typing.cast("AppmeshVirtualGatewaySpecListenerPortMapping", result)

    @builtins.property
    def connection_pool(
        self,
    ) -> typing.Optional["AppmeshVirtualGatewaySpecListenerConnectionPool"]:
        '''connection_pool block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#connection_pool AppmeshVirtualGateway#connection_pool}
        '''
        result = self._values.get("connection_pool")
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecListenerConnectionPool"], result)

    @builtins.property
    def health_check(
        self,
    ) -> typing.Optional["AppmeshVirtualGatewaySpecListenerHealthCheck"]:
        '''health_check block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#health_check AppmeshVirtualGateway#health_check}
        '''
        result = self._values.get("health_check")
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecListenerHealthCheck"], result)

    @builtins.property
    def tls(self) -> typing.Optional["AppmeshVirtualGatewaySpecListenerTls"]:
        '''tls block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#tls AppmeshVirtualGateway#tls}
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecListenerTls"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualGatewaySpecListener(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecListenerConnectionPool",
    jsii_struct_bases=[],
    name_mapping={"grpc": "grpc", "http": "http", "http2": "http2"},
)
class AppmeshVirtualGatewaySpecListenerConnectionPool:
    def __init__(
        self,
        *,
        grpc: typing.Optional[typing.Union["AppmeshVirtualGatewaySpecListenerConnectionPoolGrpc", typing.Dict[builtins.str, typing.Any]]] = None,
        http: typing.Optional[typing.Union["AppmeshVirtualGatewaySpecListenerConnectionPoolHttp", typing.Dict[builtins.str, typing.Any]]] = None,
        http2: typing.Optional[typing.Union["AppmeshVirtualGatewaySpecListenerConnectionPoolHttp2", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param grpc: grpc block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#grpc AppmeshVirtualGateway#grpc}
        :param http: http block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#http AppmeshVirtualGateway#http}
        :param http2: http2 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#http2 AppmeshVirtualGateway#http2}
        '''
        if isinstance(grpc, dict):
            grpc = AppmeshVirtualGatewaySpecListenerConnectionPoolGrpc(**grpc)
        if isinstance(http, dict):
            http = AppmeshVirtualGatewaySpecListenerConnectionPoolHttp(**http)
        if isinstance(http2, dict):
            http2 = AppmeshVirtualGatewaySpecListenerConnectionPoolHttp2(**http2)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__578f10035e25b361c9e00808a5738a234d9ba43549c148944b583c80873b8d5a)
            check_type(argname="argument grpc", value=grpc, expected_type=type_hints["grpc"])
            check_type(argname="argument http", value=http, expected_type=type_hints["http"])
            check_type(argname="argument http2", value=http2, expected_type=type_hints["http2"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if grpc is not None:
            self._values["grpc"] = grpc
        if http is not None:
            self._values["http"] = http
        if http2 is not None:
            self._values["http2"] = http2

    @builtins.property
    def grpc(
        self,
    ) -> typing.Optional["AppmeshVirtualGatewaySpecListenerConnectionPoolGrpc"]:
        '''grpc block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#grpc AppmeshVirtualGateway#grpc}
        '''
        result = self._values.get("grpc")
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecListenerConnectionPoolGrpc"], result)

    @builtins.property
    def http(
        self,
    ) -> typing.Optional["AppmeshVirtualGatewaySpecListenerConnectionPoolHttp"]:
        '''http block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#http AppmeshVirtualGateway#http}
        '''
        result = self._values.get("http")
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecListenerConnectionPoolHttp"], result)

    @builtins.property
    def http2(
        self,
    ) -> typing.Optional["AppmeshVirtualGatewaySpecListenerConnectionPoolHttp2"]:
        '''http2 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#http2 AppmeshVirtualGateway#http2}
        '''
        result = self._values.get("http2")
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecListenerConnectionPoolHttp2"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualGatewaySpecListenerConnectionPool(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecListenerConnectionPoolGrpc",
    jsii_struct_bases=[],
    name_mapping={"max_requests": "maxRequests"},
)
class AppmeshVirtualGatewaySpecListenerConnectionPoolGrpc:
    def __init__(self, *, max_requests: jsii.Number) -> None:
        '''
        :param max_requests: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#max_requests AppmeshVirtualGateway#max_requests}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a9c9c85a7aabd074e4ee4f69ff7c44cecee3fb8fa8f8e1141b304d99f60c1f4)
            check_type(argname="argument max_requests", value=max_requests, expected_type=type_hints["max_requests"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "max_requests": max_requests,
        }

    @builtins.property
    def max_requests(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#max_requests AppmeshVirtualGateway#max_requests}.'''
        result = self._values.get("max_requests")
        assert result is not None, "Required property 'max_requests' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualGatewaySpecListenerConnectionPoolGrpc(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualGatewaySpecListenerConnectionPoolGrpcOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecListenerConnectionPoolGrpcOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e629b1bc76eed0d626a2d78fcf5082613972fd3e25bd9435338d839cfe3bf79c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c23c9f13b84e9298acde25a347372436b68f7b5298ddbc997baaf17accd3ff14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxRequests", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecListenerConnectionPoolGrpc]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecListenerConnectionPoolGrpc], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualGatewaySpecListenerConnectionPoolGrpc],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1481205a71b8eec028bcab5e600a1d33220a95c6dc0aafa0feb810a713f4dfbf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecListenerConnectionPoolHttp",
    jsii_struct_bases=[],
    name_mapping={
        "max_connections": "maxConnections",
        "max_pending_requests": "maxPendingRequests",
    },
)
class AppmeshVirtualGatewaySpecListenerConnectionPoolHttp:
    def __init__(
        self,
        *,
        max_connections: jsii.Number,
        max_pending_requests: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_connections: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#max_connections AppmeshVirtualGateway#max_connections}.
        :param max_pending_requests: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#max_pending_requests AppmeshVirtualGateway#max_pending_requests}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6184b5b48eadf4f324354085675ec6fe8c3d1d0053879413a863106a109d92a)
            check_type(argname="argument max_connections", value=max_connections, expected_type=type_hints["max_connections"])
            check_type(argname="argument max_pending_requests", value=max_pending_requests, expected_type=type_hints["max_pending_requests"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "max_connections": max_connections,
        }
        if max_pending_requests is not None:
            self._values["max_pending_requests"] = max_pending_requests

    @builtins.property
    def max_connections(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#max_connections AppmeshVirtualGateway#max_connections}.'''
        result = self._values.get("max_connections")
        assert result is not None, "Required property 'max_connections' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def max_pending_requests(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#max_pending_requests AppmeshVirtualGateway#max_pending_requests}.'''
        result = self._values.get("max_pending_requests")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualGatewaySpecListenerConnectionPoolHttp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecListenerConnectionPoolHttp2",
    jsii_struct_bases=[],
    name_mapping={"max_requests": "maxRequests"},
)
class AppmeshVirtualGatewaySpecListenerConnectionPoolHttp2:
    def __init__(self, *, max_requests: jsii.Number) -> None:
        '''
        :param max_requests: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#max_requests AppmeshVirtualGateway#max_requests}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a78a848031d352a41112cde4478811ce3b2bb9daf34b63850ade57a32cdcc89d)
            check_type(argname="argument max_requests", value=max_requests, expected_type=type_hints["max_requests"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "max_requests": max_requests,
        }

    @builtins.property
    def max_requests(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#max_requests AppmeshVirtualGateway#max_requests}.'''
        result = self._values.get("max_requests")
        assert result is not None, "Required property 'max_requests' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualGatewaySpecListenerConnectionPoolHttp2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualGatewaySpecListenerConnectionPoolHttp2OutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecListenerConnectionPoolHttp2OutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fd6e80b554b000a82741807fc15763c75ac4f6183695ea67b2731b572ba5fd90)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0d1bde3d069d29af42734d79a5fff4d9e363975348bc8bc79489ae2198e84f18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxRequests", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecListenerConnectionPoolHttp2]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecListenerConnectionPoolHttp2], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualGatewaySpecListenerConnectionPoolHttp2],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1154ea49d3d95383b0b635c474ac3a936f3cc02fa2d24ee106b79427905e5f65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualGatewaySpecListenerConnectionPoolHttpOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecListenerConnectionPoolHttpOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5570db8eff3b42349e065790cc409bc3e3799934d64b24627de0c11889c2276b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__90b88e05d361ebae5639f15ccef767b814eb726cf6856cfb14b9957065725f93)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConnections", value)

    @builtins.property
    @jsii.member(jsii_name="maxPendingRequests")
    def max_pending_requests(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxPendingRequests"))

    @max_pending_requests.setter
    def max_pending_requests(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63b0cd6ba3cc5309462f9c1400f93cde9b4fd58b85cc17950086842130addd35)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxPendingRequests", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecListenerConnectionPoolHttp]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecListenerConnectionPoolHttp], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualGatewaySpecListenerConnectionPoolHttp],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c699f253ca9fd3f55ef413fe9a958251356fd4fe6d85bd22cb94008e0c38006a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualGatewaySpecListenerConnectionPoolOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecListenerConnectionPoolOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__289783099bdb2a51f7c549c05ce173d744a88e639e6266420e90354d60122c7d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putGrpc")
    def put_grpc(self, *, max_requests: jsii.Number) -> None:
        '''
        :param max_requests: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#max_requests AppmeshVirtualGateway#max_requests}.
        '''
        value = AppmeshVirtualGatewaySpecListenerConnectionPoolGrpc(
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
        :param max_connections: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#max_connections AppmeshVirtualGateway#max_connections}.
        :param max_pending_requests: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#max_pending_requests AppmeshVirtualGateway#max_pending_requests}.
        '''
        value = AppmeshVirtualGatewaySpecListenerConnectionPoolHttp(
            max_connections=max_connections, max_pending_requests=max_pending_requests
        )

        return typing.cast(None, jsii.invoke(self, "putHttp", [value]))

    @jsii.member(jsii_name="putHttp2")
    def put_http2(self, *, max_requests: jsii.Number) -> None:
        '''
        :param max_requests: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#max_requests AppmeshVirtualGateway#max_requests}.
        '''
        value = AppmeshVirtualGatewaySpecListenerConnectionPoolHttp2(
            max_requests=max_requests
        )

        return typing.cast(None, jsii.invoke(self, "putHttp2", [value]))

    @jsii.member(jsii_name="resetGrpc")
    def reset_grpc(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGrpc", []))

    @jsii.member(jsii_name="resetHttp")
    def reset_http(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttp", []))

    @jsii.member(jsii_name="resetHttp2")
    def reset_http2(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttp2", []))

    @builtins.property
    @jsii.member(jsii_name="grpc")
    def grpc(
        self,
    ) -> AppmeshVirtualGatewaySpecListenerConnectionPoolGrpcOutputReference:
        return typing.cast(AppmeshVirtualGatewaySpecListenerConnectionPoolGrpcOutputReference, jsii.get(self, "grpc"))

    @builtins.property
    @jsii.member(jsii_name="http")
    def http(
        self,
    ) -> AppmeshVirtualGatewaySpecListenerConnectionPoolHttpOutputReference:
        return typing.cast(AppmeshVirtualGatewaySpecListenerConnectionPoolHttpOutputReference, jsii.get(self, "http"))

    @builtins.property
    @jsii.member(jsii_name="http2")
    def http2(
        self,
    ) -> AppmeshVirtualGatewaySpecListenerConnectionPoolHttp2OutputReference:
        return typing.cast(AppmeshVirtualGatewaySpecListenerConnectionPoolHttp2OutputReference, jsii.get(self, "http2"))

    @builtins.property
    @jsii.member(jsii_name="grpcInput")
    def grpc_input(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecListenerConnectionPoolGrpc]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecListenerConnectionPoolGrpc], jsii.get(self, "grpcInput"))

    @builtins.property
    @jsii.member(jsii_name="http2Input")
    def http2_input(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecListenerConnectionPoolHttp2]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecListenerConnectionPoolHttp2], jsii.get(self, "http2Input"))

    @builtins.property
    @jsii.member(jsii_name="httpInput")
    def http_input(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecListenerConnectionPoolHttp]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecListenerConnectionPoolHttp], jsii.get(self, "httpInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecListenerConnectionPool]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecListenerConnectionPool], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualGatewaySpecListenerConnectionPool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cd676bba3b66f5fe78a55bacd3b47925108db919e303dbebf5fda24367802ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecListenerHealthCheck",
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
class AppmeshVirtualGatewaySpecListenerHealthCheck:
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
        :param healthy_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#healthy_threshold AppmeshVirtualGateway#healthy_threshold}.
        :param interval_millis: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#interval_millis AppmeshVirtualGateway#interval_millis}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#protocol AppmeshVirtualGateway#protocol}.
        :param timeout_millis: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#timeout_millis AppmeshVirtualGateway#timeout_millis}.
        :param unhealthy_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#unhealthy_threshold AppmeshVirtualGateway#unhealthy_threshold}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#path AppmeshVirtualGateway#path}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#port AppmeshVirtualGateway#port}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31e2ae56dbe3006e6330291e03d3fce89c5eb64b1560aa09ebaddb7b6abd3d38)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#healthy_threshold AppmeshVirtualGateway#healthy_threshold}.'''
        result = self._values.get("healthy_threshold")
        assert result is not None, "Required property 'healthy_threshold' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def interval_millis(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#interval_millis AppmeshVirtualGateway#interval_millis}.'''
        result = self._values.get("interval_millis")
        assert result is not None, "Required property 'interval_millis' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#protocol AppmeshVirtualGateway#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def timeout_millis(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#timeout_millis AppmeshVirtualGateway#timeout_millis}.'''
        result = self._values.get("timeout_millis")
        assert result is not None, "Required property 'timeout_millis' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def unhealthy_threshold(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#unhealthy_threshold AppmeshVirtualGateway#unhealthy_threshold}.'''
        result = self._values.get("unhealthy_threshold")
        assert result is not None, "Required property 'unhealthy_threshold' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#path AppmeshVirtualGateway#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#port AppmeshVirtualGateway#port}.'''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualGatewaySpecListenerHealthCheck(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualGatewaySpecListenerHealthCheckOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecListenerHealthCheckOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ef98379b970b417eb782a5ef2e18232a017fc249ae399e87d927c12ea46490ac)
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
            type_hints = typing.get_type_hints(_typecheckingstub__240878609b70ddfd16e6df958d567a71643f1314ead9af65f1e70f83876bc6a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthyThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="intervalMillis")
    def interval_millis(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "intervalMillis"))

    @interval_millis.setter
    def interval_millis(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8b7998354c42d3793bc38995a0b995085030df9106a25c3a773ae4147e081f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intervalMillis", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__760af830f2dcb1696c4af3b8f595b747a5ed8585c435125af7e17e0207c2d071)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ba577fdd1039932ef49ca9740e4ccabc6c9f55236cb03f42b4c2eb742ce7490)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a30090bf2d38e89268196f657b6a63b1ae8c3a1e84bddcc888b834d5091118e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutMillis")
    def timeout_millis(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutMillis"))

    @timeout_millis.setter
    def timeout_millis(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9b128e11c054b86f8918c137b2d55886c10b5983189e43347211a82ffc5fcd5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutMillis", value)

    @builtins.property
    @jsii.member(jsii_name="unhealthyThreshold")
    def unhealthy_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "unhealthyThreshold"))

    @unhealthy_threshold.setter
    def unhealthy_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44454b9d70f8ceca300409dbad89991f58905d0fa5eca0072353b3cdccddcf9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unhealthyThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecListenerHealthCheck]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecListenerHealthCheck], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualGatewaySpecListenerHealthCheck],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6f595ef975664e29437a813c01f29684140f15acd4764ddeb373d0209e51857)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualGatewaySpecListenerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecListenerOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0f0b38866c928442d74560296ce698ea58432ed880e1dc4b1d08821ca79a0ca9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putConnectionPool")
    def put_connection_pool(
        self,
        *,
        grpc: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecListenerConnectionPoolGrpc, typing.Dict[builtins.str, typing.Any]]] = None,
        http: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecListenerConnectionPoolHttp, typing.Dict[builtins.str, typing.Any]]] = None,
        http2: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecListenerConnectionPoolHttp2, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param grpc: grpc block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#grpc AppmeshVirtualGateway#grpc}
        :param http: http block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#http AppmeshVirtualGateway#http}
        :param http2: http2 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#http2 AppmeshVirtualGateway#http2}
        '''
        value = AppmeshVirtualGatewaySpecListenerConnectionPool(
            grpc=grpc, http=http, http2=http2
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
        :param healthy_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#healthy_threshold AppmeshVirtualGateway#healthy_threshold}.
        :param interval_millis: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#interval_millis AppmeshVirtualGateway#interval_millis}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#protocol AppmeshVirtualGateway#protocol}.
        :param timeout_millis: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#timeout_millis AppmeshVirtualGateway#timeout_millis}.
        :param unhealthy_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#unhealthy_threshold AppmeshVirtualGateway#unhealthy_threshold}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#path AppmeshVirtualGateway#path}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#port AppmeshVirtualGateway#port}.
        '''
        value = AppmeshVirtualGatewaySpecListenerHealthCheck(
            healthy_threshold=healthy_threshold,
            interval_millis=interval_millis,
            protocol=protocol,
            timeout_millis=timeout_millis,
            unhealthy_threshold=unhealthy_threshold,
            path=path,
            port=port,
        )

        return typing.cast(None, jsii.invoke(self, "putHealthCheck", [value]))

    @jsii.member(jsii_name="putPortMapping")
    def put_port_mapping(self, *, port: jsii.Number, protocol: builtins.str) -> None:
        '''
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#port AppmeshVirtualGateway#port}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#protocol AppmeshVirtualGateway#protocol}.
        '''
        value = AppmeshVirtualGatewaySpecListenerPortMapping(
            port=port, protocol=protocol
        )

        return typing.cast(None, jsii.invoke(self, "putPortMapping", [value]))

    @jsii.member(jsii_name="putTls")
    def put_tls(
        self,
        *,
        certificate: typing.Union["AppmeshVirtualGatewaySpecListenerTlsCertificate", typing.Dict[builtins.str, typing.Any]],
        mode: builtins.str,
        validation: typing.Optional[typing.Union["AppmeshVirtualGatewaySpecListenerTlsValidation", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param certificate: certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#certificate AppmeshVirtualGateway#certificate}
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#mode AppmeshVirtualGateway#mode}.
        :param validation: validation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#validation AppmeshVirtualGateway#validation}
        '''
        value = AppmeshVirtualGatewaySpecListenerTls(
            certificate=certificate, mode=mode, validation=validation
        )

        return typing.cast(None, jsii.invoke(self, "putTls", [value]))

    @jsii.member(jsii_name="resetConnectionPool")
    def reset_connection_pool(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionPool", []))

    @jsii.member(jsii_name="resetHealthCheck")
    def reset_health_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheck", []))

    @jsii.member(jsii_name="resetTls")
    def reset_tls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTls", []))

    @builtins.property
    @jsii.member(jsii_name="connectionPool")
    def connection_pool(
        self,
    ) -> AppmeshVirtualGatewaySpecListenerConnectionPoolOutputReference:
        return typing.cast(AppmeshVirtualGatewaySpecListenerConnectionPoolOutputReference, jsii.get(self, "connectionPool"))

    @builtins.property
    @jsii.member(jsii_name="healthCheck")
    def health_check(
        self,
    ) -> AppmeshVirtualGatewaySpecListenerHealthCheckOutputReference:
        return typing.cast(AppmeshVirtualGatewaySpecListenerHealthCheckOutputReference, jsii.get(self, "healthCheck"))

    @builtins.property
    @jsii.member(jsii_name="portMapping")
    def port_mapping(
        self,
    ) -> "AppmeshVirtualGatewaySpecListenerPortMappingOutputReference":
        return typing.cast("AppmeshVirtualGatewaySpecListenerPortMappingOutputReference", jsii.get(self, "portMapping"))

    @builtins.property
    @jsii.member(jsii_name="tls")
    def tls(self) -> "AppmeshVirtualGatewaySpecListenerTlsOutputReference":
        return typing.cast("AppmeshVirtualGatewaySpecListenerTlsOutputReference", jsii.get(self, "tls"))

    @builtins.property
    @jsii.member(jsii_name="connectionPoolInput")
    def connection_pool_input(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecListenerConnectionPool]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecListenerConnectionPool], jsii.get(self, "connectionPoolInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckInput")
    def health_check_input(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecListenerHealthCheck]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecListenerHealthCheck], jsii.get(self, "healthCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="portMappingInput")
    def port_mapping_input(
        self,
    ) -> typing.Optional["AppmeshVirtualGatewaySpecListenerPortMapping"]:
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecListenerPortMapping"], jsii.get(self, "portMappingInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsInput")
    def tls_input(self) -> typing.Optional["AppmeshVirtualGatewaySpecListenerTls"]:
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecListenerTls"], jsii.get(self, "tlsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshVirtualGatewaySpecListener]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecListener], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualGatewaySpecListener],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__967eb6060b62444e534a53409762f85ee01957eba41bbdbd494422913cc484b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecListenerPortMapping",
    jsii_struct_bases=[],
    name_mapping={"port": "port", "protocol": "protocol"},
)
class AppmeshVirtualGatewaySpecListenerPortMapping:
    def __init__(self, *, port: jsii.Number, protocol: builtins.str) -> None:
        '''
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#port AppmeshVirtualGateway#port}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#protocol AppmeshVirtualGateway#protocol}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__665e63b6d728face43c8708ad1f3805811f66761649000fffccc7879eee465f3)
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "port": port,
            "protocol": protocol,
        }

    @builtins.property
    def port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#port AppmeshVirtualGateway#port}.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#protocol AppmeshVirtualGateway#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualGatewaySpecListenerPortMapping(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualGatewaySpecListenerPortMappingOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecListenerPortMappingOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__42c9907d3ccb5d958ec66dfe079080cff58b62ce32f450c6aafd09e29bbec094)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8ca4347ad72c1d319bb9dd836853a7da0606e1a578e86250d6d09c6ea03c62c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c921274ad3dcf5e331cf937a8f3a493e3b91b448b138073d9cf601f0bec1b8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecListenerPortMapping]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecListenerPortMapping], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualGatewaySpecListenerPortMapping],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__710ae9f04d2774c3dc80aa59876d01bc145a51f6ef22a583fbf5b873bcd6a05f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecListenerTls",
    jsii_struct_bases=[],
    name_mapping={
        "certificate": "certificate",
        "mode": "mode",
        "validation": "validation",
    },
)
class AppmeshVirtualGatewaySpecListenerTls:
    def __init__(
        self,
        *,
        certificate: typing.Union["AppmeshVirtualGatewaySpecListenerTlsCertificate", typing.Dict[builtins.str, typing.Any]],
        mode: builtins.str,
        validation: typing.Optional[typing.Union["AppmeshVirtualGatewaySpecListenerTlsValidation", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param certificate: certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#certificate AppmeshVirtualGateway#certificate}
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#mode AppmeshVirtualGateway#mode}.
        :param validation: validation block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#validation AppmeshVirtualGateway#validation}
        '''
        if isinstance(certificate, dict):
            certificate = AppmeshVirtualGatewaySpecListenerTlsCertificate(**certificate)
        if isinstance(validation, dict):
            validation = AppmeshVirtualGatewaySpecListenerTlsValidation(**validation)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c7bd8f89cc89b7cef60d6f4f5a67563f1306fec01cf13f45357ab72dd889557)
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
    def certificate(self) -> "AppmeshVirtualGatewaySpecListenerTlsCertificate":
        '''certificate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#certificate AppmeshVirtualGateway#certificate}
        '''
        result = self._values.get("certificate")
        assert result is not None, "Required property 'certificate' is missing"
        return typing.cast("AppmeshVirtualGatewaySpecListenerTlsCertificate", result)

    @builtins.property
    def mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#mode AppmeshVirtualGateway#mode}.'''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def validation(
        self,
    ) -> typing.Optional["AppmeshVirtualGatewaySpecListenerTlsValidation"]:
        '''validation block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#validation AppmeshVirtualGateway#validation}
        '''
        result = self._values.get("validation")
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecListenerTlsValidation"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualGatewaySpecListenerTls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecListenerTlsCertificate",
    jsii_struct_bases=[],
    name_mapping={"acm": "acm", "file": "file", "sds": "sds"},
)
class AppmeshVirtualGatewaySpecListenerTlsCertificate:
    def __init__(
        self,
        *,
        acm: typing.Optional[typing.Union["AppmeshVirtualGatewaySpecListenerTlsCertificateAcm", typing.Dict[builtins.str, typing.Any]]] = None,
        file: typing.Optional[typing.Union["AppmeshVirtualGatewaySpecListenerTlsCertificateFile", typing.Dict[builtins.str, typing.Any]]] = None,
        sds: typing.Optional[typing.Union["AppmeshVirtualGatewaySpecListenerTlsCertificateSds", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param acm: acm block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#acm AppmeshVirtualGateway#acm}
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#file AppmeshVirtualGateway#file}
        :param sds: sds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#sds AppmeshVirtualGateway#sds}
        '''
        if isinstance(acm, dict):
            acm = AppmeshVirtualGatewaySpecListenerTlsCertificateAcm(**acm)
        if isinstance(file, dict):
            file = AppmeshVirtualGatewaySpecListenerTlsCertificateFile(**file)
        if isinstance(sds, dict):
            sds = AppmeshVirtualGatewaySpecListenerTlsCertificateSds(**sds)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__edcd8a8b22ff8290bd05f0d420575ea909a12a637c6669dcd628556165437040)
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
    ) -> typing.Optional["AppmeshVirtualGatewaySpecListenerTlsCertificateAcm"]:
        '''acm block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#acm AppmeshVirtualGateway#acm}
        '''
        result = self._values.get("acm")
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecListenerTlsCertificateAcm"], result)

    @builtins.property
    def file(
        self,
    ) -> typing.Optional["AppmeshVirtualGatewaySpecListenerTlsCertificateFile"]:
        '''file block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#file AppmeshVirtualGateway#file}
        '''
        result = self._values.get("file")
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecListenerTlsCertificateFile"], result)

    @builtins.property
    def sds(
        self,
    ) -> typing.Optional["AppmeshVirtualGatewaySpecListenerTlsCertificateSds"]:
        '''sds block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#sds AppmeshVirtualGateway#sds}
        '''
        result = self._values.get("sds")
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecListenerTlsCertificateSds"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualGatewaySpecListenerTlsCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecListenerTlsCertificateAcm",
    jsii_struct_bases=[],
    name_mapping={"certificate_arn": "certificateArn"},
)
class AppmeshVirtualGatewaySpecListenerTlsCertificateAcm:
    def __init__(self, *, certificate_arn: builtins.str) -> None:
        '''
        :param certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#certificate_arn AppmeshVirtualGateway#certificate_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c6baa7dfc57b8f8c952c0dea9e34c8bd2685e155688ebe940c7cbae65d912b0)
            check_type(argname="argument certificate_arn", value=certificate_arn, expected_type=type_hints["certificate_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_arn": certificate_arn,
        }

    @builtins.property
    def certificate_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#certificate_arn AppmeshVirtualGateway#certificate_arn}.'''
        result = self._values.get("certificate_arn")
        assert result is not None, "Required property 'certificate_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualGatewaySpecListenerTlsCertificateAcm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualGatewaySpecListenerTlsCertificateAcmOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecListenerTlsCertificateAcmOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0d2c86e353876775502258d0482263124ad943f19d6cad943a887c52873c4407)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9e241fac4176da75e5ae06b02971dec37f93df842b39cbf7e64220f5643f02b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecListenerTlsCertificateAcm]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecListenerTlsCertificateAcm], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualGatewaySpecListenerTlsCertificateAcm],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08838b3a968155deb038101de1e1db9f3f0af4a01abaabe3bb79626edcf50dea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecListenerTlsCertificateFile",
    jsii_struct_bases=[],
    name_mapping={
        "certificate_chain": "certificateChain",
        "private_key": "privateKey",
    },
)
class AppmeshVirtualGatewaySpecListenerTlsCertificateFile:
    def __init__(
        self,
        *,
        certificate_chain: builtins.str,
        private_key: builtins.str,
    ) -> None:
        '''
        :param certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#certificate_chain AppmeshVirtualGateway#certificate_chain}.
        :param private_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#private_key AppmeshVirtualGateway#private_key}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26875efe6083df16a96b262489e362a9beca1abb17355a5abece6b557a5a38a3)
            check_type(argname="argument certificate_chain", value=certificate_chain, expected_type=type_hints["certificate_chain"])
            check_type(argname="argument private_key", value=private_key, expected_type=type_hints["private_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_chain": certificate_chain,
            "private_key": private_key,
        }

    @builtins.property
    def certificate_chain(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#certificate_chain AppmeshVirtualGateway#certificate_chain}.'''
        result = self._values.get("certificate_chain")
        assert result is not None, "Required property 'certificate_chain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def private_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#private_key AppmeshVirtualGateway#private_key}.'''
        result = self._values.get("private_key")
        assert result is not None, "Required property 'private_key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualGatewaySpecListenerTlsCertificateFile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualGatewaySpecListenerTlsCertificateFileOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecListenerTlsCertificateFileOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bff3493b4e9a12c95f2fabe2010b9a14651edeb112d0de62196505d8d4da008c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__00e119931f78d91d9015fc2d065a9c32d7e54264e481d96a6090beb264c8edaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateChain", value)

    @builtins.property
    @jsii.member(jsii_name="privateKey")
    def private_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateKey"))

    @private_key.setter
    def private_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__022fa3957bf559d9e8e2db6c85a7cb8564f6b1a29abdc3e4646782a859ea4660)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecListenerTlsCertificateFile]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecListenerTlsCertificateFile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualGatewaySpecListenerTlsCertificateFile],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da99c97a7e005c5a33c48551aefbfc5d098efa7127af7b443a9e1b3ab664a6b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualGatewaySpecListenerTlsCertificateOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecListenerTlsCertificateOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__95ed6950ed31a7e8e9ab7a8a879187638f73e68f5fdda5d9844ec80d2fce2b7a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAcm")
    def put_acm(self, *, certificate_arn: builtins.str) -> None:
        '''
        :param certificate_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#certificate_arn AppmeshVirtualGateway#certificate_arn}.
        '''
        value = AppmeshVirtualGatewaySpecListenerTlsCertificateAcm(
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
        :param certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#certificate_chain AppmeshVirtualGateway#certificate_chain}.
        :param private_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#private_key AppmeshVirtualGateway#private_key}.
        '''
        value = AppmeshVirtualGatewaySpecListenerTlsCertificateFile(
            certificate_chain=certificate_chain, private_key=private_key
        )

        return typing.cast(None, jsii.invoke(self, "putFile", [value]))

    @jsii.member(jsii_name="putSds")
    def put_sds(self, *, secret_name: builtins.str) -> None:
        '''
        :param secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#secret_name AppmeshVirtualGateway#secret_name}.
        '''
        value = AppmeshVirtualGatewaySpecListenerTlsCertificateSds(
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
    def acm(self) -> AppmeshVirtualGatewaySpecListenerTlsCertificateAcmOutputReference:
        return typing.cast(AppmeshVirtualGatewaySpecListenerTlsCertificateAcmOutputReference, jsii.get(self, "acm"))

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(
        self,
    ) -> AppmeshVirtualGatewaySpecListenerTlsCertificateFileOutputReference:
        return typing.cast(AppmeshVirtualGatewaySpecListenerTlsCertificateFileOutputReference, jsii.get(self, "file"))

    @builtins.property
    @jsii.member(jsii_name="sds")
    def sds(
        self,
    ) -> "AppmeshVirtualGatewaySpecListenerTlsCertificateSdsOutputReference":
        return typing.cast("AppmeshVirtualGatewaySpecListenerTlsCertificateSdsOutputReference", jsii.get(self, "sds"))

    @builtins.property
    @jsii.member(jsii_name="acmInput")
    def acm_input(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecListenerTlsCertificateAcm]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecListenerTlsCertificateAcm], jsii.get(self, "acmInput"))

    @builtins.property
    @jsii.member(jsii_name="fileInput")
    def file_input(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecListenerTlsCertificateFile]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecListenerTlsCertificateFile], jsii.get(self, "fileInput"))

    @builtins.property
    @jsii.member(jsii_name="sdsInput")
    def sds_input(
        self,
    ) -> typing.Optional["AppmeshVirtualGatewaySpecListenerTlsCertificateSds"]:
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecListenerTlsCertificateSds"], jsii.get(self, "sdsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecListenerTlsCertificate]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecListenerTlsCertificate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualGatewaySpecListenerTlsCertificate],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__521844dd8f6c9ee3bdd5b9a20b434c206c9871bae52bf615cb9b0be365b01bf5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecListenerTlsCertificateSds",
    jsii_struct_bases=[],
    name_mapping={"secret_name": "secretName"},
)
class AppmeshVirtualGatewaySpecListenerTlsCertificateSds:
    def __init__(self, *, secret_name: builtins.str) -> None:
        '''
        :param secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#secret_name AppmeshVirtualGateway#secret_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3fe1723b665935bd27782455a9bd60963469ca09ce1c5ce750abfbd5e0be1f3)
            check_type(argname="argument secret_name", value=secret_name, expected_type=type_hints["secret_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "secret_name": secret_name,
        }

    @builtins.property
    def secret_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#secret_name AppmeshVirtualGateway#secret_name}.'''
        result = self._values.get("secret_name")
        assert result is not None, "Required property 'secret_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualGatewaySpecListenerTlsCertificateSds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualGatewaySpecListenerTlsCertificateSdsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecListenerTlsCertificateSdsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5779d01be8347acdaef1e69600b3292eb19bd6d93eb8576ea227ff624b028a8d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__afed7e0d7618fa93dde04cd6d2f676873f654eeba7fd9c2c616172486027bcfa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecListenerTlsCertificateSds]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecListenerTlsCertificateSds], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualGatewaySpecListenerTlsCertificateSds],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb8d81031447b52a205df3918dcf66cb1efc2bd83b510b1883a9207ed076ce00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualGatewaySpecListenerTlsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecListenerTlsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c98080e5e138034219ed4207c701d81da579edf40fdff61681a709019941b7b4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCertificate")
    def put_certificate(
        self,
        *,
        acm: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecListenerTlsCertificateAcm, typing.Dict[builtins.str, typing.Any]]] = None,
        file: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecListenerTlsCertificateFile, typing.Dict[builtins.str, typing.Any]]] = None,
        sds: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecListenerTlsCertificateSds, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param acm: acm block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#acm AppmeshVirtualGateway#acm}
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#file AppmeshVirtualGateway#file}
        :param sds: sds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#sds AppmeshVirtualGateway#sds}
        '''
        value = AppmeshVirtualGatewaySpecListenerTlsCertificate(
            acm=acm, file=file, sds=sds
        )

        return typing.cast(None, jsii.invoke(self, "putCertificate", [value]))

    @jsii.member(jsii_name="putValidation")
    def put_validation(
        self,
        *,
        trust: typing.Union["AppmeshVirtualGatewaySpecListenerTlsValidationTrust", typing.Dict[builtins.str, typing.Any]],
        subject_alternative_names: typing.Optional[typing.Union["AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNames", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param trust: trust block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#trust AppmeshVirtualGateway#trust}
        :param subject_alternative_names: subject_alternative_names block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#subject_alternative_names AppmeshVirtualGateway#subject_alternative_names}
        '''
        value = AppmeshVirtualGatewaySpecListenerTlsValidation(
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
    ) -> AppmeshVirtualGatewaySpecListenerTlsCertificateOutputReference:
        return typing.cast(AppmeshVirtualGatewaySpecListenerTlsCertificateOutputReference, jsii.get(self, "certificate"))

    @builtins.property
    @jsii.member(jsii_name="validation")
    def validation(
        self,
    ) -> "AppmeshVirtualGatewaySpecListenerTlsValidationOutputReference":
        return typing.cast("AppmeshVirtualGatewaySpecListenerTlsValidationOutputReference", jsii.get(self, "validation"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecListenerTlsCertificate]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecListenerTlsCertificate], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="validationInput")
    def validation_input(
        self,
    ) -> typing.Optional["AppmeshVirtualGatewaySpecListenerTlsValidation"]:
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecListenerTlsValidation"], jsii.get(self, "validationInput"))

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1722ae854beb4fc2f151dbc30ebf286b366e8a55b9e80cec566a4e37813a3c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshVirtualGatewaySpecListenerTls]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecListenerTls], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualGatewaySpecListenerTls],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d10ee401224fdde6f693cd6a52f8383d2ce07656e22a38a09ffc3b8fe0ca040f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecListenerTlsValidation",
    jsii_struct_bases=[],
    name_mapping={
        "trust": "trust",
        "subject_alternative_names": "subjectAlternativeNames",
    },
)
class AppmeshVirtualGatewaySpecListenerTlsValidation:
    def __init__(
        self,
        *,
        trust: typing.Union["AppmeshVirtualGatewaySpecListenerTlsValidationTrust", typing.Dict[builtins.str, typing.Any]],
        subject_alternative_names: typing.Optional[typing.Union["AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNames", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param trust: trust block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#trust AppmeshVirtualGateway#trust}
        :param subject_alternative_names: subject_alternative_names block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#subject_alternative_names AppmeshVirtualGateway#subject_alternative_names}
        '''
        if isinstance(trust, dict):
            trust = AppmeshVirtualGatewaySpecListenerTlsValidationTrust(**trust)
        if isinstance(subject_alternative_names, dict):
            subject_alternative_names = AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNames(**subject_alternative_names)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d93e28c686d44aced636f8ee4a2e0593ef16e1c41ccd74d13ec04a7633886db)
            check_type(argname="argument trust", value=trust, expected_type=type_hints["trust"])
            check_type(argname="argument subject_alternative_names", value=subject_alternative_names, expected_type=type_hints["subject_alternative_names"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "trust": trust,
        }
        if subject_alternative_names is not None:
            self._values["subject_alternative_names"] = subject_alternative_names

    @builtins.property
    def trust(self) -> "AppmeshVirtualGatewaySpecListenerTlsValidationTrust":
        '''trust block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#trust AppmeshVirtualGateway#trust}
        '''
        result = self._values.get("trust")
        assert result is not None, "Required property 'trust' is missing"
        return typing.cast("AppmeshVirtualGatewaySpecListenerTlsValidationTrust", result)

    @builtins.property
    def subject_alternative_names(
        self,
    ) -> typing.Optional["AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNames"]:
        '''subject_alternative_names block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#subject_alternative_names AppmeshVirtualGateway#subject_alternative_names}
        '''
        result = self._values.get("subject_alternative_names")
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNames"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualGatewaySpecListenerTlsValidation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualGatewaySpecListenerTlsValidationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecListenerTlsValidationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0ac45e4c3bc4416a50b17a8503691bddad5cb6533f206ef937b9f5c4797a00d1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSubjectAlternativeNames")
    def put_subject_alternative_names(
        self,
        *,
        match: typing.Union["AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesMatch", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#match AppmeshVirtualGateway#match}
        '''
        value = AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNames(
            match=match
        )

        return typing.cast(None, jsii.invoke(self, "putSubjectAlternativeNames", [value]))

    @jsii.member(jsii_name="putTrust")
    def put_trust(
        self,
        *,
        file: typing.Optional[typing.Union["AppmeshVirtualGatewaySpecListenerTlsValidationTrustFile", typing.Dict[builtins.str, typing.Any]]] = None,
        sds: typing.Optional[typing.Union["AppmeshVirtualGatewaySpecListenerTlsValidationTrustSds", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#file AppmeshVirtualGateway#file}
        :param sds: sds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#sds AppmeshVirtualGateway#sds}
        '''
        value = AppmeshVirtualGatewaySpecListenerTlsValidationTrust(file=file, sds=sds)

        return typing.cast(None, jsii.invoke(self, "putTrust", [value]))

    @jsii.member(jsii_name="resetSubjectAlternativeNames")
    def reset_subject_alternative_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubjectAlternativeNames", []))

    @builtins.property
    @jsii.member(jsii_name="subjectAlternativeNames")
    def subject_alternative_names(
        self,
    ) -> "AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesOutputReference":
        return typing.cast("AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesOutputReference", jsii.get(self, "subjectAlternativeNames"))

    @builtins.property
    @jsii.member(jsii_name="trust")
    def trust(
        self,
    ) -> "AppmeshVirtualGatewaySpecListenerTlsValidationTrustOutputReference":
        return typing.cast("AppmeshVirtualGatewaySpecListenerTlsValidationTrustOutputReference", jsii.get(self, "trust"))

    @builtins.property
    @jsii.member(jsii_name="subjectAlternativeNamesInput")
    def subject_alternative_names_input(
        self,
    ) -> typing.Optional["AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNames"]:
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNames"], jsii.get(self, "subjectAlternativeNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="trustInput")
    def trust_input(
        self,
    ) -> typing.Optional["AppmeshVirtualGatewaySpecListenerTlsValidationTrust"]:
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecListenerTlsValidationTrust"], jsii.get(self, "trustInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecListenerTlsValidation]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecListenerTlsValidation], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualGatewaySpecListenerTlsValidation],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58ad305720fb3bc6f518aea5b7275f4fa911422f02f7ea078f90951aa2b601d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNames",
    jsii_struct_bases=[],
    name_mapping={"match": "match"},
)
class AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNames:
    def __init__(
        self,
        *,
        match: typing.Union["AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesMatch", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#match AppmeshVirtualGateway#match}
        '''
        if isinstance(match, dict):
            match = AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesMatch(**match)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__331d9cfb0dbd3dbe122b24e8a114e82fba72119f2606da6cba495eab2d6594a6)
            check_type(argname="argument match", value=match, expected_type=type_hints["match"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "match": match,
        }

    @builtins.property
    def match(
        self,
    ) -> "AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesMatch":
        '''match block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#match AppmeshVirtualGateway#match}
        '''
        result = self._values.get("match")
        assert result is not None, "Required property 'match' is missing"
        return typing.cast("AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesMatch", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNames(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesMatch",
    jsii_struct_bases=[],
    name_mapping={"exact": "exact"},
)
class AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesMatch:
    def __init__(self, *, exact: typing.Sequence[builtins.str]) -> None:
        '''
        :param exact: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#exact AppmeshVirtualGateway#exact}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__444054e5fbcbbc95b99930d82240f7a8b262766c43369d23d8acd840fce1abcd)
            check_type(argname="argument exact", value=exact, expected_type=type_hints["exact"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "exact": exact,
        }

    @builtins.property
    def exact(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#exact AppmeshVirtualGateway#exact}.'''
        result = self._values.get("exact")
        assert result is not None, "Required property 'exact' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesMatchOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesMatchOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bc07f60370f939905e109c44840622e86ce706a13d96d614690559e0752e5eec)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b88b1468b41d5781dd858838d9f14e726b7a7cf4aaf4d1c94f5c805805eecda4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exact", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesMatch]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesMatch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesMatch],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__659042877fae9e6af5e7732aaa5442f02dbae790cb52d3be41a7c27300b003dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__773dc9b24e0ec48443bef1e6c81d5da80265c311d11d7a30b19f4d37d7b9d6b0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMatch")
    def put_match(self, *, exact: typing.Sequence[builtins.str]) -> None:
        '''
        :param exact: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#exact AppmeshVirtualGateway#exact}.
        '''
        value = AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesMatch(
            exact=exact
        )

        return typing.cast(None, jsii.invoke(self, "putMatch", [value]))

    @builtins.property
    @jsii.member(jsii_name="match")
    def match(
        self,
    ) -> AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesMatchOutputReference:
        return typing.cast(AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesMatchOutputReference, jsii.get(self, "match"))

    @builtins.property
    @jsii.member(jsii_name="matchInput")
    def match_input(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesMatch]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesMatch], jsii.get(self, "matchInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNames]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNames], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNames],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6a816d162568343a39e6fcf3389e6f6fd9e609b5e6123d1ad2b8158d2b276fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecListenerTlsValidationTrust",
    jsii_struct_bases=[],
    name_mapping={"file": "file", "sds": "sds"},
)
class AppmeshVirtualGatewaySpecListenerTlsValidationTrust:
    def __init__(
        self,
        *,
        file: typing.Optional[typing.Union["AppmeshVirtualGatewaySpecListenerTlsValidationTrustFile", typing.Dict[builtins.str, typing.Any]]] = None,
        sds: typing.Optional[typing.Union["AppmeshVirtualGatewaySpecListenerTlsValidationTrustSds", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#file AppmeshVirtualGateway#file}
        :param sds: sds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#sds AppmeshVirtualGateway#sds}
        '''
        if isinstance(file, dict):
            file = AppmeshVirtualGatewaySpecListenerTlsValidationTrustFile(**file)
        if isinstance(sds, dict):
            sds = AppmeshVirtualGatewaySpecListenerTlsValidationTrustSds(**sds)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcbc9c694f3928df95a407336940736ff89880587685e90df2aabd1d47dfdb46)
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
    ) -> typing.Optional["AppmeshVirtualGatewaySpecListenerTlsValidationTrustFile"]:
        '''file block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#file AppmeshVirtualGateway#file}
        '''
        result = self._values.get("file")
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecListenerTlsValidationTrustFile"], result)

    @builtins.property
    def sds(
        self,
    ) -> typing.Optional["AppmeshVirtualGatewaySpecListenerTlsValidationTrustSds"]:
        '''sds block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#sds AppmeshVirtualGateway#sds}
        '''
        result = self._values.get("sds")
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecListenerTlsValidationTrustSds"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualGatewaySpecListenerTlsValidationTrust(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecListenerTlsValidationTrustFile",
    jsii_struct_bases=[],
    name_mapping={"certificate_chain": "certificateChain"},
)
class AppmeshVirtualGatewaySpecListenerTlsValidationTrustFile:
    def __init__(self, *, certificate_chain: builtins.str) -> None:
        '''
        :param certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#certificate_chain AppmeshVirtualGateway#certificate_chain}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec1f64bc89fdc074c5471caac2166a441c6987425ca7ef3567b3fcf75683a93a)
            check_type(argname="argument certificate_chain", value=certificate_chain, expected_type=type_hints["certificate_chain"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_chain": certificate_chain,
        }

    @builtins.property
    def certificate_chain(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#certificate_chain AppmeshVirtualGateway#certificate_chain}.'''
        result = self._values.get("certificate_chain")
        assert result is not None, "Required property 'certificate_chain' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualGatewaySpecListenerTlsValidationTrustFile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualGatewaySpecListenerTlsValidationTrustFileOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecListenerTlsValidationTrustFileOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3197c77c89050aff59b12424ae1e5d80321c019a88fd7a3909120c797098c0c3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4c46023bbf270c16997a779342d712d27c74cdfb0a339923378efa3f6536fc2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateChain", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecListenerTlsValidationTrustFile]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecListenerTlsValidationTrustFile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualGatewaySpecListenerTlsValidationTrustFile],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da24861501c2e2b6612a40ad9bee4480dd8b38fe053c7c9a1609a5b9efd456a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualGatewaySpecListenerTlsValidationTrustOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecListenerTlsValidationTrustOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ed8abf60addf6f02d5644f2a2c366026070195f7f7da2f22f5a04c067b35394b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putFile")
    def put_file(self, *, certificate_chain: builtins.str) -> None:
        '''
        :param certificate_chain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#certificate_chain AppmeshVirtualGateway#certificate_chain}.
        '''
        value = AppmeshVirtualGatewaySpecListenerTlsValidationTrustFile(
            certificate_chain=certificate_chain
        )

        return typing.cast(None, jsii.invoke(self, "putFile", [value]))

    @jsii.member(jsii_name="putSds")
    def put_sds(self, *, secret_name: builtins.str) -> None:
        '''
        :param secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#secret_name AppmeshVirtualGateway#secret_name}.
        '''
        value = AppmeshVirtualGatewaySpecListenerTlsValidationTrustSds(
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
    ) -> AppmeshVirtualGatewaySpecListenerTlsValidationTrustFileOutputReference:
        return typing.cast(AppmeshVirtualGatewaySpecListenerTlsValidationTrustFileOutputReference, jsii.get(self, "file"))

    @builtins.property
    @jsii.member(jsii_name="sds")
    def sds(
        self,
    ) -> "AppmeshVirtualGatewaySpecListenerTlsValidationTrustSdsOutputReference":
        return typing.cast("AppmeshVirtualGatewaySpecListenerTlsValidationTrustSdsOutputReference", jsii.get(self, "sds"))

    @builtins.property
    @jsii.member(jsii_name="fileInput")
    def file_input(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecListenerTlsValidationTrustFile]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecListenerTlsValidationTrustFile], jsii.get(self, "fileInput"))

    @builtins.property
    @jsii.member(jsii_name="sdsInput")
    def sds_input(
        self,
    ) -> typing.Optional["AppmeshVirtualGatewaySpecListenerTlsValidationTrustSds"]:
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecListenerTlsValidationTrustSds"], jsii.get(self, "sdsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecListenerTlsValidationTrust]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecListenerTlsValidationTrust], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualGatewaySpecListenerTlsValidationTrust],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c65e344a573de6800bf7936f7de8792c8e1deb4c255ba04f1a189c449f780c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecListenerTlsValidationTrustSds",
    jsii_struct_bases=[],
    name_mapping={"secret_name": "secretName"},
)
class AppmeshVirtualGatewaySpecListenerTlsValidationTrustSds:
    def __init__(self, *, secret_name: builtins.str) -> None:
        '''
        :param secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#secret_name AppmeshVirtualGateway#secret_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__caf6918f376c852fd736473e40bb2359a0e64e88bce1704a94c23d94b90fce00)
            check_type(argname="argument secret_name", value=secret_name, expected_type=type_hints["secret_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "secret_name": secret_name,
        }

    @builtins.property
    def secret_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#secret_name AppmeshVirtualGateway#secret_name}.'''
        result = self._values.get("secret_name")
        assert result is not None, "Required property 'secret_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualGatewaySpecListenerTlsValidationTrustSds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualGatewaySpecListenerTlsValidationTrustSdsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecListenerTlsValidationTrustSdsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6247f1034dc914435a4616a674275fe159ad53e6e3b01e683661aad1ac750a2c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__06f4cfb6bc8b1224d87f83d0e73f594ef724a1ea71e9500333c89a5f8796572b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecListenerTlsValidationTrustSds]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecListenerTlsValidationTrustSds], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualGatewaySpecListenerTlsValidationTrustSds],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3dfc377e4d67bdb3d2e2316d814581144e6a28c6b880cdd1bd4b04b1302e75f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecLogging",
    jsii_struct_bases=[],
    name_mapping={"access_log": "accessLog"},
)
class AppmeshVirtualGatewaySpecLogging:
    def __init__(
        self,
        *,
        access_log: typing.Optional[typing.Union["AppmeshVirtualGatewaySpecLoggingAccessLog", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param access_log: access_log block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#access_log AppmeshVirtualGateway#access_log}
        '''
        if isinstance(access_log, dict):
            access_log = AppmeshVirtualGatewaySpecLoggingAccessLog(**access_log)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1952174eec8764c2273ed9d177117ab0d12e31a094c36d2e11064b431904fc61)
            check_type(argname="argument access_log", value=access_log, expected_type=type_hints["access_log"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if access_log is not None:
            self._values["access_log"] = access_log

    @builtins.property
    def access_log(
        self,
    ) -> typing.Optional["AppmeshVirtualGatewaySpecLoggingAccessLog"]:
        '''access_log block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#access_log AppmeshVirtualGateway#access_log}
        '''
        result = self._values.get("access_log")
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecLoggingAccessLog"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualGatewaySpecLogging(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecLoggingAccessLog",
    jsii_struct_bases=[],
    name_mapping={"file": "file"},
)
class AppmeshVirtualGatewaySpecLoggingAccessLog:
    def __init__(
        self,
        *,
        file: typing.Optional[typing.Union["AppmeshVirtualGatewaySpecLoggingAccessLogFile", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#file AppmeshVirtualGateway#file}
        '''
        if isinstance(file, dict):
            file = AppmeshVirtualGatewaySpecLoggingAccessLogFile(**file)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4273323f7335c54aef33d5682c5cd358dcd034c8406b14b486e7faabf5079cc3)
            check_type(argname="argument file", value=file, expected_type=type_hints["file"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if file is not None:
            self._values["file"] = file

    @builtins.property
    def file(self) -> typing.Optional["AppmeshVirtualGatewaySpecLoggingAccessLogFile"]:
        '''file block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#file AppmeshVirtualGateway#file}
        '''
        result = self._values.get("file")
        return typing.cast(typing.Optional["AppmeshVirtualGatewaySpecLoggingAccessLogFile"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualGatewaySpecLoggingAccessLog(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecLoggingAccessLogFile",
    jsii_struct_bases=[],
    name_mapping={"path": "path"},
)
class AppmeshVirtualGatewaySpecLoggingAccessLogFile:
    def __init__(self, *, path: builtins.str) -> None:
        '''
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#path AppmeshVirtualGateway#path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1eb6813cca9728bd9326f53ce8f9b10696fd40519c483b1b6f89c1b1c92fc050)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "path": path,
        }

    @builtins.property
    def path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#path AppmeshVirtualGateway#path}.'''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualGatewaySpecLoggingAccessLogFile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualGatewaySpecLoggingAccessLogFileOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecLoggingAccessLogFileOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e32fbd46242a2821c906956d26548341f202e75d3878f6b9d7879024db87a46b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e2bb8f031c63bc7e3bd18b6ce5f63d7d0ff292582c0db49e296e7cba8ec21adc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecLoggingAccessLogFile]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecLoggingAccessLogFile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualGatewaySpecLoggingAccessLogFile],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc6d9981a77da8e33579d293df8f0c62e1d86ae79fc97c28bad37c32e72f6b17)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualGatewaySpecLoggingAccessLogOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecLoggingAccessLogOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4baf90e9f57efd93ff831e5229ea72e019a67dbd8d39a2e3012f3e0c478e57a2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putFile")
    def put_file(self, *, path: builtins.str) -> None:
        '''
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#path AppmeshVirtualGateway#path}.
        '''
        value = AppmeshVirtualGatewaySpecLoggingAccessLogFile(path=path)

        return typing.cast(None, jsii.invoke(self, "putFile", [value]))

    @jsii.member(jsii_name="resetFile")
    def reset_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFile", []))

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(self) -> AppmeshVirtualGatewaySpecLoggingAccessLogFileOutputReference:
        return typing.cast(AppmeshVirtualGatewaySpecLoggingAccessLogFileOutputReference, jsii.get(self, "file"))

    @builtins.property
    @jsii.member(jsii_name="fileInput")
    def file_input(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecLoggingAccessLogFile]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecLoggingAccessLogFile], jsii.get(self, "fileInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecLoggingAccessLog]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecLoggingAccessLog], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualGatewaySpecLoggingAccessLog],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc0f62596f23f6b031728426c73b032857266e0098bb07fbf68c536a52d530e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualGatewaySpecLoggingOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecLoggingOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f30d58aeab2ebd4ce4f3316592ca7dd131a970c7d3fb6be4d91e7ed82c55f7b5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAccessLog")
    def put_access_log(
        self,
        *,
        file: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecLoggingAccessLogFile, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#file AppmeshVirtualGateway#file}
        '''
        value = AppmeshVirtualGatewaySpecLoggingAccessLog(file=file)

        return typing.cast(None, jsii.invoke(self, "putAccessLog", [value]))

    @jsii.member(jsii_name="resetAccessLog")
    def reset_access_log(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessLog", []))

    @builtins.property
    @jsii.member(jsii_name="accessLog")
    def access_log(self) -> AppmeshVirtualGatewaySpecLoggingAccessLogOutputReference:
        return typing.cast(AppmeshVirtualGatewaySpecLoggingAccessLogOutputReference, jsii.get(self, "accessLog"))

    @builtins.property
    @jsii.member(jsii_name="accessLogInput")
    def access_log_input(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecLoggingAccessLog]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecLoggingAccessLog], jsii.get(self, "accessLogInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshVirtualGatewaySpecLogging]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecLogging], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualGatewaySpecLogging],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c903f03ac07d981a4dc96e498e27a2917f4653b2714e3c7c140780ca9a0d69a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshVirtualGatewaySpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualGateway.AppmeshVirtualGatewaySpecOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ca5ec69d8611f45b268688eaadaf8bea364cc9df03a20af4ed13d9c5dbac4751)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBackendDefaults")
    def put_backend_defaults(
        self,
        *,
        client_policy: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param client_policy: client_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#client_policy AppmeshVirtualGateway#client_policy}
        '''
        value = AppmeshVirtualGatewaySpecBackendDefaults(client_policy=client_policy)

        return typing.cast(None, jsii.invoke(self, "putBackendDefaults", [value]))

    @jsii.member(jsii_name="putListener")
    def put_listener(
        self,
        *,
        port_mapping: typing.Union[AppmeshVirtualGatewaySpecListenerPortMapping, typing.Dict[builtins.str, typing.Any]],
        connection_pool: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecListenerConnectionPool, typing.Dict[builtins.str, typing.Any]]] = None,
        health_check: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecListenerHealthCheck, typing.Dict[builtins.str, typing.Any]]] = None,
        tls: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecListenerTls, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param port_mapping: port_mapping block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#port_mapping AppmeshVirtualGateway#port_mapping}
        :param connection_pool: connection_pool block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#connection_pool AppmeshVirtualGateway#connection_pool}
        :param health_check: health_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#health_check AppmeshVirtualGateway#health_check}
        :param tls: tls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#tls AppmeshVirtualGateway#tls}
        '''
        value = AppmeshVirtualGatewaySpecListener(
            port_mapping=port_mapping,
            connection_pool=connection_pool,
            health_check=health_check,
            tls=tls,
        )

        return typing.cast(None, jsii.invoke(self, "putListener", [value]))

    @jsii.member(jsii_name="putLogging")
    def put_logging(
        self,
        *,
        access_log: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecLoggingAccessLog, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param access_log: access_log block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_gateway#access_log AppmeshVirtualGateway#access_log}
        '''
        value = AppmeshVirtualGatewaySpecLogging(access_log=access_log)

        return typing.cast(None, jsii.invoke(self, "putLogging", [value]))

    @jsii.member(jsii_name="resetBackendDefaults")
    def reset_backend_defaults(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackendDefaults", []))

    @jsii.member(jsii_name="resetLogging")
    def reset_logging(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogging", []))

    @builtins.property
    @jsii.member(jsii_name="backendDefaults")
    def backend_defaults(
        self,
    ) -> AppmeshVirtualGatewaySpecBackendDefaultsOutputReference:
        return typing.cast(AppmeshVirtualGatewaySpecBackendDefaultsOutputReference, jsii.get(self, "backendDefaults"))

    @builtins.property
    @jsii.member(jsii_name="listener")
    def listener(self) -> AppmeshVirtualGatewaySpecListenerOutputReference:
        return typing.cast(AppmeshVirtualGatewaySpecListenerOutputReference, jsii.get(self, "listener"))

    @builtins.property
    @jsii.member(jsii_name="logging")
    def logging(self) -> AppmeshVirtualGatewaySpecLoggingOutputReference:
        return typing.cast(AppmeshVirtualGatewaySpecLoggingOutputReference, jsii.get(self, "logging"))

    @builtins.property
    @jsii.member(jsii_name="backendDefaultsInput")
    def backend_defaults_input(
        self,
    ) -> typing.Optional[AppmeshVirtualGatewaySpecBackendDefaults]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecBackendDefaults], jsii.get(self, "backendDefaultsInput"))

    @builtins.property
    @jsii.member(jsii_name="listenerInput")
    def listener_input(self) -> typing.Optional[AppmeshVirtualGatewaySpecListener]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecListener], jsii.get(self, "listenerInput"))

    @builtins.property
    @jsii.member(jsii_name="loggingInput")
    def logging_input(self) -> typing.Optional[AppmeshVirtualGatewaySpecLogging]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpecLogging], jsii.get(self, "loggingInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshVirtualGatewaySpec]:
        return typing.cast(typing.Optional[AppmeshVirtualGatewaySpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppmeshVirtualGatewaySpec]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8aa35680287600304f2acdf01f9ac32f0e8ae8e106c46833c29f91d6cc218fe3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AppmeshVirtualGateway",
    "AppmeshVirtualGatewayConfig",
    "AppmeshVirtualGatewaySpec",
    "AppmeshVirtualGatewaySpecBackendDefaults",
    "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicy",
    "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyOutputReference",
    "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTls",
    "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificate",
    "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateFile",
    "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateFileOutputReference",
    "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateOutputReference",
    "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateSds",
    "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateSdsOutputReference",
    "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsOutputReference",
    "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidation",
    "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationOutputReference",
    "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames",
    "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch",
    "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatchOutputReference",
    "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesOutputReference",
    "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrust",
    "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustAcm",
    "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustAcmOutputReference",
    "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustFile",
    "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustFileOutputReference",
    "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustOutputReference",
    "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustSds",
    "AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustSdsOutputReference",
    "AppmeshVirtualGatewaySpecBackendDefaultsOutputReference",
    "AppmeshVirtualGatewaySpecListener",
    "AppmeshVirtualGatewaySpecListenerConnectionPool",
    "AppmeshVirtualGatewaySpecListenerConnectionPoolGrpc",
    "AppmeshVirtualGatewaySpecListenerConnectionPoolGrpcOutputReference",
    "AppmeshVirtualGatewaySpecListenerConnectionPoolHttp",
    "AppmeshVirtualGatewaySpecListenerConnectionPoolHttp2",
    "AppmeshVirtualGatewaySpecListenerConnectionPoolHttp2OutputReference",
    "AppmeshVirtualGatewaySpecListenerConnectionPoolHttpOutputReference",
    "AppmeshVirtualGatewaySpecListenerConnectionPoolOutputReference",
    "AppmeshVirtualGatewaySpecListenerHealthCheck",
    "AppmeshVirtualGatewaySpecListenerHealthCheckOutputReference",
    "AppmeshVirtualGatewaySpecListenerOutputReference",
    "AppmeshVirtualGatewaySpecListenerPortMapping",
    "AppmeshVirtualGatewaySpecListenerPortMappingOutputReference",
    "AppmeshVirtualGatewaySpecListenerTls",
    "AppmeshVirtualGatewaySpecListenerTlsCertificate",
    "AppmeshVirtualGatewaySpecListenerTlsCertificateAcm",
    "AppmeshVirtualGatewaySpecListenerTlsCertificateAcmOutputReference",
    "AppmeshVirtualGatewaySpecListenerTlsCertificateFile",
    "AppmeshVirtualGatewaySpecListenerTlsCertificateFileOutputReference",
    "AppmeshVirtualGatewaySpecListenerTlsCertificateOutputReference",
    "AppmeshVirtualGatewaySpecListenerTlsCertificateSds",
    "AppmeshVirtualGatewaySpecListenerTlsCertificateSdsOutputReference",
    "AppmeshVirtualGatewaySpecListenerTlsOutputReference",
    "AppmeshVirtualGatewaySpecListenerTlsValidation",
    "AppmeshVirtualGatewaySpecListenerTlsValidationOutputReference",
    "AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNames",
    "AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesMatch",
    "AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesMatchOutputReference",
    "AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesOutputReference",
    "AppmeshVirtualGatewaySpecListenerTlsValidationTrust",
    "AppmeshVirtualGatewaySpecListenerTlsValidationTrustFile",
    "AppmeshVirtualGatewaySpecListenerTlsValidationTrustFileOutputReference",
    "AppmeshVirtualGatewaySpecListenerTlsValidationTrustOutputReference",
    "AppmeshVirtualGatewaySpecListenerTlsValidationTrustSds",
    "AppmeshVirtualGatewaySpecListenerTlsValidationTrustSdsOutputReference",
    "AppmeshVirtualGatewaySpecLogging",
    "AppmeshVirtualGatewaySpecLoggingAccessLog",
    "AppmeshVirtualGatewaySpecLoggingAccessLogFile",
    "AppmeshVirtualGatewaySpecLoggingAccessLogFileOutputReference",
    "AppmeshVirtualGatewaySpecLoggingAccessLogOutputReference",
    "AppmeshVirtualGatewaySpecLoggingOutputReference",
    "AppmeshVirtualGatewaySpecOutputReference",
]

publication.publish()

def _typecheckingstub__c9ffa1dfdc44237f563c7620b7e7a1d040fa5c8f576cb31a094d8d7a7eb37045(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    mesh_name: builtins.str,
    name: builtins.str,
    spec: typing.Union[AppmeshVirtualGatewaySpec, typing.Dict[builtins.str, typing.Any]],
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

def _typecheckingstub__1f1bc027a25e53da46d10d13d95a76cfaa380ea876fb8c81e39ccd4fc089a893(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d03dac24f7459d0bd2790fd6791b7b5ab1278adf24ef829b39ab407771819ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3029d42f2dd89ce9e3c73cdb798490ab8ecd7f7bf4f26e46d73e45f5c0f7861f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40e16538e8eb40992316e6491c68df7289128de7a8b4ffa5f28c59d8665f79a6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d8a07597818f003edfd71aa4e654b6f2baa4a331bc5f3943d3e0e8f5402e90d(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b1a837b2d6deeaa3536cd9fc7227b149e7f118565141d4afc41d1edcfde7cff(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f78d8a032e766325fde6d0826099df045709dfad853940ed5fc9a5be21498f60(
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
    spec: typing.Union[AppmeshVirtualGatewaySpec, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
    mesh_owner: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0198859f5e2790d5f29a3c04079a95eff26c2aa29783ad639381709128e6ef8d(
    *,
    listener: typing.Union[AppmeshVirtualGatewaySpecListener, typing.Dict[builtins.str, typing.Any]],
    backend_defaults: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecBackendDefaults, typing.Dict[builtins.str, typing.Any]]] = None,
    logging: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecLogging, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5caa35da86a439f032a42168cf94a159c9b0b7e61d9cd9934fe439cf99464d8c(
    *,
    client_policy: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69ab7ebf199caec9f24111ec54cd57a1e3f22df9b71541acf514a80c29fce811(
    *,
    tls: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTls, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c26f30af9d50e5b2f4d65c4ad7ed772c647aaf3c615c3cb59118e2c50c4fc580(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d15c643f9b4d79d2c424b4c5b946dbb6488f6aa7d86ca4ca98d6ac70574881f3(
    value: typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8dabb3b51eee372da40def61ce455ec09fd65806b44c531e895f84f38e65cea(
    *,
    validation: typing.Union[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidation, typing.Dict[builtins.str, typing.Any]],
    certificate: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificate, typing.Dict[builtins.str, typing.Any]]] = None,
    enforce: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ports: typing.Optional[typing.Sequence[jsii.Number]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb25a68725043ebea80a695c2c4d99291c231d61b19e58e8d41fc623b14ad10c(
    *,
    file: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateFile, typing.Dict[builtins.str, typing.Any]]] = None,
    sds: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateSds, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d120bfa9070b38b3593401939b71b59a72a157da040b5963506d1c22b19f10d8(
    *,
    certificate_chain: builtins.str,
    private_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__807fe590ae0839497ce1472cf81b877c9e32e673249a107622624e7036ac270e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72dfcafa968bab8666b6683e58820d99ebcb05eb30676c57909efd9a98a01f9e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__790cd9693d20eb312e0c5a986f4cd2cec8b4d9cd1c1366a59798acb440ac7527(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb9a488a7b66ceda41469636c76b932167f96f661f4bc15f3ab0032c6b8abd4e(
    value: typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateFile],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__088cd7062fdd1d26151b8789765a133b46b888c06d1d8b8b365d7b16f16d0ff2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e084ce4310f490e7a0ef18ab7cde3cb24f05a52878dc06bb06bfd75143a41416(
    value: typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificate],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5765ccf405d8c955d836b7f7d7d8924133a6a23b74ca84c75f7a8f28d9b6b7d(
    *,
    secret_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd57019f6ca126f1335c7bc84eed11eb5731edf95866bd8e5bca51b8331b92bd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c29332a7e26404a02494487c3634dfd707192d701ec24ae85af84eafbe629551(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cafa917f996b19b5fd7aa7432ed5c2d9bedbca7a6a0d1ff53bf049e1c9273ebd(
    value: typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsCertificateSds],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14ea9cbf47710fd8a34e2e04397a92c4024cdb60f5b653fa17064c39e0449f7f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f376b848c7a395501f63db4fabe11cf99ac7b8554a97e6b3959d1efe37c4d81d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b94ebcc898dfe5ba215b78301905da4f6f35942aa50036c7828dd07b8bc1dc7b(
    value: typing.List[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd9dd3db08cd92b898ca2546bd16cac10ffa3609e629ffa3b706f0140c4008d8(
    value: typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTls],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5e12f6a705c0dce4fd3ee33c66ce125af5894fd3728c5281b992917ef0cb608(
    *,
    trust: typing.Union[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrust, typing.Dict[builtins.str, typing.Any]],
    subject_alternative_names: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb6fcf410532476b46a2423f54aa6f00d5ad1f24539e80e8f1939a13a5ad5f90(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29814ffe271b66bc94d1fbffead4bc692e3c81776e51765277e36c6f2e93aec9(
    value: typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidation],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2aa75a7ae4ba4bc323dbc69ba483035a6e250cf5729c3485a9d5c80386899251(
    *,
    match: typing.Union[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bde2e6a498fca2ad46f82a0af53241beff0d38636dbeb1766101d92417b7f9f(
    *,
    exact: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87e56eee3322688766bed44d72a6bfdbb539d53eff928104336f7ba9473c6b42(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a44907e506d9d1cb4400a5be6165bfa1fd22c98dcd88b9595302a407cbf4fe3(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b44e2b1b40bcead7b2ddb53cda170a736b2b6368ad3c5595068cd72876e5f3e(
    value: typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNamesMatch],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b79236a6abeab96a96c6154c192a8c15ecc91027a395ca22209400bbeb1dcd4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc293c54af82eab8fbccc58937b1a0a54b375286a95628d69337522549fba9b9(
    value: typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationSubjectAlternativeNames],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7cfe5c5db36f07ec1be90e0426516cba4e3c5065fbfd6717f21e406b77ec683(
    *,
    acm: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustAcm, typing.Dict[builtins.str, typing.Any]]] = None,
    file: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustFile, typing.Dict[builtins.str, typing.Any]]] = None,
    sds: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustSds, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b6b4b6360e32b60f300b435c01d99163e183bd5e171f81071c8a51d81cbedf3(
    *,
    certificate_authority_arns: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__101c5a07bf776a80d61e927a31f97d55049ee93ebf1a6109d4868ed84d34e64f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0039f8f8b7ab0eef4988ebf6f59099793e3644a1113542161538b75ea9fa45f4(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ac656b30c03084029a5b537fd9621ed49251ad50c92fd3529d684d0ea1d5259(
    value: typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustAcm],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b0225f7bb3e2e59ea957b08d62928d890d498695d772734a6a67f71d811060d(
    *,
    certificate_chain: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__caf8c29d803acb0bf6dc17224d15d87fe0b4b10502fc220344356daf381306ea(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b3645e5b544e0a70f40a9b56aa27fe18ef0aee7698b0669745c548be6c818fd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e191e7c47fb26e994894ff51e729004681c75ddcf243016c7987c9db98949880(
    value: typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustFile],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f67ce5227bc58805f8f49bf00afb9ab280d23009f0e1b4a6509cb9307fc8103(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61b0225c2550022522b6348ebd594c8c446ff8c352394a58bd38dfb9f3ea4235(
    value: typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrust],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8242aa7415f062e143839a71d715664ae19e9eb99b4c7aad9d00aea89a58629b(
    *,
    secret_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2df0199998bbcd697c05ba1ccae64302e92918263680b6b143d6b6dd19df7ba7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d73c90a0f8b4ea072fcdd87c0aaaa6f32af106ef2227d4d6eb79c6a394a3c00(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35e062f3603ef142c6b250d2b734c744ea86b25231116e3b6d1de957470c66bc(
    value: typing.Optional[AppmeshVirtualGatewaySpecBackendDefaultsClientPolicyTlsValidationTrustSds],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40ba99a787445d24cd3bc1910a93d0ec16adb62ad8c37208edd4f967ff02b427(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea6da4dbc3b2e4c43803b9bb5ec15fb19eeb8933976bde501b7f91ccacc1b74d(
    value: typing.Optional[AppmeshVirtualGatewaySpecBackendDefaults],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e12c4676792fb05e812299033c8ef3e39a5983c0fdd227cdddbb5b7206a6df7d(
    *,
    port_mapping: typing.Union[AppmeshVirtualGatewaySpecListenerPortMapping, typing.Dict[builtins.str, typing.Any]],
    connection_pool: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecListenerConnectionPool, typing.Dict[builtins.str, typing.Any]]] = None,
    health_check: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecListenerHealthCheck, typing.Dict[builtins.str, typing.Any]]] = None,
    tls: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecListenerTls, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__578f10035e25b361c9e00808a5738a234d9ba43549c148944b583c80873b8d5a(
    *,
    grpc: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecListenerConnectionPoolGrpc, typing.Dict[builtins.str, typing.Any]]] = None,
    http: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecListenerConnectionPoolHttp, typing.Dict[builtins.str, typing.Any]]] = None,
    http2: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecListenerConnectionPoolHttp2, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a9c9c85a7aabd074e4ee4f69ff7c44cecee3fb8fa8f8e1141b304d99f60c1f4(
    *,
    max_requests: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e629b1bc76eed0d626a2d78fcf5082613972fd3e25bd9435338d839cfe3bf79c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c23c9f13b84e9298acde25a347372436b68f7b5298ddbc997baaf17accd3ff14(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1481205a71b8eec028bcab5e600a1d33220a95c6dc0aafa0feb810a713f4dfbf(
    value: typing.Optional[AppmeshVirtualGatewaySpecListenerConnectionPoolGrpc],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6184b5b48eadf4f324354085675ec6fe8c3d1d0053879413a863106a109d92a(
    *,
    max_connections: jsii.Number,
    max_pending_requests: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a78a848031d352a41112cde4478811ce3b2bb9daf34b63850ade57a32cdcc89d(
    *,
    max_requests: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd6e80b554b000a82741807fc15763c75ac4f6183695ea67b2731b572ba5fd90(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d1bde3d069d29af42734d79a5fff4d9e363975348bc8bc79489ae2198e84f18(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1154ea49d3d95383b0b635c474ac3a936f3cc02fa2d24ee106b79427905e5f65(
    value: typing.Optional[AppmeshVirtualGatewaySpecListenerConnectionPoolHttp2],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5570db8eff3b42349e065790cc409bc3e3799934d64b24627de0c11889c2276b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90b88e05d361ebae5639f15ccef767b814eb726cf6856cfb14b9957065725f93(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63b0cd6ba3cc5309462f9c1400f93cde9b4fd58b85cc17950086842130addd35(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c699f253ca9fd3f55ef413fe9a958251356fd4fe6d85bd22cb94008e0c38006a(
    value: typing.Optional[AppmeshVirtualGatewaySpecListenerConnectionPoolHttp],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__289783099bdb2a51f7c549c05ce173d744a88e639e6266420e90354d60122c7d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cd676bba3b66f5fe78a55bacd3b47925108db919e303dbebf5fda24367802ce(
    value: typing.Optional[AppmeshVirtualGatewaySpecListenerConnectionPool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31e2ae56dbe3006e6330291e03d3fce89c5eb64b1560aa09ebaddb7b6abd3d38(
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

def _typecheckingstub__ef98379b970b417eb782a5ef2e18232a017fc249ae399e87d927c12ea46490ac(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__240878609b70ddfd16e6df958d567a71643f1314ead9af65f1e70f83876bc6a7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8b7998354c42d3793bc38995a0b995085030df9106a25c3a773ae4147e081f3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__760af830f2dcb1696c4af3b8f595b747a5ed8585c435125af7e17e0207c2d071(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ba577fdd1039932ef49ca9740e4ccabc6c9f55236cb03f42b4c2eb742ce7490(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a30090bf2d38e89268196f657b6a63b1ae8c3a1e84bddcc888b834d5091118e6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9b128e11c054b86f8918c137b2d55886c10b5983189e43347211a82ffc5fcd5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44454b9d70f8ceca300409dbad89991f58905d0fa5eca0072353b3cdccddcf9e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6f595ef975664e29437a813c01f29684140f15acd4764ddeb373d0209e51857(
    value: typing.Optional[AppmeshVirtualGatewaySpecListenerHealthCheck],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f0b38866c928442d74560296ce698ea58432ed880e1dc4b1d08821ca79a0ca9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__967eb6060b62444e534a53409762f85ee01957eba41bbdbd494422913cc484b4(
    value: typing.Optional[AppmeshVirtualGatewaySpecListener],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__665e63b6d728face43c8708ad1f3805811f66761649000fffccc7879eee465f3(
    *,
    port: jsii.Number,
    protocol: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42c9907d3ccb5d958ec66dfe079080cff58b62ce32f450c6aafd09e29bbec094(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ca4347ad72c1d319bb9dd836853a7da0606e1a578e86250d6d09c6ea03c62c6(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c921274ad3dcf5e331cf937a8f3a493e3b91b448b138073d9cf601f0bec1b8b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__710ae9f04d2774c3dc80aa59876d01bc145a51f6ef22a583fbf5b873bcd6a05f(
    value: typing.Optional[AppmeshVirtualGatewaySpecListenerPortMapping],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c7bd8f89cc89b7cef60d6f4f5a67563f1306fec01cf13f45357ab72dd889557(
    *,
    certificate: typing.Union[AppmeshVirtualGatewaySpecListenerTlsCertificate, typing.Dict[builtins.str, typing.Any]],
    mode: builtins.str,
    validation: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecListenerTlsValidation, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edcd8a8b22ff8290bd05f0d420575ea909a12a637c6669dcd628556165437040(
    *,
    acm: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecListenerTlsCertificateAcm, typing.Dict[builtins.str, typing.Any]]] = None,
    file: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecListenerTlsCertificateFile, typing.Dict[builtins.str, typing.Any]]] = None,
    sds: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecListenerTlsCertificateSds, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c6baa7dfc57b8f8c952c0dea9e34c8bd2685e155688ebe940c7cbae65d912b0(
    *,
    certificate_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d2c86e353876775502258d0482263124ad943f19d6cad943a887c52873c4407(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e241fac4176da75e5ae06b02971dec37f93df842b39cbf7e64220f5643f02b1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08838b3a968155deb038101de1e1db9f3f0af4a01abaabe3bb79626edcf50dea(
    value: typing.Optional[AppmeshVirtualGatewaySpecListenerTlsCertificateAcm],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26875efe6083df16a96b262489e362a9beca1abb17355a5abece6b557a5a38a3(
    *,
    certificate_chain: builtins.str,
    private_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bff3493b4e9a12c95f2fabe2010b9a14651edeb112d0de62196505d8d4da008c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00e119931f78d91d9015fc2d065a9c32d7e54264e481d96a6090beb264c8edaf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__022fa3957bf559d9e8e2db6c85a7cb8564f6b1a29abdc3e4646782a859ea4660(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da99c97a7e005c5a33c48551aefbfc5d098efa7127af7b443a9e1b3ab664a6b3(
    value: typing.Optional[AppmeshVirtualGatewaySpecListenerTlsCertificateFile],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95ed6950ed31a7e8e9ab7a8a879187638f73e68f5fdda5d9844ec80d2fce2b7a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__521844dd8f6c9ee3bdd5b9a20b434c206c9871bae52bf615cb9b0be365b01bf5(
    value: typing.Optional[AppmeshVirtualGatewaySpecListenerTlsCertificate],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3fe1723b665935bd27782455a9bd60963469ca09ce1c5ce750abfbd5e0be1f3(
    *,
    secret_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5779d01be8347acdaef1e69600b3292eb19bd6d93eb8576ea227ff624b028a8d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afed7e0d7618fa93dde04cd6d2f676873f654eeba7fd9c2c616172486027bcfa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb8d81031447b52a205df3918dcf66cb1efc2bd83b510b1883a9207ed076ce00(
    value: typing.Optional[AppmeshVirtualGatewaySpecListenerTlsCertificateSds],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c98080e5e138034219ed4207c701d81da579edf40fdff61681a709019941b7b4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1722ae854beb4fc2f151dbc30ebf286b366e8a55b9e80cec566a4e37813a3c3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d10ee401224fdde6f693cd6a52f8383d2ce07656e22a38a09ffc3b8fe0ca040f(
    value: typing.Optional[AppmeshVirtualGatewaySpecListenerTls],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d93e28c686d44aced636f8ee4a2e0593ef16e1c41ccd74d13ec04a7633886db(
    *,
    trust: typing.Union[AppmeshVirtualGatewaySpecListenerTlsValidationTrust, typing.Dict[builtins.str, typing.Any]],
    subject_alternative_names: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNames, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ac45e4c3bc4416a50b17a8503691bddad5cb6533f206ef937b9f5c4797a00d1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58ad305720fb3bc6f518aea5b7275f4fa911422f02f7ea078f90951aa2b601d0(
    value: typing.Optional[AppmeshVirtualGatewaySpecListenerTlsValidation],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__331d9cfb0dbd3dbe122b24e8a114e82fba72119f2606da6cba495eab2d6594a6(
    *,
    match: typing.Union[AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesMatch, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__444054e5fbcbbc95b99930d82240f7a8b262766c43369d23d8acd840fce1abcd(
    *,
    exact: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc07f60370f939905e109c44840622e86ce706a13d96d614690559e0752e5eec(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b88b1468b41d5781dd858838d9f14e726b7a7cf4aaf4d1c94f5c805805eecda4(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__659042877fae9e6af5e7732aaa5442f02dbae790cb52d3be41a7c27300b003dc(
    value: typing.Optional[AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNamesMatch],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__773dc9b24e0ec48443bef1e6c81d5da80265c311d11d7a30b19f4d37d7b9d6b0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6a816d162568343a39e6fcf3389e6f6fd9e609b5e6123d1ad2b8158d2b276fb(
    value: typing.Optional[AppmeshVirtualGatewaySpecListenerTlsValidationSubjectAlternativeNames],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcbc9c694f3928df95a407336940736ff89880587685e90df2aabd1d47dfdb46(
    *,
    file: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecListenerTlsValidationTrustFile, typing.Dict[builtins.str, typing.Any]]] = None,
    sds: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecListenerTlsValidationTrustSds, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec1f64bc89fdc074c5471caac2166a441c6987425ca7ef3567b3fcf75683a93a(
    *,
    certificate_chain: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3197c77c89050aff59b12424ae1e5d80321c019a88fd7a3909120c797098c0c3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c46023bbf270c16997a779342d712d27c74cdfb0a339923378efa3f6536fc2a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da24861501c2e2b6612a40ad9bee4480dd8b38fe053c7c9a1609a5b9efd456a8(
    value: typing.Optional[AppmeshVirtualGatewaySpecListenerTlsValidationTrustFile],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed8abf60addf6f02d5644f2a2c366026070195f7f7da2f22f5a04c067b35394b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c65e344a573de6800bf7936f7de8792c8e1deb4c255ba04f1a189c449f780c4(
    value: typing.Optional[AppmeshVirtualGatewaySpecListenerTlsValidationTrust],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__caf6918f376c852fd736473e40bb2359a0e64e88bce1704a94c23d94b90fce00(
    *,
    secret_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6247f1034dc914435a4616a674275fe159ad53e6e3b01e683661aad1ac750a2c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06f4cfb6bc8b1224d87f83d0e73f594ef724a1ea71e9500333c89a5f8796572b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3dfc377e4d67bdb3d2e2316d814581144e6a28c6b880cdd1bd4b04b1302e75f4(
    value: typing.Optional[AppmeshVirtualGatewaySpecListenerTlsValidationTrustSds],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1952174eec8764c2273ed9d177117ab0d12e31a094c36d2e11064b431904fc61(
    *,
    access_log: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecLoggingAccessLog, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4273323f7335c54aef33d5682c5cd358dcd034c8406b14b486e7faabf5079cc3(
    *,
    file: typing.Optional[typing.Union[AppmeshVirtualGatewaySpecLoggingAccessLogFile, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1eb6813cca9728bd9326f53ce8f9b10696fd40519c483b1b6f89c1b1c92fc050(
    *,
    path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e32fbd46242a2821c906956d26548341f202e75d3878f6b9d7879024db87a46b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2bb8f031c63bc7e3bd18b6ce5f63d7d0ff292582c0db49e296e7cba8ec21adc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc6d9981a77da8e33579d293df8f0c62e1d86ae79fc97c28bad37c32e72f6b17(
    value: typing.Optional[AppmeshVirtualGatewaySpecLoggingAccessLogFile],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4baf90e9f57efd93ff831e5229ea72e019a67dbd8d39a2e3012f3e0c478e57a2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc0f62596f23f6b031728426c73b032857266e0098bb07fbf68c536a52d530e0(
    value: typing.Optional[AppmeshVirtualGatewaySpecLoggingAccessLog],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f30d58aeab2ebd4ce4f3316592ca7dd131a970c7d3fb6be4d91e7ed82c55f7b5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c903f03ac07d981a4dc96e498e27a2917f4653b2714e3c7c140780ca9a0d69a(
    value: typing.Optional[AppmeshVirtualGatewaySpecLogging],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca5ec69d8611f45b268688eaadaf8bea364cc9df03a20af4ed13d9c5dbac4751(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8aa35680287600304f2acdf01f9ac32f0e8ae8e106c46833c29f91d6cc218fe3(
    value: typing.Optional[AppmeshVirtualGatewaySpec],
) -> None:
    """Type checking stubs"""
    pass
