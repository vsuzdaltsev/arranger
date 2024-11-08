'''
# `aws_sagemaker_endpoint_configuration`

Refer to the Terraform Registory for docs: [`aws_sagemaker_endpoint_configuration`](https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration).
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


class SagemakerEndpointConfiguration(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerEndpointConfiguration.SagemakerEndpointConfiguration",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration aws_sagemaker_endpoint_configuration}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        production_variants: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerEndpointConfigurationProductionVariants", typing.Dict[builtins.str, typing.Any]]]],
        async_inference_config: typing.Optional[typing.Union["SagemakerEndpointConfigurationAsyncInferenceConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        data_capture_config: typing.Optional[typing.Union["SagemakerEndpointConfigurationDataCaptureConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        shadow_production_variants: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerEndpointConfigurationShadowProductionVariants", typing.Dict[builtins.str, typing.Any]]]]] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration aws_sagemaker_endpoint_configuration} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param production_variants: production_variants block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#production_variants SagemakerEndpointConfiguration#production_variants}
        :param async_inference_config: async_inference_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#async_inference_config SagemakerEndpointConfiguration#async_inference_config}
        :param data_capture_config: data_capture_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#data_capture_config SagemakerEndpointConfiguration#data_capture_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#id SagemakerEndpointConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#kms_key_arn SagemakerEndpointConfiguration#kms_key_arn}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#name SagemakerEndpointConfiguration#name}.
        :param shadow_production_variants: shadow_production_variants block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#shadow_production_variants SagemakerEndpointConfiguration#shadow_production_variants}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#tags SagemakerEndpointConfiguration#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#tags_all SagemakerEndpointConfiguration#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4be27fd33f6ca8cfded9c63cf2f0e11ba33858234266caaeddfef9c5a5eafe0a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SagemakerEndpointConfigurationConfig(
            production_variants=production_variants,
            async_inference_config=async_inference_config,
            data_capture_config=data_capture_config,
            id=id,
            kms_key_arn=kms_key_arn,
            name=name,
            shadow_production_variants=shadow_production_variants,
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

    @jsii.member(jsii_name="putAsyncInferenceConfig")
    def put_async_inference_config(
        self,
        *,
        output_config: typing.Union["SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfig", typing.Dict[builtins.str, typing.Any]],
        client_config: typing.Optional[typing.Union["SagemakerEndpointConfigurationAsyncInferenceConfigClientConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param output_config: output_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#output_config SagemakerEndpointConfiguration#output_config}
        :param client_config: client_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#client_config SagemakerEndpointConfiguration#client_config}
        '''
        value = SagemakerEndpointConfigurationAsyncInferenceConfig(
            output_config=output_config, client_config=client_config
        )

        return typing.cast(None, jsii.invoke(self, "putAsyncInferenceConfig", [value]))

    @jsii.member(jsii_name="putDataCaptureConfig")
    def put_data_capture_config(
        self,
        *,
        capture_options: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions", typing.Dict[builtins.str, typing.Any]]]],
        destination_s3_uri: builtins.str,
        initial_sampling_percentage: jsii.Number,
        capture_content_type_header: typing.Optional[typing.Union["SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeader", typing.Dict[builtins.str, typing.Any]]] = None,
        enable_capture: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param capture_options: capture_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#capture_options SagemakerEndpointConfiguration#capture_options}
        :param destination_s3_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#destination_s3_uri SagemakerEndpointConfiguration#destination_s3_uri}.
        :param initial_sampling_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#initial_sampling_percentage SagemakerEndpointConfiguration#initial_sampling_percentage}.
        :param capture_content_type_header: capture_content_type_header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#capture_content_type_header SagemakerEndpointConfiguration#capture_content_type_header}
        :param enable_capture: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#enable_capture SagemakerEndpointConfiguration#enable_capture}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#kms_key_id SagemakerEndpointConfiguration#kms_key_id}.
        '''
        value = SagemakerEndpointConfigurationDataCaptureConfig(
            capture_options=capture_options,
            destination_s3_uri=destination_s3_uri,
            initial_sampling_percentage=initial_sampling_percentage,
            capture_content_type_header=capture_content_type_header,
            enable_capture=enable_capture,
            kms_key_id=kms_key_id,
        )

        return typing.cast(None, jsii.invoke(self, "putDataCaptureConfig", [value]))

    @jsii.member(jsii_name="putProductionVariants")
    def put_production_variants(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerEndpointConfigurationProductionVariants", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8d09c25f9a289e1d40426eebfcdf0a16198c74a85226ee70d2d489219d51c01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putProductionVariants", [value]))

    @jsii.member(jsii_name="putShadowProductionVariants")
    def put_shadow_production_variants(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerEndpointConfigurationShadowProductionVariants", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34f289e51de2a03a9130b3296541775b1afae748d61598c7d22e9cf1143d55d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putShadowProductionVariants", [value]))

    @jsii.member(jsii_name="resetAsyncInferenceConfig")
    def reset_async_inference_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAsyncInferenceConfig", []))

    @jsii.member(jsii_name="resetDataCaptureConfig")
    def reset_data_capture_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataCaptureConfig", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKmsKeyArn")
    def reset_kms_key_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyArn", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetShadowProductionVariants")
    def reset_shadow_production_variants(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShadowProductionVariants", []))

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
    @jsii.member(jsii_name="asyncInferenceConfig")
    def async_inference_config(
        self,
    ) -> "SagemakerEndpointConfigurationAsyncInferenceConfigOutputReference":
        return typing.cast("SagemakerEndpointConfigurationAsyncInferenceConfigOutputReference", jsii.get(self, "asyncInferenceConfig"))

    @builtins.property
    @jsii.member(jsii_name="dataCaptureConfig")
    def data_capture_config(
        self,
    ) -> "SagemakerEndpointConfigurationDataCaptureConfigOutputReference":
        return typing.cast("SagemakerEndpointConfigurationDataCaptureConfigOutputReference", jsii.get(self, "dataCaptureConfig"))

    @builtins.property
    @jsii.member(jsii_name="productionVariants")
    def production_variants(
        self,
    ) -> "SagemakerEndpointConfigurationProductionVariantsList":
        return typing.cast("SagemakerEndpointConfigurationProductionVariantsList", jsii.get(self, "productionVariants"))

    @builtins.property
    @jsii.member(jsii_name="shadowProductionVariants")
    def shadow_production_variants(
        self,
    ) -> "SagemakerEndpointConfigurationShadowProductionVariantsList":
        return typing.cast("SagemakerEndpointConfigurationShadowProductionVariantsList", jsii.get(self, "shadowProductionVariants"))

    @builtins.property
    @jsii.member(jsii_name="asyncInferenceConfigInput")
    def async_inference_config_input(
        self,
    ) -> typing.Optional["SagemakerEndpointConfigurationAsyncInferenceConfig"]:
        return typing.cast(typing.Optional["SagemakerEndpointConfigurationAsyncInferenceConfig"], jsii.get(self, "asyncInferenceConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="dataCaptureConfigInput")
    def data_capture_config_input(
        self,
    ) -> typing.Optional["SagemakerEndpointConfigurationDataCaptureConfig"]:
        return typing.cast(typing.Optional["SagemakerEndpointConfigurationDataCaptureConfig"], jsii.get(self, "dataCaptureConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArnInput")
    def kms_key_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArnInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="productionVariantsInput")
    def production_variants_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerEndpointConfigurationProductionVariants"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerEndpointConfigurationProductionVariants"]]], jsii.get(self, "productionVariantsInput"))

    @builtins.property
    @jsii.member(jsii_name="shadowProductionVariantsInput")
    def shadow_production_variants_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerEndpointConfigurationShadowProductionVariants"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerEndpointConfigurationShadowProductionVariants"]]], jsii.get(self, "shadowProductionVariantsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__db55fa2c0ef90babc07a7d2623012644d0180dbf70ef6a13dbb44f0842b21ce1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5669263d6685ec022434a20eeb465361cab572a72351fc912e26de4dd11eb9ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f639271930c9147bc101de37b80919a1755a00db29aa154dd9d498b253ba882d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8f6d4a70f0c1a278e196d3ea7c0aea4912c8c362082b6b6cb1800e7d1dc2802)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e200d299ccf100a6b77ed93b23acada33d25181bc1855654ee2f6c18d518cfbf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationAsyncInferenceConfig",
    jsii_struct_bases=[],
    name_mapping={"output_config": "outputConfig", "client_config": "clientConfig"},
)
class SagemakerEndpointConfigurationAsyncInferenceConfig:
    def __init__(
        self,
        *,
        output_config: typing.Union["SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfig", typing.Dict[builtins.str, typing.Any]],
        client_config: typing.Optional[typing.Union["SagemakerEndpointConfigurationAsyncInferenceConfigClientConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param output_config: output_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#output_config SagemakerEndpointConfiguration#output_config}
        :param client_config: client_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#client_config SagemakerEndpointConfiguration#client_config}
        '''
        if isinstance(output_config, dict):
            output_config = SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfig(**output_config)
        if isinstance(client_config, dict):
            client_config = SagemakerEndpointConfigurationAsyncInferenceConfigClientConfig(**client_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc1d0f1f4fd1ffe8062d4afc81d072f67940df58fec23dac5f0d882373b48523)
            check_type(argname="argument output_config", value=output_config, expected_type=type_hints["output_config"])
            check_type(argname="argument client_config", value=client_config, expected_type=type_hints["client_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "output_config": output_config,
        }
        if client_config is not None:
            self._values["client_config"] = client_config

    @builtins.property
    def output_config(
        self,
    ) -> "SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfig":
        '''output_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#output_config SagemakerEndpointConfiguration#output_config}
        '''
        result = self._values.get("output_config")
        assert result is not None, "Required property 'output_config' is missing"
        return typing.cast("SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfig", result)

    @builtins.property
    def client_config(
        self,
    ) -> typing.Optional["SagemakerEndpointConfigurationAsyncInferenceConfigClientConfig"]:
        '''client_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#client_config SagemakerEndpointConfiguration#client_config}
        '''
        result = self._values.get("client_config")
        return typing.cast(typing.Optional["SagemakerEndpointConfigurationAsyncInferenceConfigClientConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerEndpointConfigurationAsyncInferenceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationAsyncInferenceConfigClientConfig",
    jsii_struct_bases=[],
    name_mapping={
        "max_concurrent_invocations_per_instance": "maxConcurrentInvocationsPerInstance",
    },
)
class SagemakerEndpointConfigurationAsyncInferenceConfigClientConfig:
    def __init__(
        self,
        *,
        max_concurrent_invocations_per_instance: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_concurrent_invocations_per_instance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#max_concurrent_invocations_per_instance SagemakerEndpointConfiguration#max_concurrent_invocations_per_instance}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f500801de7ed52609bff6712be2f08df5d0f64178cda1f54b46057387ce94cf2)
            check_type(argname="argument max_concurrent_invocations_per_instance", value=max_concurrent_invocations_per_instance, expected_type=type_hints["max_concurrent_invocations_per_instance"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if max_concurrent_invocations_per_instance is not None:
            self._values["max_concurrent_invocations_per_instance"] = max_concurrent_invocations_per_instance

    @builtins.property
    def max_concurrent_invocations_per_instance(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#max_concurrent_invocations_per_instance SagemakerEndpointConfiguration#max_concurrent_invocations_per_instance}.'''
        result = self._values.get("max_concurrent_invocations_per_instance")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerEndpointConfigurationAsyncInferenceConfigClientConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerEndpointConfigurationAsyncInferenceConfigClientConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationAsyncInferenceConfigClientConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e96d3c1e1750f4f552c1a98fb44a8dc052caf6c23dba988750f0c7ba7756eea1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMaxConcurrentInvocationsPerInstance")
    def reset_max_concurrent_invocations_per_instance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConcurrentInvocationsPerInstance", []))

    @builtins.property
    @jsii.member(jsii_name="maxConcurrentInvocationsPerInstanceInput")
    def max_concurrent_invocations_per_instance_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConcurrentInvocationsPerInstanceInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConcurrentInvocationsPerInstance")
    def max_concurrent_invocations_per_instance(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConcurrentInvocationsPerInstance"))

    @max_concurrent_invocations_per_instance.setter
    def max_concurrent_invocations_per_instance(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11297debb79c74e9d9b60d5d1c065af6611aa155c162a724c4b21dadf5ce1eb0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConcurrentInvocationsPerInstance", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfigClientConfig]:
        return typing.cast(typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfigClientConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfigClientConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4817601952ff59c7e4573004eb22a2e43ceb1aa25a413548bbe9b8868917f366)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfig",
    jsii_struct_bases=[],
    name_mapping={
        "s3_output_path": "s3OutputPath",
        "kms_key_id": "kmsKeyId",
        "notification_config": "notificationConfig",
    },
)
class SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfig:
    def __init__(
        self,
        *,
        s3_output_path: builtins.str,
        kms_key_id: typing.Optional[builtins.str] = None,
        notification_config: typing.Optional[typing.Union["SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param s3_output_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#s3_output_path SagemakerEndpointConfiguration#s3_output_path}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#kms_key_id SagemakerEndpointConfiguration#kms_key_id}.
        :param notification_config: notification_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#notification_config SagemakerEndpointConfiguration#notification_config}
        '''
        if isinstance(notification_config, dict):
            notification_config = SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfig(**notification_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cee4d90101ebf83952184e0212e035cbdaba2d42dfeab85ed41fb06ed260387e)
            check_type(argname="argument s3_output_path", value=s3_output_path, expected_type=type_hints["s3_output_path"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument notification_config", value=notification_config, expected_type=type_hints["notification_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "s3_output_path": s3_output_path,
        }
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if notification_config is not None:
            self._values["notification_config"] = notification_config

    @builtins.property
    def s3_output_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#s3_output_path SagemakerEndpointConfiguration#s3_output_path}.'''
        result = self._values.get("s3_output_path")
        assert result is not None, "Required property 's3_output_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#kms_key_id SagemakerEndpointConfiguration#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_config(
        self,
    ) -> typing.Optional["SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfig"]:
        '''notification_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#notification_config SagemakerEndpointConfiguration#notification_config}
        '''
        result = self._values.get("notification_config")
        return typing.cast(typing.Optional["SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfig",
    jsii_struct_bases=[],
    name_mapping={"error_topic": "errorTopic", "success_topic": "successTopic"},
)
class SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfig:
    def __init__(
        self,
        *,
        error_topic: typing.Optional[builtins.str] = None,
        success_topic: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param error_topic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#error_topic SagemakerEndpointConfiguration#error_topic}.
        :param success_topic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#success_topic SagemakerEndpointConfiguration#success_topic}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__748f9e2d8411fdd49b8b1b8b7d27e4451d5717b9a208c5ef298403288042a828)
            check_type(argname="argument error_topic", value=error_topic, expected_type=type_hints["error_topic"])
            check_type(argname="argument success_topic", value=success_topic, expected_type=type_hints["success_topic"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if error_topic is not None:
            self._values["error_topic"] = error_topic
        if success_topic is not None:
            self._values["success_topic"] = success_topic

    @builtins.property
    def error_topic(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#error_topic SagemakerEndpointConfiguration#error_topic}.'''
        result = self._values.get("error_topic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def success_topic(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#success_topic SagemakerEndpointConfiguration#success_topic}.'''
        result = self._values.get("success_topic")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e57c10dce10eef07eff5028967a2b0ffed5548e40b0a8e65259ee1def72486ac)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetErrorTopic")
    def reset_error_topic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorTopic", []))

    @jsii.member(jsii_name="resetSuccessTopic")
    def reset_success_topic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuccessTopic", []))

    @builtins.property
    @jsii.member(jsii_name="errorTopicInput")
    def error_topic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "errorTopicInput"))

    @builtins.property
    @jsii.member(jsii_name="successTopicInput")
    def success_topic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "successTopicInput"))

    @builtins.property
    @jsii.member(jsii_name="errorTopic")
    def error_topic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "errorTopic"))

    @error_topic.setter
    def error_topic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0022f7a8bd27c19718c9f713472a8532c2c0c6e7e758eb60a70b90299e3e4b44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "errorTopic", value)

    @builtins.property
    @jsii.member(jsii_name="successTopic")
    def success_topic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "successTopic"))

    @success_topic.setter
    def success_topic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d43cc8d5c05b755455448c2cfd045f048d5692590219490b907fcc0e1bacadd0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "successTopic", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfig]:
        return typing.cast(typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77d1f7edf5605e05d2bd640e45419a1a1fc92edbdb1ae527335a5fbb80c8063c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__95ea2adb1f38ad212e14aad10b8d3ce076003c282990fd626b6f6a39af9eb780)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putNotificationConfig")
    def put_notification_config(
        self,
        *,
        error_topic: typing.Optional[builtins.str] = None,
        success_topic: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param error_topic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#error_topic SagemakerEndpointConfiguration#error_topic}.
        :param success_topic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#success_topic SagemakerEndpointConfiguration#success_topic}.
        '''
        value = SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfig(
            error_topic=error_topic, success_topic=success_topic
        )

        return typing.cast(None, jsii.invoke(self, "putNotificationConfig", [value]))

    @jsii.member(jsii_name="resetKmsKeyId")
    def reset_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyId", []))

    @jsii.member(jsii_name="resetNotificationConfig")
    def reset_notification_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotificationConfig", []))

    @builtins.property
    @jsii.member(jsii_name="notificationConfig")
    def notification_config(
        self,
    ) -> SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfigOutputReference:
        return typing.cast(SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfigOutputReference, jsii.get(self, "notificationConfig"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdInput")
    def kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationConfigInput")
    def notification_config_input(
        self,
    ) -> typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfig]:
        return typing.cast(typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfig], jsii.get(self, "notificationConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="s3OutputPathInput")
    def s3_output_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3OutputPathInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4817d6f40312171d0c5eac4119498717461b7d3c628039d617d036f646990039)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="s3OutputPath")
    def s3_output_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3OutputPath"))

    @s3_output_path.setter
    def s3_output_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db6e9b82d85631bd309d1fde9299b3aab6cf9d98bb4132c2ca2649f8c7086fdd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3OutputPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfig]:
        return typing.cast(typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0db324c82e5c9ac4a28d390ebaac199e81fe1db8e62db778a25c0dd78785ecc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerEndpointConfigurationAsyncInferenceConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationAsyncInferenceConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6d3a237e1056f74c0c8982eca52f1e319b5f3110bcf13339d0271860fb18399d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putClientConfig")
    def put_client_config(
        self,
        *,
        max_concurrent_invocations_per_instance: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_concurrent_invocations_per_instance: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#max_concurrent_invocations_per_instance SagemakerEndpointConfiguration#max_concurrent_invocations_per_instance}.
        '''
        value = SagemakerEndpointConfigurationAsyncInferenceConfigClientConfig(
            max_concurrent_invocations_per_instance=max_concurrent_invocations_per_instance,
        )

        return typing.cast(None, jsii.invoke(self, "putClientConfig", [value]))

    @jsii.member(jsii_name="putOutputConfig")
    def put_output_config(
        self,
        *,
        s3_output_path: builtins.str,
        kms_key_id: typing.Optional[builtins.str] = None,
        notification_config: typing.Optional[typing.Union[SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param s3_output_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#s3_output_path SagemakerEndpointConfiguration#s3_output_path}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#kms_key_id SagemakerEndpointConfiguration#kms_key_id}.
        :param notification_config: notification_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#notification_config SagemakerEndpointConfiguration#notification_config}
        '''
        value = SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfig(
            s3_output_path=s3_output_path,
            kms_key_id=kms_key_id,
            notification_config=notification_config,
        )

        return typing.cast(None, jsii.invoke(self, "putOutputConfig", [value]))

    @jsii.member(jsii_name="resetClientConfig")
    def reset_client_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientConfig", []))

    @builtins.property
    @jsii.member(jsii_name="clientConfig")
    def client_config(
        self,
    ) -> SagemakerEndpointConfigurationAsyncInferenceConfigClientConfigOutputReference:
        return typing.cast(SagemakerEndpointConfigurationAsyncInferenceConfigClientConfigOutputReference, jsii.get(self, "clientConfig"))

    @builtins.property
    @jsii.member(jsii_name="outputConfig")
    def output_config(
        self,
    ) -> SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigOutputReference:
        return typing.cast(SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigOutputReference, jsii.get(self, "outputConfig"))

    @builtins.property
    @jsii.member(jsii_name="clientConfigInput")
    def client_config_input(
        self,
    ) -> typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfigClientConfig]:
        return typing.cast(typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfigClientConfig], jsii.get(self, "clientConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="outputConfigInput")
    def output_config_input(
        self,
    ) -> typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfig]:
        return typing.cast(typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfig], jsii.get(self, "outputConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfig]:
        return typing.cast(typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f50a225eeb954e1dba1907ffe2637d30b849ff82b88c09b595ed9968a039874)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "production_variants": "productionVariants",
        "async_inference_config": "asyncInferenceConfig",
        "data_capture_config": "dataCaptureConfig",
        "id": "id",
        "kms_key_arn": "kmsKeyArn",
        "name": "name",
        "shadow_production_variants": "shadowProductionVariants",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class SagemakerEndpointConfigurationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        production_variants: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerEndpointConfigurationProductionVariants", typing.Dict[builtins.str, typing.Any]]]],
        async_inference_config: typing.Optional[typing.Union[SagemakerEndpointConfigurationAsyncInferenceConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        data_capture_config: typing.Optional[typing.Union["SagemakerEndpointConfigurationDataCaptureConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        shadow_production_variants: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerEndpointConfigurationShadowProductionVariants", typing.Dict[builtins.str, typing.Any]]]]] = None,
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
        :param production_variants: production_variants block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#production_variants SagemakerEndpointConfiguration#production_variants}
        :param async_inference_config: async_inference_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#async_inference_config SagemakerEndpointConfiguration#async_inference_config}
        :param data_capture_config: data_capture_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#data_capture_config SagemakerEndpointConfiguration#data_capture_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#id SagemakerEndpointConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_key_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#kms_key_arn SagemakerEndpointConfiguration#kms_key_arn}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#name SagemakerEndpointConfiguration#name}.
        :param shadow_production_variants: shadow_production_variants block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#shadow_production_variants SagemakerEndpointConfiguration#shadow_production_variants}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#tags SagemakerEndpointConfiguration#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#tags_all SagemakerEndpointConfiguration#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(async_inference_config, dict):
            async_inference_config = SagemakerEndpointConfigurationAsyncInferenceConfig(**async_inference_config)
        if isinstance(data_capture_config, dict):
            data_capture_config = SagemakerEndpointConfigurationDataCaptureConfig(**data_capture_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afd1a28f339e541b4ef812f91828b16ca301223153d5130a0da4da6bd18ec156)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument production_variants", value=production_variants, expected_type=type_hints["production_variants"])
            check_type(argname="argument async_inference_config", value=async_inference_config, expected_type=type_hints["async_inference_config"])
            check_type(argname="argument data_capture_config", value=data_capture_config, expected_type=type_hints["data_capture_config"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument shadow_production_variants", value=shadow_production_variants, expected_type=type_hints["shadow_production_variants"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "production_variants": production_variants,
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
        if async_inference_config is not None:
            self._values["async_inference_config"] = async_inference_config
        if data_capture_config is not None:
            self._values["data_capture_config"] = data_capture_config
        if id is not None:
            self._values["id"] = id
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if name is not None:
            self._values["name"] = name
        if shadow_production_variants is not None:
            self._values["shadow_production_variants"] = shadow_production_variants
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
    def production_variants(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerEndpointConfigurationProductionVariants"]]:
        '''production_variants block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#production_variants SagemakerEndpointConfiguration#production_variants}
        '''
        result = self._values.get("production_variants")
        assert result is not None, "Required property 'production_variants' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerEndpointConfigurationProductionVariants"]], result)

    @builtins.property
    def async_inference_config(
        self,
    ) -> typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfig]:
        '''async_inference_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#async_inference_config SagemakerEndpointConfiguration#async_inference_config}
        '''
        result = self._values.get("async_inference_config")
        return typing.cast(typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfig], result)

    @builtins.property
    def data_capture_config(
        self,
    ) -> typing.Optional["SagemakerEndpointConfigurationDataCaptureConfig"]:
        '''data_capture_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#data_capture_config SagemakerEndpointConfiguration#data_capture_config}
        '''
        result = self._values.get("data_capture_config")
        return typing.cast(typing.Optional["SagemakerEndpointConfigurationDataCaptureConfig"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#id SagemakerEndpointConfiguration#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#kms_key_arn SagemakerEndpointConfiguration#kms_key_arn}.'''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#name SagemakerEndpointConfiguration#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def shadow_production_variants(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerEndpointConfigurationShadowProductionVariants"]]]:
        '''shadow_production_variants block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#shadow_production_variants SagemakerEndpointConfiguration#shadow_production_variants}
        '''
        result = self._values.get("shadow_production_variants")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerEndpointConfigurationShadowProductionVariants"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#tags SagemakerEndpointConfiguration#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#tags_all SagemakerEndpointConfiguration#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerEndpointConfigurationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationDataCaptureConfig",
    jsii_struct_bases=[],
    name_mapping={
        "capture_options": "captureOptions",
        "destination_s3_uri": "destinationS3Uri",
        "initial_sampling_percentage": "initialSamplingPercentage",
        "capture_content_type_header": "captureContentTypeHeader",
        "enable_capture": "enableCapture",
        "kms_key_id": "kmsKeyId",
    },
)
class SagemakerEndpointConfigurationDataCaptureConfig:
    def __init__(
        self,
        *,
        capture_options: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions", typing.Dict[builtins.str, typing.Any]]]],
        destination_s3_uri: builtins.str,
        initial_sampling_percentage: jsii.Number,
        capture_content_type_header: typing.Optional[typing.Union["SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeader", typing.Dict[builtins.str, typing.Any]]] = None,
        enable_capture: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param capture_options: capture_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#capture_options SagemakerEndpointConfiguration#capture_options}
        :param destination_s3_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#destination_s3_uri SagemakerEndpointConfiguration#destination_s3_uri}.
        :param initial_sampling_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#initial_sampling_percentage SagemakerEndpointConfiguration#initial_sampling_percentage}.
        :param capture_content_type_header: capture_content_type_header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#capture_content_type_header SagemakerEndpointConfiguration#capture_content_type_header}
        :param enable_capture: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#enable_capture SagemakerEndpointConfiguration#enable_capture}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#kms_key_id SagemakerEndpointConfiguration#kms_key_id}.
        '''
        if isinstance(capture_content_type_header, dict):
            capture_content_type_header = SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeader(**capture_content_type_header)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c77a7168af457a969eddb23ffb046b0f42271f40cbff050b3af337cbcfa648e5)
            check_type(argname="argument capture_options", value=capture_options, expected_type=type_hints["capture_options"])
            check_type(argname="argument destination_s3_uri", value=destination_s3_uri, expected_type=type_hints["destination_s3_uri"])
            check_type(argname="argument initial_sampling_percentage", value=initial_sampling_percentage, expected_type=type_hints["initial_sampling_percentage"])
            check_type(argname="argument capture_content_type_header", value=capture_content_type_header, expected_type=type_hints["capture_content_type_header"])
            check_type(argname="argument enable_capture", value=enable_capture, expected_type=type_hints["enable_capture"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "capture_options": capture_options,
            "destination_s3_uri": destination_s3_uri,
            "initial_sampling_percentage": initial_sampling_percentage,
        }
        if capture_content_type_header is not None:
            self._values["capture_content_type_header"] = capture_content_type_header
        if enable_capture is not None:
            self._values["enable_capture"] = enable_capture
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id

    @builtins.property
    def capture_options(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions"]]:
        '''capture_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#capture_options SagemakerEndpointConfiguration#capture_options}
        '''
        result = self._values.get("capture_options")
        assert result is not None, "Required property 'capture_options' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions"]], result)

    @builtins.property
    def destination_s3_uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#destination_s3_uri SagemakerEndpointConfiguration#destination_s3_uri}.'''
        result = self._values.get("destination_s3_uri")
        assert result is not None, "Required property 'destination_s3_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def initial_sampling_percentage(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#initial_sampling_percentage SagemakerEndpointConfiguration#initial_sampling_percentage}.'''
        result = self._values.get("initial_sampling_percentage")
        assert result is not None, "Required property 'initial_sampling_percentage' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def capture_content_type_header(
        self,
    ) -> typing.Optional["SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeader"]:
        '''capture_content_type_header block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#capture_content_type_header SagemakerEndpointConfiguration#capture_content_type_header}
        '''
        result = self._values.get("capture_content_type_header")
        return typing.cast(typing.Optional["SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeader"], result)

    @builtins.property
    def enable_capture(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#enable_capture SagemakerEndpointConfiguration#enable_capture}.'''
        result = self._values.get("enable_capture")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#kms_key_id SagemakerEndpointConfiguration#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerEndpointConfigurationDataCaptureConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeader",
    jsii_struct_bases=[],
    name_mapping={
        "csv_content_types": "csvContentTypes",
        "json_content_types": "jsonContentTypes",
    },
)
class SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeader:
    def __init__(
        self,
        *,
        csv_content_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        json_content_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param csv_content_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#csv_content_types SagemakerEndpointConfiguration#csv_content_types}.
        :param json_content_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#json_content_types SagemakerEndpointConfiguration#json_content_types}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5113145d114f2d11e5974a82aaed3a7d78b76df81c15e69311b5ac0841ae3d60)
            check_type(argname="argument csv_content_types", value=csv_content_types, expected_type=type_hints["csv_content_types"])
            check_type(argname="argument json_content_types", value=json_content_types, expected_type=type_hints["json_content_types"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if csv_content_types is not None:
            self._values["csv_content_types"] = csv_content_types
        if json_content_types is not None:
            self._values["json_content_types"] = json_content_types

    @builtins.property
    def csv_content_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#csv_content_types SagemakerEndpointConfiguration#csv_content_types}.'''
        result = self._values.get("csv_content_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def json_content_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#json_content_types SagemakerEndpointConfiguration#json_content_types}.'''
        result = self._values.get("json_content_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeaderOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeaderOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f2afc3c9090635ba840b4687e6f6e5475c282ab82b25010747f0da20098d9054)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCsvContentTypes")
    def reset_csv_content_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCsvContentTypes", []))

    @jsii.member(jsii_name="resetJsonContentTypes")
    def reset_json_content_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJsonContentTypes", []))

    @builtins.property
    @jsii.member(jsii_name="csvContentTypesInput")
    def csv_content_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "csvContentTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="jsonContentTypesInput")
    def json_content_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "jsonContentTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="csvContentTypes")
    def csv_content_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "csvContentTypes"))

    @csv_content_types.setter
    def csv_content_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62928ba7c4dd54491c7784ddba29b1440c67b66edfdf8705a6149054356a974c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "csvContentTypes", value)

    @builtins.property
    @jsii.member(jsii_name="jsonContentTypes")
    def json_content_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "jsonContentTypes"))

    @json_content_types.setter
    def json_content_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28842314b35cfe2567b015787f92a45a29f06d396cbad0a134bbf921cbcdf515)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jsonContentTypes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeader]:
        return typing.cast(typing.Optional[SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeader], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeader],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a287a94e01471a0b27e625979f94627af4217e56ddde92a143f827eb5b5e255)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions",
    jsii_struct_bases=[],
    name_mapping={"capture_mode": "captureMode"},
)
class SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions:
    def __init__(self, *, capture_mode: builtins.str) -> None:
        '''
        :param capture_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#capture_mode SagemakerEndpointConfiguration#capture_mode}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__439c67936d9ffe9ba3b29b0198384baca3e123c094c5d9f33fdfbf98663b5340)
            check_type(argname="argument capture_mode", value=capture_mode, expected_type=type_hints["capture_mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "capture_mode": capture_mode,
        }

    @builtins.property
    def capture_mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#capture_mode SagemakerEndpointConfiguration#capture_mode}.'''
        result = self._values.get("capture_mode")
        assert result is not None, "Required property 'capture_mode' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerEndpointConfigurationDataCaptureConfigCaptureOptionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationDataCaptureConfigCaptureOptionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__98ad2efa7b89def715d80fb24bd7faa165d1781f8a07b1113e41d3033d7d5481)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SagemakerEndpointConfigurationDataCaptureConfigCaptureOptionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3a7b9ea2a38ffc7c3bd45629a831016c63671d1f623c06b04a667dbe2324bb5)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SagemakerEndpointConfigurationDataCaptureConfigCaptureOptionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87e8905d52a88d903387bf00b6e4b6b4d716c7625bb65b5f42dc95a437f93db0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__464bf976e3645f97a8dbd7682cb6b0579b32ef56b1ca6507cb8c3a4285d6d0a0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__702ab56ec0aa6502d34e4f9b29a703a83cf0c07e65f745985459f2e715613025)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a2183be33a4f50ebed8124f7bc64ab8479320ae3c3cbcc986fd0ca53f7df639)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerEndpointConfigurationDataCaptureConfigCaptureOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationDataCaptureConfigCaptureOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dedb5842ac6f6bfec25738a05f38afab4a266c9fc3c4b0ad9b8a1328b37cb26a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="captureModeInput")
    def capture_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "captureModeInput"))

    @builtins.property
    @jsii.member(jsii_name="captureMode")
    def capture_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "captureMode"))

    @capture_mode.setter
    def capture_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84eeb465ac7e19352554af7630bb591c8a7d2ce6cbcfc2128b20a25b1de2029e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "captureMode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d10680f0970e78147153cb123eabc26dffaddf9b514f1155a59c0191ead95e7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerEndpointConfigurationDataCaptureConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationDataCaptureConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__af7d166f866e7f8d27263554d7cf92de9224719ffbde4a74f924b6fbfb54eaa3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCaptureContentTypeHeader")
    def put_capture_content_type_header(
        self,
        *,
        csv_content_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        json_content_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param csv_content_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#csv_content_types SagemakerEndpointConfiguration#csv_content_types}.
        :param json_content_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#json_content_types SagemakerEndpointConfiguration#json_content_types}.
        '''
        value = SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeader(
            csv_content_types=csv_content_types, json_content_types=json_content_types
        )

        return typing.cast(None, jsii.invoke(self, "putCaptureContentTypeHeader", [value]))

    @jsii.member(jsii_name="putCaptureOptions")
    def put_capture_options(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32cb19851bac7b9c54a8c9ee784c7053557c97d2a646bca001bf0693d34d02b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCaptureOptions", [value]))

    @jsii.member(jsii_name="resetCaptureContentTypeHeader")
    def reset_capture_content_type_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaptureContentTypeHeader", []))

    @jsii.member(jsii_name="resetEnableCapture")
    def reset_enable_capture(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableCapture", []))

    @jsii.member(jsii_name="resetKmsKeyId")
    def reset_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyId", []))

    @builtins.property
    @jsii.member(jsii_name="captureContentTypeHeader")
    def capture_content_type_header(
        self,
    ) -> SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeaderOutputReference:
        return typing.cast(SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeaderOutputReference, jsii.get(self, "captureContentTypeHeader"))

    @builtins.property
    @jsii.member(jsii_name="captureOptions")
    def capture_options(
        self,
    ) -> SagemakerEndpointConfigurationDataCaptureConfigCaptureOptionsList:
        return typing.cast(SagemakerEndpointConfigurationDataCaptureConfigCaptureOptionsList, jsii.get(self, "captureOptions"))

    @builtins.property
    @jsii.member(jsii_name="captureContentTypeHeaderInput")
    def capture_content_type_header_input(
        self,
    ) -> typing.Optional[SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeader]:
        return typing.cast(typing.Optional[SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeader], jsii.get(self, "captureContentTypeHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="captureOptionsInput")
    def capture_options_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions]]], jsii.get(self, "captureOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationS3UriInput")
    def destination_s3_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationS3UriInput"))

    @builtins.property
    @jsii.member(jsii_name="enableCaptureInput")
    def enable_capture_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enableCaptureInput"))

    @builtins.property
    @jsii.member(jsii_name="initialSamplingPercentageInput")
    def initial_sampling_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "initialSamplingPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdInput")
    def kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationS3Uri")
    def destination_s3_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationS3Uri"))

    @destination_s3_uri.setter
    def destination_s3_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56b2928d05489b8ef5005427c6dc0d9557ac5493c9f73f0f61cd93c3662e4561)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationS3Uri", value)

    @builtins.property
    @jsii.member(jsii_name="enableCapture")
    def enable_capture(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enableCapture"))

    @enable_capture.setter
    def enable_capture(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9a0bfc9e121aff1a6a034275fd9364fe099f8f4a9cb7c653917637711521db7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableCapture", value)

    @builtins.property
    @jsii.member(jsii_name="initialSamplingPercentage")
    def initial_sampling_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "initialSamplingPercentage"))

    @initial_sampling_percentage.setter
    def initial_sampling_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8106eb29a94c5f2284356f5f24c1c8706fd6c52a9f89767f16bbeb2368cbee28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialSamplingPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8a31c98312b3314fc8d96ed83ae227f4556d3155e27676a2e4e914e9b036914)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerEndpointConfigurationDataCaptureConfig]:
        return typing.cast(typing.Optional[SagemakerEndpointConfigurationDataCaptureConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerEndpointConfigurationDataCaptureConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ba91bb890af9301e6230cd513093dd31b263c168cd55602302cf5f8d9682715)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationProductionVariants",
    jsii_struct_bases=[],
    name_mapping={
        "model_name": "modelName",
        "accelerator_type": "acceleratorType",
        "container_startup_health_check_timeout_in_seconds": "containerStartupHealthCheckTimeoutInSeconds",
        "core_dump_config": "coreDumpConfig",
        "initial_instance_count": "initialInstanceCount",
        "initial_variant_weight": "initialVariantWeight",
        "instance_type": "instanceType",
        "model_data_download_timeout_in_seconds": "modelDataDownloadTimeoutInSeconds",
        "serverless_config": "serverlessConfig",
        "variant_name": "variantName",
        "volume_size_in_gb": "volumeSizeInGb",
    },
)
class SagemakerEndpointConfigurationProductionVariants:
    def __init__(
        self,
        *,
        model_name: builtins.str,
        accelerator_type: typing.Optional[builtins.str] = None,
        container_startup_health_check_timeout_in_seconds: typing.Optional[jsii.Number] = None,
        core_dump_config: typing.Optional[typing.Union["SagemakerEndpointConfigurationProductionVariantsCoreDumpConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        initial_instance_count: typing.Optional[jsii.Number] = None,
        initial_variant_weight: typing.Optional[jsii.Number] = None,
        instance_type: typing.Optional[builtins.str] = None,
        model_data_download_timeout_in_seconds: typing.Optional[jsii.Number] = None,
        serverless_config: typing.Optional[typing.Union["SagemakerEndpointConfigurationProductionVariantsServerlessConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        variant_name: typing.Optional[builtins.str] = None,
        volume_size_in_gb: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param model_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#model_name SagemakerEndpointConfiguration#model_name}.
        :param accelerator_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#accelerator_type SagemakerEndpointConfiguration#accelerator_type}.
        :param container_startup_health_check_timeout_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#container_startup_health_check_timeout_in_seconds SagemakerEndpointConfiguration#container_startup_health_check_timeout_in_seconds}.
        :param core_dump_config: core_dump_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#core_dump_config SagemakerEndpointConfiguration#core_dump_config}
        :param initial_instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#initial_instance_count SagemakerEndpointConfiguration#initial_instance_count}.
        :param initial_variant_weight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#initial_variant_weight SagemakerEndpointConfiguration#initial_variant_weight}.
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#instance_type SagemakerEndpointConfiguration#instance_type}.
        :param model_data_download_timeout_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#model_data_download_timeout_in_seconds SagemakerEndpointConfiguration#model_data_download_timeout_in_seconds}.
        :param serverless_config: serverless_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#serverless_config SagemakerEndpointConfiguration#serverless_config}
        :param variant_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#variant_name SagemakerEndpointConfiguration#variant_name}.
        :param volume_size_in_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#volume_size_in_gb SagemakerEndpointConfiguration#volume_size_in_gb}.
        '''
        if isinstance(core_dump_config, dict):
            core_dump_config = SagemakerEndpointConfigurationProductionVariantsCoreDumpConfig(**core_dump_config)
        if isinstance(serverless_config, dict):
            serverless_config = SagemakerEndpointConfigurationProductionVariantsServerlessConfig(**serverless_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1590ad4d99afcfdf661ac0c9705742c3ee75a54fb6056f04e82c2b575019fe4)
            check_type(argname="argument model_name", value=model_name, expected_type=type_hints["model_name"])
            check_type(argname="argument accelerator_type", value=accelerator_type, expected_type=type_hints["accelerator_type"])
            check_type(argname="argument container_startup_health_check_timeout_in_seconds", value=container_startup_health_check_timeout_in_seconds, expected_type=type_hints["container_startup_health_check_timeout_in_seconds"])
            check_type(argname="argument core_dump_config", value=core_dump_config, expected_type=type_hints["core_dump_config"])
            check_type(argname="argument initial_instance_count", value=initial_instance_count, expected_type=type_hints["initial_instance_count"])
            check_type(argname="argument initial_variant_weight", value=initial_variant_weight, expected_type=type_hints["initial_variant_weight"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument model_data_download_timeout_in_seconds", value=model_data_download_timeout_in_seconds, expected_type=type_hints["model_data_download_timeout_in_seconds"])
            check_type(argname="argument serverless_config", value=serverless_config, expected_type=type_hints["serverless_config"])
            check_type(argname="argument variant_name", value=variant_name, expected_type=type_hints["variant_name"])
            check_type(argname="argument volume_size_in_gb", value=volume_size_in_gb, expected_type=type_hints["volume_size_in_gb"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "model_name": model_name,
        }
        if accelerator_type is not None:
            self._values["accelerator_type"] = accelerator_type
        if container_startup_health_check_timeout_in_seconds is not None:
            self._values["container_startup_health_check_timeout_in_seconds"] = container_startup_health_check_timeout_in_seconds
        if core_dump_config is not None:
            self._values["core_dump_config"] = core_dump_config
        if initial_instance_count is not None:
            self._values["initial_instance_count"] = initial_instance_count
        if initial_variant_weight is not None:
            self._values["initial_variant_weight"] = initial_variant_weight
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if model_data_download_timeout_in_seconds is not None:
            self._values["model_data_download_timeout_in_seconds"] = model_data_download_timeout_in_seconds
        if serverless_config is not None:
            self._values["serverless_config"] = serverless_config
        if variant_name is not None:
            self._values["variant_name"] = variant_name
        if volume_size_in_gb is not None:
            self._values["volume_size_in_gb"] = volume_size_in_gb

    @builtins.property
    def model_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#model_name SagemakerEndpointConfiguration#model_name}.'''
        result = self._values.get("model_name")
        assert result is not None, "Required property 'model_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def accelerator_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#accelerator_type SagemakerEndpointConfiguration#accelerator_type}.'''
        result = self._values.get("accelerator_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def container_startup_health_check_timeout_in_seconds(
        self,
    ) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#container_startup_health_check_timeout_in_seconds SagemakerEndpointConfiguration#container_startup_health_check_timeout_in_seconds}.'''
        result = self._values.get("container_startup_health_check_timeout_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def core_dump_config(
        self,
    ) -> typing.Optional["SagemakerEndpointConfigurationProductionVariantsCoreDumpConfig"]:
        '''core_dump_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#core_dump_config SagemakerEndpointConfiguration#core_dump_config}
        '''
        result = self._values.get("core_dump_config")
        return typing.cast(typing.Optional["SagemakerEndpointConfigurationProductionVariantsCoreDumpConfig"], result)

    @builtins.property
    def initial_instance_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#initial_instance_count SagemakerEndpointConfiguration#initial_instance_count}.'''
        result = self._values.get("initial_instance_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def initial_variant_weight(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#initial_variant_weight SagemakerEndpointConfiguration#initial_variant_weight}.'''
        result = self._values.get("initial_variant_weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def instance_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#instance_type SagemakerEndpointConfiguration#instance_type}.'''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def model_data_download_timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#model_data_download_timeout_in_seconds SagemakerEndpointConfiguration#model_data_download_timeout_in_seconds}.'''
        result = self._values.get("model_data_download_timeout_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def serverless_config(
        self,
    ) -> typing.Optional["SagemakerEndpointConfigurationProductionVariantsServerlessConfig"]:
        '''serverless_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#serverless_config SagemakerEndpointConfiguration#serverless_config}
        '''
        result = self._values.get("serverless_config")
        return typing.cast(typing.Optional["SagemakerEndpointConfigurationProductionVariantsServerlessConfig"], result)

    @builtins.property
    def variant_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#variant_name SagemakerEndpointConfiguration#variant_name}.'''
        result = self._values.get("variant_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volume_size_in_gb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#volume_size_in_gb SagemakerEndpointConfiguration#volume_size_in_gb}.'''
        result = self._values.get("volume_size_in_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerEndpointConfigurationProductionVariants(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationProductionVariantsCoreDumpConfig",
    jsii_struct_bases=[],
    name_mapping={"destination_s3_uri": "destinationS3Uri", "kms_key_id": "kmsKeyId"},
)
class SagemakerEndpointConfigurationProductionVariantsCoreDumpConfig:
    def __init__(
        self,
        *,
        destination_s3_uri: builtins.str,
        kms_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param destination_s3_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#destination_s3_uri SagemakerEndpointConfiguration#destination_s3_uri}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#kms_key_id SagemakerEndpointConfiguration#kms_key_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65c07563da5be0d7b9d37f934b9b35b0892b8f5a72ab5a1fd87af374d40ce1fd)
            check_type(argname="argument destination_s3_uri", value=destination_s3_uri, expected_type=type_hints["destination_s3_uri"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination_s3_uri": destination_s3_uri,
        }
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id

    @builtins.property
    def destination_s3_uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#destination_s3_uri SagemakerEndpointConfiguration#destination_s3_uri}.'''
        result = self._values.get("destination_s3_uri")
        assert result is not None, "Required property 'destination_s3_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#kms_key_id SagemakerEndpointConfiguration#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerEndpointConfigurationProductionVariantsCoreDumpConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerEndpointConfigurationProductionVariantsCoreDumpConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationProductionVariantsCoreDumpConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c2d9e91917e24ffbbb6b7645370da55a007df43581ad98b4b9fcebfcac6b1039)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKmsKeyId")
    def reset_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyId", []))

    @builtins.property
    @jsii.member(jsii_name="destinationS3UriInput")
    def destination_s3_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationS3UriInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdInput")
    def kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationS3Uri")
    def destination_s3_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationS3Uri"))

    @destination_s3_uri.setter
    def destination_s3_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5ec7729e42859aa0b1c9ac7deeffd8779e235a7b754482c2d4dc9ba3b8f808b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationS3Uri", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__014f3565e28f8ab739895579efa92b7f309dc2200e98bb6c222eece814aa616a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerEndpointConfigurationProductionVariantsCoreDumpConfig]:
        return typing.cast(typing.Optional[SagemakerEndpointConfigurationProductionVariantsCoreDumpConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerEndpointConfigurationProductionVariantsCoreDumpConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cf2715f097879a1ee716515e194c9464e12ff294857c668264b6b004edc98b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerEndpointConfigurationProductionVariantsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationProductionVariantsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3d6e3eae65d35a38e3713939c6569c5e5a15c5dd7897aeeb312c2be9d7d48cbd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SagemakerEndpointConfigurationProductionVariantsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3957f68af4e50057afab0fe19077edf3d14148ef82b0908bc7e77d0620adedc)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SagemakerEndpointConfigurationProductionVariantsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea35346ff81d0223db0df114bbaeba2f56bb5d0d2582277b0c6f5759dd342b7b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__295d5bda2aca64bde9496b0172adb400baa6d8f97e1152b5956fd1a17f8a5c96)
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
            type_hints = typing.get_type_hints(_typecheckingstub__76269b2e67a40089dc4338c4fa867146d358a417ffa95c66cc496e45ae74f1bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerEndpointConfigurationProductionVariants]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerEndpointConfigurationProductionVariants]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerEndpointConfigurationProductionVariants]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70aa0c5fc117916c452e0f555e85c8a4408bb2d5582c473373606c34bde962cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerEndpointConfigurationProductionVariantsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationProductionVariantsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dfcb59d2d6de7b21dba8ac8705e386c93feaa1c5c9b7e45ecb1d8835fb702c00)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCoreDumpConfig")
    def put_core_dump_config(
        self,
        *,
        destination_s3_uri: builtins.str,
        kms_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param destination_s3_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#destination_s3_uri SagemakerEndpointConfiguration#destination_s3_uri}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#kms_key_id SagemakerEndpointConfiguration#kms_key_id}.
        '''
        value = SagemakerEndpointConfigurationProductionVariantsCoreDumpConfig(
            destination_s3_uri=destination_s3_uri, kms_key_id=kms_key_id
        )

        return typing.cast(None, jsii.invoke(self, "putCoreDumpConfig", [value]))

    @jsii.member(jsii_name="putServerlessConfig")
    def put_serverless_config(
        self,
        *,
        max_concurrency: jsii.Number,
        memory_size_in_mb: jsii.Number,
    ) -> None:
        '''
        :param max_concurrency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#max_concurrency SagemakerEndpointConfiguration#max_concurrency}.
        :param memory_size_in_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#memory_size_in_mb SagemakerEndpointConfiguration#memory_size_in_mb}.
        '''
        value = SagemakerEndpointConfigurationProductionVariantsServerlessConfig(
            max_concurrency=max_concurrency, memory_size_in_mb=memory_size_in_mb
        )

        return typing.cast(None, jsii.invoke(self, "putServerlessConfig", [value]))

    @jsii.member(jsii_name="resetAcceleratorType")
    def reset_accelerator_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcceleratorType", []))

    @jsii.member(jsii_name="resetContainerStartupHealthCheckTimeoutInSeconds")
    def reset_container_startup_health_check_timeout_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerStartupHealthCheckTimeoutInSeconds", []))

    @jsii.member(jsii_name="resetCoreDumpConfig")
    def reset_core_dump_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCoreDumpConfig", []))

    @jsii.member(jsii_name="resetInitialInstanceCount")
    def reset_initial_instance_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitialInstanceCount", []))

    @jsii.member(jsii_name="resetInitialVariantWeight")
    def reset_initial_variant_weight(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitialVariantWeight", []))

    @jsii.member(jsii_name="resetInstanceType")
    def reset_instance_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceType", []))

    @jsii.member(jsii_name="resetModelDataDownloadTimeoutInSeconds")
    def reset_model_data_download_timeout_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetModelDataDownloadTimeoutInSeconds", []))

    @jsii.member(jsii_name="resetServerlessConfig")
    def reset_serverless_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerlessConfig", []))

    @jsii.member(jsii_name="resetVariantName")
    def reset_variant_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVariantName", []))

    @jsii.member(jsii_name="resetVolumeSizeInGb")
    def reset_volume_size_in_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeSizeInGb", []))

    @builtins.property
    @jsii.member(jsii_name="coreDumpConfig")
    def core_dump_config(
        self,
    ) -> SagemakerEndpointConfigurationProductionVariantsCoreDumpConfigOutputReference:
        return typing.cast(SagemakerEndpointConfigurationProductionVariantsCoreDumpConfigOutputReference, jsii.get(self, "coreDumpConfig"))

    @builtins.property
    @jsii.member(jsii_name="serverlessConfig")
    def serverless_config(
        self,
    ) -> "SagemakerEndpointConfigurationProductionVariantsServerlessConfigOutputReference":
        return typing.cast("SagemakerEndpointConfigurationProductionVariantsServerlessConfigOutputReference", jsii.get(self, "serverlessConfig"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorTypeInput")
    def accelerator_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "acceleratorTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="containerStartupHealthCheckTimeoutInSecondsInput")
    def container_startup_health_check_timeout_in_seconds_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "containerStartupHealthCheckTimeoutInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="coreDumpConfigInput")
    def core_dump_config_input(
        self,
    ) -> typing.Optional[SagemakerEndpointConfigurationProductionVariantsCoreDumpConfig]:
        return typing.cast(typing.Optional[SagemakerEndpointConfigurationProductionVariantsCoreDumpConfig], jsii.get(self, "coreDumpConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="initialInstanceCountInput")
    def initial_instance_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "initialInstanceCountInput"))

    @builtins.property
    @jsii.member(jsii_name="initialVariantWeightInput")
    def initial_variant_weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "initialVariantWeightInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="modelDataDownloadTimeoutInSecondsInput")
    def model_data_download_timeout_in_seconds_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "modelDataDownloadTimeoutInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="modelNameInput")
    def model_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modelNameInput"))

    @builtins.property
    @jsii.member(jsii_name="serverlessConfigInput")
    def serverless_config_input(
        self,
    ) -> typing.Optional["SagemakerEndpointConfigurationProductionVariantsServerlessConfig"]:
        return typing.cast(typing.Optional["SagemakerEndpointConfigurationProductionVariantsServerlessConfig"], jsii.get(self, "serverlessConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="variantNameInput")
    def variant_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "variantNameInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeSizeInGbInput")
    def volume_size_in_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "volumeSizeInGbInput"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorType")
    def accelerator_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "acceleratorType"))

    @accelerator_type.setter
    def accelerator_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a66d07fdbe417ecceb15e7d1247f7427d1941e18b981b8317ddca8fcc33278a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceleratorType", value)

    @builtins.property
    @jsii.member(jsii_name="containerStartupHealthCheckTimeoutInSeconds")
    def container_startup_health_check_timeout_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "containerStartupHealthCheckTimeoutInSeconds"))

    @container_startup_health_check_timeout_in_seconds.setter
    def container_startup_health_check_timeout_in_seconds(
        self,
        value: jsii.Number,
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90dd659a649b0ae286de4ef8916ac816f9979eab46b358b1ffd251dd6f98a680)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerStartupHealthCheckTimeoutInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="initialInstanceCount")
    def initial_instance_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "initialInstanceCount"))

    @initial_instance_count.setter
    def initial_instance_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96403feeaed1605025837a0fde8f32fd5ac8a1bbc29e730b98b1855189c76d12)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialInstanceCount", value)

    @builtins.property
    @jsii.member(jsii_name="initialVariantWeight")
    def initial_variant_weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "initialVariantWeight"))

    @initial_variant_weight.setter
    def initial_variant_weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c17a3d49fcdc409b50ddcd366946f9629048d3b513a4c7977fbd6280951bd631)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialVariantWeight", value)

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fd5856f170ebe149326ed173298d1380eb11d63ed77a05df07a3377e1c27d9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="modelDataDownloadTimeoutInSeconds")
    def model_data_download_timeout_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "modelDataDownloadTimeoutInSeconds"))

    @model_data_download_timeout_in_seconds.setter
    def model_data_download_timeout_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0b79e3a3e59d748298d5684fea0fe75261e5caaa8ba2e78926b224178c3d97a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modelDataDownloadTimeoutInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="modelName")
    def model_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "modelName"))

    @model_name.setter
    def model_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef6801d39a2f0de88fed7c872ebd72084911c9cec9797dafe57fdda4e3843610)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modelName", value)

    @builtins.property
    @jsii.member(jsii_name="variantName")
    def variant_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "variantName"))

    @variant_name.setter
    def variant_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__927fbe42716b6d9598064f3b11d7edb9b2cdb6024e829bf674e779620f0e2396)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "variantName", value)

    @builtins.property
    @jsii.member(jsii_name="volumeSizeInGb")
    def volume_size_in_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "volumeSizeInGb"))

    @volume_size_in_gb.setter
    def volume_size_in_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a134fd04de0cc7605714414e4fbb3373e411d1f17541baa198604fc9a4a67099)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeSizeInGb", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SagemakerEndpointConfigurationProductionVariants, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SagemakerEndpointConfigurationProductionVariants, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SagemakerEndpointConfigurationProductionVariants, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43e6de920ca90b649410a02cd8035b5eef0f069255bc946efc0c29c8be849ee0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationProductionVariantsServerlessConfig",
    jsii_struct_bases=[],
    name_mapping={
        "max_concurrency": "maxConcurrency",
        "memory_size_in_mb": "memorySizeInMb",
    },
)
class SagemakerEndpointConfigurationProductionVariantsServerlessConfig:
    def __init__(
        self,
        *,
        max_concurrency: jsii.Number,
        memory_size_in_mb: jsii.Number,
    ) -> None:
        '''
        :param max_concurrency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#max_concurrency SagemakerEndpointConfiguration#max_concurrency}.
        :param memory_size_in_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#memory_size_in_mb SagemakerEndpointConfiguration#memory_size_in_mb}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d79cf86f3789536ed9199c805493724ea4bc765b4a91b41caa35e428d8cc80b7)
            check_type(argname="argument max_concurrency", value=max_concurrency, expected_type=type_hints["max_concurrency"])
            check_type(argname="argument memory_size_in_mb", value=memory_size_in_mb, expected_type=type_hints["memory_size_in_mb"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "max_concurrency": max_concurrency,
            "memory_size_in_mb": memory_size_in_mb,
        }

    @builtins.property
    def max_concurrency(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#max_concurrency SagemakerEndpointConfiguration#max_concurrency}.'''
        result = self._values.get("max_concurrency")
        assert result is not None, "Required property 'max_concurrency' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def memory_size_in_mb(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#memory_size_in_mb SagemakerEndpointConfiguration#memory_size_in_mb}.'''
        result = self._values.get("memory_size_in_mb")
        assert result is not None, "Required property 'memory_size_in_mb' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerEndpointConfigurationProductionVariantsServerlessConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerEndpointConfigurationProductionVariantsServerlessConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationProductionVariantsServerlessConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__99f4187061c9f16f23c9059b8062a4c8cd214dad30754c186cdc5508c50ae9ff)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="maxConcurrencyInput")
    def max_concurrency_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConcurrencyInput"))

    @builtins.property
    @jsii.member(jsii_name="memorySizeInMbInput")
    def memory_size_in_mb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memorySizeInMbInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConcurrency")
    def max_concurrency(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConcurrency"))

    @max_concurrency.setter
    def max_concurrency(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e09c8b0eb9bc237e338c95802228875587c20ecb1cb1fdb0fe626d610b8f42d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConcurrency", value)

    @builtins.property
    @jsii.member(jsii_name="memorySizeInMb")
    def memory_size_in_mb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memorySizeInMb"))

    @memory_size_in_mb.setter
    def memory_size_in_mb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ca78818910a5987b29df48a6001b368cb61acc678605cd203dead90cdaf82ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memorySizeInMb", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerEndpointConfigurationProductionVariantsServerlessConfig]:
        return typing.cast(typing.Optional[SagemakerEndpointConfigurationProductionVariantsServerlessConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerEndpointConfigurationProductionVariantsServerlessConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4c0330c9b5eb53b84ac07aeeb8e371bb64a5c44c9f0eee1ce881d6e217988dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationShadowProductionVariants",
    jsii_struct_bases=[],
    name_mapping={
        "model_name": "modelName",
        "accelerator_type": "acceleratorType",
        "container_startup_health_check_timeout_in_seconds": "containerStartupHealthCheckTimeoutInSeconds",
        "core_dump_config": "coreDumpConfig",
        "initial_instance_count": "initialInstanceCount",
        "initial_variant_weight": "initialVariantWeight",
        "instance_type": "instanceType",
        "model_data_download_timeout_in_seconds": "modelDataDownloadTimeoutInSeconds",
        "serverless_config": "serverlessConfig",
        "variant_name": "variantName",
        "volume_size_in_gb": "volumeSizeInGb",
    },
)
class SagemakerEndpointConfigurationShadowProductionVariants:
    def __init__(
        self,
        *,
        model_name: builtins.str,
        accelerator_type: typing.Optional[builtins.str] = None,
        container_startup_health_check_timeout_in_seconds: typing.Optional[jsii.Number] = None,
        core_dump_config: typing.Optional[typing.Union["SagemakerEndpointConfigurationShadowProductionVariantsCoreDumpConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        initial_instance_count: typing.Optional[jsii.Number] = None,
        initial_variant_weight: typing.Optional[jsii.Number] = None,
        instance_type: typing.Optional[builtins.str] = None,
        model_data_download_timeout_in_seconds: typing.Optional[jsii.Number] = None,
        serverless_config: typing.Optional[typing.Union["SagemakerEndpointConfigurationShadowProductionVariantsServerlessConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        variant_name: typing.Optional[builtins.str] = None,
        volume_size_in_gb: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param model_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#model_name SagemakerEndpointConfiguration#model_name}.
        :param accelerator_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#accelerator_type SagemakerEndpointConfiguration#accelerator_type}.
        :param container_startup_health_check_timeout_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#container_startup_health_check_timeout_in_seconds SagemakerEndpointConfiguration#container_startup_health_check_timeout_in_seconds}.
        :param core_dump_config: core_dump_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#core_dump_config SagemakerEndpointConfiguration#core_dump_config}
        :param initial_instance_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#initial_instance_count SagemakerEndpointConfiguration#initial_instance_count}.
        :param initial_variant_weight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#initial_variant_weight SagemakerEndpointConfiguration#initial_variant_weight}.
        :param instance_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#instance_type SagemakerEndpointConfiguration#instance_type}.
        :param model_data_download_timeout_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#model_data_download_timeout_in_seconds SagemakerEndpointConfiguration#model_data_download_timeout_in_seconds}.
        :param serverless_config: serverless_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#serverless_config SagemakerEndpointConfiguration#serverless_config}
        :param variant_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#variant_name SagemakerEndpointConfiguration#variant_name}.
        :param volume_size_in_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#volume_size_in_gb SagemakerEndpointConfiguration#volume_size_in_gb}.
        '''
        if isinstance(core_dump_config, dict):
            core_dump_config = SagemakerEndpointConfigurationShadowProductionVariantsCoreDumpConfig(**core_dump_config)
        if isinstance(serverless_config, dict):
            serverless_config = SagemakerEndpointConfigurationShadowProductionVariantsServerlessConfig(**serverless_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8620c84881829c0dc4e04ed69a8259518892b57b210335dc6b6cb30c65dedeb3)
            check_type(argname="argument model_name", value=model_name, expected_type=type_hints["model_name"])
            check_type(argname="argument accelerator_type", value=accelerator_type, expected_type=type_hints["accelerator_type"])
            check_type(argname="argument container_startup_health_check_timeout_in_seconds", value=container_startup_health_check_timeout_in_seconds, expected_type=type_hints["container_startup_health_check_timeout_in_seconds"])
            check_type(argname="argument core_dump_config", value=core_dump_config, expected_type=type_hints["core_dump_config"])
            check_type(argname="argument initial_instance_count", value=initial_instance_count, expected_type=type_hints["initial_instance_count"])
            check_type(argname="argument initial_variant_weight", value=initial_variant_weight, expected_type=type_hints["initial_variant_weight"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument model_data_download_timeout_in_seconds", value=model_data_download_timeout_in_seconds, expected_type=type_hints["model_data_download_timeout_in_seconds"])
            check_type(argname="argument serverless_config", value=serverless_config, expected_type=type_hints["serverless_config"])
            check_type(argname="argument variant_name", value=variant_name, expected_type=type_hints["variant_name"])
            check_type(argname="argument volume_size_in_gb", value=volume_size_in_gb, expected_type=type_hints["volume_size_in_gb"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "model_name": model_name,
        }
        if accelerator_type is not None:
            self._values["accelerator_type"] = accelerator_type
        if container_startup_health_check_timeout_in_seconds is not None:
            self._values["container_startup_health_check_timeout_in_seconds"] = container_startup_health_check_timeout_in_seconds
        if core_dump_config is not None:
            self._values["core_dump_config"] = core_dump_config
        if initial_instance_count is not None:
            self._values["initial_instance_count"] = initial_instance_count
        if initial_variant_weight is not None:
            self._values["initial_variant_weight"] = initial_variant_weight
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if model_data_download_timeout_in_seconds is not None:
            self._values["model_data_download_timeout_in_seconds"] = model_data_download_timeout_in_seconds
        if serverless_config is not None:
            self._values["serverless_config"] = serverless_config
        if variant_name is not None:
            self._values["variant_name"] = variant_name
        if volume_size_in_gb is not None:
            self._values["volume_size_in_gb"] = volume_size_in_gb

    @builtins.property
    def model_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#model_name SagemakerEndpointConfiguration#model_name}.'''
        result = self._values.get("model_name")
        assert result is not None, "Required property 'model_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def accelerator_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#accelerator_type SagemakerEndpointConfiguration#accelerator_type}.'''
        result = self._values.get("accelerator_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def container_startup_health_check_timeout_in_seconds(
        self,
    ) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#container_startup_health_check_timeout_in_seconds SagemakerEndpointConfiguration#container_startup_health_check_timeout_in_seconds}.'''
        result = self._values.get("container_startup_health_check_timeout_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def core_dump_config(
        self,
    ) -> typing.Optional["SagemakerEndpointConfigurationShadowProductionVariantsCoreDumpConfig"]:
        '''core_dump_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#core_dump_config SagemakerEndpointConfiguration#core_dump_config}
        '''
        result = self._values.get("core_dump_config")
        return typing.cast(typing.Optional["SagemakerEndpointConfigurationShadowProductionVariantsCoreDumpConfig"], result)

    @builtins.property
    def initial_instance_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#initial_instance_count SagemakerEndpointConfiguration#initial_instance_count}.'''
        result = self._values.get("initial_instance_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def initial_variant_weight(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#initial_variant_weight SagemakerEndpointConfiguration#initial_variant_weight}.'''
        result = self._values.get("initial_variant_weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def instance_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#instance_type SagemakerEndpointConfiguration#instance_type}.'''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def model_data_download_timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#model_data_download_timeout_in_seconds SagemakerEndpointConfiguration#model_data_download_timeout_in_seconds}.'''
        result = self._values.get("model_data_download_timeout_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def serverless_config(
        self,
    ) -> typing.Optional["SagemakerEndpointConfigurationShadowProductionVariantsServerlessConfig"]:
        '''serverless_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#serverless_config SagemakerEndpointConfiguration#serverless_config}
        '''
        result = self._values.get("serverless_config")
        return typing.cast(typing.Optional["SagemakerEndpointConfigurationShadowProductionVariantsServerlessConfig"], result)

    @builtins.property
    def variant_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#variant_name SagemakerEndpointConfiguration#variant_name}.'''
        result = self._values.get("variant_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volume_size_in_gb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#volume_size_in_gb SagemakerEndpointConfiguration#volume_size_in_gb}.'''
        result = self._values.get("volume_size_in_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerEndpointConfigurationShadowProductionVariants(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationShadowProductionVariantsCoreDumpConfig",
    jsii_struct_bases=[],
    name_mapping={"destination_s3_uri": "destinationS3Uri", "kms_key_id": "kmsKeyId"},
)
class SagemakerEndpointConfigurationShadowProductionVariantsCoreDumpConfig:
    def __init__(
        self,
        *,
        destination_s3_uri: builtins.str,
        kms_key_id: builtins.str,
    ) -> None:
        '''
        :param destination_s3_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#destination_s3_uri SagemakerEndpointConfiguration#destination_s3_uri}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#kms_key_id SagemakerEndpointConfiguration#kms_key_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25e3bf2c4428e19b1e2e2a895dc108f58542cd69a114a70f85d4644bee27d9c5)
            check_type(argname="argument destination_s3_uri", value=destination_s3_uri, expected_type=type_hints["destination_s3_uri"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination_s3_uri": destination_s3_uri,
            "kms_key_id": kms_key_id,
        }

    @builtins.property
    def destination_s3_uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#destination_s3_uri SagemakerEndpointConfiguration#destination_s3_uri}.'''
        result = self._values.get("destination_s3_uri")
        assert result is not None, "Required property 'destination_s3_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kms_key_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#kms_key_id SagemakerEndpointConfiguration#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        assert result is not None, "Required property 'kms_key_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerEndpointConfigurationShadowProductionVariantsCoreDumpConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerEndpointConfigurationShadowProductionVariantsCoreDumpConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationShadowProductionVariantsCoreDumpConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d1ffdce6403227e13d13857a8fc14ff3ada59f637ea71a44652d053b2ff4ff26)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="destinationS3UriInput")
    def destination_s3_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationS3UriInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdInput")
    def kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationS3Uri")
    def destination_s3_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationS3Uri"))

    @destination_s3_uri.setter
    def destination_s3_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23b3c26539fc085f7498a1d37a6c409e5f1a73bcdc2cd8781e297f68b946dca1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationS3Uri", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41eb0225c8ee95eadb32f9bcb257ab109b4876c846bb1ff0a5f238e7fd0bf80e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerEndpointConfigurationShadowProductionVariantsCoreDumpConfig]:
        return typing.cast(typing.Optional[SagemakerEndpointConfigurationShadowProductionVariantsCoreDumpConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerEndpointConfigurationShadowProductionVariantsCoreDumpConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06ef71c102b3f285d2ce7e2cbf38dd2c697207d552b1c121c2ffebf4bcfa054a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerEndpointConfigurationShadowProductionVariantsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationShadowProductionVariantsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__20246014b1ef63ce69bdaa51448302a6a8423046e45c0c316aeb9b6d9e571e84)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SagemakerEndpointConfigurationShadowProductionVariantsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f662cfb9ce2cbffd687e02311c583dcb5cd6fbfabdabac14808d7b13eb66fa9)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SagemakerEndpointConfigurationShadowProductionVariantsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e11605b80556e3fdfdc477230d0312c583ab6742aff6fbe1eed74dd4ee599adc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4cbfdbe5db9a842670da09cfe30eb6cd9bf943bfa497402a0ebfdb1e4836d522)
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
            type_hints = typing.get_type_hints(_typecheckingstub__062d31ed62efc1aa8a344323eccbce9bd4b3cd3548a475b0152cf39ce03ea4a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerEndpointConfigurationShadowProductionVariants]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerEndpointConfigurationShadowProductionVariants]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerEndpointConfigurationShadowProductionVariants]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00c400187c3fb9894f00f411059f0d8bee87da6798f442a267acbf441baa501b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SagemakerEndpointConfigurationShadowProductionVariantsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationShadowProductionVariantsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9b2e6f60c4cd0acc1068fdc64533f0573a72954dc8347d6390fd3fa87770dc35)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCoreDumpConfig")
    def put_core_dump_config(
        self,
        *,
        destination_s3_uri: builtins.str,
        kms_key_id: builtins.str,
    ) -> None:
        '''
        :param destination_s3_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#destination_s3_uri SagemakerEndpointConfiguration#destination_s3_uri}.
        :param kms_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#kms_key_id SagemakerEndpointConfiguration#kms_key_id}.
        '''
        value = SagemakerEndpointConfigurationShadowProductionVariantsCoreDumpConfig(
            destination_s3_uri=destination_s3_uri, kms_key_id=kms_key_id
        )

        return typing.cast(None, jsii.invoke(self, "putCoreDumpConfig", [value]))

    @jsii.member(jsii_name="putServerlessConfig")
    def put_serverless_config(
        self,
        *,
        max_concurrency: jsii.Number,
        memory_size_in_mb: jsii.Number,
    ) -> None:
        '''
        :param max_concurrency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#max_concurrency SagemakerEndpointConfiguration#max_concurrency}.
        :param memory_size_in_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#memory_size_in_mb SagemakerEndpointConfiguration#memory_size_in_mb}.
        '''
        value = SagemakerEndpointConfigurationShadowProductionVariantsServerlessConfig(
            max_concurrency=max_concurrency, memory_size_in_mb=memory_size_in_mb
        )

        return typing.cast(None, jsii.invoke(self, "putServerlessConfig", [value]))

    @jsii.member(jsii_name="resetAcceleratorType")
    def reset_accelerator_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcceleratorType", []))

    @jsii.member(jsii_name="resetContainerStartupHealthCheckTimeoutInSeconds")
    def reset_container_startup_health_check_timeout_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerStartupHealthCheckTimeoutInSeconds", []))

    @jsii.member(jsii_name="resetCoreDumpConfig")
    def reset_core_dump_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCoreDumpConfig", []))

    @jsii.member(jsii_name="resetInitialInstanceCount")
    def reset_initial_instance_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitialInstanceCount", []))

    @jsii.member(jsii_name="resetInitialVariantWeight")
    def reset_initial_variant_weight(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitialVariantWeight", []))

    @jsii.member(jsii_name="resetInstanceType")
    def reset_instance_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceType", []))

    @jsii.member(jsii_name="resetModelDataDownloadTimeoutInSeconds")
    def reset_model_data_download_timeout_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetModelDataDownloadTimeoutInSeconds", []))

    @jsii.member(jsii_name="resetServerlessConfig")
    def reset_serverless_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerlessConfig", []))

    @jsii.member(jsii_name="resetVariantName")
    def reset_variant_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVariantName", []))

    @jsii.member(jsii_name="resetVolumeSizeInGb")
    def reset_volume_size_in_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeSizeInGb", []))

    @builtins.property
    @jsii.member(jsii_name="coreDumpConfig")
    def core_dump_config(
        self,
    ) -> SagemakerEndpointConfigurationShadowProductionVariantsCoreDumpConfigOutputReference:
        return typing.cast(SagemakerEndpointConfigurationShadowProductionVariantsCoreDumpConfigOutputReference, jsii.get(self, "coreDumpConfig"))

    @builtins.property
    @jsii.member(jsii_name="serverlessConfig")
    def serverless_config(
        self,
    ) -> "SagemakerEndpointConfigurationShadowProductionVariantsServerlessConfigOutputReference":
        return typing.cast("SagemakerEndpointConfigurationShadowProductionVariantsServerlessConfigOutputReference", jsii.get(self, "serverlessConfig"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorTypeInput")
    def accelerator_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "acceleratorTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="containerStartupHealthCheckTimeoutInSecondsInput")
    def container_startup_health_check_timeout_in_seconds_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "containerStartupHealthCheckTimeoutInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="coreDumpConfigInput")
    def core_dump_config_input(
        self,
    ) -> typing.Optional[SagemakerEndpointConfigurationShadowProductionVariantsCoreDumpConfig]:
        return typing.cast(typing.Optional[SagemakerEndpointConfigurationShadowProductionVariantsCoreDumpConfig], jsii.get(self, "coreDumpConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="initialInstanceCountInput")
    def initial_instance_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "initialInstanceCountInput"))

    @builtins.property
    @jsii.member(jsii_name="initialVariantWeightInput")
    def initial_variant_weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "initialVariantWeightInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="modelDataDownloadTimeoutInSecondsInput")
    def model_data_download_timeout_in_seconds_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "modelDataDownloadTimeoutInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="modelNameInput")
    def model_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modelNameInput"))

    @builtins.property
    @jsii.member(jsii_name="serverlessConfigInput")
    def serverless_config_input(
        self,
    ) -> typing.Optional["SagemakerEndpointConfigurationShadowProductionVariantsServerlessConfig"]:
        return typing.cast(typing.Optional["SagemakerEndpointConfigurationShadowProductionVariantsServerlessConfig"], jsii.get(self, "serverlessConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="variantNameInput")
    def variant_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "variantNameInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeSizeInGbInput")
    def volume_size_in_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "volumeSizeInGbInput"))

    @builtins.property
    @jsii.member(jsii_name="acceleratorType")
    def accelerator_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "acceleratorType"))

    @accelerator_type.setter
    def accelerator_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7eca50798dbc26a373b72203cf4a4a8ed5208640c7bf81be59bfe67dccd9bdf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceleratorType", value)

    @builtins.property
    @jsii.member(jsii_name="containerStartupHealthCheckTimeoutInSeconds")
    def container_startup_health_check_timeout_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "containerStartupHealthCheckTimeoutInSeconds"))

    @container_startup_health_check_timeout_in_seconds.setter
    def container_startup_health_check_timeout_in_seconds(
        self,
        value: jsii.Number,
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e46d37a02b7f5d1892785a6d76a38336837d84a921c106d9345ab7334995dc5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerStartupHealthCheckTimeoutInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="initialInstanceCount")
    def initial_instance_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "initialInstanceCount"))

    @initial_instance_count.setter
    def initial_instance_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69977ac8a2b1d25b9b259268bca07a4a0b668d97ccbec54b416d3d6eae4e89aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialInstanceCount", value)

    @builtins.property
    @jsii.member(jsii_name="initialVariantWeight")
    def initial_variant_weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "initialVariantWeight"))

    @initial_variant_weight.setter
    def initial_variant_weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a59cfb9661ad503edea5f33cda5146fb995b11521bf35cf9516b10acf56f3d9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialVariantWeight", value)

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29cb19dca9ae751df6290d805c4693a60a5f572ca83d903cf1dfaa64ea30bf6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="modelDataDownloadTimeoutInSeconds")
    def model_data_download_timeout_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "modelDataDownloadTimeoutInSeconds"))

    @model_data_download_timeout_in_seconds.setter
    def model_data_download_timeout_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__158af2476bdd9c7366fa43a3cccf56ecfacf27193e523bf458129674bfe0fc46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modelDataDownloadTimeoutInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="modelName")
    def model_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "modelName"))

    @model_name.setter
    def model_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a87ff0a881fd8ff26e943fe250e0a2da570b62f49251d8ff4dcc4564277312d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modelName", value)

    @builtins.property
    @jsii.member(jsii_name="variantName")
    def variant_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "variantName"))

    @variant_name.setter
    def variant_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__498f156971d2c31cb1c1a9380fdb535f1debecbb6779c6f68bb56126f325b988)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "variantName", value)

    @builtins.property
    @jsii.member(jsii_name="volumeSizeInGb")
    def volume_size_in_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "volumeSizeInGb"))

    @volume_size_in_gb.setter
    def volume_size_in_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ffe2e418b93fef1d4e5ee9a130973b0811dab7fe37a91131fc9dd51cad4adea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeSizeInGb", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SagemakerEndpointConfigurationShadowProductionVariants, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SagemakerEndpointConfigurationShadowProductionVariants, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SagemakerEndpointConfigurationShadowProductionVariants, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40cf18a7ee609f35d3e55f1b637e12386582247d6701b61362ab3ca3490fe837)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationShadowProductionVariantsServerlessConfig",
    jsii_struct_bases=[],
    name_mapping={
        "max_concurrency": "maxConcurrency",
        "memory_size_in_mb": "memorySizeInMb",
    },
)
class SagemakerEndpointConfigurationShadowProductionVariantsServerlessConfig:
    def __init__(
        self,
        *,
        max_concurrency: jsii.Number,
        memory_size_in_mb: jsii.Number,
    ) -> None:
        '''
        :param max_concurrency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#max_concurrency SagemakerEndpointConfiguration#max_concurrency}.
        :param memory_size_in_mb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#memory_size_in_mb SagemakerEndpointConfiguration#memory_size_in_mb}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a7e4f6e016c62f6dd9c513e51a0397f334b5cf87719e7d695b53f4ed57529f4)
            check_type(argname="argument max_concurrency", value=max_concurrency, expected_type=type_hints["max_concurrency"])
            check_type(argname="argument memory_size_in_mb", value=memory_size_in_mb, expected_type=type_hints["memory_size_in_mb"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "max_concurrency": max_concurrency,
            "memory_size_in_mb": memory_size_in_mb,
        }

    @builtins.property
    def max_concurrency(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#max_concurrency SagemakerEndpointConfiguration#max_concurrency}.'''
        result = self._values.get("max_concurrency")
        assert result is not None, "Required property 'max_concurrency' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def memory_size_in_mb(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sagemaker_endpoint_configuration#memory_size_in_mb SagemakerEndpointConfiguration#memory_size_in_mb}.'''
        result = self._values.get("memory_size_in_mb")
        assert result is not None, "Required property 'memory_size_in_mb' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerEndpointConfigurationShadowProductionVariantsServerlessConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerEndpointConfigurationShadowProductionVariantsServerlessConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerEndpointConfiguration.SagemakerEndpointConfigurationShadowProductionVariantsServerlessConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__86193b934485b3da7f11864a64e570f2f82ef18e85658d051b8b6c6dad6d2657)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="maxConcurrencyInput")
    def max_concurrency_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConcurrencyInput"))

    @builtins.property
    @jsii.member(jsii_name="memorySizeInMbInput")
    def memory_size_in_mb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memorySizeInMbInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConcurrency")
    def max_concurrency(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConcurrency"))

    @max_concurrency.setter
    def max_concurrency(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb6804faa31e25ed10254a4f05c2f2182eee56b2bb7ae2d1eceb4001512a671b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConcurrency", value)

    @builtins.property
    @jsii.member(jsii_name="memorySizeInMb")
    def memory_size_in_mb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "memorySizeInMb"))

    @memory_size_in_mb.setter
    def memory_size_in_mb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf6ef2dd00c729d913e0ab1cb953c4f7a1cc36a78c5c9093468ac91de5603285)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memorySizeInMb", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerEndpointConfigurationShadowProductionVariantsServerlessConfig]:
        return typing.cast(typing.Optional[SagemakerEndpointConfigurationShadowProductionVariantsServerlessConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerEndpointConfigurationShadowProductionVariantsServerlessConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e5b12765d798c4c41ef62b4ec12f8a3fd2fd9f2eeac9393d01948a07160d723)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SagemakerEndpointConfiguration",
    "SagemakerEndpointConfigurationAsyncInferenceConfig",
    "SagemakerEndpointConfigurationAsyncInferenceConfigClientConfig",
    "SagemakerEndpointConfigurationAsyncInferenceConfigClientConfigOutputReference",
    "SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfig",
    "SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfig",
    "SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfigOutputReference",
    "SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigOutputReference",
    "SagemakerEndpointConfigurationAsyncInferenceConfigOutputReference",
    "SagemakerEndpointConfigurationConfig",
    "SagemakerEndpointConfigurationDataCaptureConfig",
    "SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeader",
    "SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeaderOutputReference",
    "SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions",
    "SagemakerEndpointConfigurationDataCaptureConfigCaptureOptionsList",
    "SagemakerEndpointConfigurationDataCaptureConfigCaptureOptionsOutputReference",
    "SagemakerEndpointConfigurationDataCaptureConfigOutputReference",
    "SagemakerEndpointConfigurationProductionVariants",
    "SagemakerEndpointConfigurationProductionVariantsCoreDumpConfig",
    "SagemakerEndpointConfigurationProductionVariantsCoreDumpConfigOutputReference",
    "SagemakerEndpointConfigurationProductionVariantsList",
    "SagemakerEndpointConfigurationProductionVariantsOutputReference",
    "SagemakerEndpointConfigurationProductionVariantsServerlessConfig",
    "SagemakerEndpointConfigurationProductionVariantsServerlessConfigOutputReference",
    "SagemakerEndpointConfigurationShadowProductionVariants",
    "SagemakerEndpointConfigurationShadowProductionVariantsCoreDumpConfig",
    "SagemakerEndpointConfigurationShadowProductionVariantsCoreDumpConfigOutputReference",
    "SagemakerEndpointConfigurationShadowProductionVariantsList",
    "SagemakerEndpointConfigurationShadowProductionVariantsOutputReference",
    "SagemakerEndpointConfigurationShadowProductionVariantsServerlessConfig",
    "SagemakerEndpointConfigurationShadowProductionVariantsServerlessConfigOutputReference",
]

publication.publish()

def _typecheckingstub__4be27fd33f6ca8cfded9c63cf2f0e11ba33858234266caaeddfef9c5a5eafe0a(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    production_variants: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerEndpointConfigurationProductionVariants, typing.Dict[builtins.str, typing.Any]]]],
    async_inference_config: typing.Optional[typing.Union[SagemakerEndpointConfigurationAsyncInferenceConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    data_capture_config: typing.Optional[typing.Union[SagemakerEndpointConfigurationDataCaptureConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    shadow_production_variants: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerEndpointConfigurationShadowProductionVariants, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__a8d09c25f9a289e1d40426eebfcdf0a16198c74a85226ee70d2d489219d51c01(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerEndpointConfigurationProductionVariants, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34f289e51de2a03a9130b3296541775b1afae748d61598c7d22e9cf1143d55d5(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerEndpointConfigurationShadowProductionVariants, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db55fa2c0ef90babc07a7d2623012644d0180dbf70ef6a13dbb44f0842b21ce1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5669263d6685ec022434a20eeb465361cab572a72351fc912e26de4dd11eb9ac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f639271930c9147bc101de37b80919a1755a00db29aa154dd9d498b253ba882d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8f6d4a70f0c1a278e196d3ea7c0aea4912c8c362082b6b6cb1800e7d1dc2802(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e200d299ccf100a6b77ed93b23acada33d25181bc1855654ee2f6c18d518cfbf(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc1d0f1f4fd1ffe8062d4afc81d072f67940df58fec23dac5f0d882373b48523(
    *,
    output_config: typing.Union[SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfig, typing.Dict[builtins.str, typing.Any]],
    client_config: typing.Optional[typing.Union[SagemakerEndpointConfigurationAsyncInferenceConfigClientConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f500801de7ed52609bff6712be2f08df5d0f64178cda1f54b46057387ce94cf2(
    *,
    max_concurrent_invocations_per_instance: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e96d3c1e1750f4f552c1a98fb44a8dc052caf6c23dba988750f0c7ba7756eea1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11297debb79c74e9d9b60d5d1c065af6611aa155c162a724c4b21dadf5ce1eb0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4817601952ff59c7e4573004eb22a2e43ceb1aa25a413548bbe9b8868917f366(
    value: typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfigClientConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cee4d90101ebf83952184e0212e035cbdaba2d42dfeab85ed41fb06ed260387e(
    *,
    s3_output_path: builtins.str,
    kms_key_id: typing.Optional[builtins.str] = None,
    notification_config: typing.Optional[typing.Union[SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__748f9e2d8411fdd49b8b1b8b7d27e4451d5717b9a208c5ef298403288042a828(
    *,
    error_topic: typing.Optional[builtins.str] = None,
    success_topic: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e57c10dce10eef07eff5028967a2b0ffed5548e40b0a8e65259ee1def72486ac(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0022f7a8bd27c19718c9f713472a8532c2c0c6e7e758eb60a70b90299e3e4b44(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d43cc8d5c05b755455448c2cfd045f048d5692590219490b907fcc0e1bacadd0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77d1f7edf5605e05d2bd640e45419a1a1fc92edbdb1ae527335a5fbb80c8063c(
    value: typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfigNotificationConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95ea2adb1f38ad212e14aad10b8d3ce076003c282990fd626b6f6a39af9eb780(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4817d6f40312171d0c5eac4119498717461b7d3c628039d617d036f646990039(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db6e9b82d85631bd309d1fde9299b3aab6cf9d98bb4132c2ca2649f8c7086fdd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0db324c82e5c9ac4a28d390ebaac199e81fe1db8e62db778a25c0dd78785ecc(
    value: typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfigOutputConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d3a237e1056f74c0c8982eca52f1e319b5f3110bcf13339d0271860fb18399d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f50a225eeb954e1dba1907ffe2637d30b849ff82b88c09b595ed9968a039874(
    value: typing.Optional[SagemakerEndpointConfigurationAsyncInferenceConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afd1a28f339e541b4ef812f91828b16ca301223153d5130a0da4da6bd18ec156(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    production_variants: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerEndpointConfigurationProductionVariants, typing.Dict[builtins.str, typing.Any]]]],
    async_inference_config: typing.Optional[typing.Union[SagemakerEndpointConfigurationAsyncInferenceConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    data_capture_config: typing.Optional[typing.Union[SagemakerEndpointConfigurationDataCaptureConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    shadow_production_variants: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerEndpointConfigurationShadowProductionVariants, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c77a7168af457a969eddb23ffb046b0f42271f40cbff050b3af337cbcfa648e5(
    *,
    capture_options: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions, typing.Dict[builtins.str, typing.Any]]]],
    destination_s3_uri: builtins.str,
    initial_sampling_percentage: jsii.Number,
    capture_content_type_header: typing.Optional[typing.Union[SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeader, typing.Dict[builtins.str, typing.Any]]] = None,
    enable_capture: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5113145d114f2d11e5974a82aaed3a7d78b76df81c15e69311b5ac0841ae3d60(
    *,
    csv_content_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    json_content_types: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2afc3c9090635ba840b4687e6f6e5475c282ab82b25010747f0da20098d9054(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62928ba7c4dd54491c7784ddba29b1440c67b66edfdf8705a6149054356a974c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28842314b35cfe2567b015787f92a45a29f06d396cbad0a134bbf921cbcdf515(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a287a94e01471a0b27e625979f94627af4217e56ddde92a143f827eb5b5e255(
    value: typing.Optional[SagemakerEndpointConfigurationDataCaptureConfigCaptureContentTypeHeader],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__439c67936d9ffe9ba3b29b0198384baca3e123c094c5d9f33fdfbf98663b5340(
    *,
    capture_mode: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98ad2efa7b89def715d80fb24bd7faa165d1781f8a07b1113e41d3033d7d5481(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3a7b9ea2a38ffc7c3bd45629a831016c63671d1f623c06b04a667dbe2324bb5(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87e8905d52a88d903387bf00b6e4b6b4d716c7625bb65b5f42dc95a437f93db0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__464bf976e3645f97a8dbd7682cb6b0579b32ef56b1ca6507cb8c3a4285d6d0a0(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__702ab56ec0aa6502d34e4f9b29a703a83cf0c07e65f745985459f2e715613025(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a2183be33a4f50ebed8124f7bc64ab8479320ae3c3cbcc986fd0ca53f7df639(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dedb5842ac6f6bfec25738a05f38afab4a266c9fc3c4b0ad9b8a1328b37cb26a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84eeb465ac7e19352554af7630bb591c8a7d2ce6cbcfc2128b20a25b1de2029e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d10680f0970e78147153cb123eabc26dffaddf9b514f1155a59c0191ead95e7c(
    value: typing.Optional[typing.Union[SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af7d166f866e7f8d27263554d7cf92de9224719ffbde4a74f924b6fbfb54eaa3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32cb19851bac7b9c54a8c9ee784c7053557c97d2a646bca001bf0693d34d02b1(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerEndpointConfigurationDataCaptureConfigCaptureOptions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56b2928d05489b8ef5005427c6dc0d9557ac5493c9f73f0f61cd93c3662e4561(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9a0bfc9e121aff1a6a034275fd9364fe099f8f4a9cb7c653917637711521db7(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8106eb29a94c5f2284356f5f24c1c8706fd6c52a9f89767f16bbeb2368cbee28(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8a31c98312b3314fc8d96ed83ae227f4556d3155e27676a2e4e914e9b036914(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ba91bb890af9301e6230cd513093dd31b263c168cd55602302cf5f8d9682715(
    value: typing.Optional[SagemakerEndpointConfigurationDataCaptureConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1590ad4d99afcfdf661ac0c9705742c3ee75a54fb6056f04e82c2b575019fe4(
    *,
    model_name: builtins.str,
    accelerator_type: typing.Optional[builtins.str] = None,
    container_startup_health_check_timeout_in_seconds: typing.Optional[jsii.Number] = None,
    core_dump_config: typing.Optional[typing.Union[SagemakerEndpointConfigurationProductionVariantsCoreDumpConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    initial_instance_count: typing.Optional[jsii.Number] = None,
    initial_variant_weight: typing.Optional[jsii.Number] = None,
    instance_type: typing.Optional[builtins.str] = None,
    model_data_download_timeout_in_seconds: typing.Optional[jsii.Number] = None,
    serverless_config: typing.Optional[typing.Union[SagemakerEndpointConfigurationProductionVariantsServerlessConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    variant_name: typing.Optional[builtins.str] = None,
    volume_size_in_gb: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65c07563da5be0d7b9d37f934b9b35b0892b8f5a72ab5a1fd87af374d40ce1fd(
    *,
    destination_s3_uri: builtins.str,
    kms_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2d9e91917e24ffbbb6b7645370da55a007df43581ad98b4b9fcebfcac6b1039(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5ec7729e42859aa0b1c9ac7deeffd8779e235a7b754482c2d4dc9ba3b8f808b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__014f3565e28f8ab739895579efa92b7f309dc2200e98bb6c222eece814aa616a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cf2715f097879a1ee716515e194c9464e12ff294857c668264b6b004edc98b6(
    value: typing.Optional[SagemakerEndpointConfigurationProductionVariantsCoreDumpConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d6e3eae65d35a38e3713939c6569c5e5a15c5dd7897aeeb312c2be9d7d48cbd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3957f68af4e50057afab0fe19077edf3d14148ef82b0908bc7e77d0620adedc(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea35346ff81d0223db0df114bbaeba2f56bb5d0d2582277b0c6f5759dd342b7b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__295d5bda2aca64bde9496b0172adb400baa6d8f97e1152b5956fd1a17f8a5c96(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76269b2e67a40089dc4338c4fa867146d358a417ffa95c66cc496e45ae74f1bd(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70aa0c5fc117916c452e0f555e85c8a4408bb2d5582c473373606c34bde962cb(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerEndpointConfigurationProductionVariants]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfcb59d2d6de7b21dba8ac8705e386c93feaa1c5c9b7e45ecb1d8835fb702c00(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a66d07fdbe417ecceb15e7d1247f7427d1941e18b981b8317ddca8fcc33278a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90dd659a649b0ae286de4ef8916ac816f9979eab46b358b1ffd251dd6f98a680(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96403feeaed1605025837a0fde8f32fd5ac8a1bbc29e730b98b1855189c76d12(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c17a3d49fcdc409b50ddcd366946f9629048d3b513a4c7977fbd6280951bd631(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fd5856f170ebe149326ed173298d1380eb11d63ed77a05df07a3377e1c27d9e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0b79e3a3e59d748298d5684fea0fe75261e5caaa8ba2e78926b224178c3d97a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef6801d39a2f0de88fed7c872ebd72084911c9cec9797dafe57fdda4e3843610(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__927fbe42716b6d9598064f3b11d7edb9b2cdb6024e829bf674e779620f0e2396(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a134fd04de0cc7605714414e4fbb3373e411d1f17541baa198604fc9a4a67099(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43e6de920ca90b649410a02cd8035b5eef0f069255bc946efc0c29c8be849ee0(
    value: typing.Optional[typing.Union[SagemakerEndpointConfigurationProductionVariants, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d79cf86f3789536ed9199c805493724ea4bc765b4a91b41caa35e428d8cc80b7(
    *,
    max_concurrency: jsii.Number,
    memory_size_in_mb: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99f4187061c9f16f23c9059b8062a4c8cd214dad30754c186cdc5508c50ae9ff(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e09c8b0eb9bc237e338c95802228875587c20ecb1cb1fdb0fe626d610b8f42d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ca78818910a5987b29df48a6001b368cb61acc678605cd203dead90cdaf82ee(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4c0330c9b5eb53b84ac07aeeb8e371bb64a5c44c9f0eee1ce881d6e217988dc(
    value: typing.Optional[SagemakerEndpointConfigurationProductionVariantsServerlessConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8620c84881829c0dc4e04ed69a8259518892b57b210335dc6b6cb30c65dedeb3(
    *,
    model_name: builtins.str,
    accelerator_type: typing.Optional[builtins.str] = None,
    container_startup_health_check_timeout_in_seconds: typing.Optional[jsii.Number] = None,
    core_dump_config: typing.Optional[typing.Union[SagemakerEndpointConfigurationShadowProductionVariantsCoreDumpConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    initial_instance_count: typing.Optional[jsii.Number] = None,
    initial_variant_weight: typing.Optional[jsii.Number] = None,
    instance_type: typing.Optional[builtins.str] = None,
    model_data_download_timeout_in_seconds: typing.Optional[jsii.Number] = None,
    serverless_config: typing.Optional[typing.Union[SagemakerEndpointConfigurationShadowProductionVariantsServerlessConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    variant_name: typing.Optional[builtins.str] = None,
    volume_size_in_gb: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25e3bf2c4428e19b1e2e2a895dc108f58542cd69a114a70f85d4644bee27d9c5(
    *,
    destination_s3_uri: builtins.str,
    kms_key_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1ffdce6403227e13d13857a8fc14ff3ada59f637ea71a44652d053b2ff4ff26(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23b3c26539fc085f7498a1d37a6c409e5f1a73bcdc2cd8781e297f68b946dca1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41eb0225c8ee95eadb32f9bcb257ab109b4876c846bb1ff0a5f238e7fd0bf80e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06ef71c102b3f285d2ce7e2cbf38dd2c697207d552b1c121c2ffebf4bcfa054a(
    value: typing.Optional[SagemakerEndpointConfigurationShadowProductionVariantsCoreDumpConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20246014b1ef63ce69bdaa51448302a6a8423046e45c0c316aeb9b6d9e571e84(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f662cfb9ce2cbffd687e02311c583dcb5cd6fbfabdabac14808d7b13eb66fa9(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e11605b80556e3fdfdc477230d0312c583ab6742aff6fbe1eed74dd4ee599adc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cbfdbe5db9a842670da09cfe30eb6cd9bf943bfa497402a0ebfdb1e4836d522(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__062d31ed62efc1aa8a344323eccbce9bd4b3cd3548a475b0152cf39ce03ea4a0(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00c400187c3fb9894f00f411059f0d8bee87da6798f442a267acbf441baa501b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerEndpointConfigurationShadowProductionVariants]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b2e6f60c4cd0acc1068fdc64533f0573a72954dc8347d6390fd3fa87770dc35(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7eca50798dbc26a373b72203cf4a4a8ed5208640c7bf81be59bfe67dccd9bdf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e46d37a02b7f5d1892785a6d76a38336837d84a921c106d9345ab7334995dc5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69977ac8a2b1d25b9b259268bca07a4a0b668d97ccbec54b416d3d6eae4e89aa(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a59cfb9661ad503edea5f33cda5146fb995b11521bf35cf9516b10acf56f3d9c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29cb19dca9ae751df6290d805c4693a60a5f572ca83d903cf1dfaa64ea30bf6b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__158af2476bdd9c7366fa43a3cccf56ecfacf27193e523bf458129674bfe0fc46(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a87ff0a881fd8ff26e943fe250e0a2da570b62f49251d8ff4dcc4564277312d6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__498f156971d2c31cb1c1a9380fdb535f1debecbb6779c6f68bb56126f325b988(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ffe2e418b93fef1d4e5ee9a130973b0811dab7fe37a91131fc9dd51cad4adea(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40cf18a7ee609f35d3e55f1b637e12386582247d6701b61362ab3ca3490fe837(
    value: typing.Optional[typing.Union[SagemakerEndpointConfigurationShadowProductionVariants, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a7e4f6e016c62f6dd9c513e51a0397f334b5cf87719e7d695b53f4ed57529f4(
    *,
    max_concurrency: jsii.Number,
    memory_size_in_mb: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86193b934485b3da7f11864a64e570f2f82ef18e85658d051b8b6c6dad6d2657(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb6804faa31e25ed10254a4f05c2f2182eee56b2bb7ae2d1eceb4001512a671b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf6ef2dd00c729d913e0ab1cb953c4f7a1cc36a78c5c9093468ac91de5603285(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e5b12765d798c4c41ef62b4ec12f8a3fd2fd9f2eeac9393d01948a07160d723(
    value: typing.Optional[SagemakerEndpointConfigurationShadowProductionVariantsServerlessConfig],
) -> None:
    """Type checking stubs"""
    pass
