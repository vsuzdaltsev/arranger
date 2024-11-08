'''
# `aws_appmesh_virtual_service`

Refer to the Terraform Registory for docs: [`aws_appmesh_virtual_service`](https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service).
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


class AppmeshVirtualService(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualService.AppmeshVirtualService",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service aws_appmesh_virtual_service}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        mesh_name: builtins.str,
        name: builtins.str,
        spec: typing.Union["AppmeshVirtualServiceSpec", typing.Dict[builtins.str, typing.Any]],
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service aws_appmesh_virtual_service} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param mesh_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service#mesh_name AppmeshVirtualService#mesh_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service#name AppmeshVirtualService#name}.
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service#spec AppmeshVirtualService#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service#id AppmeshVirtualService#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mesh_owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service#mesh_owner AppmeshVirtualService#mesh_owner}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service#tags AppmeshVirtualService#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service#tags_all AppmeshVirtualService#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e22c21bf38933e9a56fab112cb15e538646be07c574038b11352122965700902)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AppmeshVirtualServiceConfig(
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
        provider: typing.Optional[typing.Union["AppmeshVirtualServiceSpecProvider", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param provider: provider block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service#provider AppmeshVirtualService#provider}
        '''
        value = AppmeshVirtualServiceSpec(provider=provider)

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
    def spec(self) -> "AppmeshVirtualServiceSpecOutputReference":
        return typing.cast("AppmeshVirtualServiceSpecOutputReference", jsii.get(self, "spec"))

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
    def spec_input(self) -> typing.Optional["AppmeshVirtualServiceSpec"]:
        return typing.cast(typing.Optional["AppmeshVirtualServiceSpec"], jsii.get(self, "specInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__6c01972a22fb94929ec60ab5a3ba4b059ab628761ffb873f019ec9610ab9d287)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="meshName")
    def mesh_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "meshName"))

    @mesh_name.setter
    def mesh_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__872ed426f5bba0cd105c8aa9728291dc3b0a0f0cfd7e362a7a76a3dfd5717314)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "meshName", value)

    @builtins.property
    @jsii.member(jsii_name="meshOwner")
    def mesh_owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "meshOwner"))

    @mesh_owner.setter
    def mesh_owner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0a03873c7fae434813771e88a9e47e72720e620021eb54d66b8a89a311d0f51)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "meshOwner", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea46f5263da53ddbf5e8d0b4865e10757d22e02eecce9e8a643f03d02fd8c343)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__816d342ff7e47fef244a5d19aec10c6482ba592ac28d009f8e2785b6e13ad662)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7fba5efc19940454ee23dbb47d4b1b6964aa09a15f179d1e2d1c4a772edfeca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualService.AppmeshVirtualServiceConfig",
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
class AppmeshVirtualServiceConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        spec: typing.Union["AppmeshVirtualServiceSpec", typing.Dict[builtins.str, typing.Any]],
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
        :param mesh_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service#mesh_name AppmeshVirtualService#mesh_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service#name AppmeshVirtualService#name}.
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service#spec AppmeshVirtualService#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service#id AppmeshVirtualService#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mesh_owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service#mesh_owner AppmeshVirtualService#mesh_owner}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service#tags AppmeshVirtualService#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service#tags_all AppmeshVirtualService#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(spec, dict):
            spec = AppmeshVirtualServiceSpec(**spec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__630871f23f245fab7395ea4caf899be9cf0ed649badf63076211b98de24e356b)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service#mesh_name AppmeshVirtualService#mesh_name}.'''
        result = self._values.get("mesh_name")
        assert result is not None, "Required property 'mesh_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service#name AppmeshVirtualService#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def spec(self) -> "AppmeshVirtualServiceSpec":
        '''spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service#spec AppmeshVirtualService#spec}
        '''
        result = self._values.get("spec")
        assert result is not None, "Required property 'spec' is missing"
        return typing.cast("AppmeshVirtualServiceSpec", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service#id AppmeshVirtualService#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mesh_owner(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service#mesh_owner AppmeshVirtualService#mesh_owner}.'''
        result = self._values.get("mesh_owner")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service#tags AppmeshVirtualService#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service#tags_all AppmeshVirtualService#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualServiceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.appmeshVirtualService.AppmeshVirtualServiceSpec",
    jsii_struct_bases=[],
    name_mapping={"provider": "provider"},
)
class AppmeshVirtualServiceSpec:
    def __init__(
        self,
        *,
        provider: typing.Optional[typing.Union["AppmeshVirtualServiceSpecProvider", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param provider: provider block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service#provider AppmeshVirtualService#provider}
        '''
        if isinstance(provider, dict):
            provider = AppmeshVirtualServiceSpecProvider(**provider)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16ccc97a668bc7ffdd3e77e15a334acc5344fee8ad8cb09d8fd7669729959716)
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if provider is not None:
            self._values["provider"] = provider

    @builtins.property
    def provider(self) -> typing.Optional["AppmeshVirtualServiceSpecProvider"]:
        '''provider block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service#provider AppmeshVirtualService#provider}
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional["AppmeshVirtualServiceSpecProvider"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualServiceSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualServiceSpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualService.AppmeshVirtualServiceSpecOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9c18dcd6a61af53afd571ddbc537903bda6ed413cbfaec4ff486d842531d6bef)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putProvider")
    def put_provider(
        self,
        *,
        virtual_node: typing.Optional[typing.Union["AppmeshVirtualServiceSpecProviderVirtualNode", typing.Dict[builtins.str, typing.Any]]] = None,
        virtual_router: typing.Optional[typing.Union["AppmeshVirtualServiceSpecProviderVirtualRouter", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param virtual_node: virtual_node block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service#virtual_node AppmeshVirtualService#virtual_node}
        :param virtual_router: virtual_router block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service#virtual_router AppmeshVirtualService#virtual_router}
        '''
        value = AppmeshVirtualServiceSpecProvider(
            virtual_node=virtual_node, virtual_router=virtual_router
        )

        return typing.cast(None, jsii.invoke(self, "putProvider", [value]))

    @jsii.member(jsii_name="resetProvider")
    def reset_provider(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProvider", []))

    @builtins.property
    @jsii.member(jsii_name="provider")
    def provider(self) -> "AppmeshVirtualServiceSpecProviderOutputReference":
        return typing.cast("AppmeshVirtualServiceSpecProviderOutputReference", jsii.get(self, "provider"))

    @builtins.property
    @jsii.member(jsii_name="providerInput")
    def provider_input(self) -> typing.Optional["AppmeshVirtualServiceSpecProvider"]:
        return typing.cast(typing.Optional["AppmeshVirtualServiceSpecProvider"], jsii.get(self, "providerInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshVirtualServiceSpec]:
        return typing.cast(typing.Optional[AppmeshVirtualServiceSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppmeshVirtualServiceSpec]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4198cfdf16a23fc44968b66dc4aec791087bcec487f68cfa17cf22fb8c17451)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualService.AppmeshVirtualServiceSpecProvider",
    jsii_struct_bases=[],
    name_mapping={"virtual_node": "virtualNode", "virtual_router": "virtualRouter"},
)
class AppmeshVirtualServiceSpecProvider:
    def __init__(
        self,
        *,
        virtual_node: typing.Optional[typing.Union["AppmeshVirtualServiceSpecProviderVirtualNode", typing.Dict[builtins.str, typing.Any]]] = None,
        virtual_router: typing.Optional[typing.Union["AppmeshVirtualServiceSpecProviderVirtualRouter", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param virtual_node: virtual_node block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service#virtual_node AppmeshVirtualService#virtual_node}
        :param virtual_router: virtual_router block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service#virtual_router AppmeshVirtualService#virtual_router}
        '''
        if isinstance(virtual_node, dict):
            virtual_node = AppmeshVirtualServiceSpecProviderVirtualNode(**virtual_node)
        if isinstance(virtual_router, dict):
            virtual_router = AppmeshVirtualServiceSpecProviderVirtualRouter(**virtual_router)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88618b8ef8219b2c743b0b5a55fd7c3f6d7745a267d90fb31ce3e2b97e6196ff)
            check_type(argname="argument virtual_node", value=virtual_node, expected_type=type_hints["virtual_node"])
            check_type(argname="argument virtual_router", value=virtual_router, expected_type=type_hints["virtual_router"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if virtual_node is not None:
            self._values["virtual_node"] = virtual_node
        if virtual_router is not None:
            self._values["virtual_router"] = virtual_router

    @builtins.property
    def virtual_node(
        self,
    ) -> typing.Optional["AppmeshVirtualServiceSpecProviderVirtualNode"]:
        '''virtual_node block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service#virtual_node AppmeshVirtualService#virtual_node}
        '''
        result = self._values.get("virtual_node")
        return typing.cast(typing.Optional["AppmeshVirtualServiceSpecProviderVirtualNode"], result)

    @builtins.property
    def virtual_router(
        self,
    ) -> typing.Optional["AppmeshVirtualServiceSpecProviderVirtualRouter"]:
        '''virtual_router block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service#virtual_router AppmeshVirtualService#virtual_router}
        '''
        result = self._values.get("virtual_router")
        return typing.cast(typing.Optional["AppmeshVirtualServiceSpecProviderVirtualRouter"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualServiceSpecProvider(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualServiceSpecProviderOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualService.AppmeshVirtualServiceSpecProviderOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__73226c6eac311d831a529b8a4866c9e087e06340aae6a9cfade11b7a7b94b426)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putVirtualNode")
    def put_virtual_node(self, *, virtual_node_name: builtins.str) -> None:
        '''
        :param virtual_node_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service#virtual_node_name AppmeshVirtualService#virtual_node_name}.
        '''
        value = AppmeshVirtualServiceSpecProviderVirtualNode(
            virtual_node_name=virtual_node_name
        )

        return typing.cast(None, jsii.invoke(self, "putVirtualNode", [value]))

    @jsii.member(jsii_name="putVirtualRouter")
    def put_virtual_router(self, *, virtual_router_name: builtins.str) -> None:
        '''
        :param virtual_router_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service#virtual_router_name AppmeshVirtualService#virtual_router_name}.
        '''
        value = AppmeshVirtualServiceSpecProviderVirtualRouter(
            virtual_router_name=virtual_router_name
        )

        return typing.cast(None, jsii.invoke(self, "putVirtualRouter", [value]))

    @jsii.member(jsii_name="resetVirtualNode")
    def reset_virtual_node(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualNode", []))

    @jsii.member(jsii_name="resetVirtualRouter")
    def reset_virtual_router(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualRouter", []))

    @builtins.property
    @jsii.member(jsii_name="virtualNode")
    def virtual_node(
        self,
    ) -> "AppmeshVirtualServiceSpecProviderVirtualNodeOutputReference":
        return typing.cast("AppmeshVirtualServiceSpecProviderVirtualNodeOutputReference", jsii.get(self, "virtualNode"))

    @builtins.property
    @jsii.member(jsii_name="virtualRouter")
    def virtual_router(
        self,
    ) -> "AppmeshVirtualServiceSpecProviderVirtualRouterOutputReference":
        return typing.cast("AppmeshVirtualServiceSpecProviderVirtualRouterOutputReference", jsii.get(self, "virtualRouter"))

    @builtins.property
    @jsii.member(jsii_name="virtualNodeInput")
    def virtual_node_input(
        self,
    ) -> typing.Optional["AppmeshVirtualServiceSpecProviderVirtualNode"]:
        return typing.cast(typing.Optional["AppmeshVirtualServiceSpecProviderVirtualNode"], jsii.get(self, "virtualNodeInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualRouterInput")
    def virtual_router_input(
        self,
    ) -> typing.Optional["AppmeshVirtualServiceSpecProviderVirtualRouter"]:
        return typing.cast(typing.Optional["AppmeshVirtualServiceSpecProviderVirtualRouter"], jsii.get(self, "virtualRouterInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppmeshVirtualServiceSpecProvider]:
        return typing.cast(typing.Optional[AppmeshVirtualServiceSpecProvider], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualServiceSpecProvider],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06f5eb686ca7a7adfbe15fb3cbaa74f3f8a09f80937ec4062a1ab9c4a06786b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualService.AppmeshVirtualServiceSpecProviderVirtualNode",
    jsii_struct_bases=[],
    name_mapping={"virtual_node_name": "virtualNodeName"},
)
class AppmeshVirtualServiceSpecProviderVirtualNode:
    def __init__(self, *, virtual_node_name: builtins.str) -> None:
        '''
        :param virtual_node_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service#virtual_node_name AppmeshVirtualService#virtual_node_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__831ec65b23983bfab4ccf26d73427a34644ced82d26d3cb8db8117cf9a2a10a1)
            check_type(argname="argument virtual_node_name", value=virtual_node_name, expected_type=type_hints["virtual_node_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "virtual_node_name": virtual_node_name,
        }

    @builtins.property
    def virtual_node_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service#virtual_node_name AppmeshVirtualService#virtual_node_name}.'''
        result = self._values.get("virtual_node_name")
        assert result is not None, "Required property 'virtual_node_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualServiceSpecProviderVirtualNode(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualServiceSpecProviderVirtualNodeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualService.AppmeshVirtualServiceSpecProviderVirtualNodeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b44036e9fe7d18ca2c9ab6fbec8473f8a4c144e24b70856daa6374eb9bab0e47)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="virtualNodeNameInput")
    def virtual_node_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualNodeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNodeName")
    def virtual_node_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualNodeName"))

    @virtual_node_name.setter
    def virtual_node_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fff2dea4cc6ea48da88e94801ecf236aad76f77aed05c15292c8b21cb492a7c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualNodeName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualServiceSpecProviderVirtualNode]:
        return typing.cast(typing.Optional[AppmeshVirtualServiceSpecProviderVirtualNode], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualServiceSpecProviderVirtualNode],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79d4dc873b9a02f3818fbba43d66fa68ee44940ea3393b51333c11484886cbee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.appmeshVirtualService.AppmeshVirtualServiceSpecProviderVirtualRouter",
    jsii_struct_bases=[],
    name_mapping={"virtual_router_name": "virtualRouterName"},
)
class AppmeshVirtualServiceSpecProviderVirtualRouter:
    def __init__(self, *, virtual_router_name: builtins.str) -> None:
        '''
        :param virtual_router_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service#virtual_router_name AppmeshVirtualService#virtual_router_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae6c77f629d307ea9b6e36d8b70595eb65ff67e691a1f92bf5a92278319c5a14)
            check_type(argname="argument virtual_router_name", value=virtual_router_name, expected_type=type_hints["virtual_router_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "virtual_router_name": virtual_router_name,
        }

    @builtins.property
    def virtual_router_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/appmesh_virtual_service#virtual_router_name AppmeshVirtualService#virtual_router_name}.'''
        result = self._values.get("virtual_router_name")
        assert result is not None, "Required property 'virtual_router_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppmeshVirtualServiceSpecProviderVirtualRouter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppmeshVirtualServiceSpecProviderVirtualRouterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.appmeshVirtualService.AppmeshVirtualServiceSpecProviderVirtualRouterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7d6fffe3895bea2b70d342cf808e65afb895724986973e55e1db2737330dac8d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="virtualRouterNameInput")
    def virtual_router_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualRouterNameInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualRouterName")
    def virtual_router_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualRouterName"))

    @virtual_router_name.setter
    def virtual_router_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02cc849db672314005800e8790ce9b6665d0185508cedc0fae47bd0b564e1030)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualRouterName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppmeshVirtualServiceSpecProviderVirtualRouter]:
        return typing.cast(typing.Optional[AppmeshVirtualServiceSpecProviderVirtualRouter], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppmeshVirtualServiceSpecProviderVirtualRouter],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a548875ad938d50fae9a5344fa0aeff19b11aa661e588296d956b1ca268a922)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AppmeshVirtualService",
    "AppmeshVirtualServiceConfig",
    "AppmeshVirtualServiceSpec",
    "AppmeshVirtualServiceSpecOutputReference",
    "AppmeshVirtualServiceSpecProvider",
    "AppmeshVirtualServiceSpecProviderOutputReference",
    "AppmeshVirtualServiceSpecProviderVirtualNode",
    "AppmeshVirtualServiceSpecProviderVirtualNodeOutputReference",
    "AppmeshVirtualServiceSpecProviderVirtualRouter",
    "AppmeshVirtualServiceSpecProviderVirtualRouterOutputReference",
]

publication.publish()

def _typecheckingstub__e22c21bf38933e9a56fab112cb15e538646be07c574038b11352122965700902(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    mesh_name: builtins.str,
    name: builtins.str,
    spec: typing.Union[AppmeshVirtualServiceSpec, typing.Dict[builtins.str, typing.Any]],
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

def _typecheckingstub__6c01972a22fb94929ec60ab5a3ba4b059ab628761ffb873f019ec9610ab9d287(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__872ed426f5bba0cd105c8aa9728291dc3b0a0f0cfd7e362a7a76a3dfd5717314(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0a03873c7fae434813771e88a9e47e72720e620021eb54d66b8a89a311d0f51(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea46f5263da53ddbf5e8d0b4865e10757d22e02eecce9e8a643f03d02fd8c343(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__816d342ff7e47fef244a5d19aec10c6482ba592ac28d009f8e2785b6e13ad662(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7fba5efc19940454ee23dbb47d4b1b6964aa09a15f179d1e2d1c4a772edfeca(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__630871f23f245fab7395ea4caf899be9cf0ed649badf63076211b98de24e356b(
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
    spec: typing.Union[AppmeshVirtualServiceSpec, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
    mesh_owner: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16ccc97a668bc7ffdd3e77e15a334acc5344fee8ad8cb09d8fd7669729959716(
    *,
    provider: typing.Optional[typing.Union[AppmeshVirtualServiceSpecProvider, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c18dcd6a61af53afd571ddbc537903bda6ed413cbfaec4ff486d842531d6bef(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4198cfdf16a23fc44968b66dc4aec791087bcec487f68cfa17cf22fb8c17451(
    value: typing.Optional[AppmeshVirtualServiceSpec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88618b8ef8219b2c743b0b5a55fd7c3f6d7745a267d90fb31ce3e2b97e6196ff(
    *,
    virtual_node: typing.Optional[typing.Union[AppmeshVirtualServiceSpecProviderVirtualNode, typing.Dict[builtins.str, typing.Any]]] = None,
    virtual_router: typing.Optional[typing.Union[AppmeshVirtualServiceSpecProviderVirtualRouter, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73226c6eac311d831a529b8a4866c9e087e06340aae6a9cfade11b7a7b94b426(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06f5eb686ca7a7adfbe15fb3cbaa74f3f8a09f80937ec4062a1ab9c4a06786b5(
    value: typing.Optional[AppmeshVirtualServiceSpecProvider],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__831ec65b23983bfab4ccf26d73427a34644ced82d26d3cb8db8117cf9a2a10a1(
    *,
    virtual_node_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b44036e9fe7d18ca2c9ab6fbec8473f8a4c144e24b70856daa6374eb9bab0e47(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fff2dea4cc6ea48da88e94801ecf236aad76f77aed05c15292c8b21cb492a7c4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79d4dc873b9a02f3818fbba43d66fa68ee44940ea3393b51333c11484886cbee(
    value: typing.Optional[AppmeshVirtualServiceSpecProviderVirtualNode],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae6c77f629d307ea9b6e36d8b70595eb65ff67e691a1f92bf5a92278319c5a14(
    *,
    virtual_router_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d6fffe3895bea2b70d342cf808e65afb895724986973e55e1db2737330dac8d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02cc849db672314005800e8790ce9b6665d0185508cedc0fae47bd0b564e1030(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a548875ad938d50fae9a5344fa0aeff19b11aa661e588296d956b1ca268a922(
    value: typing.Optional[AppmeshVirtualServiceSpecProviderVirtualRouter],
) -> None:
    """Type checking stubs"""
    pass
