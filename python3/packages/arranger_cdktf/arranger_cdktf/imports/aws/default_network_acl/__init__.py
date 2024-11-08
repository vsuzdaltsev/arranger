'''
# `aws_default_network_acl`

Refer to the Terraform Registory for docs: [`aws_default_network_acl`](https://www.terraform.io/docs/providers/aws/r/default_network_acl).
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


class DefaultNetworkAcl(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.defaultNetworkAcl.DefaultNetworkAcl",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl aws_default_network_acl}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        default_network_acl_id: builtins.str,
        egress: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DefaultNetworkAclEgress", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        ingress: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DefaultNetworkAclIngress", typing.Dict[builtins.str, typing.Any]]]]] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl aws_default_network_acl} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param default_network_acl_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#default_network_acl_id DefaultNetworkAcl#default_network_acl_id}.
        :param egress: egress block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#egress DefaultNetworkAcl#egress}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#id DefaultNetworkAcl#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ingress: ingress block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#ingress DefaultNetworkAcl#ingress}
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#subnet_ids DefaultNetworkAcl#subnet_ids}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#tags DefaultNetworkAcl#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#tags_all DefaultNetworkAcl#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e06420262f0fd1681df88de7c9a122b1c45ba5b97ad2eb7bd66c059e0caa1a6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DefaultNetworkAclConfig(
            default_network_acl_id=default_network_acl_id,
            egress=egress,
            id=id,
            ingress=ingress,
            subnet_ids=subnet_ids,
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

    @jsii.member(jsii_name="putEgress")
    def put_egress(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DefaultNetworkAclEgress", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__040e7a41164454b08e85a481d1346794bf1f90c6249e0683e3c1665efc67c932)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEgress", [value]))

    @jsii.member(jsii_name="putIngress")
    def put_ingress(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DefaultNetworkAclIngress", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__691b3ba1d8d24c68259a0e9c7d2436e028d35ad1a4506f377aeaa2f43cef1fab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIngress", [value]))

    @jsii.member(jsii_name="resetEgress")
    def reset_egress(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEgress", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIngress")
    def reset_ingress(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIngress", []))

    @jsii.member(jsii_name="resetSubnetIds")
    def reset_subnet_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetIds", []))

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
    @jsii.member(jsii_name="egress")
    def egress(self) -> "DefaultNetworkAclEgressList":
        return typing.cast("DefaultNetworkAclEgressList", jsii.get(self, "egress"))

    @builtins.property
    @jsii.member(jsii_name="ingress")
    def ingress(self) -> "DefaultNetworkAclIngressList":
        return typing.cast("DefaultNetworkAclIngressList", jsii.get(self, "ingress"))

    @builtins.property
    @jsii.member(jsii_name="ownerId")
    def owner_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ownerId"))

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @builtins.property
    @jsii.member(jsii_name="defaultNetworkAclIdInput")
    def default_network_acl_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultNetworkAclIdInput"))

    @builtins.property
    @jsii.member(jsii_name="egressInput")
    def egress_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DefaultNetworkAclEgress"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DefaultNetworkAclEgress"]]], jsii.get(self, "egressInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ingressInput")
    def ingress_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DefaultNetworkAclIngress"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DefaultNetworkAclIngress"]]], jsii.get(self, "ingressInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdsInput")
    def subnet_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetIdsInput"))

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
    @jsii.member(jsii_name="defaultNetworkAclId")
    def default_network_acl_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultNetworkAclId"))

    @default_network_acl_id.setter
    def default_network_acl_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__367a0ac89f50e9cbf61a0b409d1f16e1f30e36cd94b55db32adde8f948a96992)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultNetworkAclId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da804a036c4fdd2db89fa49e6a68b5769aacff8af025163d5f3457722f19fbee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54cd1669b9cfd6c51d3dff845371a1099f8e6b3ec72e9c7db00c301cdc658544)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a146872edc4cd1cf4bb0dd10ea6b65c0045bd4e4bdc43263979c92b17d0d7cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88b57250cfdfd3e2099636dfa7d80f27965f0579c053e38b8c38beecdaf149de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.defaultNetworkAcl.DefaultNetworkAclConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "default_network_acl_id": "defaultNetworkAclId",
        "egress": "egress",
        "id": "id",
        "ingress": "ingress",
        "subnet_ids": "subnetIds",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class DefaultNetworkAclConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        default_network_acl_id: builtins.str,
        egress: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DefaultNetworkAclEgress", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        ingress: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DefaultNetworkAclIngress", typing.Dict[builtins.str, typing.Any]]]]] = None,
        subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
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
        :param default_network_acl_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#default_network_acl_id DefaultNetworkAcl#default_network_acl_id}.
        :param egress: egress block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#egress DefaultNetworkAcl#egress}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#id DefaultNetworkAcl#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ingress: ingress block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#ingress DefaultNetworkAcl#ingress}
        :param subnet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#subnet_ids DefaultNetworkAcl#subnet_ids}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#tags DefaultNetworkAcl#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#tags_all DefaultNetworkAcl#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6aa831285f2837924eb108d26ea45131c98faf7062993148466a850837975952)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument default_network_acl_id", value=default_network_acl_id, expected_type=type_hints["default_network_acl_id"])
            check_type(argname="argument egress", value=egress, expected_type=type_hints["egress"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ingress", value=ingress, expected_type=type_hints["ingress"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "default_network_acl_id": default_network_acl_id,
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
        if egress is not None:
            self._values["egress"] = egress
        if id is not None:
            self._values["id"] = id
        if ingress is not None:
            self._values["ingress"] = ingress
        if subnet_ids is not None:
            self._values["subnet_ids"] = subnet_ids
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
    def default_network_acl_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#default_network_acl_id DefaultNetworkAcl#default_network_acl_id}.'''
        result = self._values.get("default_network_acl_id")
        assert result is not None, "Required property 'default_network_acl_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def egress(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DefaultNetworkAclEgress"]]]:
        '''egress block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#egress DefaultNetworkAcl#egress}
        '''
        result = self._values.get("egress")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DefaultNetworkAclEgress"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#id DefaultNetworkAcl#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ingress(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DefaultNetworkAclIngress"]]]:
        '''ingress block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#ingress DefaultNetworkAcl#ingress}
        '''
        result = self._values.get("ingress")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DefaultNetworkAclIngress"]]], result)

    @builtins.property
    def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#subnet_ids DefaultNetworkAcl#subnet_ids}.'''
        result = self._values.get("subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#tags DefaultNetworkAcl#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#tags_all DefaultNetworkAcl#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DefaultNetworkAclConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.defaultNetworkAcl.DefaultNetworkAclEgress",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "from_port": "fromPort",
        "protocol": "protocol",
        "rule_no": "ruleNo",
        "to_port": "toPort",
        "cidr_block": "cidrBlock",
        "icmp_code": "icmpCode",
        "icmp_type": "icmpType",
        "ipv6_cidr_block": "ipv6CidrBlock",
    },
)
class DefaultNetworkAclEgress:
    def __init__(
        self,
        *,
        action: builtins.str,
        from_port: jsii.Number,
        protocol: builtins.str,
        rule_no: jsii.Number,
        to_port: jsii.Number,
        cidr_block: typing.Optional[builtins.str] = None,
        icmp_code: typing.Optional[jsii.Number] = None,
        icmp_type: typing.Optional[jsii.Number] = None,
        ipv6_cidr_block: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#action DefaultNetworkAcl#action}.
        :param from_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#from_port DefaultNetworkAcl#from_port}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#protocol DefaultNetworkAcl#protocol}.
        :param rule_no: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#rule_no DefaultNetworkAcl#rule_no}.
        :param to_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#to_port DefaultNetworkAcl#to_port}.
        :param cidr_block: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#cidr_block DefaultNetworkAcl#cidr_block}.
        :param icmp_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#icmp_code DefaultNetworkAcl#icmp_code}.
        :param icmp_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#icmp_type DefaultNetworkAcl#icmp_type}.
        :param ipv6_cidr_block: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#ipv6_cidr_block DefaultNetworkAcl#ipv6_cidr_block}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6665954aef7bd61edf87ea9aa84e5c2069f2baa23f93b5788e038ada3894ae05)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument from_port", value=from_port, expected_type=type_hints["from_port"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument rule_no", value=rule_no, expected_type=type_hints["rule_no"])
            check_type(argname="argument to_port", value=to_port, expected_type=type_hints["to_port"])
            check_type(argname="argument cidr_block", value=cidr_block, expected_type=type_hints["cidr_block"])
            check_type(argname="argument icmp_code", value=icmp_code, expected_type=type_hints["icmp_code"])
            check_type(argname="argument icmp_type", value=icmp_type, expected_type=type_hints["icmp_type"])
            check_type(argname="argument ipv6_cidr_block", value=ipv6_cidr_block, expected_type=type_hints["ipv6_cidr_block"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action": action,
            "from_port": from_port,
            "protocol": protocol,
            "rule_no": rule_no,
            "to_port": to_port,
        }
        if cidr_block is not None:
            self._values["cidr_block"] = cidr_block
        if icmp_code is not None:
            self._values["icmp_code"] = icmp_code
        if icmp_type is not None:
            self._values["icmp_type"] = icmp_type
        if ipv6_cidr_block is not None:
            self._values["ipv6_cidr_block"] = ipv6_cidr_block

    @builtins.property
    def action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#action DefaultNetworkAcl#action}.'''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def from_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#from_port DefaultNetworkAcl#from_port}.'''
        result = self._values.get("from_port")
        assert result is not None, "Required property 'from_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#protocol DefaultNetworkAcl#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_no(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#rule_no DefaultNetworkAcl#rule_no}.'''
        result = self._values.get("rule_no")
        assert result is not None, "Required property 'rule_no' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def to_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#to_port DefaultNetworkAcl#to_port}.'''
        result = self._values.get("to_port")
        assert result is not None, "Required property 'to_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def cidr_block(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#cidr_block DefaultNetworkAcl#cidr_block}.'''
        result = self._values.get("cidr_block")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def icmp_code(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#icmp_code DefaultNetworkAcl#icmp_code}.'''
        result = self._values.get("icmp_code")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def icmp_type(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#icmp_type DefaultNetworkAcl#icmp_type}.'''
        result = self._values.get("icmp_type")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ipv6_cidr_block(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#ipv6_cidr_block DefaultNetworkAcl#ipv6_cidr_block}.'''
        result = self._values.get("ipv6_cidr_block")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DefaultNetworkAclEgress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DefaultNetworkAclEgressList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.defaultNetworkAcl.DefaultNetworkAclEgressList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b4d9ea6bf97e958984ea62993c8bbf2102ab9d4b50814b6ac96f69e6ef281693)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DefaultNetworkAclEgressOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7d4e224ddcefdf1d325d1215b48f07db49adfbda79a1526732ddf1b7440ebb6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DefaultNetworkAclEgressOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c43cc90f8b31fdf78c733e96e9b881d9789de8bceae6941b210560a659c812bf)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5cfd4e0257d10ca6f10cafa4dcba3ad1dda9ed153c86d41d103e37c2a91be711)
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
            type_hints = typing.get_type_hints(_typecheckingstub__aa809fec3d97ddcf4524cc9414a7935f1624d2a4b1767a6d1c3b751c3b34eec1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DefaultNetworkAclEgress]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DefaultNetworkAclEgress]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DefaultNetworkAclEgress]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88e70c3daec3f2cc7692d263f73a15f3b51f379796564c4644e08565d5592c4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DefaultNetworkAclEgressOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.defaultNetworkAcl.DefaultNetworkAclEgressOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7dd4c4809deca6e9e7d271feae8ac31fb3d3c68c417a9c19f5a441d60dd387a9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCidrBlock")
    def reset_cidr_block(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCidrBlock", []))

    @jsii.member(jsii_name="resetIcmpCode")
    def reset_icmp_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIcmpCode", []))

    @jsii.member(jsii_name="resetIcmpType")
    def reset_icmp_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIcmpType", []))

    @jsii.member(jsii_name="resetIpv6CidrBlock")
    def reset_ipv6_cidr_block(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpv6CidrBlock", []))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="cidrBlockInput")
    def cidr_block_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cidrBlockInput"))

    @builtins.property
    @jsii.member(jsii_name="fromPortInput")
    def from_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "fromPortInput"))

    @builtins.property
    @jsii.member(jsii_name="icmpCodeInput")
    def icmp_code_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "icmpCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="icmpTypeInput")
    def icmp_type_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "icmpTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv6CidrBlockInput")
    def ipv6_cidr_block_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipv6CidrBlockInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleNoInput")
    def rule_no_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ruleNoInput"))

    @builtins.property
    @jsii.member(jsii_name="toPortInput")
    def to_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "toPortInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ad6b6ea93cad050c00ce3672fa543f250d84661bd334d0e872ee20d3f0ca0e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="cidrBlock")
    def cidr_block(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cidrBlock"))

    @cidr_block.setter
    def cidr_block(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11cc7ea7f1547ba82960cfd2bcb6b7d79c2545f8c4e3cef616041184b2b8ce7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cidrBlock", value)

    @builtins.property
    @jsii.member(jsii_name="fromPort")
    def from_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "fromPort"))

    @from_port.setter
    def from_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73bd54de21816822f6c330bde946b8420ab1647a724492e2c4246f905ddf836a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fromPort", value)

    @builtins.property
    @jsii.member(jsii_name="icmpCode")
    def icmp_code(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "icmpCode"))

    @icmp_code.setter
    def icmp_code(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1ec0b71fca39ef166f23d954bd2b57894cef1260c69f852e158f25bfb261c11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "icmpCode", value)

    @builtins.property
    @jsii.member(jsii_name="icmpType")
    def icmp_type(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "icmpType"))

    @icmp_type.setter
    def icmp_type(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4afd37e455c5604793d48b9498b2f7ab07fee6cd7672196b23c424a9bb3dc0d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "icmpType", value)

    @builtins.property
    @jsii.member(jsii_name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipv6CidrBlock"))

    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c586c7bc8814c16562d43ac1d830989f82964c7581d512281a0e265e84c0366)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv6CidrBlock", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b68b9a1b31efc2c9e52211cbf3b267ea8485bfe814ce47daa52d05fd695258b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="ruleNo")
    def rule_no(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ruleNo"))

    @rule_no.setter
    def rule_no(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90eefe2c149cd1b9ac282a522d2642d29e8c53ecc1fde31146dda54c91261b43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleNo", value)

    @builtins.property
    @jsii.member(jsii_name="toPort")
    def to_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "toPort"))

    @to_port.setter
    def to_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f85307adb584e7af65b48a4f9db2cf936361235be3d514172c6adc94fc464ff3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "toPort", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DefaultNetworkAclEgress, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DefaultNetworkAclEgress, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DefaultNetworkAclEgress, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0332a04dac9f9f0633ac424e19e83866baa8c164e7be3a92479eeae0f0ac9b3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.defaultNetworkAcl.DefaultNetworkAclIngress",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "from_port": "fromPort",
        "protocol": "protocol",
        "rule_no": "ruleNo",
        "to_port": "toPort",
        "cidr_block": "cidrBlock",
        "icmp_code": "icmpCode",
        "icmp_type": "icmpType",
        "ipv6_cidr_block": "ipv6CidrBlock",
    },
)
class DefaultNetworkAclIngress:
    def __init__(
        self,
        *,
        action: builtins.str,
        from_port: jsii.Number,
        protocol: builtins.str,
        rule_no: jsii.Number,
        to_port: jsii.Number,
        cidr_block: typing.Optional[builtins.str] = None,
        icmp_code: typing.Optional[jsii.Number] = None,
        icmp_type: typing.Optional[jsii.Number] = None,
        ipv6_cidr_block: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#action DefaultNetworkAcl#action}.
        :param from_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#from_port DefaultNetworkAcl#from_port}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#protocol DefaultNetworkAcl#protocol}.
        :param rule_no: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#rule_no DefaultNetworkAcl#rule_no}.
        :param to_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#to_port DefaultNetworkAcl#to_port}.
        :param cidr_block: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#cidr_block DefaultNetworkAcl#cidr_block}.
        :param icmp_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#icmp_code DefaultNetworkAcl#icmp_code}.
        :param icmp_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#icmp_type DefaultNetworkAcl#icmp_type}.
        :param ipv6_cidr_block: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#ipv6_cidr_block DefaultNetworkAcl#ipv6_cidr_block}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__979ba7eb4323e55e482ea7d723babb51724c1f02aefee825d9eb5957b95e3a4c)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument from_port", value=from_port, expected_type=type_hints["from_port"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument rule_no", value=rule_no, expected_type=type_hints["rule_no"])
            check_type(argname="argument to_port", value=to_port, expected_type=type_hints["to_port"])
            check_type(argname="argument cidr_block", value=cidr_block, expected_type=type_hints["cidr_block"])
            check_type(argname="argument icmp_code", value=icmp_code, expected_type=type_hints["icmp_code"])
            check_type(argname="argument icmp_type", value=icmp_type, expected_type=type_hints["icmp_type"])
            check_type(argname="argument ipv6_cidr_block", value=ipv6_cidr_block, expected_type=type_hints["ipv6_cidr_block"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action": action,
            "from_port": from_port,
            "protocol": protocol,
            "rule_no": rule_no,
            "to_port": to_port,
        }
        if cidr_block is not None:
            self._values["cidr_block"] = cidr_block
        if icmp_code is not None:
            self._values["icmp_code"] = icmp_code
        if icmp_type is not None:
            self._values["icmp_type"] = icmp_type
        if ipv6_cidr_block is not None:
            self._values["ipv6_cidr_block"] = ipv6_cidr_block

    @builtins.property
    def action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#action DefaultNetworkAcl#action}.'''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def from_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#from_port DefaultNetworkAcl#from_port}.'''
        result = self._values.get("from_port")
        assert result is not None, "Required property 'from_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#protocol DefaultNetworkAcl#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_no(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#rule_no DefaultNetworkAcl#rule_no}.'''
        result = self._values.get("rule_no")
        assert result is not None, "Required property 'rule_no' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def to_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#to_port DefaultNetworkAcl#to_port}.'''
        result = self._values.get("to_port")
        assert result is not None, "Required property 'to_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def cidr_block(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#cidr_block DefaultNetworkAcl#cidr_block}.'''
        result = self._values.get("cidr_block")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def icmp_code(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#icmp_code DefaultNetworkAcl#icmp_code}.'''
        result = self._values.get("icmp_code")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def icmp_type(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#icmp_type DefaultNetworkAcl#icmp_type}.'''
        result = self._values.get("icmp_type")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ipv6_cidr_block(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/default_network_acl#ipv6_cidr_block DefaultNetworkAcl#ipv6_cidr_block}.'''
        result = self._values.get("ipv6_cidr_block")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DefaultNetworkAclIngress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DefaultNetworkAclIngressList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.defaultNetworkAcl.DefaultNetworkAclIngressList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d221babb5d4870051c4202e4dea65913589407561a9c3beeb6de8a9a0802505c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DefaultNetworkAclIngressOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b445eb9073b0dc62dd4e4fd3c8aad9ba35d0d0d8195736db5edc6b16606a6c5)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DefaultNetworkAclIngressOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c837509e35a1b8858933943cf627097a3142c0294e40c51467a0a2ae4aae589b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8282ec8a9fdc88446ae3ca2dff7c66a539697b0d3684aeeb7e2cfee6c749df9b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4e0567d34c0afb04007bd76ea18ce36ffc6e69d2cd27cf99e2cb3f267eb11a67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DefaultNetworkAclIngress]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DefaultNetworkAclIngress]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DefaultNetworkAclIngress]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3938336a5e34b3e9f2fd577676ff96bdf8793be8e56e76f2a1fb8114ace77904)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DefaultNetworkAclIngressOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.defaultNetworkAcl.DefaultNetworkAclIngressOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__65acd4d22564d9a285b154474dfb1fb2c470b3bc2dd72a8a936393de78f80956)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCidrBlock")
    def reset_cidr_block(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCidrBlock", []))

    @jsii.member(jsii_name="resetIcmpCode")
    def reset_icmp_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIcmpCode", []))

    @jsii.member(jsii_name="resetIcmpType")
    def reset_icmp_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIcmpType", []))

    @jsii.member(jsii_name="resetIpv6CidrBlock")
    def reset_ipv6_cidr_block(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpv6CidrBlock", []))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="cidrBlockInput")
    def cidr_block_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cidrBlockInput"))

    @builtins.property
    @jsii.member(jsii_name="fromPortInput")
    def from_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "fromPortInput"))

    @builtins.property
    @jsii.member(jsii_name="icmpCodeInput")
    def icmp_code_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "icmpCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="icmpTypeInput")
    def icmp_type_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "icmpTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv6CidrBlockInput")
    def ipv6_cidr_block_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipv6CidrBlockInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleNoInput")
    def rule_no_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ruleNoInput"))

    @builtins.property
    @jsii.member(jsii_name="toPortInput")
    def to_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "toPortInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e4d790315f5e29ed6f67743c9e806c26e5e896e83bb245142304b327e73f337)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="cidrBlock")
    def cidr_block(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cidrBlock"))

    @cidr_block.setter
    def cidr_block(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2fe2ffeb963fa7ce172f81dcd993029efb53a342863e0efa987293bd663f165)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cidrBlock", value)

    @builtins.property
    @jsii.member(jsii_name="fromPort")
    def from_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "fromPort"))

    @from_port.setter
    def from_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2642ece1d6fa666d283a26d8c89861308cc9eefeefb2f1a5c279243f8ec1d74e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fromPort", value)

    @builtins.property
    @jsii.member(jsii_name="icmpCode")
    def icmp_code(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "icmpCode"))

    @icmp_code.setter
    def icmp_code(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__156595b117668394d7f391a0e61cb0bf1b6cbbf9057200892be171cbf1e7480d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "icmpCode", value)

    @builtins.property
    @jsii.member(jsii_name="icmpType")
    def icmp_type(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "icmpType"))

    @icmp_type.setter
    def icmp_type(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__554f58b287c4ad99e99a1a778598764ea2c93aa40a86f09334b0e14c0fd1afff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "icmpType", value)

    @builtins.property
    @jsii.member(jsii_name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipv6CidrBlock"))

    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05b01a0c9e47b674d66696160b3425369855fe496c8a0996e64516298262109d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv6CidrBlock", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__173433035bc06d7c653d6d0c8e0c52545f5d4a8462141c0a70437ce2edb7d8e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="ruleNo")
    def rule_no(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ruleNo"))

    @rule_no.setter
    def rule_no(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54cd5166d5f56559edb3916c3d22d9bc1ea574c687eb4c1b8c7b3353062d4ce6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleNo", value)

    @builtins.property
    @jsii.member(jsii_name="toPort")
    def to_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "toPort"))

    @to_port.setter
    def to_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8aea658a8e421cc8649df9657aac541940c735869ad8eed7525767d4654b58f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "toPort", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DefaultNetworkAclIngress, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DefaultNetworkAclIngress, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DefaultNetworkAclIngress, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cbc35ad7d09935ffc2165690902528bb850de44b4760f902ad3182825ad7766)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DefaultNetworkAcl",
    "DefaultNetworkAclConfig",
    "DefaultNetworkAclEgress",
    "DefaultNetworkAclEgressList",
    "DefaultNetworkAclEgressOutputReference",
    "DefaultNetworkAclIngress",
    "DefaultNetworkAclIngressList",
    "DefaultNetworkAclIngressOutputReference",
]

publication.publish()

def _typecheckingstub__8e06420262f0fd1681df88de7c9a122b1c45ba5b97ad2eb7bd66c059e0caa1a6(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    default_network_acl_id: builtins.str,
    egress: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DefaultNetworkAclEgress, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    ingress: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DefaultNetworkAclIngress, typing.Dict[builtins.str, typing.Any]]]]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
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

def _typecheckingstub__040e7a41164454b08e85a481d1346794bf1f90c6249e0683e3c1665efc67c932(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DefaultNetworkAclEgress, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__691b3ba1d8d24c68259a0e9c7d2436e028d35ad1a4506f377aeaa2f43cef1fab(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DefaultNetworkAclIngress, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__367a0ac89f50e9cbf61a0b409d1f16e1f30e36cd94b55db32adde8f948a96992(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da804a036c4fdd2db89fa49e6a68b5769aacff8af025163d5f3457722f19fbee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54cd1669b9cfd6c51d3dff845371a1099f8e6b3ec72e9c7db00c301cdc658544(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a146872edc4cd1cf4bb0dd10ea6b65c0045bd4e4bdc43263979c92b17d0d7cb(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88b57250cfdfd3e2099636dfa7d80f27965f0579c053e38b8c38beecdaf149de(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6aa831285f2837924eb108d26ea45131c98faf7062993148466a850837975952(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    default_network_acl_id: builtins.str,
    egress: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DefaultNetworkAclEgress, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    ingress: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DefaultNetworkAclIngress, typing.Dict[builtins.str, typing.Any]]]]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6665954aef7bd61edf87ea9aa84e5c2069f2baa23f93b5788e038ada3894ae05(
    *,
    action: builtins.str,
    from_port: jsii.Number,
    protocol: builtins.str,
    rule_no: jsii.Number,
    to_port: jsii.Number,
    cidr_block: typing.Optional[builtins.str] = None,
    icmp_code: typing.Optional[jsii.Number] = None,
    icmp_type: typing.Optional[jsii.Number] = None,
    ipv6_cidr_block: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4d9ea6bf97e958984ea62993c8bbf2102ab9d4b50814b6ac96f69e6ef281693(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7d4e224ddcefdf1d325d1215b48f07db49adfbda79a1526732ddf1b7440ebb6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c43cc90f8b31fdf78c733e96e9b881d9789de8bceae6941b210560a659c812bf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cfd4e0257d10ca6f10cafa4dcba3ad1dda9ed153c86d41d103e37c2a91be711(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa809fec3d97ddcf4524cc9414a7935f1624d2a4b1767a6d1c3b751c3b34eec1(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88e70c3daec3f2cc7692d263f73a15f3b51f379796564c4644e08565d5592c4f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DefaultNetworkAclEgress]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7dd4c4809deca6e9e7d271feae8ac31fb3d3c68c417a9c19f5a441d60dd387a9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ad6b6ea93cad050c00ce3672fa543f250d84661bd334d0e872ee20d3f0ca0e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11cc7ea7f1547ba82960cfd2bcb6b7d79c2545f8c4e3cef616041184b2b8ce7e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73bd54de21816822f6c330bde946b8420ab1647a724492e2c4246f905ddf836a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1ec0b71fca39ef166f23d954bd2b57894cef1260c69f852e158f25bfb261c11(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4afd37e455c5604793d48b9498b2f7ab07fee6cd7672196b23c424a9bb3dc0d5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c586c7bc8814c16562d43ac1d830989f82964c7581d512281a0e265e84c0366(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b68b9a1b31efc2c9e52211cbf3b267ea8485bfe814ce47daa52d05fd695258b7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90eefe2c149cd1b9ac282a522d2642d29e8c53ecc1fde31146dda54c91261b43(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f85307adb584e7af65b48a4f9db2cf936361235be3d514172c6adc94fc464ff3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0332a04dac9f9f0633ac424e19e83866baa8c164e7be3a92479eeae0f0ac9b3e(
    value: typing.Optional[typing.Union[DefaultNetworkAclEgress, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__979ba7eb4323e55e482ea7d723babb51724c1f02aefee825d9eb5957b95e3a4c(
    *,
    action: builtins.str,
    from_port: jsii.Number,
    protocol: builtins.str,
    rule_no: jsii.Number,
    to_port: jsii.Number,
    cidr_block: typing.Optional[builtins.str] = None,
    icmp_code: typing.Optional[jsii.Number] = None,
    icmp_type: typing.Optional[jsii.Number] = None,
    ipv6_cidr_block: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d221babb5d4870051c4202e4dea65913589407561a9c3beeb6de8a9a0802505c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b445eb9073b0dc62dd4e4fd3c8aad9ba35d0d0d8195736db5edc6b16606a6c5(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c837509e35a1b8858933943cf627097a3142c0294e40c51467a0a2ae4aae589b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8282ec8a9fdc88446ae3ca2dff7c66a539697b0d3684aeeb7e2cfee6c749df9b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e0567d34c0afb04007bd76ea18ce36ffc6e69d2cd27cf99e2cb3f267eb11a67(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3938336a5e34b3e9f2fd577676ff96bdf8793be8e56e76f2a1fb8114ace77904(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DefaultNetworkAclIngress]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65acd4d22564d9a285b154474dfb1fb2c470b3bc2dd72a8a936393de78f80956(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e4d790315f5e29ed6f67743c9e806c26e5e896e83bb245142304b327e73f337(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2fe2ffeb963fa7ce172f81dcd993029efb53a342863e0efa987293bd663f165(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2642ece1d6fa666d283a26d8c89861308cc9eefeefb2f1a5c279243f8ec1d74e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__156595b117668394d7f391a0e61cb0bf1b6cbbf9057200892be171cbf1e7480d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__554f58b287c4ad99e99a1a778598764ea2c93aa40a86f09334b0e14c0fd1afff(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05b01a0c9e47b674d66696160b3425369855fe496c8a0996e64516298262109d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__173433035bc06d7c653d6d0c8e0c52545f5d4a8462141c0a70437ce2edb7d8e3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54cd5166d5f56559edb3916c3d22d9bc1ea574c687eb4c1b8c7b3353062d4ce6(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8aea658a8e421cc8649df9657aac541940c735869ad8eed7525767d4654b58f1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cbc35ad7d09935ffc2165690902528bb850de44b4760f902ad3182825ad7766(
    value: typing.Optional[typing.Union[DefaultNetworkAclIngress, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
