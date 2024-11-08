'''
# `aws_apigatewayv2_integration`

Refer to the Terraform Registory for docs: [`aws_apigatewayv2_integration`](https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration).
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


class Apigatewayv2Integration(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.apigatewayv2Integration.Apigatewayv2Integration",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration aws_apigatewayv2_integration}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        api_id: builtins.str,
        integration_type: builtins.str,
        connection_id: typing.Optional[builtins.str] = None,
        connection_type: typing.Optional[builtins.str] = None,
        content_handling_strategy: typing.Optional[builtins.str] = None,
        credentials_arn: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        integration_method: typing.Optional[builtins.str] = None,
        integration_subtype: typing.Optional[builtins.str] = None,
        integration_uri: typing.Optional[builtins.str] = None,
        passthrough_behavior: typing.Optional[builtins.str] = None,
        payload_format_version: typing.Optional[builtins.str] = None,
        request_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        request_templates: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        response_parameters: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Apigatewayv2IntegrationResponseParameters", typing.Dict[builtins.str, typing.Any]]]]] = None,
        template_selection_expression: typing.Optional[builtins.str] = None,
        timeout_milliseconds: typing.Optional[jsii.Number] = None,
        tls_config: typing.Optional[typing.Union["Apigatewayv2IntegrationTlsConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration aws_apigatewayv2_integration} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param api_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#api_id Apigatewayv2Integration#api_id}.
        :param integration_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#integration_type Apigatewayv2Integration#integration_type}.
        :param connection_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#connection_id Apigatewayv2Integration#connection_id}.
        :param connection_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#connection_type Apigatewayv2Integration#connection_type}.
        :param content_handling_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#content_handling_strategy Apigatewayv2Integration#content_handling_strategy}.
        :param credentials_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#credentials_arn Apigatewayv2Integration#credentials_arn}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#description Apigatewayv2Integration#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#id Apigatewayv2Integration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param integration_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#integration_method Apigatewayv2Integration#integration_method}.
        :param integration_subtype: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#integration_subtype Apigatewayv2Integration#integration_subtype}.
        :param integration_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#integration_uri Apigatewayv2Integration#integration_uri}.
        :param passthrough_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#passthrough_behavior Apigatewayv2Integration#passthrough_behavior}.
        :param payload_format_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#payload_format_version Apigatewayv2Integration#payload_format_version}.
        :param request_parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#request_parameters Apigatewayv2Integration#request_parameters}.
        :param request_templates: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#request_templates Apigatewayv2Integration#request_templates}.
        :param response_parameters: response_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#response_parameters Apigatewayv2Integration#response_parameters}
        :param template_selection_expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#template_selection_expression Apigatewayv2Integration#template_selection_expression}.
        :param timeout_milliseconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#timeout_milliseconds Apigatewayv2Integration#timeout_milliseconds}.
        :param tls_config: tls_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#tls_config Apigatewayv2Integration#tls_config}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__602e1a4980c171451f811fab54521da5bfe65f90419c9c9c6f04d55b30f5c52a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = Apigatewayv2IntegrationConfig(
            api_id=api_id,
            integration_type=integration_type,
            connection_id=connection_id,
            connection_type=connection_type,
            content_handling_strategy=content_handling_strategy,
            credentials_arn=credentials_arn,
            description=description,
            id=id,
            integration_method=integration_method,
            integration_subtype=integration_subtype,
            integration_uri=integration_uri,
            passthrough_behavior=passthrough_behavior,
            payload_format_version=payload_format_version,
            request_parameters=request_parameters,
            request_templates=request_templates,
            response_parameters=response_parameters,
            template_selection_expression=template_selection_expression,
            timeout_milliseconds=timeout_milliseconds,
            tls_config=tls_config,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putResponseParameters")
    def put_response_parameters(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Apigatewayv2IntegrationResponseParameters", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f4404497565b0f48a652b90d7ee6b6c0673ad1fe146e17a6c7aba58ef151f5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putResponseParameters", [value]))

    @jsii.member(jsii_name="putTlsConfig")
    def put_tls_config(
        self,
        *,
        server_name_to_verify: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param server_name_to_verify: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#server_name_to_verify Apigatewayv2Integration#server_name_to_verify}.
        '''
        value = Apigatewayv2IntegrationTlsConfig(
            server_name_to_verify=server_name_to_verify
        )

        return typing.cast(None, jsii.invoke(self, "putTlsConfig", [value]))

    @jsii.member(jsii_name="resetConnectionId")
    def reset_connection_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionId", []))

    @jsii.member(jsii_name="resetConnectionType")
    def reset_connection_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionType", []))

    @jsii.member(jsii_name="resetContentHandlingStrategy")
    def reset_content_handling_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentHandlingStrategy", []))

    @jsii.member(jsii_name="resetCredentialsArn")
    def reset_credentials_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCredentialsArn", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIntegrationMethod")
    def reset_integration_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIntegrationMethod", []))

    @jsii.member(jsii_name="resetIntegrationSubtype")
    def reset_integration_subtype(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIntegrationSubtype", []))

    @jsii.member(jsii_name="resetIntegrationUri")
    def reset_integration_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIntegrationUri", []))

    @jsii.member(jsii_name="resetPassthroughBehavior")
    def reset_passthrough_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassthroughBehavior", []))

    @jsii.member(jsii_name="resetPayloadFormatVersion")
    def reset_payload_format_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPayloadFormatVersion", []))

    @jsii.member(jsii_name="resetRequestParameters")
    def reset_request_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestParameters", []))

    @jsii.member(jsii_name="resetRequestTemplates")
    def reset_request_templates(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestTemplates", []))

    @jsii.member(jsii_name="resetResponseParameters")
    def reset_response_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseParameters", []))

    @jsii.member(jsii_name="resetTemplateSelectionExpression")
    def reset_template_selection_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTemplateSelectionExpression", []))

    @jsii.member(jsii_name="resetTimeoutMilliseconds")
    def reset_timeout_milliseconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeoutMilliseconds", []))

    @jsii.member(jsii_name="resetTlsConfig")
    def reset_tls_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsConfig", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="integrationResponseSelectionExpression")
    def integration_response_selection_expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "integrationResponseSelectionExpression"))

    @builtins.property
    @jsii.member(jsii_name="responseParameters")
    def response_parameters(self) -> "Apigatewayv2IntegrationResponseParametersList":
        return typing.cast("Apigatewayv2IntegrationResponseParametersList", jsii.get(self, "responseParameters"))

    @builtins.property
    @jsii.member(jsii_name="tlsConfig")
    def tls_config(self) -> "Apigatewayv2IntegrationTlsConfigOutputReference":
        return typing.cast("Apigatewayv2IntegrationTlsConfigOutputReference", jsii.get(self, "tlsConfig"))

    @builtins.property
    @jsii.member(jsii_name="apiIdInput")
    def api_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiIdInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionIdInput")
    def connection_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionTypeInput")
    def connection_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="contentHandlingStrategyInput")
    def content_handling_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentHandlingStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="credentialsArnInput")
    def credentials_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "credentialsArnInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="integrationMethodInput")
    def integration_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "integrationMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="integrationSubtypeInput")
    def integration_subtype_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "integrationSubtypeInput"))

    @builtins.property
    @jsii.member(jsii_name="integrationTypeInput")
    def integration_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "integrationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="integrationUriInput")
    def integration_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "integrationUriInput"))

    @builtins.property
    @jsii.member(jsii_name="passthroughBehaviorInput")
    def passthrough_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passthroughBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="payloadFormatVersionInput")
    def payload_format_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "payloadFormatVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="requestParametersInput")
    def request_parameters_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "requestParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="requestTemplatesInput")
    def request_templates_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "requestTemplatesInput"))

    @builtins.property
    @jsii.member(jsii_name="responseParametersInput")
    def response_parameters_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Apigatewayv2IntegrationResponseParameters"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Apigatewayv2IntegrationResponseParameters"]]], jsii.get(self, "responseParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="templateSelectionExpressionInput")
    def template_selection_expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateSelectionExpressionInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutMillisecondsInput")
    def timeout_milliseconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutMillisecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsConfigInput")
    def tls_config_input(self) -> typing.Optional["Apigatewayv2IntegrationTlsConfig"]:
        return typing.cast(typing.Optional["Apigatewayv2IntegrationTlsConfig"], jsii.get(self, "tlsConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__292168bf9b7278edb669897f76e4971140af074be09938cedc779719bff64f34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="connectionId")
    def connection_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionId"))

    @connection_id.setter
    def connection_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64bb7444585325283ddda93fcc125a3db5de3b55c3309e155a52148c8d645267)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionId", value)

    @builtins.property
    @jsii.member(jsii_name="connectionType")
    def connection_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionType"))

    @connection_type.setter
    def connection_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b62354ed8a0ac3db229ce41fde993296bbc1b1df02967d39edab4cc9b6e4057)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionType", value)

    @builtins.property
    @jsii.member(jsii_name="contentHandlingStrategy")
    def content_handling_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentHandlingStrategy"))

    @content_handling_strategy.setter
    def content_handling_strategy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__104ddbc51ab3b380d923a183a9fb43dfb8ae6d76f72ee29a78eecc0928ad16e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentHandlingStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="credentialsArn")
    def credentials_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "credentialsArn"))

    @credentials_arn.setter
    def credentials_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__632a714e8aa12b19760e14bc8106d5dcbb59f186fb84b5c9442847988d512481)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "credentialsArn", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce290eb69da401e6bf352533788564b6559c23455e57e9afe97a691231de4986)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80d40231aa95022cef3e9cf657591aa664702c085061e4739e9b4abce0bdc209)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="integrationMethod")
    def integration_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "integrationMethod"))

    @integration_method.setter
    def integration_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2563b97de92ceb2c46182cb674a4c60cbae38446e652ba16b88442283f2faca5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "integrationMethod", value)

    @builtins.property
    @jsii.member(jsii_name="integrationSubtype")
    def integration_subtype(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "integrationSubtype"))

    @integration_subtype.setter
    def integration_subtype(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4db2d8a552527fdc3812310166725ff19fcc78866e7a7c72635ac8d6d0fd68f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "integrationSubtype", value)

    @builtins.property
    @jsii.member(jsii_name="integrationType")
    def integration_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "integrationType"))

    @integration_type.setter
    def integration_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4364b3bd0a9d991e31d1ec3acb0a37bb76b4435272f574e991dc2d8032f3f33d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "integrationType", value)

    @builtins.property
    @jsii.member(jsii_name="integrationUri")
    def integration_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "integrationUri"))

    @integration_uri.setter
    def integration_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fce9d861aaf7dc9b0234556fc3c6851e66a9e3deb2e8ab9257b1123eb98047bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "integrationUri", value)

    @builtins.property
    @jsii.member(jsii_name="passthroughBehavior")
    def passthrough_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "passthroughBehavior"))

    @passthrough_behavior.setter
    def passthrough_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5eaec79c2d195f87fe3d2baad1133663a3a5b49e5ac5559990c83563f12021a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passthroughBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="payloadFormatVersion")
    def payload_format_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "payloadFormatVersion"))

    @payload_format_version.setter
    def payload_format_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__463712afd56d84971605686d1bed7d8304d27f386ecf6914d543c4a08f66d610)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "payloadFormatVersion", value)

    @builtins.property
    @jsii.member(jsii_name="requestParameters")
    def request_parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "requestParameters"))

    @request_parameters.setter
    def request_parameters(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2913b9b2c984f2cd94f5c3dabd2a60870dcfefc799123c616a5f684607651f71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestParameters", value)

    @builtins.property
    @jsii.member(jsii_name="requestTemplates")
    def request_templates(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "requestTemplates"))

    @request_templates.setter
    def request_templates(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47b8f4cb631b0f54820b2b1659bbef0402146213afad5374fd3e40afa1d719c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestTemplates", value)

    @builtins.property
    @jsii.member(jsii_name="templateSelectionExpression")
    def template_selection_expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "templateSelectionExpression"))

    @template_selection_expression.setter
    def template_selection_expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7211e13c6a38d0a6c74325b28a8ab8efdc3e619830f51b8e76669a1dc94269bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateSelectionExpression", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutMilliseconds")
    def timeout_milliseconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutMilliseconds"))

    @timeout_milliseconds.setter
    def timeout_milliseconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a72843a8a37cc808adb50ee7f147da372b53b250f8cd4fbe9693f7d464ee1931)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutMilliseconds", value)


@jsii.data_type(
    jsii_type="aws.apigatewayv2Integration.Apigatewayv2IntegrationConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "api_id": "apiId",
        "integration_type": "integrationType",
        "connection_id": "connectionId",
        "connection_type": "connectionType",
        "content_handling_strategy": "contentHandlingStrategy",
        "credentials_arn": "credentialsArn",
        "description": "description",
        "id": "id",
        "integration_method": "integrationMethod",
        "integration_subtype": "integrationSubtype",
        "integration_uri": "integrationUri",
        "passthrough_behavior": "passthroughBehavior",
        "payload_format_version": "payloadFormatVersion",
        "request_parameters": "requestParameters",
        "request_templates": "requestTemplates",
        "response_parameters": "responseParameters",
        "template_selection_expression": "templateSelectionExpression",
        "timeout_milliseconds": "timeoutMilliseconds",
        "tls_config": "tlsConfig",
    },
)
class Apigatewayv2IntegrationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        api_id: builtins.str,
        integration_type: builtins.str,
        connection_id: typing.Optional[builtins.str] = None,
        connection_type: typing.Optional[builtins.str] = None,
        content_handling_strategy: typing.Optional[builtins.str] = None,
        credentials_arn: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        integration_method: typing.Optional[builtins.str] = None,
        integration_subtype: typing.Optional[builtins.str] = None,
        integration_uri: typing.Optional[builtins.str] = None,
        passthrough_behavior: typing.Optional[builtins.str] = None,
        payload_format_version: typing.Optional[builtins.str] = None,
        request_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        request_templates: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        response_parameters: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["Apigatewayv2IntegrationResponseParameters", typing.Dict[builtins.str, typing.Any]]]]] = None,
        template_selection_expression: typing.Optional[builtins.str] = None,
        timeout_milliseconds: typing.Optional[jsii.Number] = None,
        tls_config: typing.Optional[typing.Union["Apigatewayv2IntegrationTlsConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param api_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#api_id Apigatewayv2Integration#api_id}.
        :param integration_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#integration_type Apigatewayv2Integration#integration_type}.
        :param connection_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#connection_id Apigatewayv2Integration#connection_id}.
        :param connection_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#connection_type Apigatewayv2Integration#connection_type}.
        :param content_handling_strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#content_handling_strategy Apigatewayv2Integration#content_handling_strategy}.
        :param credentials_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#credentials_arn Apigatewayv2Integration#credentials_arn}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#description Apigatewayv2Integration#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#id Apigatewayv2Integration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param integration_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#integration_method Apigatewayv2Integration#integration_method}.
        :param integration_subtype: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#integration_subtype Apigatewayv2Integration#integration_subtype}.
        :param integration_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#integration_uri Apigatewayv2Integration#integration_uri}.
        :param passthrough_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#passthrough_behavior Apigatewayv2Integration#passthrough_behavior}.
        :param payload_format_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#payload_format_version Apigatewayv2Integration#payload_format_version}.
        :param request_parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#request_parameters Apigatewayv2Integration#request_parameters}.
        :param request_templates: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#request_templates Apigatewayv2Integration#request_templates}.
        :param response_parameters: response_parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#response_parameters Apigatewayv2Integration#response_parameters}
        :param template_selection_expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#template_selection_expression Apigatewayv2Integration#template_selection_expression}.
        :param timeout_milliseconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#timeout_milliseconds Apigatewayv2Integration#timeout_milliseconds}.
        :param tls_config: tls_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#tls_config Apigatewayv2Integration#tls_config}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(tls_config, dict):
            tls_config = Apigatewayv2IntegrationTlsConfig(**tls_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a303038aec0e8afaebd6583288ba84b9f1860ba223235ef5085ef3e7feb96795)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument integration_type", value=integration_type, expected_type=type_hints["integration_type"])
            check_type(argname="argument connection_id", value=connection_id, expected_type=type_hints["connection_id"])
            check_type(argname="argument connection_type", value=connection_type, expected_type=type_hints["connection_type"])
            check_type(argname="argument content_handling_strategy", value=content_handling_strategy, expected_type=type_hints["content_handling_strategy"])
            check_type(argname="argument credentials_arn", value=credentials_arn, expected_type=type_hints["credentials_arn"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument integration_method", value=integration_method, expected_type=type_hints["integration_method"])
            check_type(argname="argument integration_subtype", value=integration_subtype, expected_type=type_hints["integration_subtype"])
            check_type(argname="argument integration_uri", value=integration_uri, expected_type=type_hints["integration_uri"])
            check_type(argname="argument passthrough_behavior", value=passthrough_behavior, expected_type=type_hints["passthrough_behavior"])
            check_type(argname="argument payload_format_version", value=payload_format_version, expected_type=type_hints["payload_format_version"])
            check_type(argname="argument request_parameters", value=request_parameters, expected_type=type_hints["request_parameters"])
            check_type(argname="argument request_templates", value=request_templates, expected_type=type_hints["request_templates"])
            check_type(argname="argument response_parameters", value=response_parameters, expected_type=type_hints["response_parameters"])
            check_type(argname="argument template_selection_expression", value=template_selection_expression, expected_type=type_hints["template_selection_expression"])
            check_type(argname="argument timeout_milliseconds", value=timeout_milliseconds, expected_type=type_hints["timeout_milliseconds"])
            check_type(argname="argument tls_config", value=tls_config, expected_type=type_hints["tls_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_id": api_id,
            "integration_type": integration_type,
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
        if connection_id is not None:
            self._values["connection_id"] = connection_id
        if connection_type is not None:
            self._values["connection_type"] = connection_type
        if content_handling_strategy is not None:
            self._values["content_handling_strategy"] = content_handling_strategy
        if credentials_arn is not None:
            self._values["credentials_arn"] = credentials_arn
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if integration_method is not None:
            self._values["integration_method"] = integration_method
        if integration_subtype is not None:
            self._values["integration_subtype"] = integration_subtype
        if integration_uri is not None:
            self._values["integration_uri"] = integration_uri
        if passthrough_behavior is not None:
            self._values["passthrough_behavior"] = passthrough_behavior
        if payload_format_version is not None:
            self._values["payload_format_version"] = payload_format_version
        if request_parameters is not None:
            self._values["request_parameters"] = request_parameters
        if request_templates is not None:
            self._values["request_templates"] = request_templates
        if response_parameters is not None:
            self._values["response_parameters"] = response_parameters
        if template_selection_expression is not None:
            self._values["template_selection_expression"] = template_selection_expression
        if timeout_milliseconds is not None:
            self._values["timeout_milliseconds"] = timeout_milliseconds
        if tls_config is not None:
            self._values["tls_config"] = tls_config

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
    def api_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#api_id Apigatewayv2Integration#api_id}.'''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def integration_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#integration_type Apigatewayv2Integration#integration_type}.'''
        result = self._values.get("integration_type")
        assert result is not None, "Required property 'integration_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def connection_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#connection_id Apigatewayv2Integration#connection_id}.'''
        result = self._values.get("connection_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connection_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#connection_type Apigatewayv2Integration#connection_type}.'''
        result = self._values.get("connection_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_handling_strategy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#content_handling_strategy Apigatewayv2Integration#content_handling_strategy}.'''
        result = self._values.get("content_handling_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def credentials_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#credentials_arn Apigatewayv2Integration#credentials_arn}.'''
        result = self._values.get("credentials_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#description Apigatewayv2Integration#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#id Apigatewayv2Integration#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def integration_method(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#integration_method Apigatewayv2Integration#integration_method}.'''
        result = self._values.get("integration_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def integration_subtype(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#integration_subtype Apigatewayv2Integration#integration_subtype}.'''
        result = self._values.get("integration_subtype")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def integration_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#integration_uri Apigatewayv2Integration#integration_uri}.'''
        result = self._values.get("integration_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def passthrough_behavior(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#passthrough_behavior Apigatewayv2Integration#passthrough_behavior}.'''
        result = self._values.get("passthrough_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def payload_format_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#payload_format_version Apigatewayv2Integration#payload_format_version}.'''
        result = self._values.get("payload_format_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#request_parameters Apigatewayv2Integration#request_parameters}.'''
        result = self._values.get("request_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def request_templates(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#request_templates Apigatewayv2Integration#request_templates}.'''
        result = self._values.get("request_templates")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def response_parameters(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Apigatewayv2IntegrationResponseParameters"]]]:
        '''response_parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#response_parameters Apigatewayv2Integration#response_parameters}
        '''
        result = self._values.get("response_parameters")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["Apigatewayv2IntegrationResponseParameters"]]], result)

    @builtins.property
    def template_selection_expression(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#template_selection_expression Apigatewayv2Integration#template_selection_expression}.'''
        result = self._values.get("template_selection_expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeout_milliseconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#timeout_milliseconds Apigatewayv2Integration#timeout_milliseconds}.'''
        result = self._values.get("timeout_milliseconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tls_config(self) -> typing.Optional["Apigatewayv2IntegrationTlsConfig"]:
        '''tls_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#tls_config Apigatewayv2Integration#tls_config}
        '''
        result = self._values.get("tls_config")
        return typing.cast(typing.Optional["Apigatewayv2IntegrationTlsConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Apigatewayv2IntegrationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.apigatewayv2Integration.Apigatewayv2IntegrationResponseParameters",
    jsii_struct_bases=[],
    name_mapping={"mappings": "mappings", "status_code": "statusCode"},
)
class Apigatewayv2IntegrationResponseParameters:
    def __init__(
        self,
        *,
        mappings: typing.Mapping[builtins.str, builtins.str],
        status_code: builtins.str,
    ) -> None:
        '''
        :param mappings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#mappings Apigatewayv2Integration#mappings}.
        :param status_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#status_code Apigatewayv2Integration#status_code}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e2745431d6f17056a9de87ca4ea7fe6ae4ced8dc288f85bf4c8709ff004ef31)
            check_type(argname="argument mappings", value=mappings, expected_type=type_hints["mappings"])
            check_type(argname="argument status_code", value=status_code, expected_type=type_hints["status_code"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "mappings": mappings,
            "status_code": status_code,
        }

    @builtins.property
    def mappings(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#mappings Apigatewayv2Integration#mappings}.'''
        result = self._values.get("mappings")
        assert result is not None, "Required property 'mappings' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    @builtins.property
    def status_code(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#status_code Apigatewayv2Integration#status_code}.'''
        result = self._values.get("status_code")
        assert result is not None, "Required property 'status_code' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Apigatewayv2IntegrationResponseParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Apigatewayv2IntegrationResponseParametersList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.apigatewayv2Integration.Apigatewayv2IntegrationResponseParametersList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__01827ad0879dbc38b7426e705f902a42b4a885c66181e82ebf54a7400c2bbba5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "Apigatewayv2IntegrationResponseParametersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82fbc8a5e54670cb85fb2fefe947782914627c43422095d5020cfed9b45d69be)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("Apigatewayv2IntegrationResponseParametersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b033e7df9f4fdda8bbc4a38f6c32cd63b3272265847e7b012674b46e44810a83)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6614b86e464f769a8f329b1cdae6145cf0f8202b6a2de87e773815c0465b4d73)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4bd8367c2cc3491fc7c573de7e423327886e8c8ac09db3f9a717d2a645737afa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Apigatewayv2IntegrationResponseParameters]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Apigatewayv2IntegrationResponseParameters]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Apigatewayv2IntegrationResponseParameters]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a768d5d038a4df6066362ed98657b3c99644c70dc9a0939afb8c5e033446c113)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class Apigatewayv2IntegrationResponseParametersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.apigatewayv2Integration.Apigatewayv2IntegrationResponseParametersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0b0146bf2aa6d9b8b4c6d6b68ab5dcc302c722a4264b4300afaf3d4cea940a8c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="mappingsInput")
    def mappings_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "mappingsInput"))

    @builtins.property
    @jsii.member(jsii_name="statusCodeInput")
    def status_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="mappings")
    def mappings(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "mappings"))

    @mappings.setter
    def mappings(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56d0bb238ee25ab0aa66c5246ac0b914704b8e7f11c6471014ec8c88a9041fef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mappings", value)

    @builtins.property
    @jsii.member(jsii_name="statusCode")
    def status_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statusCode"))

    @status_code.setter
    def status_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2539331fa5a4dc51fca125143572ba74bc6a3415ceda8099b557c2a8d22b88fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statusCode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[Apigatewayv2IntegrationResponseParameters, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[Apigatewayv2IntegrationResponseParameters, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[Apigatewayv2IntegrationResponseParameters, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49e17e0e4cfa9ad8626dfc86e152f61bead8ca58e3590d2d820f8c7d81fabd22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.apigatewayv2Integration.Apigatewayv2IntegrationTlsConfig",
    jsii_struct_bases=[],
    name_mapping={"server_name_to_verify": "serverNameToVerify"},
)
class Apigatewayv2IntegrationTlsConfig:
    def __init__(
        self,
        *,
        server_name_to_verify: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param server_name_to_verify: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#server_name_to_verify Apigatewayv2Integration#server_name_to_verify}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fdb6f4f9737a46d2080741646f1cbbe4ecc512fbb9ca502d51f20e9342d4467a)
            check_type(argname="argument server_name_to_verify", value=server_name_to_verify, expected_type=type_hints["server_name_to_verify"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if server_name_to_verify is not None:
            self._values["server_name_to_verify"] = server_name_to_verify

    @builtins.property
    def server_name_to_verify(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/apigatewayv2_integration#server_name_to_verify Apigatewayv2Integration#server_name_to_verify}.'''
        result = self._values.get("server_name_to_verify")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Apigatewayv2IntegrationTlsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Apigatewayv2IntegrationTlsConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.apigatewayv2Integration.Apigatewayv2IntegrationTlsConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__824f44254505d44d6d567bcac9cedb6882e39134214e808d351a5dd37ecb55d2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetServerNameToVerify")
    def reset_server_name_to_verify(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerNameToVerify", []))

    @builtins.property
    @jsii.member(jsii_name="serverNameToVerifyInput")
    def server_name_to_verify_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverNameToVerifyInput"))

    @builtins.property
    @jsii.member(jsii_name="serverNameToVerify")
    def server_name_to_verify(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverNameToVerify"))

    @server_name_to_verify.setter
    def server_name_to_verify(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65da4f062f783d063c54d46230350e07704152aca93e0ace837709fefa04cad2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverNameToVerify", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[Apigatewayv2IntegrationTlsConfig]:
        return typing.cast(typing.Optional[Apigatewayv2IntegrationTlsConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Apigatewayv2IntegrationTlsConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6738da95c1c45a7ab73a8b08210881d1a6d5cc7e019b33468114406576978fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Apigatewayv2Integration",
    "Apigatewayv2IntegrationConfig",
    "Apigatewayv2IntegrationResponseParameters",
    "Apigatewayv2IntegrationResponseParametersList",
    "Apigatewayv2IntegrationResponseParametersOutputReference",
    "Apigatewayv2IntegrationTlsConfig",
    "Apigatewayv2IntegrationTlsConfigOutputReference",
]

publication.publish()

def _typecheckingstub__602e1a4980c171451f811fab54521da5bfe65f90419c9c9c6f04d55b30f5c52a(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    api_id: builtins.str,
    integration_type: builtins.str,
    connection_id: typing.Optional[builtins.str] = None,
    connection_type: typing.Optional[builtins.str] = None,
    content_handling_strategy: typing.Optional[builtins.str] = None,
    credentials_arn: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    integration_method: typing.Optional[builtins.str] = None,
    integration_subtype: typing.Optional[builtins.str] = None,
    integration_uri: typing.Optional[builtins.str] = None,
    passthrough_behavior: typing.Optional[builtins.str] = None,
    payload_format_version: typing.Optional[builtins.str] = None,
    request_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    request_templates: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    response_parameters: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Apigatewayv2IntegrationResponseParameters, typing.Dict[builtins.str, typing.Any]]]]] = None,
    template_selection_expression: typing.Optional[builtins.str] = None,
    timeout_milliseconds: typing.Optional[jsii.Number] = None,
    tls_config: typing.Optional[typing.Union[Apigatewayv2IntegrationTlsConfig, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__5f4404497565b0f48a652b90d7ee6b6c0673ad1fe146e17a6c7aba58ef151f5d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Apigatewayv2IntegrationResponseParameters, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__292168bf9b7278edb669897f76e4971140af074be09938cedc779719bff64f34(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64bb7444585325283ddda93fcc125a3db5de3b55c3309e155a52148c8d645267(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b62354ed8a0ac3db229ce41fde993296bbc1b1df02967d39edab4cc9b6e4057(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__104ddbc51ab3b380d923a183a9fb43dfb8ae6d76f72ee29a78eecc0928ad16e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__632a714e8aa12b19760e14bc8106d5dcbb59f186fb84b5c9442847988d512481(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce290eb69da401e6bf352533788564b6559c23455e57e9afe97a691231de4986(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80d40231aa95022cef3e9cf657591aa664702c085061e4739e9b4abce0bdc209(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2563b97de92ceb2c46182cb674a4c60cbae38446e652ba16b88442283f2faca5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4db2d8a552527fdc3812310166725ff19fcc78866e7a7c72635ac8d6d0fd68f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4364b3bd0a9d991e31d1ec3acb0a37bb76b4435272f574e991dc2d8032f3f33d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fce9d861aaf7dc9b0234556fc3c6851e66a9e3deb2e8ab9257b1123eb98047bd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5eaec79c2d195f87fe3d2baad1133663a3a5b49e5ac5559990c83563f12021a0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__463712afd56d84971605686d1bed7d8304d27f386ecf6914d543c4a08f66d610(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2913b9b2c984f2cd94f5c3dabd2a60870dcfefc799123c616a5f684607651f71(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47b8f4cb631b0f54820b2b1659bbef0402146213afad5374fd3e40afa1d719c0(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7211e13c6a38d0a6c74325b28a8ab8efdc3e619830f51b8e76669a1dc94269bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a72843a8a37cc808adb50ee7f147da372b53b250f8cd4fbe9693f7d464ee1931(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a303038aec0e8afaebd6583288ba84b9f1860ba223235ef5085ef3e7feb96795(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    api_id: builtins.str,
    integration_type: builtins.str,
    connection_id: typing.Optional[builtins.str] = None,
    connection_type: typing.Optional[builtins.str] = None,
    content_handling_strategy: typing.Optional[builtins.str] = None,
    credentials_arn: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    integration_method: typing.Optional[builtins.str] = None,
    integration_subtype: typing.Optional[builtins.str] = None,
    integration_uri: typing.Optional[builtins.str] = None,
    passthrough_behavior: typing.Optional[builtins.str] = None,
    payload_format_version: typing.Optional[builtins.str] = None,
    request_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    request_templates: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    response_parameters: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[Apigatewayv2IntegrationResponseParameters, typing.Dict[builtins.str, typing.Any]]]]] = None,
    template_selection_expression: typing.Optional[builtins.str] = None,
    timeout_milliseconds: typing.Optional[jsii.Number] = None,
    tls_config: typing.Optional[typing.Union[Apigatewayv2IntegrationTlsConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e2745431d6f17056a9de87ca4ea7fe6ae4ced8dc288f85bf4c8709ff004ef31(
    *,
    mappings: typing.Mapping[builtins.str, builtins.str],
    status_code: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01827ad0879dbc38b7426e705f902a42b4a885c66181e82ebf54a7400c2bbba5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82fbc8a5e54670cb85fb2fefe947782914627c43422095d5020cfed9b45d69be(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b033e7df9f4fdda8bbc4a38f6c32cd63b3272265847e7b012674b46e44810a83(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6614b86e464f769a8f329b1cdae6145cf0f8202b6a2de87e773815c0465b4d73(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bd8367c2cc3491fc7c573de7e423327886e8c8ac09db3f9a717d2a645737afa(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a768d5d038a4df6066362ed98657b3c99644c70dc9a0939afb8c5e033446c113(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[Apigatewayv2IntegrationResponseParameters]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b0146bf2aa6d9b8b4c6d6b68ab5dcc302c722a4264b4300afaf3d4cea940a8c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56d0bb238ee25ab0aa66c5246ac0b914704b8e7f11c6471014ec8c88a9041fef(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2539331fa5a4dc51fca125143572ba74bc6a3415ceda8099b557c2a8d22b88fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49e17e0e4cfa9ad8626dfc86e152f61bead8ca58e3590d2d820f8c7d81fabd22(
    value: typing.Optional[typing.Union[Apigatewayv2IntegrationResponseParameters, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdb6f4f9737a46d2080741646f1cbbe4ecc512fbb9ca502d51f20e9342d4467a(
    *,
    server_name_to_verify: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__824f44254505d44d6d567bcac9cedb6882e39134214e808d351a5dd37ecb55d2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65da4f062f783d063c54d46230350e07704152aca93e0ace837709fefa04cad2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6738da95c1c45a7ab73a8b08210881d1a6d5cc7e019b33468114406576978fc(
    value: typing.Optional[Apigatewayv2IntegrationTlsConfig],
) -> None:
    """Type checking stubs"""
    pass
