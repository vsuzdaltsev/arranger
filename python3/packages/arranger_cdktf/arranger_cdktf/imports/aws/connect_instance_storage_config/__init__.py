'''
# `aws_connect_instance_storage_config`

Refer to the Terraform Registory for docs: [`aws_connect_instance_storage_config`](https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config).
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


class ConnectInstanceStorageConfig(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.connectInstanceStorageConfig.ConnectInstanceStorageConfig",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config aws_connect_instance_storage_config}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        instance_id: builtins.str,
        resource_type: builtins.str,
        storage_config: typing.Union["ConnectInstanceStorageConfigStorageConfig", typing.Dict[builtins.str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config aws_connect_instance_storage_config} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#instance_id ConnectInstanceStorageConfig#instance_id}.
        :param resource_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#resource_type ConnectInstanceStorageConfig#resource_type}.
        :param storage_config: storage_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#storage_config ConnectInstanceStorageConfig#storage_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#id ConnectInstanceStorageConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c488ef541476149c3114b9fb908c6e418e8b239efaa925452c50dca727a48b82)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ConnectInstanceStorageConfigConfig(
            instance_id=instance_id,
            resource_type=resource_type,
            storage_config=storage_config,
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

    @jsii.member(jsii_name="putStorageConfig")
    def put_storage_config(
        self,
        *,
        storage_type: builtins.str,
        kinesis_firehose_config: typing.Optional[typing.Union["ConnectInstanceStorageConfigStorageConfigKinesisFirehoseConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        kinesis_stream_config: typing.Optional[typing.Union["ConnectInstanceStorageConfigStorageConfigKinesisStreamConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        kinesis_video_stream_config: typing.Optional[typing.Union["ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        s3_config: typing.Optional[typing.Union["ConnectInstanceStorageConfigStorageConfigS3Config", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param storage_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#storage_type ConnectInstanceStorageConfig#storage_type}.
        :param kinesis_firehose_config: kinesis_firehose_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#kinesis_firehose_config ConnectInstanceStorageConfig#kinesis_firehose_config}
        :param kinesis_stream_config: kinesis_stream_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#kinesis_stream_config ConnectInstanceStorageConfig#kinesis_stream_config}
        :param kinesis_video_stream_config: kinesis_video_stream_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#kinesis_video_stream_config ConnectInstanceStorageConfig#kinesis_video_stream_config}
        :param s3_config: s3_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#s3_config ConnectInstanceStorageConfig#s3_config}
        '''
        value = ConnectInstanceStorageConfigStorageConfig(
            storage_type=storage_type,
            kinesis_firehose_config=kinesis_firehose_config,
            kinesis_stream_config=kinesis_stream_config,
            kinesis_video_stream_config=kinesis_video_stream_config,
            s3_config=s3_config,
        )

        return typing.cast(None, jsii.invoke(self, "putStorageConfig", [value]))

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
    @jsii.member(jsii_name="associationId")
    def association_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "associationId"))

    @builtins.property
    @jsii.member(jsii_name="storageConfig")
    def storage_config(
        self,
    ) -> "ConnectInstanceStorageConfigStorageConfigOutputReference":
        return typing.cast("ConnectInstanceStorageConfigStorageConfigOutputReference", jsii.get(self, "storageConfig"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceIdInput")
    def instance_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceTypeInput")
    def resource_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="storageConfigInput")
    def storage_config_input(
        self,
    ) -> typing.Optional["ConnectInstanceStorageConfigStorageConfig"]:
        return typing.cast(typing.Optional["ConnectInstanceStorageConfigStorageConfig"], jsii.get(self, "storageConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e839ef4cd5e344ca1120579895e9190351df8ba5a0e0865ae97db4d952f2d598)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @instance_id.setter
    def instance_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7c984e5b177987af7c42cf34fd92dbcf0fbfcbd7eef0259fbe490038dea9578)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceId", value)

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @resource_type.setter
    def resource_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__851fbd5da866bf040dca1f11bc253fadf78237fffcdde902b5f2fb675762ef19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceType", value)


@jsii.data_type(
    jsii_type="aws.connectInstanceStorageConfig.ConnectInstanceStorageConfigConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "instance_id": "instanceId",
        "resource_type": "resourceType",
        "storage_config": "storageConfig",
        "id": "id",
    },
)
class ConnectInstanceStorageConfigConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        instance_id: builtins.str,
        resource_type: builtins.str,
        storage_config: typing.Union["ConnectInstanceStorageConfigStorageConfig", typing.Dict[builtins.str, typing.Any]],
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
        :param instance_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#instance_id ConnectInstanceStorageConfig#instance_id}.
        :param resource_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#resource_type ConnectInstanceStorageConfig#resource_type}.
        :param storage_config: storage_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#storage_config ConnectInstanceStorageConfig#storage_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#id ConnectInstanceStorageConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(storage_config, dict):
            storage_config = ConnectInstanceStorageConfigStorageConfig(**storage_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08a3e46457f81329c421abf1c910d955f323cd98f08a058cbcdee1d4281102b0)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument instance_id", value=instance_id, expected_type=type_hints["instance_id"])
            check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
            check_type(argname="argument storage_config", value=storage_config, expected_type=type_hints["storage_config"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_id": instance_id,
            "resource_type": resource_type,
            "storage_config": storage_config,
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
    def instance_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#instance_id ConnectInstanceStorageConfig#instance_id}.'''
        result = self._values.get("instance_id")
        assert result is not None, "Required property 'instance_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#resource_type ConnectInstanceStorageConfig#resource_type}.'''
        result = self._values.get("resource_type")
        assert result is not None, "Required property 'resource_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_config(self) -> "ConnectInstanceStorageConfigStorageConfig":
        '''storage_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#storage_config ConnectInstanceStorageConfig#storage_config}
        '''
        result = self._values.get("storage_config")
        assert result is not None, "Required property 'storage_config' is missing"
        return typing.cast("ConnectInstanceStorageConfigStorageConfig", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#id ConnectInstanceStorageConfig#id}.

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
        return "ConnectInstanceStorageConfigConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.connectInstanceStorageConfig.ConnectInstanceStorageConfigStorageConfig",
    jsii_struct_bases=[],
    name_mapping={
        "storage_type": "storageType",
        "kinesis_firehose_config": "kinesisFirehoseConfig",
        "kinesis_stream_config": "kinesisStreamConfig",
        "kinesis_video_stream_config": "kinesisVideoStreamConfig",
        "s3_config": "s3Config",
    },
)
class ConnectInstanceStorageConfigStorageConfig:
    def __init__(
        self,
        *,
        storage_type: builtins.str,
        kinesis_firehose_config: typing.Optional[typing.Union["ConnectInstanceStorageConfigStorageConfigKinesisFirehoseConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        kinesis_stream_config: typing.Optional[typing.Union["ConnectInstanceStorageConfigStorageConfigKinesisStreamConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        kinesis_video_stream_config: typing.Optional[typing.Union["ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        s3_config: typing.Optional[typing.Union["ConnectInstanceStorageConfigStorageConfigS3Config", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param storage_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#storage_type ConnectInstanceStorageConfig#storage_type}.
        :param kinesis_firehose_config: kinesis_firehose_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#kinesis_firehose_config ConnectInstanceStorageConfig#kinesis_firehose_config}
        :param kinesis_stream_config: kinesis_stream_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#kinesis_stream_config ConnectInstanceStorageConfig#kinesis_stream_config}
        :param kinesis_video_stream_config: kinesis_video_stream_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#kinesis_video_stream_config ConnectInstanceStorageConfig#kinesis_video_stream_config}
        :param s3_config: s3_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#s3_config ConnectInstanceStorageConfig#s3_config}
        '''
        if isinstance(kinesis_firehose_config, dict):
            kinesis_firehose_config = ConnectInstanceStorageConfigStorageConfigKinesisFirehoseConfig(**kinesis_firehose_config)
        if isinstance(kinesis_stream_config, dict):
            kinesis_stream_config = ConnectInstanceStorageConfigStorageConfigKinesisStreamConfig(**kinesis_stream_config)
        if isinstance(kinesis_video_stream_config, dict):
            kinesis_video_stream_config = ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfig(**kinesis_video_stream_config)
        if isinstance(s3_config, dict):
            s3_config = ConnectInstanceStorageConfigStorageConfigS3Config(**s3_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d0fb9d3eff7e7a4c59333cd240473476548acc07e06c0b8612ac2909f9841da)
            check_type(argname="argument storage_type", value=storage_type, expected_type=type_hints["storage_type"])
            check_type(argname="argument kinesis_firehose_config", value=kinesis_firehose_config, expected_type=type_hints["kinesis_firehose_config"])
            check_type(argname="argument kinesis_stream_config", value=kinesis_stream_config, expected_type=type_hints["kinesis_stream_config"])
            check_type(argname="argument kinesis_video_stream_config", value=kinesis_video_stream_config, expected_type=type_hints["kinesis_video_stream_config"])
            check_type(argname="argument s3_config", value=s3_config, expected_type=type_hints["s3_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "storage_type": storage_type,
        }
        if kinesis_firehose_config is not None:
            self._values["kinesis_firehose_config"] = kinesis_firehose_config
        if kinesis_stream_config is not None:
            self._values["kinesis_stream_config"] = kinesis_stream_config
        if kinesis_video_stream_config is not None:
            self._values["kinesis_video_stream_config"] = kinesis_video_stream_config
        if s3_config is not None:
            self._values["s3_config"] = s3_config

    @builtins.property
    def storage_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#storage_type ConnectInstanceStorageConfig#storage_type}.'''
        result = self._values.get("storage_type")
        assert result is not None, "Required property 'storage_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kinesis_firehose_config(
        self,
    ) -> typing.Optional["ConnectInstanceStorageConfigStorageConfigKinesisFirehoseConfig"]:
        '''kinesis_firehose_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#kinesis_firehose_config ConnectInstanceStorageConfig#kinesis_firehose_config}
        '''
        result = self._values.get("kinesis_firehose_config")
        return typing.cast(typing.Optional["ConnectInstanceStorageConfigStorageConfigKinesisFirehoseConfig"], result)

    @builtins.property
    def kinesis_stream_config(
        self,
    ) -> typing.Optional["ConnectInstanceStorageConfigStorageConfigKinesisStreamConfig"]:
        '''kinesis_stream_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#kinesis_stream_config ConnectInstanceStorageConfig#kinesis_stream_config}
        '''
        result = self._values.get("kinesis_stream_config")
        return typing.cast(typing.Optional["ConnectInstanceStorageConfigStorageConfigKinesisStreamConfig"], result)

    @builtins.property
    def kinesis_video_stream_config(
        self,
    ) -> typing.Optional["ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfig"]:
        '''kinesis_video_stream_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#kinesis_video_stream_config ConnectInstanceStorageConfig#kinesis_video_stream_config}
        '''
        result = self._values.get("kinesis_video_stream_config")
        return typing.cast(typing.Optional["ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfig"], result)

    @builtins.property
    def s3_config(
        self,
    ) -> typing.Optional["ConnectInstanceStorageConfigStorageConfigS3Config"]:
        '''s3_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#s3_config ConnectInstanceStorageConfig#s3_config}
        '''
        result = self._values.get("s3_config")
        return typing.cast(typing.Optional["ConnectInstanceStorageConfigStorageConfigS3Config"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectInstanceStorageConfigStorageConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.connectInstanceStorageConfig.ConnectInstanceStorageConfigStorageConfigKinesisFirehoseConfig",
    jsii_struct_bases=[],
    name_mapping={"firehose_arn": "firehoseArn"},
)
class ConnectInstanceStorageConfigStorageConfigKinesisFirehoseConfig:
    def __init__(self, *, firehose_arn: builtins.str) -> None:
        '''
        :param firehose_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#firehose_arn ConnectInstanceStorageConfig#firehose_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1ae85325092adb13da697d49c9df1d147653c3826044ac01d33adec95dee49e)
            check_type(argname="argument firehose_arn", value=firehose_arn, expected_type=type_hints["firehose_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "firehose_arn": firehose_arn,
        }

    @builtins.property
    def firehose_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#firehose_arn ConnectInstanceStorageConfig#firehose_arn}.'''
        result = self._values.get("firehose_arn")
        assert result is not None, "Required property 'firehose_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectInstanceStorageConfigStorageConfigKinesisFirehoseConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConnectInstanceStorageConfigStorageConfigKinesisFirehoseConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.connectInstanceStorageConfig.ConnectInstanceStorageConfigStorageConfigKinesisFirehoseConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6573b67baa96f5a39d32da5a00e75764e88ee9393360e51fd68131ac32635af9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="firehoseArnInput")
    def firehose_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "firehoseArnInput"))

    @builtins.property
    @jsii.member(jsii_name="firehoseArn")
    def firehose_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firehoseArn"))

    @firehose_arn.setter
    def firehose_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7b30ff263420da88d5d5d53fe02b78ea32da1470e6b108a90b49f04c150771c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firehoseArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ConnectInstanceStorageConfigStorageConfigKinesisFirehoseConfig]:
        return typing.cast(typing.Optional[ConnectInstanceStorageConfigStorageConfigKinesisFirehoseConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ConnectInstanceStorageConfigStorageConfigKinesisFirehoseConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3078c3eb6a9bab6898861ff17964cf383e3e97a49a4cd88b540dd1d2281633e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.connectInstanceStorageConfig.ConnectInstanceStorageConfigStorageConfigKinesisStreamConfig",
    jsii_struct_bases=[],
    name_mapping={"stream_arn": "streamArn"},
)
class ConnectInstanceStorageConfigStorageConfigKinesisStreamConfig:
    def __init__(self, *, stream_arn: builtins.str) -> None:
        '''
        :param stream_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#stream_arn ConnectInstanceStorageConfig#stream_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1567ae99285c681d2536f7e52f5259c8c2c44dbb162a51770cb5f3d415ab07e)
            check_type(argname="argument stream_arn", value=stream_arn, expected_type=type_hints["stream_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "stream_arn": stream_arn,
        }

    @builtins.property
    def stream_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#stream_arn ConnectInstanceStorageConfig#stream_arn}.'''
        result = self._values.get("stream_arn")
        assert result is not None, "Required property 'stream_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectInstanceStorageConfigStorageConfigKinesisStreamConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConnectInstanceStorageConfigStorageConfigKinesisStreamConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.connectInstanceStorageConfig.ConnectInstanceStorageConfigStorageConfigKinesisStreamConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__966dad94644cd86bc1bcb51e126fddc1b21b59029109d58492fd3790370b7b09)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="streamArnInput")
    def stream_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streamArnInput"))

    @builtins.property
    @jsii.member(jsii_name="streamArn")
    def stream_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "streamArn"))

    @stream_arn.setter
    def stream_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05666b62985b313397c29b92f4898275cc9ceb481500861dde28d6bd208f241e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ConnectInstanceStorageConfigStorageConfigKinesisStreamConfig]:
        return typing.cast(typing.Optional[ConnectInstanceStorageConfigStorageConfigKinesisStreamConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ConnectInstanceStorageConfigStorageConfigKinesisStreamConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59bfc52f1469f4473b286d06541d1f3fd2792c73fbf2295a90650c5471a9a42d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.connectInstanceStorageConfig.ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfig",
    jsii_struct_bases=[],
    name_mapping={
        "encryption_config": "encryptionConfig",
        "prefix": "prefix",
        "retention_period_hours": "retentionPeriodHours",
    },
)
class ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfig:
    def __init__(
        self,
        *,
        encryption_config: typing.Union["ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfigEncryptionConfig", typing.Dict[builtins.str, typing.Any]],
        prefix: builtins.str,
        retention_period_hours: jsii.Number,
    ) -> None:
        '''
        :param encryption_config: encryption_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#encryption_config ConnectInstanceStorageConfig#encryption_config}
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#prefix ConnectInstanceStorageConfig#prefix}.
        :param retention_period_hours: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#retention_period_hours ConnectInstanceStorageConfig#retention_period_hours}.
        '''
        if isinstance(encryption_config, dict):
            encryption_config = ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfigEncryptionConfig(**encryption_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95b11f145ee0db3496515eacc96d4d4ea8f9fbb27d9e4ebfd3776d87e425e3f3)
            check_type(argname="argument encryption_config", value=encryption_config, expected_type=type_hints["encryption_config"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument retention_period_hours", value=retention_period_hours, expected_type=type_hints["retention_period_hours"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "encryption_config": encryption_config,
            "prefix": prefix,
            "retention_period_hours": retention_period_hours,
        }

    @builtins.property
    def encryption_config(
        self,
    ) -> "ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfigEncryptionConfig":
        '''encryption_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#encryption_config ConnectInstanceStorageConfig#encryption_config}
        '''
        result = self._values.get("encryption_config")
        assert result is not None, "Required property 'encryption_config' is missing"
        return typing.cast("ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfigEncryptionConfig", result)

    @builtins.property
    def prefix(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#prefix ConnectInstanceStorageConfig#prefix}.'''
        result = self._values.get("prefix")
        assert result is not None, "Required property 'prefix' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def retention_period_hours(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#retention_period_hours ConnectInstanceStorageConfig#retention_period_hours}.'''
        result = self._values.get("retention_period_hours")
        assert result is not None, "Required property 'retention_period_hours' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.connectInstanceStorageConfig.ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfigEncryptionConfig",
    jsii_struct_bases=[],
    name_mapping={"encryption_type": "encryptionType", "key_id": "keyId"},
)
class ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfigEncryptionConfig:
    def __init__(self, *, encryption_type: builtins.str, key_id: builtins.str) -> None:
        '''
        :param encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#encryption_type ConnectInstanceStorageConfig#encryption_type}.
        :param key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#key_id ConnectInstanceStorageConfig#key_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26714f0efb4f38ca206d739c8911210b4a9efc4e5d34181f67bf261cab9b79da)
            check_type(argname="argument encryption_type", value=encryption_type, expected_type=type_hints["encryption_type"])
            check_type(argname="argument key_id", value=key_id, expected_type=type_hints["key_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "encryption_type": encryption_type,
            "key_id": key_id,
        }

    @builtins.property
    def encryption_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#encryption_type ConnectInstanceStorageConfig#encryption_type}.'''
        result = self._values.get("encryption_type")
        assert result is not None, "Required property 'encryption_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#key_id ConnectInstanceStorageConfig#key_id}.'''
        result = self._values.get("key_id")
        assert result is not None, "Required property 'key_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfigEncryptionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfigEncryptionConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.connectInstanceStorageConfig.ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfigEncryptionConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__eec2c03ed525f6e7e8f2b6275b804e0a577046d82fb534887f040c0a87920a09)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="encryptionTypeInput")
    def encryption_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="keyIdInput")
    def key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionType")
    def encryption_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptionType"))

    @encryption_type.setter
    def encryption_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c964117a984326044f07eb5f3de0f170398c3f832de21383eec36e2657fca182)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionType", value)

    @builtins.property
    @jsii.member(jsii_name="keyId")
    def key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyId"))

    @key_id.setter
    def key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40a63016639b9d820a82a5c5cc4810de8e043cb81dbf9117f95c2b3cc12d6d59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfigEncryptionConfig]:
        return typing.cast(typing.Optional[ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfigEncryptionConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfigEncryptionConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6ec44b2041d9d23415be84d966299e4c3dc9b774dbe92dda51b4610212f4745)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.connectInstanceStorageConfig.ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c16ace3b4c42bb7117ea304cab93bbe4490655c54bb8c687292c16d58005310f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putEncryptionConfig")
    def put_encryption_config(
        self,
        *,
        encryption_type: builtins.str,
        key_id: builtins.str,
    ) -> None:
        '''
        :param encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#encryption_type ConnectInstanceStorageConfig#encryption_type}.
        :param key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#key_id ConnectInstanceStorageConfig#key_id}.
        '''
        value = ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfigEncryptionConfig(
            encryption_type=encryption_type, key_id=key_id
        )

        return typing.cast(None, jsii.invoke(self, "putEncryptionConfig", [value]))

    @builtins.property
    @jsii.member(jsii_name="encryptionConfig")
    def encryption_config(
        self,
    ) -> ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfigEncryptionConfigOutputReference:
        return typing.cast(ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfigEncryptionConfigOutputReference, jsii.get(self, "encryptionConfig"))

    @builtins.property
    @jsii.member(jsii_name="encryptionConfigInput")
    def encryption_config_input(
        self,
    ) -> typing.Optional[ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfigEncryptionConfig]:
        return typing.cast(typing.Optional[ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfigEncryptionConfig], jsii.get(self, "encryptionConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionPeriodHoursInput")
    def retention_period_hours_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionPeriodHoursInput"))

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f15d64bb0e87dae8f22467623b10adc68837114386435e040a0b0e1eaed16327)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="retentionPeriodHours")
    def retention_period_hours(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionPeriodHours"))

    @retention_period_hours.setter
    def retention_period_hours(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c3e4f90252fe502db510fe832b998bc1685467e62e0c912698d6bf592bbc782)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionPeriodHours", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfig]:
        return typing.cast(typing.Optional[ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3932aa782a10a5b9f0a45fa8fe78450b29ef12bfbcdf62f83f8ed992226afd4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ConnectInstanceStorageConfigStorageConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.connectInstanceStorageConfig.ConnectInstanceStorageConfigStorageConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__eb63c5bdd3850fcf1410d523d9494882c0797c3604758eaa0bf5d8fc5260be2e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putKinesisFirehoseConfig")
    def put_kinesis_firehose_config(self, *, firehose_arn: builtins.str) -> None:
        '''
        :param firehose_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#firehose_arn ConnectInstanceStorageConfig#firehose_arn}.
        '''
        value = ConnectInstanceStorageConfigStorageConfigKinesisFirehoseConfig(
            firehose_arn=firehose_arn
        )

        return typing.cast(None, jsii.invoke(self, "putKinesisFirehoseConfig", [value]))

    @jsii.member(jsii_name="putKinesisStreamConfig")
    def put_kinesis_stream_config(self, *, stream_arn: builtins.str) -> None:
        '''
        :param stream_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#stream_arn ConnectInstanceStorageConfig#stream_arn}.
        '''
        value = ConnectInstanceStorageConfigStorageConfigKinesisStreamConfig(
            stream_arn=stream_arn
        )

        return typing.cast(None, jsii.invoke(self, "putKinesisStreamConfig", [value]))

    @jsii.member(jsii_name="putKinesisVideoStreamConfig")
    def put_kinesis_video_stream_config(
        self,
        *,
        encryption_config: typing.Union[ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfigEncryptionConfig, typing.Dict[builtins.str, typing.Any]],
        prefix: builtins.str,
        retention_period_hours: jsii.Number,
    ) -> None:
        '''
        :param encryption_config: encryption_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#encryption_config ConnectInstanceStorageConfig#encryption_config}
        :param prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#prefix ConnectInstanceStorageConfig#prefix}.
        :param retention_period_hours: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#retention_period_hours ConnectInstanceStorageConfig#retention_period_hours}.
        '''
        value = ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfig(
            encryption_config=encryption_config,
            prefix=prefix,
            retention_period_hours=retention_period_hours,
        )

        return typing.cast(None, jsii.invoke(self, "putKinesisVideoStreamConfig", [value]))

    @jsii.member(jsii_name="putS3Config")
    def put_s3_config(
        self,
        *,
        bucket_name: builtins.str,
        bucket_prefix: builtins.str,
        encryption_config: typing.Optional[typing.Union["ConnectInstanceStorageConfigStorageConfigS3ConfigEncryptionConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#bucket_name ConnectInstanceStorageConfig#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#bucket_prefix ConnectInstanceStorageConfig#bucket_prefix}.
        :param encryption_config: encryption_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#encryption_config ConnectInstanceStorageConfig#encryption_config}
        '''
        value = ConnectInstanceStorageConfigStorageConfigS3Config(
            bucket_name=bucket_name,
            bucket_prefix=bucket_prefix,
            encryption_config=encryption_config,
        )

        return typing.cast(None, jsii.invoke(self, "putS3Config", [value]))

    @jsii.member(jsii_name="resetKinesisFirehoseConfig")
    def reset_kinesis_firehose_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKinesisFirehoseConfig", []))

    @jsii.member(jsii_name="resetKinesisStreamConfig")
    def reset_kinesis_stream_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKinesisStreamConfig", []))

    @jsii.member(jsii_name="resetKinesisVideoStreamConfig")
    def reset_kinesis_video_stream_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKinesisVideoStreamConfig", []))

    @jsii.member(jsii_name="resetS3Config")
    def reset_s3_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3Config", []))

    @builtins.property
    @jsii.member(jsii_name="kinesisFirehoseConfig")
    def kinesis_firehose_config(
        self,
    ) -> ConnectInstanceStorageConfigStorageConfigKinesisFirehoseConfigOutputReference:
        return typing.cast(ConnectInstanceStorageConfigStorageConfigKinesisFirehoseConfigOutputReference, jsii.get(self, "kinesisFirehoseConfig"))

    @builtins.property
    @jsii.member(jsii_name="kinesisStreamConfig")
    def kinesis_stream_config(
        self,
    ) -> ConnectInstanceStorageConfigStorageConfigKinesisStreamConfigOutputReference:
        return typing.cast(ConnectInstanceStorageConfigStorageConfigKinesisStreamConfigOutputReference, jsii.get(self, "kinesisStreamConfig"))

    @builtins.property
    @jsii.member(jsii_name="kinesisVideoStreamConfig")
    def kinesis_video_stream_config(
        self,
    ) -> ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfigOutputReference:
        return typing.cast(ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfigOutputReference, jsii.get(self, "kinesisVideoStreamConfig"))

    @builtins.property
    @jsii.member(jsii_name="s3Config")
    def s3_config(
        self,
    ) -> "ConnectInstanceStorageConfigStorageConfigS3ConfigOutputReference":
        return typing.cast("ConnectInstanceStorageConfigStorageConfigS3ConfigOutputReference", jsii.get(self, "s3Config"))

    @builtins.property
    @jsii.member(jsii_name="kinesisFirehoseConfigInput")
    def kinesis_firehose_config_input(
        self,
    ) -> typing.Optional[ConnectInstanceStorageConfigStorageConfigKinesisFirehoseConfig]:
        return typing.cast(typing.Optional[ConnectInstanceStorageConfigStorageConfigKinesisFirehoseConfig], jsii.get(self, "kinesisFirehoseConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="kinesisStreamConfigInput")
    def kinesis_stream_config_input(
        self,
    ) -> typing.Optional[ConnectInstanceStorageConfigStorageConfigKinesisStreamConfig]:
        return typing.cast(typing.Optional[ConnectInstanceStorageConfigStorageConfigKinesisStreamConfig], jsii.get(self, "kinesisStreamConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="kinesisVideoStreamConfigInput")
    def kinesis_video_stream_config_input(
        self,
    ) -> typing.Optional[ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfig]:
        return typing.cast(typing.Optional[ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfig], jsii.get(self, "kinesisVideoStreamConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="s3ConfigInput")
    def s3_config_input(
        self,
    ) -> typing.Optional["ConnectInstanceStorageConfigStorageConfigS3Config"]:
        return typing.cast(typing.Optional["ConnectInstanceStorageConfigStorageConfigS3Config"], jsii.get(self, "s3ConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="storageTypeInput")
    def storage_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="storageType")
    def storage_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageType"))

    @storage_type.setter
    def storage_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__515929b38811e688911c436ac5426d05554c10279978ff24dcc56fea5333ecf1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ConnectInstanceStorageConfigStorageConfig]:
        return typing.cast(typing.Optional[ConnectInstanceStorageConfigStorageConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ConnectInstanceStorageConfigStorageConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87af4d024d893b83203d696fa46a5f91fc6e6b2ffdbfb2f3656c2bdf924745b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.connectInstanceStorageConfig.ConnectInstanceStorageConfigStorageConfigS3Config",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "bucket_prefix": "bucketPrefix",
        "encryption_config": "encryptionConfig",
    },
)
class ConnectInstanceStorageConfigStorageConfigS3Config:
    def __init__(
        self,
        *,
        bucket_name: builtins.str,
        bucket_prefix: builtins.str,
        encryption_config: typing.Optional[typing.Union["ConnectInstanceStorageConfigStorageConfigS3ConfigEncryptionConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#bucket_name ConnectInstanceStorageConfig#bucket_name}.
        :param bucket_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#bucket_prefix ConnectInstanceStorageConfig#bucket_prefix}.
        :param encryption_config: encryption_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#encryption_config ConnectInstanceStorageConfig#encryption_config}
        '''
        if isinstance(encryption_config, dict):
            encryption_config = ConnectInstanceStorageConfigStorageConfigS3ConfigEncryptionConfig(**encryption_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f814e4432ac0cedf8e18aa692173e6af6956f7fb9100e3f0c4aa84642a5e4de2)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            check_type(argname="argument encryption_config", value=encryption_config, expected_type=type_hints["encryption_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket_name": bucket_name,
            "bucket_prefix": bucket_prefix,
        }
        if encryption_config is not None:
            self._values["encryption_config"] = encryption_config

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#bucket_name ConnectInstanceStorageConfig#bucket_name}.'''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bucket_prefix(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#bucket_prefix ConnectInstanceStorageConfig#bucket_prefix}.'''
        result = self._values.get("bucket_prefix")
        assert result is not None, "Required property 'bucket_prefix' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def encryption_config(
        self,
    ) -> typing.Optional["ConnectInstanceStorageConfigStorageConfigS3ConfigEncryptionConfig"]:
        '''encryption_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#encryption_config ConnectInstanceStorageConfig#encryption_config}
        '''
        result = self._values.get("encryption_config")
        return typing.cast(typing.Optional["ConnectInstanceStorageConfigStorageConfigS3ConfigEncryptionConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectInstanceStorageConfigStorageConfigS3Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.connectInstanceStorageConfig.ConnectInstanceStorageConfigStorageConfigS3ConfigEncryptionConfig",
    jsii_struct_bases=[],
    name_mapping={"encryption_type": "encryptionType", "key_id": "keyId"},
)
class ConnectInstanceStorageConfigStorageConfigS3ConfigEncryptionConfig:
    def __init__(self, *, encryption_type: builtins.str, key_id: builtins.str) -> None:
        '''
        :param encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#encryption_type ConnectInstanceStorageConfig#encryption_type}.
        :param key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#key_id ConnectInstanceStorageConfig#key_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e97f0b29e3bd78a641d30cb6000cde6e1c09ff60acfa0b9ea49b0c7c15c8c2ea)
            check_type(argname="argument encryption_type", value=encryption_type, expected_type=type_hints["encryption_type"])
            check_type(argname="argument key_id", value=key_id, expected_type=type_hints["key_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "encryption_type": encryption_type,
            "key_id": key_id,
        }

    @builtins.property
    def encryption_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#encryption_type ConnectInstanceStorageConfig#encryption_type}.'''
        result = self._values.get("encryption_type")
        assert result is not None, "Required property 'encryption_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#key_id ConnectInstanceStorageConfig#key_id}.'''
        result = self._values.get("key_id")
        assert result is not None, "Required property 'key_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectInstanceStorageConfigStorageConfigS3ConfigEncryptionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ConnectInstanceStorageConfigStorageConfigS3ConfigEncryptionConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.connectInstanceStorageConfig.ConnectInstanceStorageConfigStorageConfigS3ConfigEncryptionConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__621c2723ed273103db250f4d2170a6b82c7de11bbd3f7b8364a9a3a1388987c2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="encryptionTypeInput")
    def encryption_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="keyIdInput")
    def key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionType")
    def encryption_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptionType"))

    @encryption_type.setter
    def encryption_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4291cd69df208bd65109ea640ae21559d24d1a0be051f21e71e607ba638e89dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionType", value)

    @builtins.property
    @jsii.member(jsii_name="keyId")
    def key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyId"))

    @key_id.setter
    def key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a23cb7e0212450d4e2b7ac7af310383a167fe6cddd2cc4434609426b8631d984)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ConnectInstanceStorageConfigStorageConfigS3ConfigEncryptionConfig]:
        return typing.cast(typing.Optional[ConnectInstanceStorageConfigStorageConfigS3ConfigEncryptionConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ConnectInstanceStorageConfigStorageConfigS3ConfigEncryptionConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8713471faf7dadeef9469b4e32c04da696a6a88e59002f54bfc2d7d0a4985ed2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ConnectInstanceStorageConfigStorageConfigS3ConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.connectInstanceStorageConfig.ConnectInstanceStorageConfigStorageConfigS3ConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8090305a617934d5191fe2d0d5d7a7d6017ea1848e609bd913b8c82aa6fafe38)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putEncryptionConfig")
    def put_encryption_config(
        self,
        *,
        encryption_type: builtins.str,
        key_id: builtins.str,
    ) -> None:
        '''
        :param encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#encryption_type ConnectInstanceStorageConfig#encryption_type}.
        :param key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/connect_instance_storage_config#key_id ConnectInstanceStorageConfig#key_id}.
        '''
        value = ConnectInstanceStorageConfigStorageConfigS3ConfigEncryptionConfig(
            encryption_type=encryption_type, key_id=key_id
        )

        return typing.cast(None, jsii.invoke(self, "putEncryptionConfig", [value]))

    @jsii.member(jsii_name="resetEncryptionConfig")
    def reset_encryption_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionConfig", []))

    @builtins.property
    @jsii.member(jsii_name="encryptionConfig")
    def encryption_config(
        self,
    ) -> ConnectInstanceStorageConfigStorageConfigS3ConfigEncryptionConfigOutputReference:
        return typing.cast(ConnectInstanceStorageConfigStorageConfigS3ConfigEncryptionConfigOutputReference, jsii.get(self, "encryptionConfig"))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketPrefixInput")
    def bucket_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionConfigInput")
    def encryption_config_input(
        self,
    ) -> typing.Optional[ConnectInstanceStorageConfigStorageConfigS3ConfigEncryptionConfig]:
        return typing.cast(typing.Optional[ConnectInstanceStorageConfigStorageConfigS3ConfigEncryptionConfig], jsii.get(self, "encryptionConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__451ac7a31dfd7c20adaaef4e74b57aa6959f2853045a7ca306d5b6ce0e246740)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="bucketPrefix")
    def bucket_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketPrefix"))

    @bucket_prefix.setter
    def bucket_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64758d1555340fd1df532468fda042f42b9bbb6d8a041f8ddf02cbcdd2d225cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ConnectInstanceStorageConfigStorageConfigS3Config]:
        return typing.cast(typing.Optional[ConnectInstanceStorageConfigStorageConfigS3Config], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ConnectInstanceStorageConfigStorageConfigS3Config],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__562b40c53ebf271ed3a9dd211f1334fd27ed0260618f424dd165713d6dd7b492)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ConnectInstanceStorageConfig",
    "ConnectInstanceStorageConfigConfig",
    "ConnectInstanceStorageConfigStorageConfig",
    "ConnectInstanceStorageConfigStorageConfigKinesisFirehoseConfig",
    "ConnectInstanceStorageConfigStorageConfigKinesisFirehoseConfigOutputReference",
    "ConnectInstanceStorageConfigStorageConfigKinesisStreamConfig",
    "ConnectInstanceStorageConfigStorageConfigKinesisStreamConfigOutputReference",
    "ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfig",
    "ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfigEncryptionConfig",
    "ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfigEncryptionConfigOutputReference",
    "ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfigOutputReference",
    "ConnectInstanceStorageConfigStorageConfigOutputReference",
    "ConnectInstanceStorageConfigStorageConfigS3Config",
    "ConnectInstanceStorageConfigStorageConfigS3ConfigEncryptionConfig",
    "ConnectInstanceStorageConfigStorageConfigS3ConfigEncryptionConfigOutputReference",
    "ConnectInstanceStorageConfigStorageConfigS3ConfigOutputReference",
]

publication.publish()

def _typecheckingstub__c488ef541476149c3114b9fb908c6e418e8b239efaa925452c50dca727a48b82(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    instance_id: builtins.str,
    resource_type: builtins.str,
    storage_config: typing.Union[ConnectInstanceStorageConfigStorageConfig, typing.Dict[builtins.str, typing.Any]],
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

def _typecheckingstub__e839ef4cd5e344ca1120579895e9190351df8ba5a0e0865ae97db4d952f2d598(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7c984e5b177987af7c42cf34fd92dbcf0fbfcbd7eef0259fbe490038dea9578(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__851fbd5da866bf040dca1f11bc253fadf78237fffcdde902b5f2fb675762ef19(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08a3e46457f81329c421abf1c910d955f323cd98f08a058cbcdee1d4281102b0(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    instance_id: builtins.str,
    resource_type: builtins.str,
    storage_config: typing.Union[ConnectInstanceStorageConfigStorageConfig, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d0fb9d3eff7e7a4c59333cd240473476548acc07e06c0b8612ac2909f9841da(
    *,
    storage_type: builtins.str,
    kinesis_firehose_config: typing.Optional[typing.Union[ConnectInstanceStorageConfigStorageConfigKinesisFirehoseConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    kinesis_stream_config: typing.Optional[typing.Union[ConnectInstanceStorageConfigStorageConfigKinesisStreamConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    kinesis_video_stream_config: typing.Optional[typing.Union[ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    s3_config: typing.Optional[typing.Union[ConnectInstanceStorageConfigStorageConfigS3Config, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1ae85325092adb13da697d49c9df1d147653c3826044ac01d33adec95dee49e(
    *,
    firehose_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6573b67baa96f5a39d32da5a00e75764e88ee9393360e51fd68131ac32635af9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7b30ff263420da88d5d5d53fe02b78ea32da1470e6b108a90b49f04c150771c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3078c3eb6a9bab6898861ff17964cf383e3e97a49a4cd88b540dd1d2281633e(
    value: typing.Optional[ConnectInstanceStorageConfigStorageConfigKinesisFirehoseConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1567ae99285c681d2536f7e52f5259c8c2c44dbb162a51770cb5f3d415ab07e(
    *,
    stream_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__966dad94644cd86bc1bcb51e126fddc1b21b59029109d58492fd3790370b7b09(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05666b62985b313397c29b92f4898275cc9ceb481500861dde28d6bd208f241e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59bfc52f1469f4473b286d06541d1f3fd2792c73fbf2295a90650c5471a9a42d(
    value: typing.Optional[ConnectInstanceStorageConfigStorageConfigKinesisStreamConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95b11f145ee0db3496515eacc96d4d4ea8f9fbb27d9e4ebfd3776d87e425e3f3(
    *,
    encryption_config: typing.Union[ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfigEncryptionConfig, typing.Dict[builtins.str, typing.Any]],
    prefix: builtins.str,
    retention_period_hours: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26714f0efb4f38ca206d739c8911210b4a9efc4e5d34181f67bf261cab9b79da(
    *,
    encryption_type: builtins.str,
    key_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eec2c03ed525f6e7e8f2b6275b804e0a577046d82fb534887f040c0a87920a09(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c964117a984326044f07eb5f3de0f170398c3f832de21383eec36e2657fca182(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40a63016639b9d820a82a5c5cc4810de8e043cb81dbf9117f95c2b3cc12d6d59(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6ec44b2041d9d23415be84d966299e4c3dc9b774dbe92dda51b4610212f4745(
    value: typing.Optional[ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfigEncryptionConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c16ace3b4c42bb7117ea304cab93bbe4490655c54bb8c687292c16d58005310f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f15d64bb0e87dae8f22467623b10adc68837114386435e040a0b0e1eaed16327(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c3e4f90252fe502db510fe832b998bc1685467e62e0c912698d6bf592bbc782(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3932aa782a10a5b9f0a45fa8fe78450b29ef12bfbcdf62f83f8ed992226afd4e(
    value: typing.Optional[ConnectInstanceStorageConfigStorageConfigKinesisVideoStreamConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb63c5bdd3850fcf1410d523d9494882c0797c3604758eaa0bf5d8fc5260be2e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__515929b38811e688911c436ac5426d05554c10279978ff24dcc56fea5333ecf1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87af4d024d893b83203d696fa46a5f91fc6e6b2ffdbfb2f3656c2bdf924745b8(
    value: typing.Optional[ConnectInstanceStorageConfigStorageConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f814e4432ac0cedf8e18aa692173e6af6956f7fb9100e3f0c4aa84642a5e4de2(
    *,
    bucket_name: builtins.str,
    bucket_prefix: builtins.str,
    encryption_config: typing.Optional[typing.Union[ConnectInstanceStorageConfigStorageConfigS3ConfigEncryptionConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e97f0b29e3bd78a641d30cb6000cde6e1c09ff60acfa0b9ea49b0c7c15c8c2ea(
    *,
    encryption_type: builtins.str,
    key_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__621c2723ed273103db250f4d2170a6b82c7de11bbd3f7b8364a9a3a1388987c2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4291cd69df208bd65109ea640ae21559d24d1a0be051f21e71e607ba638e89dd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a23cb7e0212450d4e2b7ac7af310383a167fe6cddd2cc4434609426b8631d984(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8713471faf7dadeef9469b4e32c04da696a6a88e59002f54bfc2d7d0a4985ed2(
    value: typing.Optional[ConnectInstanceStorageConfigStorageConfigS3ConfigEncryptionConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8090305a617934d5191fe2d0d5d7a7d6017ea1848e609bd913b8c82aa6fafe38(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__451ac7a31dfd7c20adaaef4e74b57aa6959f2853045a7ca306d5b6ce0e246740(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64758d1555340fd1df532468fda042f42b9bbb6d8a041f8ddf02cbcdd2d225cc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__562b40c53ebf271ed3a9dd211f1334fd27ed0260618f424dd165713d6dd7b492(
    value: typing.Optional[ConnectInstanceStorageConfigStorageConfigS3Config],
) -> None:
    """Type checking stubs"""
    pass
