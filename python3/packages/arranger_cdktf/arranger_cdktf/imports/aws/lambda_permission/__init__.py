'''
# `aws_lambda_permission`

Refer to the Terraform Registory for docs: [`aws_lambda_permission`](https://www.terraform.io/docs/providers/aws/r/lambda_permission).
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


class LambdaPermission(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.lambdaPermission.LambdaPermission",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission aws_lambda_permission}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        action: builtins.str,
        function_name: builtins.str,
        principal: builtins.str,
        event_source_token: typing.Optional[builtins.str] = None,
        function_url_auth_type: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        principal_org_id: typing.Optional[builtins.str] = None,
        qualifier: typing.Optional[builtins.str] = None,
        source_account: typing.Optional[builtins.str] = None,
        source_arn: typing.Optional[builtins.str] = None,
        statement_id: typing.Optional[builtins.str] = None,
        statement_id_prefix: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission aws_lambda_permission} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission#action LambdaPermission#action}.
        :param function_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission#function_name LambdaPermission#function_name}.
        :param principal: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission#principal LambdaPermission#principal}.
        :param event_source_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission#event_source_token LambdaPermission#event_source_token}.
        :param function_url_auth_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission#function_url_auth_type LambdaPermission#function_url_auth_type}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission#id LambdaPermission#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param principal_org_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission#principal_org_id LambdaPermission#principal_org_id}.
        :param qualifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission#qualifier LambdaPermission#qualifier}.
        :param source_account: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission#source_account LambdaPermission#source_account}.
        :param source_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission#source_arn LambdaPermission#source_arn}.
        :param statement_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission#statement_id LambdaPermission#statement_id}.
        :param statement_id_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission#statement_id_prefix LambdaPermission#statement_id_prefix}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ed098d3678e8a8c6848cc1c6ff62aa3029a92cddb9a8d9b8b8454f9a24e3433)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LambdaPermissionConfig(
            action=action,
            function_name=function_name,
            principal=principal,
            event_source_token=event_source_token,
            function_url_auth_type=function_url_auth_type,
            id=id,
            principal_org_id=principal_org_id,
            qualifier=qualifier,
            source_account=source_account,
            source_arn=source_arn,
            statement_id=statement_id,
            statement_id_prefix=statement_id_prefix,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetEventSourceToken")
    def reset_event_source_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventSourceToken", []))

    @jsii.member(jsii_name="resetFunctionUrlAuthType")
    def reset_function_url_auth_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFunctionUrlAuthType", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPrincipalOrgId")
    def reset_principal_org_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrincipalOrgId", []))

    @jsii.member(jsii_name="resetQualifier")
    def reset_qualifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQualifier", []))

    @jsii.member(jsii_name="resetSourceAccount")
    def reset_source_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceAccount", []))

    @jsii.member(jsii_name="resetSourceArn")
    def reset_source_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceArn", []))

    @jsii.member(jsii_name="resetStatementId")
    def reset_statement_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatementId", []))

    @jsii.member(jsii_name="resetStatementIdPrefix")
    def reset_statement_id_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatementIdPrefix", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="eventSourceTokenInput")
    def event_source_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventSourceTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="functionNameInput")
    def function_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "functionNameInput"))

    @builtins.property
    @jsii.member(jsii_name="functionUrlAuthTypeInput")
    def function_url_auth_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "functionUrlAuthTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="principalInput")
    def principal_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "principalInput"))

    @builtins.property
    @jsii.member(jsii_name="principalOrgIdInput")
    def principal_org_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "principalOrgIdInput"))

    @builtins.property
    @jsii.member(jsii_name="qualifierInput")
    def qualifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "qualifierInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceAccountInput")
    def source_account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceArnInput")
    def source_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceArnInput"))

    @builtins.property
    @jsii.member(jsii_name="statementIdInput")
    def statement_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statementIdInput"))

    @builtins.property
    @jsii.member(jsii_name="statementIdPrefixInput")
    def statement_id_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statementIdPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f696711a401f8a3e3c2f5e4e0dbdcc0e2dd36c0f901c29df8f38a1015634bbf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="eventSourceToken")
    def event_source_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventSourceToken"))

    @event_source_token.setter
    def event_source_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6178d775d6a0ce9eeb954057897b917667ac88c24579b34e8e9e35ae0a158c05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventSourceToken", value)

    @builtins.property
    @jsii.member(jsii_name="functionName")
    def function_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "functionName"))

    @function_name.setter
    def function_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e414a0513da72b03b7bb3ecdec636a9fb95c2e1fa405cba98854b54b51ee8cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functionName", value)

    @builtins.property
    @jsii.member(jsii_name="functionUrlAuthType")
    def function_url_auth_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "functionUrlAuthType"))

    @function_url_auth_type.setter
    def function_url_auth_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4c16d9b77c9a0554e77b082f60efbdaf0d0483fa0c52bbd8e7485c65c559489)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functionUrlAuthType", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24b09acf2a3eacdcea2ab1ca28279d8a570f3d2bef32c4c3ff4fd38432813fe3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="principal")
    def principal(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "principal"))

    @principal.setter
    def principal(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__717a9f6a908a0732f8177fa66fe779b8f3dfc8b9592233c5c6bfe9aa76f6dd9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "principal", value)

    @builtins.property
    @jsii.member(jsii_name="principalOrgId")
    def principal_org_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "principalOrgId"))

    @principal_org_id.setter
    def principal_org_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c29b0d97dac3d10e090a18d5a34f822d1963aab4eb7bf91b6f776c1933a42b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "principalOrgId", value)

    @builtins.property
    @jsii.member(jsii_name="qualifier")
    def qualifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "qualifier"))

    @qualifier.setter
    def qualifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50808d01da693a3a6b290c8323192d7797a5f3e6cafa6d59d2615e15bb48f899)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "qualifier", value)

    @builtins.property
    @jsii.member(jsii_name="sourceAccount")
    def source_account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceAccount"))

    @source_account.setter
    def source_account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d3291577f3145e73ab0a85eebfddfd7f5627875515c738ce71bece1bcf6d133)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceAccount", value)

    @builtins.property
    @jsii.member(jsii_name="sourceArn")
    def source_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceArn"))

    @source_arn.setter
    def source_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0dc7c8ee72ada9436fa3eba9afb1823464e581ca161dd972893c989a5cedd8b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceArn", value)

    @builtins.property
    @jsii.member(jsii_name="statementId")
    def statement_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statementId"))

    @statement_id.setter
    def statement_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8277c3c872a39b5af9c65089fe2532763c3c424f287212d659ba21e197c4c687)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statementId", value)

    @builtins.property
    @jsii.member(jsii_name="statementIdPrefix")
    def statement_id_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statementIdPrefix"))

    @statement_id_prefix.setter
    def statement_id_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19e2e8afcf3d41c7e2bc313ac6571ea797a26d2922132ea1a49c4bf4e8c13fda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statementIdPrefix", value)


@jsii.data_type(
    jsii_type="aws.lambdaPermission.LambdaPermissionConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "action": "action",
        "function_name": "functionName",
        "principal": "principal",
        "event_source_token": "eventSourceToken",
        "function_url_auth_type": "functionUrlAuthType",
        "id": "id",
        "principal_org_id": "principalOrgId",
        "qualifier": "qualifier",
        "source_account": "sourceAccount",
        "source_arn": "sourceArn",
        "statement_id": "statementId",
        "statement_id_prefix": "statementIdPrefix",
    },
)
class LambdaPermissionConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        action: builtins.str,
        function_name: builtins.str,
        principal: builtins.str,
        event_source_token: typing.Optional[builtins.str] = None,
        function_url_auth_type: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        principal_org_id: typing.Optional[builtins.str] = None,
        qualifier: typing.Optional[builtins.str] = None,
        source_account: typing.Optional[builtins.str] = None,
        source_arn: typing.Optional[builtins.str] = None,
        statement_id: typing.Optional[builtins.str] = None,
        statement_id_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission#action LambdaPermission#action}.
        :param function_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission#function_name LambdaPermission#function_name}.
        :param principal: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission#principal LambdaPermission#principal}.
        :param event_source_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission#event_source_token LambdaPermission#event_source_token}.
        :param function_url_auth_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission#function_url_auth_type LambdaPermission#function_url_auth_type}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission#id LambdaPermission#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param principal_org_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission#principal_org_id LambdaPermission#principal_org_id}.
        :param qualifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission#qualifier LambdaPermission#qualifier}.
        :param source_account: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission#source_account LambdaPermission#source_account}.
        :param source_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission#source_arn LambdaPermission#source_arn}.
        :param statement_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission#statement_id LambdaPermission#statement_id}.
        :param statement_id_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission#statement_id_prefix LambdaPermission#statement_id_prefix}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a453a991102fd01319102838038d6902c9c55880e4085a14c1abda3109ed017)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument function_name", value=function_name, expected_type=type_hints["function_name"])
            check_type(argname="argument principal", value=principal, expected_type=type_hints["principal"])
            check_type(argname="argument event_source_token", value=event_source_token, expected_type=type_hints["event_source_token"])
            check_type(argname="argument function_url_auth_type", value=function_url_auth_type, expected_type=type_hints["function_url_auth_type"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument principal_org_id", value=principal_org_id, expected_type=type_hints["principal_org_id"])
            check_type(argname="argument qualifier", value=qualifier, expected_type=type_hints["qualifier"])
            check_type(argname="argument source_account", value=source_account, expected_type=type_hints["source_account"])
            check_type(argname="argument source_arn", value=source_arn, expected_type=type_hints["source_arn"])
            check_type(argname="argument statement_id", value=statement_id, expected_type=type_hints["statement_id"])
            check_type(argname="argument statement_id_prefix", value=statement_id_prefix, expected_type=type_hints["statement_id_prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action": action,
            "function_name": function_name,
            "principal": principal,
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
        if event_source_token is not None:
            self._values["event_source_token"] = event_source_token
        if function_url_auth_type is not None:
            self._values["function_url_auth_type"] = function_url_auth_type
        if id is not None:
            self._values["id"] = id
        if principal_org_id is not None:
            self._values["principal_org_id"] = principal_org_id
        if qualifier is not None:
            self._values["qualifier"] = qualifier
        if source_account is not None:
            self._values["source_account"] = source_account
        if source_arn is not None:
            self._values["source_arn"] = source_arn
        if statement_id is not None:
            self._values["statement_id"] = statement_id
        if statement_id_prefix is not None:
            self._values["statement_id_prefix"] = statement_id_prefix

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
    def action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission#action LambdaPermission#action}.'''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def function_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission#function_name LambdaPermission#function_name}.'''
        result = self._values.get("function_name")
        assert result is not None, "Required property 'function_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def principal(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission#principal LambdaPermission#principal}.'''
        result = self._values.get("principal")
        assert result is not None, "Required property 'principal' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_source_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission#event_source_token LambdaPermission#event_source_token}.'''
        result = self._values.get("event_source_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def function_url_auth_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission#function_url_auth_type LambdaPermission#function_url_auth_type}.'''
        result = self._values.get("function_url_auth_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission#id LambdaPermission#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def principal_org_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission#principal_org_id LambdaPermission#principal_org_id}.'''
        result = self._values.get("principal_org_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def qualifier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission#qualifier LambdaPermission#qualifier}.'''
        result = self._values.get("qualifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_account(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission#source_account LambdaPermission#source_account}.'''
        result = self._values.get("source_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission#source_arn LambdaPermission#source_arn}.'''
        result = self._values.get("source_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def statement_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission#statement_id LambdaPermission#statement_id}.'''
        result = self._values.get("statement_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def statement_id_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lambda_permission#statement_id_prefix LambdaPermission#statement_id_prefix}.'''
        result = self._values.get("statement_id_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaPermissionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "LambdaPermission",
    "LambdaPermissionConfig",
]

publication.publish()

def _typecheckingstub__3ed098d3678e8a8c6848cc1c6ff62aa3029a92cddb9a8d9b8b8454f9a24e3433(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    action: builtins.str,
    function_name: builtins.str,
    principal: builtins.str,
    event_source_token: typing.Optional[builtins.str] = None,
    function_url_auth_type: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    principal_org_id: typing.Optional[builtins.str] = None,
    qualifier: typing.Optional[builtins.str] = None,
    source_account: typing.Optional[builtins.str] = None,
    source_arn: typing.Optional[builtins.str] = None,
    statement_id: typing.Optional[builtins.str] = None,
    statement_id_prefix: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__5f696711a401f8a3e3c2f5e4e0dbdcc0e2dd36c0f901c29df8f38a1015634bbf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6178d775d6a0ce9eeb954057897b917667ac88c24579b34e8e9e35ae0a158c05(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e414a0513da72b03b7bb3ecdec636a9fb95c2e1fa405cba98854b54b51ee8cf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4c16d9b77c9a0554e77b082f60efbdaf0d0483fa0c52bbd8e7485c65c559489(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24b09acf2a3eacdcea2ab1ca28279d8a570f3d2bef32c4c3ff4fd38432813fe3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__717a9f6a908a0732f8177fa66fe779b8f3dfc8b9592233c5c6bfe9aa76f6dd9b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c29b0d97dac3d10e090a18d5a34f822d1963aab4eb7bf91b6f776c1933a42b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50808d01da693a3a6b290c8323192d7797a5f3e6cafa6d59d2615e15bb48f899(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d3291577f3145e73ab0a85eebfddfd7f5627875515c738ce71bece1bcf6d133(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dc7c8ee72ada9436fa3eba9afb1823464e581ca161dd972893c989a5cedd8b1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8277c3c872a39b5af9c65089fe2532763c3c424f287212d659ba21e197c4c687(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19e2e8afcf3d41c7e2bc313ac6571ea797a26d2922132ea1a49c4bf4e8c13fda(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a453a991102fd01319102838038d6902c9c55880e4085a14c1abda3109ed017(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    action: builtins.str,
    function_name: builtins.str,
    principal: builtins.str,
    event_source_token: typing.Optional[builtins.str] = None,
    function_url_auth_type: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    principal_org_id: typing.Optional[builtins.str] = None,
    qualifier: typing.Optional[builtins.str] = None,
    source_account: typing.Optional[builtins.str] = None,
    source_arn: typing.Optional[builtins.str] = None,
    statement_id: typing.Optional[builtins.str] = None,
    statement_id_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
