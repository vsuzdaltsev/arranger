'''
# `aws_rolesanywhere_trust_anchor`

Refer to the Terraform Registory for docs: [`aws_rolesanywhere_trust_anchor`](https://www.terraform.io/docs/providers/aws/r/rolesanywhere_trust_anchor).
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


class RolesanywhereTrustAnchor(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.rolesanywhereTrustAnchor.RolesanywhereTrustAnchor",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/rolesanywhere_trust_anchor aws_rolesanywhere_trust_anchor}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        source: typing.Union["RolesanywhereTrustAnchorSource", typing.Dict[builtins.str, typing.Any]],
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/rolesanywhere_trust_anchor aws_rolesanywhere_trust_anchor} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rolesanywhere_trust_anchor#name RolesanywhereTrustAnchor#name}.
        :param source: source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rolesanywhere_trust_anchor#source RolesanywhereTrustAnchor#source}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rolesanywhere_trust_anchor#enabled RolesanywhereTrustAnchor#enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rolesanywhere_trust_anchor#id RolesanywhereTrustAnchor#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rolesanywhere_trust_anchor#tags RolesanywhereTrustAnchor#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rolesanywhere_trust_anchor#tags_all RolesanywhereTrustAnchor#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34cc890feb0b549eaa4114fe034818d6d1159e064006407c441419e8f9ff118d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = RolesanywhereTrustAnchorConfig(
            name=name,
            source=source,
            enabled=enabled,
            id=id,
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

    @jsii.member(jsii_name="putSource")
    def put_source(
        self,
        *,
        source_data: typing.Union["RolesanywhereTrustAnchorSourceSourceData", typing.Dict[builtins.str, typing.Any]],
        source_type: builtins.str,
    ) -> None:
        '''
        :param source_data: source_data block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rolesanywhere_trust_anchor#source_data RolesanywhereTrustAnchor#source_data}
        :param source_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rolesanywhere_trust_anchor#source_type RolesanywhereTrustAnchor#source_type}.
        '''
        value = RolesanywhereTrustAnchorSource(
            source_data=source_data, source_type=source_type
        )

        return typing.cast(None, jsii.invoke(self, "putSource", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    @jsii.member(jsii_name="source")
    def source(self) -> "RolesanywhereTrustAnchorSourceOutputReference":
        return typing.cast("RolesanywhereTrustAnchorSourceOutputReference", jsii.get(self, "source"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional["RolesanywhereTrustAnchorSource"]:
        return typing.cast(typing.Optional["RolesanywhereTrustAnchorSource"], jsii.get(self, "sourceInput"))

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
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b19fb702239bcbac665a3efd3ddd42ec7083c78ac1753a39c13b4eb0e4e5525)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52584e5daaf75e05dce2fd53756ab9c88271c9bf7800de722d4fe89528479a00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ea72248cdf1276e3c711fd4ceb546baea2c1e17d303ba073b31d0353fe91edc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9215bb745de84ae7ff79021f18b9e1f088c6032b04d22acb93066de0ff36bf0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8e18e7ecd276ae46701b48804c9d3dffafd42bb8f306666eb4a3c820cf18c07)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.rolesanywhereTrustAnchor.RolesanywhereTrustAnchorConfig",
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
        "source": "source",
        "enabled": "enabled",
        "id": "id",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class RolesanywhereTrustAnchorConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        name: builtins.str,
        source: typing.Union["RolesanywhereTrustAnchorSource", typing.Dict[builtins.str, typing.Any]],
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
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
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rolesanywhere_trust_anchor#name RolesanywhereTrustAnchor#name}.
        :param source: source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rolesanywhere_trust_anchor#source RolesanywhereTrustAnchor#source}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rolesanywhere_trust_anchor#enabled RolesanywhereTrustAnchor#enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rolesanywhere_trust_anchor#id RolesanywhereTrustAnchor#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rolesanywhere_trust_anchor#tags RolesanywhereTrustAnchor#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rolesanywhere_trust_anchor#tags_all RolesanywhereTrustAnchor#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(source, dict):
            source = RolesanywhereTrustAnchorSource(**source)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1dde2c3405c49d1240ba7053563a2c1d6730a74eb0ecfddf05754acd7c27585e)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "source": source,
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
        if enabled is not None:
            self._values["enabled"] = enabled
        if id is not None:
            self._values["id"] = id
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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rolesanywhere_trust_anchor#name RolesanywhereTrustAnchor#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source(self) -> "RolesanywhereTrustAnchorSource":
        '''source block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rolesanywhere_trust_anchor#source RolesanywhereTrustAnchor#source}
        '''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast("RolesanywhereTrustAnchorSource", result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rolesanywhere_trust_anchor#enabled RolesanywhereTrustAnchor#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rolesanywhere_trust_anchor#id RolesanywhereTrustAnchor#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rolesanywhere_trust_anchor#tags RolesanywhereTrustAnchor#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rolesanywhere_trust_anchor#tags_all RolesanywhereTrustAnchor#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RolesanywhereTrustAnchorConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.rolesanywhereTrustAnchor.RolesanywhereTrustAnchorSource",
    jsii_struct_bases=[],
    name_mapping={"source_data": "sourceData", "source_type": "sourceType"},
)
class RolesanywhereTrustAnchorSource:
    def __init__(
        self,
        *,
        source_data: typing.Union["RolesanywhereTrustAnchorSourceSourceData", typing.Dict[builtins.str, typing.Any]],
        source_type: builtins.str,
    ) -> None:
        '''
        :param source_data: source_data block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rolesanywhere_trust_anchor#source_data RolesanywhereTrustAnchor#source_data}
        :param source_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rolesanywhere_trust_anchor#source_type RolesanywhereTrustAnchor#source_type}.
        '''
        if isinstance(source_data, dict):
            source_data = RolesanywhereTrustAnchorSourceSourceData(**source_data)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d81433f439d3dea79959246d639247a9ac4c263c80103c1b41d56859d196c764)
            check_type(argname="argument source_data", value=source_data, expected_type=type_hints["source_data"])
            check_type(argname="argument source_type", value=source_type, expected_type=type_hints["source_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "source_data": source_data,
            "source_type": source_type,
        }

    @builtins.property
    def source_data(self) -> "RolesanywhereTrustAnchorSourceSourceData":
        '''source_data block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rolesanywhere_trust_anchor#source_data RolesanywhereTrustAnchor#source_data}
        '''
        result = self._values.get("source_data")
        assert result is not None, "Required property 'source_data' is missing"
        return typing.cast("RolesanywhereTrustAnchorSourceSourceData", result)

    @builtins.property
    def source_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rolesanywhere_trust_anchor#source_type RolesanywhereTrustAnchor#source_type}.'''
        result = self._values.get("source_type")
        assert result is not None, "Required property 'source_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RolesanywhereTrustAnchorSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RolesanywhereTrustAnchorSourceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.rolesanywhereTrustAnchor.RolesanywhereTrustAnchorSourceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6f0510412d87c967c47b5a645cdca58caeaf57eb2a44f4e166a3c081dab9d21b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSourceData")
    def put_source_data(
        self,
        *,
        acm_pca_arn: typing.Optional[builtins.str] = None,
        x509_certificate_data: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param acm_pca_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rolesanywhere_trust_anchor#acm_pca_arn RolesanywhereTrustAnchor#acm_pca_arn}.
        :param x509_certificate_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rolesanywhere_trust_anchor#x509_certificate_data RolesanywhereTrustAnchor#x509_certificate_data}.
        '''
        value = RolesanywhereTrustAnchorSourceSourceData(
            acm_pca_arn=acm_pca_arn, x509_certificate_data=x509_certificate_data
        )

        return typing.cast(None, jsii.invoke(self, "putSourceData", [value]))

    @builtins.property
    @jsii.member(jsii_name="sourceData")
    def source_data(self) -> "RolesanywhereTrustAnchorSourceSourceDataOutputReference":
        return typing.cast("RolesanywhereTrustAnchorSourceSourceDataOutputReference", jsii.get(self, "sourceData"))

    @builtins.property
    @jsii.member(jsii_name="sourceDataInput")
    def source_data_input(
        self,
    ) -> typing.Optional["RolesanywhereTrustAnchorSourceSourceData"]:
        return typing.cast(typing.Optional["RolesanywhereTrustAnchorSourceSourceData"], jsii.get(self, "sourceDataInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceTypeInput")
    def source_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceType")
    def source_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceType"))

    @source_type.setter
    def source_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__389dbe9ae21ab7eaed90617dd16f1c446f60cd62f5ca655569205bf48bf4d8b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RolesanywhereTrustAnchorSource]:
        return typing.cast(typing.Optional[RolesanywhereTrustAnchorSource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[RolesanywhereTrustAnchorSource],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b148e8d162a6dd6d7e03e4725620708af896e293a29ead5316fc8dbe00c6e9a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.rolesanywhereTrustAnchor.RolesanywhereTrustAnchorSourceSourceData",
    jsii_struct_bases=[],
    name_mapping={
        "acm_pca_arn": "acmPcaArn",
        "x509_certificate_data": "x509CertificateData",
    },
)
class RolesanywhereTrustAnchorSourceSourceData:
    def __init__(
        self,
        *,
        acm_pca_arn: typing.Optional[builtins.str] = None,
        x509_certificate_data: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param acm_pca_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rolesanywhere_trust_anchor#acm_pca_arn RolesanywhereTrustAnchor#acm_pca_arn}.
        :param x509_certificate_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rolesanywhere_trust_anchor#x509_certificate_data RolesanywhereTrustAnchor#x509_certificate_data}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e7e94c1144811d836c05e5823fe02ad0ac35199440bd87755a939ebc3f7b6ed)
            check_type(argname="argument acm_pca_arn", value=acm_pca_arn, expected_type=type_hints["acm_pca_arn"])
            check_type(argname="argument x509_certificate_data", value=x509_certificate_data, expected_type=type_hints["x509_certificate_data"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if acm_pca_arn is not None:
            self._values["acm_pca_arn"] = acm_pca_arn
        if x509_certificate_data is not None:
            self._values["x509_certificate_data"] = x509_certificate_data

    @builtins.property
    def acm_pca_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rolesanywhere_trust_anchor#acm_pca_arn RolesanywhereTrustAnchor#acm_pca_arn}.'''
        result = self._values.get("acm_pca_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def x509_certificate_data(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/rolesanywhere_trust_anchor#x509_certificate_data RolesanywhereTrustAnchor#x509_certificate_data}.'''
        result = self._values.get("x509_certificate_data")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RolesanywhereTrustAnchorSourceSourceData(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RolesanywhereTrustAnchorSourceSourceDataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.rolesanywhereTrustAnchor.RolesanywhereTrustAnchorSourceSourceDataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__24a8e5d91c623ad9fd5fb3bb8440c0a49d8b85ba7d15c6266deefa8ae750dc4a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAcmPcaArn")
    def reset_acm_pca_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcmPcaArn", []))

    @jsii.member(jsii_name="resetX509CertificateData")
    def reset_x509_certificate_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetX509CertificateData", []))

    @builtins.property
    @jsii.member(jsii_name="acmPcaArnInput")
    def acm_pca_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "acmPcaArnInput"))

    @builtins.property
    @jsii.member(jsii_name="x509CertificateDataInput")
    def x509_certificate_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "x509CertificateDataInput"))

    @builtins.property
    @jsii.member(jsii_name="acmPcaArn")
    def acm_pca_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "acmPcaArn"))

    @acm_pca_arn.setter
    def acm_pca_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e3b0daa3011550fc88fc4bdde5858689af4bbc822272ef24a732464163003db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acmPcaArn", value)

    @builtins.property
    @jsii.member(jsii_name="x509CertificateData")
    def x509_certificate_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "x509CertificateData"))

    @x509_certificate_data.setter
    def x509_certificate_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__caf32a9062375fd35099c6b097e5747ddaa152e91619b0036f76de41149965cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "x509CertificateData", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[RolesanywhereTrustAnchorSourceSourceData]:
        return typing.cast(typing.Optional[RolesanywhereTrustAnchorSourceSourceData], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[RolesanywhereTrustAnchorSourceSourceData],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99fdf85e1bd966564af9a82ab5c45651f732f32e073b950a7e1b5890f8348e3d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "RolesanywhereTrustAnchor",
    "RolesanywhereTrustAnchorConfig",
    "RolesanywhereTrustAnchorSource",
    "RolesanywhereTrustAnchorSourceOutputReference",
    "RolesanywhereTrustAnchorSourceSourceData",
    "RolesanywhereTrustAnchorSourceSourceDataOutputReference",
]

publication.publish()

def _typecheckingstub__34cc890feb0b549eaa4114fe034818d6d1159e064006407c441419e8f9ff118d(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    source: typing.Union[RolesanywhereTrustAnchorSource, typing.Dict[builtins.str, typing.Any]],
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__2b19fb702239bcbac665a3efd3ddd42ec7083c78ac1753a39c13b4eb0e4e5525(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52584e5daaf75e05dce2fd53756ab9c88271c9bf7800de722d4fe89528479a00(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ea72248cdf1276e3c711fd4ceb546baea2c1e17d303ba073b31d0353fe91edc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9215bb745de84ae7ff79021f18b9e1f088c6032b04d22acb93066de0ff36bf0(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8e18e7ecd276ae46701b48804c9d3dffafd42bb8f306666eb4a3c820cf18c07(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1dde2c3405c49d1240ba7053563a2c1d6730a74eb0ecfddf05754acd7c27585e(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    source: typing.Union[RolesanywhereTrustAnchorSource, typing.Dict[builtins.str, typing.Any]],
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d81433f439d3dea79959246d639247a9ac4c263c80103c1b41d56859d196c764(
    *,
    source_data: typing.Union[RolesanywhereTrustAnchorSourceSourceData, typing.Dict[builtins.str, typing.Any]],
    source_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f0510412d87c967c47b5a645cdca58caeaf57eb2a44f4e166a3c081dab9d21b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__389dbe9ae21ab7eaed90617dd16f1c446f60cd62f5ca655569205bf48bf4d8b5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b148e8d162a6dd6d7e03e4725620708af896e293a29ead5316fc8dbe00c6e9a1(
    value: typing.Optional[RolesanywhereTrustAnchorSource],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e7e94c1144811d836c05e5823fe02ad0ac35199440bd87755a939ebc3f7b6ed(
    *,
    acm_pca_arn: typing.Optional[builtins.str] = None,
    x509_certificate_data: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24a8e5d91c623ad9fd5fb3bb8440c0a49d8b85ba7d15c6266deefa8ae750dc4a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e3b0daa3011550fc88fc4bdde5858689af4bbc822272ef24a732464163003db(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__caf32a9062375fd35099c6b097e5747ddaa152e91619b0036f76de41149965cb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99fdf85e1bd966564af9a82ab5c45651f732f32e073b950a7e1b5890f8348e3d(
    value: typing.Optional[RolesanywhereTrustAnchorSourceSourceData],
) -> None:
    """Type checking stubs"""
    pass
