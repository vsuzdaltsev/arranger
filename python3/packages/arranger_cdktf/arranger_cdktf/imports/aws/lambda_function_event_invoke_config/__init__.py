'''
# `aws_lambda_function_event_invoke_config`

Refer to the Terraform Registory for docs: [`aws_lambda_function_event_invoke_config`](https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config).
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


class LambdaFunctionEventInvokeConfig(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lambdaFunctionEventInvokeConfig.LambdaFunctionEventInvokeConfig",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config aws_lambda_function_event_invoke_config}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        function_name: builtins.str,
        destination_config: typing.Optional[typing.Union["LambdaFunctionEventInvokeConfigDestinationConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        maximum_event_age_in_seconds: typing.Optional[jsii.Number] = None,
        maximum_retry_attempts: typing.Optional[jsii.Number] = None,
        qualifier: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config aws_lambda_function_event_invoke_config} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param function_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#function_name LambdaFunctionEventInvokeConfig#function_name}.
        :param destination_config: destination_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#destination_config LambdaFunctionEventInvokeConfig#destination_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#id LambdaFunctionEventInvokeConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param maximum_event_age_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#maximum_event_age_in_seconds LambdaFunctionEventInvokeConfig#maximum_event_age_in_seconds}.
        :param maximum_retry_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#maximum_retry_attempts LambdaFunctionEventInvokeConfig#maximum_retry_attempts}.
        :param qualifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#qualifier LambdaFunctionEventInvokeConfig#qualifier}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f2884c5b362c0bff65c631cb246c43f63d73c5cbc92468792ce29cbfb543fe4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LambdaFunctionEventInvokeConfigConfig(
            function_name=function_name,
            destination_config=destination_config,
            id=id,
            maximum_event_age_in_seconds=maximum_event_age_in_seconds,
            maximum_retry_attempts=maximum_retry_attempts,
            qualifier=qualifier,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putDestinationConfig")
    def put_destination_config(
        self,
        *,
        on_failure: typing.Optional[typing.Union["LambdaFunctionEventInvokeConfigDestinationConfigOnFailure", typing.Dict[builtins.str, typing.Any]]] = None,
        on_success: typing.Optional[typing.Union["LambdaFunctionEventInvokeConfigDestinationConfigOnSuccess", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param on_failure: on_failure block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#on_failure LambdaFunctionEventInvokeConfig#on_failure}
        :param on_success: on_success block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#on_success LambdaFunctionEventInvokeConfig#on_success}
        '''
        value = LambdaFunctionEventInvokeConfigDestinationConfig(
            on_failure=on_failure, on_success=on_success
        )

        return typing.cast(None, jsii.invoke(self, "putDestinationConfig", [value]))

    @jsii.member(jsii_name="resetDestinationConfig")
    def reset_destination_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationConfig", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMaximumEventAgeInSeconds")
    def reset_maximum_event_age_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximumEventAgeInSeconds", []))

    @jsii.member(jsii_name="resetMaximumRetryAttempts")
    def reset_maximum_retry_attempts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximumRetryAttempts", []))

    @jsii.member(jsii_name="resetQualifier")
    def reset_qualifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQualifier", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="destinationConfig")
    def destination_config(
        self,
    ) -> "LambdaFunctionEventInvokeConfigDestinationConfigOutputReference":
        return typing.cast("LambdaFunctionEventInvokeConfigDestinationConfigOutputReference", jsii.get(self, "destinationConfig"))

    @builtins.property
    @jsii.member(jsii_name="destinationConfigInput")
    def destination_config_input(
        self,
    ) -> typing.Optional["LambdaFunctionEventInvokeConfigDestinationConfig"]:
        return typing.cast(typing.Optional["LambdaFunctionEventInvokeConfigDestinationConfig"], jsii.get(self, "destinationConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="functionNameInput")
    def function_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "functionNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumEventAgeInSecondsInput")
    def maximum_event_age_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumEventAgeInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumRetryAttemptsInput")
    def maximum_retry_attempts_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumRetryAttemptsInput"))

    @builtins.property
    @jsii.member(jsii_name="qualifierInput")
    def qualifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "qualifierInput"))

    @builtins.property
    @jsii.member(jsii_name="functionName")
    def function_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "functionName"))

    @function_name.setter
    def function_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68e690d73f5b6f945d20cb3f9a95a24652e046e01adda69d59ad9336db19f642)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functionName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4690f61914c54b2a2d4321a91305da17f18b35fd328a317a628ed4b039a56e09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="maximumEventAgeInSeconds")
    def maximum_event_age_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumEventAgeInSeconds"))

    @maximum_event_age_in_seconds.setter
    def maximum_event_age_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c2a2d9280e5c11ede46eb0a47b5e83ea39eebdb0c69a8fbea0b9852c6460ea0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumEventAgeInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="maximumRetryAttempts")
    def maximum_retry_attempts(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumRetryAttempts"))

    @maximum_retry_attempts.setter
    def maximum_retry_attempts(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d686375acc1b721a9b9109f1ced3701d59a0517fd90e22d70eda3d1e1a0cb9c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumRetryAttempts", value)

    @builtins.property
    @jsii.member(jsii_name="qualifier")
    def qualifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "qualifier"))

    @qualifier.setter
    def qualifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e767caf1b94e64291c9e5a05c98a6c468c8c8ff0eb5e4ac5b6564c50e974ef4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "qualifier", value)


@jsii.data_type(
    jsii_type="aws.lambdaFunctionEventInvokeConfig.LambdaFunctionEventInvokeConfigConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "function_name": "functionName",
        "destination_config": "destinationConfig",
        "id": "id",
        "maximum_event_age_in_seconds": "maximumEventAgeInSeconds",
        "maximum_retry_attempts": "maximumRetryAttempts",
        "qualifier": "qualifier",
    },
)
class LambdaFunctionEventInvokeConfigConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        function_name: builtins.str,
        destination_config: typing.Optional[typing.Union["LambdaFunctionEventInvokeConfigDestinationConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        maximum_event_age_in_seconds: typing.Optional[jsii.Number] = None,
        maximum_retry_attempts: typing.Optional[jsii.Number] = None,
        qualifier: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param function_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#function_name LambdaFunctionEventInvokeConfig#function_name}.
        :param destination_config: destination_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#destination_config LambdaFunctionEventInvokeConfig#destination_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#id LambdaFunctionEventInvokeConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param maximum_event_age_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#maximum_event_age_in_seconds LambdaFunctionEventInvokeConfig#maximum_event_age_in_seconds}.
        :param maximum_retry_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#maximum_retry_attempts LambdaFunctionEventInvokeConfig#maximum_retry_attempts}.
        :param qualifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#qualifier LambdaFunctionEventInvokeConfig#qualifier}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(destination_config, dict):
            destination_config = LambdaFunctionEventInvokeConfigDestinationConfig(**destination_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__398ea5d0eb2bb085cc025d0f801cb6cdadb65033756d6ee7268b3931fcf981c8)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument function_name", value=function_name, expected_type=type_hints["function_name"])
            check_type(argname="argument destination_config", value=destination_config, expected_type=type_hints["destination_config"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument maximum_event_age_in_seconds", value=maximum_event_age_in_seconds, expected_type=type_hints["maximum_event_age_in_seconds"])
            check_type(argname="argument maximum_retry_attempts", value=maximum_retry_attempts, expected_type=type_hints["maximum_retry_attempts"])
            check_type(argname="argument qualifier", value=qualifier, expected_type=type_hints["qualifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "function_name": function_name,
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
        if destination_config is not None:
            self._values["destination_config"] = destination_config
        if id is not None:
            self._values["id"] = id
        if maximum_event_age_in_seconds is not None:
            self._values["maximum_event_age_in_seconds"] = maximum_event_age_in_seconds
        if maximum_retry_attempts is not None:
            self._values["maximum_retry_attempts"] = maximum_retry_attempts
        if qualifier is not None:
            self._values["qualifier"] = qualifier

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
    def function_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#function_name LambdaFunctionEventInvokeConfig#function_name}.'''
        result = self._values.get("function_name")
        assert result is not None, "Required property 'function_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def destination_config(
        self,
    ) -> typing.Optional["LambdaFunctionEventInvokeConfigDestinationConfig"]:
        '''destination_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#destination_config LambdaFunctionEventInvokeConfig#destination_config}
        '''
        result = self._values.get("destination_config")
        return typing.cast(typing.Optional["LambdaFunctionEventInvokeConfigDestinationConfig"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#id LambdaFunctionEventInvokeConfig#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maximum_event_age_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#maximum_event_age_in_seconds LambdaFunctionEventInvokeConfig#maximum_event_age_in_seconds}.'''
        result = self._values.get("maximum_event_age_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def maximum_retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#maximum_retry_attempts LambdaFunctionEventInvokeConfig#maximum_retry_attempts}.'''
        result = self._values.get("maximum_retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def qualifier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#qualifier LambdaFunctionEventInvokeConfig#qualifier}.'''
        result = self._values.get("qualifier")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaFunctionEventInvokeConfigConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.lambdaFunctionEventInvokeConfig.LambdaFunctionEventInvokeConfigDestinationConfig",
    jsii_struct_bases=[],
    name_mapping={"on_failure": "onFailure", "on_success": "onSuccess"},
)
class LambdaFunctionEventInvokeConfigDestinationConfig:
    def __init__(
        self,
        *,
        on_failure: typing.Optional[typing.Union["LambdaFunctionEventInvokeConfigDestinationConfigOnFailure", typing.Dict[builtins.str, typing.Any]]] = None,
        on_success: typing.Optional[typing.Union["LambdaFunctionEventInvokeConfigDestinationConfigOnSuccess", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param on_failure: on_failure block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#on_failure LambdaFunctionEventInvokeConfig#on_failure}
        :param on_success: on_success block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#on_success LambdaFunctionEventInvokeConfig#on_success}
        '''
        if isinstance(on_failure, dict):
            on_failure = LambdaFunctionEventInvokeConfigDestinationConfigOnFailure(**on_failure)
        if isinstance(on_success, dict):
            on_success = LambdaFunctionEventInvokeConfigDestinationConfigOnSuccess(**on_success)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f09add0a9fe57fabcb93af04066146699c64c3cf96d00662975c1f57dd1bbd6a)
            check_type(argname="argument on_failure", value=on_failure, expected_type=type_hints["on_failure"])
            check_type(argname="argument on_success", value=on_success, expected_type=type_hints["on_success"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if on_failure is not None:
            self._values["on_failure"] = on_failure
        if on_success is not None:
            self._values["on_success"] = on_success

    @builtins.property
    def on_failure(
        self,
    ) -> typing.Optional["LambdaFunctionEventInvokeConfigDestinationConfigOnFailure"]:
        '''on_failure block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#on_failure LambdaFunctionEventInvokeConfig#on_failure}
        '''
        result = self._values.get("on_failure")
        return typing.cast(typing.Optional["LambdaFunctionEventInvokeConfigDestinationConfigOnFailure"], result)

    @builtins.property
    def on_success(
        self,
    ) -> typing.Optional["LambdaFunctionEventInvokeConfigDestinationConfigOnSuccess"]:
        '''on_success block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#on_success LambdaFunctionEventInvokeConfig#on_success}
        '''
        result = self._values.get("on_success")
        return typing.cast(typing.Optional["LambdaFunctionEventInvokeConfigDestinationConfigOnSuccess"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaFunctionEventInvokeConfigDestinationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.lambdaFunctionEventInvokeConfig.LambdaFunctionEventInvokeConfigDestinationConfigOnFailure",
    jsii_struct_bases=[],
    name_mapping={"destination": "destination"},
)
class LambdaFunctionEventInvokeConfigDestinationConfigOnFailure:
    def __init__(self, *, destination: builtins.str) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#destination LambdaFunctionEventInvokeConfig#destination}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a814fe2292ca4b793ab111774c6455c697cec43eb9f6f9e016f39b10bde6e2f)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination": destination,
        }

    @builtins.property
    def destination(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#destination LambdaFunctionEventInvokeConfig#destination}.'''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaFunctionEventInvokeConfigDestinationConfigOnFailure(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LambdaFunctionEventInvokeConfigDestinationConfigOnFailureOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lambdaFunctionEventInvokeConfig.LambdaFunctionEventInvokeConfigDestinationConfigOnFailureOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__858d1cded56c3883596b9d45c3d16ed7053ea637cb5e19a22098bd4afb425629)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20e8d8ce3a94c08c2fc33dea28732e3a691657e171cce6ceaeb66fa8c63e6a71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LambdaFunctionEventInvokeConfigDestinationConfigOnFailure]:
        return typing.cast(typing.Optional[LambdaFunctionEventInvokeConfigDestinationConfigOnFailure], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LambdaFunctionEventInvokeConfigDestinationConfigOnFailure],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5e36e2872042cdb207da94b887d484c241a65e21cf5d3b3a73c8fd5d1c1f85e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.lambdaFunctionEventInvokeConfig.LambdaFunctionEventInvokeConfigDestinationConfigOnSuccess",
    jsii_struct_bases=[],
    name_mapping={"destination": "destination"},
)
class LambdaFunctionEventInvokeConfigDestinationConfigOnSuccess:
    def __init__(self, *, destination: builtins.str) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#destination LambdaFunctionEventInvokeConfig#destination}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae5b3359e3170110a934260d6a2dd1bf1fc00d2d6e35fe2fa4d8608ba058c166)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination": destination,
        }

    @builtins.property
    def destination(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#destination LambdaFunctionEventInvokeConfig#destination}.'''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaFunctionEventInvokeConfigDestinationConfigOnSuccess(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LambdaFunctionEventInvokeConfigDestinationConfigOnSuccessOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lambdaFunctionEventInvokeConfig.LambdaFunctionEventInvokeConfigDestinationConfigOnSuccessOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__93598294d669e783a7b1060db49f7591e5993c709aeb5bcc3e83cf9d0cc2129d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f56e5dcb300cd2d9ba7ff3ed26b5b7dbb07ea1e7f3e858c11ee77c7d403b94e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LambdaFunctionEventInvokeConfigDestinationConfigOnSuccess]:
        return typing.cast(typing.Optional[LambdaFunctionEventInvokeConfigDestinationConfigOnSuccess], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LambdaFunctionEventInvokeConfigDestinationConfigOnSuccess],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72862e4a07a4b81a82e838ae8cfbeb6b2b32f6212f8f7a2e60b52cbfa8bbf040)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LambdaFunctionEventInvokeConfigDestinationConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lambdaFunctionEventInvokeConfig.LambdaFunctionEventInvokeConfigDestinationConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__631e8a8d72805f5fdde5b51d76ff14f76d2d21fd31e312ed82bc6f2aeb132b42)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putOnFailure")
    def put_on_failure(self, *, destination: builtins.str) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#destination LambdaFunctionEventInvokeConfig#destination}.
        '''
        value = LambdaFunctionEventInvokeConfigDestinationConfigOnFailure(
            destination=destination
        )

        return typing.cast(None, jsii.invoke(self, "putOnFailure", [value]))

    @jsii.member(jsii_name="putOnSuccess")
    def put_on_success(self, *, destination: builtins.str) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_function_event_invoke_config#destination LambdaFunctionEventInvokeConfig#destination}.
        '''
        value = LambdaFunctionEventInvokeConfigDestinationConfigOnSuccess(
            destination=destination
        )

        return typing.cast(None, jsii.invoke(self, "putOnSuccess", [value]))

    @jsii.member(jsii_name="resetOnFailure")
    def reset_on_failure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnFailure", []))

    @jsii.member(jsii_name="resetOnSuccess")
    def reset_on_success(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnSuccess", []))

    @builtins.property
    @jsii.member(jsii_name="onFailure")
    def on_failure(
        self,
    ) -> LambdaFunctionEventInvokeConfigDestinationConfigOnFailureOutputReference:
        return typing.cast(LambdaFunctionEventInvokeConfigDestinationConfigOnFailureOutputReference, jsii.get(self, "onFailure"))

    @builtins.property
    @jsii.member(jsii_name="onSuccess")
    def on_success(
        self,
    ) -> LambdaFunctionEventInvokeConfigDestinationConfigOnSuccessOutputReference:
        return typing.cast(LambdaFunctionEventInvokeConfigDestinationConfigOnSuccessOutputReference, jsii.get(self, "onSuccess"))

    @builtins.property
    @jsii.member(jsii_name="onFailureInput")
    def on_failure_input(
        self,
    ) -> typing.Optional[LambdaFunctionEventInvokeConfigDestinationConfigOnFailure]:
        return typing.cast(typing.Optional[LambdaFunctionEventInvokeConfigDestinationConfigOnFailure], jsii.get(self, "onFailureInput"))

    @builtins.property
    @jsii.member(jsii_name="onSuccessInput")
    def on_success_input(
        self,
    ) -> typing.Optional[LambdaFunctionEventInvokeConfigDestinationConfigOnSuccess]:
        return typing.cast(typing.Optional[LambdaFunctionEventInvokeConfigDestinationConfigOnSuccess], jsii.get(self, "onSuccessInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LambdaFunctionEventInvokeConfigDestinationConfig]:
        return typing.cast(typing.Optional[LambdaFunctionEventInvokeConfigDestinationConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LambdaFunctionEventInvokeConfigDestinationConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbff78ac38dffebab736dac63ce0972d284dc6a9247b413ed1796cc72c93612c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "LambdaFunctionEventInvokeConfig",
    "LambdaFunctionEventInvokeConfigConfig",
    "LambdaFunctionEventInvokeConfigDestinationConfig",
    "LambdaFunctionEventInvokeConfigDestinationConfigOnFailure",
    "LambdaFunctionEventInvokeConfigDestinationConfigOnFailureOutputReference",
    "LambdaFunctionEventInvokeConfigDestinationConfigOnSuccess",
    "LambdaFunctionEventInvokeConfigDestinationConfigOnSuccessOutputReference",
    "LambdaFunctionEventInvokeConfigDestinationConfigOutputReference",
]

publication.publish()

def _typecheckingstub__6f2884c5b362c0bff65c631cb246c43f63d73c5cbc92468792ce29cbfb543fe4(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    function_name: builtins.str,
    destination_config: typing.Optional[typing.Union[LambdaFunctionEventInvokeConfigDestinationConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    maximum_event_age_in_seconds: typing.Optional[jsii.Number] = None,
    maximum_retry_attempts: typing.Optional[jsii.Number] = None,
    qualifier: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__68e690d73f5b6f945d20cb3f9a95a24652e046e01adda69d59ad9336db19f642(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4690f61914c54b2a2d4321a91305da17f18b35fd328a317a628ed4b039a56e09(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c2a2d9280e5c11ede46eb0a47b5e83ea39eebdb0c69a8fbea0b9852c6460ea0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d686375acc1b721a9b9109f1ced3701d59a0517fd90e22d70eda3d1e1a0cb9c5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e767caf1b94e64291c9e5a05c98a6c468c8c8ff0eb5e4ac5b6564c50e974ef4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__398ea5d0eb2bb085cc025d0f801cb6cdadb65033756d6ee7268b3931fcf981c8(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    function_name: builtins.str,
    destination_config: typing.Optional[typing.Union[LambdaFunctionEventInvokeConfigDestinationConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    maximum_event_age_in_seconds: typing.Optional[jsii.Number] = None,
    maximum_retry_attempts: typing.Optional[jsii.Number] = None,
    qualifier: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f09add0a9fe57fabcb93af04066146699c64c3cf96d00662975c1f57dd1bbd6a(
    *,
    on_failure: typing.Optional[typing.Union[LambdaFunctionEventInvokeConfigDestinationConfigOnFailure, typing.Dict[builtins.str, typing.Any]]] = None,
    on_success: typing.Optional[typing.Union[LambdaFunctionEventInvokeConfigDestinationConfigOnSuccess, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a814fe2292ca4b793ab111774c6455c697cec43eb9f6f9e016f39b10bde6e2f(
    *,
    destination: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__858d1cded56c3883596b9d45c3d16ed7053ea637cb5e19a22098bd4afb425629(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20e8d8ce3a94c08c2fc33dea28732e3a691657e171cce6ceaeb66fa8c63e6a71(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5e36e2872042cdb207da94b887d484c241a65e21cf5d3b3a73c8fd5d1c1f85e(
    value: typing.Optional[LambdaFunctionEventInvokeConfigDestinationConfigOnFailure],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae5b3359e3170110a934260d6a2dd1bf1fc00d2d6e35fe2fa4d8608ba058c166(
    *,
    destination: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93598294d669e783a7b1060db49f7591e5993c709aeb5bcc3e83cf9d0cc2129d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f56e5dcb300cd2d9ba7ff3ed26b5b7dbb07ea1e7f3e858c11ee77c7d403b94e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72862e4a07a4b81a82e838ae8cfbeb6b2b32f6212f8f7a2e60b52cbfa8bbf040(
    value: typing.Optional[LambdaFunctionEventInvokeConfigDestinationConfigOnSuccess],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__631e8a8d72805f5fdde5b51d76ff14f76d2d21fd31e312ed82bc6f2aeb132b42(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbff78ac38dffebab736dac63ce0972d284dc6a9247b413ed1796cc72c93612c(
    value: typing.Optional[LambdaFunctionEventInvokeConfigDestinationConfig],
) -> None:
    """Type checking stubs"""
    pass
