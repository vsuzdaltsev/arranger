'''
# `aws_cloudfront_field_level_encryption_config`

Refer to the Terraform Registory for docs: [`aws_cloudfront_field_level_encryption_config`](https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config).
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


class CloudfrontFieldLevelEncryptionConfig(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontFieldLevelEncryptionConfig.CloudfrontFieldLevelEncryptionConfig",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config aws_cloudfront_field_level_encryption_config}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        content_type_profile_config: typing.Union["CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfig", typing.Dict[builtins.str, typing.Any]],
        query_arg_profile_config: typing.Union["CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfig", typing.Dict[builtins.str, typing.Any]],
        comment: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config aws_cloudfront_field_level_encryption_config} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param content_type_profile_config: content_type_profile_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#content_type_profile_config CloudfrontFieldLevelEncryptionConfig#content_type_profile_config}
        :param query_arg_profile_config: query_arg_profile_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#query_arg_profile_config CloudfrontFieldLevelEncryptionConfig#query_arg_profile_config}
        :param comment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#comment CloudfrontFieldLevelEncryptionConfig#comment}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#id CloudfrontFieldLevelEncryptionConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90a2ef236151cee827f42d65789f103e2c25675b0edf9b5477abc7857bb9af1e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CloudfrontFieldLevelEncryptionConfigConfig(
            content_type_profile_config=content_type_profile_config,
            query_arg_profile_config=query_arg_profile_config,
            comment=comment,
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

    @jsii.member(jsii_name="putContentTypeProfileConfig")
    def put_content_type_profile_config(
        self,
        *,
        content_type_profiles: typing.Union["CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles", typing.Dict[builtins.str, typing.Any]],
        forward_when_content_type_is_unknown: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param content_type_profiles: content_type_profiles block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#content_type_profiles CloudfrontFieldLevelEncryptionConfig#content_type_profiles}
        :param forward_when_content_type_is_unknown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#forward_when_content_type_is_unknown CloudfrontFieldLevelEncryptionConfig#forward_when_content_type_is_unknown}.
        '''
        value = CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfig(
            content_type_profiles=content_type_profiles,
            forward_when_content_type_is_unknown=forward_when_content_type_is_unknown,
        )

        return typing.cast(None, jsii.invoke(self, "putContentTypeProfileConfig", [value]))

    @jsii.member(jsii_name="putQueryArgProfileConfig")
    def put_query_arg_profile_config(
        self,
        *,
        forward_when_query_arg_profile_is_unknown: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        query_arg_profiles: typing.Optional[typing.Union["CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param forward_when_query_arg_profile_is_unknown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#forward_when_query_arg_profile_is_unknown CloudfrontFieldLevelEncryptionConfig#forward_when_query_arg_profile_is_unknown}.
        :param query_arg_profiles: query_arg_profiles block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#query_arg_profiles CloudfrontFieldLevelEncryptionConfig#query_arg_profiles}
        '''
        value = CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfig(
            forward_when_query_arg_profile_is_unknown=forward_when_query_arg_profile_is_unknown,
            query_arg_profiles=query_arg_profiles,
        )

        return typing.cast(None, jsii.invoke(self, "putQueryArgProfileConfig", [value]))

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

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
    @jsii.member(jsii_name="callerReference")
    def caller_reference(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "callerReference"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeProfileConfig")
    def content_type_profile_config(
        self,
    ) -> "CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigOutputReference":
        return typing.cast("CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigOutputReference", jsii.get(self, "contentTypeProfileConfig"))

    @builtins.property
    @jsii.member(jsii_name="etag")
    def etag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "etag"))

    @builtins.property
    @jsii.member(jsii_name="queryArgProfileConfig")
    def query_arg_profile_config(
        self,
    ) -> "CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigOutputReference":
        return typing.cast("CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigOutputReference", jsii.get(self, "queryArgProfileConfig"))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentInput"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeProfileConfigInput")
    def content_type_profile_config_input(
        self,
    ) -> typing.Optional["CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfig"]:
        return typing.cast(typing.Optional["CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfig"], jsii.get(self, "contentTypeProfileConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="queryArgProfileConfigInput")
    def query_arg_profile_config_input(
        self,
    ) -> typing.Optional["CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfig"]:
        return typing.cast(typing.Optional["CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfig"], jsii.get(self, "queryArgProfileConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71c67ce4b7aee406a23fa9342c793b6025ccb706b4cfed2f26d0e4047508f8f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f41d915435d6b917b01596e9ccaf19b9f2152cbabde03d1c815122510197f786)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="aws.cloudfrontFieldLevelEncryptionConfig.CloudfrontFieldLevelEncryptionConfigConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "content_type_profile_config": "contentTypeProfileConfig",
        "query_arg_profile_config": "queryArgProfileConfig",
        "comment": "comment",
        "id": "id",
    },
)
class CloudfrontFieldLevelEncryptionConfigConfig(
    _cdktf_9a9027ec.TerraformMetaArguments,
):
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
        content_type_profile_config: typing.Union["CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfig", typing.Dict[builtins.str, typing.Any]],
        query_arg_profile_config: typing.Union["CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfig", typing.Dict[builtins.str, typing.Any]],
        comment: typing.Optional[builtins.str] = None,
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
        :param content_type_profile_config: content_type_profile_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#content_type_profile_config CloudfrontFieldLevelEncryptionConfig#content_type_profile_config}
        :param query_arg_profile_config: query_arg_profile_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#query_arg_profile_config CloudfrontFieldLevelEncryptionConfig#query_arg_profile_config}
        :param comment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#comment CloudfrontFieldLevelEncryptionConfig#comment}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#id CloudfrontFieldLevelEncryptionConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(content_type_profile_config, dict):
            content_type_profile_config = CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfig(**content_type_profile_config)
        if isinstance(query_arg_profile_config, dict):
            query_arg_profile_config = CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfig(**query_arg_profile_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00c695111071301ddaa0265f3ea81b4a8d2793d4e6a7b8dcd4016a290e056a2c)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument content_type_profile_config", value=content_type_profile_config, expected_type=type_hints["content_type_profile_config"])
            check_type(argname="argument query_arg_profile_config", value=query_arg_profile_config, expected_type=type_hints["query_arg_profile_config"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "content_type_profile_config": content_type_profile_config,
            "query_arg_profile_config": query_arg_profile_config,
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
        if comment is not None:
            self._values["comment"] = comment
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
    def content_type_profile_config(
        self,
    ) -> "CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfig":
        '''content_type_profile_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#content_type_profile_config CloudfrontFieldLevelEncryptionConfig#content_type_profile_config}
        '''
        result = self._values.get("content_type_profile_config")
        assert result is not None, "Required property 'content_type_profile_config' is missing"
        return typing.cast("CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfig", result)

    @builtins.property
    def query_arg_profile_config(
        self,
    ) -> "CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfig":
        '''query_arg_profile_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#query_arg_profile_config CloudfrontFieldLevelEncryptionConfig#query_arg_profile_config}
        '''
        result = self._values.get("query_arg_profile_config")
        assert result is not None, "Required property 'query_arg_profile_config' is missing"
        return typing.cast("CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfig", result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#comment CloudfrontFieldLevelEncryptionConfig#comment}.'''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#id CloudfrontFieldLevelEncryptionConfig#id}.

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
        return "CloudfrontFieldLevelEncryptionConfigConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.cloudfrontFieldLevelEncryptionConfig.CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfig",
    jsii_struct_bases=[],
    name_mapping={
        "content_type_profiles": "contentTypeProfiles",
        "forward_when_content_type_is_unknown": "forwardWhenContentTypeIsUnknown",
    },
)
class CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfig:
    def __init__(
        self,
        *,
        content_type_profiles: typing.Union["CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles", typing.Dict[builtins.str, typing.Any]],
        forward_when_content_type_is_unknown: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param content_type_profiles: content_type_profiles block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#content_type_profiles CloudfrontFieldLevelEncryptionConfig#content_type_profiles}
        :param forward_when_content_type_is_unknown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#forward_when_content_type_is_unknown CloudfrontFieldLevelEncryptionConfig#forward_when_content_type_is_unknown}.
        '''
        if isinstance(content_type_profiles, dict):
            content_type_profiles = CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles(**content_type_profiles)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3625f278d9f09e7b57e531cda3c35ccd49449772161fa7183aef073cd0267461)
            check_type(argname="argument content_type_profiles", value=content_type_profiles, expected_type=type_hints["content_type_profiles"])
            check_type(argname="argument forward_when_content_type_is_unknown", value=forward_when_content_type_is_unknown, expected_type=type_hints["forward_when_content_type_is_unknown"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "content_type_profiles": content_type_profiles,
            "forward_when_content_type_is_unknown": forward_when_content_type_is_unknown,
        }

    @builtins.property
    def content_type_profiles(
        self,
    ) -> "CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles":
        '''content_type_profiles block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#content_type_profiles CloudfrontFieldLevelEncryptionConfig#content_type_profiles}
        '''
        result = self._values.get("content_type_profiles")
        assert result is not None, "Required property 'content_type_profiles' is missing"
        return typing.cast("CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles", result)

    @builtins.property
    def forward_when_content_type_is_unknown(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#forward_when_content_type_is_unknown CloudfrontFieldLevelEncryptionConfig#forward_when_content_type_is_unknown}.'''
        result = self._values.get("forward_when_content_type_is_unknown")
        assert result is not None, "Required property 'forward_when_content_type_is_unknown' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.cloudfrontFieldLevelEncryptionConfig.CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles",
    jsii_struct_bases=[],
    name_mapping={"items": "items"},
)
class CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles:
    def __init__(
        self,
        *,
        items: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param items: items block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#items CloudfrontFieldLevelEncryptionConfig#items}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53e94e88f6f56fe827fcafe7a79d8abaf6cd6c2799c09eaa114e16865dd19c2c)
            check_type(argname="argument items", value=items, expected_type=type_hints["items"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "items": items,
        }

    @builtins.property
    def items(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems"]]:
        '''items block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#items CloudfrontFieldLevelEncryptionConfig#items}
        '''
        result = self._values.get("items")
        assert result is not None, "Required property 'items' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.cloudfrontFieldLevelEncryptionConfig.CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems",
    jsii_struct_bases=[],
    name_mapping={
        "content_type": "contentType",
        "format": "format",
        "profile_id": "profileId",
    },
)
class CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems:
    def __init__(
        self,
        *,
        content_type: builtins.str,
        format: builtins.str,
        profile_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#content_type CloudfrontFieldLevelEncryptionConfig#content_type}.
        :param format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#format CloudfrontFieldLevelEncryptionConfig#format}.
        :param profile_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#profile_id CloudfrontFieldLevelEncryptionConfig#profile_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f953bf49559715e332ac345046d293071c0ff05d41d5ed471ebc715eaace43f)
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument format", value=format, expected_type=type_hints["format"])
            check_type(argname="argument profile_id", value=profile_id, expected_type=type_hints["profile_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "content_type": content_type,
            "format": format,
        }
        if profile_id is not None:
            self._values["profile_id"] = profile_id

    @builtins.property
    def content_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#content_type CloudfrontFieldLevelEncryptionConfig#content_type}.'''
        result = self._values.get("content_type")
        assert result is not None, "Required property 'content_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def format(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#format CloudfrontFieldLevelEncryptionConfig#format}.'''
        result = self._values.get("format")
        assert result is not None, "Required property 'format' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def profile_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#profile_id CloudfrontFieldLevelEncryptionConfig#profile_id}.'''
        result = self._values.get("profile_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontFieldLevelEncryptionConfig.CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4321b653c14857462022af90d68bffc5099710a1a842cb5fb3240333aeae9a08)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7bd5b0693ccf1b175800398210249014e66c7aa9649f5aab376a5a6768ca3f2e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41461e2cc32da74e46d7b2445792449d8994a5771ca2680dea9d1de941635e0f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4151fff17b0bca1e6a05daa5aa6b47b5d79e77cea459e9bc14b835601f0390c0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ec8d7542aded49be98ba33c96e2b0fe10de1df1814127e39f2d1b57e88de2567)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d13c0083eb0bea465a5b60bd1c3d2a7d18c87b52a6a8e51af63099aae23baae2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontFieldLevelEncryptionConfig.CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fb814fe7d7722e09695a94ecdaf41e4b653a06905e8cc561c717bce8ce28877a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetProfileId")
    def reset_profile_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProfileId", []))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="formatInput")
    def format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "formatInput"))

    @builtins.property
    @jsii.member(jsii_name="profileIdInput")
    def profile_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "profileIdInput"))

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1409bac6bf58a7815c66e333efe58ff2814e20635a27c0ce98ff13792eff4a57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="format")
    def format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "format"))

    @format.setter
    def format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21b6efe7c9921c15c90ed4b72aa75f71e3d641bf2eabc0438932cabf5d01aa39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "format", value)

    @builtins.property
    @jsii.member(jsii_name="profileId")
    def profile_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "profileId"))

    @profile_id.setter
    def profile_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fefd67458215789991a3d1f425638425085bf4fce68a7afad24fd0cf571bc6ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "profileId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea84701d06eb37271b8b572bd442a24d0e9f73bd9275768a95452b6fc119e97f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontFieldLevelEncryptionConfig.CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1101a7f6758723e366ab7072ec142b928db60688c196cc7b02a3b852d31ad0e2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putItems")
    def put_items(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85c2e5573fa8a26e10e65f74c0d97db0f0ccf5929d837f0b524c781179cc7a3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putItems", [value]))

    @builtins.property
    @jsii.member(jsii_name="items")
    def items(
        self,
    ) -> CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsList:
        return typing.cast(CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsList, jsii.get(self, "items"))

    @builtins.property
    @jsii.member(jsii_name="itemsInput")
    def items_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems]]], jsii.get(self, "itemsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles]:
        return typing.cast(typing.Optional[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__264c6238f0a10b109d88a14ef5fc8e2bed82a7a410d127b377691ba36ab4c0d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontFieldLevelEncryptionConfig.CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fe3dbf4d9e33fc71b1094845396a09801c61a7a848bb2dea9abe094080bbd01d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putContentTypeProfiles")
    def put_content_type_profiles(
        self,
        *,
        items: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param items: items block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#items CloudfrontFieldLevelEncryptionConfig#items}
        '''
        value = CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles(
            items=items
        )

        return typing.cast(None, jsii.invoke(self, "putContentTypeProfiles", [value]))

    @builtins.property
    @jsii.member(jsii_name="contentTypeProfiles")
    def content_type_profiles(
        self,
    ) -> CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesOutputReference:
        return typing.cast(CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesOutputReference, jsii.get(self, "contentTypeProfiles"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeProfilesInput")
    def content_type_profiles_input(
        self,
    ) -> typing.Optional[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles]:
        return typing.cast(typing.Optional[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles], jsii.get(self, "contentTypeProfilesInput"))

    @builtins.property
    @jsii.member(jsii_name="forwardWhenContentTypeIsUnknownInput")
    def forward_when_content_type_is_unknown_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "forwardWhenContentTypeIsUnknownInput"))

    @builtins.property
    @jsii.member(jsii_name="forwardWhenContentTypeIsUnknown")
    def forward_when_content_type_is_unknown(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "forwardWhenContentTypeIsUnknown"))

    @forward_when_content_type_is_unknown.setter
    def forward_when_content_type_is_unknown(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee474e1a8039fcd64ffae1f0594f3d11a110fd50069ff0003bb9f03129cf74d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forwardWhenContentTypeIsUnknown", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfig]:
        return typing.cast(typing.Optional[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51798442b1728d46ed2aaf88b2c678ace01bef36b1cc843f4cf5101f9334fcc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudfrontFieldLevelEncryptionConfig.CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfig",
    jsii_struct_bases=[],
    name_mapping={
        "forward_when_query_arg_profile_is_unknown": "forwardWhenQueryArgProfileIsUnknown",
        "query_arg_profiles": "queryArgProfiles",
    },
)
class CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfig:
    def __init__(
        self,
        *,
        forward_when_query_arg_profile_is_unknown: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        query_arg_profiles: typing.Optional[typing.Union["CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param forward_when_query_arg_profile_is_unknown: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#forward_when_query_arg_profile_is_unknown CloudfrontFieldLevelEncryptionConfig#forward_when_query_arg_profile_is_unknown}.
        :param query_arg_profiles: query_arg_profiles block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#query_arg_profiles CloudfrontFieldLevelEncryptionConfig#query_arg_profiles}
        '''
        if isinstance(query_arg_profiles, dict):
            query_arg_profiles = CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles(**query_arg_profiles)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04efba17d011f4adbf0c64cee38b5595dae7c34b27339f3bd44947fb4929cfe7)
            check_type(argname="argument forward_when_query_arg_profile_is_unknown", value=forward_when_query_arg_profile_is_unknown, expected_type=type_hints["forward_when_query_arg_profile_is_unknown"])
            check_type(argname="argument query_arg_profiles", value=query_arg_profiles, expected_type=type_hints["query_arg_profiles"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "forward_when_query_arg_profile_is_unknown": forward_when_query_arg_profile_is_unknown,
        }
        if query_arg_profiles is not None:
            self._values["query_arg_profiles"] = query_arg_profiles

    @builtins.property
    def forward_when_query_arg_profile_is_unknown(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#forward_when_query_arg_profile_is_unknown CloudfrontFieldLevelEncryptionConfig#forward_when_query_arg_profile_is_unknown}.'''
        result = self._values.get("forward_when_query_arg_profile_is_unknown")
        assert result is not None, "Required property 'forward_when_query_arg_profile_is_unknown' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def query_arg_profiles(
        self,
    ) -> typing.Optional["CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles"]:
        '''query_arg_profiles block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#query_arg_profiles CloudfrontFieldLevelEncryptionConfig#query_arg_profiles}
        '''
        result = self._values.get("query_arg_profiles")
        return typing.cast(typing.Optional["CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontFieldLevelEncryptionConfig.CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__08c6fda6d97e5402f98cdbc4ee2733f72d11eedac7c67b4472d7a64a506f3e15)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putQueryArgProfiles")
    def put_query_arg_profiles(
        self,
        *,
        items: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param items: items block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#items CloudfrontFieldLevelEncryptionConfig#items}
        '''
        value = CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles(
            items=items
        )

        return typing.cast(None, jsii.invoke(self, "putQueryArgProfiles", [value]))

    @jsii.member(jsii_name="resetQueryArgProfiles")
    def reset_query_arg_profiles(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryArgProfiles", []))

    @builtins.property
    @jsii.member(jsii_name="queryArgProfiles")
    def query_arg_profiles(
        self,
    ) -> "CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesOutputReference":
        return typing.cast("CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesOutputReference", jsii.get(self, "queryArgProfiles"))

    @builtins.property
    @jsii.member(jsii_name="forwardWhenQueryArgProfileIsUnknownInput")
    def forward_when_query_arg_profile_is_unknown_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "forwardWhenQueryArgProfileIsUnknownInput"))

    @builtins.property
    @jsii.member(jsii_name="queryArgProfilesInput")
    def query_arg_profiles_input(
        self,
    ) -> typing.Optional["CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles"]:
        return typing.cast(typing.Optional["CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles"], jsii.get(self, "queryArgProfilesInput"))

    @builtins.property
    @jsii.member(jsii_name="forwardWhenQueryArgProfileIsUnknown")
    def forward_when_query_arg_profile_is_unknown(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "forwardWhenQueryArgProfileIsUnknown"))

    @forward_when_query_arg_profile_is_unknown.setter
    def forward_when_query_arg_profile_is_unknown(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6264a64e118749640e176f28e2748ae1cdbb2732bf15bd6721e81e49cdec93e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forwardWhenQueryArgProfileIsUnknown", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfig]:
        return typing.cast(typing.Optional[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57dbf43d0ebd3f5401fb0b48d7c019cd13e561671e345f93894591819c0e722b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudfrontFieldLevelEncryptionConfig.CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles",
    jsii_struct_bases=[],
    name_mapping={"items": "items"},
)
class CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles:
    def __init__(
        self,
        *,
        items: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param items: items block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#items CloudfrontFieldLevelEncryptionConfig#items}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e6e2c84492a09cbceadc0f7e60f7e1ba7c5013240c08b2dda259a0b60c0e455)
            check_type(argname="argument items", value=items, expected_type=type_hints["items"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if items is not None:
            self._values["items"] = items

    @builtins.property
    def items(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems"]]]:
        '''items block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#items CloudfrontFieldLevelEncryptionConfig#items}
        '''
        result = self._values.get("items")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.cloudfrontFieldLevelEncryptionConfig.CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems",
    jsii_struct_bases=[],
    name_mapping={"profile_id": "profileId", "query_arg": "queryArg"},
)
class CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems:
    def __init__(self, *, profile_id: builtins.str, query_arg: builtins.str) -> None:
        '''
        :param profile_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#profile_id CloudfrontFieldLevelEncryptionConfig#profile_id}.
        :param query_arg: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#query_arg CloudfrontFieldLevelEncryptionConfig#query_arg}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c37f86f7f9eeb910666186f012dea7ad6b8e5301a697226718d26d95ad51b34)
            check_type(argname="argument profile_id", value=profile_id, expected_type=type_hints["profile_id"])
            check_type(argname="argument query_arg", value=query_arg, expected_type=type_hints["query_arg"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "profile_id": profile_id,
            "query_arg": query_arg,
        }

    @builtins.property
    def profile_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#profile_id CloudfrontFieldLevelEncryptionConfig#profile_id}.'''
        result = self._values.get("profile_id")
        assert result is not None, "Required property 'profile_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def query_arg(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_field_level_encryption_config#query_arg CloudfrontFieldLevelEncryptionConfig#query_arg}.'''
        result = self._values.get("query_arg")
        assert result is not None, "Required property 'query_arg' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontFieldLevelEncryptionConfig.CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__74b196fc63a50758e9b0069b3604589ff16f3f075574a7471b727b793625ffb7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e54765c52e1e7caa0603b424a6bb116f4341126409c45d662235cdb63cc101b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__179b5d61b23561ac93f8d743aa422e555308df72fa5c049081ed5e9d1861d95b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__935bc144600f24da15e111da96db85c6571cae7255d7e0684c4fa92f6f0ac361)
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
            type_hints = typing.get_type_hints(_typecheckingstub__05a9bdd865506ef2fa246094db1a2d3272f3df23d0cd0646e8a2a2aafa20936c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7033e739b9b2b849e98c86c54bbf1a3780195aa4bbce4f70fb47778f9f9b70bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontFieldLevelEncryptionConfig.CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__87084c207b2897bb8b433ea6a3771fe5407a6334ee4069b5aee24671d4d172aa)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="profileIdInput")
    def profile_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "profileIdInput"))

    @builtins.property
    @jsii.member(jsii_name="queryArgInput")
    def query_arg_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryArgInput"))

    @builtins.property
    @jsii.member(jsii_name="profileId")
    def profile_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "profileId"))

    @profile_id.setter
    def profile_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8a47777630ca44f4cee083fa7b63d61991cbe2d17252ed72563e595ce701fc3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "profileId", value)

    @builtins.property
    @jsii.member(jsii_name="queryArg")
    def query_arg(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "queryArg"))

    @query_arg.setter
    def query_arg(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c7a549fcb42029184ba542661f2b41f2724b94d281abf19e2a6b987b6b31e5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryArg", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84d75a8b92fd982529741d2821205a86e310dfc12d6e3de2eb5e3b86265e22f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontFieldLevelEncryptionConfig.CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2469ae8873a88842669b7f73352b09664a1cfec60cbfd217089d8ce67bfd81e4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putItems")
    def put_items(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f1fdce9cac70e0c93f59f59d6d2b2e0572ce8059fb0f181c4f985362625700c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putItems", [value]))

    @jsii.member(jsii_name="resetItems")
    def reset_items(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetItems", []))

    @builtins.property
    @jsii.member(jsii_name="items")
    def items(
        self,
    ) -> CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsList:
        return typing.cast(CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsList, jsii.get(self, "items"))

    @builtins.property
    @jsii.member(jsii_name="itemsInput")
    def items_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems]]], jsii.get(self, "itemsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles]:
        return typing.cast(typing.Optional[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af9ed3c6af8b5e37b09bc0a070d38389e511dd84e2b852b3bf0a0453136addce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CloudfrontFieldLevelEncryptionConfig",
    "CloudfrontFieldLevelEncryptionConfigConfig",
    "CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfig",
    "CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles",
    "CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems",
    "CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsList",
    "CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItemsOutputReference",
    "CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesOutputReference",
    "CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigOutputReference",
    "CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfig",
    "CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigOutputReference",
    "CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles",
    "CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems",
    "CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsList",
    "CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItemsOutputReference",
    "CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesOutputReference",
]

publication.publish()

def _typecheckingstub__90a2ef236151cee827f42d65789f103e2c25675b0edf9b5477abc7857bb9af1e(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    content_type_profile_config: typing.Union[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfig, typing.Dict[builtins.str, typing.Any]],
    query_arg_profile_config: typing.Union[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfig, typing.Dict[builtins.str, typing.Any]],
    comment: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__71c67ce4b7aee406a23fa9342c793b6025ccb706b4cfed2f26d0e4047508f8f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f41d915435d6b917b01596e9ccaf19b9f2152cbabde03d1c815122510197f786(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00c695111071301ddaa0265f3ea81b4a8d2793d4e6a7b8dcd4016a290e056a2c(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    content_type_profile_config: typing.Union[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfig, typing.Dict[builtins.str, typing.Any]],
    query_arg_profile_config: typing.Union[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfig, typing.Dict[builtins.str, typing.Any]],
    comment: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3625f278d9f09e7b57e531cda3c35ccd49449772161fa7183aef073cd0267461(
    *,
    content_type_profiles: typing.Union[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles, typing.Dict[builtins.str, typing.Any]],
    forward_when_content_type_is_unknown: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53e94e88f6f56fe827fcafe7a79d8abaf6cd6c2799c09eaa114e16865dd19c2c(
    *,
    items: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f953bf49559715e332ac345046d293071c0ff05d41d5ed471ebc715eaace43f(
    *,
    content_type: builtins.str,
    format: builtins.str,
    profile_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4321b653c14857462022af90d68bffc5099710a1a842cb5fb3240333aeae9a08(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bd5b0693ccf1b175800398210249014e66c7aa9649f5aab376a5a6768ca3f2e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41461e2cc32da74e46d7b2445792449d8994a5771ca2680dea9d1de941635e0f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4151fff17b0bca1e6a05daa5aa6b47b5d79e77cea459e9bc14b835601f0390c0(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec8d7542aded49be98ba33c96e2b0fe10de1df1814127e39f2d1b57e88de2567(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d13c0083eb0bea465a5b60bd1c3d2a7d18c87b52a6a8e51af63099aae23baae2(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb814fe7d7722e09695a94ecdaf41e4b653a06905e8cc561c717bce8ce28877a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1409bac6bf58a7815c66e333efe58ff2814e20635a27c0ce98ff13792eff4a57(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21b6efe7c9921c15c90ed4b72aa75f71e3d641bf2eabc0438932cabf5d01aa39(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fefd67458215789991a3d1f425638425085bf4fce68a7afad24fd0cf571bc6ca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea84701d06eb37271b8b572bd442a24d0e9f73bd9275768a95452b6fc119e97f(
    value: typing.Optional[typing.Union[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1101a7f6758723e366ab7072ec142b928db60688c196cc7b02a3b852d31ad0e2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85c2e5573fa8a26e10e65f74c0d97db0f0ccf5929d837f0b524c781179cc7a3b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfilesItems, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__264c6238f0a10b109d88a14ef5fc8e2bed82a7a410d127b377691ba36ab4c0d7(
    value: typing.Optional[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfigContentTypeProfiles],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe3dbf4d9e33fc71b1094845396a09801c61a7a848bb2dea9abe094080bbd01d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee474e1a8039fcd64ffae1f0594f3d11a110fd50069ff0003bb9f03129cf74d0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51798442b1728d46ed2aaf88b2c678ace01bef36b1cc843f4cf5101f9334fcc0(
    value: typing.Optional[CloudfrontFieldLevelEncryptionConfigContentTypeProfileConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04efba17d011f4adbf0c64cee38b5595dae7c34b27339f3bd44947fb4929cfe7(
    *,
    forward_when_query_arg_profile_is_unknown: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    query_arg_profiles: typing.Optional[typing.Union[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08c6fda6d97e5402f98cdbc4ee2733f72d11eedac7c67b4472d7a64a506f3e15(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6264a64e118749640e176f28e2748ae1cdbb2732bf15bd6721e81e49cdec93e1(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57dbf43d0ebd3f5401fb0b48d7c019cd13e561671e345f93894591819c0e722b(
    value: typing.Optional[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e6e2c84492a09cbceadc0f7e60f7e1ba7c5013240c08b2dda259a0b60c0e455(
    *,
    items: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c37f86f7f9eeb910666186f012dea7ad6b8e5301a697226718d26d95ad51b34(
    *,
    profile_id: builtins.str,
    query_arg: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74b196fc63a50758e9b0069b3604589ff16f3f075574a7471b727b793625ffb7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e54765c52e1e7caa0603b424a6bb116f4341126409c45d662235cdb63cc101b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__179b5d61b23561ac93f8d743aa422e555308df72fa5c049081ed5e9d1861d95b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__935bc144600f24da15e111da96db85c6571cae7255d7e0684c4fa92f6f0ac361(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05a9bdd865506ef2fa246094db1a2d3272f3df23d0cd0646e8a2a2aafa20936c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7033e739b9b2b849e98c86c54bbf1a3780195aa4bbce4f70fb47778f9f9b70bb(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87084c207b2897bb8b433ea6a3771fe5407a6334ee4069b5aee24671d4d172aa(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8a47777630ca44f4cee083fa7b63d61991cbe2d17252ed72563e595ce701fc3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c7a549fcb42029184ba542661f2b41f2724b94d281abf19e2a6b987b6b31e5d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84d75a8b92fd982529741d2821205a86e310dfc12d6e3de2eb5e3b86265e22f2(
    value: typing.Optional[typing.Union[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2469ae8873a88842669b7f73352b09664a1cfec60cbfd217089d8ce67bfd81e4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f1fdce9cac70e0c93f59f59d6d2b2e0572ce8059fb0f181c4f985362625700c(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfilesItems, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af9ed3c6af8b5e37b09bc0a070d38389e511dd84e2b852b3bf0a0453136addce(
    value: typing.Optional[CloudfrontFieldLevelEncryptionConfigQueryArgProfileConfigQueryArgProfiles],
) -> None:
    """Type checking stubs"""
    pass
