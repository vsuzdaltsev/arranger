'''
# `aws_appmesh_route`

Refer to the Terraform Registory for docs: [`aws_appmesh_route`](https://www.terraform.io/docs/providers/aws/r/appmesh_route).
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


class AppmeshRoute(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRoute",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route aws_appmesh_route}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        mesh_name: builtins.str,
        name: builtins.str,
        spec: typing.Union["AppmeshRouteSpec", typing.Dict[builtins.str, typing.Any]],
        virtual_router_name: builtins.str,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route aws_appmesh_route} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param mesh_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#mesh_name AppmeshRoute#mesh_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#name AppmeshRoute#name}.
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#spec AppmeshRoute#spec}
        :param virtual_router_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#virtual_router_name AppmeshRoute#virtual_router_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#id AppmeshRoute#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mesh_owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#mesh_owner AppmeshRoute#mesh_owner}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#tags AppmeshRoute#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#tags_all AppmeshRoute#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__499d83546f51cceddcb769519c984570619874357f30feab8625fec171bfc113)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AppmeshRouteConfig(
            mesh_name=mesh_name,
            name=name,
            spec=spec,
            virtual_router_name=virtual_router_name,
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
        grpc_route: typing.Optional[typing.Union["AppmeshRouteSpecGrpcRoute", typing.Dict[builtins.str, typing.Any]]] = None,
        http2_route: typing.Optional[typing.Union["AppmeshRouteSpecHttp2Route", typing.Dict[builtins.str, typing.Any]]] = None,
        http_route: typing.Optional[typing.Union["AppmeshRouteSpecHttpRoute", typing.Dict[builtins.str, typing.Any]]] = None,
        priority: typing.Optional[jsii.Number] = None,
        tcp_route: typing.Optional[typing.Union["AppmeshRouteSpecTcpRoute", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param grpc_route: grpc_route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#grpc_route AppmeshRoute#grpc_route}
        :param http2_route: http2_route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#http2_route AppmeshRoute#http2_route}
        :param http_route: http_route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#http_route AppmeshRoute#http_route}
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#priority AppmeshRoute#priority}.
        :param tcp_route: tcp_route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#tcp_route AppmeshRoute#tcp_route}
        '''
        value = AppmeshRouteSpec(
            grpc_route=grpc_route,
            http2_route=http2_route,
            http_route=http_route,
            priority=priority,
            tcp_route=tcp_route,
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
    def spec(self) -> "AppmeshRouteSpecOutputReference":
        return typing.cast("AppmeshRouteSpecOutputReference", jsii.get(self, "spec"))

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
    def spec_input(self) -> typing.Optional["AppmeshRouteSpec"]:
        return typing.cast(typing.Optional["AppmeshRouteSpec"], jsii.get(self, "specInput"))

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
    @jsii.member(jsii_name="virtualRouterNameInput")
    def virtual_router_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualRouterNameInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7dba324d7e133718364d8ab038d32d28ce364b6b76daa256c53f932ff27c6433)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="meshName")
    def mesh_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "meshName"))

    @mesh_name.setter
    def mesh_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e584e5becd0196157e82e66cbc42cbcba02e97953cb58a3d707d2767f6d8af15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "meshName", value)

    @builtins.property
    @jsii.member(jsii_name="meshOwner")
    def mesh_owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "meshOwner"))

    @mesh_owner.setter
    def mesh_owner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c476d888e315d810ad21fc21e13df6d349863f1b5fe3c22429515927818561b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "meshOwner", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33a5e64c718469ffd56cb3dff63ffae7a72128843c47f262b73d66298f4332a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d31d507f8c156b7afa8933b7cca728bd522ec6ad2ba486c64420cfffaaa28fb0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d742c33216c5f2c02de95ebe1b83d2cd77acc2bce14130f72419009fd42957bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="virtualRouterName")
    def virtual_router_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualRouterName"))

    @virtual_router_name.setter
    def virtual_router_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0051872ca32ca6887399275ca9030b827f28dcdc7701fd49ead8d2b8305e5811)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualRouterName", value)


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteConfig",
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
        "virtual_router_name": "virtualRouterName",
        "id": "id",
        "mesh_owner": "meshOwner",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class AppmeshRouteConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        spec: typing.Union["AppmeshRouteSpec", typing.Dict[builtins.str, typing.Any]],
        virtual_router_name: builtins.str,
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
        :param mesh_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#mesh_name AppmeshRoute#mesh_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#name AppmeshRoute#name}.
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#spec AppmeshRoute#spec}
        :param virtual_router_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#virtual_router_name AppmeshRoute#virtual_router_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#id AppmeshRoute#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mesh_owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#mesh_owner AppmeshRoute#mesh_owner}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#tags AppmeshRoute#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#tags_all AppmeshRoute#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(spec, dict):
            spec = AppmeshRouteSpec(**spec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__594bdf1650e42f4ccd51b19f32715f923d8ff4907b9484c491a626e41ba72cb7)
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
            check_type(argname="argument virtual_router_name", value=virtual_router_name, expected_type=type_hints["virtual_router_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument mesh_owner", value=mesh_owner, expected_type=type_hints["mesh_owner"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "mesh_name": mesh_name,
            "name": name,
            "spec": spec,
            "virtual_router_name": virtual_router_name,
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#mesh_name AppmeshRoute#mesh_name}.'''
        result = self._values.get("mesh_name")
        assert result is not None, "Required property 'mesh_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#name AppmeshRoute#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def spec(self) -> "AppmeshRouteSpec":
        '''spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#spec AppmeshRoute#spec}
        '''
        result = self._values.get("spec")
        assert result is not None, "Required property 'spec' is missing"
        return typing.cast("AppmeshRouteSpec", result)

    @builtins.property
    def virtual_router_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#virtual_router_name AppmeshRoute#virtual_router_name}.'''
        result = self._values.get("virtual_router_name")
        assert result is not None, "Required property 'virtual_router_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#id AppmeshRoute#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mesh_owner(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#mesh_owner AppmeshRoute#mesh_owner}.'''
        result = self._values.get("mesh_owner")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#tags AppmeshRoute#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#tags_all AppmeshRoute#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpec",
    jsii_struct_bases=[],
    name_mapping={
        "grpc_route": "grpcRoute",
        "http2_route": "http2Route",
        "http_route": "httpRoute",
        "priority": "priority",
        "tcp_route": "tcpRoute",
    },
)
class AppmeshRouteSpec:
    def __init__(
        self,
        *,
        grpc_route: typing.Optional[typing.Union["AppmeshRouteSpecGrpcRoute", typing.Dict[builtins.str, typing.Any]]] = None,
        http2_route: typing.Optional[typing.Union["AppmeshRouteSpecHttp2Route", typing.Dict[builtins.str, typing.Any]]] = None,
        http_route: typing.Optional[typing.Union["AppmeshRouteSpecHttpRoute", typing.Dict[builtins.str, typing.Any]]] = None,
        priority: typing.Optional[jsii.Number] = None,
        tcp_route: typing.Optional[typing.Union["AppmeshRouteSpecTcpRoute", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param grpc_route: grpc_route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#grpc_route AppmeshRoute#grpc_route}
        :param http2_route: http2_route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#http2_route AppmeshRoute#http2_route}
        :param http_route: http_route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#http_route AppmeshRoute#http_route}
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#priority AppmeshRoute#priority}.
        :param tcp_route: tcp_route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#tcp_route AppmeshRoute#tcp_route}
        '''
        if isinstance(grpc_route, dict):
            grpc_route = AppmeshRouteSpecGrpcRoute(**grpc_route)
        if isinstance(http2_route, dict):
            http2_route = AppmeshRouteSpecHttp2Route(**http2_route)
        if isinstance(http_route, dict):
            http_route = AppmeshRouteSpecHttpRoute(**http_route)
        if isinstance(tcp_route, dict):
            tcp_route = AppmeshRouteSpecTcpRoute(**tcp_route)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7540b62900c9022fc14a9cb2fad09782afdf7505effde7e17f1e857b1e74259f)
            check_type(argname="argument grpc_route", value=grpc_route, expected_type=type_hints["grpc_route"])
            check_type(argname="argument http2_route", value=http2_route, expected_type=type_hints["http2_route"])
            check_type(argname="argument http_route", value=http_route, expected_type=type_hints["http_route"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument tcp_route", value=tcp_route, expected_type=type_hints["tcp_route"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if grpc_route is not None:
            self._values["grpc_route"] = grpc_route
        if http2_route is not None:
            self._values["http2_route"] = http2_route
        if http_route is not None:
            self._values["http_route"] = http_route
        if priority is not None:
            self._values["priority"] = priority
        if tcp_route is not None:
            self._values["tcp_route"] = tcp_route

    @builtins.property
    def grpc_route(self) -> typing.Optional["AppmeshRouteSpecGrpcRoute"]:
        '''grpc_route block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#grpc_route AppmeshRoute#grpc_route}
        '''
        result = self._values.get("grpc_route")
        return typing.cast(typing.Optional["AppmeshRouteSpecGrpcRoute"], result)

    @builtins.property
    def http2_route(self) -> typing.Optional["AppmeshRouteSpecHttp2Route"]:
        '''http2_route block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#http2_route AppmeshRoute#http2_route}
        '''
        result = self._values.get("http2_route")
        return typing.cast(typing.Optional["AppmeshRouteSpecHttp2Route"], result)

    @builtins.property
    def http_route(self) -> typing.Optional["AppmeshRouteSpecHttpRoute"]:
        '''http_route block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#http_route AppmeshRoute#http_route}
        '''
        result = self._values.get("http_route")
        return typing.cast(typing.Optional["AppmeshRouteSpecHttpRoute"], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#priority AppmeshRoute#priority}.'''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tcp_route(self) -> typing.Optional["AppmeshRouteSpecTcpRoute"]:
        '''tcp_route block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#tcp_route AppmeshRoute#tcp_route}
        '''
        result = self._values.get("tcp_route")
        return typing.cast(typing.Optional["AppmeshRouteSpecTcpRoute"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecGrpcRoute",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "match": "match",
        "retry_policy": "retryPolicy",
        "timeout": "timeout",
    },
)
class AppmeshRouteSpecGrpcRoute:
    def __init__(
        self,
        *,
        action: typing.Union["AppmeshRouteSpecGrpcRouteAction", typing.Dict[builtins.str, typing.Any]],
        match: typing.Optional[typing.Union["AppmeshRouteSpecGrpcRouteMatch", typing.Dict[builtins.str, typing.Any]]] = None,
        retry_policy: typing.Optional[typing.Union["AppmeshRouteSpecGrpcRouteRetryPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        timeout: typing.Optional[typing.Union["AppmeshRouteSpecGrpcRouteTimeout", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#action AppmeshRoute#action}
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#match AppmeshRoute#match}
        :param retry_policy: retry_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#retry_policy AppmeshRoute#retry_policy}
        :param timeout: timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#timeout AppmeshRoute#timeout}
        '''
        if isinstance(action, dict):
            action = AppmeshRouteSpecGrpcRouteAction(**action)
        if isinstance(match, dict):
            match = AppmeshRouteSpecGrpcRouteMatch(**match)
        if isinstance(retry_policy, dict):
            retry_policy = AppmeshRouteSpecGrpcRouteRetryPolicy(**retry_policy)
        if isinstance(timeout, dict):
            timeout = AppmeshRouteSpecGrpcRouteTimeout(**timeout)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd319ffac56c2124480c1ef84147cb35b1a46fe9ddf9ec7a93539ff1186b989a)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument match", value=match, expected_type=type_hints["match"])
            check_type(argname="argument retry_policy", value=retry_policy, expected_type=type_hints["retry_policy"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action": action,
        }
        if match is not None:
            self._values["match"] = match
        if retry_policy is not None:
            self._values["retry_policy"] = retry_policy
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def action(self) -> "AppmeshRouteSpecGrpcRouteAction":
        '''action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#action AppmeshRoute#action}
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast("AppmeshRouteSpecGrpcRouteAction", result)

    @builtins.property
    def match(self) -> typing.Optional["AppmeshRouteSpecGrpcRouteMatch"]:
        '''match block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#match AppmeshRoute#match}
        '''
        result = self._values.get("match")
        return typing.cast(typing.Optional["AppmeshRouteSpecGrpcRouteMatch"], result)

    @builtins.property
    def retry_policy(self) -> typing.Optional["AppmeshRouteSpecGrpcRouteRetryPolicy"]:
        '''retry_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#retry_policy AppmeshRoute#retry_policy}
        '''
        result = self._values.get("retry_policy")
        return typing.cast(typing.Optional["AppmeshRouteSpecGrpcRouteRetryPolicy"], result)

    @builtins.property
    def timeout(self) -> typing.Optional["AppmeshRouteSpecGrpcRouteTimeout"]:
        '''timeout block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#timeout AppmeshRoute#timeout}
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional["AppmeshRouteSpecGrpcRouteTimeout"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecGrpcRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecGrpcRouteAction",
    jsii_struct_bases=[],
    name_mapping={"weighted_target": "weightedTarget"},
)
class AppmeshRouteSpecGrpcRouteAction:
    def __init__(
        self,
        *,
        weighted_target: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AppmeshRouteSpecGrpcRouteActionWeightedTarget", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param weighted_target: weighted_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#weighted_target AppmeshRoute#weighted_target}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__406ed44a0eeae677559372942f25ec13dd00817650a4ec55c9d3f6f7b20e5a26)
            check_type(argname="argument weighted_target", value=weighted_target, expected_type=type_hints["weighted_target"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "weighted_target": weighted_target,
        }

    @builtins.property
    def weighted_target(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppmeshRouteSpecGrpcRouteActionWeightedTarget"]]:
        '''weighted_target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#weighted_target AppmeshRoute#weighted_target}
        '''
        result = self._values.get("weighted_target")
        assert result is not None, "Required property 'weighted_target' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppmeshRouteSpecGrpcRouteActionWeightedTarget"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecGrpcRouteAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshRouteSpecGrpcRouteActionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecGrpcRouteActionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__95310011b50709cc1982b713c1bd996e7a172924fe456b7fade5160d109de8a3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putWeightedTarget")
    def put_weighted_target(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AppmeshRouteSpecGrpcRouteActionWeightedTarget", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4502215445b7206d4afc486ef83d002382f6b132b351b5108005c6391c830087)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWeightedTarget", [value]))

    @builtins.property
    @jsii.member(jsii_name="weightedTarget")
    def weighted_target(self) -> "AppmeshRouteSpecGrpcRouteActionWeightedTargetList":
        return typing.cast("AppmeshRouteSpecGrpcRouteActionWeightedTargetList", jsii.get(self, "weightedTarget"))

    @builtins.property
    @jsii.member(jsii_name="weightedTargetInput")
    def weighted_target_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppmeshRouteSpecGrpcRouteActionWeightedTarget"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppmeshRouteSpecGrpcRouteActionWeightedTarget"]]], jsii.get(self, "weightedTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshRouteSpecGrpcRouteAction]:
        return typing.cast(typing.Optional[AppmeshRouteSpecGrpcRouteAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshRouteSpecGrpcRouteAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a07716348b397b797eb8152fcd1bd11e4900b10e24b4db183af5641e07fec4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecGrpcRouteActionWeightedTarget",
    jsii_struct_bases=[],
    name_mapping={"virtual_node": "virtualNode", "weight": "weight"},
)
class AppmeshRouteSpecGrpcRouteActionWeightedTarget:
    def __init__(self, *, virtual_node: builtins.str, weight: jsii.Number) -> None:
        '''
        :param virtual_node: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#virtual_node AppmeshRoute#virtual_node}.
        :param weight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#weight AppmeshRoute#weight}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7138c7ca95b2f4688250f648fac99ed2e9b45721e82bdc5d8ec2ccc65558f479)
            check_type(argname="argument virtual_node", value=virtual_node, expected_type=type_hints["virtual_node"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "virtual_node": virtual_node,
            "weight": weight,
        }

    @builtins.property
    def virtual_node(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#virtual_node AppmeshRoute#virtual_node}.'''
        result = self._values.get("virtual_node")
        assert result is not None, "Required property 'virtual_node' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def weight(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#weight AppmeshRoute#weight}.'''
        result = self._values.get("weight")
        assert result is not None, "Required property 'weight' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecGrpcRouteActionWeightedTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshRouteSpecGrpcRouteActionWeightedTargetList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecGrpcRouteActionWeightedTargetList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3efc45f8db0bbab296df7a5c169358e54e88dac1cc503cc32bbd6e7da120bf30)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AppmeshRouteSpecGrpcRouteActionWeightedTargetOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__259586adaff0dd125e5f386c21b8d3a9bc95add39b03403064fd07b70fd644ae)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppmeshRouteSpecGrpcRouteActionWeightedTargetOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40fe8bfd65f059bc57b1cbc23be51da804e41fc8b7f9fb43a3d1951e86164f34)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4c8b182a6c4a52c5ea2b046eee955f50c06141f9b6c5204dec8fe82219140e4c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b4a424b97b49fb59e8198182ac15046664ab015e5b58710991fa34ac260c09b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshRouteSpecGrpcRouteActionWeightedTarget]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshRouteSpecGrpcRouteActionWeightedTarget]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshRouteSpecGrpcRouteActionWeightedTarget]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67e9a3560e71628e69a1e369e281564cd06c606d354ebcad08ee25a35f8c8eea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshRouteSpecGrpcRouteActionWeightedTargetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecGrpcRouteActionWeightedTargetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bbdaee0dfc2c8102876d5669d0a6d5849447bd25c1a105670b91f01693992a81)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="virtualNodeInput")
    def virtual_node_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualNodeInput"))

    @builtins.property
    @jsii.member(jsii_name="weightInput")
    def weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNode")
    def virtual_node(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualNode"))

    @virtual_node.setter
    def virtual_node(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f48bfc30ae59f94d2c31f4ebdd87e6e3af84f11dcebc18df6f485c94c5710fc9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualNode", value)

    @builtins.property
    @jsii.member(jsii_name="weight")
    def weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weight"))

    @weight.setter
    def weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d15db8945f3d9aecf5232ae33c4978094494cfd798e1bde59ed2f8baf134c23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weight", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppmeshRouteSpecGrpcRouteActionWeightedTarget, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppmeshRouteSpecGrpcRouteActionWeightedTarget, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppmeshRouteSpecGrpcRouteActionWeightedTarget, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdd19af0ac7e17bb0ef8c7dc3e6444a6ef139429d98441945b76b745a8c91465)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecGrpcRouteMatch",
    jsii_struct_bases=[],
    name_mapping={
        "metadata": "metadata",
        "method_name": "methodName",
        "prefix": "prefix",
        "service_name": "serviceName",
    },
)
class AppmeshRouteSpecGrpcRouteMatch:
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AppmeshRouteSpecGrpcRouteMatchMetadata", typing.Dict[builtins.str, typing.Any]]]]] = None,
        method_name: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        service_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#metadata AppmeshRoute#metadata}
        :param method_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#method_name AppmeshRoute#method_name}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#prefix AppmeshRoute#prefix}.
        :param service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#service_name AppmeshRoute#service_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3893328932cb68be97fbfb8a092a0fd13dbab6723060eaae578ad644a0561a47)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument method_name", value=method_name, expected_type=type_hints["method_name"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if method_name is not None:
            self._values["method_name"] = method_name
        if prefix is not None:
            self._values["prefix"] = prefix
        if service_name is not None:
            self._values["service_name"] = service_name

    @builtins.property
    def metadata(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppmeshRouteSpecGrpcRouteMatchMetadata"]]]:
        '''metadata block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#metadata AppmeshRoute#metadata}
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppmeshRouteSpecGrpcRouteMatchMetadata"]]], result)

    @builtins.property
    def method_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#method_name AppmeshRoute#method_name}.'''
        result = self._values.get("method_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#prefix AppmeshRoute#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#service_name AppmeshRoute#service_name}.'''
        result = self._values.get("service_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecGrpcRouteMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecGrpcRouteMatchMetadata",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "invert": "invert", "match": "match"},
)
class AppmeshRouteSpecGrpcRouteMatchMetadata:
    def __init__(
        self,
        *,
        name: builtins.str,
        invert: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        match: typing.Optional[typing.Union["AppmeshRouteSpecGrpcRouteMatchMetadataMatch", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#name AppmeshRoute#name}.
        :param invert: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#invert AppmeshRoute#invert}.
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#match AppmeshRoute#match}
        '''
        if isinstance(match, dict):
            match = AppmeshRouteSpecGrpcRouteMatchMetadataMatch(**match)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__473001717cd70955668867e4b555debf8ec2e0e32e74008ee61fa75d46035720)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument invert", value=invert, expected_type=type_hints["invert"])
            check_type(argname="argument match", value=match, expected_type=type_hints["match"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if invert is not None:
            self._values["invert"] = invert
        if match is not None:
            self._values["match"] = match

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#name AppmeshRoute#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def invert(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#invert AppmeshRoute#invert}.'''
        result = self._values.get("invert")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def match(self) -> typing.Optional["AppmeshRouteSpecGrpcRouteMatchMetadataMatch"]:
        '''match block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#match AppmeshRoute#match}
        '''
        result = self._values.get("match")
        return typing.cast(typing.Optional["AppmeshRouteSpecGrpcRouteMatchMetadataMatch"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecGrpcRouteMatchMetadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshRouteSpecGrpcRouteMatchMetadataList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecGrpcRouteMatchMetadataList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6b9c5e9850f578d2f0ca20d4803bf1db798e5b3697b1d01a2e1c24e237739e5a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AppmeshRouteSpecGrpcRouteMatchMetadataOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7b8fd4a526cd30abc5e30ec8fb353438bc996737f7f3d0b3f2c6ca498d38674)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppmeshRouteSpecGrpcRouteMatchMetadataOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c42a67519ac2ca4186b24f26ad9f1bcf726534e8bdfaab2ec436fe4e85f36c8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a1b3e6748e8862344380c1ebbbbab4a26e82977b7dcb1a29f08c00cc61c666b2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__360d09f5a273c7703d02402f5f128245873ed366c06a4aee6e10647a23156149)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshRouteSpecGrpcRouteMatchMetadata]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshRouteSpecGrpcRouteMatchMetadata]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshRouteSpecGrpcRouteMatchMetadata]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a23d8166d0e0aa91b9379f1c4bac67bc73bf8e890c6c7c2deab72462b8771a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecGrpcRouteMatchMetadataMatch",
    jsii_struct_bases=[],
    name_mapping={
        "exact": "exact",
        "prefix": "prefix",
        "range": "range",
        "regex": "regex",
        "suffix": "suffix",
    },
)
class AppmeshRouteSpecGrpcRouteMatchMetadataMatch:
    def __init__(
        self,
        *,
        exact: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        range: typing.Optional[typing.Union["AppmeshRouteSpecGrpcRouteMatchMetadataMatchRange", typing.Dict[builtins.str, typing.Any]]] = None,
        regex: typing.Optional[builtins.str] = None,
        suffix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param exact: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#exact AppmeshRoute#exact}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#prefix AppmeshRoute#prefix}.
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#range AppmeshRoute#range}
        :param regex: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#regex AppmeshRoute#regex}.
        :param suffix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#suffix AppmeshRoute#suffix}.
        '''
        if isinstance(range, dict):
            range = AppmeshRouteSpecGrpcRouteMatchMetadataMatchRange(**range)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6999507796e6a24dad0580a0b5c608f3715bddb5dbcb04c5fecfa48cc5c2a16)
            check_type(argname="argument exact", value=exact, expected_type=type_hints["exact"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument range", value=range, expected_type=type_hints["range"])
            check_type(argname="argument regex", value=regex, expected_type=type_hints["regex"])
            check_type(argname="argument suffix", value=suffix, expected_type=type_hints["suffix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if exact is not None:
            self._values["exact"] = exact
        if prefix is not None:
            self._values["prefix"] = prefix
        if range is not None:
            self._values["range"] = range
        if regex is not None:
            self._values["regex"] = regex
        if suffix is not None:
            self._values["suffix"] = suffix

    @builtins.property
    def exact(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#exact AppmeshRoute#exact}.'''
        result = self._values.get("exact")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#prefix AppmeshRoute#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def range(
        self,
    ) -> typing.Optional["AppmeshRouteSpecGrpcRouteMatchMetadataMatchRange"]:
        '''range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#range AppmeshRoute#range}
        '''
        result = self._values.get("range")
        return typing.cast(typing.Optional["AppmeshRouteSpecGrpcRouteMatchMetadataMatchRange"], result)

    @builtins.property
    def regex(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#regex AppmeshRoute#regex}.'''
        result = self._values.get("regex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def suffix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#suffix AppmeshRoute#suffix}.'''
        result = self._values.get("suffix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecGrpcRouteMatchMetadataMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshRouteSpecGrpcRouteMatchMetadataMatchOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecGrpcRouteMatchMetadataMatchOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e2db06ebcbc67280137e012a207781816c8a47f9a6df4d19f1decb248df9e4c6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRange")
    def put_range(self, *, end: jsii.Number, start: jsii.Number) -> None:
        '''
        :param end: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#end AppmeshRoute#end}.
        :param start: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#start AppmeshRoute#start}.
        '''
        value = AppmeshRouteSpecGrpcRouteMatchMetadataMatchRange(end=end, start=start)

        return typing.cast(None, jsii.invoke(self, "putRange", [value]))

    @jsii.member(jsii_name="resetExact")
    def reset_exact(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExact", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @jsii.member(jsii_name="resetRange")
    def reset_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRange", []))

    @jsii.member(jsii_name="resetRegex")
    def reset_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegex", []))

    @jsii.member(jsii_name="resetSuffix")
    def reset_suffix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuffix", []))

    @builtins.property
    @jsii.member(jsii_name="range")
    def range(
        self,
    ) -> "AppmeshRouteSpecGrpcRouteMatchMetadataMatchRangeOutputReference":
        return typing.cast("AppmeshRouteSpecGrpcRouteMatchMetadataMatchRangeOutputReference", jsii.get(self, "range"))

    @builtins.property
    @jsii.member(jsii_name="exactInput")
    def exact_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "exactInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="rangeInput")
    def range_input(
        self,
    ) -> typing.Optional["AppmeshRouteSpecGrpcRouteMatchMetadataMatchRange"]:
        return typing.cast(typing.Optional["AppmeshRouteSpecGrpcRouteMatchMetadataMatchRange"], jsii.get(self, "rangeInput"))

    @builtins.property
    @jsii.member(jsii_name="regexInput")
    def regex_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regexInput"))

    @builtins.property
    @jsii.member(jsii_name="suffixInput")
    def suffix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "suffixInput"))

    @builtins.property
    @jsii.member(jsii_name="exact")
    def exact(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "exact"))

    @exact.setter
    def exact(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f404bfb4a93e7bad6fbd7fb8ece0c69dabcf09cb74d524b0ddc7bac41aab0c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exact", value)

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f99525424ad2c3456f5edb2082386b09ac7f44e8f5b34a9ec284d1e16772bcbc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="regex")
    def regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "regex"))

    @regex.setter
    def regex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75f3b5eb368dae5a3c75c793c1f721799a1eccf4452e026c76b3af983662cd1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regex", value)

    @builtins.property
    @jsii.member(jsii_name="suffix")
    def suffix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "suffix"))

    @suffix.setter
    def suffix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__328c0f5180b92a172c11e765c2c106a566c47cfb11797bb72852c8a793b0bb16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "suffix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshRouteSpecGrpcRouteMatchMetadataMatch]:
        return typing.cast(typing.Optional[AppmeshRouteSpecGrpcRouteMatchMetadataMatch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshRouteSpecGrpcRouteMatchMetadataMatch],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f69401d3400e45c6e3c3a9e0acbdedea8f3024a59a84a74f2f21242eb48828f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecGrpcRouteMatchMetadataMatchRange",
    jsii_struct_bases=[],
    name_mapping={"end": "end", "start": "start"},
)
class AppmeshRouteSpecGrpcRouteMatchMetadataMatchRange:
    def __init__(self, *, end: jsii.Number, start: jsii.Number) -> None:
        '''
        :param end: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#end AppmeshRoute#end}.
        :param start: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#start AppmeshRoute#start}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80e2a66ff8d38cb1edf4cf31f776a81965812b2b459fa1d8ea4f1f49f272e312)
            check_type(argname="argument end", value=end, expected_type=type_hints["end"])
            check_type(argname="argument start", value=start, expected_type=type_hints["start"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "end": end,
            "start": start,
        }

    @builtins.property
    def end(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#end AppmeshRoute#end}.'''
        result = self._values.get("end")
        assert result is not None, "Required property 'end' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def start(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#start AppmeshRoute#start}.'''
        result = self._values.get("start")
        assert result is not None, "Required property 'start' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecGrpcRouteMatchMetadataMatchRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshRouteSpecGrpcRouteMatchMetadataMatchRangeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecGrpcRouteMatchMetadataMatchRangeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6f31e9c3c59fffe96b36f59ead4ec2c481a0343347eff509961262fe2f371027)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="endInput")
    def end_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "endInput"))

    @builtins.property
    @jsii.member(jsii_name="startInput")
    def start_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "startInput"))

    @builtins.property
    @jsii.member(jsii_name="end")
    def end(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "end"))

    @end.setter
    def end(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83782a7961265f9a4f7fc090a112245a0470b3901e6281711fe14ea8cbffa64b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "end", value)

    @builtins.property
    @jsii.member(jsii_name="start")
    def start(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "start"))

    @start.setter
    def start(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9523916225796accd845a61f40d91060e8a9f8c969ea969e60b292661d0b492)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "start", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshRouteSpecGrpcRouteMatchMetadataMatchRange]:
        return typing.cast(typing.Optional[AppmeshRouteSpecGrpcRouteMatchMetadataMatchRange], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshRouteSpecGrpcRouteMatchMetadataMatchRange],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e9eb7648b53073c5080a8b5d6cdc00bb7d636406b4125a8ff80370cbc4d05d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshRouteSpecGrpcRouteMatchMetadataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecGrpcRouteMatchMetadataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__46e4b150615b9d39c3ad89beef7c738129a7bbed08899bc8a058bc20d8e7feb9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMatch")
    def put_match(
        self,
        *,
        exact: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        range: typing.Optional[typing.Union[AppmeshRouteSpecGrpcRouteMatchMetadataMatchRange, typing.Dict[builtins.str, typing.Any]]] = None,
        regex: typing.Optional[builtins.str] = None,
        suffix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param exact: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#exact AppmeshRoute#exact}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#prefix AppmeshRoute#prefix}.
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#range AppmeshRoute#range}
        :param regex: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#regex AppmeshRoute#regex}.
        :param suffix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#suffix AppmeshRoute#suffix}.
        '''
        value = AppmeshRouteSpecGrpcRouteMatchMetadataMatch(
            exact=exact, prefix=prefix, range=range, regex=regex, suffix=suffix
        )

        return typing.cast(None, jsii.invoke(self, "putMatch", [value]))

    @jsii.member(jsii_name="resetInvert")
    def reset_invert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInvert", []))

    @jsii.member(jsii_name="resetMatch")
    def reset_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatch", []))

    @builtins.property
    @jsii.member(jsii_name="match")
    def match(self) -> AppmeshRouteSpecGrpcRouteMatchMetadataMatchOutputReference:
        return typing.cast(AppmeshRouteSpecGrpcRouteMatchMetadataMatchOutputReference, jsii.get(self, "match"))

    @builtins.property
    @jsii.member(jsii_name="invertInput")
    def invert_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "invertInput"))

    @builtins.property
    @jsii.member(jsii_name="matchInput")
    def match_input(
        self,
    ) -> typing.Optional[AppmeshRouteSpecGrpcRouteMatchMetadataMatch]:
        return typing.cast(typing.Optional[AppmeshRouteSpecGrpcRouteMatchMetadataMatch], jsii.get(self, "matchInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="invert")
    def invert(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "invert"))

    @invert.setter
    def invert(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cde7b582f4356b82fde650e8c8192d837c136be44233711fe102d8649ed834d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "invert", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f25644d2626755c7f7c43ab6c95736ece76a8a4afc80abf6a8a1e62ec5a410cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppmeshRouteSpecGrpcRouteMatchMetadata, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppmeshRouteSpecGrpcRouteMatchMetadata, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppmeshRouteSpecGrpcRouteMatchMetadata, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c39d086f769ef688ae0607fdc325105ff134965fd90f04b86bcd3ec491ef7a43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshRouteSpecGrpcRouteMatchOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecGrpcRouteMatchOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__692c5970f6bfa914fedb05549b238f9402c316483e229d04d231fcfbccca58a5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMetadata")
    def put_metadata(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppmeshRouteSpecGrpcRouteMatchMetadata, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5cff764febb639b12f7b3b69b7848dbe279d9ac65fe268cb0a0200eb05c5cdc3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMetadata", [value]))

    @jsii.member(jsii_name="resetMetadata")
    def reset_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadata", []))

    @jsii.member(jsii_name="resetMethodName")
    def reset_method_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMethodName", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @jsii.member(jsii_name="resetServiceName")
    def reset_service_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceName", []))

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> AppmeshRouteSpecGrpcRouteMatchMetadataList:
        return typing.cast(AppmeshRouteSpecGrpcRouteMatchMetadataList, jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshRouteSpecGrpcRouteMatchMetadata]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshRouteSpecGrpcRouteMatchMetadata]]], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="methodNameInput")
    def method_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "methodNameInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceNameInput")
    def service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="methodName")
    def method_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "methodName"))

    @method_name.setter
    def method_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__244c4e02f6f357fdc56c7f950f6529c7c4fa72dd02afcb9161235d68288fe99a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "methodName", value)

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2536b5c1533ed11718c66c8265ea1101bcc7763b6b5fe814df807de6a66dd3d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceName"))

    @service_name.setter
    def service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56d009b955d4d952a294cd709fd224a3bee609fbf84b3adb2cfb6a1d258ed02c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshRouteSpecGrpcRouteMatch]:
        return typing.cast(typing.Optional[AppmeshRouteSpecGrpcRouteMatch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshRouteSpecGrpcRouteMatch],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c3b27ad442456a05c7b68d0c8d99caca5337bd77cc927d16a3ad43daf08cc1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshRouteSpecGrpcRouteOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecGrpcRouteOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8db137452782a41137825c14d8ceb81625d34d0948ab7f12766e037a726b9f96)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAction")
    def put_action(
        self,
        *,
        weighted_target: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppmeshRouteSpecGrpcRouteActionWeightedTarget, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param weighted_target: weighted_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#weighted_target AppmeshRoute#weighted_target}
        '''
        value = AppmeshRouteSpecGrpcRouteAction(weighted_target=weighted_target)

        return typing.cast(None, jsii.invoke(self, "putAction", [value]))

    @jsii.member(jsii_name="putMatch")
    def put_match(
        self,
        *,
        metadata: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppmeshRouteSpecGrpcRouteMatchMetadata, typing.Dict[builtins.str, typing.Any]]]]] = None,
        method_name: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        service_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#metadata AppmeshRoute#metadata}
        :param method_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#method_name AppmeshRoute#method_name}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#prefix AppmeshRoute#prefix}.
        :param service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#service_name AppmeshRoute#service_name}.
        '''
        value = AppmeshRouteSpecGrpcRouteMatch(
            metadata=metadata,
            method_name=method_name,
            prefix=prefix,
            service_name=service_name,
        )

        return typing.cast(None, jsii.invoke(self, "putMatch", [value]))

    @jsii.member(jsii_name="putRetryPolicy")
    def put_retry_policy(
        self,
        *,
        max_retries: jsii.Number,
        per_retry_timeout: typing.Union["AppmeshRouteSpecGrpcRouteRetryPolicyPerRetryTimeout", typing.Dict[builtins.str, typing.Any]],
        grpc_retry_events: typing.Optional[typing.Sequence[builtins.str]] = None,
        http_retry_events: typing.Optional[typing.Sequence[builtins.str]] = None,
        tcp_retry_events: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param max_retries: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#max_retries AppmeshRoute#max_retries}.
        :param per_retry_timeout: per_retry_timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#per_retry_timeout AppmeshRoute#per_retry_timeout}
        :param grpc_retry_events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#grpc_retry_events AppmeshRoute#grpc_retry_events}.
        :param http_retry_events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#http_retry_events AppmeshRoute#http_retry_events}.
        :param tcp_retry_events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#tcp_retry_events AppmeshRoute#tcp_retry_events}.
        '''
        value = AppmeshRouteSpecGrpcRouteRetryPolicy(
            max_retries=max_retries,
            per_retry_timeout=per_retry_timeout,
            grpc_retry_events=grpc_retry_events,
            http_retry_events=http_retry_events,
            tcp_retry_events=tcp_retry_events,
        )

        return typing.cast(None, jsii.invoke(self, "putRetryPolicy", [value]))

    @jsii.member(jsii_name="putTimeout")
    def put_timeout(
        self,
        *,
        idle: typing.Optional[typing.Union["AppmeshRouteSpecGrpcRouteTimeoutIdle", typing.Dict[builtins.str, typing.Any]]] = None,
        per_request: typing.Optional[typing.Union["AppmeshRouteSpecGrpcRouteTimeoutPerRequest", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param idle: idle block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#idle AppmeshRoute#idle}
        :param per_request: per_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#per_request AppmeshRoute#per_request}
        '''
        value = AppmeshRouteSpecGrpcRouteTimeout(idle=idle, per_request=per_request)

        return typing.cast(None, jsii.invoke(self, "putTimeout", [value]))

    @jsii.member(jsii_name="resetMatch")
    def reset_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatch", []))

    @jsii.member(jsii_name="resetRetryPolicy")
    def reset_retry_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetryPolicy", []))

    @jsii.member(jsii_name="resetTimeout")
    def reset_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeout", []))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> AppmeshRouteSpecGrpcRouteActionOutputReference:
        return typing.cast(AppmeshRouteSpecGrpcRouteActionOutputReference, jsii.get(self, "action"))

    @builtins.property
    @jsii.member(jsii_name="match")
    def match(self) -> AppmeshRouteSpecGrpcRouteMatchOutputReference:
        return typing.cast(AppmeshRouteSpecGrpcRouteMatchOutputReference, jsii.get(self, "match"))

    @builtins.property
    @jsii.member(jsii_name="retryPolicy")
    def retry_policy(self) -> "AppmeshRouteSpecGrpcRouteRetryPolicyOutputReference":
        return typing.cast("AppmeshRouteSpecGrpcRouteRetryPolicyOutputReference", jsii.get(self, "retryPolicy"))

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> "AppmeshRouteSpecGrpcRouteTimeoutOutputReference":
        return typing.cast("AppmeshRouteSpecGrpcRouteTimeoutOutputReference", jsii.get(self, "timeout"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[AppmeshRouteSpecGrpcRouteAction]:
        return typing.cast(typing.Optional[AppmeshRouteSpecGrpcRouteAction], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="matchInput")
    def match_input(self) -> typing.Optional[AppmeshRouteSpecGrpcRouteMatch]:
        return typing.cast(typing.Optional[AppmeshRouteSpecGrpcRouteMatch], jsii.get(self, "matchInput"))

    @builtins.property
    @jsii.member(jsii_name="retryPolicyInput")
    def retry_policy_input(
        self,
    ) -> typing.Optional["AppmeshRouteSpecGrpcRouteRetryPolicy"]:
        return typing.cast(typing.Optional["AppmeshRouteSpecGrpcRouteRetryPolicy"], jsii.get(self, "retryPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(self) -> typing.Optional["AppmeshRouteSpecGrpcRouteTimeout"]:
        return typing.cast(typing.Optional["AppmeshRouteSpecGrpcRouteTimeout"], jsii.get(self, "timeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshRouteSpecGrpcRoute]:
        return typing.cast(typing.Optional[AppmeshRouteSpecGrpcRoute], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppmeshRouteSpecGrpcRoute]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9db9e0377d9201075f081972c15e3c7026da0b8202b303efb895ce9de7d0e848)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecGrpcRouteRetryPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "max_retries": "maxRetries",
        "per_retry_timeout": "perRetryTimeout",
        "grpc_retry_events": "grpcRetryEvents",
        "http_retry_events": "httpRetryEvents",
        "tcp_retry_events": "tcpRetryEvents",
    },
)
class AppmeshRouteSpecGrpcRouteRetryPolicy:
    def __init__(
        self,
        *,
        max_retries: jsii.Number,
        per_retry_timeout: typing.Union["AppmeshRouteSpecGrpcRouteRetryPolicyPerRetryTimeout", typing.Dict[builtins.str, typing.Any]],
        grpc_retry_events: typing.Optional[typing.Sequence[builtins.str]] = None,
        http_retry_events: typing.Optional[typing.Sequence[builtins.str]] = None,
        tcp_retry_events: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param max_retries: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#max_retries AppmeshRoute#max_retries}.
        :param per_retry_timeout: per_retry_timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#per_retry_timeout AppmeshRoute#per_retry_timeout}
        :param grpc_retry_events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#grpc_retry_events AppmeshRoute#grpc_retry_events}.
        :param http_retry_events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#http_retry_events AppmeshRoute#http_retry_events}.
        :param tcp_retry_events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#tcp_retry_events AppmeshRoute#tcp_retry_events}.
        '''
        if isinstance(per_retry_timeout, dict):
            per_retry_timeout = AppmeshRouteSpecGrpcRouteRetryPolicyPerRetryTimeout(**per_retry_timeout)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a433619ff60dedcb54e5508b2559647157115f1ad20a0723cb8024c223b5ac8e)
            check_type(argname="argument max_retries", value=max_retries, expected_type=type_hints["max_retries"])
            check_type(argname="argument per_retry_timeout", value=per_retry_timeout, expected_type=type_hints["per_retry_timeout"])
            check_type(argname="argument grpc_retry_events", value=grpc_retry_events, expected_type=type_hints["grpc_retry_events"])
            check_type(argname="argument http_retry_events", value=http_retry_events, expected_type=type_hints["http_retry_events"])
            check_type(argname="argument tcp_retry_events", value=tcp_retry_events, expected_type=type_hints["tcp_retry_events"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "max_retries": max_retries,
            "per_retry_timeout": per_retry_timeout,
        }
        if grpc_retry_events is not None:
            self._values["grpc_retry_events"] = grpc_retry_events
        if http_retry_events is not None:
            self._values["http_retry_events"] = http_retry_events
        if tcp_retry_events is not None:
            self._values["tcp_retry_events"] = tcp_retry_events

    @builtins.property
    def max_retries(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#max_retries AppmeshRoute#max_retries}.'''
        result = self._values.get("max_retries")
        assert result is not None, "Required property 'max_retries' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def per_retry_timeout(
        self,
    ) -> "AppmeshRouteSpecGrpcRouteRetryPolicyPerRetryTimeout":
        '''per_retry_timeout block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#per_retry_timeout AppmeshRoute#per_retry_timeout}
        '''
        result = self._values.get("per_retry_timeout")
        assert result is not None, "Required property 'per_retry_timeout' is missing"
        return typing.cast("AppmeshRouteSpecGrpcRouteRetryPolicyPerRetryTimeout", result)

    @builtins.property
    def grpc_retry_events(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#grpc_retry_events AppmeshRoute#grpc_retry_events}.'''
        result = self._values.get("grpc_retry_events")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def http_retry_events(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#http_retry_events AppmeshRoute#http_retry_events}.'''
        result = self._values.get("http_retry_events")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tcp_retry_events(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#tcp_retry_events AppmeshRoute#tcp_retry_events}.'''
        result = self._values.get("tcp_retry_events")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecGrpcRouteRetryPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshRouteSpecGrpcRouteRetryPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecGrpcRouteRetryPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8be5d73fe085f9fca4221d19fb082a7674d81f5152b0ca85f3f249aa7a5278ab)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPerRetryTimeout")
    def put_per_retry_timeout(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#unit AppmeshRoute#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#value AppmeshRoute#value}.
        '''
        value_ = AppmeshRouteSpecGrpcRouteRetryPolicyPerRetryTimeout(
            unit=unit, value=value
        )

        return typing.cast(None, jsii.invoke(self, "putPerRetryTimeout", [value_]))

    @jsii.member(jsii_name="resetGrpcRetryEvents")
    def reset_grpc_retry_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGrpcRetryEvents", []))

    @jsii.member(jsii_name="resetHttpRetryEvents")
    def reset_http_retry_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpRetryEvents", []))

    @jsii.member(jsii_name="resetTcpRetryEvents")
    def reset_tcp_retry_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTcpRetryEvents", []))

    @builtins.property
    @jsii.member(jsii_name="perRetryTimeout")
    def per_retry_timeout(
        self,
    ) -> "AppmeshRouteSpecGrpcRouteRetryPolicyPerRetryTimeoutOutputReference":
        return typing.cast("AppmeshRouteSpecGrpcRouteRetryPolicyPerRetryTimeoutOutputReference", jsii.get(self, "perRetryTimeout"))

    @builtins.property
    @jsii.member(jsii_name="grpcRetryEventsInput")
    def grpc_retry_events_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "grpcRetryEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="httpRetryEventsInput")
    def http_retry_events_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "httpRetryEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxRetriesInput")
    def max_retries_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxRetriesInput"))

    @builtins.property
    @jsii.member(jsii_name="perRetryTimeoutInput")
    def per_retry_timeout_input(
        self,
    ) -> typing.Optional["AppmeshRouteSpecGrpcRouteRetryPolicyPerRetryTimeout"]:
        return typing.cast(typing.Optional["AppmeshRouteSpecGrpcRouteRetryPolicyPerRetryTimeout"], jsii.get(self, "perRetryTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="tcpRetryEventsInput")
    def tcp_retry_events_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tcpRetryEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="grpcRetryEvents")
    def grpc_retry_events(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "grpcRetryEvents"))

    @grpc_retry_events.setter
    def grpc_retry_events(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b3874db100b34a10f81feadbf41da0fbb73b2586f92c309f3fa3f60042eca04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "grpcRetryEvents", value)

    @builtins.property
    @jsii.member(jsii_name="httpRetryEvents")
    def http_retry_events(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "httpRetryEvents"))

    @http_retry_events.setter
    def http_retry_events(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07f3bb6e74494e6fac537ee2a1283c54f18a70c60ef946b2094e33f7c11182af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpRetryEvents", value)

    @builtins.property
    @jsii.member(jsii_name="maxRetries")
    def max_retries(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxRetries"))

    @max_retries.setter
    def max_retries(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f901a63d62b4aa7485b645933bca5c2269124bd4756f7677add54f395883aff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxRetries", value)

    @builtins.property
    @jsii.member(jsii_name="tcpRetryEvents")
    def tcp_retry_events(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tcpRetryEvents"))

    @tcp_retry_events.setter
    def tcp_retry_events(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0de05ccf8248ae08b41e60609bda57ba6eddd211acdeb0ab3258df2712085c3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tcpRetryEvents", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshRouteSpecGrpcRouteRetryPolicy]:
        return typing.cast(typing.Optional[AppmeshRouteSpecGrpcRouteRetryPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshRouteSpecGrpcRouteRetryPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46c296bee6c57239bbb5d5938a87e3eb5e61b0cc746be5731153a05032a4a2cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecGrpcRouteRetryPolicyPerRetryTimeout",
    jsii_struct_bases=[],
    name_mapping={"unit": "unit", "value": "value"},
)
class AppmeshRouteSpecGrpcRouteRetryPolicyPerRetryTimeout:
    def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#unit AppmeshRoute#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#value AppmeshRoute#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91d042704cbd63dca9b1272afa6af17665e3ff5ee0db0a3c5be596a159629cd6)
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "unit": unit,
            "value": value,
        }

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#unit AppmeshRoute#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#value AppmeshRoute#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecGrpcRouteRetryPolicyPerRetryTimeout(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshRouteSpecGrpcRouteRetryPolicyPerRetryTimeoutOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecGrpcRouteRetryPolicyPerRetryTimeoutOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c31e51e64352b8b0c9470fdf91112b199c09bb961264f89929a7ccf39064cc2a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__57f42b3b5fb85cc519a654a64ae153ead1c0cff5c56cad64afbc9472ee6b3b13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb7cf42b16e8dca0e5148942020d970ee1dd204899a308028c8dcf560b64a39d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshRouteSpecGrpcRouteRetryPolicyPerRetryTimeout]:
        return typing.cast(typing.Optional[AppmeshRouteSpecGrpcRouteRetryPolicyPerRetryTimeout], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshRouteSpecGrpcRouteRetryPolicyPerRetryTimeout],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d7bf76e1d7c3fbd4c55897c1606c7a42e8ea9b63dedb68559f3832b9d9e8a96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecGrpcRouteTimeout",
    jsii_struct_bases=[],
    name_mapping={"idle": "idle", "per_request": "perRequest"},
)
class AppmeshRouteSpecGrpcRouteTimeout:
    def __init__(
        self,
        *,
        idle: typing.Optional[typing.Union["AppmeshRouteSpecGrpcRouteTimeoutIdle", typing.Dict[builtins.str, typing.Any]]] = None,
        per_request: typing.Optional[typing.Union["AppmeshRouteSpecGrpcRouteTimeoutPerRequest", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param idle: idle block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#idle AppmeshRoute#idle}
        :param per_request: per_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#per_request AppmeshRoute#per_request}
        '''
        if isinstance(idle, dict):
            idle = AppmeshRouteSpecGrpcRouteTimeoutIdle(**idle)
        if isinstance(per_request, dict):
            per_request = AppmeshRouteSpecGrpcRouteTimeoutPerRequest(**per_request)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__215c9ac86a95796584cc2be5cc340f5541dedf487f7e3d17e5e062a4cb99df48)
            check_type(argname="argument idle", value=idle, expected_type=type_hints["idle"])
            check_type(argname="argument per_request", value=per_request, expected_type=type_hints["per_request"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if idle is not None:
            self._values["idle"] = idle
        if per_request is not None:
            self._values["per_request"] = per_request

    @builtins.property
    def idle(self) -> typing.Optional["AppmeshRouteSpecGrpcRouteTimeoutIdle"]:
        '''idle block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#idle AppmeshRoute#idle}
        '''
        result = self._values.get("idle")
        return typing.cast(typing.Optional["AppmeshRouteSpecGrpcRouteTimeoutIdle"], result)

    @builtins.property
    def per_request(
        self,
    ) -> typing.Optional["AppmeshRouteSpecGrpcRouteTimeoutPerRequest"]:
        '''per_request block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#per_request AppmeshRoute#per_request}
        '''
        result = self._values.get("per_request")
        return typing.cast(typing.Optional["AppmeshRouteSpecGrpcRouteTimeoutPerRequest"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecGrpcRouteTimeout(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecGrpcRouteTimeoutIdle",
    jsii_struct_bases=[],
    name_mapping={"unit": "unit", "value": "value"},
)
class AppmeshRouteSpecGrpcRouteTimeoutIdle:
    def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#unit AppmeshRoute#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#value AppmeshRoute#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c13b19a81f3a07ad124cdd3e44167dbf3be28b461dad9e37accf3e86f8249257)
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "unit": unit,
            "value": value,
        }

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#unit AppmeshRoute#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#value AppmeshRoute#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecGrpcRouteTimeoutIdle(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshRouteSpecGrpcRouteTimeoutIdleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecGrpcRouteTimeoutIdleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6beb400bbd1dfde7bb07a43e09221372627558c18df80c58b240bdfda0986e3b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2528f7af55147755d6e2f2f6df74a2e740834219979be7685e117e5dc150916b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5f188309bd3493943ef76e4f3d296870deb17c94a924cb0d7172c63e003dca8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshRouteSpecGrpcRouteTimeoutIdle]:
        return typing.cast(typing.Optional[AppmeshRouteSpecGrpcRouteTimeoutIdle], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshRouteSpecGrpcRouteTimeoutIdle],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb6b4117bb3440f747a606fb49052979e390c3ff7b335ff27bfe6c52a5f6af03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshRouteSpecGrpcRouteTimeoutOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecGrpcRouteTimeoutOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b49bfb1f7ca2345ecaf3821c84b845b1457572e67eff28245429912cffaaf3e5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putIdle")
    def put_idle(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#unit AppmeshRoute#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#value AppmeshRoute#value}.
        '''
        value_ = AppmeshRouteSpecGrpcRouteTimeoutIdle(unit=unit, value=value)

        return typing.cast(None, jsii.invoke(self, "putIdle", [value_]))

    @jsii.member(jsii_name="putPerRequest")
    def put_per_request(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#unit AppmeshRoute#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#value AppmeshRoute#value}.
        '''
        value_ = AppmeshRouteSpecGrpcRouteTimeoutPerRequest(unit=unit, value=value)

        return typing.cast(None, jsii.invoke(self, "putPerRequest", [value_]))

    @jsii.member(jsii_name="resetIdle")
    def reset_idle(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdle", []))

    @jsii.member(jsii_name="resetPerRequest")
    def reset_per_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPerRequest", []))

    @builtins.property
    @jsii.member(jsii_name="idle")
    def idle(self) -> AppmeshRouteSpecGrpcRouteTimeoutIdleOutputReference:
        return typing.cast(AppmeshRouteSpecGrpcRouteTimeoutIdleOutputReference, jsii.get(self, "idle"))

    @builtins.property
    @jsii.member(jsii_name="perRequest")
    def per_request(
        self,
    ) -> "AppmeshRouteSpecGrpcRouteTimeoutPerRequestOutputReference":
        return typing.cast("AppmeshRouteSpecGrpcRouteTimeoutPerRequestOutputReference", jsii.get(self, "perRequest"))

    @builtins.property
    @jsii.member(jsii_name="idleInput")
    def idle_input(self) -> typing.Optional[AppmeshRouteSpecGrpcRouteTimeoutIdle]:
        return typing.cast(typing.Optional[AppmeshRouteSpecGrpcRouteTimeoutIdle], jsii.get(self, "idleInput"))

    @builtins.property
    @jsii.member(jsii_name="perRequestInput")
    def per_request_input(
        self,
    ) -> typing.Optional["AppmeshRouteSpecGrpcRouteTimeoutPerRequest"]:
        return typing.cast(typing.Optional["AppmeshRouteSpecGrpcRouteTimeoutPerRequest"], jsii.get(self, "perRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshRouteSpecGrpcRouteTimeout]:
        return typing.cast(typing.Optional[AppmeshRouteSpecGrpcRouteTimeout], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshRouteSpecGrpcRouteTimeout],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33a6ef38a824881968f53a64344d11f8d7ed4e76bca098c8f53e8d21b7310580)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecGrpcRouteTimeoutPerRequest",
    jsii_struct_bases=[],
    name_mapping={"unit": "unit", "value": "value"},
)
class AppmeshRouteSpecGrpcRouteTimeoutPerRequest:
    def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#unit AppmeshRoute#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#value AppmeshRoute#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a5516844260162667ca4c143f4cdd7ff5a210fd37913cba7a5cb361ec551213)
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "unit": unit,
            "value": value,
        }

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#unit AppmeshRoute#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#value AppmeshRoute#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecGrpcRouteTimeoutPerRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshRouteSpecGrpcRouteTimeoutPerRequestOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecGrpcRouteTimeoutPerRequestOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bff3c4866a05f5b8734fd84de617bf43a5e6a1860d977b8a54db7e66a6be5f26)
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
            type_hints = typing.get_type_hints(_typecheckingstub__44c5d7459f87ff64de40598980025a056d3c437556c15a7d572cb4af80cf79a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__482bbb23740de2d51e6a908c41c074796654937efaabcfde7d387c8980c7e80e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshRouteSpecGrpcRouteTimeoutPerRequest]:
        return typing.cast(typing.Optional[AppmeshRouteSpecGrpcRouteTimeoutPerRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshRouteSpecGrpcRouteTimeoutPerRequest],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5665b2143565d04980ccf42bc8537779a4b23ce3e731f1926d724d599a90f506)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttp2Route",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "match": "match",
        "retry_policy": "retryPolicy",
        "timeout": "timeout",
    },
)
class AppmeshRouteSpecHttp2Route:
    def __init__(
        self,
        *,
        action: typing.Union["AppmeshRouteSpecHttp2RouteAction", typing.Dict[builtins.str, typing.Any]],
        match: typing.Union["AppmeshRouteSpecHttp2RouteMatch", typing.Dict[builtins.str, typing.Any]],
        retry_policy: typing.Optional[typing.Union["AppmeshRouteSpecHttp2RouteRetryPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        timeout: typing.Optional[typing.Union["AppmeshRouteSpecHttp2RouteTimeout", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#action AppmeshRoute#action}
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#match AppmeshRoute#match}
        :param retry_policy: retry_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#retry_policy AppmeshRoute#retry_policy}
        :param timeout: timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#timeout AppmeshRoute#timeout}
        '''
        if isinstance(action, dict):
            action = AppmeshRouteSpecHttp2RouteAction(**action)
        if isinstance(match, dict):
            match = AppmeshRouteSpecHttp2RouteMatch(**match)
        if isinstance(retry_policy, dict):
            retry_policy = AppmeshRouteSpecHttp2RouteRetryPolicy(**retry_policy)
        if isinstance(timeout, dict):
            timeout = AppmeshRouteSpecHttp2RouteTimeout(**timeout)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0aaed28fb43b7d062cd3afcb708865cc176d5586d8bc2bb7df975dac5a8d29a)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument match", value=match, expected_type=type_hints["match"])
            check_type(argname="argument retry_policy", value=retry_policy, expected_type=type_hints["retry_policy"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action": action,
            "match": match,
        }
        if retry_policy is not None:
            self._values["retry_policy"] = retry_policy
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def action(self) -> "AppmeshRouteSpecHttp2RouteAction":
        '''action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#action AppmeshRoute#action}
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast("AppmeshRouteSpecHttp2RouteAction", result)

    @builtins.property
    def match(self) -> "AppmeshRouteSpecHttp2RouteMatch":
        '''match block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#match AppmeshRoute#match}
        '''
        result = self._values.get("match")
        assert result is not None, "Required property 'match' is missing"
        return typing.cast("AppmeshRouteSpecHttp2RouteMatch", result)

    @builtins.property
    def retry_policy(self) -> typing.Optional["AppmeshRouteSpecHttp2RouteRetryPolicy"]:
        '''retry_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#retry_policy AppmeshRoute#retry_policy}
        '''
        result = self._values.get("retry_policy")
        return typing.cast(typing.Optional["AppmeshRouteSpecHttp2RouteRetryPolicy"], result)

    @builtins.property
    def timeout(self) -> typing.Optional["AppmeshRouteSpecHttp2RouteTimeout"]:
        '''timeout block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#timeout AppmeshRoute#timeout}
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional["AppmeshRouteSpecHttp2RouteTimeout"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecHttp2Route(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttp2RouteAction",
    jsii_struct_bases=[],
    name_mapping={"weighted_target": "weightedTarget"},
)
class AppmeshRouteSpecHttp2RouteAction:
    def __init__(
        self,
        *,
        weighted_target: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AppmeshRouteSpecHttp2RouteActionWeightedTarget", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param weighted_target: weighted_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#weighted_target AppmeshRoute#weighted_target}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8d7e49927c80f4f357f3891371be93458b355f09bb65fe825365c9b3346d8b1)
            check_type(argname="argument weighted_target", value=weighted_target, expected_type=type_hints["weighted_target"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "weighted_target": weighted_target,
        }

    @builtins.property
    def weighted_target(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppmeshRouteSpecHttp2RouteActionWeightedTarget"]]:
        '''weighted_target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#weighted_target AppmeshRoute#weighted_target}
        '''
        result = self._values.get("weighted_target")
        assert result is not None, "Required property 'weighted_target' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppmeshRouteSpecHttp2RouteActionWeightedTarget"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecHttp2RouteAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshRouteSpecHttp2RouteActionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttp2RouteActionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__99fd4f7e43a75c4373b5a94d2629524894330aaa5c477973323c30f4d23cb56f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putWeightedTarget")
    def put_weighted_target(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AppmeshRouteSpecHttp2RouteActionWeightedTarget", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e048c5fa04ddd1e25aea9539beee5eddffd491bb5b6ef9fe3c21ed0ed08bc1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWeightedTarget", [value]))

    @builtins.property
    @jsii.member(jsii_name="weightedTarget")
    def weighted_target(self) -> "AppmeshRouteSpecHttp2RouteActionWeightedTargetList":
        return typing.cast("AppmeshRouteSpecHttp2RouteActionWeightedTargetList", jsii.get(self, "weightedTarget"))

    @builtins.property
    @jsii.member(jsii_name="weightedTargetInput")
    def weighted_target_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppmeshRouteSpecHttp2RouteActionWeightedTarget"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppmeshRouteSpecHttp2RouteActionWeightedTarget"]]], jsii.get(self, "weightedTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshRouteSpecHttp2RouteAction]:
        return typing.cast(typing.Optional[AppmeshRouteSpecHttp2RouteAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshRouteSpecHttp2RouteAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__062852739e47f8b1f6eaa5700d16a415e02da52ca2f40e828d138edf8c3a0771)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttp2RouteActionWeightedTarget",
    jsii_struct_bases=[],
    name_mapping={"virtual_node": "virtualNode", "weight": "weight"},
)
class AppmeshRouteSpecHttp2RouteActionWeightedTarget:
    def __init__(self, *, virtual_node: builtins.str, weight: jsii.Number) -> None:
        '''
        :param virtual_node: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#virtual_node AppmeshRoute#virtual_node}.
        :param weight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#weight AppmeshRoute#weight}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__397cfc70162e4fb72debc1df1571f6cd4c63d8dfe62c19e4fb3ecb6051f259d1)
            check_type(argname="argument virtual_node", value=virtual_node, expected_type=type_hints["virtual_node"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "virtual_node": virtual_node,
            "weight": weight,
        }

    @builtins.property
    def virtual_node(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#virtual_node AppmeshRoute#virtual_node}.'''
        result = self._values.get("virtual_node")
        assert result is not None, "Required property 'virtual_node' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def weight(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#weight AppmeshRoute#weight}.'''
        result = self._values.get("weight")
        assert result is not None, "Required property 'weight' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecHttp2RouteActionWeightedTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshRouteSpecHttp2RouteActionWeightedTargetList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttp2RouteActionWeightedTargetList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__981bd1d6b26e89c40999714d43d81fc08a2800495d4aa6bf8989fab5c3dc173a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AppmeshRouteSpecHttp2RouteActionWeightedTargetOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91c3e0cec88bf185dfd278eef763a1a0bc36fbeccf793de9ce252a380bc4b7f6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppmeshRouteSpecHttp2RouteActionWeightedTargetOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e564b010037706ce4fb16a2187d19716cc3d5a98ae9623f825c9051803dabbe5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__22f42c7e43716d6606830fa263fe062da70be2a2e9e2ce866a8c0d80510705a2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8a0e26de173c21d8688ad24ce532532be7eaed193b8f2c45a0efc9d3f4ee9aaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshRouteSpecHttp2RouteActionWeightedTarget]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshRouteSpecHttp2RouteActionWeightedTarget]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshRouteSpecHttp2RouteActionWeightedTarget]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3ebe33cb8447f0c5f873b23ecb07efa312577b9d9af033fd0158b69b19c9ae4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshRouteSpecHttp2RouteActionWeightedTargetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttp2RouteActionWeightedTargetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d47ffb0f97bb7b00ed3423c1379ce82108dd7fc5133e4e7a9243c3698ae0a9e7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="virtualNodeInput")
    def virtual_node_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualNodeInput"))

    @builtins.property
    @jsii.member(jsii_name="weightInput")
    def weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNode")
    def virtual_node(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualNode"))

    @virtual_node.setter
    def virtual_node(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c53ca54115396c5596a578267564e960096216cb0499936dc3453c2c5622c087)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualNode", value)

    @builtins.property
    @jsii.member(jsii_name="weight")
    def weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weight"))

    @weight.setter
    def weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f148924bc57722f24b64917027a22bcd399af39eb9e74b4733b2b12922726a6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weight", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppmeshRouteSpecHttp2RouteActionWeightedTarget, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppmeshRouteSpecHttp2RouteActionWeightedTarget, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppmeshRouteSpecHttp2RouteActionWeightedTarget, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__125f0fd8030593eccd25fe4a84c33200a69f775a7bba52ec7e293aa23294b0fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttp2RouteMatch",
    jsii_struct_bases=[],
    name_mapping={
        "prefix": "prefix",
        "header": "header",
        "method": "method",
        "scheme": "scheme",
    },
)
class AppmeshRouteSpecHttp2RouteMatch:
    def __init__(
        self,
        *,
        prefix: builtins.str,
        header: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AppmeshRouteSpecHttp2RouteMatchHeader", typing.Dict[builtins.str, typing.Any]]]]] = None,
        method: typing.Optional[builtins.str] = None,
        scheme: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#prefix AppmeshRoute#prefix}.
        :param header: header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#header AppmeshRoute#header}
        :param method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#method AppmeshRoute#method}.
        :param scheme: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#scheme AppmeshRoute#scheme}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e1e4a7787fdac3df0bb347da487fb1a7be79d5b7469d5c8e7903017432d960c)
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument header", value=header, expected_type=type_hints["header"])
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument scheme", value=scheme, expected_type=type_hints["scheme"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "prefix": prefix,
        }
        if header is not None:
            self._values["header"] = header
        if method is not None:
            self._values["method"] = method
        if scheme is not None:
            self._values["scheme"] = scheme

    @builtins.property
    def prefix(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#prefix AppmeshRoute#prefix}.'''
        result = self._values.get("prefix")
        assert result is not None, "Required property 'prefix' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def header(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppmeshRouteSpecHttp2RouteMatchHeader"]]]:
        '''header block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#header AppmeshRoute#header}
        '''
        result = self._values.get("header")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppmeshRouteSpecHttp2RouteMatchHeader"]]], result)

    @builtins.property
    def method(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#method AppmeshRoute#method}.'''
        result = self._values.get("method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scheme(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#scheme AppmeshRoute#scheme}.'''
        result = self._values.get("scheme")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecHttp2RouteMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttp2RouteMatchHeader",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "invert": "invert", "match": "match"},
)
class AppmeshRouteSpecHttp2RouteMatchHeader:
    def __init__(
        self,
        *,
        name: builtins.str,
        invert: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        match: typing.Optional[typing.Union["AppmeshRouteSpecHttp2RouteMatchHeaderMatch", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#name AppmeshRoute#name}.
        :param invert: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#invert AppmeshRoute#invert}.
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#match AppmeshRoute#match}
        '''
        if isinstance(match, dict):
            match = AppmeshRouteSpecHttp2RouteMatchHeaderMatch(**match)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2beaf0e848e50aaf4df42e71b85f2735261d1a51f147fef3324c20fb5270fe9f)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument invert", value=invert, expected_type=type_hints["invert"])
            check_type(argname="argument match", value=match, expected_type=type_hints["match"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if invert is not None:
            self._values["invert"] = invert
        if match is not None:
            self._values["match"] = match

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#name AppmeshRoute#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def invert(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#invert AppmeshRoute#invert}.'''
        result = self._values.get("invert")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def match(self) -> typing.Optional["AppmeshRouteSpecHttp2RouteMatchHeaderMatch"]:
        '''match block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#match AppmeshRoute#match}
        '''
        result = self._values.get("match")
        return typing.cast(typing.Optional["AppmeshRouteSpecHttp2RouteMatchHeaderMatch"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecHttp2RouteMatchHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshRouteSpecHttp2RouteMatchHeaderList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttp2RouteMatchHeaderList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8fd094798cfa42c31f41f2911fed3dadd0c5f0212c6a863c7848779ca79e28c4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AppmeshRouteSpecHttp2RouteMatchHeaderOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__136af7957632e4adbafeb831629647e0aadb11d10273f05ceee2ed3bec67e795)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppmeshRouteSpecHttp2RouteMatchHeaderOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8284074049b564a673928abcb6b81b25dde47cb2e5e6d636e3a95f73e434148e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__01db0d9f1773dc0c0fa579d7a04bba4e48051dbc9f160515bc586d087a310a77)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3eaa99e1445939e0a7b0ff8962f44cdf60f34e7ac8213d3855fe4151cf852668)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshRouteSpecHttp2RouteMatchHeader]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshRouteSpecHttp2RouteMatchHeader]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshRouteSpecHttp2RouteMatchHeader]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__695fe79caf6b5d5e7eb0f1cdf5eb76be1748eadba40c3c17a377f63da297bb7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttp2RouteMatchHeaderMatch",
    jsii_struct_bases=[],
    name_mapping={
        "exact": "exact",
        "prefix": "prefix",
        "range": "range",
        "regex": "regex",
        "suffix": "suffix",
    },
)
class AppmeshRouteSpecHttp2RouteMatchHeaderMatch:
    def __init__(
        self,
        *,
        exact: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        range: typing.Optional[typing.Union["AppmeshRouteSpecHttp2RouteMatchHeaderMatchRange", typing.Dict[builtins.str, typing.Any]]] = None,
        regex: typing.Optional[builtins.str] = None,
        suffix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param exact: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#exact AppmeshRoute#exact}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#prefix AppmeshRoute#prefix}.
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#range AppmeshRoute#range}
        :param regex: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#regex AppmeshRoute#regex}.
        :param suffix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#suffix AppmeshRoute#suffix}.
        '''
        if isinstance(range, dict):
            range = AppmeshRouteSpecHttp2RouteMatchHeaderMatchRange(**range)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a67d4350b1f3cbeed243d003152d020d4591979a79e0f82874a17ee7bf269d3)
            check_type(argname="argument exact", value=exact, expected_type=type_hints["exact"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument range", value=range, expected_type=type_hints["range"])
            check_type(argname="argument regex", value=regex, expected_type=type_hints["regex"])
            check_type(argname="argument suffix", value=suffix, expected_type=type_hints["suffix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if exact is not None:
            self._values["exact"] = exact
        if prefix is not None:
            self._values["prefix"] = prefix
        if range is not None:
            self._values["range"] = range
        if regex is not None:
            self._values["regex"] = regex
        if suffix is not None:
            self._values["suffix"] = suffix

    @builtins.property
    def exact(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#exact AppmeshRoute#exact}.'''
        result = self._values.get("exact")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#prefix AppmeshRoute#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def range(
        self,
    ) -> typing.Optional["AppmeshRouteSpecHttp2RouteMatchHeaderMatchRange"]:
        '''range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#range AppmeshRoute#range}
        '''
        result = self._values.get("range")
        return typing.cast(typing.Optional["AppmeshRouteSpecHttp2RouteMatchHeaderMatchRange"], result)

    @builtins.property
    def regex(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#regex AppmeshRoute#regex}.'''
        result = self._values.get("regex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def suffix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#suffix AppmeshRoute#suffix}.'''
        result = self._values.get("suffix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecHttp2RouteMatchHeaderMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshRouteSpecHttp2RouteMatchHeaderMatchOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttp2RouteMatchHeaderMatchOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__922b42fc54d355a4fa2dd89129fa3f96538ec8b313e876b54a0bf787154f58bf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRange")
    def put_range(self, *, end: jsii.Number, start: jsii.Number) -> None:
        '''
        :param end: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#end AppmeshRoute#end}.
        :param start: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#start AppmeshRoute#start}.
        '''
        value = AppmeshRouteSpecHttp2RouteMatchHeaderMatchRange(end=end, start=start)

        return typing.cast(None, jsii.invoke(self, "putRange", [value]))

    @jsii.member(jsii_name="resetExact")
    def reset_exact(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExact", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @jsii.member(jsii_name="resetRange")
    def reset_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRange", []))

    @jsii.member(jsii_name="resetRegex")
    def reset_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegex", []))

    @jsii.member(jsii_name="resetSuffix")
    def reset_suffix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuffix", []))

    @builtins.property
    @jsii.member(jsii_name="range")
    def range(self) -> "AppmeshRouteSpecHttp2RouteMatchHeaderMatchRangeOutputReference":
        return typing.cast("AppmeshRouteSpecHttp2RouteMatchHeaderMatchRangeOutputReference", jsii.get(self, "range"))

    @builtins.property
    @jsii.member(jsii_name="exactInput")
    def exact_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "exactInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="rangeInput")
    def range_input(
        self,
    ) -> typing.Optional["AppmeshRouteSpecHttp2RouteMatchHeaderMatchRange"]:
        return typing.cast(typing.Optional["AppmeshRouteSpecHttp2RouteMatchHeaderMatchRange"], jsii.get(self, "rangeInput"))

    @builtins.property
    @jsii.member(jsii_name="regexInput")
    def regex_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regexInput"))

    @builtins.property
    @jsii.member(jsii_name="suffixInput")
    def suffix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "suffixInput"))

    @builtins.property
    @jsii.member(jsii_name="exact")
    def exact(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "exact"))

    @exact.setter
    def exact(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d448d5de33989879bc9e8384d0047cb535659a85b2a441f6ef7937186fdac42)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exact", value)

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4aa34562b828b58f744061a385537640939185ca703bd7bcdb6643a410ca718d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="regex")
    def regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "regex"))

    @regex.setter
    def regex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9d263999f6521d5667d8eef31790e61916e40228e8f47cdffc4e930427e3ef3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regex", value)

    @builtins.property
    @jsii.member(jsii_name="suffix")
    def suffix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "suffix"))

    @suffix.setter
    def suffix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60934c430def92249103c1d880bc7983689feffb7fafa9ce6a9c13e9e4b39033)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "suffix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshRouteSpecHttp2RouteMatchHeaderMatch]:
        return typing.cast(typing.Optional[AppmeshRouteSpecHttp2RouteMatchHeaderMatch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshRouteSpecHttp2RouteMatchHeaderMatch],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed9dd0a1697ced419cb2460d220cc500a689a0a4ab79a9cdbcf11e12b2ec8548)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttp2RouteMatchHeaderMatchRange",
    jsii_struct_bases=[],
    name_mapping={"end": "end", "start": "start"},
)
class AppmeshRouteSpecHttp2RouteMatchHeaderMatchRange:
    def __init__(self, *, end: jsii.Number, start: jsii.Number) -> None:
        '''
        :param end: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#end AppmeshRoute#end}.
        :param start: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#start AppmeshRoute#start}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02748169b133d37a9771e66aecd016cf39d0a8d4daab6a851b784ae2dfb99ba3)
            check_type(argname="argument end", value=end, expected_type=type_hints["end"])
            check_type(argname="argument start", value=start, expected_type=type_hints["start"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "end": end,
            "start": start,
        }

    @builtins.property
    def end(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#end AppmeshRoute#end}.'''
        result = self._values.get("end")
        assert result is not None, "Required property 'end' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def start(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#start AppmeshRoute#start}.'''
        result = self._values.get("start")
        assert result is not None, "Required property 'start' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecHttp2RouteMatchHeaderMatchRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshRouteSpecHttp2RouteMatchHeaderMatchRangeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttp2RouteMatchHeaderMatchRangeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__100a88147e7d8db81ee4ccc5aea649fbf0412589194fb41558a81ea39796043f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="endInput")
    def end_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "endInput"))

    @builtins.property
    @jsii.member(jsii_name="startInput")
    def start_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "startInput"))

    @builtins.property
    @jsii.member(jsii_name="end")
    def end(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "end"))

    @end.setter
    def end(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5e66f884bf4b36c7627b04cc23c50df880e1c97952ff265a9faf5c985fccbd1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "end", value)

    @builtins.property
    @jsii.member(jsii_name="start")
    def start(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "start"))

    @start.setter
    def start(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a01e68e9f3c9ae52ea46c8542fdb06bb0aa0527431876696a40a08abf2b5030b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "start", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshRouteSpecHttp2RouteMatchHeaderMatchRange]:
        return typing.cast(typing.Optional[AppmeshRouteSpecHttp2RouteMatchHeaderMatchRange], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshRouteSpecHttp2RouteMatchHeaderMatchRange],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__603cead9912d3c9fc05836c7e776be4e88fa374941080d7b50efe500ee088afa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshRouteSpecHttp2RouteMatchHeaderOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttp2RouteMatchHeaderOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a267518b5da427620073fd230217cec902647239cc4070a4791f6d0f259e3d0b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMatch")
    def put_match(
        self,
        *,
        exact: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        range: typing.Optional[typing.Union[AppmeshRouteSpecHttp2RouteMatchHeaderMatchRange, typing.Dict[builtins.str, typing.Any]]] = None,
        regex: typing.Optional[builtins.str] = None,
        suffix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param exact: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#exact AppmeshRoute#exact}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#prefix AppmeshRoute#prefix}.
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#range AppmeshRoute#range}
        :param regex: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#regex AppmeshRoute#regex}.
        :param suffix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#suffix AppmeshRoute#suffix}.
        '''
        value = AppmeshRouteSpecHttp2RouteMatchHeaderMatch(
            exact=exact, prefix=prefix, range=range, regex=regex, suffix=suffix
        )

        return typing.cast(None, jsii.invoke(self, "putMatch", [value]))

    @jsii.member(jsii_name="resetInvert")
    def reset_invert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInvert", []))

    @jsii.member(jsii_name="resetMatch")
    def reset_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatch", []))

    @builtins.property
    @jsii.member(jsii_name="match")
    def match(self) -> AppmeshRouteSpecHttp2RouteMatchHeaderMatchOutputReference:
        return typing.cast(AppmeshRouteSpecHttp2RouteMatchHeaderMatchOutputReference, jsii.get(self, "match"))

    @builtins.property
    @jsii.member(jsii_name="invertInput")
    def invert_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "invertInput"))

    @builtins.property
    @jsii.member(jsii_name="matchInput")
    def match_input(
        self,
    ) -> typing.Optional[AppmeshRouteSpecHttp2RouteMatchHeaderMatch]:
        return typing.cast(typing.Optional[AppmeshRouteSpecHttp2RouteMatchHeaderMatch], jsii.get(self, "matchInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="invert")
    def invert(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "invert"))

    @invert.setter
    def invert(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4545e161673405ee2e2158fe7a3587de7b74d0bf2bb5b814435b77a060b63480)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "invert", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fc8b81305acdaee87a7d4f2f304f810c2505e361cce8b6a2e5eb19eae47a87e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppmeshRouteSpecHttp2RouteMatchHeader, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppmeshRouteSpecHttp2RouteMatchHeader, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppmeshRouteSpecHttp2RouteMatchHeader, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddecde5e789ff797bf73abea161fe7668aef5e05191bcb128091bb360f9ec202)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshRouteSpecHttp2RouteMatchOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttp2RouteMatchOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f0b2c4408b1c88365a9e1c0453fd13fd41a96e1e57581d2667e015766745135c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putHeader")
    def put_header(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppmeshRouteSpecHttp2RouteMatchHeader, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc8c5b3f2a9758e385d30bfa3743abd71d3b4070f1aa3c4c9ca0f5d38948f872)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHeader", [value]))

    @jsii.member(jsii_name="resetHeader")
    def reset_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeader", []))

    @jsii.member(jsii_name="resetMethod")
    def reset_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMethod", []))

    @jsii.member(jsii_name="resetScheme")
    def reset_scheme(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheme", []))

    @builtins.property
    @jsii.member(jsii_name="header")
    def header(self) -> AppmeshRouteSpecHttp2RouteMatchHeaderList:
        return typing.cast(AppmeshRouteSpecHttp2RouteMatchHeaderList, jsii.get(self, "header"))

    @builtins.property
    @jsii.member(jsii_name="headerInput")
    def header_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshRouteSpecHttp2RouteMatchHeader]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshRouteSpecHttp2RouteMatchHeader]]], jsii.get(self, "headerInput"))

    @builtins.property
    @jsii.member(jsii_name="methodInput")
    def method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "methodInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="schemeInput")
    def scheme_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemeInput"))

    @builtins.property
    @jsii.member(jsii_name="method")
    def method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "method"))

    @method.setter
    def method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96c852759f07c09eee72c811f20cecce7f1174cced5363194b7afd583c2c2fe9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "method", value)

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85235154423c3bae5aa742297b05352186e9fb8977d58ce77602901ae6eb39d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="scheme")
    def scheme(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scheme"))

    @scheme.setter
    def scheme(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad2c1a87b59767990ecf2a2f32d185f67e1c18e6ebb09fb5c322253d83917aec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheme", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshRouteSpecHttp2RouteMatch]:
        return typing.cast(typing.Optional[AppmeshRouteSpecHttp2RouteMatch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshRouteSpecHttp2RouteMatch],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca4cc450a91c77d2face5e65b9490834773296bd099521bac3cdfaf3fe8daeb0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshRouteSpecHttp2RouteOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttp2RouteOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__345d4bc70ebc842b2d8c0f1826d5f0743f3746419e07fc1d72649a622a9bcb63)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAction")
    def put_action(
        self,
        *,
        weighted_target: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppmeshRouteSpecHttp2RouteActionWeightedTarget, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param weighted_target: weighted_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#weighted_target AppmeshRoute#weighted_target}
        '''
        value = AppmeshRouteSpecHttp2RouteAction(weighted_target=weighted_target)

        return typing.cast(None, jsii.invoke(self, "putAction", [value]))

    @jsii.member(jsii_name="putMatch")
    def put_match(
        self,
        *,
        prefix: builtins.str,
        header: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppmeshRouteSpecHttp2RouteMatchHeader, typing.Dict[builtins.str, typing.Any]]]]] = None,
        method: typing.Optional[builtins.str] = None,
        scheme: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#prefix AppmeshRoute#prefix}.
        :param header: header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#header AppmeshRoute#header}
        :param method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#method AppmeshRoute#method}.
        :param scheme: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#scheme AppmeshRoute#scheme}.
        '''
        value = AppmeshRouteSpecHttp2RouteMatch(
            prefix=prefix, header=header, method=method, scheme=scheme
        )

        return typing.cast(None, jsii.invoke(self, "putMatch", [value]))

    @jsii.member(jsii_name="putRetryPolicy")
    def put_retry_policy(
        self,
        *,
        max_retries: jsii.Number,
        per_retry_timeout: typing.Union["AppmeshRouteSpecHttp2RouteRetryPolicyPerRetryTimeout", typing.Dict[builtins.str, typing.Any]],
        http_retry_events: typing.Optional[typing.Sequence[builtins.str]] = None,
        tcp_retry_events: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param max_retries: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#max_retries AppmeshRoute#max_retries}.
        :param per_retry_timeout: per_retry_timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#per_retry_timeout AppmeshRoute#per_retry_timeout}
        :param http_retry_events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#http_retry_events AppmeshRoute#http_retry_events}.
        :param tcp_retry_events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#tcp_retry_events AppmeshRoute#tcp_retry_events}.
        '''
        value = AppmeshRouteSpecHttp2RouteRetryPolicy(
            max_retries=max_retries,
            per_retry_timeout=per_retry_timeout,
            http_retry_events=http_retry_events,
            tcp_retry_events=tcp_retry_events,
        )

        return typing.cast(None, jsii.invoke(self, "putRetryPolicy", [value]))

    @jsii.member(jsii_name="putTimeout")
    def put_timeout(
        self,
        *,
        idle: typing.Optional[typing.Union["AppmeshRouteSpecHttp2RouteTimeoutIdle", typing.Dict[builtins.str, typing.Any]]] = None,
        per_request: typing.Optional[typing.Union["AppmeshRouteSpecHttp2RouteTimeoutPerRequest", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param idle: idle block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#idle AppmeshRoute#idle}
        :param per_request: per_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#per_request AppmeshRoute#per_request}
        '''
        value = AppmeshRouteSpecHttp2RouteTimeout(idle=idle, per_request=per_request)

        return typing.cast(None, jsii.invoke(self, "putTimeout", [value]))

    @jsii.member(jsii_name="resetRetryPolicy")
    def reset_retry_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetryPolicy", []))

    @jsii.member(jsii_name="resetTimeout")
    def reset_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeout", []))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> AppmeshRouteSpecHttp2RouteActionOutputReference:
        return typing.cast(AppmeshRouteSpecHttp2RouteActionOutputReference, jsii.get(self, "action"))

    @builtins.property
    @jsii.member(jsii_name="match")
    def match(self) -> AppmeshRouteSpecHttp2RouteMatchOutputReference:
        return typing.cast(AppmeshRouteSpecHttp2RouteMatchOutputReference, jsii.get(self, "match"))

    @builtins.property
    @jsii.member(jsii_name="retryPolicy")
    def retry_policy(self) -> "AppmeshRouteSpecHttp2RouteRetryPolicyOutputReference":
        return typing.cast("AppmeshRouteSpecHttp2RouteRetryPolicyOutputReference", jsii.get(self, "retryPolicy"))

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> "AppmeshRouteSpecHttp2RouteTimeoutOutputReference":
        return typing.cast("AppmeshRouteSpecHttp2RouteTimeoutOutputReference", jsii.get(self, "timeout"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[AppmeshRouteSpecHttp2RouteAction]:
        return typing.cast(typing.Optional[AppmeshRouteSpecHttp2RouteAction], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="matchInput")
    def match_input(self) -> typing.Optional[AppmeshRouteSpecHttp2RouteMatch]:
        return typing.cast(typing.Optional[AppmeshRouteSpecHttp2RouteMatch], jsii.get(self, "matchInput"))

    @builtins.property
    @jsii.member(jsii_name="retryPolicyInput")
    def retry_policy_input(
        self,
    ) -> typing.Optional["AppmeshRouteSpecHttp2RouteRetryPolicy"]:
        return typing.cast(typing.Optional["AppmeshRouteSpecHttp2RouteRetryPolicy"], jsii.get(self, "retryPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(self) -> typing.Optional["AppmeshRouteSpecHttp2RouteTimeout"]:
        return typing.cast(typing.Optional["AppmeshRouteSpecHttp2RouteTimeout"], jsii.get(self, "timeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshRouteSpecHttp2Route]:
        return typing.cast(typing.Optional[AppmeshRouteSpecHttp2Route], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshRouteSpecHttp2Route],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9398555ce9ed23de9f9f95611fb283f48a2107e79529b95e82210e39518e1eaa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttp2RouteRetryPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "max_retries": "maxRetries",
        "per_retry_timeout": "perRetryTimeout",
        "http_retry_events": "httpRetryEvents",
        "tcp_retry_events": "tcpRetryEvents",
    },
)
class AppmeshRouteSpecHttp2RouteRetryPolicy:
    def __init__(
        self,
        *,
        max_retries: jsii.Number,
        per_retry_timeout: typing.Union["AppmeshRouteSpecHttp2RouteRetryPolicyPerRetryTimeout", typing.Dict[builtins.str, typing.Any]],
        http_retry_events: typing.Optional[typing.Sequence[builtins.str]] = None,
        tcp_retry_events: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param max_retries: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#max_retries AppmeshRoute#max_retries}.
        :param per_retry_timeout: per_retry_timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#per_retry_timeout AppmeshRoute#per_retry_timeout}
        :param http_retry_events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#http_retry_events AppmeshRoute#http_retry_events}.
        :param tcp_retry_events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#tcp_retry_events AppmeshRoute#tcp_retry_events}.
        '''
        if isinstance(per_retry_timeout, dict):
            per_retry_timeout = AppmeshRouteSpecHttp2RouteRetryPolicyPerRetryTimeout(**per_retry_timeout)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e04c19daa1fcd01e4f60111b47cb1be9c88ef354a7b1497983a79163be54ccc)
            check_type(argname="argument max_retries", value=max_retries, expected_type=type_hints["max_retries"])
            check_type(argname="argument per_retry_timeout", value=per_retry_timeout, expected_type=type_hints["per_retry_timeout"])
            check_type(argname="argument http_retry_events", value=http_retry_events, expected_type=type_hints["http_retry_events"])
            check_type(argname="argument tcp_retry_events", value=tcp_retry_events, expected_type=type_hints["tcp_retry_events"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "max_retries": max_retries,
            "per_retry_timeout": per_retry_timeout,
        }
        if http_retry_events is not None:
            self._values["http_retry_events"] = http_retry_events
        if tcp_retry_events is not None:
            self._values["tcp_retry_events"] = tcp_retry_events

    @builtins.property
    def max_retries(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#max_retries AppmeshRoute#max_retries}.'''
        result = self._values.get("max_retries")
        assert result is not None, "Required property 'max_retries' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def per_retry_timeout(
        self,
    ) -> "AppmeshRouteSpecHttp2RouteRetryPolicyPerRetryTimeout":
        '''per_retry_timeout block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#per_retry_timeout AppmeshRoute#per_retry_timeout}
        '''
        result = self._values.get("per_retry_timeout")
        assert result is not None, "Required property 'per_retry_timeout' is missing"
        return typing.cast("AppmeshRouteSpecHttp2RouteRetryPolicyPerRetryTimeout", result)

    @builtins.property
    def http_retry_events(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#http_retry_events AppmeshRoute#http_retry_events}.'''
        result = self._values.get("http_retry_events")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tcp_retry_events(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#tcp_retry_events AppmeshRoute#tcp_retry_events}.'''
        result = self._values.get("tcp_retry_events")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecHttp2RouteRetryPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshRouteSpecHttp2RouteRetryPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttp2RouteRetryPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7f96ce08da5a81b1686dc979947fcce837a2a25158489aee8fa8d2e67496d404)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPerRetryTimeout")
    def put_per_retry_timeout(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#unit AppmeshRoute#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#value AppmeshRoute#value}.
        '''
        value_ = AppmeshRouteSpecHttp2RouteRetryPolicyPerRetryTimeout(
            unit=unit, value=value
        )

        return typing.cast(None, jsii.invoke(self, "putPerRetryTimeout", [value_]))

    @jsii.member(jsii_name="resetHttpRetryEvents")
    def reset_http_retry_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpRetryEvents", []))

    @jsii.member(jsii_name="resetTcpRetryEvents")
    def reset_tcp_retry_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTcpRetryEvents", []))

    @builtins.property
    @jsii.member(jsii_name="perRetryTimeout")
    def per_retry_timeout(
        self,
    ) -> "AppmeshRouteSpecHttp2RouteRetryPolicyPerRetryTimeoutOutputReference":
        return typing.cast("AppmeshRouteSpecHttp2RouteRetryPolicyPerRetryTimeoutOutputReference", jsii.get(self, "perRetryTimeout"))

    @builtins.property
    @jsii.member(jsii_name="httpRetryEventsInput")
    def http_retry_events_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "httpRetryEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxRetriesInput")
    def max_retries_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxRetriesInput"))

    @builtins.property
    @jsii.member(jsii_name="perRetryTimeoutInput")
    def per_retry_timeout_input(
        self,
    ) -> typing.Optional["AppmeshRouteSpecHttp2RouteRetryPolicyPerRetryTimeout"]:
        return typing.cast(typing.Optional["AppmeshRouteSpecHttp2RouteRetryPolicyPerRetryTimeout"], jsii.get(self, "perRetryTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="tcpRetryEventsInput")
    def tcp_retry_events_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tcpRetryEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="httpRetryEvents")
    def http_retry_events(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "httpRetryEvents"))

    @http_retry_events.setter
    def http_retry_events(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c18944586ed94bfccacbfa5d5d1cc5b3193c190591f7ddc69e161988b91ab593)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpRetryEvents", value)

    @builtins.property
    @jsii.member(jsii_name="maxRetries")
    def max_retries(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxRetries"))

    @max_retries.setter
    def max_retries(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f58530461ea6b9e2e3af164e0dac77008a32e89b1a0c5d9627cc9990cd7e31f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxRetries", value)

    @builtins.property
    @jsii.member(jsii_name="tcpRetryEvents")
    def tcp_retry_events(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tcpRetryEvents"))

    @tcp_retry_events.setter
    def tcp_retry_events(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7db79f0804e97326d555b29cd9643db39cc504f9b402df11af6632798ddf4d5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tcpRetryEvents", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshRouteSpecHttp2RouteRetryPolicy]:
        return typing.cast(typing.Optional[AppmeshRouteSpecHttp2RouteRetryPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshRouteSpecHttp2RouteRetryPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bde774d9b437b8ddd94522ac73408c790b21c98dfbf816598dfcc263fbf85df2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttp2RouteRetryPolicyPerRetryTimeout",
    jsii_struct_bases=[],
    name_mapping={"unit": "unit", "value": "value"},
)
class AppmeshRouteSpecHttp2RouteRetryPolicyPerRetryTimeout:
    def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#unit AppmeshRoute#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#value AppmeshRoute#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a33c40c6893965a22e11b634eb3644d7d6b92944214672e9b36c40d9077600b2)
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "unit": unit,
            "value": value,
        }

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#unit AppmeshRoute#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#value AppmeshRoute#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecHttp2RouteRetryPolicyPerRetryTimeout(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshRouteSpecHttp2RouteRetryPolicyPerRetryTimeoutOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttp2RouteRetryPolicyPerRetryTimeoutOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__eea31d6634a3c132c65aa4c33d4eba3ce87c879e6ef900da7481f218ed3afd16)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5ee8bc7cfb97bedfd8ca0f2665ce3a8777d4abf5a8d5615257d050b11282d2b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__264cd7ea83840edd4469e63951fde07b8604826500450630933d2b601c3842f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshRouteSpecHttp2RouteRetryPolicyPerRetryTimeout]:
        return typing.cast(typing.Optional[AppmeshRouteSpecHttp2RouteRetryPolicyPerRetryTimeout], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshRouteSpecHttp2RouteRetryPolicyPerRetryTimeout],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f536d908ced8922f8e688a0ade9b5f819cd690b0af3d1ff448a482dac57b2ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttp2RouteTimeout",
    jsii_struct_bases=[],
    name_mapping={"idle": "idle", "per_request": "perRequest"},
)
class AppmeshRouteSpecHttp2RouteTimeout:
    def __init__(
        self,
        *,
        idle: typing.Optional[typing.Union["AppmeshRouteSpecHttp2RouteTimeoutIdle", typing.Dict[builtins.str, typing.Any]]] = None,
        per_request: typing.Optional[typing.Union["AppmeshRouteSpecHttp2RouteTimeoutPerRequest", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param idle: idle block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#idle AppmeshRoute#idle}
        :param per_request: per_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#per_request AppmeshRoute#per_request}
        '''
        if isinstance(idle, dict):
            idle = AppmeshRouteSpecHttp2RouteTimeoutIdle(**idle)
        if isinstance(per_request, dict):
            per_request = AppmeshRouteSpecHttp2RouteTimeoutPerRequest(**per_request)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b1979de7654603ec4f36af44cc2759c36b36d939b0a3e6d8ce940e7ecb22da2)
            check_type(argname="argument idle", value=idle, expected_type=type_hints["idle"])
            check_type(argname="argument per_request", value=per_request, expected_type=type_hints["per_request"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if idle is not None:
            self._values["idle"] = idle
        if per_request is not None:
            self._values["per_request"] = per_request

    @builtins.property
    def idle(self) -> typing.Optional["AppmeshRouteSpecHttp2RouteTimeoutIdle"]:
        '''idle block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#idle AppmeshRoute#idle}
        '''
        result = self._values.get("idle")
        return typing.cast(typing.Optional["AppmeshRouteSpecHttp2RouteTimeoutIdle"], result)

    @builtins.property
    def per_request(
        self,
    ) -> typing.Optional["AppmeshRouteSpecHttp2RouteTimeoutPerRequest"]:
        '''per_request block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#per_request AppmeshRoute#per_request}
        '''
        result = self._values.get("per_request")
        return typing.cast(typing.Optional["AppmeshRouteSpecHttp2RouteTimeoutPerRequest"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecHttp2RouteTimeout(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttp2RouteTimeoutIdle",
    jsii_struct_bases=[],
    name_mapping={"unit": "unit", "value": "value"},
)
class AppmeshRouteSpecHttp2RouteTimeoutIdle:
    def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#unit AppmeshRoute#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#value AppmeshRoute#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d3da9f62992da5fe9d4d29f3d5565f190ed68e7a65b215692b205a8ee23aea7)
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "unit": unit,
            "value": value,
        }

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#unit AppmeshRoute#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#value AppmeshRoute#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecHttp2RouteTimeoutIdle(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshRouteSpecHttp2RouteTimeoutIdleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttp2RouteTimeoutIdleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__11877cbc3aeab63a70e092e39af826b9830eae1624e6d5eeb7f32f289e760e64)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e79b8994b99f7ac79433b6ba62a39692828e6f395638ea4865ee8f2c45bd5bda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74f7fbdc6671182bed1677f6a08c1c79cd6bde0a7eddce2d8976b8548329cf56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshRouteSpecHttp2RouteTimeoutIdle]:
        return typing.cast(typing.Optional[AppmeshRouteSpecHttp2RouteTimeoutIdle], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshRouteSpecHttp2RouteTimeoutIdle],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30d795b8a4ea2b685a1bfc3cd621ed2b5d15959078fe38c74c98a66c355e5875)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshRouteSpecHttp2RouteTimeoutOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttp2RouteTimeoutOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a63630c2b4fd81c834b912482b3720cdc93e9a4d2fead11d9cd39aa04ab88a0b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putIdle")
    def put_idle(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#unit AppmeshRoute#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#value AppmeshRoute#value}.
        '''
        value_ = AppmeshRouteSpecHttp2RouteTimeoutIdle(unit=unit, value=value)

        return typing.cast(None, jsii.invoke(self, "putIdle", [value_]))

    @jsii.member(jsii_name="putPerRequest")
    def put_per_request(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#unit AppmeshRoute#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#value AppmeshRoute#value}.
        '''
        value_ = AppmeshRouteSpecHttp2RouteTimeoutPerRequest(unit=unit, value=value)

        return typing.cast(None, jsii.invoke(self, "putPerRequest", [value_]))

    @jsii.member(jsii_name="resetIdle")
    def reset_idle(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdle", []))

    @jsii.member(jsii_name="resetPerRequest")
    def reset_per_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPerRequest", []))

    @builtins.property
    @jsii.member(jsii_name="idle")
    def idle(self) -> AppmeshRouteSpecHttp2RouteTimeoutIdleOutputReference:
        return typing.cast(AppmeshRouteSpecHttp2RouteTimeoutIdleOutputReference, jsii.get(self, "idle"))

    @builtins.property
    @jsii.member(jsii_name="perRequest")
    def per_request(
        self,
    ) -> "AppmeshRouteSpecHttp2RouteTimeoutPerRequestOutputReference":
        return typing.cast("AppmeshRouteSpecHttp2RouteTimeoutPerRequestOutputReference", jsii.get(self, "perRequest"))

    @builtins.property
    @jsii.member(jsii_name="idleInput")
    def idle_input(self) -> typing.Optional[AppmeshRouteSpecHttp2RouteTimeoutIdle]:
        return typing.cast(typing.Optional[AppmeshRouteSpecHttp2RouteTimeoutIdle], jsii.get(self, "idleInput"))

    @builtins.property
    @jsii.member(jsii_name="perRequestInput")
    def per_request_input(
        self,
    ) -> typing.Optional["AppmeshRouteSpecHttp2RouteTimeoutPerRequest"]:
        return typing.cast(typing.Optional["AppmeshRouteSpecHttp2RouteTimeoutPerRequest"], jsii.get(self, "perRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshRouteSpecHttp2RouteTimeout]:
        return typing.cast(typing.Optional[AppmeshRouteSpecHttp2RouteTimeout], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshRouteSpecHttp2RouteTimeout],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6df5e1ada9f6b5e53c99fc8e1c71fe08fdb44b27af73c1b267b6957ee7c4e0b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttp2RouteTimeoutPerRequest",
    jsii_struct_bases=[],
    name_mapping={"unit": "unit", "value": "value"},
)
class AppmeshRouteSpecHttp2RouteTimeoutPerRequest:
    def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#unit AppmeshRoute#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#value AppmeshRoute#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d125492cd842c611c1deac99630cb4da0c7e6b11f376a7f7ec87f8c19fe5367)
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "unit": unit,
            "value": value,
        }

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#unit AppmeshRoute#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#value AppmeshRoute#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecHttp2RouteTimeoutPerRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshRouteSpecHttp2RouteTimeoutPerRequestOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttp2RouteTimeoutPerRequestOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a282e21af3a1b8e6d588855fa8ad6237e19a6b8e8a40178e3ade5f5c9d30126a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d518750a2c92c77320765c6be0c350a74953765f391deab6a7a35d6989626ab3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__401ce784406dd2825a4b7a7f6c8bd4c46830bcd7d6d60153b82060527bce0ab9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshRouteSpecHttp2RouteTimeoutPerRequest]:
        return typing.cast(typing.Optional[AppmeshRouteSpecHttp2RouteTimeoutPerRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshRouteSpecHttp2RouteTimeoutPerRequest],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ea72610c8888c31b7ab3d90cf0d9124d87bd75af72529590c2f7daff2b33220)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttpRoute",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "match": "match",
        "retry_policy": "retryPolicy",
        "timeout": "timeout",
    },
)
class AppmeshRouteSpecHttpRoute:
    def __init__(
        self,
        *,
        action: typing.Union["AppmeshRouteSpecHttpRouteAction", typing.Dict[builtins.str, typing.Any]],
        match: typing.Union["AppmeshRouteSpecHttpRouteMatch", typing.Dict[builtins.str, typing.Any]],
        retry_policy: typing.Optional[typing.Union["AppmeshRouteSpecHttpRouteRetryPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        timeout: typing.Optional[typing.Union["AppmeshRouteSpecHttpRouteTimeout", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#action AppmeshRoute#action}
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#match AppmeshRoute#match}
        :param retry_policy: retry_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#retry_policy AppmeshRoute#retry_policy}
        :param timeout: timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#timeout AppmeshRoute#timeout}
        '''
        if isinstance(action, dict):
            action = AppmeshRouteSpecHttpRouteAction(**action)
        if isinstance(match, dict):
            match = AppmeshRouteSpecHttpRouteMatch(**match)
        if isinstance(retry_policy, dict):
            retry_policy = AppmeshRouteSpecHttpRouteRetryPolicy(**retry_policy)
        if isinstance(timeout, dict):
            timeout = AppmeshRouteSpecHttpRouteTimeout(**timeout)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57c5deaf8893249698efef0884d803b84d59f5e4a5212d5bfa829ecfc2d78e7f)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument match", value=match, expected_type=type_hints["match"])
            check_type(argname="argument retry_policy", value=retry_policy, expected_type=type_hints["retry_policy"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action": action,
            "match": match,
        }
        if retry_policy is not None:
            self._values["retry_policy"] = retry_policy
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def action(self) -> "AppmeshRouteSpecHttpRouteAction":
        '''action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#action AppmeshRoute#action}
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast("AppmeshRouteSpecHttpRouteAction", result)

    @builtins.property
    def match(self) -> "AppmeshRouteSpecHttpRouteMatch":
        '''match block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#match AppmeshRoute#match}
        '''
        result = self._values.get("match")
        assert result is not None, "Required property 'match' is missing"
        return typing.cast("AppmeshRouteSpecHttpRouteMatch", result)

    @builtins.property
    def retry_policy(self) -> typing.Optional["AppmeshRouteSpecHttpRouteRetryPolicy"]:
        '''retry_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#retry_policy AppmeshRoute#retry_policy}
        '''
        result = self._values.get("retry_policy")
        return typing.cast(typing.Optional["AppmeshRouteSpecHttpRouteRetryPolicy"], result)

    @builtins.property
    def timeout(self) -> typing.Optional["AppmeshRouteSpecHttpRouteTimeout"]:
        '''timeout block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#timeout AppmeshRoute#timeout}
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional["AppmeshRouteSpecHttpRouteTimeout"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecHttpRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttpRouteAction",
    jsii_struct_bases=[],
    name_mapping={"weighted_target": "weightedTarget"},
)
class AppmeshRouteSpecHttpRouteAction:
    def __init__(
        self,
        *,
        weighted_target: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AppmeshRouteSpecHttpRouteActionWeightedTarget", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param weighted_target: weighted_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#weighted_target AppmeshRoute#weighted_target}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__386bf668701dbeed7885549600619a906926097d94d54d63e0f1b138f280272b)
            check_type(argname="argument weighted_target", value=weighted_target, expected_type=type_hints["weighted_target"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "weighted_target": weighted_target,
        }

    @builtins.property
    def weighted_target(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppmeshRouteSpecHttpRouteActionWeightedTarget"]]:
        '''weighted_target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#weighted_target AppmeshRoute#weighted_target}
        '''
        result = self._values.get("weighted_target")
        assert result is not None, "Required property 'weighted_target' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppmeshRouteSpecHttpRouteActionWeightedTarget"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecHttpRouteAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshRouteSpecHttpRouteActionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttpRouteActionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7056d7469d158d8bb3d0324347b468aaad6fcac78c91d078799bd59fa7f92b84)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putWeightedTarget")
    def put_weighted_target(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AppmeshRouteSpecHttpRouteActionWeightedTarget", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a66678ec01eed5f77a957e2ce21404282a6c06d8779329a3650231181dd79a7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWeightedTarget", [value]))

    @builtins.property
    @jsii.member(jsii_name="weightedTarget")
    def weighted_target(self) -> "AppmeshRouteSpecHttpRouteActionWeightedTargetList":
        return typing.cast("AppmeshRouteSpecHttpRouteActionWeightedTargetList", jsii.get(self, "weightedTarget"))

    @builtins.property
    @jsii.member(jsii_name="weightedTargetInput")
    def weighted_target_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppmeshRouteSpecHttpRouteActionWeightedTarget"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppmeshRouteSpecHttpRouteActionWeightedTarget"]]], jsii.get(self, "weightedTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshRouteSpecHttpRouteAction]:
        return typing.cast(typing.Optional[AppmeshRouteSpecHttpRouteAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshRouteSpecHttpRouteAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a52d7bdbd48ee476495c5491dabe13d67d193354ab35a3a4c424695ff552f9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttpRouteActionWeightedTarget",
    jsii_struct_bases=[],
    name_mapping={"virtual_node": "virtualNode", "weight": "weight"},
)
class AppmeshRouteSpecHttpRouteActionWeightedTarget:
    def __init__(self, *, virtual_node: builtins.str, weight: jsii.Number) -> None:
        '''
        :param virtual_node: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#virtual_node AppmeshRoute#virtual_node}.
        :param weight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#weight AppmeshRoute#weight}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9cf40cab211901068af6a01ec7f2304f5a8d50d6e3602575558ef92520450b7)
            check_type(argname="argument virtual_node", value=virtual_node, expected_type=type_hints["virtual_node"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "virtual_node": virtual_node,
            "weight": weight,
        }

    @builtins.property
    def virtual_node(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#virtual_node AppmeshRoute#virtual_node}.'''
        result = self._values.get("virtual_node")
        assert result is not None, "Required property 'virtual_node' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def weight(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#weight AppmeshRoute#weight}.'''
        result = self._values.get("weight")
        assert result is not None, "Required property 'weight' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecHttpRouteActionWeightedTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshRouteSpecHttpRouteActionWeightedTargetList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttpRouteActionWeightedTargetList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__663fb27fc4881bb6392a30c0a8d9c20745e221e9d7711111bc84ff350f460cef)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AppmeshRouteSpecHttpRouteActionWeightedTargetOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__078a9b2363dc66bbb2a7d1eb3288df61ccd488d3fd624576df376abb73e815a1)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppmeshRouteSpecHttpRouteActionWeightedTargetOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__778b1fcc221cf85e365755fb57b67877ee4f329cc4163771a8d41504dde6c0bd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9b8b6ca11f92cb5d519c9068f8dde1d022dd4c07de6b5336e897115d15c7573f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9899fd205b409d2506a7f8a4e2d8d83ecc8e78d8ce72005d1f2e5b3cadd28711)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshRouteSpecHttpRouteActionWeightedTarget]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshRouteSpecHttpRouteActionWeightedTarget]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshRouteSpecHttpRouteActionWeightedTarget]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c42ff9edc44103a2b96dca27ab17d4ab314641d84dfbf9c6f25c7912ccc45b87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshRouteSpecHttpRouteActionWeightedTargetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttpRouteActionWeightedTargetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ecc792eb5a42fdfe87449e91eb8e57ceaef1147d6e06b99563b2304227ac103b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="virtualNodeInput")
    def virtual_node_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualNodeInput"))

    @builtins.property
    @jsii.member(jsii_name="weightInput")
    def weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNode")
    def virtual_node(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualNode"))

    @virtual_node.setter
    def virtual_node(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e94f232fdffa90647054297ee21c1cb81c2888f7398f1fc5553a2806dc7c43e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualNode", value)

    @builtins.property
    @jsii.member(jsii_name="weight")
    def weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weight"))

    @weight.setter
    def weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3609f6963e77ba9987ade322f589070be6c17470374fa695daf0f516ae0bf686)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weight", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppmeshRouteSpecHttpRouteActionWeightedTarget, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppmeshRouteSpecHttpRouteActionWeightedTarget, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppmeshRouteSpecHttpRouteActionWeightedTarget, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b3d12f16d3e11c24c493a7fffebae86b2b4c526a5f741f8e3aa91d314665127)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttpRouteMatch",
    jsii_struct_bases=[],
    name_mapping={
        "prefix": "prefix",
        "header": "header",
        "method": "method",
        "scheme": "scheme",
    },
)
class AppmeshRouteSpecHttpRouteMatch:
    def __init__(
        self,
        *,
        prefix: builtins.str,
        header: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AppmeshRouteSpecHttpRouteMatchHeader", typing.Dict[builtins.str, typing.Any]]]]] = None,
        method: typing.Optional[builtins.str] = None,
        scheme: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#prefix AppmeshRoute#prefix}.
        :param header: header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#header AppmeshRoute#header}
        :param method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#method AppmeshRoute#method}.
        :param scheme: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#scheme AppmeshRoute#scheme}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02694482fb69ad07b28eee14219c70b0eca262df73e17fd18a16a6f62a2aea33)
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument header", value=header, expected_type=type_hints["header"])
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument scheme", value=scheme, expected_type=type_hints["scheme"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "prefix": prefix,
        }
        if header is not None:
            self._values["header"] = header
        if method is not None:
            self._values["method"] = method
        if scheme is not None:
            self._values["scheme"] = scheme

    @builtins.property
    def prefix(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#prefix AppmeshRoute#prefix}.'''
        result = self._values.get("prefix")
        assert result is not None, "Required property 'prefix' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def header(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppmeshRouteSpecHttpRouteMatchHeader"]]]:
        '''header block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#header AppmeshRoute#header}
        '''
        result = self._values.get("header")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppmeshRouteSpecHttpRouteMatchHeader"]]], result)

    @builtins.property
    def method(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#method AppmeshRoute#method}.'''
        result = self._values.get("method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scheme(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#scheme AppmeshRoute#scheme}.'''
        result = self._values.get("scheme")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecHttpRouteMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttpRouteMatchHeader",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "invert": "invert", "match": "match"},
)
class AppmeshRouteSpecHttpRouteMatchHeader:
    def __init__(
        self,
        *,
        name: builtins.str,
        invert: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        match: typing.Optional[typing.Union["AppmeshRouteSpecHttpRouteMatchHeaderMatch", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#name AppmeshRoute#name}.
        :param invert: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#invert AppmeshRoute#invert}.
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#match AppmeshRoute#match}
        '''
        if isinstance(match, dict):
            match = AppmeshRouteSpecHttpRouteMatchHeaderMatch(**match)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__082b351fe6ae029a75a33a1a54a0a20004a48a8b4897bd3cde3d6e14750e81be)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument invert", value=invert, expected_type=type_hints["invert"])
            check_type(argname="argument match", value=match, expected_type=type_hints["match"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if invert is not None:
            self._values["invert"] = invert
        if match is not None:
            self._values["match"] = match

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#name AppmeshRoute#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def invert(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#invert AppmeshRoute#invert}.'''
        result = self._values.get("invert")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def match(self) -> typing.Optional["AppmeshRouteSpecHttpRouteMatchHeaderMatch"]:
        '''match block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#match AppmeshRoute#match}
        '''
        result = self._values.get("match")
        return typing.cast(typing.Optional["AppmeshRouteSpecHttpRouteMatchHeaderMatch"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecHttpRouteMatchHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshRouteSpecHttpRouteMatchHeaderList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttpRouteMatchHeaderList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1511daccd74db7420ff36e811ffec3204d66482e3a8bfe9c78112b5826fc2266)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AppmeshRouteSpecHttpRouteMatchHeaderOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f2fa707e5839bc514bb225a44c3dc1a9210e7cc3ca3cec63901808eceb0ae9d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppmeshRouteSpecHttpRouteMatchHeaderOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9391fb7f93da1636c8117173cdbaeff37a560925d7b0606d5fc8d6ff77dade0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2475a8231cccf9f83109e7e9288b8619a4d83f5a6f7d76ee8941bfe569ed99cf)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1712477c9f3580a8fa7a56fff323f7501cc10087234742120fd6b9667f170f45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshRouteSpecHttpRouteMatchHeader]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshRouteSpecHttpRouteMatchHeader]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshRouteSpecHttpRouteMatchHeader]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab8b4271861118bb4bee80aef9db1bea618e9eca3577d639514604f1d163295f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttpRouteMatchHeaderMatch",
    jsii_struct_bases=[],
    name_mapping={
        "exact": "exact",
        "prefix": "prefix",
        "range": "range",
        "regex": "regex",
        "suffix": "suffix",
    },
)
class AppmeshRouteSpecHttpRouteMatchHeaderMatch:
    def __init__(
        self,
        *,
        exact: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        range: typing.Optional[typing.Union["AppmeshRouteSpecHttpRouteMatchHeaderMatchRange", typing.Dict[builtins.str, typing.Any]]] = None,
        regex: typing.Optional[builtins.str] = None,
        suffix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param exact: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#exact AppmeshRoute#exact}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#prefix AppmeshRoute#prefix}.
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#range AppmeshRoute#range}
        :param regex: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#regex AppmeshRoute#regex}.
        :param suffix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#suffix AppmeshRoute#suffix}.
        '''
        if isinstance(range, dict):
            range = AppmeshRouteSpecHttpRouteMatchHeaderMatchRange(**range)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf6a6906cd192558b397f54208f407dd80a4906e35b3304bc929634f8b42464f)
            check_type(argname="argument exact", value=exact, expected_type=type_hints["exact"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument range", value=range, expected_type=type_hints["range"])
            check_type(argname="argument regex", value=regex, expected_type=type_hints["regex"])
            check_type(argname="argument suffix", value=suffix, expected_type=type_hints["suffix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if exact is not None:
            self._values["exact"] = exact
        if prefix is not None:
            self._values["prefix"] = prefix
        if range is not None:
            self._values["range"] = range
        if regex is not None:
            self._values["regex"] = regex
        if suffix is not None:
            self._values["suffix"] = suffix

    @builtins.property
    def exact(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#exact AppmeshRoute#exact}.'''
        result = self._values.get("exact")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#prefix AppmeshRoute#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def range(
        self,
    ) -> typing.Optional["AppmeshRouteSpecHttpRouteMatchHeaderMatchRange"]:
        '''range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#range AppmeshRoute#range}
        '''
        result = self._values.get("range")
        return typing.cast(typing.Optional["AppmeshRouteSpecHttpRouteMatchHeaderMatchRange"], result)

    @builtins.property
    def regex(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#regex AppmeshRoute#regex}.'''
        result = self._values.get("regex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def suffix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#suffix AppmeshRoute#suffix}.'''
        result = self._values.get("suffix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecHttpRouteMatchHeaderMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshRouteSpecHttpRouteMatchHeaderMatchOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttpRouteMatchHeaderMatchOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__06d5f9c3e446208714594f484e8563ec24f8bcaf467d9eca1d2aef568d919f73)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRange")
    def put_range(self, *, end: jsii.Number, start: jsii.Number) -> None:
        '''
        :param end: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#end AppmeshRoute#end}.
        :param start: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#start AppmeshRoute#start}.
        '''
        value = AppmeshRouteSpecHttpRouteMatchHeaderMatchRange(end=end, start=start)

        return typing.cast(None, jsii.invoke(self, "putRange", [value]))

    @jsii.member(jsii_name="resetExact")
    def reset_exact(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExact", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @jsii.member(jsii_name="resetRange")
    def reset_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRange", []))

    @jsii.member(jsii_name="resetRegex")
    def reset_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegex", []))

    @jsii.member(jsii_name="resetSuffix")
    def reset_suffix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuffix", []))

    @builtins.property
    @jsii.member(jsii_name="range")
    def range(self) -> "AppmeshRouteSpecHttpRouteMatchHeaderMatchRangeOutputReference":
        return typing.cast("AppmeshRouteSpecHttpRouteMatchHeaderMatchRangeOutputReference", jsii.get(self, "range"))

    @builtins.property
    @jsii.member(jsii_name="exactInput")
    def exact_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "exactInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="rangeInput")
    def range_input(
        self,
    ) -> typing.Optional["AppmeshRouteSpecHttpRouteMatchHeaderMatchRange"]:
        return typing.cast(typing.Optional["AppmeshRouteSpecHttpRouteMatchHeaderMatchRange"], jsii.get(self, "rangeInput"))

    @builtins.property
    @jsii.member(jsii_name="regexInput")
    def regex_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regexInput"))

    @builtins.property
    @jsii.member(jsii_name="suffixInput")
    def suffix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "suffixInput"))

    @builtins.property
    @jsii.member(jsii_name="exact")
    def exact(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "exact"))

    @exact.setter
    def exact(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0560e26cfa629c000242d6b00adca5eea6d5b28a423811257452574f78a65d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exact", value)

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b048bf8a59aa5e95e20b4006b0871018deb7d0d1b2256fc7d6ef7fb1246fd9a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="regex")
    def regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "regex"))

    @regex.setter
    def regex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c62a6c487db716070f7b75d104abc16cf7d534da2a07522322346c6566ab35a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regex", value)

    @builtins.property
    @jsii.member(jsii_name="suffix")
    def suffix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "suffix"))

    @suffix.setter
    def suffix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__163a33615a76b62710045f3539f6ac447a85e4cb92cfe35405e3f7e930df4ce0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "suffix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshRouteSpecHttpRouteMatchHeaderMatch]:
        return typing.cast(typing.Optional[AppmeshRouteSpecHttpRouteMatchHeaderMatch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshRouteSpecHttpRouteMatchHeaderMatch],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06fb8202e4a14d5d49d07e763062981e9f42b69b2d4308e955fda7dbb25c9980)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttpRouteMatchHeaderMatchRange",
    jsii_struct_bases=[],
    name_mapping={"end": "end", "start": "start"},
)
class AppmeshRouteSpecHttpRouteMatchHeaderMatchRange:
    def __init__(self, *, end: jsii.Number, start: jsii.Number) -> None:
        '''
        :param end: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#end AppmeshRoute#end}.
        :param start: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#start AppmeshRoute#start}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05513f2281c9ddefe53cf527c0d489be227b67cc76a4fadff7286e3bfe010fce)
            check_type(argname="argument end", value=end, expected_type=type_hints["end"])
            check_type(argname="argument start", value=start, expected_type=type_hints["start"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "end": end,
            "start": start,
        }

    @builtins.property
    def end(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#end AppmeshRoute#end}.'''
        result = self._values.get("end")
        assert result is not None, "Required property 'end' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def start(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#start AppmeshRoute#start}.'''
        result = self._values.get("start")
        assert result is not None, "Required property 'start' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecHttpRouteMatchHeaderMatchRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshRouteSpecHttpRouteMatchHeaderMatchRangeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttpRouteMatchHeaderMatchRangeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ac36e231361cf417adf8160363e93ddf670b3bd8c16f282d44ae8d8848154913)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="endInput")
    def end_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "endInput"))

    @builtins.property
    @jsii.member(jsii_name="startInput")
    def start_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "startInput"))

    @builtins.property
    @jsii.member(jsii_name="end")
    def end(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "end"))

    @end.setter
    def end(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e529fee44e952d54ab10c9e21c4231d6b46784defae60787bfb86e47e3826e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "end", value)

    @builtins.property
    @jsii.member(jsii_name="start")
    def start(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "start"))

    @start.setter
    def start(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__baf997212d089bb90e3e03750d99664535cefbf39439fa00aaf422215ba5cc96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "start", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshRouteSpecHttpRouteMatchHeaderMatchRange]:
        return typing.cast(typing.Optional[AppmeshRouteSpecHttpRouteMatchHeaderMatchRange], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshRouteSpecHttpRouteMatchHeaderMatchRange],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a1e84956a8a10d075445a16e85781aecdbc047771a21500bc82e30eef206b69)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshRouteSpecHttpRouteMatchHeaderOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttpRouteMatchHeaderOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2e23caed84012533c0126c487ae9da3b937753fc456c3f4db9ee1dcbcbc80f05)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMatch")
    def put_match(
        self,
        *,
        exact: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        range: typing.Optional[typing.Union[AppmeshRouteSpecHttpRouteMatchHeaderMatchRange, typing.Dict[builtins.str, typing.Any]]] = None,
        regex: typing.Optional[builtins.str] = None,
        suffix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param exact: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#exact AppmeshRoute#exact}.
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#prefix AppmeshRoute#prefix}.
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#range AppmeshRoute#range}
        :param regex: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#regex AppmeshRoute#regex}.
        :param suffix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#suffix AppmeshRoute#suffix}.
        '''
        value = AppmeshRouteSpecHttpRouteMatchHeaderMatch(
            exact=exact, prefix=prefix, range=range, regex=regex, suffix=suffix
        )

        return typing.cast(None, jsii.invoke(self, "putMatch", [value]))

    @jsii.member(jsii_name="resetInvert")
    def reset_invert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInvert", []))

    @jsii.member(jsii_name="resetMatch")
    def reset_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatch", []))

    @builtins.property
    @jsii.member(jsii_name="match")
    def match(self) -> AppmeshRouteSpecHttpRouteMatchHeaderMatchOutputReference:
        return typing.cast(AppmeshRouteSpecHttpRouteMatchHeaderMatchOutputReference, jsii.get(self, "match"))

    @builtins.property
    @jsii.member(jsii_name="invertInput")
    def invert_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "invertInput"))

    @builtins.property
    @jsii.member(jsii_name="matchInput")
    def match_input(self) -> typing.Optional[AppmeshRouteSpecHttpRouteMatchHeaderMatch]:
        return typing.cast(typing.Optional[AppmeshRouteSpecHttpRouteMatchHeaderMatch], jsii.get(self, "matchInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="invert")
    def invert(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "invert"))

    @invert.setter
    def invert(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__659fed6c4bd84dd46b8333caa91b632f8a8737dc6b469b0bd805b3089d8a60c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "invert", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c23a443c9615cfc114863af8a062696c259acc109bf195600de45c3a69344745)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppmeshRouteSpecHttpRouteMatchHeader, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppmeshRouteSpecHttpRouteMatchHeader, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppmeshRouteSpecHttpRouteMatchHeader, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__959d391742f0c8a92459f02c4fd1d8fd6589626a204009bb24d4a88f210c4cda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshRouteSpecHttpRouteMatchOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttpRouteMatchOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1c288b676ebdc61f9a877820129b71bdacd590f9a7f6c5f6fa4856f3c2772079)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putHeader")
    def put_header(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppmeshRouteSpecHttpRouteMatchHeader, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c564fb7dbbcecd7b6273b5fb18539b57b668c357c5c5c098a99b01d6dedbd75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHeader", [value]))

    @jsii.member(jsii_name="resetHeader")
    def reset_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeader", []))

    @jsii.member(jsii_name="resetMethod")
    def reset_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMethod", []))

    @jsii.member(jsii_name="resetScheme")
    def reset_scheme(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheme", []))

    @builtins.property
    @jsii.member(jsii_name="header")
    def header(self) -> AppmeshRouteSpecHttpRouteMatchHeaderList:
        return typing.cast(AppmeshRouteSpecHttpRouteMatchHeaderList, jsii.get(self, "header"))

    @builtins.property
    @jsii.member(jsii_name="headerInput")
    def header_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshRouteSpecHttpRouteMatchHeader]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshRouteSpecHttpRouteMatchHeader]]], jsii.get(self, "headerInput"))

    @builtins.property
    @jsii.member(jsii_name="methodInput")
    def method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "methodInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="schemeInput")
    def scheme_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemeInput"))

    @builtins.property
    @jsii.member(jsii_name="method")
    def method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "method"))

    @method.setter
    def method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2d143759cf06c48d6c3eca5932f85dbf960d2f58312ebcc8d1984e6df643f0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "method", value)

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d1cd2c9874eddde2042167ea5b705a9c8ea58b25924452f6f9ab05e9d65c176)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="scheme")
    def scheme(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scheme"))

    @scheme.setter
    def scheme(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b40ac02d360ae3cf1bc400c87cdcb60a414b6a128a5f60d1f45d91875a001e86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheme", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshRouteSpecHttpRouteMatch]:
        return typing.cast(typing.Optional[AppmeshRouteSpecHttpRouteMatch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshRouteSpecHttpRouteMatch],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1885c9013c5d96e99bbb1e5829436957cb5bfb501edeb910dcd3fb98d8b8ce6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshRouteSpecHttpRouteOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttpRouteOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4c0a09ecfeca8dbd493226ce16563c67ef13c4ec94b88e2761a528ddd58a2ff7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAction")
    def put_action(
        self,
        *,
        weighted_target: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppmeshRouteSpecHttpRouteActionWeightedTarget, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param weighted_target: weighted_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#weighted_target AppmeshRoute#weighted_target}
        '''
        value = AppmeshRouteSpecHttpRouteAction(weighted_target=weighted_target)

        return typing.cast(None, jsii.invoke(self, "putAction", [value]))

    @jsii.member(jsii_name="putMatch")
    def put_match(
        self,
        *,
        prefix: builtins.str,
        header: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppmeshRouteSpecHttpRouteMatchHeader, typing.Dict[builtins.str, typing.Any]]]]] = None,
        method: typing.Optional[builtins.str] = None,
        scheme: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#prefix AppmeshRoute#prefix}.
        :param header: header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#header AppmeshRoute#header}
        :param method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#method AppmeshRoute#method}.
        :param scheme: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#scheme AppmeshRoute#scheme}.
        '''
        value = AppmeshRouteSpecHttpRouteMatch(
            prefix=prefix, header=header, method=method, scheme=scheme
        )

        return typing.cast(None, jsii.invoke(self, "putMatch", [value]))

    @jsii.member(jsii_name="putRetryPolicy")
    def put_retry_policy(
        self,
        *,
        max_retries: jsii.Number,
        per_retry_timeout: typing.Union["AppmeshRouteSpecHttpRouteRetryPolicyPerRetryTimeout", typing.Dict[builtins.str, typing.Any]],
        http_retry_events: typing.Optional[typing.Sequence[builtins.str]] = None,
        tcp_retry_events: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param max_retries: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#max_retries AppmeshRoute#max_retries}.
        :param per_retry_timeout: per_retry_timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#per_retry_timeout AppmeshRoute#per_retry_timeout}
        :param http_retry_events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#http_retry_events AppmeshRoute#http_retry_events}.
        :param tcp_retry_events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#tcp_retry_events AppmeshRoute#tcp_retry_events}.
        '''
        value = AppmeshRouteSpecHttpRouteRetryPolicy(
            max_retries=max_retries,
            per_retry_timeout=per_retry_timeout,
            http_retry_events=http_retry_events,
            tcp_retry_events=tcp_retry_events,
        )

        return typing.cast(None, jsii.invoke(self, "putRetryPolicy", [value]))

    @jsii.member(jsii_name="putTimeout")
    def put_timeout(
        self,
        *,
        idle: typing.Optional[typing.Union["AppmeshRouteSpecHttpRouteTimeoutIdle", typing.Dict[builtins.str, typing.Any]]] = None,
        per_request: typing.Optional[typing.Union["AppmeshRouteSpecHttpRouteTimeoutPerRequest", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param idle: idle block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#idle AppmeshRoute#idle}
        :param per_request: per_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#per_request AppmeshRoute#per_request}
        '''
        value = AppmeshRouteSpecHttpRouteTimeout(idle=idle, per_request=per_request)

        return typing.cast(None, jsii.invoke(self, "putTimeout", [value]))

    @jsii.member(jsii_name="resetRetryPolicy")
    def reset_retry_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetryPolicy", []))

    @jsii.member(jsii_name="resetTimeout")
    def reset_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeout", []))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> AppmeshRouteSpecHttpRouteActionOutputReference:
        return typing.cast(AppmeshRouteSpecHttpRouteActionOutputReference, jsii.get(self, "action"))

    @builtins.property
    @jsii.member(jsii_name="match")
    def match(self) -> AppmeshRouteSpecHttpRouteMatchOutputReference:
        return typing.cast(AppmeshRouteSpecHttpRouteMatchOutputReference, jsii.get(self, "match"))

    @builtins.property
    @jsii.member(jsii_name="retryPolicy")
    def retry_policy(self) -> "AppmeshRouteSpecHttpRouteRetryPolicyOutputReference":
        return typing.cast("AppmeshRouteSpecHttpRouteRetryPolicyOutputReference", jsii.get(self, "retryPolicy"))

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> "AppmeshRouteSpecHttpRouteTimeoutOutputReference":
        return typing.cast("AppmeshRouteSpecHttpRouteTimeoutOutputReference", jsii.get(self, "timeout"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[AppmeshRouteSpecHttpRouteAction]:
        return typing.cast(typing.Optional[AppmeshRouteSpecHttpRouteAction], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="matchInput")
    def match_input(self) -> typing.Optional[AppmeshRouteSpecHttpRouteMatch]:
        return typing.cast(typing.Optional[AppmeshRouteSpecHttpRouteMatch], jsii.get(self, "matchInput"))

    @builtins.property
    @jsii.member(jsii_name="retryPolicyInput")
    def retry_policy_input(
        self,
    ) -> typing.Optional["AppmeshRouteSpecHttpRouteRetryPolicy"]:
        return typing.cast(typing.Optional["AppmeshRouteSpecHttpRouteRetryPolicy"], jsii.get(self, "retryPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(self) -> typing.Optional["AppmeshRouteSpecHttpRouteTimeout"]:
        return typing.cast(typing.Optional["AppmeshRouteSpecHttpRouteTimeout"], jsii.get(self, "timeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshRouteSpecHttpRoute]:
        return typing.cast(typing.Optional[AppmeshRouteSpecHttpRoute], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppmeshRouteSpecHttpRoute]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55ebdee774000fbdbc63c3050d0ae46b243120f1e5aae1f44c90bcede4549306)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttpRouteRetryPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "max_retries": "maxRetries",
        "per_retry_timeout": "perRetryTimeout",
        "http_retry_events": "httpRetryEvents",
        "tcp_retry_events": "tcpRetryEvents",
    },
)
class AppmeshRouteSpecHttpRouteRetryPolicy:
    def __init__(
        self,
        *,
        max_retries: jsii.Number,
        per_retry_timeout: typing.Union["AppmeshRouteSpecHttpRouteRetryPolicyPerRetryTimeout", typing.Dict[builtins.str, typing.Any]],
        http_retry_events: typing.Optional[typing.Sequence[builtins.str]] = None,
        tcp_retry_events: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param max_retries: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#max_retries AppmeshRoute#max_retries}.
        :param per_retry_timeout: per_retry_timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#per_retry_timeout AppmeshRoute#per_retry_timeout}
        :param http_retry_events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#http_retry_events AppmeshRoute#http_retry_events}.
        :param tcp_retry_events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#tcp_retry_events AppmeshRoute#tcp_retry_events}.
        '''
        if isinstance(per_retry_timeout, dict):
            per_retry_timeout = AppmeshRouteSpecHttpRouteRetryPolicyPerRetryTimeout(**per_retry_timeout)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__436ad581bbd5769a2180ae91769d35a1dca23e91a73cc0d39dbc8494eb1ad0a1)
            check_type(argname="argument max_retries", value=max_retries, expected_type=type_hints["max_retries"])
            check_type(argname="argument per_retry_timeout", value=per_retry_timeout, expected_type=type_hints["per_retry_timeout"])
            check_type(argname="argument http_retry_events", value=http_retry_events, expected_type=type_hints["http_retry_events"])
            check_type(argname="argument tcp_retry_events", value=tcp_retry_events, expected_type=type_hints["tcp_retry_events"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "max_retries": max_retries,
            "per_retry_timeout": per_retry_timeout,
        }
        if http_retry_events is not None:
            self._values["http_retry_events"] = http_retry_events
        if tcp_retry_events is not None:
            self._values["tcp_retry_events"] = tcp_retry_events

    @builtins.property
    def max_retries(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#max_retries AppmeshRoute#max_retries}.'''
        result = self._values.get("max_retries")
        assert result is not None, "Required property 'max_retries' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def per_retry_timeout(
        self,
    ) -> "AppmeshRouteSpecHttpRouteRetryPolicyPerRetryTimeout":
        '''per_retry_timeout block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#per_retry_timeout AppmeshRoute#per_retry_timeout}
        '''
        result = self._values.get("per_retry_timeout")
        assert result is not None, "Required property 'per_retry_timeout' is missing"
        return typing.cast("AppmeshRouteSpecHttpRouteRetryPolicyPerRetryTimeout", result)

    @builtins.property
    def http_retry_events(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#http_retry_events AppmeshRoute#http_retry_events}.'''
        result = self._values.get("http_retry_events")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tcp_retry_events(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#tcp_retry_events AppmeshRoute#tcp_retry_events}.'''
        result = self._values.get("tcp_retry_events")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecHttpRouteRetryPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshRouteSpecHttpRouteRetryPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttpRouteRetryPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d5d04ecdebbd2995b68da7643d85457d73fed685dfbee65ba453a9c517a970f6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPerRetryTimeout")
    def put_per_retry_timeout(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#unit AppmeshRoute#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#value AppmeshRoute#value}.
        '''
        value_ = AppmeshRouteSpecHttpRouteRetryPolicyPerRetryTimeout(
            unit=unit, value=value
        )

        return typing.cast(None, jsii.invoke(self, "putPerRetryTimeout", [value_]))

    @jsii.member(jsii_name="resetHttpRetryEvents")
    def reset_http_retry_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpRetryEvents", []))

    @jsii.member(jsii_name="resetTcpRetryEvents")
    def reset_tcp_retry_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTcpRetryEvents", []))

    @builtins.property
    @jsii.member(jsii_name="perRetryTimeout")
    def per_retry_timeout(
        self,
    ) -> "AppmeshRouteSpecHttpRouteRetryPolicyPerRetryTimeoutOutputReference":
        return typing.cast("AppmeshRouteSpecHttpRouteRetryPolicyPerRetryTimeoutOutputReference", jsii.get(self, "perRetryTimeout"))

    @builtins.property
    @jsii.member(jsii_name="httpRetryEventsInput")
    def http_retry_events_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "httpRetryEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxRetriesInput")
    def max_retries_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxRetriesInput"))

    @builtins.property
    @jsii.member(jsii_name="perRetryTimeoutInput")
    def per_retry_timeout_input(
        self,
    ) -> typing.Optional["AppmeshRouteSpecHttpRouteRetryPolicyPerRetryTimeout"]:
        return typing.cast(typing.Optional["AppmeshRouteSpecHttpRouteRetryPolicyPerRetryTimeout"], jsii.get(self, "perRetryTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="tcpRetryEventsInput")
    def tcp_retry_events_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tcpRetryEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="httpRetryEvents")
    def http_retry_events(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "httpRetryEvents"))

    @http_retry_events.setter
    def http_retry_events(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be6d53cb01f3090dd019b747930cc73654d3740377fe589ddffaff6e0318d53a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpRetryEvents", value)

    @builtins.property
    @jsii.member(jsii_name="maxRetries")
    def max_retries(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxRetries"))

    @max_retries.setter
    def max_retries(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13e087ce98488e41fe439883672e41ba2ae005bd3692ec4e4d5bd39105ea29cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxRetries", value)

    @builtins.property
    @jsii.member(jsii_name="tcpRetryEvents")
    def tcp_retry_events(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tcpRetryEvents"))

    @tcp_retry_events.setter
    def tcp_retry_events(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6649e3f70e8d198b6538832cda0f5f68ad7a7a4205dd55448181c76c6e2fa5b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tcpRetryEvents", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshRouteSpecHttpRouteRetryPolicy]:
        return typing.cast(typing.Optional[AppmeshRouteSpecHttpRouteRetryPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshRouteSpecHttpRouteRetryPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__158d1025d473ab3441bf8d565a3ee7a792c8faf411461f52ce497f88b5c897bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttpRouteRetryPolicyPerRetryTimeout",
    jsii_struct_bases=[],
    name_mapping={"unit": "unit", "value": "value"},
)
class AppmeshRouteSpecHttpRouteRetryPolicyPerRetryTimeout:
    def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#unit AppmeshRoute#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#value AppmeshRoute#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__565654f302707c9532c7d3bbab3bd58eda3341e9ca6f6024e76b53c1697bbe0a)
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "unit": unit,
            "value": value,
        }

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#unit AppmeshRoute#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#value AppmeshRoute#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecHttpRouteRetryPolicyPerRetryTimeout(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshRouteSpecHttpRouteRetryPolicyPerRetryTimeoutOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttpRouteRetryPolicyPerRetryTimeoutOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__978716900366b440a14b259c7b7dc1f58c95059becb4799632ea2ec06be62552)
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
            type_hints = typing.get_type_hints(_typecheckingstub__09d9566764c2c069f1fa3ee214de8ef25fd7839c088f23ef4e9774cd2b712361)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d118e9bbd8c55366436deb8b8716efd5459f5d1c72e2b889e4f4e580c6a23ed8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshRouteSpecHttpRouteRetryPolicyPerRetryTimeout]:
        return typing.cast(typing.Optional[AppmeshRouteSpecHttpRouteRetryPolicyPerRetryTimeout], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshRouteSpecHttpRouteRetryPolicyPerRetryTimeout],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__869da9d41e251329165c1130a0c5eb8714fbc95e6ccbefdbbc829130d9f760df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttpRouteTimeout",
    jsii_struct_bases=[],
    name_mapping={"idle": "idle", "per_request": "perRequest"},
)
class AppmeshRouteSpecHttpRouteTimeout:
    def __init__(
        self,
        *,
        idle: typing.Optional[typing.Union["AppmeshRouteSpecHttpRouteTimeoutIdle", typing.Dict[builtins.str, typing.Any]]] = None,
        per_request: typing.Optional[typing.Union["AppmeshRouteSpecHttpRouteTimeoutPerRequest", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param idle: idle block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#idle AppmeshRoute#idle}
        :param per_request: per_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#per_request AppmeshRoute#per_request}
        '''
        if isinstance(idle, dict):
            idle = AppmeshRouteSpecHttpRouteTimeoutIdle(**idle)
        if isinstance(per_request, dict):
            per_request = AppmeshRouteSpecHttpRouteTimeoutPerRequest(**per_request)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be878e9b92483dd2da5c3c41f54fa59e341c1da0f9cc5538c2f74a880c845b92)
            check_type(argname="argument idle", value=idle, expected_type=type_hints["idle"])
            check_type(argname="argument per_request", value=per_request, expected_type=type_hints["per_request"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if idle is not None:
            self._values["idle"] = idle
        if per_request is not None:
            self._values["per_request"] = per_request

    @builtins.property
    def idle(self) -> typing.Optional["AppmeshRouteSpecHttpRouteTimeoutIdle"]:
        '''idle block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#idle AppmeshRoute#idle}
        '''
        result = self._values.get("idle")
        return typing.cast(typing.Optional["AppmeshRouteSpecHttpRouteTimeoutIdle"], result)

    @builtins.property
    def per_request(
        self,
    ) -> typing.Optional["AppmeshRouteSpecHttpRouteTimeoutPerRequest"]:
        '''per_request block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#per_request AppmeshRoute#per_request}
        '''
        result = self._values.get("per_request")
        return typing.cast(typing.Optional["AppmeshRouteSpecHttpRouteTimeoutPerRequest"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecHttpRouteTimeout(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttpRouteTimeoutIdle",
    jsii_struct_bases=[],
    name_mapping={"unit": "unit", "value": "value"},
)
class AppmeshRouteSpecHttpRouteTimeoutIdle:
    def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#unit AppmeshRoute#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#value AppmeshRoute#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a42620801eb7bd0947cc040a304c2af623a4994e7dd71b4cae4438581642a98c)
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "unit": unit,
            "value": value,
        }

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#unit AppmeshRoute#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#value AppmeshRoute#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecHttpRouteTimeoutIdle(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshRouteSpecHttpRouteTimeoutIdleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttpRouteTimeoutIdleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7baee180bf42ed71d143c7e5c0be979ac5c495c1a3537abb7f5f7acb94c98a6a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a4479889b3411966c02211e95651b9232cd957bdc2d89ef2748b1267f6016ea1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__124efc1dee7ab3e9ba483ab9205afe346dd57032951773b1b28ca80dfee97e2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshRouteSpecHttpRouteTimeoutIdle]:
        return typing.cast(typing.Optional[AppmeshRouteSpecHttpRouteTimeoutIdle], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshRouteSpecHttpRouteTimeoutIdle],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33d30176d9da941fa7a2b9b5780f190331e574c3cbe3f71eb388317e35ee9903)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshRouteSpecHttpRouteTimeoutOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttpRouteTimeoutOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__02ac65bd2ef7b67b1e5e3a1e3a86293d94495619818fee59ad6c946bdaf610c2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putIdle")
    def put_idle(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#unit AppmeshRoute#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#value AppmeshRoute#value}.
        '''
        value_ = AppmeshRouteSpecHttpRouteTimeoutIdle(unit=unit, value=value)

        return typing.cast(None, jsii.invoke(self, "putIdle", [value_]))

    @jsii.member(jsii_name="putPerRequest")
    def put_per_request(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#unit AppmeshRoute#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#value AppmeshRoute#value}.
        '''
        value_ = AppmeshRouteSpecHttpRouteTimeoutPerRequest(unit=unit, value=value)

        return typing.cast(None, jsii.invoke(self, "putPerRequest", [value_]))

    @jsii.member(jsii_name="resetIdle")
    def reset_idle(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdle", []))

    @jsii.member(jsii_name="resetPerRequest")
    def reset_per_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPerRequest", []))

    @builtins.property
    @jsii.member(jsii_name="idle")
    def idle(self) -> AppmeshRouteSpecHttpRouteTimeoutIdleOutputReference:
        return typing.cast(AppmeshRouteSpecHttpRouteTimeoutIdleOutputReference, jsii.get(self, "idle"))

    @builtins.property
    @jsii.member(jsii_name="perRequest")
    def per_request(
        self,
    ) -> "AppmeshRouteSpecHttpRouteTimeoutPerRequestOutputReference":
        return typing.cast("AppmeshRouteSpecHttpRouteTimeoutPerRequestOutputReference", jsii.get(self, "perRequest"))

    @builtins.property
    @jsii.member(jsii_name="idleInput")
    def idle_input(self) -> typing.Optional[AppmeshRouteSpecHttpRouteTimeoutIdle]:
        return typing.cast(typing.Optional[AppmeshRouteSpecHttpRouteTimeoutIdle], jsii.get(self, "idleInput"))

    @builtins.property
    @jsii.member(jsii_name="perRequestInput")
    def per_request_input(
        self,
    ) -> typing.Optional["AppmeshRouteSpecHttpRouteTimeoutPerRequest"]:
        return typing.cast(typing.Optional["AppmeshRouteSpecHttpRouteTimeoutPerRequest"], jsii.get(self, "perRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshRouteSpecHttpRouteTimeout]:
        return typing.cast(typing.Optional[AppmeshRouteSpecHttpRouteTimeout], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshRouteSpecHttpRouteTimeout],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71a0d0ba90520917c89d798564d3cce244c934dbc6cfe706c2b03a3a6299632d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttpRouteTimeoutPerRequest",
    jsii_struct_bases=[],
    name_mapping={"unit": "unit", "value": "value"},
)
class AppmeshRouteSpecHttpRouteTimeoutPerRequest:
    def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#unit AppmeshRoute#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#value AppmeshRoute#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3e3040425e233ee3dec01128e59ecc2c2c34f9ef6fa3f47534adf49b2d26596)
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "unit": unit,
            "value": value,
        }

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#unit AppmeshRoute#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#value AppmeshRoute#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecHttpRouteTimeoutPerRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshRouteSpecHttpRouteTimeoutPerRequestOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecHttpRouteTimeoutPerRequestOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6226041df88ea714699ad5975bdc6fd96bc3d38b41163ab1cec55fde496f4357)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4d57371033143ce6d52c750774dc10a4662616bdd611f099286a2eaf146312e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1edd276349dfce407daec1c957d9243200be10de2e69b62ff81c32b0fdba7de0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshRouteSpecHttpRouteTimeoutPerRequest]:
        return typing.cast(typing.Optional[AppmeshRouteSpecHttpRouteTimeoutPerRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshRouteSpecHttpRouteTimeoutPerRequest],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__261b67e5a9af87843ce2caeea972b3c8e614f5c924dd78b0dca9553ded971c04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshRouteSpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b20c0e00f6c14f4493396523001dfaa2dac10e5b9105638f293dc750b1abf947)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putGrpcRoute")
    def put_grpc_route(
        self,
        *,
        action: typing.Union[AppmeshRouteSpecGrpcRouteAction, typing.Dict[builtins.str, typing.Any]],
        match: typing.Optional[typing.Union[AppmeshRouteSpecGrpcRouteMatch, typing.Dict[builtins.str, typing.Any]]] = None,
        retry_policy: typing.Optional[typing.Union[AppmeshRouteSpecGrpcRouteRetryPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
        timeout: typing.Optional[typing.Union[AppmeshRouteSpecGrpcRouteTimeout, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#action AppmeshRoute#action}
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#match AppmeshRoute#match}
        :param retry_policy: retry_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#retry_policy AppmeshRoute#retry_policy}
        :param timeout: timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#timeout AppmeshRoute#timeout}
        '''
        value = AppmeshRouteSpecGrpcRoute(
            action=action, match=match, retry_policy=retry_policy, timeout=timeout
        )

        return typing.cast(None, jsii.invoke(self, "putGrpcRoute", [value]))

    @jsii.member(jsii_name="putHttp2Route")
    def put_http2_route(
        self,
        *,
        action: typing.Union[AppmeshRouteSpecHttp2RouteAction, typing.Dict[builtins.str, typing.Any]],
        match: typing.Union[AppmeshRouteSpecHttp2RouteMatch, typing.Dict[builtins.str, typing.Any]],
        retry_policy: typing.Optional[typing.Union[AppmeshRouteSpecHttp2RouteRetryPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
        timeout: typing.Optional[typing.Union[AppmeshRouteSpecHttp2RouteTimeout, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#action AppmeshRoute#action}
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#match AppmeshRoute#match}
        :param retry_policy: retry_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#retry_policy AppmeshRoute#retry_policy}
        :param timeout: timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#timeout AppmeshRoute#timeout}
        '''
        value = AppmeshRouteSpecHttp2Route(
            action=action, match=match, retry_policy=retry_policy, timeout=timeout
        )

        return typing.cast(None, jsii.invoke(self, "putHttp2Route", [value]))

    @jsii.member(jsii_name="putHttpRoute")
    def put_http_route(
        self,
        *,
        action: typing.Union[AppmeshRouteSpecHttpRouteAction, typing.Dict[builtins.str, typing.Any]],
        match: typing.Union[AppmeshRouteSpecHttpRouteMatch, typing.Dict[builtins.str, typing.Any]],
        retry_policy: typing.Optional[typing.Union[AppmeshRouteSpecHttpRouteRetryPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
        timeout: typing.Optional[typing.Union[AppmeshRouteSpecHttpRouteTimeout, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#action AppmeshRoute#action}
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#match AppmeshRoute#match}
        :param retry_policy: retry_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#retry_policy AppmeshRoute#retry_policy}
        :param timeout: timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#timeout AppmeshRoute#timeout}
        '''
        value = AppmeshRouteSpecHttpRoute(
            action=action, match=match, retry_policy=retry_policy, timeout=timeout
        )

        return typing.cast(None, jsii.invoke(self, "putHttpRoute", [value]))

    @jsii.member(jsii_name="putTcpRoute")
    def put_tcp_route(
        self,
        *,
        action: typing.Union["AppmeshRouteSpecTcpRouteAction", typing.Dict[builtins.str, typing.Any]],
        timeout: typing.Optional[typing.Union["AppmeshRouteSpecTcpRouteTimeout", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#action AppmeshRoute#action}
        :param timeout: timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#timeout AppmeshRoute#timeout}
        '''
        value = AppmeshRouteSpecTcpRoute(action=action, timeout=timeout)

        return typing.cast(None, jsii.invoke(self, "putTcpRoute", [value]))

    @jsii.member(jsii_name="resetGrpcRoute")
    def reset_grpc_route(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGrpcRoute", []))

    @jsii.member(jsii_name="resetHttp2Route")
    def reset_http2_route(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttp2Route", []))

    @jsii.member(jsii_name="resetHttpRoute")
    def reset_http_route(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpRoute", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetTcpRoute")
    def reset_tcp_route(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTcpRoute", []))

    @builtins.property
    @jsii.member(jsii_name="grpcRoute")
    def grpc_route(self) -> AppmeshRouteSpecGrpcRouteOutputReference:
        return typing.cast(AppmeshRouteSpecGrpcRouteOutputReference, jsii.get(self, "grpcRoute"))

    @builtins.property
    @jsii.member(jsii_name="http2Route")
    def http2_route(self) -> AppmeshRouteSpecHttp2RouteOutputReference:
        return typing.cast(AppmeshRouteSpecHttp2RouteOutputReference, jsii.get(self, "http2Route"))

    @builtins.property
    @jsii.member(jsii_name="httpRoute")
    def http_route(self) -> AppmeshRouteSpecHttpRouteOutputReference:
        return typing.cast(AppmeshRouteSpecHttpRouteOutputReference, jsii.get(self, "httpRoute"))

    @builtins.property
    @jsii.member(jsii_name="tcpRoute")
    def tcp_route(self) -> "AppmeshRouteSpecTcpRouteOutputReference":
        return typing.cast("AppmeshRouteSpecTcpRouteOutputReference", jsii.get(self, "tcpRoute"))

    @builtins.property
    @jsii.member(jsii_name="grpcRouteInput")
    def grpc_route_input(self) -> typing.Optional[AppmeshRouteSpecGrpcRoute]:
        return typing.cast(typing.Optional[AppmeshRouteSpecGrpcRoute], jsii.get(self, "grpcRouteInput"))

    @builtins.property
    @jsii.member(jsii_name="http2RouteInput")
    def http2_route_input(self) -> typing.Optional[AppmeshRouteSpecHttp2Route]:
        return typing.cast(typing.Optional[AppmeshRouteSpecHttp2Route], jsii.get(self, "http2RouteInput"))

    @builtins.property
    @jsii.member(jsii_name="httpRouteInput")
    def http_route_input(self) -> typing.Optional[AppmeshRouteSpecHttpRoute]:
        return typing.cast(typing.Optional[AppmeshRouteSpecHttpRoute], jsii.get(self, "httpRouteInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="tcpRouteInput")
    def tcp_route_input(self) -> typing.Optional["AppmeshRouteSpecTcpRoute"]:
        return typing.cast(typing.Optional["AppmeshRouteSpecTcpRoute"], jsii.get(self, "tcpRouteInput"))

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a26b05b6e6d849e05a9a31da5265ae78b193cc01241c08a17366e66216c1c1a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshRouteSpec]:
        return typing.cast(typing.Optional[AppmeshRouteSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppmeshRouteSpec]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b2aeec8f3d198c29ae4cb119f5d33084729ee163ba89aa53be8794c74415cb9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecTcpRoute",
    jsii_struct_bases=[],
    name_mapping={"action": "action", "timeout": "timeout"},
)
class AppmeshRouteSpecTcpRoute:
    def __init__(
        self,
        *,
        action: typing.Union["AppmeshRouteSpecTcpRouteAction", typing.Dict[builtins.str, typing.Any]],
        timeout: typing.Optional[typing.Union["AppmeshRouteSpecTcpRouteTimeout", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#action AppmeshRoute#action}
        :param timeout: timeout block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#timeout AppmeshRoute#timeout}
        '''
        if isinstance(action, dict):
            action = AppmeshRouteSpecTcpRouteAction(**action)
        if isinstance(timeout, dict):
            timeout = AppmeshRouteSpecTcpRouteTimeout(**timeout)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e67d4456d9adbd773cc9cd086521304a10dec5b95e5a6ffe4a41881093db4c6)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action": action,
        }
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def action(self) -> "AppmeshRouteSpecTcpRouteAction":
        '''action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#action AppmeshRoute#action}
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast("AppmeshRouteSpecTcpRouteAction", result)

    @builtins.property
    def timeout(self) -> typing.Optional["AppmeshRouteSpecTcpRouteTimeout"]:
        '''timeout block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#timeout AppmeshRoute#timeout}
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional["AppmeshRouteSpecTcpRouteTimeout"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecTcpRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecTcpRouteAction",
    jsii_struct_bases=[],
    name_mapping={"weighted_target": "weightedTarget"},
)
class AppmeshRouteSpecTcpRouteAction:
    def __init__(
        self,
        *,
        weighted_target: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AppmeshRouteSpecTcpRouteActionWeightedTarget", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param weighted_target: weighted_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#weighted_target AppmeshRoute#weighted_target}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1076e1910326b723f27a6aac58a87f59c2121ec33747c100c19d7545b4c3caa)
            check_type(argname="argument weighted_target", value=weighted_target, expected_type=type_hints["weighted_target"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "weighted_target": weighted_target,
        }

    @builtins.property
    def weighted_target(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppmeshRouteSpecTcpRouteActionWeightedTarget"]]:
        '''weighted_target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#weighted_target AppmeshRoute#weighted_target}
        '''
        result = self._values.get("weighted_target")
        assert result is not None, "Required property 'weighted_target' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppmeshRouteSpecTcpRouteActionWeightedTarget"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecTcpRouteAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshRouteSpecTcpRouteActionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecTcpRouteActionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b1b9ca3e1f161d1262a8444663d1ae925c814eac3c695a9407b3576b8caa34f0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putWeightedTarget")
    def put_weighted_target(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AppmeshRouteSpecTcpRouteActionWeightedTarget", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__103d24140ea8c788fd5a415bef38fef6f80460a5b15eb9950e83118aa10dd737)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWeightedTarget", [value]))

    @builtins.property
    @jsii.member(jsii_name="weightedTarget")
    def weighted_target(self) -> "AppmeshRouteSpecTcpRouteActionWeightedTargetList":
        return typing.cast("AppmeshRouteSpecTcpRouteActionWeightedTargetList", jsii.get(self, "weightedTarget"))

    @builtins.property
    @jsii.member(jsii_name="weightedTargetInput")
    def weighted_target_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppmeshRouteSpecTcpRouteActionWeightedTarget"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AppmeshRouteSpecTcpRouteActionWeightedTarget"]]], jsii.get(self, "weightedTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshRouteSpecTcpRouteAction]:
        return typing.cast(typing.Optional[AppmeshRouteSpecTcpRouteAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshRouteSpecTcpRouteAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__124b2e35c2cc3931c3a72aa33e0666d4fb710c0151b3f31d38fd846794db4e9a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecTcpRouteActionWeightedTarget",
    jsii_struct_bases=[],
    name_mapping={"virtual_node": "virtualNode", "weight": "weight"},
)
class AppmeshRouteSpecTcpRouteActionWeightedTarget:
    def __init__(self, *, virtual_node: builtins.str, weight: jsii.Number) -> None:
        '''
        :param virtual_node: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#virtual_node AppmeshRoute#virtual_node}.
        :param weight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#weight AppmeshRoute#weight}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f979db187b8a1a7c026f15b4a80754e8f6dcca94e494812d53e8d6ae23429cc)
            check_type(argname="argument virtual_node", value=virtual_node, expected_type=type_hints["virtual_node"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "virtual_node": virtual_node,
            "weight": weight,
        }

    @builtins.property
    def virtual_node(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#virtual_node AppmeshRoute#virtual_node}.'''
        result = self._values.get("virtual_node")
        assert result is not None, "Required property 'virtual_node' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def weight(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#weight AppmeshRoute#weight}.'''
        result = self._values.get("weight")
        assert result is not None, "Required property 'weight' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecTcpRouteActionWeightedTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshRouteSpecTcpRouteActionWeightedTargetList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecTcpRouteActionWeightedTargetList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fcb032d707592311aa26d5f8a3471a2270159b5b475f892d33566562dbded9e5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AppmeshRouteSpecTcpRouteActionWeightedTargetOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcf10b7402476354ded397d208d9fb471193e1be571d6504115965ca8dd0bf6e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppmeshRouteSpecTcpRouteActionWeightedTargetOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c48a8a5c2c517cd7fdada8437f63ac9ae190a11e9d8674eeecff2de24b8238ca)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ea816f19f763095d9b0a26961da1a6def0b854abb45ef991becfc5430f8667c6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bb0ba545a940b71b1c777b7fd1c193add494526999a5233720ae3a86ff524728)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshRouteSpecTcpRouteActionWeightedTarget]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshRouteSpecTcpRouteActionWeightedTarget]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshRouteSpecTcpRouteActionWeightedTarget]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__491eb8f690fd5f7e7f13d7e4a678717e4d4275819a5758925f6a24a4c3e0d841)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshRouteSpecTcpRouteActionWeightedTargetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecTcpRouteActionWeightedTargetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d902b39373f26a10a7c52afb12c60e5bce8d6e32843fdad9c0aa9706c76dfd0c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="virtualNodeInput")
    def virtual_node_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualNodeInput"))

    @builtins.property
    @jsii.member(jsii_name="weightInput")
    def weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNode")
    def virtual_node(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualNode"))

    @virtual_node.setter
    def virtual_node(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9eda045394fbf3e4a26c5b3ea2d9552c4986ef21f98c422b2b8042643f69d583)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualNode", value)

    @builtins.property
    @jsii.member(jsii_name="weight")
    def weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weight"))

    @weight.setter
    def weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6594d885ef76f9f115b589ab0dd35bc30a76e632f927bd3d044050f77b7e14b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weight", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppmeshRouteSpecTcpRouteActionWeightedTarget, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppmeshRouteSpecTcpRouteActionWeightedTarget, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppmeshRouteSpecTcpRouteActionWeightedTarget, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__505eedec42acadc30b44f27d1e25c5ca7931e77ac8b7430907c2af1a4a2c833d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshRouteSpecTcpRouteOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecTcpRouteOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c0fe9ef5234bb4b2bbb67418055f0803c33b2f34e5ae30c9a94ac1d4180d941d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAction")
    def put_action(
        self,
        *,
        weighted_target: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppmeshRouteSpecTcpRouteActionWeightedTarget, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param weighted_target: weighted_target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#weighted_target AppmeshRoute#weighted_target}
        '''
        value = AppmeshRouteSpecTcpRouteAction(weighted_target=weighted_target)

        return typing.cast(None, jsii.invoke(self, "putAction", [value]))

    @jsii.member(jsii_name="putTimeout")
    def put_timeout(
        self,
        *,
        idle: typing.Optional[typing.Union["AppmeshRouteSpecTcpRouteTimeoutIdle", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param idle: idle block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#idle AppmeshRoute#idle}
        '''
        value = AppmeshRouteSpecTcpRouteTimeout(idle=idle)

        return typing.cast(None, jsii.invoke(self, "putTimeout", [value]))

    @jsii.member(jsii_name="resetTimeout")
    def reset_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeout", []))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> AppmeshRouteSpecTcpRouteActionOutputReference:
        return typing.cast(AppmeshRouteSpecTcpRouteActionOutputReference, jsii.get(self, "action"))

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> "AppmeshRouteSpecTcpRouteTimeoutOutputReference":
        return typing.cast("AppmeshRouteSpecTcpRouteTimeoutOutputReference", jsii.get(self, "timeout"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[AppmeshRouteSpecTcpRouteAction]:
        return typing.cast(typing.Optional[AppmeshRouteSpecTcpRouteAction], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(self) -> typing.Optional["AppmeshRouteSpecTcpRouteTimeout"]:
        return typing.cast(typing.Optional["AppmeshRouteSpecTcpRouteTimeout"], jsii.get(self, "timeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshRouteSpecTcpRoute]:
        return typing.cast(typing.Optional[AppmeshRouteSpecTcpRoute], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppmeshRouteSpecTcpRoute]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6ff1cb720c127ea1b781a6638e9d44fb99691910f8df7bba5a24d28acc9d764)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecTcpRouteTimeout",
    jsii_struct_bases=[],
    name_mapping={"idle": "idle"},
)
class AppmeshRouteSpecTcpRouteTimeout:
    def __init__(
        self,
        *,
        idle: typing.Optional[typing.Union["AppmeshRouteSpecTcpRouteTimeoutIdle", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param idle: idle block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#idle AppmeshRoute#idle}
        '''
        if isinstance(idle, dict):
            idle = AppmeshRouteSpecTcpRouteTimeoutIdle(**idle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4835b958e4cc9fc253e55d0e4d5a472402e08d6e64ec415ba3dda105832cf0ca)
            check_type(argname="argument idle", value=idle, expected_type=type_hints["idle"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if idle is not None:
            self._values["idle"] = idle

    @builtins.property
    def idle(self) -> typing.Optional["AppmeshRouteSpecTcpRouteTimeoutIdle"]:
        '''idle block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#idle AppmeshRoute#idle}
        '''
        result = self._values.get("idle")
        return typing.cast(typing.Optional["AppmeshRouteSpecTcpRouteTimeoutIdle"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecTcpRouteTimeout(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecTcpRouteTimeoutIdle",
    jsii_struct_bases=[],
    name_mapping={"unit": "unit", "value": "value"},
)
class AppmeshRouteSpecTcpRouteTimeoutIdle:
    def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#unit AppmeshRoute#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#value AppmeshRoute#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d46739c04a8e91b6a64772490fb5905fff467af3ef33ae921a3ee9e012ff8db1)
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "unit": unit,
            "value": value,
        }

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#unit AppmeshRoute#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#value AppmeshRoute#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshRouteSpecTcpRouteTimeoutIdle(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshRouteSpecTcpRouteTimeoutIdleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecTcpRouteTimeoutIdleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e71fbaddbab487c92020d0f63aca2612d84b7dee30d8a7582b5e59d28d8b469c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__63012fdba6dd89e2217f8e062695fa734c8181f5cbfbc12470d8445913192a0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5442438154fce1fa144ad9991ab46d66f1bd78c9a2f187af64ff293b0d86f7f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshRouteSpecTcpRouteTimeoutIdle]:
        return typing.cast(typing.Optional[AppmeshRouteSpecTcpRouteTimeoutIdle], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshRouteSpecTcpRouteTimeoutIdle],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9c1c0b882e260773a59342af0fb9f28dbc798938a8d78621411ae137f49f8fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshRouteSpecTcpRouteTimeoutOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshRoute.AppmeshRouteSpecTcpRouteTimeoutOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f11c0807e72d10bbfaa2afbe4ecc9fa700a523e4268b1b5ce405ceda9d066eda)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putIdle")
    def put_idle(self, *, unit: builtins.str, value: jsii.Number) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#unit AppmeshRoute#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_route#value AppmeshRoute#value}.
        '''
        value_ = AppmeshRouteSpecTcpRouteTimeoutIdle(unit=unit, value=value)

        return typing.cast(None, jsii.invoke(self, "putIdle", [value_]))

    @jsii.member(jsii_name="resetIdle")
    def reset_idle(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdle", []))

    @builtins.property
    @jsii.member(jsii_name="idle")
    def idle(self) -> AppmeshRouteSpecTcpRouteTimeoutIdleOutputReference:
        return typing.cast(AppmeshRouteSpecTcpRouteTimeoutIdleOutputReference, jsii.get(self, "idle"))

    @builtins.property
    @jsii.member(jsii_name="idleInput")
    def idle_input(self) -> typing.Optional[AppmeshRouteSpecTcpRouteTimeoutIdle]:
        return typing.cast(typing.Optional[AppmeshRouteSpecTcpRouteTimeoutIdle], jsii.get(self, "idleInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshRouteSpecTcpRouteTimeout]:
        return typing.cast(typing.Optional[AppmeshRouteSpecTcpRouteTimeout], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshRouteSpecTcpRouteTimeout],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1570617cdb5d4703ffd7b7d2840b5fbcb2b81746d29ce3e8cdc39c2f4f43c273)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AppmeshRoute",
    "AppmeshRouteConfig",
    "AppmeshRouteSpec",
    "AppmeshRouteSpecGrpcRoute",
    "AppmeshRouteSpecGrpcRouteAction",
    "AppmeshRouteSpecGrpcRouteActionOutputReference",
    "AppmeshRouteSpecGrpcRouteActionWeightedTarget",
    "AppmeshRouteSpecGrpcRouteActionWeightedTargetList",
    "AppmeshRouteSpecGrpcRouteActionWeightedTargetOutputReference",
    "AppmeshRouteSpecGrpcRouteMatch",
    "AppmeshRouteSpecGrpcRouteMatchMetadata",
    "AppmeshRouteSpecGrpcRouteMatchMetadataList",
    "AppmeshRouteSpecGrpcRouteMatchMetadataMatch",
    "AppmeshRouteSpecGrpcRouteMatchMetadataMatchOutputReference",
    "AppmeshRouteSpecGrpcRouteMatchMetadataMatchRange",
    "AppmeshRouteSpecGrpcRouteMatchMetadataMatchRangeOutputReference",
    "AppmeshRouteSpecGrpcRouteMatchMetadataOutputReference",
    "AppmeshRouteSpecGrpcRouteMatchOutputReference",
    "AppmeshRouteSpecGrpcRouteOutputReference",
    "AppmeshRouteSpecGrpcRouteRetryPolicy",
    "AppmeshRouteSpecGrpcRouteRetryPolicyOutputReference",
    "AppmeshRouteSpecGrpcRouteRetryPolicyPerRetryTimeout",
    "AppmeshRouteSpecGrpcRouteRetryPolicyPerRetryTimeoutOutputReference",
    "AppmeshRouteSpecGrpcRouteTimeout",
    "AppmeshRouteSpecGrpcRouteTimeoutIdle",
    "AppmeshRouteSpecGrpcRouteTimeoutIdleOutputReference",
    "AppmeshRouteSpecGrpcRouteTimeoutOutputReference",
    "AppmeshRouteSpecGrpcRouteTimeoutPerRequest",
    "AppmeshRouteSpecGrpcRouteTimeoutPerRequestOutputReference",
    "AppmeshRouteSpecHttp2Route",
    "AppmeshRouteSpecHttp2RouteAction",
    "AppmeshRouteSpecHttp2RouteActionOutputReference",
    "AppmeshRouteSpecHttp2RouteActionWeightedTarget",
    "AppmeshRouteSpecHttp2RouteActionWeightedTargetList",
    "AppmeshRouteSpecHttp2RouteActionWeightedTargetOutputReference",
    "AppmeshRouteSpecHttp2RouteMatch",
    "AppmeshRouteSpecHttp2RouteMatchHeader",
    "AppmeshRouteSpecHttp2RouteMatchHeaderList",
    "AppmeshRouteSpecHttp2RouteMatchHeaderMatch",
    "AppmeshRouteSpecHttp2RouteMatchHeaderMatchOutputReference",
    "AppmeshRouteSpecHttp2RouteMatchHeaderMatchRange",
    "AppmeshRouteSpecHttp2RouteMatchHeaderMatchRangeOutputReference",
    "AppmeshRouteSpecHttp2RouteMatchHeaderOutputReference",
    "AppmeshRouteSpecHttp2RouteMatchOutputReference",
    "AppmeshRouteSpecHttp2RouteOutputReference",
    "AppmeshRouteSpecHttp2RouteRetryPolicy",
    "AppmeshRouteSpecHttp2RouteRetryPolicyOutputReference",
    "AppmeshRouteSpecHttp2RouteRetryPolicyPerRetryTimeout",
    "AppmeshRouteSpecHttp2RouteRetryPolicyPerRetryTimeoutOutputReference",
    "AppmeshRouteSpecHttp2RouteTimeout",
    "AppmeshRouteSpecHttp2RouteTimeoutIdle",
    "AppmeshRouteSpecHttp2RouteTimeoutIdleOutputReference",
    "AppmeshRouteSpecHttp2RouteTimeoutOutputReference",
    "AppmeshRouteSpecHttp2RouteTimeoutPerRequest",
    "AppmeshRouteSpecHttp2RouteTimeoutPerRequestOutputReference",
    "AppmeshRouteSpecHttpRoute",
    "AppmeshRouteSpecHttpRouteAction",
    "AppmeshRouteSpecHttpRouteActionOutputReference",
    "AppmeshRouteSpecHttpRouteActionWeightedTarget",
    "AppmeshRouteSpecHttpRouteActionWeightedTargetList",
    "AppmeshRouteSpecHttpRouteActionWeightedTargetOutputReference",
    "AppmeshRouteSpecHttpRouteMatch",
    "AppmeshRouteSpecHttpRouteMatchHeader",
    "AppmeshRouteSpecHttpRouteMatchHeaderList",
    "AppmeshRouteSpecHttpRouteMatchHeaderMatch",
    "AppmeshRouteSpecHttpRouteMatchHeaderMatchOutputReference",
    "AppmeshRouteSpecHttpRouteMatchHeaderMatchRange",
    "AppmeshRouteSpecHttpRouteMatchHeaderMatchRangeOutputReference",
    "AppmeshRouteSpecHttpRouteMatchHeaderOutputReference",
    "AppmeshRouteSpecHttpRouteMatchOutputReference",
    "AppmeshRouteSpecHttpRouteOutputReference",
    "AppmeshRouteSpecHttpRouteRetryPolicy",
    "AppmeshRouteSpecHttpRouteRetryPolicyOutputReference",
    "AppmeshRouteSpecHttpRouteRetryPolicyPerRetryTimeout",
    "AppmeshRouteSpecHttpRouteRetryPolicyPerRetryTimeoutOutputReference",
    "AppmeshRouteSpecHttpRouteTimeout",
    "AppmeshRouteSpecHttpRouteTimeoutIdle",
    "AppmeshRouteSpecHttpRouteTimeoutIdleOutputReference",
    "AppmeshRouteSpecHttpRouteTimeoutOutputReference",
    "AppmeshRouteSpecHttpRouteTimeoutPerRequest",
    "AppmeshRouteSpecHttpRouteTimeoutPerRequestOutputReference",
    "AppmeshRouteSpecOutputReference",
    "AppmeshRouteSpecTcpRoute",
    "AppmeshRouteSpecTcpRouteAction",
    "AppmeshRouteSpecTcpRouteActionOutputReference",
    "AppmeshRouteSpecTcpRouteActionWeightedTarget",
    "AppmeshRouteSpecTcpRouteActionWeightedTargetList",
    "AppmeshRouteSpecTcpRouteActionWeightedTargetOutputReference",
    "AppmeshRouteSpecTcpRouteOutputReference",
    "AppmeshRouteSpecTcpRouteTimeout",
    "AppmeshRouteSpecTcpRouteTimeoutIdle",
    "AppmeshRouteSpecTcpRouteTimeoutIdleOutputReference",
    "AppmeshRouteSpecTcpRouteTimeoutOutputReference",
]

publication.publish()

def _typecheckingstub__499d83546f51cceddcb769519c984570619874357f30feab8625fec171bfc113(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    mesh_name: builtins.str,
    name: builtins.str,
    spec: typing.Union[AppmeshRouteSpec, typing.Dict[builtins.str, typing.Any]],
    virtual_router_name: builtins.str,
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

def _typecheckingstub__7dba324d7e133718364d8ab038d32d28ce364b6b76daa256c53f932ff27c6433(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e584e5becd0196157e82e66cbc42cbcba02e97953cb58a3d707d2767f6d8af15(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c476d888e315d810ad21fc21e13df6d349863f1b5fe3c22429515927818561b2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33a5e64c718469ffd56cb3dff63ffae7a72128843c47f262b73d66298f4332a1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d31d507f8c156b7afa8933b7cca728bd522ec6ad2ba486c64420cfffaaa28fb0(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d742c33216c5f2c02de95ebe1b83d2cd77acc2bce14130f72419009fd42957bb(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0051872ca32ca6887399275ca9030b827f28dcdc7701fd49ead8d2b8305e5811(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__594bdf1650e42f4ccd51b19f32715f923d8ff4907b9484c491a626e41ba72cb7(
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
    spec: typing.Union[AppmeshRouteSpec, typing.Dict[builtins.str, typing.Any]],
    virtual_router_name: builtins.str,
    id: typing.Optional[builtins.str] = None,
    mesh_owner: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7540b62900c9022fc14a9cb2fad09782afdf7505effde7e17f1e857b1e74259f(
    *,
    grpc_route: typing.Optional[typing.Union[AppmeshRouteSpecGrpcRoute, typing.Dict[builtins.str, typing.Any]]] = None,
    http2_route: typing.Optional[typing.Union[AppmeshRouteSpecHttp2Route, typing.Dict[builtins.str, typing.Any]]] = None,
    http_route: typing.Optional[typing.Union[AppmeshRouteSpecHttpRoute, typing.Dict[builtins.str, typing.Any]]] = None,
    priority: typing.Optional[jsii.Number] = None,
    tcp_route: typing.Optional[typing.Union[AppmeshRouteSpecTcpRoute, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd319ffac56c2124480c1ef84147cb35b1a46fe9ddf9ec7a93539ff1186b989a(
    *,
    action: typing.Union[AppmeshRouteSpecGrpcRouteAction, typing.Dict[builtins.str, typing.Any]],
    match: typing.Optional[typing.Union[AppmeshRouteSpecGrpcRouteMatch, typing.Dict[builtins.str, typing.Any]]] = None,
    retry_policy: typing.Optional[typing.Union[AppmeshRouteSpecGrpcRouteRetryPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    timeout: typing.Optional[typing.Union[AppmeshRouteSpecGrpcRouteTimeout, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__406ed44a0eeae677559372942f25ec13dd00817650a4ec55c9d3f6f7b20e5a26(
    *,
    weighted_target: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppmeshRouteSpecGrpcRouteActionWeightedTarget, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95310011b50709cc1982b713c1bd996e7a172924fe456b7fade5160d109de8a3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4502215445b7206d4afc486ef83d002382f6b132b351b5108005c6391c830087(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppmeshRouteSpecGrpcRouteActionWeightedTarget, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a07716348b397b797eb8152fcd1bd11e4900b10e24b4db183af5641e07fec4e(
    value: typing.Optional[AppmeshRouteSpecGrpcRouteAction],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7138c7ca95b2f4688250f648fac99ed2e9b45721e82bdc5d8ec2ccc65558f479(
    *,
    virtual_node: builtins.str,
    weight: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3efc45f8db0bbab296df7a5c169358e54e88dac1cc503cc32bbd6e7da120bf30(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__259586adaff0dd125e5f386c21b8d3a9bc95add39b03403064fd07b70fd644ae(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40fe8bfd65f059bc57b1cbc23be51da804e41fc8b7f9fb43a3d1951e86164f34(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c8b182a6c4a52c5ea2b046eee955f50c06141f9b6c5204dec8fe82219140e4c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4a424b97b49fb59e8198182ac15046664ab015e5b58710991fa34ac260c09b8(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67e9a3560e71628e69a1e369e281564cd06c606d354ebcad08ee25a35f8c8eea(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshRouteSpecGrpcRouteActionWeightedTarget]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbdaee0dfc2c8102876d5669d0a6d5849447bd25c1a105670b91f01693992a81(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f48bfc30ae59f94d2c31f4ebdd87e6e3af84f11dcebc18df6f485c94c5710fc9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d15db8945f3d9aecf5232ae33c4978094494cfd798e1bde59ed2f8baf134c23(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdd19af0ac7e17bb0ef8c7dc3e6444a6ef139429d98441945b76b745a8c91465(
    value: typing.Optional[typing.Union[AppmeshRouteSpecGrpcRouteActionWeightedTarget, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3893328932cb68be97fbfb8a092a0fd13dbab6723060eaae578ad644a0561a47(
    *,
    metadata: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppmeshRouteSpecGrpcRouteMatchMetadata, typing.Dict[builtins.str, typing.Any]]]]] = None,
    method_name: typing.Optional[builtins.str] = None,
    prefix: typing.Optional[builtins.str] = None,
    service_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__473001717cd70955668867e4b555debf8ec2e0e32e74008ee61fa75d46035720(
    *,
    name: builtins.str,
    invert: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    match: typing.Optional[typing.Union[AppmeshRouteSpecGrpcRouteMatchMetadataMatch, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b9c5e9850f578d2f0ca20d4803bf1db798e5b3697b1d01a2e1c24e237739e5a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7b8fd4a526cd30abc5e30ec8fb353438bc996737f7f3d0b3f2c6ca498d38674(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c42a67519ac2ca4186b24f26ad9f1bcf726534e8bdfaab2ec436fe4e85f36c8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1b3e6748e8862344380c1ebbbbab4a26e82977b7dcb1a29f08c00cc61c666b2(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__360d09f5a273c7703d02402f5f128245873ed366c06a4aee6e10647a23156149(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a23d8166d0e0aa91b9379f1c4bac67bc73bf8e890c6c7c2deab72462b8771a1(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshRouteSpecGrpcRouteMatchMetadata]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6999507796e6a24dad0580a0b5c608f3715bddb5dbcb04c5fecfa48cc5c2a16(
    *,
    exact: typing.Optional[builtins.str] = None,
    prefix: typing.Optional[builtins.str] = None,
    range: typing.Optional[typing.Union[AppmeshRouteSpecGrpcRouteMatchMetadataMatchRange, typing.Dict[builtins.str, typing.Any]]] = None,
    regex: typing.Optional[builtins.str] = None,
    suffix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2db06ebcbc67280137e012a207781816c8a47f9a6df4d19f1decb248df9e4c6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f404bfb4a93e7bad6fbd7fb8ece0c69dabcf09cb74d524b0ddc7bac41aab0c0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f99525424ad2c3456f5edb2082386b09ac7f44e8f5b34a9ec284d1e16772bcbc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75f3b5eb368dae5a3c75c793c1f721799a1eccf4452e026c76b3af983662cd1b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__328c0f5180b92a172c11e765c2c106a566c47cfb11797bb72852c8a793b0bb16(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f69401d3400e45c6e3c3a9e0acbdedea8f3024a59a84a74f2f21242eb48828f4(
    value: typing.Optional[AppmeshRouteSpecGrpcRouteMatchMetadataMatch],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80e2a66ff8d38cb1edf4cf31f776a81965812b2b459fa1d8ea4f1f49f272e312(
    *,
    end: jsii.Number,
    start: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f31e9c3c59fffe96b36f59ead4ec2c481a0343347eff509961262fe2f371027(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83782a7961265f9a4f7fc090a112245a0470b3901e6281711fe14ea8cbffa64b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9523916225796accd845a61f40d91060e8a9f8c969ea969e60b292661d0b492(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e9eb7648b53073c5080a8b5d6cdc00bb7d636406b4125a8ff80370cbc4d05d0(
    value: typing.Optional[AppmeshRouteSpecGrpcRouteMatchMetadataMatchRange],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46e4b150615b9d39c3ad89beef7c738129a7bbed08899bc8a058bc20d8e7feb9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cde7b582f4356b82fde650e8c8192d837c136be44233711fe102d8649ed834d5(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f25644d2626755c7f7c43ab6c95736ece76a8a4afc80abf6a8a1e62ec5a410cf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c39d086f769ef688ae0607fdc325105ff134965fd90f04b86bcd3ec491ef7a43(
    value: typing.Optional[typing.Union[AppmeshRouteSpecGrpcRouteMatchMetadata, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__692c5970f6bfa914fedb05549b238f9402c316483e229d04d231fcfbccca58a5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cff764febb639b12f7b3b69b7848dbe279d9ac65fe268cb0a0200eb05c5cdc3(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppmeshRouteSpecGrpcRouteMatchMetadata, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__244c4e02f6f357fdc56c7f950f6529c7c4fa72dd02afcb9161235d68288fe99a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2536b5c1533ed11718c66c8265ea1101bcc7763b6b5fe814df807de6a66dd3d5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56d009b955d4d952a294cd709fd224a3bee609fbf84b3adb2cfb6a1d258ed02c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c3b27ad442456a05c7b68d0c8d99caca5337bd77cc927d16a3ad43daf08cc1b(
    value: typing.Optional[AppmeshRouteSpecGrpcRouteMatch],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8db137452782a41137825c14d8ceb81625d34d0948ab7f12766e037a726b9f96(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9db9e0377d9201075f081972c15e3c7026da0b8202b303efb895ce9de7d0e848(
    value: typing.Optional[AppmeshRouteSpecGrpcRoute],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a433619ff60dedcb54e5508b2559647157115f1ad20a0723cb8024c223b5ac8e(
    *,
    max_retries: jsii.Number,
    per_retry_timeout: typing.Union[AppmeshRouteSpecGrpcRouteRetryPolicyPerRetryTimeout, typing.Dict[builtins.str, typing.Any]],
    grpc_retry_events: typing.Optional[typing.Sequence[builtins.str]] = None,
    http_retry_events: typing.Optional[typing.Sequence[builtins.str]] = None,
    tcp_retry_events: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8be5d73fe085f9fca4221d19fb082a7674d81f5152b0ca85f3f249aa7a5278ab(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b3874db100b34a10f81feadbf41da0fbb73b2586f92c309f3fa3f60042eca04(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07f3bb6e74494e6fac537ee2a1283c54f18a70c60ef946b2094e33f7c11182af(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f901a63d62b4aa7485b645933bca5c2269124bd4756f7677add54f395883aff(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0de05ccf8248ae08b41e60609bda57ba6eddd211acdeb0ab3258df2712085c3a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46c296bee6c57239bbb5d5938a87e3eb5e61b0cc746be5731153a05032a4a2cc(
    value: typing.Optional[AppmeshRouteSpecGrpcRouteRetryPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91d042704cbd63dca9b1272afa6af17665e3ff5ee0db0a3c5be596a159629cd6(
    *,
    unit: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c31e51e64352b8b0c9470fdf91112b199c09bb961264f89929a7ccf39064cc2a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57f42b3b5fb85cc519a654a64ae153ead1c0cff5c56cad64afbc9472ee6b3b13(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb7cf42b16e8dca0e5148942020d970ee1dd204899a308028c8dcf560b64a39d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d7bf76e1d7c3fbd4c55897c1606c7a42e8ea9b63dedb68559f3832b9d9e8a96(
    value: typing.Optional[AppmeshRouteSpecGrpcRouteRetryPolicyPerRetryTimeout],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__215c9ac86a95796584cc2be5cc340f5541dedf487f7e3d17e5e062a4cb99df48(
    *,
    idle: typing.Optional[typing.Union[AppmeshRouteSpecGrpcRouteTimeoutIdle, typing.Dict[builtins.str, typing.Any]]] = None,
    per_request: typing.Optional[typing.Union[AppmeshRouteSpecGrpcRouteTimeoutPerRequest, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c13b19a81f3a07ad124cdd3e44167dbf3be28b461dad9e37accf3e86f8249257(
    *,
    unit: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6beb400bbd1dfde7bb07a43e09221372627558c18df80c58b240bdfda0986e3b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2528f7af55147755d6e2f2f6df74a2e740834219979be7685e117e5dc150916b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5f188309bd3493943ef76e4f3d296870deb17c94a924cb0d7172c63e003dca8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb6b4117bb3440f747a606fb49052979e390c3ff7b335ff27bfe6c52a5f6af03(
    value: typing.Optional[AppmeshRouteSpecGrpcRouteTimeoutIdle],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b49bfb1f7ca2345ecaf3821c84b845b1457572e67eff28245429912cffaaf3e5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33a6ef38a824881968f53a64344d11f8d7ed4e76bca098c8f53e8d21b7310580(
    value: typing.Optional[AppmeshRouteSpecGrpcRouteTimeout],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a5516844260162667ca4c143f4cdd7ff5a210fd37913cba7a5cb361ec551213(
    *,
    unit: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bff3c4866a05f5b8734fd84de617bf43a5e6a1860d977b8a54db7e66a6be5f26(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44c5d7459f87ff64de40598980025a056d3c437556c15a7d572cb4af80cf79a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__482bbb23740de2d51e6a908c41c074796654937efaabcfde7d387c8980c7e80e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5665b2143565d04980ccf42bc8537779a4b23ce3e731f1926d724d599a90f506(
    value: typing.Optional[AppmeshRouteSpecGrpcRouteTimeoutPerRequest],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0aaed28fb43b7d062cd3afcb708865cc176d5586d8bc2bb7df975dac5a8d29a(
    *,
    action: typing.Union[AppmeshRouteSpecHttp2RouteAction, typing.Dict[builtins.str, typing.Any]],
    match: typing.Union[AppmeshRouteSpecHttp2RouteMatch, typing.Dict[builtins.str, typing.Any]],
    retry_policy: typing.Optional[typing.Union[AppmeshRouteSpecHttp2RouteRetryPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    timeout: typing.Optional[typing.Union[AppmeshRouteSpecHttp2RouteTimeout, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8d7e49927c80f4f357f3891371be93458b355f09bb65fe825365c9b3346d8b1(
    *,
    weighted_target: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppmeshRouteSpecHttp2RouteActionWeightedTarget, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99fd4f7e43a75c4373b5a94d2629524894330aaa5c477973323c30f4d23cb56f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e048c5fa04ddd1e25aea9539beee5eddffd491bb5b6ef9fe3c21ed0ed08bc1b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppmeshRouteSpecHttp2RouteActionWeightedTarget, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__062852739e47f8b1f6eaa5700d16a415e02da52ca2f40e828d138edf8c3a0771(
    value: typing.Optional[AppmeshRouteSpecHttp2RouteAction],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__397cfc70162e4fb72debc1df1571f6cd4c63d8dfe62c19e4fb3ecb6051f259d1(
    *,
    virtual_node: builtins.str,
    weight: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__981bd1d6b26e89c40999714d43d81fc08a2800495d4aa6bf8989fab5c3dc173a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91c3e0cec88bf185dfd278eef763a1a0bc36fbeccf793de9ce252a380bc4b7f6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e564b010037706ce4fb16a2187d19716cc3d5a98ae9623f825c9051803dabbe5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22f42c7e43716d6606830fa263fe062da70be2a2e9e2ce866a8c0d80510705a2(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a0e26de173c21d8688ad24ce532532be7eaed193b8f2c45a0efc9d3f4ee9aaf(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3ebe33cb8447f0c5f873b23ecb07efa312577b9d9af033fd0158b69b19c9ae4(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshRouteSpecHttp2RouteActionWeightedTarget]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d47ffb0f97bb7b00ed3423c1379ce82108dd7fc5133e4e7a9243c3698ae0a9e7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c53ca54115396c5596a578267564e960096216cb0499936dc3453c2c5622c087(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f148924bc57722f24b64917027a22bcd399af39eb9e74b4733b2b12922726a6f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__125f0fd8030593eccd25fe4a84c33200a69f775a7bba52ec7e293aa23294b0fb(
    value: typing.Optional[typing.Union[AppmeshRouteSpecHttp2RouteActionWeightedTarget, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e1e4a7787fdac3df0bb347da487fb1a7be79d5b7469d5c8e7903017432d960c(
    *,
    prefix: builtins.str,
    header: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppmeshRouteSpecHttp2RouteMatchHeader, typing.Dict[builtins.str, typing.Any]]]]] = None,
    method: typing.Optional[builtins.str] = None,
    scheme: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2beaf0e848e50aaf4df42e71b85f2735261d1a51f147fef3324c20fb5270fe9f(
    *,
    name: builtins.str,
    invert: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    match: typing.Optional[typing.Union[AppmeshRouteSpecHttp2RouteMatchHeaderMatch, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fd094798cfa42c31f41f2911fed3dadd0c5f0212c6a863c7848779ca79e28c4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__136af7957632e4adbafeb831629647e0aadb11d10273f05ceee2ed3bec67e795(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8284074049b564a673928abcb6b81b25dde47cb2e5e6d636e3a95f73e434148e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01db0d9f1773dc0c0fa579d7a04bba4e48051dbc9f160515bc586d087a310a77(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3eaa99e1445939e0a7b0ff8962f44cdf60f34e7ac8213d3855fe4151cf852668(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__695fe79caf6b5d5e7eb0f1cdf5eb76be1748eadba40c3c17a377f63da297bb7d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshRouteSpecHttp2RouteMatchHeader]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a67d4350b1f3cbeed243d003152d020d4591979a79e0f82874a17ee7bf269d3(
    *,
    exact: typing.Optional[builtins.str] = None,
    prefix: typing.Optional[builtins.str] = None,
    range: typing.Optional[typing.Union[AppmeshRouteSpecHttp2RouteMatchHeaderMatchRange, typing.Dict[builtins.str, typing.Any]]] = None,
    regex: typing.Optional[builtins.str] = None,
    suffix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__922b42fc54d355a4fa2dd89129fa3f96538ec8b313e876b54a0bf787154f58bf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d448d5de33989879bc9e8384d0047cb535659a85b2a441f6ef7937186fdac42(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4aa34562b828b58f744061a385537640939185ca703bd7bcdb6643a410ca718d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9d263999f6521d5667d8eef31790e61916e40228e8f47cdffc4e930427e3ef3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60934c430def92249103c1d880bc7983689feffb7fafa9ce6a9c13e9e4b39033(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed9dd0a1697ced419cb2460d220cc500a689a0a4ab79a9cdbcf11e12b2ec8548(
    value: typing.Optional[AppmeshRouteSpecHttp2RouteMatchHeaderMatch],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02748169b133d37a9771e66aecd016cf39d0a8d4daab6a851b784ae2dfb99ba3(
    *,
    end: jsii.Number,
    start: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__100a88147e7d8db81ee4ccc5aea649fbf0412589194fb41558a81ea39796043f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5e66f884bf4b36c7627b04cc23c50df880e1c97952ff265a9faf5c985fccbd1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a01e68e9f3c9ae52ea46c8542fdb06bb0aa0527431876696a40a08abf2b5030b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__603cead9912d3c9fc05836c7e776be4e88fa374941080d7b50efe500ee088afa(
    value: typing.Optional[AppmeshRouteSpecHttp2RouteMatchHeaderMatchRange],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a267518b5da427620073fd230217cec902647239cc4070a4791f6d0f259e3d0b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4545e161673405ee2e2158fe7a3587de7b74d0bf2bb5b814435b77a060b63480(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fc8b81305acdaee87a7d4f2f304f810c2505e361cce8b6a2e5eb19eae47a87e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddecde5e789ff797bf73abea161fe7668aef5e05191bcb128091bb360f9ec202(
    value: typing.Optional[typing.Union[AppmeshRouteSpecHttp2RouteMatchHeader, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0b2c4408b1c88365a9e1c0453fd13fd41a96e1e57581d2667e015766745135c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc8c5b3f2a9758e385d30bfa3743abd71d3b4070f1aa3c4c9ca0f5d38948f872(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppmeshRouteSpecHttp2RouteMatchHeader, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96c852759f07c09eee72c811f20cecce7f1174cced5363194b7afd583c2c2fe9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85235154423c3bae5aa742297b05352186e9fb8977d58ce77602901ae6eb39d7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad2c1a87b59767990ecf2a2f32d185f67e1c18e6ebb09fb5c322253d83917aec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca4cc450a91c77d2face5e65b9490834773296bd099521bac3cdfaf3fe8daeb0(
    value: typing.Optional[AppmeshRouteSpecHttp2RouteMatch],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__345d4bc70ebc842b2d8c0f1826d5f0743f3746419e07fc1d72649a622a9bcb63(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9398555ce9ed23de9f9f95611fb283f48a2107e79529b95e82210e39518e1eaa(
    value: typing.Optional[AppmeshRouteSpecHttp2Route],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e04c19daa1fcd01e4f60111b47cb1be9c88ef354a7b1497983a79163be54ccc(
    *,
    max_retries: jsii.Number,
    per_retry_timeout: typing.Union[AppmeshRouteSpecHttp2RouteRetryPolicyPerRetryTimeout, typing.Dict[builtins.str, typing.Any]],
    http_retry_events: typing.Optional[typing.Sequence[builtins.str]] = None,
    tcp_retry_events: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f96ce08da5a81b1686dc979947fcce837a2a25158489aee8fa8d2e67496d404(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c18944586ed94bfccacbfa5d5d1cc5b3193c190591f7ddc69e161988b91ab593(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f58530461ea6b9e2e3af164e0dac77008a32e89b1a0c5d9627cc9990cd7e31f2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7db79f0804e97326d555b29cd9643db39cc504f9b402df11af6632798ddf4d5c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bde774d9b437b8ddd94522ac73408c790b21c98dfbf816598dfcc263fbf85df2(
    value: typing.Optional[AppmeshRouteSpecHttp2RouteRetryPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a33c40c6893965a22e11b634eb3644d7d6b92944214672e9b36c40d9077600b2(
    *,
    unit: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eea31d6634a3c132c65aa4c33d4eba3ce87c879e6ef900da7481f218ed3afd16(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ee8bc7cfb97bedfd8ca0f2665ce3a8777d4abf5a8d5615257d050b11282d2b5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__264cd7ea83840edd4469e63951fde07b8604826500450630933d2b601c3842f8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f536d908ced8922f8e688a0ade9b5f819cd690b0af3d1ff448a482dac57b2ba(
    value: typing.Optional[AppmeshRouteSpecHttp2RouteRetryPolicyPerRetryTimeout],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b1979de7654603ec4f36af44cc2759c36b36d939b0a3e6d8ce940e7ecb22da2(
    *,
    idle: typing.Optional[typing.Union[AppmeshRouteSpecHttp2RouteTimeoutIdle, typing.Dict[builtins.str, typing.Any]]] = None,
    per_request: typing.Optional[typing.Union[AppmeshRouteSpecHttp2RouteTimeoutPerRequest, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d3da9f62992da5fe9d4d29f3d5565f190ed68e7a65b215692b205a8ee23aea7(
    *,
    unit: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11877cbc3aeab63a70e092e39af826b9830eae1624e6d5eeb7f32f289e760e64(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e79b8994b99f7ac79433b6ba62a39692828e6f395638ea4865ee8f2c45bd5bda(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74f7fbdc6671182bed1677f6a08c1c79cd6bde0a7eddce2d8976b8548329cf56(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30d795b8a4ea2b685a1bfc3cd621ed2b5d15959078fe38c74c98a66c355e5875(
    value: typing.Optional[AppmeshRouteSpecHttp2RouteTimeoutIdle],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a63630c2b4fd81c834b912482b3720cdc93e9a4d2fead11d9cd39aa04ab88a0b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6df5e1ada9f6b5e53c99fc8e1c71fe08fdb44b27af73c1b267b6957ee7c4e0b1(
    value: typing.Optional[AppmeshRouteSpecHttp2RouteTimeout],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d125492cd842c611c1deac99630cb4da0c7e6b11f376a7f7ec87f8c19fe5367(
    *,
    unit: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a282e21af3a1b8e6d588855fa8ad6237e19a6b8e8a40178e3ade5f5c9d30126a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d518750a2c92c77320765c6be0c350a74953765f391deab6a7a35d6989626ab3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__401ce784406dd2825a4b7a7f6c8bd4c46830bcd7d6d60153b82060527bce0ab9(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ea72610c8888c31b7ab3d90cf0d9124d87bd75af72529590c2f7daff2b33220(
    value: typing.Optional[AppmeshRouteSpecHttp2RouteTimeoutPerRequest],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57c5deaf8893249698efef0884d803b84d59f5e4a5212d5bfa829ecfc2d78e7f(
    *,
    action: typing.Union[AppmeshRouteSpecHttpRouteAction, typing.Dict[builtins.str, typing.Any]],
    match: typing.Union[AppmeshRouteSpecHttpRouteMatch, typing.Dict[builtins.str, typing.Any]],
    retry_policy: typing.Optional[typing.Union[AppmeshRouteSpecHttpRouteRetryPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    timeout: typing.Optional[typing.Union[AppmeshRouteSpecHttpRouteTimeout, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__386bf668701dbeed7885549600619a906926097d94d54d63e0f1b138f280272b(
    *,
    weighted_target: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppmeshRouteSpecHttpRouteActionWeightedTarget, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7056d7469d158d8bb3d0324347b468aaad6fcac78c91d078799bd59fa7f92b84(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a66678ec01eed5f77a957e2ce21404282a6c06d8779329a3650231181dd79a7a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppmeshRouteSpecHttpRouteActionWeightedTarget, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a52d7bdbd48ee476495c5491dabe13d67d193354ab35a3a4c424695ff552f9e(
    value: typing.Optional[AppmeshRouteSpecHttpRouteAction],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9cf40cab211901068af6a01ec7f2304f5a8d50d6e3602575558ef92520450b7(
    *,
    virtual_node: builtins.str,
    weight: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__663fb27fc4881bb6392a30c0a8d9c20745e221e9d7711111bc84ff350f460cef(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__078a9b2363dc66bbb2a7d1eb3288df61ccd488d3fd624576df376abb73e815a1(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__778b1fcc221cf85e365755fb57b67877ee4f329cc4163771a8d41504dde6c0bd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b8b6ca11f92cb5d519c9068f8dde1d022dd4c07de6b5336e897115d15c7573f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9899fd205b409d2506a7f8a4e2d8d83ecc8e78d8ce72005d1f2e5b3cadd28711(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c42ff9edc44103a2b96dca27ab17d4ab314641d84dfbf9c6f25c7912ccc45b87(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshRouteSpecHttpRouteActionWeightedTarget]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecc792eb5a42fdfe87449e91eb8e57ceaef1147d6e06b99563b2304227ac103b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e94f232fdffa90647054297ee21c1cb81c2888f7398f1fc5553a2806dc7c43e2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3609f6963e77ba9987ade322f589070be6c17470374fa695daf0f516ae0bf686(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b3d12f16d3e11c24c493a7fffebae86b2b4c526a5f741f8e3aa91d314665127(
    value: typing.Optional[typing.Union[AppmeshRouteSpecHttpRouteActionWeightedTarget, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02694482fb69ad07b28eee14219c70b0eca262df73e17fd18a16a6f62a2aea33(
    *,
    prefix: builtins.str,
    header: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppmeshRouteSpecHttpRouteMatchHeader, typing.Dict[builtins.str, typing.Any]]]]] = None,
    method: typing.Optional[builtins.str] = None,
    scheme: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__082b351fe6ae029a75a33a1a54a0a20004a48a8b4897bd3cde3d6e14750e81be(
    *,
    name: builtins.str,
    invert: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    match: typing.Optional[typing.Union[AppmeshRouteSpecHttpRouteMatchHeaderMatch, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1511daccd74db7420ff36e811ffec3204d66482e3a8bfe9c78112b5826fc2266(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f2fa707e5839bc514bb225a44c3dc1a9210e7cc3ca3cec63901808eceb0ae9d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9391fb7f93da1636c8117173cdbaeff37a560925d7b0606d5fc8d6ff77dade0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2475a8231cccf9f83109e7e9288b8619a4d83f5a6f7d76ee8941bfe569ed99cf(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1712477c9f3580a8fa7a56fff323f7501cc10087234742120fd6b9667f170f45(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab8b4271861118bb4bee80aef9db1bea618e9eca3577d639514604f1d163295f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshRouteSpecHttpRouteMatchHeader]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf6a6906cd192558b397f54208f407dd80a4906e35b3304bc929634f8b42464f(
    *,
    exact: typing.Optional[builtins.str] = None,
    prefix: typing.Optional[builtins.str] = None,
    range: typing.Optional[typing.Union[AppmeshRouteSpecHttpRouteMatchHeaderMatchRange, typing.Dict[builtins.str, typing.Any]]] = None,
    regex: typing.Optional[builtins.str] = None,
    suffix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06d5f9c3e446208714594f484e8563ec24f8bcaf467d9eca1d2aef568d919f73(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0560e26cfa629c000242d6b00adca5eea6d5b28a423811257452574f78a65d0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b048bf8a59aa5e95e20b4006b0871018deb7d0d1b2256fc7d6ef7fb1246fd9a4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c62a6c487db716070f7b75d104abc16cf7d534da2a07522322346c6566ab35a1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__163a33615a76b62710045f3539f6ac447a85e4cb92cfe35405e3f7e930df4ce0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06fb8202e4a14d5d49d07e763062981e9f42b69b2d4308e955fda7dbb25c9980(
    value: typing.Optional[AppmeshRouteSpecHttpRouteMatchHeaderMatch],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05513f2281c9ddefe53cf527c0d489be227b67cc76a4fadff7286e3bfe010fce(
    *,
    end: jsii.Number,
    start: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac36e231361cf417adf8160363e93ddf670b3bd8c16f282d44ae8d8848154913(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e529fee44e952d54ab10c9e21c4231d6b46784defae60787bfb86e47e3826e3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__baf997212d089bb90e3e03750d99664535cefbf39439fa00aaf422215ba5cc96(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a1e84956a8a10d075445a16e85781aecdbc047771a21500bc82e30eef206b69(
    value: typing.Optional[AppmeshRouteSpecHttpRouteMatchHeaderMatchRange],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e23caed84012533c0126c487ae9da3b937753fc456c3f4db9ee1dcbcbc80f05(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__659fed6c4bd84dd46b8333caa91b632f8a8737dc6b469b0bd805b3089d8a60c8(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c23a443c9615cfc114863af8a062696c259acc109bf195600de45c3a69344745(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__959d391742f0c8a92459f02c4fd1d8fd6589626a204009bb24d4a88f210c4cda(
    value: typing.Optional[typing.Union[AppmeshRouteSpecHttpRouteMatchHeader, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c288b676ebdc61f9a877820129b71bdacd590f9a7f6c5f6fa4856f3c2772079(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c564fb7dbbcecd7b6273b5fb18539b57b668c357c5c5c098a99b01d6dedbd75(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppmeshRouteSpecHttpRouteMatchHeader, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2d143759cf06c48d6c3eca5932f85dbf960d2f58312ebcc8d1984e6df643f0c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d1cd2c9874eddde2042167ea5b705a9c8ea58b25924452f6f9ab05e9d65c176(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b40ac02d360ae3cf1bc400c87cdcb60a414b6a128a5f60d1f45d91875a001e86(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1885c9013c5d96e99bbb1e5829436957cb5bfb501edeb910dcd3fb98d8b8ce6a(
    value: typing.Optional[AppmeshRouteSpecHttpRouteMatch],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c0a09ecfeca8dbd493226ce16563c67ef13c4ec94b88e2761a528ddd58a2ff7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55ebdee774000fbdbc63c3050d0ae46b243120f1e5aae1f44c90bcede4549306(
    value: typing.Optional[AppmeshRouteSpecHttpRoute],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__436ad581bbd5769a2180ae91769d35a1dca23e91a73cc0d39dbc8494eb1ad0a1(
    *,
    max_retries: jsii.Number,
    per_retry_timeout: typing.Union[AppmeshRouteSpecHttpRouteRetryPolicyPerRetryTimeout, typing.Dict[builtins.str, typing.Any]],
    http_retry_events: typing.Optional[typing.Sequence[builtins.str]] = None,
    tcp_retry_events: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5d04ecdebbd2995b68da7643d85457d73fed685dfbee65ba453a9c517a970f6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be6d53cb01f3090dd019b747930cc73654d3740377fe589ddffaff6e0318d53a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13e087ce98488e41fe439883672e41ba2ae005bd3692ec4e4d5bd39105ea29cc(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6649e3f70e8d198b6538832cda0f5f68ad7a7a4205dd55448181c76c6e2fa5b5(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__158d1025d473ab3441bf8d565a3ee7a792c8faf411461f52ce497f88b5c897bb(
    value: typing.Optional[AppmeshRouteSpecHttpRouteRetryPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__565654f302707c9532c7d3bbab3bd58eda3341e9ca6f6024e76b53c1697bbe0a(
    *,
    unit: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__978716900366b440a14b259c7b7dc1f58c95059becb4799632ea2ec06be62552(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09d9566764c2c069f1fa3ee214de8ef25fd7839c088f23ef4e9774cd2b712361(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d118e9bbd8c55366436deb8b8716efd5459f5d1c72e2b889e4f4e580c6a23ed8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__869da9d41e251329165c1130a0c5eb8714fbc95e6ccbefdbbc829130d9f760df(
    value: typing.Optional[AppmeshRouteSpecHttpRouteRetryPolicyPerRetryTimeout],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be878e9b92483dd2da5c3c41f54fa59e341c1da0f9cc5538c2f74a880c845b92(
    *,
    idle: typing.Optional[typing.Union[AppmeshRouteSpecHttpRouteTimeoutIdle, typing.Dict[builtins.str, typing.Any]]] = None,
    per_request: typing.Optional[typing.Union[AppmeshRouteSpecHttpRouteTimeoutPerRequest, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a42620801eb7bd0947cc040a304c2af623a4994e7dd71b4cae4438581642a98c(
    *,
    unit: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7baee180bf42ed71d143c7e5c0be979ac5c495c1a3537abb7f5f7acb94c98a6a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4479889b3411966c02211e95651b9232cd957bdc2d89ef2748b1267f6016ea1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__124efc1dee7ab3e9ba483ab9205afe346dd57032951773b1b28ca80dfee97e2c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33d30176d9da941fa7a2b9b5780f190331e574c3cbe3f71eb388317e35ee9903(
    value: typing.Optional[AppmeshRouteSpecHttpRouteTimeoutIdle],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02ac65bd2ef7b67b1e5e3a1e3a86293d94495619818fee59ad6c946bdaf610c2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71a0d0ba90520917c89d798564d3cce244c934dbc6cfe706c2b03a3a6299632d(
    value: typing.Optional[AppmeshRouteSpecHttpRouteTimeout],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3e3040425e233ee3dec01128e59ecc2c2c34f9ef6fa3f47534adf49b2d26596(
    *,
    unit: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6226041df88ea714699ad5975bdc6fd96bc3d38b41163ab1cec55fde496f4357(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d57371033143ce6d52c750774dc10a4662616bdd611f099286a2eaf146312e4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1edd276349dfce407daec1c957d9243200be10de2e69b62ff81c32b0fdba7de0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__261b67e5a9af87843ce2caeea972b3c8e614f5c924dd78b0dca9553ded971c04(
    value: typing.Optional[AppmeshRouteSpecHttpRouteTimeoutPerRequest],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b20c0e00f6c14f4493396523001dfaa2dac10e5b9105638f293dc750b1abf947(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a26b05b6e6d849e05a9a31da5265ae78b193cc01241c08a17366e66216c1c1a6(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b2aeec8f3d198c29ae4cb119f5d33084729ee163ba89aa53be8794c74415cb9(
    value: typing.Optional[AppmeshRouteSpec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e67d4456d9adbd773cc9cd086521304a10dec5b95e5a6ffe4a41881093db4c6(
    *,
    action: typing.Union[AppmeshRouteSpecTcpRouteAction, typing.Dict[builtins.str, typing.Any]],
    timeout: typing.Optional[typing.Union[AppmeshRouteSpecTcpRouteTimeout, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1076e1910326b723f27a6aac58a87f59c2121ec33747c100c19d7545b4c3caa(
    *,
    weighted_target: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppmeshRouteSpecTcpRouteActionWeightedTarget, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1b9ca3e1f161d1262a8444663d1ae925c814eac3c695a9407b3576b8caa34f0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__103d24140ea8c788fd5a415bef38fef6f80460a5b15eb9950e83118aa10dd737(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AppmeshRouteSpecTcpRouteActionWeightedTarget, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__124b2e35c2cc3931c3a72aa33e0666d4fb710c0151b3f31d38fd846794db4e9a(
    value: typing.Optional[AppmeshRouteSpecTcpRouteAction],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f979db187b8a1a7c026f15b4a80754e8f6dcca94e494812d53e8d6ae23429cc(
    *,
    virtual_node: builtins.str,
    weight: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcb032d707592311aa26d5f8a3471a2270159b5b475f892d33566562dbded9e5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcf10b7402476354ded397d208d9fb471193e1be571d6504115965ca8dd0bf6e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c48a8a5c2c517cd7fdada8437f63ac9ae190a11e9d8674eeecff2de24b8238ca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea816f19f763095d9b0a26961da1a6def0b854abb45ef991becfc5430f8667c6(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb0ba545a940b71b1c777b7fd1c193add494526999a5233720ae3a86ff524728(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__491eb8f690fd5f7e7f13d7e4a678717e4d4275819a5758925f6a24a4c3e0d841(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AppmeshRouteSpecTcpRouteActionWeightedTarget]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d902b39373f26a10a7c52afb12c60e5bce8d6e32843fdad9c0aa9706c76dfd0c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9eda045394fbf3e4a26c5b3ea2d9552c4986ef21f98c422b2b8042643f69d583(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6594d885ef76f9f115b589ab0dd35bc30a76e632f927bd3d044050f77b7e14b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__505eedec42acadc30b44f27d1e25c5ca7931e77ac8b7430907c2af1a4a2c833d(
    value: typing.Optional[typing.Union[AppmeshRouteSpecTcpRouteActionWeightedTarget, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0fe9ef5234bb4b2bbb67418055f0803c33b2f34e5ae30c9a94ac1d4180d941d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6ff1cb720c127ea1b781a6638e9d44fb99691910f8df7bba5a24d28acc9d764(
    value: typing.Optional[AppmeshRouteSpecTcpRoute],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4835b958e4cc9fc253e55d0e4d5a472402e08d6e64ec415ba3dda105832cf0ca(
    *,
    idle: typing.Optional[typing.Union[AppmeshRouteSpecTcpRouteTimeoutIdle, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d46739c04a8e91b6a64772490fb5905fff467af3ef33ae921a3ee9e012ff8db1(
    *,
    unit: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e71fbaddbab487c92020d0f63aca2612d84b7dee30d8a7582b5e59d28d8b469c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63012fdba6dd89e2217f8e062695fa734c8181f5cbfbc12470d8445913192a0b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5442438154fce1fa144ad9991ab46d66f1bd78c9a2f187af64ff293b0d86f7f4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9c1c0b882e260773a59342af0fb9f28dbc798938a8d78621411ae137f49f8fc(
    value: typing.Optional[AppmeshRouteSpecTcpRouteTimeoutIdle],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f11c0807e72d10bbfaa2afbe4ecc9fa700a523e4268b1b5ce405ceda9d066eda(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1570617cdb5d4703ffd7b7d2840b5fbcb2b81746d29ce3e8cdc39c2f4f43c273(
    value: typing.Optional[AppmeshRouteSpecTcpRouteTimeout],
) -> None:
    """Type checking stubs"""
    pass
