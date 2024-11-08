'''
# `aws_datasync_location_s3`

Refer to the Terraform Registory for docs: [`aws_datasync_location_s3`](https://www.terraform.io/docs/providers/aws/r/datasync_location_s3).
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


class DatasyncLocationS3(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.datasyncLocationS3.DatasyncLocationS3",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_s3 aws_datasync_location_s3}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        s3_bucket_arn: builtins.str,
        s3_config: typing.Union["DatasyncLocationS3S3Config", typing.Dict[builtins.str, typing.Any]],
        subdirectory: builtins.str,
        agent_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        s3_storage_class: typing.Optional[builtins.str] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_s3 aws_datasync_location_s3} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param s3_bucket_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_s3#s3_bucket_arn DatasyncLocationS3#s3_bucket_arn}.
        :param s3_config: s3_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_s3#s3_config DatasyncLocationS3#s3_config}
        :param subdirectory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_s3#subdirectory DatasyncLocationS3#subdirectory}.
        :param agent_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_s3#agent_arns DatasyncLocationS3#agent_arns}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_s3#id DatasyncLocationS3#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param s3_storage_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_s3#s3_storage_class DatasyncLocationS3#s3_storage_class}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_s3#tags DatasyncLocationS3#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_s3#tags_all DatasyncLocationS3#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd637910dac96522c410d505412c923406bec6c685850cc15beca85eb03c8bc0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DatasyncLocationS3Config(
            s3_bucket_arn=s3_bucket_arn,
            s3_config=s3_config,
            subdirectory=subdirectory,
            agent_arns=agent_arns,
            id=id,
            s3_storage_class=s3_storage_class,
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

    @jsii.member(jsii_name="putS3Config")
    def put_s3_config(self, *, bucket_access_role_arn: builtins.str) -> None:
        '''
        :param bucket_access_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_s3#bucket_access_role_arn DatasyncLocationS3#bucket_access_role_arn}.
        '''
        value = DatasyncLocationS3S3Config(
            bucket_access_role_arn=bucket_access_role_arn
        )

        return typing.cast(None, jsii.invoke(self, "putS3Config", [value]))

    @jsii.member(jsii_name="resetAgentArns")
    def reset_agent_arns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAgentArns", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetS3StorageClass")
    def reset_s3_storage_class(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3StorageClass", []))

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
    @jsii.member(jsii_name="s3Config")
    def s3_config(self) -> "DatasyncLocationS3S3ConfigOutputReference":
        return typing.cast("DatasyncLocationS3S3ConfigOutputReference", jsii.get(self, "s3Config"))

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @builtins.property
    @jsii.member(jsii_name="agentArnsInput")
    def agent_arns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "agentArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="s3BucketArnInput")
    def s3_bucket_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3BucketArnInput"))

    @builtins.property
    @jsii.member(jsii_name="s3ConfigInput")
    def s3_config_input(self) -> typing.Optional["DatasyncLocationS3S3Config"]:
        return typing.cast(typing.Optional["DatasyncLocationS3S3Config"], jsii.get(self, "s3ConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="s3StorageClassInput")
    def s3_storage_class_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3StorageClassInput"))

    @builtins.property
    @jsii.member(jsii_name="subdirectoryInput")
    def subdirectory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subdirectoryInput"))

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
    @jsii.member(jsii_name="agentArns")
    def agent_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "agentArns"))

    @agent_arns.setter
    def agent_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fdc69ec2e0fe6f003a2b05b844b782822b2dce44744155f5d0bfd8ee6160b60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "agentArns", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f49b868446c8b5a800eb44fec0b109f535980cfc3e55c38d54ccef72c5f95f2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="s3BucketArn")
    def s3_bucket_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3BucketArn"))

    @s3_bucket_arn.setter
    def s3_bucket_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b82b44f8cbeb337b005845c8243a51411c58d4725040d9176845e32b46904182)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3BucketArn", value)

    @builtins.property
    @jsii.member(jsii_name="s3StorageClass")
    def s3_storage_class(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3StorageClass"))

    @s3_storage_class.setter
    def s3_storage_class(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acf617e378301cdff63c6dbdd104a3ad6a2f5661bfa8a26da6ea22f4f47084bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3StorageClass", value)

    @builtins.property
    @jsii.member(jsii_name="subdirectory")
    def subdirectory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subdirectory"))

    @subdirectory.setter
    def subdirectory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6929aaa3e3ac4e1aee1b1a723446fe537d1d60af968e5b74b1cef0fc59b94b2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subdirectory", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__884bacea29a72ba33770c4873b61afda2deb09eb7cd0721b9661ddc6c57cfa27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91397981cdf26a7bb7e2097ca12825a32c50458ada3e37b7a3f80fb5d75a0a31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.datasyncLocationS3.DatasyncLocationS3Config",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "s3_bucket_arn": "s3BucketArn",
        "s3_config": "s3Config",
        "subdirectory": "subdirectory",
        "agent_arns": "agentArns",
        "id": "id",
        "s3_storage_class": "s3StorageClass",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class DatasyncLocationS3Config(_cdktf_9a9027ec.TerraformMetaArguments):
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
        s3_bucket_arn: builtins.str,
        s3_config: typing.Union["DatasyncLocationS3S3Config", typing.Dict[builtins.str, typing.Any]],
        subdirectory: builtins.str,
        agent_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        s3_storage_class: typing.Optional[builtins.str] = None,
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
        :param s3_bucket_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_s3#s3_bucket_arn DatasyncLocationS3#s3_bucket_arn}.
        :param s3_config: s3_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_s3#s3_config DatasyncLocationS3#s3_config}
        :param subdirectory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_s3#subdirectory DatasyncLocationS3#subdirectory}.
        :param agent_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_s3#agent_arns DatasyncLocationS3#agent_arns}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_s3#id DatasyncLocationS3#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param s3_storage_class: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_s3#s3_storage_class DatasyncLocationS3#s3_storage_class}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_s3#tags DatasyncLocationS3#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_s3#tags_all DatasyncLocationS3#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(s3_config, dict):
            s3_config = DatasyncLocationS3S3Config(**s3_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bc947cdc0d61f04913696df9c2a39eac04e7c118f4bb3051b1834f6f89637a3)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument s3_bucket_arn", value=s3_bucket_arn, expected_type=type_hints["s3_bucket_arn"])
            check_type(argname="argument s3_config", value=s3_config, expected_type=type_hints["s3_config"])
            check_type(argname="argument subdirectory", value=subdirectory, expected_type=type_hints["subdirectory"])
            check_type(argname="argument agent_arns", value=agent_arns, expected_type=type_hints["agent_arns"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument s3_storage_class", value=s3_storage_class, expected_type=type_hints["s3_storage_class"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "s3_bucket_arn": s3_bucket_arn,
            "s3_config": s3_config,
            "subdirectory": subdirectory,
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
        if agent_arns is not None:
            self._values["agent_arns"] = agent_arns
        if id is not None:
            self._values["id"] = id
        if s3_storage_class is not None:
            self._values["s3_storage_class"] = s3_storage_class
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
    def s3_bucket_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_s3#s3_bucket_arn DatasyncLocationS3#s3_bucket_arn}.'''
        result = self._values.get("s3_bucket_arn")
        assert result is not None, "Required property 's3_bucket_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def s3_config(self) -> "DatasyncLocationS3S3Config":
        '''s3_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_s3#s3_config DatasyncLocationS3#s3_config}
        '''
        result = self._values.get("s3_config")
        assert result is not None, "Required property 's3_config' is missing"
        return typing.cast("DatasyncLocationS3S3Config", result)

    @builtins.property
    def subdirectory(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_s3#subdirectory DatasyncLocationS3#subdirectory}.'''
        result = self._values.get("subdirectory")
        assert result is not None, "Required property 'subdirectory' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def agent_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_s3#agent_arns DatasyncLocationS3#agent_arns}.'''
        result = self._values.get("agent_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_s3#id DatasyncLocationS3#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_storage_class(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_s3#s3_storage_class DatasyncLocationS3#s3_storage_class}.'''
        result = self._values.get("s3_storage_class")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_s3#tags DatasyncLocationS3#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_s3#tags_all DatasyncLocationS3#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatasyncLocationS3Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.datasyncLocationS3.DatasyncLocationS3S3Config",
    jsii_struct_bases=[],
    name_mapping={"bucket_access_role_arn": "bucketAccessRoleArn"},
)
class DatasyncLocationS3S3Config:
    def __init__(self, *, bucket_access_role_arn: builtins.str) -> None:
        '''
        :param bucket_access_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_s3#bucket_access_role_arn DatasyncLocationS3#bucket_access_role_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d91999c1ad4136846a149e20f697b9512c4b452f6d01f5ac65c5f8a49f0a6ce)
            check_type(argname="argument bucket_access_role_arn", value=bucket_access_role_arn, expected_type=type_hints["bucket_access_role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket_access_role_arn": bucket_access_role_arn,
        }

    @builtins.property
    def bucket_access_role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/datasync_location_s3#bucket_access_role_arn DatasyncLocationS3#bucket_access_role_arn}.'''
        result = self._values.get("bucket_access_role_arn")
        assert result is not None, "Required property 'bucket_access_role_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatasyncLocationS3S3Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DatasyncLocationS3S3ConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.datasyncLocationS3.DatasyncLocationS3S3ConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__aae2c8b7fa8a9d9f41721f2b010d09a008134143fb3fa251bff83162db316d4f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="bucketAccessRoleArnInput")
    def bucket_access_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketAccessRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketAccessRoleArn")
    def bucket_access_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketAccessRoleArn"))

    @bucket_access_role_arn.setter
    def bucket_access_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc39b3175d1fc68e4a593fcb9a4e8b72697cbd5056b14d01c91287712fc2b75c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketAccessRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DatasyncLocationS3S3Config]:
        return typing.cast(typing.Optional[DatasyncLocationS3S3Config], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DatasyncLocationS3S3Config],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9048bb621e9fbe7854dc5045fe7c0eb3b67e31c26d95fec142c5d872a94be7a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DatasyncLocationS3",
    "DatasyncLocationS3Config",
    "DatasyncLocationS3S3Config",
    "DatasyncLocationS3S3ConfigOutputReference",
]

publication.publish()

def _typecheckingstub__bd637910dac96522c410d505412c923406bec6c685850cc15beca85eb03c8bc0(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    s3_bucket_arn: builtins.str,
    s3_config: typing.Union[DatasyncLocationS3S3Config, typing.Dict[builtins.str, typing.Any]],
    subdirectory: builtins.str,
    agent_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    id: typing.Optional[builtins.str] = None,
    s3_storage_class: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__9fdc69ec2e0fe6f003a2b05b844b782822b2dce44744155f5d0bfd8ee6160b60(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f49b868446c8b5a800eb44fec0b109f535980cfc3e55c38d54ccef72c5f95f2d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b82b44f8cbeb337b005845c8243a51411c58d4725040d9176845e32b46904182(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acf617e378301cdff63c6dbdd104a3ad6a2f5661bfa8a26da6ea22f4f47084bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6929aaa3e3ac4e1aee1b1a723446fe537d1d60af968e5b74b1cef0fc59b94b2c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__884bacea29a72ba33770c4873b61afda2deb09eb7cd0721b9661ddc6c57cfa27(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91397981cdf26a7bb7e2097ca12825a32c50458ada3e37b7a3f80fb5d75a0a31(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bc947cdc0d61f04913696df9c2a39eac04e7c118f4bb3051b1834f6f89637a3(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    s3_bucket_arn: builtins.str,
    s3_config: typing.Union[DatasyncLocationS3S3Config, typing.Dict[builtins.str, typing.Any]],
    subdirectory: builtins.str,
    agent_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    id: typing.Optional[builtins.str] = None,
    s3_storage_class: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d91999c1ad4136846a149e20f697b9512c4b452f6d01f5ac65c5f8a49f0a6ce(
    *,
    bucket_access_role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aae2c8b7fa8a9d9f41721f2b010d09a008134143fb3fa251bff83162db316d4f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc39b3175d1fc68e4a593fcb9a4e8b72697cbd5056b14d01c91287712fc2b75c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9048bb621e9fbe7854dc5045fe7c0eb3b67e31c26d95fec142c5d872a94be7a1(
    value: typing.Optional[DatasyncLocationS3S3Config],
) -> None:
    """Type checking stubs"""
    pass
