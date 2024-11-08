'''
# `aws_cloudfront_realtime_log_config`

Refer to the Terraform Registory for docs: [`aws_cloudfront_realtime_log_config`](https://www.terraform.io/docs/providers/aws/r/cloudfront_realtime_log_config).
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


class CloudfrontRealtimeLogConfig(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontRealtimeLogConfig.CloudfrontRealtimeLogConfig",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_realtime_log_config aws_cloudfront_realtime_log_config}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        endpoint: typing.Union["CloudfrontRealtimeLogConfigEndpoint", typing.Dict[builtins.str, typing.Any]],
        fields: typing.Sequence[builtins.str],
        name: builtins.str,
        sampling_rate: jsii.Number,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_realtime_log_config aws_cloudfront_realtime_log_config} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param endpoint: endpoint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_realtime_log_config#endpoint CloudfrontRealtimeLogConfig#endpoint}
        :param fields: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_realtime_log_config#fields CloudfrontRealtimeLogConfig#fields}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_realtime_log_config#name CloudfrontRealtimeLogConfig#name}.
        :param sampling_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_realtime_log_config#sampling_rate CloudfrontRealtimeLogConfig#sampling_rate}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_realtime_log_config#id CloudfrontRealtimeLogConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d438fcb5cdbb7160c65ae0414759a245c03df081a7893326ae39f44db31fec87)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CloudfrontRealtimeLogConfigConfig(
            endpoint=endpoint,
            fields=fields,
            name=name,
            sampling_rate=sampling_rate,
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

    @jsii.member(jsii_name="putEndpoint")
    def put_endpoint(
        self,
        *,
        kinesis_stream_config: typing.Union["CloudfrontRealtimeLogConfigEndpointKinesisStreamConfig", typing.Dict[builtins.str, typing.Any]],
        stream_type: builtins.str,
    ) -> None:
        '''
        :param kinesis_stream_config: kinesis_stream_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_realtime_log_config#kinesis_stream_config CloudfrontRealtimeLogConfig#kinesis_stream_config}
        :param stream_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_realtime_log_config#stream_type CloudfrontRealtimeLogConfig#stream_type}.
        '''
        value = CloudfrontRealtimeLogConfigEndpoint(
            kinesis_stream_config=kinesis_stream_config, stream_type=stream_type
        )

        return typing.cast(None, jsii.invoke(self, "putEndpoint", [value]))

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
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> "CloudfrontRealtimeLogConfigEndpointOutputReference":
        return typing.cast("CloudfrontRealtimeLogConfigEndpointOutputReference", jsii.get(self, "endpoint"))

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional["CloudfrontRealtimeLogConfigEndpoint"]:
        return typing.cast(typing.Optional["CloudfrontRealtimeLogConfigEndpoint"], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="fieldsInput")
    def fields_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "fieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="samplingRateInput")
    def sampling_rate_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "samplingRateInput"))

    @builtins.property
    @jsii.member(jsii_name="fields")
    def fields(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "fields"))

    @fields.setter
    def fields(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fe2f3d9f38a1ae44d781dba92e6aba0018398aa2bdc06d9bc20123ab875a82d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fields", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fe79e93f80caadb4bf51e45bf4aaf834133ca10fc0cbc0534511c0e22059c01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ccf7df694ae608d054139a67faf1587cbbe7affb8390781a7a33ab9955d1cfe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="samplingRate")
    def sampling_rate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "samplingRate"))

    @sampling_rate.setter
    def sampling_rate(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1040656d15d8217ef4140e44f12068f7a3d4d5281c118cd5f2c5bd25ed3a155)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "samplingRate", value)


@jsii.data_type(
    jsii_type="aws.cloudfrontRealtimeLogConfig.CloudfrontRealtimeLogConfigConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "endpoint": "endpoint",
        "fields": "fields",
        "name": "name",
        "sampling_rate": "samplingRate",
        "id": "id",
    },
)
class CloudfrontRealtimeLogConfigConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        endpoint: typing.Union["CloudfrontRealtimeLogConfigEndpoint", typing.Dict[builtins.str, typing.Any]],
        fields: typing.Sequence[builtins.str],
        name: builtins.str,
        sampling_rate: jsii.Number,
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
        :param endpoint: endpoint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_realtime_log_config#endpoint CloudfrontRealtimeLogConfig#endpoint}
        :param fields: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_realtime_log_config#fields CloudfrontRealtimeLogConfig#fields}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_realtime_log_config#name CloudfrontRealtimeLogConfig#name}.
        :param sampling_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_realtime_log_config#sampling_rate CloudfrontRealtimeLogConfig#sampling_rate}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_realtime_log_config#id CloudfrontRealtimeLogConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(endpoint, dict):
            endpoint = CloudfrontRealtimeLogConfigEndpoint(**endpoint)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7c5da11b5a396f41afd0364a3f4c0d0c2028a2e06c6296dab2214526e1dce08)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument fields", value=fields, expected_type=type_hints["fields"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument sampling_rate", value=sampling_rate, expected_type=type_hints["sampling_rate"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoint": endpoint,
            "fields": fields,
            "name": name,
            "sampling_rate": sampling_rate,
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
    def endpoint(self) -> "CloudfrontRealtimeLogConfigEndpoint":
        '''endpoint block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_realtime_log_config#endpoint CloudfrontRealtimeLogConfig#endpoint}
        '''
        result = self._values.get("endpoint")
        assert result is not None, "Required property 'endpoint' is missing"
        return typing.cast("CloudfrontRealtimeLogConfigEndpoint", result)

    @builtins.property
    def fields(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_realtime_log_config#fields CloudfrontRealtimeLogConfig#fields}.'''
        result = self._values.get("fields")
        assert result is not None, "Required property 'fields' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_realtime_log_config#name CloudfrontRealtimeLogConfig#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sampling_rate(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_realtime_log_config#sampling_rate CloudfrontRealtimeLogConfig#sampling_rate}.'''
        result = self._values.get("sampling_rate")
        assert result is not None, "Required property 'sampling_rate' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_realtime_log_config#id CloudfrontRealtimeLogConfig#id}.

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
        return "CloudfrontRealtimeLogConfigConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.cloudfrontRealtimeLogConfig.CloudfrontRealtimeLogConfigEndpoint",
    jsii_struct_bases=[],
    name_mapping={
        "kinesis_stream_config": "kinesisStreamConfig",
        "stream_type": "streamType",
    },
)
class CloudfrontRealtimeLogConfigEndpoint:
    def __init__(
        self,
        *,
        kinesis_stream_config: typing.Union["CloudfrontRealtimeLogConfigEndpointKinesisStreamConfig", typing.Dict[builtins.str, typing.Any]],
        stream_type: builtins.str,
    ) -> None:
        '''
        :param kinesis_stream_config: kinesis_stream_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_realtime_log_config#kinesis_stream_config CloudfrontRealtimeLogConfig#kinesis_stream_config}
        :param stream_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_realtime_log_config#stream_type CloudfrontRealtimeLogConfig#stream_type}.
        '''
        if isinstance(kinesis_stream_config, dict):
            kinesis_stream_config = CloudfrontRealtimeLogConfigEndpointKinesisStreamConfig(**kinesis_stream_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2fdfa75486398c18d4263195f52d6c239d5006e8b1e8f386d5f3d0b6d389e1c)
            check_type(argname="argument kinesis_stream_config", value=kinesis_stream_config, expected_type=type_hints["kinesis_stream_config"])
            check_type(argname="argument stream_type", value=stream_type, expected_type=type_hints["stream_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "kinesis_stream_config": kinesis_stream_config,
            "stream_type": stream_type,
        }

    @builtins.property
    def kinesis_stream_config(
        self,
    ) -> "CloudfrontRealtimeLogConfigEndpointKinesisStreamConfig":
        '''kinesis_stream_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_realtime_log_config#kinesis_stream_config CloudfrontRealtimeLogConfig#kinesis_stream_config}
        '''
        result = self._values.get("kinesis_stream_config")
        assert result is not None, "Required property 'kinesis_stream_config' is missing"
        return typing.cast("CloudfrontRealtimeLogConfigEndpointKinesisStreamConfig", result)

    @builtins.property
    def stream_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_realtime_log_config#stream_type CloudfrontRealtimeLogConfig#stream_type}.'''
        result = self._values.get("stream_type")
        assert result is not None, "Required property 'stream_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontRealtimeLogConfigEndpoint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.cloudfrontRealtimeLogConfig.CloudfrontRealtimeLogConfigEndpointKinesisStreamConfig",
    jsii_struct_bases=[],
    name_mapping={"role_arn": "roleArn", "stream_arn": "streamArn"},
)
class CloudfrontRealtimeLogConfigEndpointKinesisStreamConfig:
    def __init__(self, *, role_arn: builtins.str, stream_arn: builtins.str) -> None:
        '''
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_realtime_log_config#role_arn CloudfrontRealtimeLogConfig#role_arn}.
        :param stream_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_realtime_log_config#stream_arn CloudfrontRealtimeLogConfig#stream_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d19c7068bbcc1064e8c65b787a646e4033414ae344476016340d44a7c830fc0)
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument stream_arn", value=stream_arn, expected_type=type_hints["stream_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "role_arn": role_arn,
            "stream_arn": stream_arn,
        }

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_realtime_log_config#role_arn CloudfrontRealtimeLogConfig#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stream_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_realtime_log_config#stream_arn CloudfrontRealtimeLogConfig#stream_arn}.'''
        result = self._values.get("stream_arn")
        assert result is not None, "Required property 'stream_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontRealtimeLogConfigEndpointKinesisStreamConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontRealtimeLogConfigEndpointKinesisStreamConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontRealtimeLogConfig.CloudfrontRealtimeLogConfigEndpointKinesisStreamConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e94709f13d9d566e4cb9b6dbb2f96c5ac4ebd5b4de890ec883a123e8dc758477)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="streamArnInput")
    def stream_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streamArnInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5b93e2800fdf71b9ae33435bc1feade6c82ee8c93ce6dfd0fb83a32fad7dd55)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="streamArn")
    def stream_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "streamArn"))

    @stream_arn.setter
    def stream_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af9fc31db11776a3e6090842da499825e1cc20f0e6e1ceb9d2152614a6393043)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontRealtimeLogConfigEndpointKinesisStreamConfig]:
        return typing.cast(typing.Optional[CloudfrontRealtimeLogConfigEndpointKinesisStreamConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontRealtimeLogConfigEndpointKinesisStreamConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6ba5eb643d8d3caa2a2e4957c10c32b0fc4d38c243249e9a14e3a3472f65dc6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudfrontRealtimeLogConfigEndpointOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontRealtimeLogConfig.CloudfrontRealtimeLogConfigEndpointOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3e16b1036424839d96a8b3742cabeed035d2cdf0dcd884b152bf0403277e37fc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putKinesisStreamConfig")
    def put_kinesis_stream_config(
        self,
        *,
        role_arn: builtins.str,
        stream_arn: builtins.str,
    ) -> None:
        '''
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_realtime_log_config#role_arn CloudfrontRealtimeLogConfig#role_arn}.
        :param stream_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_realtime_log_config#stream_arn CloudfrontRealtimeLogConfig#stream_arn}.
        '''
        value = CloudfrontRealtimeLogConfigEndpointKinesisStreamConfig(
            role_arn=role_arn, stream_arn=stream_arn
        )

        return typing.cast(None, jsii.invoke(self, "putKinesisStreamConfig", [value]))

    @builtins.property
    @jsii.member(jsii_name="kinesisStreamConfig")
    def kinesis_stream_config(
        self,
    ) -> CloudfrontRealtimeLogConfigEndpointKinesisStreamConfigOutputReference:
        return typing.cast(CloudfrontRealtimeLogConfigEndpointKinesisStreamConfigOutputReference, jsii.get(self, "kinesisStreamConfig"))

    @builtins.property
    @jsii.member(jsii_name="kinesisStreamConfigInput")
    def kinesis_stream_config_input(
        self,
    ) -> typing.Optional[CloudfrontRealtimeLogConfigEndpointKinesisStreamConfig]:
        return typing.cast(typing.Optional[CloudfrontRealtimeLogConfigEndpointKinesisStreamConfig], jsii.get(self, "kinesisStreamConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="streamTypeInput")
    def stream_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streamTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="streamType")
    def stream_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "streamType"))

    @stream_type.setter
    def stream_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71fad193402676bb18d83d07b248f081c907448d5c3ea1d75011658254a584bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudfrontRealtimeLogConfigEndpoint]:
        return typing.cast(typing.Optional[CloudfrontRealtimeLogConfigEndpoint], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontRealtimeLogConfigEndpoint],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7f1a8ba306785725882bf733293961991b49e7ab9d1539794dc6ba4aad148c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CloudfrontRealtimeLogConfig",
    "CloudfrontRealtimeLogConfigConfig",
    "CloudfrontRealtimeLogConfigEndpoint",
    "CloudfrontRealtimeLogConfigEndpointKinesisStreamConfig",
    "CloudfrontRealtimeLogConfigEndpointKinesisStreamConfigOutputReference",
    "CloudfrontRealtimeLogConfigEndpointOutputReference",
]

publication.publish()

def _typecheckingstub__d438fcb5cdbb7160c65ae0414759a245c03df081a7893326ae39f44db31fec87(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    endpoint: typing.Union[CloudfrontRealtimeLogConfigEndpoint, typing.Dict[builtins.str, typing.Any]],
    fields: typing.Sequence[builtins.str],
    name: builtins.str,
    sampling_rate: jsii.Number,
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

def _typecheckingstub__1fe2f3d9f38a1ae44d781dba92e6aba0018398aa2bdc06d9bc20123ab875a82d(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fe79e93f80caadb4bf51e45bf4aaf834133ca10fc0cbc0534511c0e22059c01(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ccf7df694ae608d054139a67faf1587cbbe7affb8390781a7a33ab9955d1cfe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1040656d15d8217ef4140e44f12068f7a3d4d5281c118cd5f2c5bd25ed3a155(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7c5da11b5a396f41afd0364a3f4c0d0c2028a2e06c6296dab2214526e1dce08(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    endpoint: typing.Union[CloudfrontRealtimeLogConfigEndpoint, typing.Dict[builtins.str, typing.Any]],
    fields: typing.Sequence[builtins.str],
    name: builtins.str,
    sampling_rate: jsii.Number,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2fdfa75486398c18d4263195f52d6c239d5006e8b1e8f386d5f3d0b6d389e1c(
    *,
    kinesis_stream_config: typing.Union[CloudfrontRealtimeLogConfigEndpointKinesisStreamConfig, typing.Dict[builtins.str, typing.Any]],
    stream_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d19c7068bbcc1064e8c65b787a646e4033414ae344476016340d44a7c830fc0(
    *,
    role_arn: builtins.str,
    stream_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e94709f13d9d566e4cb9b6dbb2f96c5ac4ebd5b4de890ec883a123e8dc758477(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5b93e2800fdf71b9ae33435bc1feade6c82ee8c93ce6dfd0fb83a32fad7dd55(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af9fc31db11776a3e6090842da499825e1cc20f0e6e1ceb9d2152614a6393043(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6ba5eb643d8d3caa2a2e4957c10c32b0fc4d38c243249e9a14e3a3472f65dc6(
    value: typing.Optional[CloudfrontRealtimeLogConfigEndpointKinesisStreamConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e16b1036424839d96a8b3742cabeed035d2cdf0dcd884b152bf0403277e37fc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71fad193402676bb18d83d07b248f081c907448d5c3ea1d75011658254a584bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7f1a8ba306785725882bf733293961991b49e7ab9d1539794dc6ba4aad148c5(
    value: typing.Optional[CloudfrontRealtimeLogConfigEndpoint],
) -> None:
    """Type checking stubs"""
    pass
