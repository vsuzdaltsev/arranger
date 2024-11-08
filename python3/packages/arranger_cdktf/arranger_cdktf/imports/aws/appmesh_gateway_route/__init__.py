'''
# `aws_appmesh_gateway_route`

Refer to the Terraform Registory for docs: [`aws_appmesh_gateway_route`](https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route).
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


class AppmeshGatewayRoute(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRoute",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route aws_appmesh_gateway_route}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        mesh_name: builtins.str,
        name: builtins.str,
        spec: typing.Union["AppmeshGatewayRouteSpec", typing.Dict[builtins.str, typing.Any]],
        virtual_gateway_name: builtins.str,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route aws_appmesh_gateway_route} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param mesh_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#mesh_name AppmeshGatewayRoute#mesh_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#name AppmeshGatewayRoute#name}.
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#spec AppmeshGatewayRoute#spec}
        :param virtual_gateway_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_gateway_name AppmeshGatewayRoute#virtual_gateway_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#id AppmeshGatewayRoute#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mesh_owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#mesh_owner AppmeshGatewayRoute#mesh_owner}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#tags AppmeshGatewayRoute#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#tags_all AppmeshGatewayRoute#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e60d33798b71a225a7d1f2942dd246a1100cc356a144a34f58197f1ac05aabbc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AppmeshGatewayRouteConfig(
            mesh_name=mesh_name,
            name=name,
            spec=spec,
            virtual_gateway_name=virtual_gateway_name,
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
        grpc_route: typing.Optional[typing.Union["AppmeshGatewayRouteSpecGrpcRoute", typing.Dict[builtins.str, typing.Any]]] = None,
        http2_route: typing.Optional[typing.Union["AppmeshGatewayRouteSpecHttp2Route", typing.Dict[builtins.str, typing.Any]]] = None,
        http_route: typing.Optional[typing.Union["AppmeshGatewayRouteSpecHttpRoute", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param grpc_route: grpc_route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#grpc_route AppmeshGatewayRoute#grpc_route}
        :param http2_route: http2_route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#http2_route AppmeshGatewayRoute#http2_route}
        :param http_route: http_route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#http_route AppmeshGatewayRoute#http_route}
        '''
        value = AppmeshGatewayRouteSpec(
            grpc_route=grpc_route, http2_route=http2_route, http_route=http_route
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
    def spec(self) -> "AppmeshGatewayRouteSpecOutputReference":
        return typing.cast("AppmeshGatewayRouteSpecOutputReference", jsii.get(self, "spec"))

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
    def spec_input(self) -> typing.Optional["AppmeshGatewayRouteSpec"]:
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpec"], jsii.get(self, "specInput"))

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
    @jsii.member(jsii_name="virtualGatewayNameInput")
    def virtual_gateway_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualGatewayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e587e325912359a1611f4133e921b36e8cebb9fd0cdf584a0f2eab51e08c625)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="meshName")
    def mesh_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "meshName"))

    @mesh_name.setter
    def mesh_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3031a49d4ce416efe28766b7a5ae2908c34a138d87eb0f346f842e158415413b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "meshName", value)

    @builtins.property
    @jsii.member(jsii_name="meshOwner")
    def mesh_owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "meshOwner"))

    @mesh_owner.setter
    def mesh_owner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce46ffdcd8eefcd444df38ae445888b443c90276232e84f272b7d849bbf19e74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "meshOwner", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97873d709654eab8a9700dabd17d36113957588483fb81714ce560fb10042974)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ffba99add67cf77e231c7d1476e5bc361e79a7b7b01676ac346ac5d17049008)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3822414f6a8bd589a8e153c2ec4155bdde84b8d25db5af17b30e58ebc54667d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)

    @builtins.property
    @jsii.member(jsii_name="virtualGatewayName")
    def virtual_gateway_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualGatewayName"))

    @virtual_gateway_name.setter
    def virtual_gateway_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6970ae0c3b698185d3698bf6fb594a016fe48662217d461ae91a2093f20b5855)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualGatewayName", value)


@jsii.data_type(
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteConfig",
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
        "virtual_gateway_name": "virtualGatewayName",
        "id": "id",
        "mesh_owner": "meshOwner",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class AppmeshGatewayRouteConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        spec: typing.Union["AppmeshGatewayRouteSpec", typing.Dict[builtins.str, typing.Any]],
        virtual_gateway_name: builtins.str,
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
        :param mesh_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#mesh_name AppmeshGatewayRoute#mesh_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#name AppmeshGatewayRoute#name}.
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#spec AppmeshGatewayRoute#spec}
        :param virtual_gateway_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_gateway_name AppmeshGatewayRoute#virtual_gateway_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#id AppmeshGatewayRoute#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mesh_owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#mesh_owner AppmeshGatewayRoute#mesh_owner}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#tags AppmeshGatewayRoute#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#tags_all AppmeshGatewayRoute#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(spec, dict):
            spec = AppmeshGatewayRouteSpec(**spec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3eedc0182e1c2f6974092d2f3718ffe056cc08bc85cd4ad8a14c5b1e0c1dfb4)
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
            check_type(argname="argument virtual_gateway_name", value=virtual_gateway_name, expected_type=type_hints["virtual_gateway_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument mesh_owner", value=mesh_owner, expected_type=type_hints["mesh_owner"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "mesh_name": mesh_name,
            "name": name,
            "spec": spec,
            "virtual_gateway_name": virtual_gateway_name,
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#mesh_name AppmeshGatewayRoute#mesh_name}.'''
        result = self._values.get("mesh_name")
        assert result is not None, "Required property 'mesh_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#name AppmeshGatewayRoute#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def spec(self) -> "AppmeshGatewayRouteSpec":
        '''spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#spec AppmeshGatewayRoute#spec}
        '''
        result = self._values.get("spec")
        assert result is not None, "Required property 'spec' is missing"
        return typing.cast("AppmeshGatewayRouteSpec", result)

    @builtins.property
    def virtual_gateway_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_gateway_name AppmeshGatewayRoute#virtual_gateway_name}.'''
        result = self._values.get("virtual_gateway_name")
        assert result is not None, "Required property 'virtual_gateway_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#id AppmeshGatewayRoute#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mesh_owner(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#mesh_owner AppmeshGatewayRoute#mesh_owner}.'''
        result = self._values.get("mesh_owner")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#tags AppmeshGatewayRoute#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#tags_all AppmeshGatewayRoute#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpec",
    jsii_struct_bases=[],
    name_mapping={
        "grpc_route": "grpcRoute",
        "http2_route": "http2Route",
        "http_route": "httpRoute",
    },
)
class AppmeshGatewayRouteSpec:
    def __init__(
        self,
        *,
        grpc_route: typing.Optional[typing.Union["AppmeshGatewayRouteSpecGrpcRoute", typing.Dict[builtins.str, typing.Any]]] = None,
        http2_route: typing.Optional[typing.Union["AppmeshGatewayRouteSpecHttp2Route", typing.Dict[builtins.str, typing.Any]]] = None,
        http_route: typing.Optional[typing.Union["AppmeshGatewayRouteSpecHttpRoute", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param grpc_route: grpc_route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#grpc_route AppmeshGatewayRoute#grpc_route}
        :param http2_route: http2_route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#http2_route AppmeshGatewayRoute#http2_route}
        :param http_route: http_route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#http_route AppmeshGatewayRoute#http_route}
        '''
        if isinstance(grpc_route, dict):
            grpc_route = AppmeshGatewayRouteSpecGrpcRoute(**grpc_route)
        if isinstance(http2_route, dict):
            http2_route = AppmeshGatewayRouteSpecHttp2Route(**http2_route)
        if isinstance(http_route, dict):
            http_route = AppmeshGatewayRouteSpecHttpRoute(**http_route)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ee41fbde5295cf1ffa05c763927f1dc70e4bbba7dea173815b1ac1f01f45f40)
            check_type(argname="argument grpc_route", value=grpc_route, expected_type=type_hints["grpc_route"])
            check_type(argname="argument http2_route", value=http2_route, expected_type=type_hints["http2_route"])
            check_type(argname="argument http_route", value=http_route, expected_type=type_hints["http_route"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if grpc_route is not None:
            self._values["grpc_route"] = grpc_route
        if http2_route is not None:
            self._values["http2_route"] = http2_route
        if http_route is not None:
            self._values["http_route"] = http_route

    @builtins.property
    def grpc_route(self) -> typing.Optional["AppmeshGatewayRouteSpecGrpcRoute"]:
        '''grpc_route block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#grpc_route AppmeshGatewayRoute#grpc_route}
        '''
        result = self._values.get("grpc_route")
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecGrpcRoute"], result)

    @builtins.property
    def http2_route(self) -> typing.Optional["AppmeshGatewayRouteSpecHttp2Route"]:
        '''http2_route block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#http2_route AppmeshGatewayRoute#http2_route}
        '''
        result = self._values.get("http2_route")
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecHttp2Route"], result)

    @builtins.property
    def http_route(self) -> typing.Optional["AppmeshGatewayRouteSpecHttpRoute"]:
        '''http_route block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#http_route AppmeshGatewayRoute#http_route}
        '''
        result = self._values.get("http_route")
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecHttpRoute"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecGrpcRoute",
    jsii_struct_bases=[],
    name_mapping={"action": "action", "match": "match"},
)
class AppmeshGatewayRouteSpecGrpcRoute:
    def __init__(
        self,
        *,
        action: typing.Union["AppmeshGatewayRouteSpecGrpcRouteAction", typing.Dict[builtins.str, typing.Any]],
        match: typing.Union["AppmeshGatewayRouteSpecGrpcRouteMatch", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#action AppmeshGatewayRoute#action}
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#match AppmeshGatewayRoute#match}
        '''
        if isinstance(action, dict):
            action = AppmeshGatewayRouteSpecGrpcRouteAction(**action)
        if isinstance(match, dict):
            match = AppmeshGatewayRouteSpecGrpcRouteMatch(**match)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7dbb0f76051a578abee8e324f92b80a3d18851d7ef60ba935e6f5490eaa5313)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument match", value=match, expected_type=type_hints["match"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action": action,
            "match": match,
        }

    @builtins.property
    def action(self) -> "AppmeshGatewayRouteSpecGrpcRouteAction":
        '''action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#action AppmeshGatewayRoute#action}
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast("AppmeshGatewayRouteSpecGrpcRouteAction", result)

    @builtins.property
    def match(self) -> "AppmeshGatewayRouteSpecGrpcRouteMatch":
        '''match block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#match AppmeshGatewayRoute#match}
        '''
        result = self._values.get("match")
        assert result is not None, "Required property 'match' is missing"
        return typing.cast("AppmeshGatewayRouteSpecGrpcRouteMatch", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecGrpcRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecGrpcRouteAction",
    jsii_struct_bases=[],
    name_mapping={"target": "target"},
)
class AppmeshGatewayRouteSpecGrpcRouteAction:
    def __init__(
        self,
        *,
        target: typing.Union["AppmeshGatewayRouteSpecGrpcRouteActionTarget", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param target: target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#target AppmeshGatewayRoute#target}
        '''
        if isinstance(target, dict):
            target = AppmeshGatewayRouteSpecGrpcRouteActionTarget(**target)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d1daf217b0f498e434ddc5e1298c8be353963d4edf2c5cdfff3424f6613a9c7)
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "target": target,
        }

    @builtins.property
    def target(self) -> "AppmeshGatewayRouteSpecGrpcRouteActionTarget":
        '''target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#target AppmeshGatewayRoute#target}
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast("AppmeshGatewayRouteSpecGrpcRouteActionTarget", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecGrpcRouteAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshGatewayRouteSpecGrpcRouteActionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecGrpcRouteActionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5b27f7d594f24628476be98172eba889c51755fcb01c01bd41444427aee06086)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTarget")
    def put_target(
        self,
        *,
        virtual_service: typing.Union["AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualService", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param virtual_service: virtual_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_service AppmeshGatewayRoute#virtual_service}
        '''
        value = AppmeshGatewayRouteSpecGrpcRouteActionTarget(
            virtual_service=virtual_service
        )

        return typing.cast(None, jsii.invoke(self, "putTarget", [value]))

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> "AppmeshGatewayRouteSpecGrpcRouteActionTargetOutputReference":
        return typing.cast("AppmeshGatewayRouteSpecGrpcRouteActionTargetOutputReference", jsii.get(self, "target"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(
        self,
    ) -> typing.Optional["AppmeshGatewayRouteSpecGrpcRouteActionTarget"]:
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecGrpcRouteActionTarget"], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshGatewayRouteSpecGrpcRouteAction]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecGrpcRouteAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecGrpcRouteAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d43425c5a796c29e40ee45734ddf79929aae88b0dd1f83a84f02f7917b57af64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecGrpcRouteActionTarget",
    jsii_struct_bases=[],
    name_mapping={"virtual_service": "virtualService"},
)
class AppmeshGatewayRouteSpecGrpcRouteActionTarget:
    def __init__(
        self,
        *,
        virtual_service: typing.Union["AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualService", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param virtual_service: virtual_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_service AppmeshGatewayRoute#virtual_service}
        '''
        if isinstance(virtual_service, dict):
            virtual_service = AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualService(**virtual_service)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d0db52090970c424d5719e8d5c3315c0bfe68a086b5fc8f40242af8c129120e)
            check_type(argname="argument virtual_service", value=virtual_service, expected_type=type_hints["virtual_service"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "virtual_service": virtual_service,
        }

    @builtins.property
    def virtual_service(
        self,
    ) -> "AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualService":
        '''virtual_service block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_service AppmeshGatewayRoute#virtual_service}
        '''
        result = self._values.get("virtual_service")
        assert result is not None, "Required property 'virtual_service' is missing"
        return typing.cast("AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualService", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecGrpcRouteActionTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshGatewayRouteSpecGrpcRouteActionTargetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecGrpcRouteActionTargetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__164b7379690bfb045ce9d8cbf53011b9641d574f9e46459a3a18239e98cc3868)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putVirtualService")
    def put_virtual_service(self, *, virtual_service_name: builtins.str) -> None:
        '''
        :param virtual_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_service_name AppmeshGatewayRoute#virtual_service_name}.
        '''
        value = AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualService(
            virtual_service_name=virtual_service_name
        )

        return typing.cast(None, jsii.invoke(self, "putVirtualService", [value]))

    @builtins.property
    @jsii.member(jsii_name="virtualService")
    def virtual_service(
        self,
    ) -> "AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualServiceOutputReference":
        return typing.cast("AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualServiceOutputReference", jsii.get(self, "virtualService"))

    @builtins.property
    @jsii.member(jsii_name="virtualServiceInput")
    def virtual_service_input(
        self,
    ) -> typing.Optional["AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualService"]:
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualService"], jsii.get(self, "virtualServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecGrpcRouteActionTarget]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecGrpcRouteActionTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecGrpcRouteActionTarget],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__696e5f59073b72d6ff5bc0d7ce618d26e949655ef7193c1e8aee0980eb6b529d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualService",
    jsii_struct_bases=[],
    name_mapping={"virtual_service_name": "virtualServiceName"},
)
class AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualService:
    def __init__(self, *, virtual_service_name: builtins.str) -> None:
        '''
        :param virtual_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_service_name AppmeshGatewayRoute#virtual_service_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41b4e7df913f68fd6b67a3783be159e2117f5821d73d50caa65320a5eb647d85)
            check_type(argname="argument virtual_service_name", value=virtual_service_name, expected_type=type_hints["virtual_service_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "virtual_service_name": virtual_service_name,
        }

    @builtins.property
    def virtual_service_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_service_name AppmeshGatewayRoute#virtual_service_name}.'''
        result = self._values.get("virtual_service_name")
        assert result is not None, "Required property 'virtual_service_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualServiceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualServiceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bbadf1254c179b7811d557075da006b5b05098b904cf5e07d462164a9a67f6a3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

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
            type_hints = typing.get_type_hints(_typecheckingstub__3c9fe8ddb636bb6c6cd0ede052b9391baa204bd0ba15257eefc66f6f069c685c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualServiceName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualService]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualService], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualService],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6f373a92aac69d2a38d10d097f05cd342f1fadd2636d59b72848be2ecffbe29)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecGrpcRouteMatch",
    jsii_struct_bases=[],
    name_mapping={"service_name": "serviceName"},
)
class AppmeshGatewayRouteSpecGrpcRouteMatch:
    def __init__(self, *, service_name: builtins.str) -> None:
        '''
        :param service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#service_name AppmeshGatewayRoute#service_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__592a13e8cf7d8b7449cb676b6a5f804bd709019f7dfe8a4dd8251e1b272b6257)
            check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "service_name": service_name,
        }

    @builtins.property
    def service_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#service_name AppmeshGatewayRoute#service_name}.'''
        result = self._values.get("service_name")
        assert result is not None, "Required property 'service_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecGrpcRouteMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshGatewayRouteSpecGrpcRouteMatchOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecGrpcRouteMatchOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__450c94714afd1336eba6e944237cd7fe275eac61e64f7e26ac377ed54a0ba0d1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="serviceNameInput")
    def service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceName"))

    @service_name.setter
    def service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8bcb67d2a5144e9def022b33b6c7da088acf9c975ffb6d9a98ffd310154b2a40)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshGatewayRouteSpecGrpcRouteMatch]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecGrpcRouteMatch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecGrpcRouteMatch],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__713a6f086d58c1ea51ce6c5b11e30fb64e380ba5b4a219db8d3267d60224250f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshGatewayRouteSpecGrpcRouteOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecGrpcRouteOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5d56eeefeb64483322d2ec8c56907216621fdaf8470cdebc7391008d6944d647)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAction")
    def put_action(
        self,
        *,
        target: typing.Union[AppmeshGatewayRouteSpecGrpcRouteActionTarget, typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param target: target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#target AppmeshGatewayRoute#target}
        '''
        value = AppmeshGatewayRouteSpecGrpcRouteAction(target=target)

        return typing.cast(None, jsii.invoke(self, "putAction", [value]))

    @jsii.member(jsii_name="putMatch")
    def put_match(self, *, service_name: builtins.str) -> None:
        '''
        :param service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#service_name AppmeshGatewayRoute#service_name}.
        '''
        value = AppmeshGatewayRouteSpecGrpcRouteMatch(service_name=service_name)

        return typing.cast(None, jsii.invoke(self, "putMatch", [value]))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> AppmeshGatewayRouteSpecGrpcRouteActionOutputReference:
        return typing.cast(AppmeshGatewayRouteSpecGrpcRouteActionOutputReference, jsii.get(self, "action"))

    @builtins.property
    @jsii.member(jsii_name="match")
    def match(self) -> AppmeshGatewayRouteSpecGrpcRouteMatchOutputReference:
        return typing.cast(AppmeshGatewayRouteSpecGrpcRouteMatchOutputReference, jsii.get(self, "match"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[AppmeshGatewayRouteSpecGrpcRouteAction]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecGrpcRouteAction], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="matchInput")
    def match_input(self) -> typing.Optional[AppmeshGatewayRouteSpecGrpcRouteMatch]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecGrpcRouteMatch], jsii.get(self, "matchInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshGatewayRouteSpecGrpcRoute]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecGrpcRoute], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecGrpcRoute],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3599e43427c491b43fae0e0618ee02dc803f15421117f826178815522f2e9bee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttp2Route",
    jsii_struct_bases=[],
    name_mapping={"action": "action", "match": "match"},
)
class AppmeshGatewayRouteSpecHttp2Route:
    def __init__(
        self,
        *,
        action: typing.Union["AppmeshGatewayRouteSpecHttp2RouteAction", typing.Dict[builtins.str, typing.Any]],
        match: typing.Union["AppmeshGatewayRouteSpecHttp2RouteMatch", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#action AppmeshGatewayRoute#action}
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#match AppmeshGatewayRoute#match}
        '''
        if isinstance(action, dict):
            action = AppmeshGatewayRouteSpecHttp2RouteAction(**action)
        if isinstance(match, dict):
            match = AppmeshGatewayRouteSpecHttp2RouteMatch(**match)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dc3d5d7beacd2020c67bb018d60de37fb98a8885bb6ea9e87e81bb12feff5a4)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument match", value=match, expected_type=type_hints["match"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action": action,
            "match": match,
        }

    @builtins.property
    def action(self) -> "AppmeshGatewayRouteSpecHttp2RouteAction":
        '''action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#action AppmeshGatewayRoute#action}
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast("AppmeshGatewayRouteSpecHttp2RouteAction", result)

    @builtins.property
    def match(self) -> "AppmeshGatewayRouteSpecHttp2RouteMatch":
        '''match block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#match AppmeshGatewayRoute#match}
        '''
        result = self._values.get("match")
        assert result is not None, "Required property 'match' is missing"
        return typing.cast("AppmeshGatewayRouteSpecHttp2RouteMatch", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecHttp2Route(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttp2RouteAction",
    jsii_struct_bases=[],
    name_mapping={"target": "target", "rewrite": "rewrite"},
)
class AppmeshGatewayRouteSpecHttp2RouteAction:
    def __init__(
        self,
        *,
        target: typing.Union["AppmeshGatewayRouteSpecHttp2RouteActionTarget", typing.Dict[builtins.str, typing.Any]],
        rewrite: typing.Optional[typing.Union["AppmeshGatewayRouteSpecHttp2RouteActionRewrite", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param target: target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#target AppmeshGatewayRoute#target}
        :param rewrite: rewrite block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#rewrite AppmeshGatewayRoute#rewrite}
        '''
        if isinstance(target, dict):
            target = AppmeshGatewayRouteSpecHttp2RouteActionTarget(**target)
        if isinstance(rewrite, dict):
            rewrite = AppmeshGatewayRouteSpecHttp2RouteActionRewrite(**rewrite)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__879f60664815ac30c796c8f1023f6b22be62e393a692afe9cb5fd7a854239c91)
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument rewrite", value=rewrite, expected_type=type_hints["rewrite"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "target": target,
        }
        if rewrite is not None:
            self._values["rewrite"] = rewrite

    @builtins.property
    def target(self) -> "AppmeshGatewayRouteSpecHttp2RouteActionTarget":
        '''target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#target AppmeshGatewayRoute#target}
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast("AppmeshGatewayRouteSpecHttp2RouteActionTarget", result)

    @builtins.property
    def rewrite(
        self,
    ) -> typing.Optional["AppmeshGatewayRouteSpecHttp2RouteActionRewrite"]:
        '''rewrite block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#rewrite AppmeshGatewayRoute#rewrite}
        '''
        result = self._values.get("rewrite")
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecHttp2RouteActionRewrite"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecHttp2RouteAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshGatewayRouteSpecHttp2RouteActionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttp2RouteActionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d714c07e1cb1c488d7f1980334607e1681a7ffce93c8faa054819443c3b69211)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRewrite")
    def put_rewrite(
        self,
        *,
        hostname: typing.Optional[typing.Union["AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostname", typing.Dict[builtins.str, typing.Any]]] = None,
        prefix: typing.Optional[typing.Union["AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefix", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param hostname: hostname block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#hostname AppmeshGatewayRoute#hostname}
        :param prefix: prefix block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#prefix AppmeshGatewayRoute#prefix}
        '''
        value = AppmeshGatewayRouteSpecHttp2RouteActionRewrite(
            hostname=hostname, prefix=prefix
        )

        return typing.cast(None, jsii.invoke(self, "putRewrite", [value]))

    @jsii.member(jsii_name="putTarget")
    def put_target(
        self,
        *,
        virtual_service: typing.Union["AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualService", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param virtual_service: virtual_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_service AppmeshGatewayRoute#virtual_service}
        '''
        value = AppmeshGatewayRouteSpecHttp2RouteActionTarget(
            virtual_service=virtual_service
        )

        return typing.cast(None, jsii.invoke(self, "putTarget", [value]))

    @jsii.member(jsii_name="resetRewrite")
    def reset_rewrite(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRewrite", []))

    @builtins.property
    @jsii.member(jsii_name="rewrite")
    def rewrite(
        self,
    ) -> "AppmeshGatewayRouteSpecHttp2RouteActionRewriteOutputReference":
        return typing.cast("AppmeshGatewayRouteSpecHttp2RouteActionRewriteOutputReference", jsii.get(self, "rewrite"))

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> "AppmeshGatewayRouteSpecHttp2RouteActionTargetOutputReference":
        return typing.cast("AppmeshGatewayRouteSpecHttp2RouteActionTargetOutputReference", jsii.get(self, "target"))

    @builtins.property
    @jsii.member(jsii_name="rewriteInput")
    def rewrite_input(
        self,
    ) -> typing.Optional["AppmeshGatewayRouteSpecHttp2RouteActionRewrite"]:
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecHttp2RouteActionRewrite"], jsii.get(self, "rewriteInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(
        self,
    ) -> typing.Optional["AppmeshGatewayRouteSpecHttp2RouteActionTarget"]:
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecHttp2RouteActionTarget"], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecHttp2RouteAction]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttp2RouteAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecHttp2RouteAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73311656927a476df9e30fa8192c95004d069a8ba782e31e1fc7099a9c8778d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttp2RouteActionRewrite",
    jsii_struct_bases=[],
    name_mapping={"hostname": "hostname", "prefix": "prefix"},
)
class AppmeshGatewayRouteSpecHttp2RouteActionRewrite:
    def __init__(
        self,
        *,
        hostname: typing.Optional[typing.Union["AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostname", typing.Dict[builtins.str, typing.Any]]] = None,
        prefix: typing.Optional[typing.Union["AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefix", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param hostname: hostname block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#hostname AppmeshGatewayRoute#hostname}
        :param prefix: prefix block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#prefix AppmeshGatewayRoute#prefix}
        '''
        if isinstance(hostname, dict):
            hostname = AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostname(**hostname)
        if isinstance(prefix, dict):
            prefix = AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefix(**prefix)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__003a6c2fac0d1710578cc8cc6490a0a9da88c66f235246fa0eb5772a4203f719)
            check_type(argname="argument hostname", value=hostname, expected_type=type_hints["hostname"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if hostname is not None:
            self._values["hostname"] = hostname
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def hostname(
        self,
    ) -> typing.Optional["AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostname"]:
        '''hostname block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#hostname AppmeshGatewayRoute#hostname}
        '''
        result = self._values.get("hostname")
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostname"], result)

    @builtins.property
    def prefix(
        self,
    ) -> typing.Optional["AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefix"]:
        '''prefix block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#prefix AppmeshGatewayRoute#prefix}
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefix"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecHttp2RouteActionRewrite(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostname",
    jsii_struct_bases=[],
    name_mapping={"default_target_hostname": "defaultTargetHostname"},
)
class AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostname:
    def __init__(self, *, default_target_hostname: builtins.str) -> None:
        '''
        :param default_target_hostname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#default_target_hostname AppmeshGatewayRoute#default_target_hostname}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0bf7c9a3f58c1e3762b23365ef15cdb912bbaa6c24e0a939cf478417cb02f63)
            check_type(argname="argument default_target_hostname", value=default_target_hostname, expected_type=type_hints["default_target_hostname"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "default_target_hostname": default_target_hostname,
        }

    @builtins.property
    def default_target_hostname(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#default_target_hostname AppmeshGatewayRoute#default_target_hostname}.'''
        result = self._values.get("default_target_hostname")
        assert result is not None, "Required property 'default_target_hostname' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostname(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostnameOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostnameOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4f21de293b0d2f7798760f8f21512068d1be689066960a6b067be5fd4bc0dd92)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="defaultTargetHostnameInput")
    def default_target_hostname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultTargetHostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultTargetHostname")
    def default_target_hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultTargetHostname"))

    @default_target_hostname.setter
    def default_target_hostname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b83dbd685badd8e84f2f674b183bcd558418559bf6a9fb3e27203463385ef7ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultTargetHostname", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostname]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostname], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostname],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59f4c7546c66f9e14748c8d6677ed6e2c4497410e479be3538f89700b83844ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshGatewayRouteSpecHttp2RouteActionRewriteOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttp2RouteActionRewriteOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b8e8b8f5690e0c54f2a534a600323b461b23a32e1ad88fc0c84aff8ea5cf65c9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putHostname")
    def put_hostname(self, *, default_target_hostname: builtins.str) -> None:
        '''
        :param default_target_hostname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#default_target_hostname AppmeshGatewayRoute#default_target_hostname}.
        '''
        value = AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostname(
            default_target_hostname=default_target_hostname
        )

        return typing.cast(None, jsii.invoke(self, "putHostname", [value]))

    @jsii.member(jsii_name="putPrefix")
    def put_prefix(
        self,
        *,
        default_prefix: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param default_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#default_prefix AppmeshGatewayRoute#default_prefix}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#value AppmeshGatewayRoute#value}.
        '''
        value_ = AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefix(
            default_prefix=default_prefix, value=value
        )

        return typing.cast(None, jsii.invoke(self, "putPrefix", [value_]))

    @jsii.member(jsii_name="resetHostname")
    def reset_hostname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostname", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(
        self,
    ) -> AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostnameOutputReference:
        return typing.cast(AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostnameOutputReference, jsii.get(self, "hostname"))

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(
        self,
    ) -> "AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefixOutputReference":
        return typing.cast("AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefixOutputReference", jsii.get(self, "prefix"))

    @builtins.property
    @jsii.member(jsii_name="hostnameInput")
    def hostname_input(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostname]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostname], jsii.get(self, "hostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(
        self,
    ) -> typing.Optional["AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefix"]:
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefix"], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionRewrite]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionRewrite], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionRewrite],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__572d2727240e7ac54c5a39bf20616e6b558d1a71704e035e812e84f2b5d385a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefix",
    jsii_struct_bases=[],
    name_mapping={"default_prefix": "defaultPrefix", "value": "value"},
)
class AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefix:
    def __init__(
        self,
        *,
        default_prefix: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param default_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#default_prefix AppmeshGatewayRoute#default_prefix}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#value AppmeshGatewayRoute#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8556e3e051d28a50aa4da32e62b4198b9bb871f70451a8131f47d77e944d95f)
            check_type(argname="argument default_prefix", value=default_prefix, expected_type=type_hints["default_prefix"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if default_prefix is not None:
            self._values["default_prefix"] = default_prefix
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def default_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#default_prefix AppmeshGatewayRoute#default_prefix}.'''
        result = self._values.get("default_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#value AppmeshGatewayRoute#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefix(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefixOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefixOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__268ac17d728dfed31c8840811a94d61c24ff8916cdee6565736ddda53b7deca4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDefaultPrefix")
    def reset_default_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultPrefix", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="defaultPrefixInput")
    def default_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultPrefix")
    def default_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultPrefix"))

    @default_prefix.setter
    def default_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49d9441c402363512c4773e0633fde298b4ba1703a9e51cc14c39def3f25fac0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__780a3cb1dc52a936c63bbe1d2f0ccfc4c7fc8e1ffece72ab2c9b8cfd453164f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefix]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefix], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefix],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84c620a06d042aa3d7bf7d3c600f038755e37876bdc5ebec890744585a435d5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttp2RouteActionTarget",
    jsii_struct_bases=[],
    name_mapping={"virtual_service": "virtualService"},
)
class AppmeshGatewayRouteSpecHttp2RouteActionTarget:
    def __init__(
        self,
        *,
        virtual_service: typing.Union["AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualService", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param virtual_service: virtual_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_service AppmeshGatewayRoute#virtual_service}
        '''
        if isinstance(virtual_service, dict):
            virtual_service = AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualService(**virtual_service)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__434bff24fa465804651d514f74bf543ba3cac61544d896955bd373a961f71f5c)
            check_type(argname="argument virtual_service", value=virtual_service, expected_type=type_hints["virtual_service"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "virtual_service": virtual_service,
        }

    @builtins.property
    def virtual_service(
        self,
    ) -> "AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualService":
        '''virtual_service block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_service AppmeshGatewayRoute#virtual_service}
        '''
        result = self._values.get("virtual_service")
        assert result is not None, "Required property 'virtual_service' is missing"
        return typing.cast("AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualService", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecHttp2RouteActionTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshGatewayRouteSpecHttp2RouteActionTargetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttp2RouteActionTargetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__387256da9c1f06575b339ba2bff7e1566241a48fdda4cc050ce2b0140e30810b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putVirtualService")
    def put_virtual_service(self, *, virtual_service_name: builtins.str) -> None:
        '''
        :param virtual_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_service_name AppmeshGatewayRoute#virtual_service_name}.
        '''
        value = AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualService(
            virtual_service_name=virtual_service_name
        )

        return typing.cast(None, jsii.invoke(self, "putVirtualService", [value]))

    @builtins.property
    @jsii.member(jsii_name="virtualService")
    def virtual_service(
        self,
    ) -> "AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualServiceOutputReference":
        return typing.cast("AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualServiceOutputReference", jsii.get(self, "virtualService"))

    @builtins.property
    @jsii.member(jsii_name="virtualServiceInput")
    def virtual_service_input(
        self,
    ) -> typing.Optional["AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualService"]:
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualService"], jsii.get(self, "virtualServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionTarget]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionTarget],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__694d60667dc4ef9c437185d45be15f361c19fd5cc5b68fbcfbaba18aa263f791)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualService",
    jsii_struct_bases=[],
    name_mapping={"virtual_service_name": "virtualServiceName"},
)
class AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualService:
    def __init__(self, *, virtual_service_name: builtins.str) -> None:
        '''
        :param virtual_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_service_name AppmeshGatewayRoute#virtual_service_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1c201730fca46745c36321029271f2514c33617dca813bd1745ee54971172e9)
            check_type(argname="argument virtual_service_name", value=virtual_service_name, expected_type=type_hints["virtual_service_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "virtual_service_name": virtual_service_name,
        }

    @builtins.property
    def virtual_service_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_service_name AppmeshGatewayRoute#virtual_service_name}.'''
        result = self._values.get("virtual_service_name")
        assert result is not None, "Required property 'virtual_service_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualServiceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualServiceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1141f8c76ed73083cc051351b072b192daaf599103d9733a50270aedccb93f8c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

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
            type_hints = typing.get_type_hints(_typecheckingstub__a68b2aa825554597a559f57e79bf78f719b3f0a372e2f7c0c55873b2ae710555)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualServiceName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualService]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualService], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualService],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a8c3cd9296c5a48e940e402a386db8872bbd6b2eb2ec8f42bebefa0b407623d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttp2RouteMatch",
    jsii_struct_bases=[],
    name_mapping={"hostname": "hostname", "prefix": "prefix"},
)
class AppmeshGatewayRouteSpecHttp2RouteMatch:
    def __init__(
        self,
        *,
        hostname: typing.Optional[typing.Union["AppmeshGatewayRouteSpecHttp2RouteMatchHostname", typing.Dict[builtins.str, typing.Any]]] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param hostname: hostname block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#hostname AppmeshGatewayRoute#hostname}
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#prefix AppmeshGatewayRoute#prefix}.
        '''
        if isinstance(hostname, dict):
            hostname = AppmeshGatewayRouteSpecHttp2RouteMatchHostname(**hostname)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0918b8b9e29543ae3482336c78c43cc7102ba8f721ded8ea2784937843c347c)
            check_type(argname="argument hostname", value=hostname, expected_type=type_hints["hostname"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if hostname is not None:
            self._values["hostname"] = hostname
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def hostname(
        self,
    ) -> typing.Optional["AppmeshGatewayRouteSpecHttp2RouteMatchHostname"]:
        '''hostname block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#hostname AppmeshGatewayRoute#hostname}
        '''
        result = self._values.get("hostname")
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecHttp2RouteMatchHostname"], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#prefix AppmeshGatewayRoute#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecHttp2RouteMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttp2RouteMatchHostname",
    jsii_struct_bases=[],
    name_mapping={"exact": "exact", "suffix": "suffix"},
)
class AppmeshGatewayRouteSpecHttp2RouteMatchHostname:
    def __init__(
        self,
        *,
        exact: typing.Optional[builtins.str] = None,
        suffix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param exact: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#exact AppmeshGatewayRoute#exact}.
        :param suffix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#suffix AppmeshGatewayRoute#suffix}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5da2b88496ec4d660d49886fc63c8b820015352281c865eec2c58c0ae68a90bd)
            check_type(argname="argument exact", value=exact, expected_type=type_hints["exact"])
            check_type(argname="argument suffix", value=suffix, expected_type=type_hints["suffix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if exact is not None:
            self._values["exact"] = exact
        if suffix is not None:
            self._values["suffix"] = suffix

    @builtins.property
    def exact(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#exact AppmeshGatewayRoute#exact}.'''
        result = self._values.get("exact")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def suffix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#suffix AppmeshGatewayRoute#suffix}.'''
        result = self._values.get("suffix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecHttp2RouteMatchHostname(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshGatewayRouteSpecHttp2RouteMatchHostnameOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttp2RouteMatchHostnameOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1779a06e416cc939b475a5a128a9782b4b1acec7b0ce36ca6c0e81c33c19ea68)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetExact")
    def reset_exact(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExact", []))

    @jsii.member(jsii_name="resetSuffix")
    def reset_suffix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuffix", []))

    @builtins.property
    @jsii.member(jsii_name="exactInput")
    def exact_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "exactInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__fcbbd5d8f86e32c2aabd81c8cb90acdcffac69630eb98af2b3bab533215bddc7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exact", value)

    @builtins.property
    @jsii.member(jsii_name="suffix")
    def suffix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "suffix"))

    @suffix.setter
    def suffix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b20320ff05e8cbc494267b4cd955eb644941c4a2e756d608eeeafa8b9ff7ebaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "suffix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecHttp2RouteMatchHostname]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttp2RouteMatchHostname], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecHttp2RouteMatchHostname],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1935cf360c51204f58faaee1e26f275dfeeec6ce6390c2789ed074132010a6c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshGatewayRouteSpecHttp2RouteMatchOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttp2RouteMatchOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__074339a247df0727aad27b639a0eedc60bada052335be024bfa974ac71136db9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putHostname")
    def put_hostname(
        self,
        *,
        exact: typing.Optional[builtins.str] = None,
        suffix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param exact: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#exact AppmeshGatewayRoute#exact}.
        :param suffix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#suffix AppmeshGatewayRoute#suffix}.
        '''
        value = AppmeshGatewayRouteSpecHttp2RouteMatchHostname(
            exact=exact, suffix=suffix
        )

        return typing.cast(None, jsii.invoke(self, "putHostname", [value]))

    @jsii.member(jsii_name="resetHostname")
    def reset_hostname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostname", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> AppmeshGatewayRouteSpecHttp2RouteMatchHostnameOutputReference:
        return typing.cast(AppmeshGatewayRouteSpecHttp2RouteMatchHostnameOutputReference, jsii.get(self, "hostname"))

    @builtins.property
    @jsii.member(jsii_name="hostnameInput")
    def hostname_input(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecHttp2RouteMatchHostname]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttp2RouteMatchHostname], jsii.get(self, "hostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddd412045304c5ab9bdc11a39ee1d9160178578905f8695c9b7cf01cb9c175c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshGatewayRouteSpecHttp2RouteMatch]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttp2RouteMatch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecHttp2RouteMatch],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4397fcf97d0bf76179070b7a1c4f40e90cf682e24f82b869cb87ea66d2c2bfb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshGatewayRouteSpecHttp2RouteOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttp2RouteOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a3da95e7e7595f6066727ff9fa0662ec0bf16f220accfcca00e43435009c9516)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAction")
    def put_action(
        self,
        *,
        target: typing.Union[AppmeshGatewayRouteSpecHttp2RouteActionTarget, typing.Dict[builtins.str, typing.Any]],
        rewrite: typing.Optional[typing.Union[AppmeshGatewayRouteSpecHttp2RouteActionRewrite, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param target: target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#target AppmeshGatewayRoute#target}
        :param rewrite: rewrite block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#rewrite AppmeshGatewayRoute#rewrite}
        '''
        value = AppmeshGatewayRouteSpecHttp2RouteAction(target=target, rewrite=rewrite)

        return typing.cast(None, jsii.invoke(self, "putAction", [value]))

    @jsii.member(jsii_name="putMatch")
    def put_match(
        self,
        *,
        hostname: typing.Optional[typing.Union[AppmeshGatewayRouteSpecHttp2RouteMatchHostname, typing.Dict[builtins.str, typing.Any]]] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param hostname: hostname block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#hostname AppmeshGatewayRoute#hostname}
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#prefix AppmeshGatewayRoute#prefix}.
        '''
        value = AppmeshGatewayRouteSpecHttp2RouteMatch(
            hostname=hostname, prefix=prefix
        )

        return typing.cast(None, jsii.invoke(self, "putMatch", [value]))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> AppmeshGatewayRouteSpecHttp2RouteActionOutputReference:
        return typing.cast(AppmeshGatewayRouteSpecHttp2RouteActionOutputReference, jsii.get(self, "action"))

    @builtins.property
    @jsii.member(jsii_name="match")
    def match(self) -> AppmeshGatewayRouteSpecHttp2RouteMatchOutputReference:
        return typing.cast(AppmeshGatewayRouteSpecHttp2RouteMatchOutputReference, jsii.get(self, "match"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[AppmeshGatewayRouteSpecHttp2RouteAction]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttp2RouteAction], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="matchInput")
    def match_input(self) -> typing.Optional[AppmeshGatewayRouteSpecHttp2RouteMatch]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttp2RouteMatch], jsii.get(self, "matchInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshGatewayRouteSpecHttp2Route]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttp2Route], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecHttp2Route],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6556172d0c127901a9219e1c554438e1b42facc6e174980cad70f1902f9dee4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttpRoute",
    jsii_struct_bases=[],
    name_mapping={"action": "action", "match": "match"},
)
class AppmeshGatewayRouteSpecHttpRoute:
    def __init__(
        self,
        *,
        action: typing.Union["AppmeshGatewayRouteSpecHttpRouteAction", typing.Dict[builtins.str, typing.Any]],
        match: typing.Union["AppmeshGatewayRouteSpecHttpRouteMatch", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#action AppmeshGatewayRoute#action}
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#match AppmeshGatewayRoute#match}
        '''
        if isinstance(action, dict):
            action = AppmeshGatewayRouteSpecHttpRouteAction(**action)
        if isinstance(match, dict):
            match = AppmeshGatewayRouteSpecHttpRouteMatch(**match)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33ead66e1ef18e39230de37b614acc7dbebc3d8f7105ca6e0257f489fb42354c)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument match", value=match, expected_type=type_hints["match"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action": action,
            "match": match,
        }

    @builtins.property
    def action(self) -> "AppmeshGatewayRouteSpecHttpRouteAction":
        '''action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#action AppmeshGatewayRoute#action}
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast("AppmeshGatewayRouteSpecHttpRouteAction", result)

    @builtins.property
    def match(self) -> "AppmeshGatewayRouteSpecHttpRouteMatch":
        '''match block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#match AppmeshGatewayRoute#match}
        '''
        result = self._values.get("match")
        assert result is not None, "Required property 'match' is missing"
        return typing.cast("AppmeshGatewayRouteSpecHttpRouteMatch", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecHttpRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttpRouteAction",
    jsii_struct_bases=[],
    name_mapping={"target": "target", "rewrite": "rewrite"},
)
class AppmeshGatewayRouteSpecHttpRouteAction:
    def __init__(
        self,
        *,
        target: typing.Union["AppmeshGatewayRouteSpecHttpRouteActionTarget", typing.Dict[builtins.str, typing.Any]],
        rewrite: typing.Optional[typing.Union["AppmeshGatewayRouteSpecHttpRouteActionRewrite", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param target: target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#target AppmeshGatewayRoute#target}
        :param rewrite: rewrite block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#rewrite AppmeshGatewayRoute#rewrite}
        '''
        if isinstance(target, dict):
            target = AppmeshGatewayRouteSpecHttpRouteActionTarget(**target)
        if isinstance(rewrite, dict):
            rewrite = AppmeshGatewayRouteSpecHttpRouteActionRewrite(**rewrite)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b597a6255dc21725f3b54c30a8cf96c3512d9abe1742323a5f6d28cd737d3f59)
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument rewrite", value=rewrite, expected_type=type_hints["rewrite"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "target": target,
        }
        if rewrite is not None:
            self._values["rewrite"] = rewrite

    @builtins.property
    def target(self) -> "AppmeshGatewayRouteSpecHttpRouteActionTarget":
        '''target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#target AppmeshGatewayRoute#target}
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast("AppmeshGatewayRouteSpecHttpRouteActionTarget", result)

    @builtins.property
    def rewrite(
        self,
    ) -> typing.Optional["AppmeshGatewayRouteSpecHttpRouteActionRewrite"]:
        '''rewrite block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#rewrite AppmeshGatewayRoute#rewrite}
        '''
        result = self._values.get("rewrite")
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecHttpRouteActionRewrite"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecHttpRouteAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshGatewayRouteSpecHttpRouteActionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttpRouteActionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dcd5873c8b03f866f16b110fc1937cfef6886b1f78c345c2390b78e4e13b26da)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRewrite")
    def put_rewrite(
        self,
        *,
        hostname: typing.Optional[typing.Union["AppmeshGatewayRouteSpecHttpRouteActionRewriteHostname", typing.Dict[builtins.str, typing.Any]]] = None,
        prefix: typing.Optional[typing.Union["AppmeshGatewayRouteSpecHttpRouteActionRewritePrefix", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param hostname: hostname block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#hostname AppmeshGatewayRoute#hostname}
        :param prefix: prefix block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#prefix AppmeshGatewayRoute#prefix}
        '''
        value = AppmeshGatewayRouteSpecHttpRouteActionRewrite(
            hostname=hostname, prefix=prefix
        )

        return typing.cast(None, jsii.invoke(self, "putRewrite", [value]))

    @jsii.member(jsii_name="putTarget")
    def put_target(
        self,
        *,
        virtual_service: typing.Union["AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualService", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param virtual_service: virtual_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_service AppmeshGatewayRoute#virtual_service}
        '''
        value = AppmeshGatewayRouteSpecHttpRouteActionTarget(
            virtual_service=virtual_service
        )

        return typing.cast(None, jsii.invoke(self, "putTarget", [value]))

    @jsii.member(jsii_name="resetRewrite")
    def reset_rewrite(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRewrite", []))

    @builtins.property
    @jsii.member(jsii_name="rewrite")
    def rewrite(self) -> "AppmeshGatewayRouteSpecHttpRouteActionRewriteOutputReference":
        return typing.cast("AppmeshGatewayRouteSpecHttpRouteActionRewriteOutputReference", jsii.get(self, "rewrite"))

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> "AppmeshGatewayRouteSpecHttpRouteActionTargetOutputReference":
        return typing.cast("AppmeshGatewayRouteSpecHttpRouteActionTargetOutputReference", jsii.get(self, "target"))

    @builtins.property
    @jsii.member(jsii_name="rewriteInput")
    def rewrite_input(
        self,
    ) -> typing.Optional["AppmeshGatewayRouteSpecHttpRouteActionRewrite"]:
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecHttpRouteActionRewrite"], jsii.get(self, "rewriteInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(
        self,
    ) -> typing.Optional["AppmeshGatewayRouteSpecHttpRouteActionTarget"]:
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecHttpRouteActionTarget"], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshGatewayRouteSpecHttpRouteAction]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttpRouteAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecHttpRouteAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__951c906eecc4980e254099a3bdbc3bfb97c75f291ed30f6f3ffa262f1ed4687e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttpRouteActionRewrite",
    jsii_struct_bases=[],
    name_mapping={"hostname": "hostname", "prefix": "prefix"},
)
class AppmeshGatewayRouteSpecHttpRouteActionRewrite:
    def __init__(
        self,
        *,
        hostname: typing.Optional[typing.Union["AppmeshGatewayRouteSpecHttpRouteActionRewriteHostname", typing.Dict[builtins.str, typing.Any]]] = None,
        prefix: typing.Optional[typing.Union["AppmeshGatewayRouteSpecHttpRouteActionRewritePrefix", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param hostname: hostname block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#hostname AppmeshGatewayRoute#hostname}
        :param prefix: prefix block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#prefix AppmeshGatewayRoute#prefix}
        '''
        if isinstance(hostname, dict):
            hostname = AppmeshGatewayRouteSpecHttpRouteActionRewriteHostname(**hostname)
        if isinstance(prefix, dict):
            prefix = AppmeshGatewayRouteSpecHttpRouteActionRewritePrefix(**prefix)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6715a64235161d1d1dd6516dc9d4838534f47f68f0d313a88c83b11031b1f845)
            check_type(argname="argument hostname", value=hostname, expected_type=type_hints["hostname"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if hostname is not None:
            self._values["hostname"] = hostname
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def hostname(
        self,
    ) -> typing.Optional["AppmeshGatewayRouteSpecHttpRouteActionRewriteHostname"]:
        '''hostname block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#hostname AppmeshGatewayRoute#hostname}
        '''
        result = self._values.get("hostname")
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecHttpRouteActionRewriteHostname"], result)

    @builtins.property
    def prefix(
        self,
    ) -> typing.Optional["AppmeshGatewayRouteSpecHttpRouteActionRewritePrefix"]:
        '''prefix block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#prefix AppmeshGatewayRoute#prefix}
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecHttpRouteActionRewritePrefix"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecHttpRouteActionRewrite(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttpRouteActionRewriteHostname",
    jsii_struct_bases=[],
    name_mapping={"default_target_hostname": "defaultTargetHostname"},
)
class AppmeshGatewayRouteSpecHttpRouteActionRewriteHostname:
    def __init__(self, *, default_target_hostname: builtins.str) -> None:
        '''
        :param default_target_hostname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#default_target_hostname AppmeshGatewayRoute#default_target_hostname}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76998c61b8bcae2218bccedf1343f4804e97f1205d475dfada177154f348ba0b)
            check_type(argname="argument default_target_hostname", value=default_target_hostname, expected_type=type_hints["default_target_hostname"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "default_target_hostname": default_target_hostname,
        }

    @builtins.property
    def default_target_hostname(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#default_target_hostname AppmeshGatewayRoute#default_target_hostname}.'''
        result = self._values.get("default_target_hostname")
        assert result is not None, "Required property 'default_target_hostname' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecHttpRouteActionRewriteHostname(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshGatewayRouteSpecHttpRouteActionRewriteHostnameOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttpRouteActionRewriteHostnameOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__15d3b9760cc5f4796b5be73f04876f3fe0dc5646ee7e405c548505c941e36a57)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="defaultTargetHostnameInput")
    def default_target_hostname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultTargetHostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultTargetHostname")
    def default_target_hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultTargetHostname"))

    @default_target_hostname.setter
    def default_target_hostname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91ebf8adefe30e9b63daca56537b00687c89b8a972aa6581ef6e1d98773baaa9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultTargetHostname", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionRewriteHostname]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionRewriteHostname], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionRewriteHostname],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5594156d6d19d69c51cad00446f58d71e90347f193240f93217bf86ccab1504)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshGatewayRouteSpecHttpRouteActionRewriteOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttpRouteActionRewriteOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__590d81ca5027b731a8c720e0813fd94d18dd5668ce2c38f83d9f71f423588e21)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putHostname")
    def put_hostname(self, *, default_target_hostname: builtins.str) -> None:
        '''
        :param default_target_hostname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#default_target_hostname AppmeshGatewayRoute#default_target_hostname}.
        '''
        value = AppmeshGatewayRouteSpecHttpRouteActionRewriteHostname(
            default_target_hostname=default_target_hostname
        )

        return typing.cast(None, jsii.invoke(self, "putHostname", [value]))

    @jsii.member(jsii_name="putPrefix")
    def put_prefix(
        self,
        *,
        default_prefix: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param default_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#default_prefix AppmeshGatewayRoute#default_prefix}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#value AppmeshGatewayRoute#value}.
        '''
        value_ = AppmeshGatewayRouteSpecHttpRouteActionRewritePrefix(
            default_prefix=default_prefix, value=value
        )

        return typing.cast(None, jsii.invoke(self, "putPrefix", [value_]))

    @jsii.member(jsii_name="resetHostname")
    def reset_hostname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostname", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(
        self,
    ) -> AppmeshGatewayRouteSpecHttpRouteActionRewriteHostnameOutputReference:
        return typing.cast(AppmeshGatewayRouteSpecHttpRouteActionRewriteHostnameOutputReference, jsii.get(self, "hostname"))

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(
        self,
    ) -> "AppmeshGatewayRouteSpecHttpRouteActionRewritePrefixOutputReference":
        return typing.cast("AppmeshGatewayRouteSpecHttpRouteActionRewritePrefixOutputReference", jsii.get(self, "prefix"))

    @builtins.property
    @jsii.member(jsii_name="hostnameInput")
    def hostname_input(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionRewriteHostname]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionRewriteHostname], jsii.get(self, "hostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(
        self,
    ) -> typing.Optional["AppmeshGatewayRouteSpecHttpRouteActionRewritePrefix"]:
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecHttpRouteActionRewritePrefix"], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionRewrite]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionRewrite], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionRewrite],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbbc6c0a7908801c9c7bc7266b85ab76492ca44c65c9b55dca4522ec8c8ab623)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttpRouteActionRewritePrefix",
    jsii_struct_bases=[],
    name_mapping={"default_prefix": "defaultPrefix", "value": "value"},
)
class AppmeshGatewayRouteSpecHttpRouteActionRewritePrefix:
    def __init__(
        self,
        *,
        default_prefix: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param default_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#default_prefix AppmeshGatewayRoute#default_prefix}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#value AppmeshGatewayRoute#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02195a58e0ff18a5bcabe0dc802883be5e8a1a7ec58213c12cec3e7554b50653)
            check_type(argname="argument default_prefix", value=default_prefix, expected_type=type_hints["default_prefix"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if default_prefix is not None:
            self._values["default_prefix"] = default_prefix
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def default_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#default_prefix AppmeshGatewayRoute#default_prefix}.'''
        result = self._values.get("default_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#value AppmeshGatewayRoute#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecHttpRouteActionRewritePrefix(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshGatewayRouteSpecHttpRouteActionRewritePrefixOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttpRouteActionRewritePrefixOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c6c09c06bcf7ec47aff366090c03594f512ca5239634ef77590812df205aec69)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDefaultPrefix")
    def reset_default_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultPrefix", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="defaultPrefixInput")
    def default_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultPrefix")
    def default_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultPrefix"))

    @default_prefix.setter
    def default_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca53ad288d996b98bec434a89f39649d0576e377e4e4e87055f87c2b4bbaed66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d16a09876d794a30f61d14db43dfdf84f910d9dfaba23410c40e1881ec8a46ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionRewritePrefix]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionRewritePrefix], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionRewritePrefix],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc4302a94cb3da7cf705e0c6bef0f1275f9368286b83b5861e9d09fff0cbd12c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttpRouteActionTarget",
    jsii_struct_bases=[],
    name_mapping={"virtual_service": "virtualService"},
)
class AppmeshGatewayRouteSpecHttpRouteActionTarget:
    def __init__(
        self,
        *,
        virtual_service: typing.Union["AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualService", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param virtual_service: virtual_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_service AppmeshGatewayRoute#virtual_service}
        '''
        if isinstance(virtual_service, dict):
            virtual_service = AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualService(**virtual_service)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86cfa0c1d7066bacb3d23840e507e908d262811eb617e119c936b1bbaf753349)
            check_type(argname="argument virtual_service", value=virtual_service, expected_type=type_hints["virtual_service"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "virtual_service": virtual_service,
        }

    @builtins.property
    def virtual_service(
        self,
    ) -> "AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualService":
        '''virtual_service block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_service AppmeshGatewayRoute#virtual_service}
        '''
        result = self._values.get("virtual_service")
        assert result is not None, "Required property 'virtual_service' is missing"
        return typing.cast("AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualService", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecHttpRouteActionTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshGatewayRouteSpecHttpRouteActionTargetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttpRouteActionTargetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6c48a0cb14c2c8e2d20c81f5a373c1e1435eb4867a1a136f5637e2c8c4bbf5ea)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putVirtualService")
    def put_virtual_service(self, *, virtual_service_name: builtins.str) -> None:
        '''
        :param virtual_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_service_name AppmeshGatewayRoute#virtual_service_name}.
        '''
        value = AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualService(
            virtual_service_name=virtual_service_name
        )

        return typing.cast(None, jsii.invoke(self, "putVirtualService", [value]))

    @builtins.property
    @jsii.member(jsii_name="virtualService")
    def virtual_service(
        self,
    ) -> "AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualServiceOutputReference":
        return typing.cast("AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualServiceOutputReference", jsii.get(self, "virtualService"))

    @builtins.property
    @jsii.member(jsii_name="virtualServiceInput")
    def virtual_service_input(
        self,
    ) -> typing.Optional["AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualService"]:
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualService"], jsii.get(self, "virtualServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionTarget]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionTarget],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4133a930d1303b872fe28732879377c1e24a4566019358e19ae794b9efce48f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualService",
    jsii_struct_bases=[],
    name_mapping={"virtual_service_name": "virtualServiceName"},
)
class AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualService:
    def __init__(self, *, virtual_service_name: builtins.str) -> None:
        '''
        :param virtual_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_service_name AppmeshGatewayRoute#virtual_service_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79216cbe1eb67d9ab4f0509f2dec3c0343f83df99cb7881ba3c05de35320a925)
            check_type(argname="argument virtual_service_name", value=virtual_service_name, expected_type=type_hints["virtual_service_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "virtual_service_name": virtual_service_name,
        }

    @builtins.property
    def virtual_service_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#virtual_service_name AppmeshGatewayRoute#virtual_service_name}.'''
        result = self._values.get("virtual_service_name")
        assert result is not None, "Required property 'virtual_service_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualServiceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualServiceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__07a568c80caad0228f32ffd35f6c940d0fbb5f91fe1334e2f411e04e50c993fa)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

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
            type_hints = typing.get_type_hints(_typecheckingstub__46de8222c679f4affd2d701c48602197049bcc7109b84ab0b19d57ff5b179e8c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualServiceName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualService]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualService], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualService],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4df9a30985ab336d61cf822ab08fa3ae3f84acba724925b2d8fff7a55df7caa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttpRouteMatch",
    jsii_struct_bases=[],
    name_mapping={"hostname": "hostname", "prefix": "prefix"},
)
class AppmeshGatewayRouteSpecHttpRouteMatch:
    def __init__(
        self,
        *,
        hostname: typing.Optional[typing.Union["AppmeshGatewayRouteSpecHttpRouteMatchHostname", typing.Dict[builtins.str, typing.Any]]] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param hostname: hostname block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#hostname AppmeshGatewayRoute#hostname}
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#prefix AppmeshGatewayRoute#prefix}.
        '''
        if isinstance(hostname, dict):
            hostname = AppmeshGatewayRouteSpecHttpRouteMatchHostname(**hostname)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7587cfcf9964652f282ea89969e68ddcba711e40c1eed026d26e8242419b474)
            check_type(argname="argument hostname", value=hostname, expected_type=type_hints["hostname"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if hostname is not None:
            self._values["hostname"] = hostname
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def hostname(
        self,
    ) -> typing.Optional["AppmeshGatewayRouteSpecHttpRouteMatchHostname"]:
        '''hostname block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#hostname AppmeshGatewayRoute#hostname}
        '''
        result = self._values.get("hostname")
        return typing.cast(typing.Optional["AppmeshGatewayRouteSpecHttpRouteMatchHostname"], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#prefix AppmeshGatewayRoute#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecHttpRouteMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttpRouteMatchHostname",
    jsii_struct_bases=[],
    name_mapping={"exact": "exact", "suffix": "suffix"},
)
class AppmeshGatewayRouteSpecHttpRouteMatchHostname:
    def __init__(
        self,
        *,
        exact: typing.Optional[builtins.str] = None,
        suffix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param exact: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#exact AppmeshGatewayRoute#exact}.
        :param suffix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#suffix AppmeshGatewayRoute#suffix}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__958b0129fd819287ee91040a95b8c931457242374a3d7bdadf44d07d72f1f061)
            check_type(argname="argument exact", value=exact, expected_type=type_hints["exact"])
            check_type(argname="argument suffix", value=suffix, expected_type=type_hints["suffix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if exact is not None:
            self._values["exact"] = exact
        if suffix is not None:
            self._values["suffix"] = suffix

    @builtins.property
    def exact(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#exact AppmeshGatewayRoute#exact}.'''
        result = self._values.get("exact")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def suffix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#suffix AppmeshGatewayRoute#suffix}.'''
        result = self._values.get("suffix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshGatewayRouteSpecHttpRouteMatchHostname(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshGatewayRouteSpecHttpRouteMatchHostnameOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttpRouteMatchHostnameOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__66521b969d496992844e3dc537d6a521de5ddf2bec7f0a5529e912a9bc5bd860)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetExact")
    def reset_exact(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExact", []))

    @jsii.member(jsii_name="resetSuffix")
    def reset_suffix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuffix", []))

    @builtins.property
    @jsii.member(jsii_name="exactInput")
    def exact_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "exactInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__b711a44de00acf63f0f61cd6a63ae2df67ba250fe0ca1e29d0945fc63055ef13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exact", value)

    @builtins.property
    @jsii.member(jsii_name="suffix")
    def suffix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "suffix"))

    @suffix.setter
    def suffix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42d6c23cb7362e66a31643e1696c9b52214e16db1290109e9852bbf20b69accb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "suffix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecHttpRouteMatchHostname]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttpRouteMatchHostname], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecHttpRouteMatchHostname],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__988c69332d9baca89a4e4a878aebbe004de99896ea90a11352225523c178f32c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshGatewayRouteSpecHttpRouteMatchOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttpRouteMatchOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f30448249dcf21f0899e9ccd3caa9f694f18ee62d4229decf0fc4205fd975a54)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putHostname")
    def put_hostname(
        self,
        *,
        exact: typing.Optional[builtins.str] = None,
        suffix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param exact: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#exact AppmeshGatewayRoute#exact}.
        :param suffix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#suffix AppmeshGatewayRoute#suffix}.
        '''
        value = AppmeshGatewayRouteSpecHttpRouteMatchHostname(
            exact=exact, suffix=suffix
        )

        return typing.cast(None, jsii.invoke(self, "putHostname", [value]))

    @jsii.member(jsii_name="resetHostname")
    def reset_hostname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostname", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> AppmeshGatewayRouteSpecHttpRouteMatchHostnameOutputReference:
        return typing.cast(AppmeshGatewayRouteSpecHttpRouteMatchHostnameOutputReference, jsii.get(self, "hostname"))

    @builtins.property
    @jsii.member(jsii_name="hostnameInput")
    def hostname_input(
        self,
    ) -> typing.Optional[AppmeshGatewayRouteSpecHttpRouteMatchHostname]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttpRouteMatchHostname], jsii.get(self, "hostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33a17ce01c8147c8988e94f3e548fb6c6fccd730d1049fa4cf2f1e15013668dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshGatewayRouteSpecHttpRouteMatch]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttpRouteMatch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecHttpRouteMatch],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eaeae8024ec7f4ad29fc38816bfcfe1fef97b2ec1c76722190a4313f34b14077)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshGatewayRouteSpecHttpRouteOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecHttpRouteOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__aa5be6974ed2d1ba1190a2fa5eabc9ab1f097683444d278acfa87a38a8e1c827)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAction")
    def put_action(
        self,
        *,
        target: typing.Union[AppmeshGatewayRouteSpecHttpRouteActionTarget, typing.Dict[builtins.str, typing.Any]],
        rewrite: typing.Optional[typing.Union[AppmeshGatewayRouteSpecHttpRouteActionRewrite, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param target: target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#target AppmeshGatewayRoute#target}
        :param rewrite: rewrite block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#rewrite AppmeshGatewayRoute#rewrite}
        '''
        value = AppmeshGatewayRouteSpecHttpRouteAction(target=target, rewrite=rewrite)

        return typing.cast(None, jsii.invoke(self, "putAction", [value]))

    @jsii.member(jsii_name="putMatch")
    def put_match(
        self,
        *,
        hostname: typing.Optional[typing.Union[AppmeshGatewayRouteSpecHttpRouteMatchHostname, typing.Dict[builtins.str, typing.Any]]] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param hostname: hostname block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#hostname AppmeshGatewayRoute#hostname}
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#prefix AppmeshGatewayRoute#prefix}.
        '''
        value = AppmeshGatewayRouteSpecHttpRouteMatch(hostname=hostname, prefix=prefix)

        return typing.cast(None, jsii.invoke(self, "putMatch", [value]))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> AppmeshGatewayRouteSpecHttpRouteActionOutputReference:
        return typing.cast(AppmeshGatewayRouteSpecHttpRouteActionOutputReference, jsii.get(self, "action"))

    @builtins.property
    @jsii.member(jsii_name="match")
    def match(self) -> AppmeshGatewayRouteSpecHttpRouteMatchOutputReference:
        return typing.cast(AppmeshGatewayRouteSpecHttpRouteMatchOutputReference, jsii.get(self, "match"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[AppmeshGatewayRouteSpecHttpRouteAction]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttpRouteAction], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="matchInput")
    def match_input(self) -> typing.Optional[AppmeshGatewayRouteSpecHttpRouteMatch]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttpRouteMatch], jsii.get(self, "matchInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshGatewayRouteSpecHttpRoute]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttpRoute], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshGatewayRouteSpecHttpRoute],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ba3910886cd136eebe6ecea9cfeb65ff093280d749c7b0be57bb0bbb98fc350)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppmeshGatewayRouteSpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshGatewayRoute.AppmeshGatewayRouteSpecOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3da4d8e4b31d8d63c10cbc5c2f89480d4feab77388de18c528e7d3b6e08120c7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putGrpcRoute")
    def put_grpc_route(
        self,
        *,
        action: typing.Union[AppmeshGatewayRouteSpecGrpcRouteAction, typing.Dict[builtins.str, typing.Any]],
        match: typing.Union[AppmeshGatewayRouteSpecGrpcRouteMatch, typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#action AppmeshGatewayRoute#action}
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#match AppmeshGatewayRoute#match}
        '''
        value = AppmeshGatewayRouteSpecGrpcRoute(action=action, match=match)

        return typing.cast(None, jsii.invoke(self, "putGrpcRoute", [value]))

    @jsii.member(jsii_name="putHttp2Route")
    def put_http2_route(
        self,
        *,
        action: typing.Union[AppmeshGatewayRouteSpecHttp2RouteAction, typing.Dict[builtins.str, typing.Any]],
        match: typing.Union[AppmeshGatewayRouteSpecHttp2RouteMatch, typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#action AppmeshGatewayRoute#action}
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#match AppmeshGatewayRoute#match}
        '''
        value = AppmeshGatewayRouteSpecHttp2Route(action=action, match=match)

        return typing.cast(None, jsii.invoke(self, "putHttp2Route", [value]))

    @jsii.member(jsii_name="putHttpRoute")
    def put_http_route(
        self,
        *,
        action: typing.Union[AppmeshGatewayRouteSpecHttpRouteAction, typing.Dict[builtins.str, typing.Any]],
        match: typing.Union[AppmeshGatewayRouteSpecHttpRouteMatch, typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#action AppmeshGatewayRoute#action}
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_gateway_route#match AppmeshGatewayRoute#match}
        '''
        value = AppmeshGatewayRouteSpecHttpRoute(action=action, match=match)

        return typing.cast(None, jsii.invoke(self, "putHttpRoute", [value]))

    @jsii.member(jsii_name="resetGrpcRoute")
    def reset_grpc_route(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGrpcRoute", []))

    @jsii.member(jsii_name="resetHttp2Route")
    def reset_http2_route(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttp2Route", []))

    @jsii.member(jsii_name="resetHttpRoute")
    def reset_http_route(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpRoute", []))

    @builtins.property
    @jsii.member(jsii_name="grpcRoute")
    def grpc_route(self) -> AppmeshGatewayRouteSpecGrpcRouteOutputReference:
        return typing.cast(AppmeshGatewayRouteSpecGrpcRouteOutputReference, jsii.get(self, "grpcRoute"))

    @builtins.property
    @jsii.member(jsii_name="http2Route")
    def http2_route(self) -> AppmeshGatewayRouteSpecHttp2RouteOutputReference:
        return typing.cast(AppmeshGatewayRouteSpecHttp2RouteOutputReference, jsii.get(self, "http2Route"))

    @builtins.property
    @jsii.member(jsii_name="httpRoute")
    def http_route(self) -> AppmeshGatewayRouteSpecHttpRouteOutputReference:
        return typing.cast(AppmeshGatewayRouteSpecHttpRouteOutputReference, jsii.get(self, "httpRoute"))

    @builtins.property
    @jsii.member(jsii_name="grpcRouteInput")
    def grpc_route_input(self) -> typing.Optional[AppmeshGatewayRouteSpecGrpcRoute]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecGrpcRoute], jsii.get(self, "grpcRouteInput"))

    @builtins.property
    @jsii.member(jsii_name="http2RouteInput")
    def http2_route_input(self) -> typing.Optional[AppmeshGatewayRouteSpecHttp2Route]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttp2Route], jsii.get(self, "http2RouteInput"))

    @builtins.property
    @jsii.member(jsii_name="httpRouteInput")
    def http_route_input(self) -> typing.Optional[AppmeshGatewayRouteSpecHttpRoute]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpecHttpRoute], jsii.get(self, "httpRouteInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshGatewayRouteSpec]:
        return typing.cast(typing.Optional[AppmeshGatewayRouteSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppmeshGatewayRouteSpec]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0c0498fa17dfb393c132679b4191916d8dc36de9e78862054d491ea14d20568)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AppmeshGatewayRoute",
    "AppmeshGatewayRouteConfig",
    "AppmeshGatewayRouteSpec",
    "AppmeshGatewayRouteSpecGrpcRoute",
    "AppmeshGatewayRouteSpecGrpcRouteAction",
    "AppmeshGatewayRouteSpecGrpcRouteActionOutputReference",
    "AppmeshGatewayRouteSpecGrpcRouteActionTarget",
    "AppmeshGatewayRouteSpecGrpcRouteActionTargetOutputReference",
    "AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualService",
    "AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualServiceOutputReference",
    "AppmeshGatewayRouteSpecGrpcRouteMatch",
    "AppmeshGatewayRouteSpecGrpcRouteMatchOutputReference",
    "AppmeshGatewayRouteSpecGrpcRouteOutputReference",
    "AppmeshGatewayRouteSpecHttp2Route",
    "AppmeshGatewayRouteSpecHttp2RouteAction",
    "AppmeshGatewayRouteSpecHttp2RouteActionOutputReference",
    "AppmeshGatewayRouteSpecHttp2RouteActionRewrite",
    "AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostname",
    "AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostnameOutputReference",
    "AppmeshGatewayRouteSpecHttp2RouteActionRewriteOutputReference",
    "AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefix",
    "AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefixOutputReference",
    "AppmeshGatewayRouteSpecHttp2RouteActionTarget",
    "AppmeshGatewayRouteSpecHttp2RouteActionTargetOutputReference",
    "AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualService",
    "AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualServiceOutputReference",
    "AppmeshGatewayRouteSpecHttp2RouteMatch",
    "AppmeshGatewayRouteSpecHttp2RouteMatchHostname",
    "AppmeshGatewayRouteSpecHttp2RouteMatchHostnameOutputReference",
    "AppmeshGatewayRouteSpecHttp2RouteMatchOutputReference",
    "AppmeshGatewayRouteSpecHttp2RouteOutputReference",
    "AppmeshGatewayRouteSpecHttpRoute",
    "AppmeshGatewayRouteSpecHttpRouteAction",
    "AppmeshGatewayRouteSpecHttpRouteActionOutputReference",
    "AppmeshGatewayRouteSpecHttpRouteActionRewrite",
    "AppmeshGatewayRouteSpecHttpRouteActionRewriteHostname",
    "AppmeshGatewayRouteSpecHttpRouteActionRewriteHostnameOutputReference",
    "AppmeshGatewayRouteSpecHttpRouteActionRewriteOutputReference",
    "AppmeshGatewayRouteSpecHttpRouteActionRewritePrefix",
    "AppmeshGatewayRouteSpecHttpRouteActionRewritePrefixOutputReference",
    "AppmeshGatewayRouteSpecHttpRouteActionTarget",
    "AppmeshGatewayRouteSpecHttpRouteActionTargetOutputReference",
    "AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualService",
    "AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualServiceOutputReference",
    "AppmeshGatewayRouteSpecHttpRouteMatch",
    "AppmeshGatewayRouteSpecHttpRouteMatchHostname",
    "AppmeshGatewayRouteSpecHttpRouteMatchHostnameOutputReference",
    "AppmeshGatewayRouteSpecHttpRouteMatchOutputReference",
    "AppmeshGatewayRouteSpecHttpRouteOutputReference",
    "AppmeshGatewayRouteSpecOutputReference",
]

publication.publish()

def _typecheckingstub__e60d33798b71a225a7d1f2942dd246a1100cc356a144a34f58197f1ac05aabbc(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    mesh_name: builtins.str,
    name: builtins.str,
    spec: typing.Union[AppmeshGatewayRouteSpec, typing.Dict[builtins.str, typing.Any]],
    virtual_gateway_name: builtins.str,
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

def _typecheckingstub__7e587e325912359a1611f4133e921b36e8cebb9fd0cdf584a0f2eab51e08c625(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3031a49d4ce416efe28766b7a5ae2908c34a138d87eb0f346f842e158415413b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce46ffdcd8eefcd444df38ae445888b443c90276232e84f272b7d849bbf19e74(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97873d709654eab8a9700dabd17d36113957588483fb81714ce560fb10042974(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ffba99add67cf77e231c7d1476e5bc361e79a7b7b01676ac346ac5d17049008(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3822414f6a8bd589a8e153c2ec4155bdde84b8d25db5af17b30e58ebc54667d(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6970ae0c3b698185d3698bf6fb594a016fe48662217d461ae91a2093f20b5855(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3eedc0182e1c2f6974092d2f3718ffe056cc08bc85cd4ad8a14c5b1e0c1dfb4(
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
    spec: typing.Union[AppmeshGatewayRouteSpec, typing.Dict[builtins.str, typing.Any]],
    virtual_gateway_name: builtins.str,
    id: typing.Optional[builtins.str] = None,
    mesh_owner: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ee41fbde5295cf1ffa05c763927f1dc70e4bbba7dea173815b1ac1f01f45f40(
    *,
    grpc_route: typing.Optional[typing.Union[AppmeshGatewayRouteSpecGrpcRoute, typing.Dict[builtins.str, typing.Any]]] = None,
    http2_route: typing.Optional[typing.Union[AppmeshGatewayRouteSpecHttp2Route, typing.Dict[builtins.str, typing.Any]]] = None,
    http_route: typing.Optional[typing.Union[AppmeshGatewayRouteSpecHttpRoute, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7dbb0f76051a578abee8e324f92b80a3d18851d7ef60ba935e6f5490eaa5313(
    *,
    action: typing.Union[AppmeshGatewayRouteSpecGrpcRouteAction, typing.Dict[builtins.str, typing.Any]],
    match: typing.Union[AppmeshGatewayRouteSpecGrpcRouteMatch, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d1daf217b0f498e434ddc5e1298c8be353963d4edf2c5cdfff3424f6613a9c7(
    *,
    target: typing.Union[AppmeshGatewayRouteSpecGrpcRouteActionTarget, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b27f7d594f24628476be98172eba889c51755fcb01c01bd41444427aee06086(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d43425c5a796c29e40ee45734ddf79929aae88b0dd1f83a84f02f7917b57af64(
    value: typing.Optional[AppmeshGatewayRouteSpecGrpcRouteAction],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d0db52090970c424d5719e8d5c3315c0bfe68a086b5fc8f40242af8c129120e(
    *,
    virtual_service: typing.Union[AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualService, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__164b7379690bfb045ce9d8cbf53011b9641d574f9e46459a3a18239e98cc3868(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__696e5f59073b72d6ff5bc0d7ce618d26e949655ef7193c1e8aee0980eb6b529d(
    value: typing.Optional[AppmeshGatewayRouteSpecGrpcRouteActionTarget],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41b4e7df913f68fd6b67a3783be159e2117f5821d73d50caa65320a5eb647d85(
    *,
    virtual_service_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbadf1254c179b7811d557075da006b5b05098b904cf5e07d462164a9a67f6a3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c9fe8ddb636bb6c6cd0ede052b9391baa204bd0ba15257eefc66f6f069c685c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6f373a92aac69d2a38d10d097f05cd342f1fadd2636d59b72848be2ecffbe29(
    value: typing.Optional[AppmeshGatewayRouteSpecGrpcRouteActionTargetVirtualService],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__592a13e8cf7d8b7449cb676b6a5f804bd709019f7dfe8a4dd8251e1b272b6257(
    *,
    service_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__450c94714afd1336eba6e944237cd7fe275eac61e64f7e26ac377ed54a0ba0d1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bcb67d2a5144e9def022b33b6c7da088acf9c975ffb6d9a98ffd310154b2a40(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__713a6f086d58c1ea51ce6c5b11e30fb64e380ba5b4a219db8d3267d60224250f(
    value: typing.Optional[AppmeshGatewayRouteSpecGrpcRouteMatch],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d56eeefeb64483322d2ec8c56907216621fdaf8470cdebc7391008d6944d647(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3599e43427c491b43fae0e0618ee02dc803f15421117f826178815522f2e9bee(
    value: typing.Optional[AppmeshGatewayRouteSpecGrpcRoute],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dc3d5d7beacd2020c67bb018d60de37fb98a8885bb6ea9e87e81bb12feff5a4(
    *,
    action: typing.Union[AppmeshGatewayRouteSpecHttp2RouteAction, typing.Dict[builtins.str, typing.Any]],
    match: typing.Union[AppmeshGatewayRouteSpecHttp2RouteMatch, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__879f60664815ac30c796c8f1023f6b22be62e393a692afe9cb5fd7a854239c91(
    *,
    target: typing.Union[AppmeshGatewayRouteSpecHttp2RouteActionTarget, typing.Dict[builtins.str, typing.Any]],
    rewrite: typing.Optional[typing.Union[AppmeshGatewayRouteSpecHttp2RouteActionRewrite, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d714c07e1cb1c488d7f1980334607e1681a7ffce93c8faa054819443c3b69211(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73311656927a476df9e30fa8192c95004d069a8ba782e31e1fc7099a9c8778d3(
    value: typing.Optional[AppmeshGatewayRouteSpecHttp2RouteAction],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__003a6c2fac0d1710578cc8cc6490a0a9da88c66f235246fa0eb5772a4203f719(
    *,
    hostname: typing.Optional[typing.Union[AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostname, typing.Dict[builtins.str, typing.Any]]] = None,
    prefix: typing.Optional[typing.Union[AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefix, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0bf7c9a3f58c1e3762b23365ef15cdb912bbaa6c24e0a939cf478417cb02f63(
    *,
    default_target_hostname: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f21de293b0d2f7798760f8f21512068d1be689066960a6b067be5fd4bc0dd92(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b83dbd685badd8e84f2f674b183bcd558418559bf6a9fb3e27203463385ef7ab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59f4c7546c66f9e14748c8d6677ed6e2c4497410e479be3538f89700b83844ed(
    value: typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionRewriteHostname],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8e8b8f5690e0c54f2a534a600323b461b23a32e1ad88fc0c84aff8ea5cf65c9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__572d2727240e7ac54c5a39bf20616e6b558d1a71704e035e812e84f2b5d385a1(
    value: typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionRewrite],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8556e3e051d28a50aa4da32e62b4198b9bb871f70451a8131f47d77e944d95f(
    *,
    default_prefix: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__268ac17d728dfed31c8840811a94d61c24ff8916cdee6565736ddda53b7deca4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49d9441c402363512c4773e0633fde298b4ba1703a9e51cc14c39def3f25fac0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__780a3cb1dc52a936c63bbe1d2f0ccfc4c7fc8e1ffece72ab2c9b8cfd453164f4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84c620a06d042aa3d7bf7d3c600f038755e37876bdc5ebec890744585a435d5e(
    value: typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionRewritePrefix],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__434bff24fa465804651d514f74bf543ba3cac61544d896955bd373a961f71f5c(
    *,
    virtual_service: typing.Union[AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualService, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__387256da9c1f06575b339ba2bff7e1566241a48fdda4cc050ce2b0140e30810b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__694d60667dc4ef9c437185d45be15f361c19fd5cc5b68fbcfbaba18aa263f791(
    value: typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionTarget],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1c201730fca46745c36321029271f2514c33617dca813bd1745ee54971172e9(
    *,
    virtual_service_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1141f8c76ed73083cc051351b072b192daaf599103d9733a50270aedccb93f8c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a68b2aa825554597a559f57e79bf78f719b3f0a372e2f7c0c55873b2ae710555(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a8c3cd9296c5a48e940e402a386db8872bbd6b2eb2ec8f42bebefa0b407623d(
    value: typing.Optional[AppmeshGatewayRouteSpecHttp2RouteActionTargetVirtualService],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0918b8b9e29543ae3482336c78c43cc7102ba8f721ded8ea2784937843c347c(
    *,
    hostname: typing.Optional[typing.Union[AppmeshGatewayRouteSpecHttp2RouteMatchHostname, typing.Dict[builtins.str, typing.Any]]] = None,
    prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5da2b88496ec4d660d49886fc63c8b820015352281c865eec2c58c0ae68a90bd(
    *,
    exact: typing.Optional[builtins.str] = None,
    suffix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1779a06e416cc939b475a5a128a9782b4b1acec7b0ce36ca6c0e81c33c19ea68(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcbbd5d8f86e32c2aabd81c8cb90acdcffac69630eb98af2b3bab533215bddc7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b20320ff05e8cbc494267b4cd955eb644941c4a2e756d608eeeafa8b9ff7ebaf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1935cf360c51204f58faaee1e26f275dfeeec6ce6390c2789ed074132010a6c3(
    value: typing.Optional[AppmeshGatewayRouteSpecHttp2RouteMatchHostname],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__074339a247df0727aad27b639a0eedc60bada052335be024bfa974ac71136db9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddd412045304c5ab9bdc11a39ee1d9160178578905f8695c9b7cf01cb9c175c8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4397fcf97d0bf76179070b7a1c4f40e90cf682e24f82b869cb87ea66d2c2bfb5(
    value: typing.Optional[AppmeshGatewayRouteSpecHttp2RouteMatch],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3da95e7e7595f6066727ff9fa0662ec0bf16f220accfcca00e43435009c9516(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6556172d0c127901a9219e1c554438e1b42facc6e174980cad70f1902f9dee4c(
    value: typing.Optional[AppmeshGatewayRouteSpecHttp2Route],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33ead66e1ef18e39230de37b614acc7dbebc3d8f7105ca6e0257f489fb42354c(
    *,
    action: typing.Union[AppmeshGatewayRouteSpecHttpRouteAction, typing.Dict[builtins.str, typing.Any]],
    match: typing.Union[AppmeshGatewayRouteSpecHttpRouteMatch, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b597a6255dc21725f3b54c30a8cf96c3512d9abe1742323a5f6d28cd737d3f59(
    *,
    target: typing.Union[AppmeshGatewayRouteSpecHttpRouteActionTarget, typing.Dict[builtins.str, typing.Any]],
    rewrite: typing.Optional[typing.Union[AppmeshGatewayRouteSpecHttpRouteActionRewrite, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcd5873c8b03f866f16b110fc1937cfef6886b1f78c345c2390b78e4e13b26da(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__951c906eecc4980e254099a3bdbc3bfb97c75f291ed30f6f3ffa262f1ed4687e(
    value: typing.Optional[AppmeshGatewayRouteSpecHttpRouteAction],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6715a64235161d1d1dd6516dc9d4838534f47f68f0d313a88c83b11031b1f845(
    *,
    hostname: typing.Optional[typing.Union[AppmeshGatewayRouteSpecHttpRouteActionRewriteHostname, typing.Dict[builtins.str, typing.Any]]] = None,
    prefix: typing.Optional[typing.Union[AppmeshGatewayRouteSpecHttpRouteActionRewritePrefix, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76998c61b8bcae2218bccedf1343f4804e97f1205d475dfada177154f348ba0b(
    *,
    default_target_hostname: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15d3b9760cc5f4796b5be73f04876f3fe0dc5646ee7e405c548505c941e36a57(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91ebf8adefe30e9b63daca56537b00687c89b8a972aa6581ef6e1d98773baaa9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5594156d6d19d69c51cad00446f58d71e90347f193240f93217bf86ccab1504(
    value: typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionRewriteHostname],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__590d81ca5027b731a8c720e0813fd94d18dd5668ce2c38f83d9f71f423588e21(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbbc6c0a7908801c9c7bc7266b85ab76492ca44c65c9b55dca4522ec8c8ab623(
    value: typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionRewrite],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02195a58e0ff18a5bcabe0dc802883be5e8a1a7ec58213c12cec3e7554b50653(
    *,
    default_prefix: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6c09c06bcf7ec47aff366090c03594f512ca5239634ef77590812df205aec69(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca53ad288d996b98bec434a89f39649d0576e377e4e4e87055f87c2b4bbaed66(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d16a09876d794a30f61d14db43dfdf84f910d9dfaba23410c40e1881ec8a46ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc4302a94cb3da7cf705e0c6bef0f1275f9368286b83b5861e9d09fff0cbd12c(
    value: typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionRewritePrefix],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86cfa0c1d7066bacb3d23840e507e908d262811eb617e119c936b1bbaf753349(
    *,
    virtual_service: typing.Union[AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualService, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c48a0cb14c2c8e2d20c81f5a373c1e1435eb4867a1a136f5637e2c8c4bbf5ea(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4133a930d1303b872fe28732879377c1e24a4566019358e19ae794b9efce48f9(
    value: typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionTarget],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79216cbe1eb67d9ab4f0509f2dec3c0343f83df99cb7881ba3c05de35320a925(
    *,
    virtual_service_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07a568c80caad0228f32ffd35f6c940d0fbb5f91fe1334e2f411e04e50c993fa(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46de8222c679f4affd2d701c48602197049bcc7109b84ab0b19d57ff5b179e8c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4df9a30985ab336d61cf822ab08fa3ae3f84acba724925b2d8fff7a55df7caa(
    value: typing.Optional[AppmeshGatewayRouteSpecHttpRouteActionTargetVirtualService],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7587cfcf9964652f282ea89969e68ddcba711e40c1eed026d26e8242419b474(
    *,
    hostname: typing.Optional[typing.Union[AppmeshGatewayRouteSpecHttpRouteMatchHostname, typing.Dict[builtins.str, typing.Any]]] = None,
    prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__958b0129fd819287ee91040a95b8c931457242374a3d7bdadf44d07d72f1f061(
    *,
    exact: typing.Optional[builtins.str] = None,
    suffix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66521b969d496992844e3dc537d6a521de5ddf2bec7f0a5529e912a9bc5bd860(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b711a44de00acf63f0f61cd6a63ae2df67ba250fe0ca1e29d0945fc63055ef13(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42d6c23cb7362e66a31643e1696c9b52214e16db1290109e9852bbf20b69accb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__988c69332d9baca89a4e4a878aebbe004de99896ea90a11352225523c178f32c(
    value: typing.Optional[AppmeshGatewayRouteSpecHttpRouteMatchHostname],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f30448249dcf21f0899e9ccd3caa9f694f18ee62d4229decf0fc4205fd975a54(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33a17ce01c8147c8988e94f3e548fb6c6fccd730d1049fa4cf2f1e15013668dd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eaeae8024ec7f4ad29fc38816bfcfe1fef97b2ec1c76722190a4313f34b14077(
    value: typing.Optional[AppmeshGatewayRouteSpecHttpRouteMatch],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa5be6974ed2d1ba1190a2fa5eabc9ab1f097683444d278acfa87a38a8e1c827(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ba3910886cd136eebe6ecea9cfeb65ff093280d749c7b0be57bb0bbb98fc350(
    value: typing.Optional[AppmeshGatewayRouteSpecHttpRoute],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3da4d8e4b31d8d63c10cbc5c2f89480d4feab77388de18c528e7d3b6e08120c7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0c0498fa17dfb393c132679b4191916d8dc36de9e78862054d491ea14d20568(
    value: typing.Optional[AppmeshGatewayRouteSpec],
) -> None:
    """Type checking stubs"""
    pass
