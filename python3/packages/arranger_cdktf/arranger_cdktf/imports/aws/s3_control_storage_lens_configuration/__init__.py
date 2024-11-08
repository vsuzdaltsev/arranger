'''
# `aws_s3control_storage_lens_configuration`

Refer to the Terraform Registory for docs: [`aws_s3control_storage_lens_configuration`](https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration).
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


class S3ControlStorageLensConfiguration(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfiguration",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration aws_s3control_storage_lens_configuration}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        config_id: builtins.str,
        storage_lens_configuration: typing.Union["S3ControlStorageLensConfigurationStorageLensConfiguration", typing.Dict[builtins.str, typing.Any]],
        account_id: typing.Optional[builtins.str] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration aws_s3control_storage_lens_configuration} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param config_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#config_id S3ControlStorageLensConfiguration#config_id}.
        :param storage_lens_configuration: storage_lens_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#storage_lens_configuration S3ControlStorageLensConfiguration#storage_lens_configuration}
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#account_id S3ControlStorageLensConfiguration#account_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#id S3ControlStorageLensConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#tags S3ControlStorageLensConfiguration#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#tags_all S3ControlStorageLensConfiguration#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e77f92f627da133b3a6df8b540fd9175d429856efe199f56f2c0896456bc84b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = S3ControlStorageLensConfigurationConfig(
            config_id=config_id,
            storage_lens_configuration=storage_lens_configuration,
            account_id=account_id,
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

    @jsii.member(jsii_name="putStorageLensConfiguration")
    def put_storage_lens_configuration(
        self,
        *,
        account_level: typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevel", typing.Dict[builtins.str, typing.Any]],
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        aws_org: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrg", typing.Dict[builtins.str, typing.Any]]] = None,
        data_export: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationDataExport", typing.Dict[builtins.str, typing.Any]]] = None,
        exclude: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationExclude", typing.Dict[builtins.str, typing.Any]]] = None,
        include: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationInclude", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param account_level: account_level block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#account_level S3ControlStorageLensConfiguration#account_level}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.
        :param aws_org: aws_org block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#aws_org S3ControlStorageLensConfiguration#aws_org}
        :param data_export: data_export block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#data_export S3ControlStorageLensConfiguration#data_export}
        :param exclude: exclude block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#exclude S3ControlStorageLensConfiguration#exclude}
        :param include: include block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#include S3ControlStorageLensConfiguration#include}
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfiguration(
            account_level=account_level,
            enabled=enabled,
            aws_org=aws_org,
            data_export=data_export,
            exclude=exclude,
            include=include,
        )

        return typing.cast(None, jsii.invoke(self, "putStorageLensConfiguration", [value]))

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

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
    @jsii.member(jsii_name="storageLensConfiguration")
    def storage_lens_configuration(
        self,
    ) -> "S3ControlStorageLensConfigurationStorageLensConfigurationOutputReference":
        return typing.cast("S3ControlStorageLensConfigurationStorageLensConfigurationOutputReference", jsii.get(self, "storageLensConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="configIdInput")
    def config_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="storageLensConfigurationInput")
    def storage_lens_configuration_input(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfiguration"]:
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfiguration"], jsii.get(self, "storageLensConfigurationInput"))

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
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cd569fe4c52a13ce41357d11b5392eb3f3e066238804673fb321bb13a819e9a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="configId")
    def config_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configId"))

    @config_id.setter
    def config_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a73c9a316b83fe31eadd5a17e1f52749d079863605a6f45e25facf99af5df747)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcb566e24bf94f515af9331810f90f38debcfacd8175e2d57011ee31a1bda4dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55239a3f35f96c6cedd4495a0cdbd1f2c3c5c8e063812eec88b79a614f4357d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96432fb78c643dd5a48080216b0262963900cc477c3883040a03715e051f3b08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "config_id": "configId",
        "storage_lens_configuration": "storageLensConfiguration",
        "account_id": "accountId",
        "id": "id",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class S3ControlStorageLensConfigurationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        config_id: builtins.str,
        storage_lens_configuration: typing.Union["S3ControlStorageLensConfigurationStorageLensConfiguration", typing.Dict[builtins.str, typing.Any]],
        account_id: typing.Optional[builtins.str] = None,
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
        :param config_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#config_id S3ControlStorageLensConfiguration#config_id}.
        :param storage_lens_configuration: storage_lens_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#storage_lens_configuration S3ControlStorageLensConfiguration#storage_lens_configuration}
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#account_id S3ControlStorageLensConfiguration#account_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#id S3ControlStorageLensConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#tags S3ControlStorageLensConfiguration#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#tags_all S3ControlStorageLensConfiguration#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(storage_lens_configuration, dict):
            storage_lens_configuration = S3ControlStorageLensConfigurationStorageLensConfiguration(**storage_lens_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d177c3dc8f5225d2ed765b7e528fa1e8cf31f2d4094eefa7c04577e80007bfa1)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument config_id", value=config_id, expected_type=type_hints["config_id"])
            check_type(argname="argument storage_lens_configuration", value=storage_lens_configuration, expected_type=type_hints["storage_lens_configuration"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "config_id": config_id,
            "storage_lens_configuration": storage_lens_configuration,
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
        if account_id is not None:
            self._values["account_id"] = account_id
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
    def config_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#config_id S3ControlStorageLensConfiguration#config_id}.'''
        result = self._values.get("config_id")
        assert result is not None, "Required property 'config_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_lens_configuration(
        self,
    ) -> "S3ControlStorageLensConfigurationStorageLensConfiguration":
        '''storage_lens_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#storage_lens_configuration S3ControlStorageLensConfiguration#storage_lens_configuration}
        '''
        result = self._values.get("storage_lens_configuration")
        assert result is not None, "Required property 'storage_lens_configuration' is missing"
        return typing.cast("S3ControlStorageLensConfigurationStorageLensConfiguration", result)

    @builtins.property
    def account_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#account_id S3ControlStorageLensConfiguration#account_id}.'''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#id S3ControlStorageLensConfiguration#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#tags S3ControlStorageLensConfiguration#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#tags_all S3ControlStorageLensConfiguration#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "account_level": "accountLevel",
        "enabled": "enabled",
        "aws_org": "awsOrg",
        "data_export": "dataExport",
        "exclude": "exclude",
        "include": "include",
    },
)
class S3ControlStorageLensConfigurationStorageLensConfiguration:
    def __init__(
        self,
        *,
        account_level: typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevel", typing.Dict[builtins.str, typing.Any]],
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        aws_org: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrg", typing.Dict[builtins.str, typing.Any]]] = None,
        data_export: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationDataExport", typing.Dict[builtins.str, typing.Any]]] = None,
        exclude: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationExclude", typing.Dict[builtins.str, typing.Any]]] = None,
        include: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationInclude", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param account_level: account_level block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#account_level S3ControlStorageLensConfiguration#account_level}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.
        :param aws_org: aws_org block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#aws_org S3ControlStorageLensConfiguration#aws_org}
        :param data_export: data_export block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#data_export S3ControlStorageLensConfiguration#data_export}
        :param exclude: exclude block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#exclude S3ControlStorageLensConfiguration#exclude}
        :param include: include block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#include S3ControlStorageLensConfiguration#include}
        '''
        if isinstance(account_level, dict):
            account_level = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevel(**account_level)
        if isinstance(aws_org, dict):
            aws_org = S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrg(**aws_org)
        if isinstance(data_export, dict):
            data_export = S3ControlStorageLensConfigurationStorageLensConfigurationDataExport(**data_export)
        if isinstance(exclude, dict):
            exclude = S3ControlStorageLensConfigurationStorageLensConfigurationExclude(**exclude)
        if isinstance(include, dict):
            include = S3ControlStorageLensConfigurationStorageLensConfigurationInclude(**include)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cc734b6d0ad45d0e4e8311790fbfcf7d2cbf20abbf6395bb5e5bf3b1b8f916c)
            check_type(argname="argument account_level", value=account_level, expected_type=type_hints["account_level"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument aws_org", value=aws_org, expected_type=type_hints["aws_org"])
            check_type(argname="argument data_export", value=data_export, expected_type=type_hints["data_export"])
            check_type(argname="argument exclude", value=exclude, expected_type=type_hints["exclude"])
            check_type(argname="argument include", value=include, expected_type=type_hints["include"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_level": account_level,
            "enabled": enabled,
        }
        if aws_org is not None:
            self._values["aws_org"] = aws_org
        if data_export is not None:
            self._values["data_export"] = data_export
        if exclude is not None:
            self._values["exclude"] = exclude
        if include is not None:
            self._values["include"] = include

    @builtins.property
    def account_level(
        self,
    ) -> "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevel":
        '''account_level block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#account_level S3ControlStorageLensConfiguration#account_level}
        '''
        result = self._values.get("account_level")
        assert result is not None, "Required property 'account_level' is missing"
        return typing.cast("S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevel", result)

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def aws_org(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrg"]:
        '''aws_org block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#aws_org S3ControlStorageLensConfiguration#aws_org}
        '''
        result = self._values.get("aws_org")
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrg"], result)

    @builtins.property
    def data_export(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationDataExport"]:
        '''data_export block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#data_export S3ControlStorageLensConfiguration#data_export}
        '''
        result = self._values.get("data_export")
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationDataExport"], result)

    @builtins.property
    def exclude(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationExclude"]:
        '''exclude block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#exclude S3ControlStorageLensConfiguration#exclude}
        '''
        result = self._values.get("exclude")
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationExclude"], result)

    @builtins.property
    def include(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationInclude"]:
        '''include block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#include S3ControlStorageLensConfiguration#include}
        '''
        result = self._values.get("include")
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationInclude"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevel",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_level": "bucketLevel",
        "activity_metrics": "activityMetrics",
        "advanced_cost_optimization_metrics": "advancedCostOptimizationMetrics",
        "advanced_data_protection_metrics": "advancedDataProtectionMetrics",
        "detailed_status_code_metrics": "detailedStatusCodeMetrics",
    },
)
class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevel:
    def __init__(
        self,
        *,
        bucket_level: typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevel", typing.Dict[builtins.str, typing.Any]],
        activity_metrics: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetrics", typing.Dict[builtins.str, typing.Any]]] = None,
        advanced_cost_optimization_metrics: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedCostOptimizationMetrics", typing.Dict[builtins.str, typing.Any]]] = None,
        advanced_data_protection_metrics: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedDataProtectionMetrics", typing.Dict[builtins.str, typing.Any]]] = None,
        detailed_status_code_metrics: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelDetailedStatusCodeMetrics", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param bucket_level: bucket_level block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#bucket_level S3ControlStorageLensConfiguration#bucket_level}
        :param activity_metrics: activity_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#activity_metrics S3ControlStorageLensConfiguration#activity_metrics}
        :param advanced_cost_optimization_metrics: advanced_cost_optimization_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#advanced_cost_optimization_metrics S3ControlStorageLensConfiguration#advanced_cost_optimization_metrics}
        :param advanced_data_protection_metrics: advanced_data_protection_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#advanced_data_protection_metrics S3ControlStorageLensConfiguration#advanced_data_protection_metrics}
        :param detailed_status_code_metrics: detailed_status_code_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#detailed_status_code_metrics S3ControlStorageLensConfiguration#detailed_status_code_metrics}
        '''
        if isinstance(bucket_level, dict):
            bucket_level = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevel(**bucket_level)
        if isinstance(activity_metrics, dict):
            activity_metrics = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetrics(**activity_metrics)
        if isinstance(advanced_cost_optimization_metrics, dict):
            advanced_cost_optimization_metrics = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedCostOptimizationMetrics(**advanced_cost_optimization_metrics)
        if isinstance(advanced_data_protection_metrics, dict):
            advanced_data_protection_metrics = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedDataProtectionMetrics(**advanced_data_protection_metrics)
        if isinstance(detailed_status_code_metrics, dict):
            detailed_status_code_metrics = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelDetailedStatusCodeMetrics(**detailed_status_code_metrics)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ce225400785f6db0ac4425d907720f6aa408ef91298e40fa4d3b444a1c39d2c)
            check_type(argname="argument bucket_level", value=bucket_level, expected_type=type_hints["bucket_level"])
            check_type(argname="argument activity_metrics", value=activity_metrics, expected_type=type_hints["activity_metrics"])
            check_type(argname="argument advanced_cost_optimization_metrics", value=advanced_cost_optimization_metrics, expected_type=type_hints["advanced_cost_optimization_metrics"])
            check_type(argname="argument advanced_data_protection_metrics", value=advanced_data_protection_metrics, expected_type=type_hints["advanced_data_protection_metrics"])
            check_type(argname="argument detailed_status_code_metrics", value=detailed_status_code_metrics, expected_type=type_hints["detailed_status_code_metrics"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket_level": bucket_level,
        }
        if activity_metrics is not None:
            self._values["activity_metrics"] = activity_metrics
        if advanced_cost_optimization_metrics is not None:
            self._values["advanced_cost_optimization_metrics"] = advanced_cost_optimization_metrics
        if advanced_data_protection_metrics is not None:
            self._values["advanced_data_protection_metrics"] = advanced_data_protection_metrics
        if detailed_status_code_metrics is not None:
            self._values["detailed_status_code_metrics"] = detailed_status_code_metrics

    @builtins.property
    def bucket_level(
        self,
    ) -> "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevel":
        '''bucket_level block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#bucket_level S3ControlStorageLensConfiguration#bucket_level}
        '''
        result = self._values.get("bucket_level")
        assert result is not None, "Required property 'bucket_level' is missing"
        return typing.cast("S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevel", result)

    @builtins.property
    def activity_metrics(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetrics"]:
        '''activity_metrics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#activity_metrics S3ControlStorageLensConfiguration#activity_metrics}
        '''
        result = self._values.get("activity_metrics")
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetrics"], result)

    @builtins.property
    def advanced_cost_optimization_metrics(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedCostOptimizationMetrics"]:
        '''advanced_cost_optimization_metrics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#advanced_cost_optimization_metrics S3ControlStorageLensConfiguration#advanced_cost_optimization_metrics}
        '''
        result = self._values.get("advanced_cost_optimization_metrics")
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedCostOptimizationMetrics"], result)

    @builtins.property
    def advanced_data_protection_metrics(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedDataProtectionMetrics"]:
        '''advanced_data_protection_metrics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#advanced_data_protection_metrics S3ControlStorageLensConfiguration#advanced_data_protection_metrics}
        '''
        result = self._values.get("advanced_data_protection_metrics")
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedDataProtectionMetrics"], result)

    @builtins.property
    def detailed_status_code_metrics(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelDetailedStatusCodeMetrics"]:
        '''detailed_status_code_metrics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#detailed_status_code_metrics S3ControlStorageLensConfiguration#detailed_status_code_metrics}
        '''
        result = self._values.get("detailed_status_code_metrics")
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelDetailedStatusCodeMetrics"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevel(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetrics",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetrics:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__627ed5ab0d976060a479a45c547e9c234d3d275c578744b026356594d62d141e)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetrics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetricsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetricsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ecebdf5489ffd2e02b8baf142fd7140a72001ce29d4d674589335eecc9af68bc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__045c2c3f57cc08d85109723eb0753f83e9e16eb890bf2ee3a52b3a4c402f19de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetrics]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetrics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetrics],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__191c7c914d6f953502d706888c58b4c7c2f1230073c359195e7b2f9198b2d187)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedCostOptimizationMetrics",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedCostOptimizationMetrics:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6a56eb96a6f9cc9ad77c1832ec85310b691b2e9b7386a9a034d3c7a8b15783b)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedCostOptimizationMetrics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedCostOptimizationMetricsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedCostOptimizationMetricsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__62129a26fdc1ba16ce13aece57854dbabb974a1b749082c860a0196b8a1e53c6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__001fa0876b67f70aa388df6233b5453d391b4a6412670b9e9514d766e9ee9cb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedCostOptimizationMetrics]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedCostOptimizationMetrics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedCostOptimizationMetrics],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4faf3071c380c66f335badce049d6416e1a4061c15f447278b64d6b52f0113b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedDataProtectionMetrics",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedDataProtectionMetrics:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8bd535e67fef98951382fb05d094c055b0b6d094a830065754df3ee81ef22046)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedDataProtectionMetrics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedDataProtectionMetricsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedDataProtectionMetricsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ae40ef6ff0b517e89c5d0b8e6c20d8f534b8c891aad348d4f8eaf7a2b55b4212)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__3114a615b5dfa2c282bcd742586eec685d561edba3b102def8c24690097f9858)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedDataProtectionMetrics]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedDataProtectionMetrics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedDataProtectionMetrics],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__043e3b8a9407d87153ecddb450d441a373cab3f51c582458a6051698e1921538)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevel",
    jsii_struct_bases=[],
    name_mapping={
        "activity_metrics": "activityMetrics",
        "advanced_cost_optimization_metrics": "advancedCostOptimizationMetrics",
        "advanced_data_protection_metrics": "advancedDataProtectionMetrics",
        "detailed_status_code_metrics": "detailedStatusCodeMetrics",
        "prefix_level": "prefixLevel",
    },
)
class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevel:
    def __init__(
        self,
        *,
        activity_metrics: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetrics", typing.Dict[builtins.str, typing.Any]]] = None,
        advanced_cost_optimization_metrics: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedCostOptimizationMetrics", typing.Dict[builtins.str, typing.Any]]] = None,
        advanced_data_protection_metrics: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedDataProtectionMetrics", typing.Dict[builtins.str, typing.Any]]] = None,
        detailed_status_code_metrics: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelDetailedStatusCodeMetrics", typing.Dict[builtins.str, typing.Any]]] = None,
        prefix_level: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevel", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param activity_metrics: activity_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#activity_metrics S3ControlStorageLensConfiguration#activity_metrics}
        :param advanced_cost_optimization_metrics: advanced_cost_optimization_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#advanced_cost_optimization_metrics S3ControlStorageLensConfiguration#advanced_cost_optimization_metrics}
        :param advanced_data_protection_metrics: advanced_data_protection_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#advanced_data_protection_metrics S3ControlStorageLensConfiguration#advanced_data_protection_metrics}
        :param detailed_status_code_metrics: detailed_status_code_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#detailed_status_code_metrics S3ControlStorageLensConfiguration#detailed_status_code_metrics}
        :param prefix_level: prefix_level block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#prefix_level S3ControlStorageLensConfiguration#prefix_level}
        '''
        if isinstance(activity_metrics, dict):
            activity_metrics = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetrics(**activity_metrics)
        if isinstance(advanced_cost_optimization_metrics, dict):
            advanced_cost_optimization_metrics = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedCostOptimizationMetrics(**advanced_cost_optimization_metrics)
        if isinstance(advanced_data_protection_metrics, dict):
            advanced_data_protection_metrics = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedDataProtectionMetrics(**advanced_data_protection_metrics)
        if isinstance(detailed_status_code_metrics, dict):
            detailed_status_code_metrics = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelDetailedStatusCodeMetrics(**detailed_status_code_metrics)
        if isinstance(prefix_level, dict):
            prefix_level = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevel(**prefix_level)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e06c3eb2ba021a3730626f8fab7dcfdff4e2ad2a7e683117c23e9726678ca375)
            check_type(argname="argument activity_metrics", value=activity_metrics, expected_type=type_hints["activity_metrics"])
            check_type(argname="argument advanced_cost_optimization_metrics", value=advanced_cost_optimization_metrics, expected_type=type_hints["advanced_cost_optimization_metrics"])
            check_type(argname="argument advanced_data_protection_metrics", value=advanced_data_protection_metrics, expected_type=type_hints["advanced_data_protection_metrics"])
            check_type(argname="argument detailed_status_code_metrics", value=detailed_status_code_metrics, expected_type=type_hints["detailed_status_code_metrics"])
            check_type(argname="argument prefix_level", value=prefix_level, expected_type=type_hints["prefix_level"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if activity_metrics is not None:
            self._values["activity_metrics"] = activity_metrics
        if advanced_cost_optimization_metrics is not None:
            self._values["advanced_cost_optimization_metrics"] = advanced_cost_optimization_metrics
        if advanced_data_protection_metrics is not None:
            self._values["advanced_data_protection_metrics"] = advanced_data_protection_metrics
        if detailed_status_code_metrics is not None:
            self._values["detailed_status_code_metrics"] = detailed_status_code_metrics
        if prefix_level is not None:
            self._values["prefix_level"] = prefix_level

    @builtins.property
    def activity_metrics(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetrics"]:
        '''activity_metrics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#activity_metrics S3ControlStorageLensConfiguration#activity_metrics}
        '''
        result = self._values.get("activity_metrics")
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetrics"], result)

    @builtins.property
    def advanced_cost_optimization_metrics(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedCostOptimizationMetrics"]:
        '''advanced_cost_optimization_metrics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#advanced_cost_optimization_metrics S3ControlStorageLensConfiguration#advanced_cost_optimization_metrics}
        '''
        result = self._values.get("advanced_cost_optimization_metrics")
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedCostOptimizationMetrics"], result)

    @builtins.property
    def advanced_data_protection_metrics(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedDataProtectionMetrics"]:
        '''advanced_data_protection_metrics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#advanced_data_protection_metrics S3ControlStorageLensConfiguration#advanced_data_protection_metrics}
        '''
        result = self._values.get("advanced_data_protection_metrics")
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedDataProtectionMetrics"], result)

    @builtins.property
    def detailed_status_code_metrics(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelDetailedStatusCodeMetrics"]:
        '''detailed_status_code_metrics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#detailed_status_code_metrics S3ControlStorageLensConfiguration#detailed_status_code_metrics}
        '''
        result = self._values.get("detailed_status_code_metrics")
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelDetailedStatusCodeMetrics"], result)

    @builtins.property
    def prefix_level(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevel"]:
        '''prefix_level block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#prefix_level S3ControlStorageLensConfiguration#prefix_level}
        '''
        result = self._values.get("prefix_level")
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevel"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevel(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetrics",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetrics:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95e878e46f47ade57f5c2fed337208673c85e897e50850ab37fa3c29e5ba7149)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetrics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetricsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetricsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2ddcc7623c85e553b71cbf161d354e0492a3df915714a4c204300cadb01dc031)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__c536af6d9d65fb49c62fa34be9858ac160ee9fb87b24dadfa79a327af242df03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetrics]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetrics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetrics],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03d78a72e54335ae035db2494a65a361b47878289f48596c2279ac863b687a41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedCostOptimizationMetrics",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedCostOptimizationMetrics:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d51cf86df5022461531478fe796677e52d50a0fd412c7945070829ebf192a863)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedCostOptimizationMetrics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedCostOptimizationMetricsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedCostOptimizationMetricsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__572c2f8175ae05f49f9606c22dd5510772d8df44ff631da72cbb2c4a0fd04dd3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__74b6a2fd0eb1dfd8651b02e4e785a5096d10d3558194a7e66be38d43c357d8a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedCostOptimizationMetrics]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedCostOptimizationMetrics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedCostOptimizationMetrics],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de73ad38307037828043b85063cb2ee9cde1c433917c30053d678eddb8db67df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedDataProtectionMetrics",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedDataProtectionMetrics:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8aed887175413c39aa67ab7ff474af4be6c5a658efe197a537afda25d0da9bb)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedDataProtectionMetrics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedDataProtectionMetricsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedDataProtectionMetricsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e8feed0f06ae78383ab52854fcf3fdc0930e039f29ee79009fe09e9e586cde27)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__f5f64deac6d68fd202532720fff163204c8d770f9a2b0eb9bba35bc94d3b8ef0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedDataProtectionMetrics]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedDataProtectionMetrics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedDataProtectionMetrics],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7e172fcc91d13dae4fb0de23f09e6eb5641fc384c09742a3511ae076d645a73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelDetailedStatusCodeMetrics",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelDetailedStatusCodeMetrics:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a68402f5890b61dc0270ad9116b4df22d153e8742c661cd2f4db80c31a22990e)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelDetailedStatusCodeMetrics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelDetailedStatusCodeMetricsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelDetailedStatusCodeMetricsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0b3a890d9222b3aebeed85436bac81cac3b044b8ddc3496e480f55a0bf8a3e90)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__f0b5c2cbcd034a705d228aa35cc21d0811862f8d84559f319e1171c450ea4083)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelDetailedStatusCodeMetrics]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelDetailedStatusCodeMetrics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelDetailedStatusCodeMetrics],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7b63bc3414312454f5fccc9f3d82fc6ad91f69b3ab0da9488b8e9ae20a1404f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d1a24041c5074fa93b04a9a7573e3b0f540e444705b2c1b34b1ae0506c095720)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putActivityMetrics")
    def put_activity_metrics(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetrics(
            enabled=enabled
        )

        return typing.cast(None, jsii.invoke(self, "putActivityMetrics", [value]))

    @jsii.member(jsii_name="putAdvancedCostOptimizationMetrics")
    def put_advanced_cost_optimization_metrics(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedCostOptimizationMetrics(
            enabled=enabled
        )

        return typing.cast(None, jsii.invoke(self, "putAdvancedCostOptimizationMetrics", [value]))

    @jsii.member(jsii_name="putAdvancedDataProtectionMetrics")
    def put_advanced_data_protection_metrics(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedDataProtectionMetrics(
            enabled=enabled
        )

        return typing.cast(None, jsii.invoke(self, "putAdvancedDataProtectionMetrics", [value]))

    @jsii.member(jsii_name="putDetailedStatusCodeMetrics")
    def put_detailed_status_code_metrics(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelDetailedStatusCodeMetrics(
            enabled=enabled
        )

        return typing.cast(None, jsii.invoke(self, "putDetailedStatusCodeMetrics", [value]))

    @jsii.member(jsii_name="putPrefixLevel")
    def put_prefix_level(
        self,
        *,
        storage_metrics: typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetrics", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param storage_metrics: storage_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#storage_metrics S3ControlStorageLensConfiguration#storage_metrics}
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevel(
            storage_metrics=storage_metrics
        )

        return typing.cast(None, jsii.invoke(self, "putPrefixLevel", [value]))

    @jsii.member(jsii_name="resetActivityMetrics")
    def reset_activity_metrics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActivityMetrics", []))

    @jsii.member(jsii_name="resetAdvancedCostOptimizationMetrics")
    def reset_advanced_cost_optimization_metrics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdvancedCostOptimizationMetrics", []))

    @jsii.member(jsii_name="resetAdvancedDataProtectionMetrics")
    def reset_advanced_data_protection_metrics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdvancedDataProtectionMetrics", []))

    @jsii.member(jsii_name="resetDetailedStatusCodeMetrics")
    def reset_detailed_status_code_metrics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDetailedStatusCodeMetrics", []))

    @jsii.member(jsii_name="resetPrefixLevel")
    def reset_prefix_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefixLevel", []))

    @builtins.property
    @jsii.member(jsii_name="activityMetrics")
    def activity_metrics(
        self,
    ) -> S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetricsOutputReference:
        return typing.cast(S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetricsOutputReference, jsii.get(self, "activityMetrics"))

    @builtins.property
    @jsii.member(jsii_name="advancedCostOptimizationMetrics")
    def advanced_cost_optimization_metrics(
        self,
    ) -> S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedCostOptimizationMetricsOutputReference:
        return typing.cast(S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedCostOptimizationMetricsOutputReference, jsii.get(self, "advancedCostOptimizationMetrics"))

    @builtins.property
    @jsii.member(jsii_name="advancedDataProtectionMetrics")
    def advanced_data_protection_metrics(
        self,
    ) -> S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedDataProtectionMetricsOutputReference:
        return typing.cast(S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedDataProtectionMetricsOutputReference, jsii.get(self, "advancedDataProtectionMetrics"))

    @builtins.property
    @jsii.member(jsii_name="detailedStatusCodeMetrics")
    def detailed_status_code_metrics(
        self,
    ) -> S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelDetailedStatusCodeMetricsOutputReference:
        return typing.cast(S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelDetailedStatusCodeMetricsOutputReference, jsii.get(self, "detailedStatusCodeMetrics"))

    @builtins.property
    @jsii.member(jsii_name="prefixLevel")
    def prefix_level(
        self,
    ) -> "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelOutputReference":
        return typing.cast("S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelOutputReference", jsii.get(self, "prefixLevel"))

    @builtins.property
    @jsii.member(jsii_name="activityMetricsInput")
    def activity_metrics_input(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetrics]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetrics], jsii.get(self, "activityMetricsInput"))

    @builtins.property
    @jsii.member(jsii_name="advancedCostOptimizationMetricsInput")
    def advanced_cost_optimization_metrics_input(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedCostOptimizationMetrics]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedCostOptimizationMetrics], jsii.get(self, "advancedCostOptimizationMetricsInput"))

    @builtins.property
    @jsii.member(jsii_name="advancedDataProtectionMetricsInput")
    def advanced_data_protection_metrics_input(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedDataProtectionMetrics]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedDataProtectionMetrics], jsii.get(self, "advancedDataProtectionMetricsInput"))

    @builtins.property
    @jsii.member(jsii_name="detailedStatusCodeMetricsInput")
    def detailed_status_code_metrics_input(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelDetailedStatusCodeMetrics]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelDetailedStatusCodeMetrics], jsii.get(self, "detailedStatusCodeMetricsInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixLevelInput")
    def prefix_level_input(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevel"]:
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevel"], jsii.get(self, "prefixLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevel]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevel], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevel],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c04d8266aca5ae3d38b5fa990a46450ee33430ce7cf6cc4f5b28d9bfcd12b580)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevel",
    jsii_struct_bases=[],
    name_mapping={"storage_metrics": "storageMetrics"},
)
class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevel:
    def __init__(
        self,
        *,
        storage_metrics: typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetrics", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param storage_metrics: storage_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#storage_metrics S3ControlStorageLensConfiguration#storage_metrics}
        '''
        if isinstance(storage_metrics, dict):
            storage_metrics = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetrics(**storage_metrics)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5b6d0b23cf1f6b7deba0a81d66ee3c43b225e3058059e91aa56cb16be3830f2)
            check_type(argname="argument storage_metrics", value=storage_metrics, expected_type=type_hints["storage_metrics"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "storage_metrics": storage_metrics,
        }

    @builtins.property
    def storage_metrics(
        self,
    ) -> "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetrics":
        '''storage_metrics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#storage_metrics S3ControlStorageLensConfiguration#storage_metrics}
        '''
        result = self._values.get("storage_metrics")
        assert result is not None, "Required property 'storage_metrics' is missing"
        return typing.cast("S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetrics", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevel(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2a3bb9c03371c544ea09cc5c07337531b0ff8ea0d0e5f9c7393666e05d4a5edf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putStorageMetrics")
    def put_storage_metrics(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        selection_criteria: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteria", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.
        :param selection_criteria: selection_criteria block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#selection_criteria S3ControlStorageLensConfiguration#selection_criteria}
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetrics(
            enabled=enabled, selection_criteria=selection_criteria
        )

        return typing.cast(None, jsii.invoke(self, "putStorageMetrics", [value]))

    @builtins.property
    @jsii.member(jsii_name="storageMetrics")
    def storage_metrics(
        self,
    ) -> "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsOutputReference":
        return typing.cast("S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsOutputReference", jsii.get(self, "storageMetrics"))

    @builtins.property
    @jsii.member(jsii_name="storageMetricsInput")
    def storage_metrics_input(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetrics"]:
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetrics"], jsii.get(self, "storageMetricsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevel]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevel], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevel],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__886a5c7f073b505de5aaed6397f30599619722332e2cf45dbe44c3ab2d4cfa0e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetrics",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "selection_criteria": "selectionCriteria"},
)
class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetrics:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        selection_criteria: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteria", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.
        :param selection_criteria: selection_criteria block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#selection_criteria S3ControlStorageLensConfiguration#selection_criteria}
        '''
        if isinstance(selection_criteria, dict):
            selection_criteria = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteria(**selection_criteria)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45dd58ae48794fcf01f2766d1e03da3e3e7d1c4d20ba130d967b2c58f29a69ba)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument selection_criteria", value=selection_criteria, expected_type=type_hints["selection_criteria"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if selection_criteria is not None:
            self._values["selection_criteria"] = selection_criteria

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def selection_criteria(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteria"]:
        '''selection_criteria block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#selection_criteria S3ControlStorageLensConfiguration#selection_criteria}
        '''
        result = self._values.get("selection_criteria")
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteria"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetrics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9defecefef2e84942707249deb6bb974374890c094e6caa29666871b528dc6c0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSelectionCriteria")
    def put_selection_criteria(
        self,
        *,
        delimiter: typing.Optional[builtins.str] = None,
        max_depth: typing.Optional[jsii.Number] = None,
        min_storage_bytes_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#delimiter S3ControlStorageLensConfiguration#delimiter}.
        :param max_depth: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#max_depth S3ControlStorageLensConfiguration#max_depth}.
        :param min_storage_bytes_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#min_storage_bytes_percentage S3ControlStorageLensConfiguration#min_storage_bytes_percentage}.
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteria(
            delimiter=delimiter,
            max_depth=max_depth,
            min_storage_bytes_percentage=min_storage_bytes_percentage,
        )

        return typing.cast(None, jsii.invoke(self, "putSelectionCriteria", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetSelectionCriteria")
    def reset_selection_criteria(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSelectionCriteria", []))

    @builtins.property
    @jsii.member(jsii_name="selectionCriteria")
    def selection_criteria(
        self,
    ) -> "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteriaOutputReference":
        return typing.cast("S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteriaOutputReference", jsii.get(self, "selectionCriteria"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="selectionCriteriaInput")
    def selection_criteria_input(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteria"]:
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteria"], jsii.get(self, "selectionCriteriaInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__c111d4f3ef0c5c1b8c29d1771e6c285896007aab003080e610965f578c8d1047)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetrics]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetrics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetrics],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89659894ab3c74b6b651d1dcd1e28f1737ab3177f56a1823214a35a94333b56b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteria",
    jsii_struct_bases=[],
    name_mapping={
        "delimiter": "delimiter",
        "max_depth": "maxDepth",
        "min_storage_bytes_percentage": "minStorageBytesPercentage",
    },
)
class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteria:
    def __init__(
        self,
        *,
        delimiter: typing.Optional[builtins.str] = None,
        max_depth: typing.Optional[jsii.Number] = None,
        min_storage_bytes_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param delimiter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#delimiter S3ControlStorageLensConfiguration#delimiter}.
        :param max_depth: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#max_depth S3ControlStorageLensConfiguration#max_depth}.
        :param min_storage_bytes_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#min_storage_bytes_percentage S3ControlStorageLensConfiguration#min_storage_bytes_percentage}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14effa2b187edab5a346072a3b1ed032e70a993a501d7dfd4a86c1cc62f32f0f)
            check_type(argname="argument delimiter", value=delimiter, expected_type=type_hints["delimiter"])
            check_type(argname="argument max_depth", value=max_depth, expected_type=type_hints["max_depth"])
            check_type(argname="argument min_storage_bytes_percentage", value=min_storage_bytes_percentage, expected_type=type_hints["min_storage_bytes_percentage"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if delimiter is not None:
            self._values["delimiter"] = delimiter
        if max_depth is not None:
            self._values["max_depth"] = max_depth
        if min_storage_bytes_percentage is not None:
            self._values["min_storage_bytes_percentage"] = min_storage_bytes_percentage

    @builtins.property
    def delimiter(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#delimiter S3ControlStorageLensConfiguration#delimiter}.'''
        result = self._values.get("delimiter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_depth(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#max_depth S3ControlStorageLensConfiguration#max_depth}.'''
        result = self._values.get("max_depth")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_storage_bytes_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#min_storage_bytes_percentage S3ControlStorageLensConfiguration#min_storage_bytes_percentage}.'''
        result = self._values.get("min_storage_bytes_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteria(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteriaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteriaOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4a3932978ec511b407cd4b12382c0063574bdcc719c3a0934dd81a19a6ab6c91)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDelimiter")
    def reset_delimiter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelimiter", []))

    @jsii.member(jsii_name="resetMaxDepth")
    def reset_max_depth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxDepth", []))

    @jsii.member(jsii_name="resetMinStorageBytesPercentage")
    def reset_min_storage_bytes_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinStorageBytesPercentage", []))

    @builtins.property
    @jsii.member(jsii_name="delimiterInput")
    def delimiter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "delimiterInput"))

    @builtins.property
    @jsii.member(jsii_name="maxDepthInput")
    def max_depth_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxDepthInput"))

    @builtins.property
    @jsii.member(jsii_name="minStorageBytesPercentageInput")
    def min_storage_bytes_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minStorageBytesPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="delimiter")
    def delimiter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delimiter"))

    @delimiter.setter
    def delimiter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95f39c9849b2af9ca55af55624e79ac02debaf01f246bb514975ff7e6d4a09e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delimiter", value)

    @builtins.property
    @jsii.member(jsii_name="maxDepth")
    def max_depth(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxDepth"))

    @max_depth.setter
    def max_depth(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b0404db0b36527bb412b5c673da1138a3335a0e16bfd9c252af7ebae12eb967)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxDepth", value)

    @builtins.property
    @jsii.member(jsii_name="minStorageBytesPercentage")
    def min_storage_bytes_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minStorageBytesPercentage"))

    @min_storage_bytes_percentage.setter
    def min_storage_bytes_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b768be731261ce50f54e46690ee16181ba681608e74101c5bb68246c02c4e28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minStorageBytesPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteria]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteria], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteria],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e35d9c9f438b920a898637804fec920ff8272caf9822e8cede81a3628707cac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelDetailedStatusCodeMetrics",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelDetailedStatusCodeMetrics:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__496e84851ee18b70f7586442593455225c3badbbe2abaf0dd00a413e345d4bc0)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelDetailedStatusCodeMetrics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelDetailedStatusCodeMetricsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelDetailedStatusCodeMetricsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f3d26c303c2f5e94a5a313154bab9001e9b24885acd63b6154c19a782c53abbf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__b6acf6e21a833416f3b7d3f94c380f7e7049778b75643f5bac39e781c0d1f12d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelDetailedStatusCodeMetrics]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelDetailedStatusCodeMetrics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelDetailedStatusCodeMetrics],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e147f0a4347306195af9f42144b1e1b8208a0f5862cca966a8df8f743b35c631)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d4188af18d39db426d82e10f6801a65cc7112eef17d53bd89464462bf9b146af)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putActivityMetrics")
    def put_activity_metrics(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetrics(
            enabled=enabled
        )

        return typing.cast(None, jsii.invoke(self, "putActivityMetrics", [value]))

    @jsii.member(jsii_name="putAdvancedCostOptimizationMetrics")
    def put_advanced_cost_optimization_metrics(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedCostOptimizationMetrics(
            enabled=enabled
        )

        return typing.cast(None, jsii.invoke(self, "putAdvancedCostOptimizationMetrics", [value]))

    @jsii.member(jsii_name="putAdvancedDataProtectionMetrics")
    def put_advanced_data_protection_metrics(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedDataProtectionMetrics(
            enabled=enabled
        )

        return typing.cast(None, jsii.invoke(self, "putAdvancedDataProtectionMetrics", [value]))

    @jsii.member(jsii_name="putBucketLevel")
    def put_bucket_level(
        self,
        *,
        activity_metrics: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetrics, typing.Dict[builtins.str, typing.Any]]] = None,
        advanced_cost_optimization_metrics: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedCostOptimizationMetrics, typing.Dict[builtins.str, typing.Any]]] = None,
        advanced_data_protection_metrics: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedDataProtectionMetrics, typing.Dict[builtins.str, typing.Any]]] = None,
        detailed_status_code_metrics: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelDetailedStatusCodeMetrics, typing.Dict[builtins.str, typing.Any]]] = None,
        prefix_level: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevel, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param activity_metrics: activity_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#activity_metrics S3ControlStorageLensConfiguration#activity_metrics}
        :param advanced_cost_optimization_metrics: advanced_cost_optimization_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#advanced_cost_optimization_metrics S3ControlStorageLensConfiguration#advanced_cost_optimization_metrics}
        :param advanced_data_protection_metrics: advanced_data_protection_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#advanced_data_protection_metrics S3ControlStorageLensConfiguration#advanced_data_protection_metrics}
        :param detailed_status_code_metrics: detailed_status_code_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#detailed_status_code_metrics S3ControlStorageLensConfiguration#detailed_status_code_metrics}
        :param prefix_level: prefix_level block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#prefix_level S3ControlStorageLensConfiguration#prefix_level}
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevel(
            activity_metrics=activity_metrics,
            advanced_cost_optimization_metrics=advanced_cost_optimization_metrics,
            advanced_data_protection_metrics=advanced_data_protection_metrics,
            detailed_status_code_metrics=detailed_status_code_metrics,
            prefix_level=prefix_level,
        )

        return typing.cast(None, jsii.invoke(self, "putBucketLevel", [value]))

    @jsii.member(jsii_name="putDetailedStatusCodeMetrics")
    def put_detailed_status_code_metrics(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelDetailedStatusCodeMetrics(
            enabled=enabled
        )

        return typing.cast(None, jsii.invoke(self, "putDetailedStatusCodeMetrics", [value]))

    @jsii.member(jsii_name="resetActivityMetrics")
    def reset_activity_metrics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActivityMetrics", []))

    @jsii.member(jsii_name="resetAdvancedCostOptimizationMetrics")
    def reset_advanced_cost_optimization_metrics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdvancedCostOptimizationMetrics", []))

    @jsii.member(jsii_name="resetAdvancedDataProtectionMetrics")
    def reset_advanced_data_protection_metrics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdvancedDataProtectionMetrics", []))

    @jsii.member(jsii_name="resetDetailedStatusCodeMetrics")
    def reset_detailed_status_code_metrics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDetailedStatusCodeMetrics", []))

    @builtins.property
    @jsii.member(jsii_name="activityMetrics")
    def activity_metrics(
        self,
    ) -> S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetricsOutputReference:
        return typing.cast(S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetricsOutputReference, jsii.get(self, "activityMetrics"))

    @builtins.property
    @jsii.member(jsii_name="advancedCostOptimizationMetrics")
    def advanced_cost_optimization_metrics(
        self,
    ) -> S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedCostOptimizationMetricsOutputReference:
        return typing.cast(S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedCostOptimizationMetricsOutputReference, jsii.get(self, "advancedCostOptimizationMetrics"))

    @builtins.property
    @jsii.member(jsii_name="advancedDataProtectionMetrics")
    def advanced_data_protection_metrics(
        self,
    ) -> S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedDataProtectionMetricsOutputReference:
        return typing.cast(S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedDataProtectionMetricsOutputReference, jsii.get(self, "advancedDataProtectionMetrics"))

    @builtins.property
    @jsii.member(jsii_name="bucketLevel")
    def bucket_level(
        self,
    ) -> S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelOutputReference:
        return typing.cast(S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelOutputReference, jsii.get(self, "bucketLevel"))

    @builtins.property
    @jsii.member(jsii_name="detailedStatusCodeMetrics")
    def detailed_status_code_metrics(
        self,
    ) -> S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelDetailedStatusCodeMetricsOutputReference:
        return typing.cast(S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelDetailedStatusCodeMetricsOutputReference, jsii.get(self, "detailedStatusCodeMetrics"))

    @builtins.property
    @jsii.member(jsii_name="activityMetricsInput")
    def activity_metrics_input(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetrics]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetrics], jsii.get(self, "activityMetricsInput"))

    @builtins.property
    @jsii.member(jsii_name="advancedCostOptimizationMetricsInput")
    def advanced_cost_optimization_metrics_input(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedCostOptimizationMetrics]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedCostOptimizationMetrics], jsii.get(self, "advancedCostOptimizationMetricsInput"))

    @builtins.property
    @jsii.member(jsii_name="advancedDataProtectionMetricsInput")
    def advanced_data_protection_metrics_input(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedDataProtectionMetrics]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedDataProtectionMetrics], jsii.get(self, "advancedDataProtectionMetricsInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketLevelInput")
    def bucket_level_input(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevel]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevel], jsii.get(self, "bucketLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="detailedStatusCodeMetricsInput")
    def detailed_status_code_metrics_input(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelDetailedStatusCodeMetrics]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelDetailedStatusCodeMetrics], jsii.get(self, "detailedStatusCodeMetricsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevel]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevel], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevel],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68b5924b8c20c02e835676540cad23bc849c698c6948fb703a2e254c1666a044)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrg",
    jsii_struct_bases=[],
    name_mapping={"arn": "arn"},
)
class S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrg:
    def __init__(self, *, arn: builtins.str) -> None:
        '''
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#arn S3ControlStorageLensConfiguration#arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8deed62ce738341ff5c4150e6f2f4dc6b499b82f0232496f89eb5613fc4d9b96)
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "arn": arn,
        }

    @builtins.property
    def arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#arn S3ControlStorageLensConfiguration#arn}.'''
        result = self._values.get("arn")
        assert result is not None, "Required property 'arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrg(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrgOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrgOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a6241f5acd4e06d522a583fb30d61765a631851488a8ae16d3733734111e51bb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="arnInput")
    def arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "arnInput"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @arn.setter
    def arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__228b49645bf946019926307046ac3efac258de5520690974381f65b2ce1b62ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrg]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrg], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrg],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c3e1338fc0537dd7a5b0164175027471b5cf00e8d5328fc571d28414a559a90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationDataExport",
    jsii_struct_bases=[],
    name_mapping={
        "cloud_watch_metrics": "cloudWatchMetrics",
        "s3_bucket_destination": "s3BucketDestination",
    },
)
class S3ControlStorageLensConfigurationStorageLensConfigurationDataExport:
    def __init__(
        self,
        *,
        cloud_watch_metrics: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetrics", typing.Dict[builtins.str, typing.Any]]] = None,
        s3_bucket_destination: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestination", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cloud_watch_metrics: cloud_watch_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#cloud_watch_metrics S3ControlStorageLensConfiguration#cloud_watch_metrics}
        :param s3_bucket_destination: s3_bucket_destination block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#s3_bucket_destination S3ControlStorageLensConfiguration#s3_bucket_destination}
        '''
        if isinstance(cloud_watch_metrics, dict):
            cloud_watch_metrics = S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetrics(**cloud_watch_metrics)
        if isinstance(s3_bucket_destination, dict):
            s3_bucket_destination = S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestination(**s3_bucket_destination)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__446c5b84c5eda4e0df9be1b0ae58b36e387d16f54f88830ad0660b7c3f07b647)
            check_type(argname="argument cloud_watch_metrics", value=cloud_watch_metrics, expected_type=type_hints["cloud_watch_metrics"])
            check_type(argname="argument s3_bucket_destination", value=s3_bucket_destination, expected_type=type_hints["s3_bucket_destination"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cloud_watch_metrics is not None:
            self._values["cloud_watch_metrics"] = cloud_watch_metrics
        if s3_bucket_destination is not None:
            self._values["s3_bucket_destination"] = s3_bucket_destination

    @builtins.property
    def cloud_watch_metrics(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetrics"]:
        '''cloud_watch_metrics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#cloud_watch_metrics S3ControlStorageLensConfiguration#cloud_watch_metrics}
        '''
        result = self._values.get("cloud_watch_metrics")
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetrics"], result)

    @builtins.property
    def s3_bucket_destination(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestination"]:
        '''s3_bucket_destination block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#s3_bucket_destination S3ControlStorageLensConfiguration#s3_bucket_destination}
        '''
        result = self._values.get("s3_bucket_destination")
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestination"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationDataExport(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetrics",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetrics:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ede7ff0d27622b5cc8bf6bdff987783e08fd4a09e18f92b207d9b3ef1ea22cd8)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled": enabled,
        }

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetrics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetricsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetricsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__856f34004f8df6b83e9ef1936412157a0733acf933ae5600cb50b43b18848c51)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__170257ed4524eaed3cb5cb30da6456093e043b744b8fded968f0df4d252ad796)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetrics]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetrics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetrics],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e6891fea632facc2ec33c3af13e4510aec50c21a70a69184ffd52ba09ed09b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3ControlStorageLensConfigurationStorageLensConfigurationDataExportOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationDataExportOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8d22115a15b2e360ac701afa7c82d42a3fd0c3bed5ab4a4d1d885af3dc670093)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCloudWatchMetrics")
    def put_cloud_watch_metrics(
        self,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#enabled S3ControlStorageLensConfiguration#enabled}.
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetrics(
            enabled=enabled
        )

        return typing.cast(None, jsii.invoke(self, "putCloudWatchMetrics", [value]))

    @jsii.member(jsii_name="putS3BucketDestination")
    def put_s3_bucket_destination(
        self,
        *,
        account_id: builtins.str,
        arn: builtins.str,
        format: builtins.str,
        output_schema_version: builtins.str,
        encryption: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryption", typing.Dict[builtins.str, typing.Any]]] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#account_id S3ControlStorageLensConfiguration#account_id}.
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#arn S3ControlStorageLensConfiguration#arn}.
        :param format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#format S3ControlStorageLensConfiguration#format}.
        :param output_schema_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#output_schema_version S3ControlStorageLensConfiguration#output_schema_version}.
        :param encryption: encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#encryption S3ControlStorageLensConfiguration#encryption}
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#prefix S3ControlStorageLensConfiguration#prefix}.
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestination(
            account_id=account_id,
            arn=arn,
            format=format,
            output_schema_version=output_schema_version,
            encryption=encryption,
            prefix=prefix,
        )

        return typing.cast(None, jsii.invoke(self, "putS3BucketDestination", [value]))

    @jsii.member(jsii_name="resetCloudWatchMetrics")
    def reset_cloud_watch_metrics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudWatchMetrics", []))

    @jsii.member(jsii_name="resetS3BucketDestination")
    def reset_s3_bucket_destination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3BucketDestination", []))

    @builtins.property
    @jsii.member(jsii_name="cloudWatchMetrics")
    def cloud_watch_metrics(
        self,
    ) -> S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetricsOutputReference:
        return typing.cast(S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetricsOutputReference, jsii.get(self, "cloudWatchMetrics"))

    @builtins.property
    @jsii.member(jsii_name="s3BucketDestination")
    def s3_bucket_destination(
        self,
    ) -> "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationOutputReference":
        return typing.cast("S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationOutputReference", jsii.get(self, "s3BucketDestination"))

    @builtins.property
    @jsii.member(jsii_name="cloudWatchMetricsInput")
    def cloud_watch_metrics_input(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetrics]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetrics], jsii.get(self, "cloudWatchMetricsInput"))

    @builtins.property
    @jsii.member(jsii_name="s3BucketDestinationInput")
    def s3_bucket_destination_input(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestination"]:
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestination"], jsii.get(self, "s3BucketDestinationInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExport]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExport], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExport],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af63872f22f09ea3ff0862904c01615714bc5054501908df086b4a409c02af6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestination",
    jsii_struct_bases=[],
    name_mapping={
        "account_id": "accountId",
        "arn": "arn",
        "format": "format",
        "output_schema_version": "outputSchemaVersion",
        "encryption": "encryption",
        "prefix": "prefix",
    },
)
class S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestination:
    def __init__(
        self,
        *,
        account_id: builtins.str,
        arn: builtins.str,
        format: builtins.str,
        output_schema_version: builtins.str,
        encryption: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryption", typing.Dict[builtins.str, typing.Any]]] = None,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#account_id S3ControlStorageLensConfiguration#account_id}.
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#arn S3ControlStorageLensConfiguration#arn}.
        :param format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#format S3ControlStorageLensConfiguration#format}.
        :param output_schema_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#output_schema_version S3ControlStorageLensConfiguration#output_schema_version}.
        :param encryption: encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#encryption S3ControlStorageLensConfiguration#encryption}
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#prefix S3ControlStorageLensConfiguration#prefix}.
        '''
        if isinstance(encryption, dict):
            encryption = S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryption(**encryption)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07a240441a8e35d8426a4b69eea68e06b6c5717e6051c27a6e5f15d0459fb0ca)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            check_type(argname="argument format", value=format, expected_type=type_hints["format"])
            check_type(argname="argument output_schema_version", value=output_schema_version, expected_type=type_hints["output_schema_version"])
            check_type(argname="argument encryption", value=encryption, expected_type=type_hints["encryption"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_id": account_id,
            "arn": arn,
            "format": format,
            "output_schema_version": output_schema_version,
        }
        if encryption is not None:
            self._values["encryption"] = encryption
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def account_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#account_id S3ControlStorageLensConfiguration#account_id}.'''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#arn S3ControlStorageLensConfiguration#arn}.'''
        result = self._values.get("arn")
        assert result is not None, "Required property 'arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def format(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#format S3ControlStorageLensConfiguration#format}.'''
        result = self._values.get("format")
        assert result is not None, "Required property 'format' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def output_schema_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#output_schema_version S3ControlStorageLensConfiguration#output_schema_version}.'''
        result = self._values.get("output_schema_version")
        assert result is not None, "Required property 'output_schema_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def encryption(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryption"]:
        '''encryption block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#encryption S3ControlStorageLensConfiguration#encryption}
        '''
        result = self._values.get("encryption")
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryption"], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#prefix S3ControlStorageLensConfiguration#prefix}.'''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestination(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryption",
    jsii_struct_bases=[],
    name_mapping={"sse_kms": "sseKms", "sse_s3": "sseS3"},
)
class S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryption:
    def __init__(
        self,
        *,
        sse_kms: typing.Optional[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKms", typing.Dict[builtins.str, typing.Any]]] = None,
        sse_s3: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param sse_kms: sse_kms block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#sse_kms S3ControlStorageLensConfiguration#sse_kms}
        :param sse_s3: sse_s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#sse_s3 S3ControlStorageLensConfiguration#sse_s3}
        '''
        if isinstance(sse_kms, dict):
            sse_kms = S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKms(**sse_kms)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a37129d3ef8d831d648d88e100c7b0d2f4d21cc85f8840e6e486af47c0267219)
            check_type(argname="argument sse_kms", value=sse_kms, expected_type=type_hints["sse_kms"])
            check_type(argname="argument sse_s3", value=sse_s3, expected_type=type_hints["sse_s3"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if sse_kms is not None:
            self._values["sse_kms"] = sse_kms
        if sse_s3 is not None:
            self._values["sse_s3"] = sse_s3

    @builtins.property
    def sse_kms(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKms"]:
        '''sse_kms block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#sse_kms S3ControlStorageLensConfiguration#sse_kms}
        '''
        result = self._values.get("sse_kms")
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKms"], result)

    @builtins.property
    def sse_s3(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3"]]]:
        '''sse_s3 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#sse_s3 S3ControlStorageLensConfiguration#sse_s3}
        '''
        result = self._values.get("sse_s3")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__aa27d704e038fda85bb44bd7fc78e50609e48c1cadaf189c274134b3b1510a72)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSseKms")
    def put_sse_kms(self, *, key_id: builtins.str) -> None:
        '''
        :param key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#key_id S3ControlStorageLensConfiguration#key_id}.
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKms(
            key_id=key_id
        )

        return typing.cast(None, jsii.invoke(self, "putSseKms", [value]))

    @jsii.member(jsii_name="putSseS3")
    def put_sse_s3(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a80da24d0b3e5a92d0d34d65f4a917a49b0ed2fbd698f746e195ef592d71c8f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSseS3", [value]))

    @jsii.member(jsii_name="resetSseKms")
    def reset_sse_kms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSseKms", []))

    @jsii.member(jsii_name="resetSseS3")
    def reset_sse_s3(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSseS3", []))

    @builtins.property
    @jsii.member(jsii_name="sseKms")
    def sse_kms(
        self,
    ) -> "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKmsOutputReference":
        return typing.cast("S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKmsOutputReference", jsii.get(self, "sseKms"))

    @builtins.property
    @jsii.member(jsii_name="sseS3")
    def sse_s3(
        self,
    ) -> "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3List":
        return typing.cast("S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3List", jsii.get(self, "sseS3"))

    @builtins.property
    @jsii.member(jsii_name="sseKmsInput")
    def sse_kms_input(
        self,
    ) -> typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKms"]:
        return typing.cast(typing.Optional["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKms"], jsii.get(self, "sseKmsInput"))

    @builtins.property
    @jsii.member(jsii_name="sseS3Input")
    def sse_s3_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3"]]], jsii.get(self, "sseS3Input"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryption]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryption], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryption],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf037b614d22fd0ac0719de9ab3d7073628ebcaee7ee8150077c464590df6b3d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKms",
    jsii_struct_bases=[],
    name_mapping={"key_id": "keyId"},
)
class S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKms:
    def __init__(self, *, key_id: builtins.str) -> None:
        '''
        :param key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#key_id S3ControlStorageLensConfiguration#key_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c343b9a44624eda702881c387f8b03750de0ccb90e6936ff71205145da3f7ef)
            check_type(argname="argument key_id", value=key_id, expected_type=type_hints["key_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key_id": key_id,
        }

    @builtins.property
    def key_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#key_id S3ControlStorageLensConfiguration#key_id}.'''
        result = self._values.get("key_id")
        assert result is not None, "Required property 'key_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKms(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKmsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKmsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__32462092e947a8b76ae662bd1237e9511fd0fb62e302afcf6906e448e19a7382)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="keyIdInput")
    def key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="keyId")
    def key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyId"))

    @key_id.setter
    def key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac66b9e9ad72886bc9d905294e1c2bffd950f73b72e2e41df106caad0c787603)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKms]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKms], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKms],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bf55c24518eaf8a22ecd1a8b962eae0767675c74011fbcfbb4d6a4cb7cfc35b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3",
    jsii_struct_bases=[],
    name_mapping={},
)
class S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3List(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3List",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f85a020b30d01a45725aac7ff1bde5455fbedd85303caf68d2aa0493ba5332f3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3OutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a6df20b768a0f015b2dcbce31ad767d57298a39dc20358b067299867d073fbd)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3OutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f009624abaeebc17770a63f8a2f4e3c5d368638e1c32ea1c43a8e1ec9e0dd1c8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a5a27583f989236053980ed9c7e95be218486d59ecb3e0faf37e44c542f36cd0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fd6d62fab43cc0a32de7ec150a277718d6a22c99d9616d362877ec4f57daf9da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e162b2a849d56ad6c27c6b927b43c9185e98709b85e9a970c04d35e805656fd5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3OutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3OutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ca4186364548b17a7525b7fd24fba7f874c1aeb316d693f235fbeddf85507a4b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2426bd9f28c955617950c86cfeb7a4dcb6fa70d0abf5e7e32d997e7be7ba0b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__008b0757e29375e5d494dafa9696e8dd39b41ef14249d9442bff01efe4afa5e8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putEncryption")
    def put_encryption(
        self,
        *,
        sse_kms: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKms, typing.Dict[builtins.str, typing.Any]]] = None,
        sse_s3: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param sse_kms: sse_kms block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#sse_kms S3ControlStorageLensConfiguration#sse_kms}
        :param sse_s3: sse_s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#sse_s3 S3ControlStorageLensConfiguration#sse_s3}
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryption(
            sse_kms=sse_kms, sse_s3=sse_s3
        )

        return typing.cast(None, jsii.invoke(self, "putEncryption", [value]))

    @jsii.member(jsii_name="resetEncryption")
    def reset_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryption", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="encryption")
    def encryption(
        self,
    ) -> S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionOutputReference:
        return typing.cast(S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionOutputReference, jsii.get(self, "encryption"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="arnInput")
    def arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "arnInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionInput")
    def encryption_input(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryption]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryption], jsii.get(self, "encryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="formatInput")
    def format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "formatInput"))

    @builtins.property
    @jsii.member(jsii_name="outputSchemaVersionInput")
    def output_schema_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "outputSchemaVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__462f914a987a854928ae2a9738479ffe20374b249ce28b06be4b7cceaf11259b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @arn.setter
    def arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6797475b2da19e12dc023e7fe78b8f398bf939e81a2393911808c687a29e2344)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arn", value)

    @builtins.property
    @jsii.member(jsii_name="format")
    def format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "format"))

    @format.setter
    def format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e97e375f29028f9a23e5150e14dd1434cbc41d9a9600b9ef1c05c0213a35343)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "format", value)

    @builtins.property
    @jsii.member(jsii_name="outputSchemaVersion")
    def output_schema_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outputSchemaVersion"))

    @output_schema_version.setter
    def output_schema_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee2bd50f29c1b31bd9649db1ef7a05ff608d23351d7d612465b7479a8888aa24)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputSchemaVersion", value)

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49572f2790a619d1275ec705513b28ef036c53d2cc6c178dfd703e36a5e8cf6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestination]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestination], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestination],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14c780f7d3be88331d285492202b6862ca6c5a7f5f824d969b5b266758e6524d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationExclude",
    jsii_struct_bases=[],
    name_mapping={"buckets": "buckets", "regions": "regions"},
)
class S3ControlStorageLensConfigurationStorageLensConfigurationExclude:
    def __init__(
        self,
        *,
        buckets: typing.Optional[typing.Sequence[builtins.str]] = None,
        regions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param buckets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#buckets S3ControlStorageLensConfiguration#buckets}.
        :param regions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#regions S3ControlStorageLensConfiguration#regions}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3f2244b81b55646347f6ce219feeb3dc30e474ed212e28cd17002747a03949b)
            check_type(argname="argument buckets", value=buckets, expected_type=type_hints["buckets"])
            check_type(argname="argument regions", value=regions, expected_type=type_hints["regions"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if buckets is not None:
            self._values["buckets"] = buckets
        if regions is not None:
            self._values["regions"] = regions

    @builtins.property
    def buckets(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#buckets S3ControlStorageLensConfiguration#buckets}.'''
        result = self._values.get("buckets")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#regions S3ControlStorageLensConfiguration#regions}.'''
        result = self._values.get("regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationExclude(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3ControlStorageLensConfigurationStorageLensConfigurationExcludeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationExcludeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__037876668784f4b16dc616a1a19f895275532716c820f4605cea2a1d7c6369b5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBuckets")
    def reset_buckets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuckets", []))

    @jsii.member(jsii_name="resetRegions")
    def reset_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegions", []))

    @builtins.property
    @jsii.member(jsii_name="bucketsInput")
    def buckets_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "bucketsInput"))

    @builtins.property
    @jsii.member(jsii_name="regionsInput")
    def regions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "regionsInput"))

    @builtins.property
    @jsii.member(jsii_name="buckets")
    def buckets(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "buckets"))

    @buckets.setter
    def buckets(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49893d2854a76855f852ec9539c475756c7ca9bc61ea1542761c24991e6345b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buckets", value)

    @builtins.property
    @jsii.member(jsii_name="regions")
    def regions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "regions"))

    @regions.setter
    def regions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12a09ea5f45d05c5c4299503f3137f6733d87e3c619614db1ab68348c55614b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regions", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationExclude]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationExclude], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationExclude],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__158e8351339c3f9735604023ee061bdfe3858577c4000aed77b42e3cd2784b4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationInclude",
    jsii_struct_bases=[],
    name_mapping={"buckets": "buckets", "regions": "regions"},
)
class S3ControlStorageLensConfigurationStorageLensConfigurationInclude:
    def __init__(
        self,
        *,
        buckets: typing.Optional[typing.Sequence[builtins.str]] = None,
        regions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param buckets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#buckets S3ControlStorageLensConfiguration#buckets}.
        :param regions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#regions S3ControlStorageLensConfiguration#regions}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c872583a23f696d915251b8d222b30059e058ee9eb02b29262131eb1a0bc07da)
            check_type(argname="argument buckets", value=buckets, expected_type=type_hints["buckets"])
            check_type(argname="argument regions", value=regions, expected_type=type_hints["regions"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if buckets is not None:
            self._values["buckets"] = buckets
        if regions is not None:
            self._values["regions"] = regions

    @builtins.property
    def buckets(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#buckets S3ControlStorageLensConfiguration#buckets}.'''
        result = self._values.get("buckets")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#regions S3ControlStorageLensConfiguration#regions}.'''
        result = self._values.get("regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ControlStorageLensConfigurationStorageLensConfigurationInclude(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class S3ControlStorageLensConfigurationStorageLensConfigurationIncludeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationIncludeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b08f1b0a1f5e0d598b607f63812af91c6b02e4e03e77812be765dc85b1be5437)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBuckets")
    def reset_buckets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuckets", []))

    @jsii.member(jsii_name="resetRegions")
    def reset_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegions", []))

    @builtins.property
    @jsii.member(jsii_name="bucketsInput")
    def buckets_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "bucketsInput"))

    @builtins.property
    @jsii.member(jsii_name="regionsInput")
    def regions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "regionsInput"))

    @builtins.property
    @jsii.member(jsii_name="buckets")
    def buckets(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "buckets"))

    @buckets.setter
    def buckets(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b81b439fc990c520af03a63153ff14bfccc558dbfbbe271684abbe33587136bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buckets", value)

    @builtins.property
    @jsii.member(jsii_name="regions")
    def regions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "regions"))

    @regions.setter
    def regions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47e938284066b41efaa99c5a0a65387921e648d5f3dea1f176b7ee04878e94b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regions", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationInclude]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationInclude], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationInclude],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8032e8aa59b69f4a807d1302e1915d6e7990098b8c5d3ea26e685357a6b5dbe1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class S3ControlStorageLensConfigurationStorageLensConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.s3ControlStorageLensConfiguration.S3ControlStorageLensConfigurationStorageLensConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ffca0e9535d90a0c6afe170ffc5d528a0c714a71f0576f937abf0135a8762d66)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAccountLevel")
    def put_account_level(
        self,
        *,
        bucket_level: typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevel, typing.Dict[builtins.str, typing.Any]],
        activity_metrics: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetrics, typing.Dict[builtins.str, typing.Any]]] = None,
        advanced_cost_optimization_metrics: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedCostOptimizationMetrics, typing.Dict[builtins.str, typing.Any]]] = None,
        advanced_data_protection_metrics: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedDataProtectionMetrics, typing.Dict[builtins.str, typing.Any]]] = None,
        detailed_status_code_metrics: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelDetailedStatusCodeMetrics, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param bucket_level: bucket_level block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#bucket_level S3ControlStorageLensConfiguration#bucket_level}
        :param activity_metrics: activity_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#activity_metrics S3ControlStorageLensConfiguration#activity_metrics}
        :param advanced_cost_optimization_metrics: advanced_cost_optimization_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#advanced_cost_optimization_metrics S3ControlStorageLensConfiguration#advanced_cost_optimization_metrics}
        :param advanced_data_protection_metrics: advanced_data_protection_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#advanced_data_protection_metrics S3ControlStorageLensConfiguration#advanced_data_protection_metrics}
        :param detailed_status_code_metrics: detailed_status_code_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#detailed_status_code_metrics S3ControlStorageLensConfiguration#detailed_status_code_metrics}
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevel(
            bucket_level=bucket_level,
            activity_metrics=activity_metrics,
            advanced_cost_optimization_metrics=advanced_cost_optimization_metrics,
            advanced_data_protection_metrics=advanced_data_protection_metrics,
            detailed_status_code_metrics=detailed_status_code_metrics,
        )

        return typing.cast(None, jsii.invoke(self, "putAccountLevel", [value]))

    @jsii.member(jsii_name="putAwsOrg")
    def put_aws_org(self, *, arn: builtins.str) -> None:
        '''
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#arn S3ControlStorageLensConfiguration#arn}.
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrg(
            arn=arn
        )

        return typing.cast(None, jsii.invoke(self, "putAwsOrg", [value]))

    @jsii.member(jsii_name="putDataExport")
    def put_data_export(
        self,
        *,
        cloud_watch_metrics: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetrics, typing.Dict[builtins.str, typing.Any]]] = None,
        s3_bucket_destination: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestination, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cloud_watch_metrics: cloud_watch_metrics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#cloud_watch_metrics S3ControlStorageLensConfiguration#cloud_watch_metrics}
        :param s3_bucket_destination: s3_bucket_destination block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#s3_bucket_destination S3ControlStorageLensConfiguration#s3_bucket_destination}
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfigurationDataExport(
            cloud_watch_metrics=cloud_watch_metrics,
            s3_bucket_destination=s3_bucket_destination,
        )

        return typing.cast(None, jsii.invoke(self, "putDataExport", [value]))

    @jsii.member(jsii_name="putExclude")
    def put_exclude(
        self,
        *,
        buckets: typing.Optional[typing.Sequence[builtins.str]] = None,
        regions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param buckets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#buckets S3ControlStorageLensConfiguration#buckets}.
        :param regions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#regions S3ControlStorageLensConfiguration#regions}.
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfigurationExclude(
            buckets=buckets, regions=regions
        )

        return typing.cast(None, jsii.invoke(self, "putExclude", [value]))

    @jsii.member(jsii_name="putInclude")
    def put_include(
        self,
        *,
        buckets: typing.Optional[typing.Sequence[builtins.str]] = None,
        regions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param buckets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#buckets S3ControlStorageLensConfiguration#buckets}.
        :param regions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/s3control_storage_lens_configuration#regions S3ControlStorageLensConfiguration#regions}.
        '''
        value = S3ControlStorageLensConfigurationStorageLensConfigurationInclude(
            buckets=buckets, regions=regions
        )

        return typing.cast(None, jsii.invoke(self, "putInclude", [value]))

    @jsii.member(jsii_name="resetAwsOrg")
    def reset_aws_org(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsOrg", []))

    @jsii.member(jsii_name="resetDataExport")
    def reset_data_export(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataExport", []))

    @jsii.member(jsii_name="resetExclude")
    def reset_exclude(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExclude", []))

    @jsii.member(jsii_name="resetInclude")
    def reset_include(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInclude", []))

    @builtins.property
    @jsii.member(jsii_name="accountLevel")
    def account_level(
        self,
    ) -> S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelOutputReference:
        return typing.cast(S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelOutputReference, jsii.get(self, "accountLevel"))

    @builtins.property
    @jsii.member(jsii_name="awsOrg")
    def aws_org(
        self,
    ) -> S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrgOutputReference:
        return typing.cast(S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrgOutputReference, jsii.get(self, "awsOrg"))

    @builtins.property
    @jsii.member(jsii_name="dataExport")
    def data_export(
        self,
    ) -> S3ControlStorageLensConfigurationStorageLensConfigurationDataExportOutputReference:
        return typing.cast(S3ControlStorageLensConfigurationStorageLensConfigurationDataExportOutputReference, jsii.get(self, "dataExport"))

    @builtins.property
    @jsii.member(jsii_name="exclude")
    def exclude(
        self,
    ) -> S3ControlStorageLensConfigurationStorageLensConfigurationExcludeOutputReference:
        return typing.cast(S3ControlStorageLensConfigurationStorageLensConfigurationExcludeOutputReference, jsii.get(self, "exclude"))

    @builtins.property
    @jsii.member(jsii_name="include")
    def include(
        self,
    ) -> S3ControlStorageLensConfigurationStorageLensConfigurationIncludeOutputReference:
        return typing.cast(S3ControlStorageLensConfigurationStorageLensConfigurationIncludeOutputReference, jsii.get(self, "include"))

    @builtins.property
    @jsii.member(jsii_name="accountLevelInput")
    def account_level_input(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevel]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevel], jsii.get(self, "accountLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="awsOrgInput")
    def aws_org_input(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrg]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrg], jsii.get(self, "awsOrgInput"))

    @builtins.property
    @jsii.member(jsii_name="dataExportInput")
    def data_export_input(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExport]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExport], jsii.get(self, "dataExportInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="excludeInput")
    def exclude_input(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationExclude]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationExclude], jsii.get(self, "excludeInput"))

    @builtins.property
    @jsii.member(jsii_name="includeInput")
    def include_input(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationInclude]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationInclude], jsii.get(self, "includeInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__a5dffacc52d8ee5dd4ee48658721d3a1916596c706d43c4fe73c470a098b2a94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[S3ControlStorageLensConfigurationStorageLensConfiguration]:
        return typing.cast(typing.Optional[S3ControlStorageLensConfigurationStorageLensConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__529f7ab92eaf06345b88ce8f3608bd803d55b92d25fe97ff405782758e9ee65e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "S3ControlStorageLensConfiguration",
    "S3ControlStorageLensConfigurationConfig",
    "S3ControlStorageLensConfigurationStorageLensConfiguration",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevel",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetrics",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetricsOutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedCostOptimizationMetrics",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedCostOptimizationMetricsOutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedDataProtectionMetrics",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedDataProtectionMetricsOutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevel",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetrics",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetricsOutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedCostOptimizationMetrics",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedCostOptimizationMetricsOutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedDataProtectionMetrics",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedDataProtectionMetricsOutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelDetailedStatusCodeMetrics",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelDetailedStatusCodeMetricsOutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelOutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevel",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelOutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetrics",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsOutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteria",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteriaOutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelDetailedStatusCodeMetrics",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelDetailedStatusCodeMetricsOutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelOutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrg",
    "S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrgOutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationDataExport",
    "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetrics",
    "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetricsOutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportOutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestination",
    "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryption",
    "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionOutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKms",
    "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKmsOutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3",
    "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3List",
    "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3OutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationOutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationExclude",
    "S3ControlStorageLensConfigurationStorageLensConfigurationExcludeOutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationInclude",
    "S3ControlStorageLensConfigurationStorageLensConfigurationIncludeOutputReference",
    "S3ControlStorageLensConfigurationStorageLensConfigurationOutputReference",
]

publication.publish()

def _typecheckingstub__9e77f92f627da133b3a6df8b540fd9175d429856efe199f56f2c0896456bc84b(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    config_id: builtins.str,
    storage_lens_configuration: typing.Union[S3ControlStorageLensConfigurationStorageLensConfiguration, typing.Dict[builtins.str, typing.Any]],
    account_id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__0cd569fe4c52a13ce41357d11b5392eb3f3e066238804673fb321bb13a819e9a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a73c9a316b83fe31eadd5a17e1f52749d079863605a6f45e25facf99af5df747(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcb566e24bf94f515af9331810f90f38debcfacd8175e2d57011ee31a1bda4dc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55239a3f35f96c6cedd4495a0cdbd1f2c3c5c8e063812eec88b79a614f4357d7(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96432fb78c643dd5a48080216b0262963900cc477c3883040a03715e051f3b08(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d177c3dc8f5225d2ed765b7e528fa1e8cf31f2d4094eefa7c04577e80007bfa1(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    config_id: builtins.str,
    storage_lens_configuration: typing.Union[S3ControlStorageLensConfigurationStorageLensConfiguration, typing.Dict[builtins.str, typing.Any]],
    account_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cc734b6d0ad45d0e4e8311790fbfcf7d2cbf20abbf6395bb5e5bf3b1b8f916c(
    *,
    account_level: typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevel, typing.Dict[builtins.str, typing.Any]],
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    aws_org: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrg, typing.Dict[builtins.str, typing.Any]]] = None,
    data_export: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationDataExport, typing.Dict[builtins.str, typing.Any]]] = None,
    exclude: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationExclude, typing.Dict[builtins.str, typing.Any]]] = None,
    include: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationInclude, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ce225400785f6db0ac4425d907720f6aa408ef91298e40fa4d3b444a1c39d2c(
    *,
    bucket_level: typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevel, typing.Dict[builtins.str, typing.Any]],
    activity_metrics: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetrics, typing.Dict[builtins.str, typing.Any]]] = None,
    advanced_cost_optimization_metrics: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedCostOptimizationMetrics, typing.Dict[builtins.str, typing.Any]]] = None,
    advanced_data_protection_metrics: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedDataProtectionMetrics, typing.Dict[builtins.str, typing.Any]]] = None,
    detailed_status_code_metrics: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelDetailedStatusCodeMetrics, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__627ed5ab0d976060a479a45c547e9c234d3d275c578744b026356594d62d141e(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecebdf5489ffd2e02b8baf142fd7140a72001ce29d4d674589335eecc9af68bc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__045c2c3f57cc08d85109723eb0753f83e9e16eb890bf2ee3a52b3a4c402f19de(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__191c7c914d6f953502d706888c58b4c7c2f1230073c359195e7b2f9198b2d187(
    value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelActivityMetrics],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6a56eb96a6f9cc9ad77c1832ec85310b691b2e9b7386a9a034d3c7a8b15783b(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62129a26fdc1ba16ce13aece57854dbabb974a1b749082c860a0196b8a1e53c6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__001fa0876b67f70aa388df6233b5453d391b4a6412670b9e9514d766e9ee9cb8(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4faf3071c380c66f335badce049d6416e1a4061c15f447278b64d6b52f0113b(
    value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedCostOptimizationMetrics],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bd535e67fef98951382fb05d094c055b0b6d094a830065754df3ee81ef22046(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae40ef6ff0b517e89c5d0b8e6c20d8f534b8c891aad348d4f8eaf7a2b55b4212(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3114a615b5dfa2c282bcd742586eec685d561edba3b102def8c24690097f9858(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__043e3b8a9407d87153ecddb450d441a373cab3f51c582458a6051698e1921538(
    value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelAdvancedDataProtectionMetrics],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e06c3eb2ba021a3730626f8fab7dcfdff4e2ad2a7e683117c23e9726678ca375(
    *,
    activity_metrics: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetrics, typing.Dict[builtins.str, typing.Any]]] = None,
    advanced_cost_optimization_metrics: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedCostOptimizationMetrics, typing.Dict[builtins.str, typing.Any]]] = None,
    advanced_data_protection_metrics: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedDataProtectionMetrics, typing.Dict[builtins.str, typing.Any]]] = None,
    detailed_status_code_metrics: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelDetailedStatusCodeMetrics, typing.Dict[builtins.str, typing.Any]]] = None,
    prefix_level: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevel, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95e878e46f47ade57f5c2fed337208673c85e897e50850ab37fa3c29e5ba7149(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ddcc7623c85e553b71cbf161d354e0492a3df915714a4c204300cadb01dc031(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c536af6d9d65fb49c62fa34be9858ac160ee9fb87b24dadfa79a327af242df03(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03d78a72e54335ae035db2494a65a361b47878289f48596c2279ac863b687a41(
    value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelActivityMetrics],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d51cf86df5022461531478fe796677e52d50a0fd412c7945070829ebf192a863(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__572c2f8175ae05f49f9606c22dd5510772d8df44ff631da72cbb2c4a0fd04dd3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74b6a2fd0eb1dfd8651b02e4e785a5096d10d3558194a7e66be38d43c357d8a8(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de73ad38307037828043b85063cb2ee9cde1c433917c30053d678eddb8db67df(
    value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedCostOptimizationMetrics],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8aed887175413c39aa67ab7ff474af4be6c5a658efe197a537afda25d0da9bb(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8feed0f06ae78383ab52854fcf3fdc0930e039f29ee79009fe09e9e586cde27(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5f64deac6d68fd202532720fff163204c8d770f9a2b0eb9bba35bc94d3b8ef0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7e172fcc91d13dae4fb0de23f09e6eb5641fc384c09742a3511ae076d645a73(
    value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelAdvancedDataProtectionMetrics],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a68402f5890b61dc0270ad9116b4df22d153e8742c661cd2f4db80c31a22990e(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b3a890d9222b3aebeed85436bac81cac3b044b8ddc3496e480f55a0bf8a3e90(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0b5c2cbcd034a705d228aa35cc21d0811862f8d84559f319e1171c450ea4083(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7b63bc3414312454f5fccc9f3d82fc6ad91f69b3ab0da9488b8e9ae20a1404f(
    value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelDetailedStatusCodeMetrics],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1a24041c5074fa93b04a9a7573e3b0f540e444705b2c1b34b1ae0506c095720(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c04d8266aca5ae3d38b5fa990a46450ee33430ce7cf6cc4f5b28d9bfcd12b580(
    value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevel],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5b6d0b23cf1f6b7deba0a81d66ee3c43b225e3058059e91aa56cb16be3830f2(
    *,
    storage_metrics: typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetrics, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a3bb9c03371c544ea09cc5c07337531b0ff8ea0d0e5f9c7393666e05d4a5edf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__886a5c7f073b505de5aaed6397f30599619722332e2cf45dbe44c3ab2d4cfa0e(
    value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevel],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45dd58ae48794fcf01f2766d1e03da3e3e7d1c4d20ba130d967b2c58f29a69ba(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    selection_criteria: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteria, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9defecefef2e84942707249deb6bb974374890c094e6caa29666871b528dc6c0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c111d4f3ef0c5c1b8c29d1771e6c285896007aab003080e610965f578c8d1047(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89659894ab3c74b6b651d1dcd1e28f1737ab3177f56a1823214a35a94333b56b(
    value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetrics],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14effa2b187edab5a346072a3b1ed032e70a993a501d7dfd4a86c1cc62f32f0f(
    *,
    delimiter: typing.Optional[builtins.str] = None,
    max_depth: typing.Optional[jsii.Number] = None,
    min_storage_bytes_percentage: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a3932978ec511b407cd4b12382c0063574bdcc719c3a0934dd81a19a6ab6c91(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95f39c9849b2af9ca55af55624e79ac02debaf01f246bb514975ff7e6d4a09e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b0404db0b36527bb412b5c673da1138a3335a0e16bfd9c252af7ebae12eb967(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b768be731261ce50f54e46690ee16181ba681608e74101c5bb68246c02c4e28(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e35d9c9f438b920a898637804fec920ff8272caf9822e8cede81a3628707cac(
    value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelBucketLevelPrefixLevelStorageMetricsSelectionCriteria],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__496e84851ee18b70f7586442593455225c3badbbe2abaf0dd00a413e345d4bc0(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3d26c303c2f5e94a5a313154bab9001e9b24885acd63b6154c19a782c53abbf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6acf6e21a833416f3b7d3f94c380f7e7049778b75643f5bac39e781c0d1f12d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e147f0a4347306195af9f42144b1e1b8208a0f5862cca966a8df8f743b35c631(
    value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevelDetailedStatusCodeMetrics],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4188af18d39db426d82e10f6801a65cc7112eef17d53bd89464462bf9b146af(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68b5924b8c20c02e835676540cad23bc849c698c6948fb703a2e254c1666a044(
    value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAccountLevel],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8deed62ce738341ff5c4150e6f2f4dc6b499b82f0232496f89eb5613fc4d9b96(
    *,
    arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6241f5acd4e06d522a583fb30d61765a631851488a8ae16d3733734111e51bb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__228b49645bf946019926307046ac3efac258de5520690974381f65b2ce1b62ec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c3e1338fc0537dd7a5b0164175027471b5cf00e8d5328fc571d28414a559a90(
    value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationAwsOrg],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__446c5b84c5eda4e0df9be1b0ae58b36e387d16f54f88830ad0660b7c3f07b647(
    *,
    cloud_watch_metrics: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetrics, typing.Dict[builtins.str, typing.Any]]] = None,
    s3_bucket_destination: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestination, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ede7ff0d27622b5cc8bf6bdff987783e08fd4a09e18f92b207d9b3ef1ea22cd8(
    *,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__856f34004f8df6b83e9ef1936412157a0733acf933ae5600cb50b43b18848c51(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__170257ed4524eaed3cb5cb30da6456093e043b744b8fded968f0df4d252ad796(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e6891fea632facc2ec33c3af13e4510aec50c21a70a69184ffd52ba09ed09b1(
    value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportCloudWatchMetrics],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d22115a15b2e360ac701afa7c82d42a3fd0c3bed5ab4a4d1d885af3dc670093(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af63872f22f09ea3ff0862904c01615714bc5054501908df086b4a409c02af6a(
    value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExport],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07a240441a8e35d8426a4b69eea68e06b6c5717e6051c27a6e5f15d0459fb0ca(
    *,
    account_id: builtins.str,
    arn: builtins.str,
    format: builtins.str,
    output_schema_version: builtins.str,
    encryption: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryption, typing.Dict[builtins.str, typing.Any]]] = None,
    prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a37129d3ef8d831d648d88e100c7b0d2f4d21cc85f8840e6e486af47c0267219(
    *,
    sse_kms: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKms, typing.Dict[builtins.str, typing.Any]]] = None,
    sse_s3: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa27d704e038fda85bb44bd7fc78e50609e48c1cadaf189c274134b3b1510a72(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a80da24d0b3e5a92d0d34d65f4a917a49b0ed2fbd698f746e195ef592d71c8f(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf037b614d22fd0ac0719de9ab3d7073628ebcaee7ee8150077c464590df6b3d(
    value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryption],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c343b9a44624eda702881c387f8b03750de0ccb90e6936ff71205145da3f7ef(
    *,
    key_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32462092e947a8b76ae662bd1237e9511fd0fb62e302afcf6906e448e19a7382(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac66b9e9ad72886bc9d905294e1c2bffd950f73b72e2e41df106caad0c787603(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bf55c24518eaf8a22ecd1a8b962eae0767675c74011fbcfbb4d6a4cb7cfc35b(
    value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseKms],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f85a020b30d01a45725aac7ff1bde5455fbedd85303caf68d2aa0493ba5332f3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a6df20b768a0f015b2dcbce31ad767d57298a39dc20358b067299867d073fbd(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f009624abaeebc17770a63f8a2f4e3c5d368638e1c32ea1c43a8e1ec9e0dd1c8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5a27583f989236053980ed9c7e95be218486d59ecb3e0faf37e44c542f36cd0(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd6d62fab43cc0a32de7ec150a277718d6a22c99d9616d362877ec4f57daf9da(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e162b2a849d56ad6c27c6b927b43c9185e98709b85e9a970c04d35e805656fd5(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca4186364548b17a7525b7fd24fba7f874c1aeb316d693f235fbeddf85507a4b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2426bd9f28c955617950c86cfeb7a4dcb6fa70d0abf5e7e32d997e7be7ba0b6(
    value: typing.Optional[typing.Union[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestinationEncryptionSseS3, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__008b0757e29375e5d494dafa9696e8dd39b41ef14249d9442bff01efe4afa5e8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__462f914a987a854928ae2a9738479ffe20374b249ce28b06be4b7cceaf11259b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6797475b2da19e12dc023e7fe78b8f398bf939e81a2393911808c687a29e2344(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e97e375f29028f9a23e5150e14dd1434cbc41d9a9600b9ef1c05c0213a35343(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee2bd50f29c1b31bd9649db1ef7a05ff608d23351d7d612465b7479a8888aa24(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49572f2790a619d1275ec705513b28ef036c53d2cc6c178dfd703e36a5e8cf6c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14c780f7d3be88331d285492202b6862ca6c5a7f5f824d969b5b266758e6524d(
    value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationDataExportS3BucketDestination],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3f2244b81b55646347f6ce219feeb3dc30e474ed212e28cd17002747a03949b(
    *,
    buckets: typing.Optional[typing.Sequence[builtins.str]] = None,
    regions: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__037876668784f4b16dc616a1a19f895275532716c820f4605cea2a1d7c6369b5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49893d2854a76855f852ec9539c475756c7ca9bc61ea1542761c24991e6345b5(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12a09ea5f45d05c5c4299503f3137f6733d87e3c619614db1ab68348c55614b8(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__158e8351339c3f9735604023ee061bdfe3858577c4000aed77b42e3cd2784b4e(
    value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationExclude],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c872583a23f696d915251b8d222b30059e058ee9eb02b29262131eb1a0bc07da(
    *,
    buckets: typing.Optional[typing.Sequence[builtins.str]] = None,
    regions: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b08f1b0a1f5e0d598b607f63812af91c6b02e4e03e77812be765dc85b1be5437(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b81b439fc990c520af03a63153ff14bfccc558dbfbbe271684abbe33587136bd(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47e938284066b41efaa99c5a0a65387921e648d5f3dea1f176b7ee04878e94b8(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8032e8aa59b69f4a807d1302e1915d6e7990098b8c5d3ea26e685357a6b5dbe1(
    value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfigurationInclude],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffca0e9535d90a0c6afe170ffc5d528a0c714a71f0576f937abf0135a8762d66(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5dffacc52d8ee5dd4ee48658721d3a1916596c706d43c4fe73c470a098b2a94(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__529f7ab92eaf06345b88ce8f3608bd803d55b92d25fe97ff405782758e9ee65e(
    value: typing.Optional[S3ControlStorageLensConfigurationStorageLensConfiguration],
) -> None:
    """Type checking stubs"""
    pass
