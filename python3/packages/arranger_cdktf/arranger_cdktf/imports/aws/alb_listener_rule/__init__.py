'''
# `aws_alb_listener_rule`

Refer to the Terraform Registory for docs: [`aws_alb_listener_rule`](https://www.terraform.io/docs/providers/aws/r/alb_listener_rule).
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


class AlbListenerRule(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.albListenerRule.AlbListenerRule",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule aws_alb_listener_rule}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        action: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AlbListenerRuleAction", typing.Dict[builtins.str, typing.Any]]]],
        condition: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AlbListenerRuleCondition", typing.Dict[builtins.str, typing.Any]]]],
        listener_arn: builtins.str,
        id: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule aws_alb_listener_rule} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#action AlbListenerRule#action}
        :param condition: condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#condition AlbListenerRule#condition}
        :param listener_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#listener_arn AlbListenerRule#listener_arn}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#id AlbListenerRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#priority AlbListenerRule#priority}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#tags AlbListenerRule#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#tags_all AlbListenerRule#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69937200e892b0f4ed12c8e82f932d738c496ba18072dd3515fb8dcda7d085fc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AlbListenerRuleConfig(
            action=action,
            condition=condition,
            listener_arn=listener_arn,
            id=id,
            priority=priority,
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

    @jsii.member(jsii_name="putAction")
    def put_action(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AlbListenerRuleAction", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6c255c9a915a1d4a04e293cafa1a909dd31b655d5857fd0bdd0e0f01037c827)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAction", [value]))

    @jsii.member(jsii_name="putCondition")
    def put_condition(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AlbListenerRuleCondition", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ea9e795d7b838a8e4ebb0673bcf5df9e16bb4c9d09fbedc13b9ee9e266de72d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCondition", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

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
    @jsii.member(jsii_name="action")
    def action(self) -> "AlbListenerRuleActionList":
        return typing.cast("AlbListenerRuleActionList", jsii.get(self, "action"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="condition")
    def condition(self) -> "AlbListenerRuleConditionList":
        return typing.cast("AlbListenerRuleConditionList", jsii.get(self, "condition"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AlbListenerRuleAction"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AlbListenerRuleAction"]]], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="conditionInput")
    def condition_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AlbListenerRuleCondition"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AlbListenerRuleCondition"]]], jsii.get(self, "conditionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="listenerArnInput")
    def listener_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "listenerArnInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__671b254a71cdbff08e78928c3b6d781473fcec1f8a16ea1a84139c440ef120d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="listenerArn")
    def listener_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "listenerArn"))

    @listener_arn.setter
    def listener_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee430219eb99601d26cc5c7fd3197960c76df915c004e80766a0a0058459017e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "listenerArn", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79d94c93cc238491afac8d5800dacfc470982771fbb07d6920660587811a956f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__320a370dd0a65cea62d89ca97f9bd8cd8c60e878c9e500d0a2bb6328889c3909)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31370c225ad9b457fa7f8001e950cc9f4a6109abd3804a68e4d8b0aaff53bb6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.albListenerRule.AlbListenerRuleAction",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "authenticate_cognito": "authenticateCognito",
        "authenticate_oidc": "authenticateOidc",
        "fixed_response": "fixedResponse",
        "forward": "forward",
        "order": "order",
        "redirect": "redirect",
        "target_group_arn": "targetGroupArn",
    },
)
class AlbListenerRuleAction:
    def __init__(
        self,
        *,
        type: builtins.str,
        authenticate_cognito: typing.Optional[typing.Union["AlbListenerRuleActionAuthenticateCognito", typing.Dict[builtins.str, typing.Any]]] = None,
        authenticate_oidc: typing.Optional[typing.Union["AlbListenerRuleActionAuthenticateOidc", typing.Dict[builtins.str, typing.Any]]] = None,
        fixed_response: typing.Optional[typing.Union["AlbListenerRuleActionFixedResponse", typing.Dict[builtins.str, typing.Any]]] = None,
        forward: typing.Optional[typing.Union["AlbListenerRuleActionForward", typing.Dict[builtins.str, typing.Any]]] = None,
        order: typing.Optional[jsii.Number] = None,
        redirect: typing.Optional[typing.Union["AlbListenerRuleActionRedirect", typing.Dict[builtins.str, typing.Any]]] = None,
        target_group_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#type AlbListenerRule#type}.
        :param authenticate_cognito: authenticate_cognito block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#authenticate_cognito AlbListenerRule#authenticate_cognito}
        :param authenticate_oidc: authenticate_oidc block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#authenticate_oidc AlbListenerRule#authenticate_oidc}
        :param fixed_response: fixed_response block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#fixed_response AlbListenerRule#fixed_response}
        :param forward: forward block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#forward AlbListenerRule#forward}
        :param order: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#order AlbListenerRule#order}.
        :param redirect: redirect block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#redirect AlbListenerRule#redirect}
        :param target_group_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#target_group_arn AlbListenerRule#target_group_arn}.
        '''
        if isinstance(authenticate_cognito, dict):
            authenticate_cognito = AlbListenerRuleActionAuthenticateCognito(**authenticate_cognito)
        if isinstance(authenticate_oidc, dict):
            authenticate_oidc = AlbListenerRuleActionAuthenticateOidc(**authenticate_oidc)
        if isinstance(fixed_response, dict):
            fixed_response = AlbListenerRuleActionFixedResponse(**fixed_response)
        if isinstance(forward, dict):
            forward = AlbListenerRuleActionForward(**forward)
        if isinstance(redirect, dict):
            redirect = AlbListenerRuleActionRedirect(**redirect)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5cdd766126aded7c81b4ac5877687fd73bd633394330826679fd5ad69a66f80b)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument authenticate_cognito", value=authenticate_cognito, expected_type=type_hints["authenticate_cognito"])
            check_type(argname="argument authenticate_oidc", value=authenticate_oidc, expected_type=type_hints["authenticate_oidc"])
            check_type(argname="argument fixed_response", value=fixed_response, expected_type=type_hints["fixed_response"])
            check_type(argname="argument forward", value=forward, expected_type=type_hints["forward"])
            check_type(argname="argument order", value=order, expected_type=type_hints["order"])
            check_type(argname="argument redirect", value=redirect, expected_type=type_hints["redirect"])
            check_type(argname="argument target_group_arn", value=target_group_arn, expected_type=type_hints["target_group_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if authenticate_cognito is not None:
            self._values["authenticate_cognito"] = authenticate_cognito
        if authenticate_oidc is not None:
            self._values["authenticate_oidc"] = authenticate_oidc
        if fixed_response is not None:
            self._values["fixed_response"] = fixed_response
        if forward is not None:
            self._values["forward"] = forward
        if order is not None:
            self._values["order"] = order
        if redirect is not None:
            self._values["redirect"] = redirect
        if target_group_arn is not None:
            self._values["target_group_arn"] = target_group_arn

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#type AlbListenerRule#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authenticate_cognito(
        self,
    ) -> typing.Optional["AlbListenerRuleActionAuthenticateCognito"]:
        '''authenticate_cognito block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#authenticate_cognito AlbListenerRule#authenticate_cognito}
        '''
        result = self._values.get("authenticate_cognito")
        return typing.cast(typing.Optional["AlbListenerRuleActionAuthenticateCognito"], result)

    @builtins.property
    def authenticate_oidc(
        self,
    ) -> typing.Optional["AlbListenerRuleActionAuthenticateOidc"]:
        '''authenticate_oidc block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#authenticate_oidc AlbListenerRule#authenticate_oidc}
        '''
        result = self._values.get("authenticate_oidc")
        return typing.cast(typing.Optional["AlbListenerRuleActionAuthenticateOidc"], result)

    @builtins.property
    def fixed_response(self) -> typing.Optional["AlbListenerRuleActionFixedResponse"]:
        '''fixed_response block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#fixed_response AlbListenerRule#fixed_response}
        '''
        result = self._values.get("fixed_response")
        return typing.cast(typing.Optional["AlbListenerRuleActionFixedResponse"], result)

    @builtins.property
    def forward(self) -> typing.Optional["AlbListenerRuleActionForward"]:
        '''forward block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#forward AlbListenerRule#forward}
        '''
        result = self._values.get("forward")
        return typing.cast(typing.Optional["AlbListenerRuleActionForward"], result)

    @builtins.property
    def order(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#order AlbListenerRule#order}.'''
        result = self._values.get("order")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def redirect(self) -> typing.Optional["AlbListenerRuleActionRedirect"]:
        '''redirect block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#redirect AlbListenerRule#redirect}
        '''
        result = self._values.get("redirect")
        return typing.cast(typing.Optional["AlbListenerRuleActionRedirect"], result)

    @builtins.property
    def target_group_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#target_group_arn AlbListenerRule#target_group_arn}.'''
        result = self._values.get("target_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AlbListenerRuleAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.albListenerRule.AlbListenerRuleActionAuthenticateCognito",
    jsii_struct_bases=[],
    name_mapping={
        "user_pool_arn": "userPoolArn",
        "user_pool_client_id": "userPoolClientId",
        "user_pool_domain": "userPoolDomain",
        "authentication_request_extra_params": "authenticationRequestExtraParams",
        "on_unauthenticated_request": "onUnauthenticatedRequest",
        "scope": "scope",
        "session_cookie_name": "sessionCookieName",
        "session_timeout": "sessionTimeout",
    },
)
class AlbListenerRuleActionAuthenticateCognito:
    def __init__(
        self,
        *,
        user_pool_arn: builtins.str,
        user_pool_client_id: builtins.str,
        user_pool_domain: builtins.str,
        authentication_request_extra_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        on_unauthenticated_request: typing.Optional[builtins.str] = None,
        scope: typing.Optional[builtins.str] = None,
        session_cookie_name: typing.Optional[builtins.str] = None,
        session_timeout: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param user_pool_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#user_pool_arn AlbListenerRule#user_pool_arn}.
        :param user_pool_client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#user_pool_client_id AlbListenerRule#user_pool_client_id}.
        :param user_pool_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#user_pool_domain AlbListenerRule#user_pool_domain}.
        :param authentication_request_extra_params: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#authentication_request_extra_params AlbListenerRule#authentication_request_extra_params}.
        :param on_unauthenticated_request: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#on_unauthenticated_request AlbListenerRule#on_unauthenticated_request}.
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#scope AlbListenerRule#scope}.
        :param session_cookie_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#session_cookie_name AlbListenerRule#session_cookie_name}.
        :param session_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#session_timeout AlbListenerRule#session_timeout}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__977b314855bf5270f2bbe81edc7d6198c10e56ab20faf17cb1641b76a7509245)
            check_type(argname="argument user_pool_arn", value=user_pool_arn, expected_type=type_hints["user_pool_arn"])
            check_type(argname="argument user_pool_client_id", value=user_pool_client_id, expected_type=type_hints["user_pool_client_id"])
            check_type(argname="argument user_pool_domain", value=user_pool_domain, expected_type=type_hints["user_pool_domain"])
            check_type(argname="argument authentication_request_extra_params", value=authentication_request_extra_params, expected_type=type_hints["authentication_request_extra_params"])
            check_type(argname="argument on_unauthenticated_request", value=on_unauthenticated_request, expected_type=type_hints["on_unauthenticated_request"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument session_cookie_name", value=session_cookie_name, expected_type=type_hints["session_cookie_name"])
            check_type(argname="argument session_timeout", value=session_timeout, expected_type=type_hints["session_timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "user_pool_arn": user_pool_arn,
            "user_pool_client_id": user_pool_client_id,
            "user_pool_domain": user_pool_domain,
        }
        if authentication_request_extra_params is not None:
            self._values["authentication_request_extra_params"] = authentication_request_extra_params
        if on_unauthenticated_request is not None:
            self._values["on_unauthenticated_request"] = on_unauthenticated_request
        if scope is not None:
            self._values["scope"] = scope
        if session_cookie_name is not None:
            self._values["session_cookie_name"] = session_cookie_name
        if session_timeout is not None:
            self._values["session_timeout"] = session_timeout

    @builtins.property
    def user_pool_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#user_pool_arn AlbListenerRule#user_pool_arn}.'''
        result = self._values.get("user_pool_arn")
        assert result is not None, "Required property 'user_pool_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_pool_client_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#user_pool_client_id AlbListenerRule#user_pool_client_id}.'''
        result = self._values.get("user_pool_client_id")
        assert result is not None, "Required property 'user_pool_client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_pool_domain(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#user_pool_domain AlbListenerRule#user_pool_domain}.'''
        result = self._values.get("user_pool_domain")
        assert result is not None, "Required property 'user_pool_domain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authentication_request_extra_params(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#authentication_request_extra_params AlbListenerRule#authentication_request_extra_params}.'''
        result = self._values.get("authentication_request_extra_params")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def on_unauthenticated_request(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#on_unauthenticated_request AlbListenerRule#on_unauthenticated_request}.'''
        result = self._values.get("on_unauthenticated_request")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scope(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#scope AlbListenerRule#scope}.'''
        result = self._values.get("scope")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_cookie_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#session_cookie_name AlbListenerRule#session_cookie_name}.'''
        result = self._values.get("session_cookie_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#session_timeout AlbListenerRule#session_timeout}.'''
        result = self._values.get("session_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AlbListenerRuleActionAuthenticateCognito(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AlbListenerRuleActionAuthenticateCognitoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.albListenerRule.AlbListenerRuleActionAuthenticateCognitoOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b434e0787e9cbeca805e3a94b70affe881a2a01d2eeba0bf34bf54f3d7641ed9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAuthenticationRequestExtraParams")
    def reset_authentication_request_extra_params(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthenticationRequestExtraParams", []))

    @jsii.member(jsii_name="resetOnUnauthenticatedRequest")
    def reset_on_unauthenticated_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnUnauthenticatedRequest", []))

    @jsii.member(jsii_name="resetScope")
    def reset_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScope", []))

    @jsii.member(jsii_name="resetSessionCookieName")
    def reset_session_cookie_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSessionCookieName", []))

    @jsii.member(jsii_name="resetSessionTimeout")
    def reset_session_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSessionTimeout", []))

    @builtins.property
    @jsii.member(jsii_name="authenticationRequestExtraParamsInput")
    def authentication_request_extra_params_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "authenticationRequestExtraParamsInput"))

    @builtins.property
    @jsii.member(jsii_name="onUnauthenticatedRequestInput")
    def on_unauthenticated_request_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "onUnauthenticatedRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="scopeInput")
    def scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scopeInput"))

    @builtins.property
    @jsii.member(jsii_name="sessionCookieNameInput")
    def session_cookie_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sessionCookieNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sessionTimeoutInput")
    def session_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sessionTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="userPoolArnInput")
    def user_pool_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userPoolArnInput"))

    @builtins.property
    @jsii.member(jsii_name="userPoolClientIdInput")
    def user_pool_client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userPoolClientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="userPoolDomainInput")
    def user_pool_domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userPoolDomainInput"))

    @builtins.property
    @jsii.member(jsii_name="authenticationRequestExtraParams")
    def authentication_request_extra_params(
        self,
    ) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "authenticationRequestExtraParams"))

    @authentication_request_extra_params.setter
    def authentication_request_extra_params(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6608d926fa377a760c61228b449e72d3379562c841911df8ea1737873efc167b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationRequestExtraParams", value)

    @builtins.property
    @jsii.member(jsii_name="onUnauthenticatedRequest")
    def on_unauthenticated_request(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "onUnauthenticatedRequest"))

    @on_unauthenticated_request.setter
    def on_unauthenticated_request(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87bf38778aaad9a62885f98238eca025ba3a431b4e3e9ff1c989a835fb66db7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onUnauthenticatedRequest", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57a6cf7a8a2eceab97ae7bc5a8cb97cf67d624c5e9a4910a5bdc50cef763d950)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value)

    @builtins.property
    @jsii.member(jsii_name="sessionCookieName")
    def session_cookie_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sessionCookieName"))

    @session_cookie_name.setter
    def session_cookie_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23b08c022a4463634e08e3246bf9d3e2b795280996c3893bfefde0e92486616c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionCookieName", value)

    @builtins.property
    @jsii.member(jsii_name="sessionTimeout")
    def session_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sessionTimeout"))

    @session_timeout.setter
    def session_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94eb0bbac89c06d940db0cc959a216d7c2e9ab3a5bcdd8f4ec3b6a3ec45a7156)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="userPoolArn")
    def user_pool_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userPoolArn"))

    @user_pool_arn.setter
    def user_pool_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4090b2cf5e6203b5df473ebcbdc11106ce0155f8f6d900d4b9b7e6ca135e240)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userPoolArn", value)

    @builtins.property
    @jsii.member(jsii_name="userPoolClientId")
    def user_pool_client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userPoolClientId"))

    @user_pool_client_id.setter
    def user_pool_client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da279659356e68b628024d2d78c8552a3c600c28af84fbbba28ced8be59af6ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userPoolClientId", value)

    @builtins.property
    @jsii.member(jsii_name="userPoolDomain")
    def user_pool_domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userPoolDomain"))

    @user_pool_domain.setter
    def user_pool_domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__614166e07f56d3fdbb68f6ac7a87d77abb0c39684996eff5d237974b9f45e0b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userPoolDomain", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AlbListenerRuleActionAuthenticateCognito]:
        return typing.cast(typing.Optional[AlbListenerRuleActionAuthenticateCognito], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AlbListenerRuleActionAuthenticateCognito],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb2f096f87615532e13d4589d35a06138bbaa890785b34003123a74985904e7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.albListenerRule.AlbListenerRuleActionAuthenticateOidc",
    jsii_struct_bases=[],
    name_mapping={
        "authorization_endpoint": "authorizationEndpoint",
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "issuer": "issuer",
        "token_endpoint": "tokenEndpoint",
        "user_info_endpoint": "userInfoEndpoint",
        "authentication_request_extra_params": "authenticationRequestExtraParams",
        "on_unauthenticated_request": "onUnauthenticatedRequest",
        "scope": "scope",
        "session_cookie_name": "sessionCookieName",
        "session_timeout": "sessionTimeout",
    },
)
class AlbListenerRuleActionAuthenticateOidc:
    def __init__(
        self,
        *,
        authorization_endpoint: builtins.str,
        client_id: builtins.str,
        client_secret: builtins.str,
        issuer: builtins.str,
        token_endpoint: builtins.str,
        user_info_endpoint: builtins.str,
        authentication_request_extra_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        on_unauthenticated_request: typing.Optional[builtins.str] = None,
        scope: typing.Optional[builtins.str] = None,
        session_cookie_name: typing.Optional[builtins.str] = None,
        session_timeout: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param authorization_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#authorization_endpoint AlbListenerRule#authorization_endpoint}.
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#client_id AlbListenerRule#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#client_secret AlbListenerRule#client_secret}.
        :param issuer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#issuer AlbListenerRule#issuer}.
        :param token_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#token_endpoint AlbListenerRule#token_endpoint}.
        :param user_info_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#user_info_endpoint AlbListenerRule#user_info_endpoint}.
        :param authentication_request_extra_params: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#authentication_request_extra_params AlbListenerRule#authentication_request_extra_params}.
        :param on_unauthenticated_request: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#on_unauthenticated_request AlbListenerRule#on_unauthenticated_request}.
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#scope AlbListenerRule#scope}.
        :param session_cookie_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#session_cookie_name AlbListenerRule#session_cookie_name}.
        :param session_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#session_timeout AlbListenerRule#session_timeout}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03cdf55bdb7992903f2fa071e0beca93766a3034653f77621dd4285815fe2e8d)
            check_type(argname="argument authorization_endpoint", value=authorization_endpoint, expected_type=type_hints["authorization_endpoint"])
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument issuer", value=issuer, expected_type=type_hints["issuer"])
            check_type(argname="argument token_endpoint", value=token_endpoint, expected_type=type_hints["token_endpoint"])
            check_type(argname="argument user_info_endpoint", value=user_info_endpoint, expected_type=type_hints["user_info_endpoint"])
            check_type(argname="argument authentication_request_extra_params", value=authentication_request_extra_params, expected_type=type_hints["authentication_request_extra_params"])
            check_type(argname="argument on_unauthenticated_request", value=on_unauthenticated_request, expected_type=type_hints["on_unauthenticated_request"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument session_cookie_name", value=session_cookie_name, expected_type=type_hints["session_cookie_name"])
            check_type(argname="argument session_timeout", value=session_timeout, expected_type=type_hints["session_timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "authorization_endpoint": authorization_endpoint,
            "client_id": client_id,
            "client_secret": client_secret,
            "issuer": issuer,
            "token_endpoint": token_endpoint,
            "user_info_endpoint": user_info_endpoint,
        }
        if authentication_request_extra_params is not None:
            self._values["authentication_request_extra_params"] = authentication_request_extra_params
        if on_unauthenticated_request is not None:
            self._values["on_unauthenticated_request"] = on_unauthenticated_request
        if scope is not None:
            self._values["scope"] = scope
        if session_cookie_name is not None:
            self._values["session_cookie_name"] = session_cookie_name
        if session_timeout is not None:
            self._values["session_timeout"] = session_timeout

    @builtins.property
    def authorization_endpoint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#authorization_endpoint AlbListenerRule#authorization_endpoint}.'''
        result = self._values.get("authorization_endpoint")
        assert result is not None, "Required property 'authorization_endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#client_id AlbListenerRule#client_id}.'''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#client_secret AlbListenerRule#client_secret}.'''
        result = self._values.get("client_secret")
        assert result is not None, "Required property 'client_secret' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def issuer(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#issuer AlbListenerRule#issuer}.'''
        result = self._values.get("issuer")
        assert result is not None, "Required property 'issuer' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def token_endpoint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#token_endpoint AlbListenerRule#token_endpoint}.'''
        result = self._values.get("token_endpoint")
        assert result is not None, "Required property 'token_endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_info_endpoint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#user_info_endpoint AlbListenerRule#user_info_endpoint}.'''
        result = self._values.get("user_info_endpoint")
        assert result is not None, "Required property 'user_info_endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authentication_request_extra_params(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#authentication_request_extra_params AlbListenerRule#authentication_request_extra_params}.'''
        result = self._values.get("authentication_request_extra_params")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def on_unauthenticated_request(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#on_unauthenticated_request AlbListenerRule#on_unauthenticated_request}.'''
        result = self._values.get("on_unauthenticated_request")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scope(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#scope AlbListenerRule#scope}.'''
        result = self._values.get("scope")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_cookie_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#session_cookie_name AlbListenerRule#session_cookie_name}.'''
        result = self._values.get("session_cookie_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#session_timeout AlbListenerRule#session_timeout}.'''
        result = self._values.get("session_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AlbListenerRuleActionAuthenticateOidc(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AlbListenerRuleActionAuthenticateOidcOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.albListenerRule.AlbListenerRuleActionAuthenticateOidcOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8c5ad8bb7f069e085c433162d3da608688bd993495271f6b5f9be6550f93d648)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAuthenticationRequestExtraParams")
    def reset_authentication_request_extra_params(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthenticationRequestExtraParams", []))

    @jsii.member(jsii_name="resetOnUnauthenticatedRequest")
    def reset_on_unauthenticated_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnUnauthenticatedRequest", []))

    @jsii.member(jsii_name="resetScope")
    def reset_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScope", []))

    @jsii.member(jsii_name="resetSessionCookieName")
    def reset_session_cookie_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSessionCookieName", []))

    @jsii.member(jsii_name="resetSessionTimeout")
    def reset_session_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSessionTimeout", []))

    @builtins.property
    @jsii.member(jsii_name="authenticationRequestExtraParamsInput")
    def authentication_request_extra_params_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "authenticationRequestExtraParamsInput"))

    @builtins.property
    @jsii.member(jsii_name="authorizationEndpointInput")
    def authorization_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorizationEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="issuerInput")
    def issuer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "issuerInput"))

    @builtins.property
    @jsii.member(jsii_name="onUnauthenticatedRequestInput")
    def on_unauthenticated_request_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "onUnauthenticatedRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="scopeInput")
    def scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scopeInput"))

    @builtins.property
    @jsii.member(jsii_name="sessionCookieNameInput")
    def session_cookie_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sessionCookieNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sessionTimeoutInput")
    def session_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sessionTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenEndpointInput")
    def token_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="userInfoEndpointInput")
    def user_info_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userInfoEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="authenticationRequestExtraParams")
    def authentication_request_extra_params(
        self,
    ) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "authenticationRequestExtraParams"))

    @authentication_request_extra_params.setter
    def authentication_request_extra_params(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea62975687755234663adc0008d97cc465785c9e462de61c9e4babc42dd50a4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationRequestExtraParams", value)

    @builtins.property
    @jsii.member(jsii_name="authorizationEndpoint")
    def authorization_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authorizationEndpoint"))

    @authorization_endpoint.setter
    def authorization_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c2246f98c7e59b30b6ff2325c8cd6b61335f3073b6e8d4eae20b047416c8bf0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizationEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f8f4007258f016c1aa4e311ceaedc1ebd6fad5809e331843533e1566890bfc3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5c363d0fe9d58146e462b654a08a6a285114f369f9dc5e4a0c6515aeec4d4b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="issuer")
    def issuer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issuer"))

    @issuer.setter
    def issuer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6edd962f1064cd2bb3709c4bd269b0d9621798befd02143d620ac847669906d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issuer", value)

    @builtins.property
    @jsii.member(jsii_name="onUnauthenticatedRequest")
    def on_unauthenticated_request(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "onUnauthenticatedRequest"))

    @on_unauthenticated_request.setter
    def on_unauthenticated_request(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae0a4222c21f0d64d05553fee65ad0576f743036e82d33221908cd692fa6b7cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onUnauthenticatedRequest", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d86d9e6375acf6e9b96b8ada3d9b0afaf68fc053d36bb4a7f081121b05f805f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value)

    @builtins.property
    @jsii.member(jsii_name="sessionCookieName")
    def session_cookie_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sessionCookieName"))

    @session_cookie_name.setter
    def session_cookie_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2776570fdaa28a5066bff646a59e66b7f6d6ac9c19ed51460760b8502d1e6bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionCookieName", value)

    @builtins.property
    @jsii.member(jsii_name="sessionTimeout")
    def session_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sessionTimeout"))

    @session_timeout.setter
    def session_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b07f7a72e71380ca030ffc5449bd637697b1f3b89cfb2d51056f8e9e4b1b960e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="tokenEndpoint")
    def token_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tokenEndpoint"))

    @token_endpoint.setter
    def token_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0975a06e58e77aa3ab09d2676d520fad284a42e9d294271597ee9dbbada59db4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="userInfoEndpoint")
    def user_info_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userInfoEndpoint"))

    @user_info_endpoint.setter
    def user_info_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa2f7cb419a01a50eeeb1d6ba2252f1682a14473dd3bedbceffc312c83a156d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userInfoEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AlbListenerRuleActionAuthenticateOidc]:
        return typing.cast(typing.Optional[AlbListenerRuleActionAuthenticateOidc], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AlbListenerRuleActionAuthenticateOidc],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2263d99212521d5fa95f4ff779d8cf87deea0f88730316171ab9816f9d6e3bb0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.albListenerRule.AlbListenerRuleActionFixedResponse",
    jsii_struct_bases=[],
    name_mapping={
        "content_type": "contentType",
        "message_body": "messageBody",
        "status_code": "statusCode",
    },
)
class AlbListenerRuleActionFixedResponse:
    def __init__(
        self,
        *,
        content_type: builtins.str,
        message_body: typing.Optional[builtins.str] = None,
        status_code: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#content_type AlbListenerRule#content_type}.
        :param message_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#message_body AlbListenerRule#message_body}.
        :param status_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#status_code AlbListenerRule#status_code}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a562e0c18fe58aab012d7bf62c2dfafb84832043cb63fe6ef0b711009327ea9e)
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument message_body", value=message_body, expected_type=type_hints["message_body"])
            check_type(argname="argument status_code", value=status_code, expected_type=type_hints["status_code"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "content_type": content_type,
        }
        if message_body is not None:
            self._values["message_body"] = message_body
        if status_code is not None:
            self._values["status_code"] = status_code

    @builtins.property
    def content_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#content_type AlbListenerRule#content_type}.'''
        result = self._values.get("content_type")
        assert result is not None, "Required property 'content_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def message_body(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#message_body AlbListenerRule#message_body}.'''
        result = self._values.get("message_body")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status_code(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#status_code AlbListenerRule#status_code}.'''
        result = self._values.get("status_code")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AlbListenerRuleActionFixedResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AlbListenerRuleActionFixedResponseOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.albListenerRule.AlbListenerRuleActionFixedResponseOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__97df3502d248b7773f51f4a04a50ac754828885aa2941b370edbe37c7461943e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMessageBody")
    def reset_message_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessageBody", []))

    @jsii.member(jsii_name="resetStatusCode")
    def reset_status_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatusCode", []))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="messageBodyInput")
    def message_body_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageBodyInput"))

    @builtins.property
    @jsii.member(jsii_name="statusCodeInput")
    def status_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0772b9586535d714e96c85ce6fe3b765517b164c5980b84381c09db4f3ddd96b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="messageBody")
    def message_body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "messageBody"))

    @message_body.setter
    def message_body(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f983e390282a73db3c8160b0cb4370cde73636764155840b3f72517ae202ebb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messageBody", value)

    @builtins.property
    @jsii.member(jsii_name="statusCode")
    def status_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statusCode"))

    @status_code.setter
    def status_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d619f7e3544f8072cc03490939d94cc24d0c1e7c59bd5ba2b0498b53fbe2e556)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statusCode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AlbListenerRuleActionFixedResponse]:
        return typing.cast(typing.Optional[AlbListenerRuleActionFixedResponse], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AlbListenerRuleActionFixedResponse],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a937559973ae74cab20a12b2ac7886497b41079d71b5b654b5f8ffeed9bbd4de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.albListenerRule.AlbListenerRuleActionForward",
    jsii_struct_bases=[],
    name_mapping={"target_group": "targetGroup", "stickiness": "stickiness"},
)
class AlbListenerRuleActionForward:
    def __init__(
        self,
        *,
        target_group: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AlbListenerRuleActionForwardTargetGroup", typing.Dict[builtins.str, typing.Any]]]],
        stickiness: typing.Optional[typing.Union["AlbListenerRuleActionForwardStickiness", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param target_group: target_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#target_group AlbListenerRule#target_group}
        :param stickiness: stickiness block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#stickiness AlbListenerRule#stickiness}
        '''
        if isinstance(stickiness, dict):
            stickiness = AlbListenerRuleActionForwardStickiness(**stickiness)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7df073273f0fc53b93177c0212fccb05ef98fb7627d2e2ded53155e34458f91b)
            check_type(argname="argument target_group", value=target_group, expected_type=type_hints["target_group"])
            check_type(argname="argument stickiness", value=stickiness, expected_type=type_hints["stickiness"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "target_group": target_group,
        }
        if stickiness is not None:
            self._values["stickiness"] = stickiness

    @builtins.property
    def target_group(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AlbListenerRuleActionForwardTargetGroup"]]:
        '''target_group block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#target_group AlbListenerRule#target_group}
        '''
        result = self._values.get("target_group")
        assert result is not None, "Required property 'target_group' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AlbListenerRuleActionForwardTargetGroup"]], result)

    @builtins.property
    def stickiness(self) -> typing.Optional["AlbListenerRuleActionForwardStickiness"]:
        '''stickiness block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#stickiness AlbListenerRule#stickiness}
        '''
        result = self._values.get("stickiness")
        return typing.cast(typing.Optional["AlbListenerRuleActionForwardStickiness"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AlbListenerRuleActionForward(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AlbListenerRuleActionForwardOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.albListenerRule.AlbListenerRuleActionForwardOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c23070da42572e7d9a501dc135362bd2803fdf9a9d5b432d6c36b3504f641a7d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putStickiness")
    def put_stickiness(
        self,
        *,
        duration: jsii.Number,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#duration AlbListenerRule#duration}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#enabled AlbListenerRule#enabled}.
        '''
        value = AlbListenerRuleActionForwardStickiness(
            duration=duration, enabled=enabled
        )

        return typing.cast(None, jsii.invoke(self, "putStickiness", [value]))

    @jsii.member(jsii_name="putTargetGroup")
    def put_target_group(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AlbListenerRuleActionForwardTargetGroup", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcf7dc4f6ed3746a1b9912b28743df144f4ed5a423d14439dc988d25785f732e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTargetGroup", [value]))

    @jsii.member(jsii_name="resetStickiness")
    def reset_stickiness(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStickiness", []))

    @builtins.property
    @jsii.member(jsii_name="stickiness")
    def stickiness(self) -> "AlbListenerRuleActionForwardStickinessOutputReference":
        return typing.cast("AlbListenerRuleActionForwardStickinessOutputReference", jsii.get(self, "stickiness"))

    @builtins.property
    @jsii.member(jsii_name="targetGroup")
    def target_group(self) -> "AlbListenerRuleActionForwardTargetGroupList":
        return typing.cast("AlbListenerRuleActionForwardTargetGroupList", jsii.get(self, "targetGroup"))

    @builtins.property
    @jsii.member(jsii_name="stickinessInput")
    def stickiness_input(
        self,
    ) -> typing.Optional["AlbListenerRuleActionForwardStickiness"]:
        return typing.cast(typing.Optional["AlbListenerRuleActionForwardStickiness"], jsii.get(self, "stickinessInput"))

    @builtins.property
    @jsii.member(jsii_name="targetGroupInput")
    def target_group_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AlbListenerRuleActionForwardTargetGroup"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AlbListenerRuleActionForwardTargetGroup"]]], jsii.get(self, "targetGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AlbListenerRuleActionForward]:
        return typing.cast(typing.Optional[AlbListenerRuleActionForward], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AlbListenerRuleActionForward],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__692e9467a722274c500dee9295ebe2739e5c8f87388486b27d76408e8d9e1000)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.albListenerRule.AlbListenerRuleActionForwardStickiness",
    jsii_struct_bases=[],
    name_mapping={"duration": "duration", "enabled": "enabled"},
)
class AlbListenerRuleActionForwardStickiness:
    def __init__(
        self,
        *,
        duration: jsii.Number,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#duration AlbListenerRule#duration}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#enabled AlbListenerRule#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a282e6b8432605bd6797d0bc51071388a5a6e050d268518e8c1231b5db32afe)
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "duration": duration,
        }
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def duration(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#duration AlbListenerRule#duration}.'''
        result = self._values.get("duration")
        assert result is not None, "Required property 'duration' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#enabled AlbListenerRule#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AlbListenerRuleActionForwardStickiness(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AlbListenerRuleActionForwardStickinessOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.albListenerRule.AlbListenerRuleActionForwardStickinessOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__72795f053a482bfeeee2452796727b4677dfc6b790bbf33b8040e368d82fae1e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="durationInput")
    def duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "durationInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="duration")
    def duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "duration"))

    @duration.setter
    def duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70e766c0c909e1a0f0ffa71163809c0713194dbc31678414b231a78ad12bde21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "duration", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__8b264cbf44e071da8d4deccebceebed5da23dc423c678f0b86b8c5a85b44f0ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AlbListenerRuleActionForwardStickiness]:
        return typing.cast(typing.Optional[AlbListenerRuleActionForwardStickiness], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AlbListenerRuleActionForwardStickiness],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__677c7a1ace33c6978ca327f7c73324ebf54598b9b352e853501f83bf5adb88eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.albListenerRule.AlbListenerRuleActionForwardTargetGroup",
    jsii_struct_bases=[],
    name_mapping={"arn": "arn", "weight": "weight"},
)
class AlbListenerRuleActionForwardTargetGroup:
    def __init__(
        self,
        *,
        arn: builtins.str,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#arn AlbListenerRule#arn}.
        :param weight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#weight AlbListenerRule#weight}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8e04378daf8e413eccceb608c3952d5810cdaa31487a877280ed494b80f103f)
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "arn": arn,
        }
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#arn AlbListenerRule#arn}.'''
        result = self._values.get("arn")
        assert result is not None, "Required property 'arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#weight AlbListenerRule#weight}.'''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AlbListenerRuleActionForwardTargetGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AlbListenerRuleActionForwardTargetGroupList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.albListenerRule.AlbListenerRuleActionForwardTargetGroupList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9f6e297546ded866fbdaedf61d92e7bde409703237329206539bdb4f5da3c611)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AlbListenerRuleActionForwardTargetGroupOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b970e29312f334e97f38248064764dca9a85f1476ef95bda73898a49b05d86c4)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AlbListenerRuleActionForwardTargetGroupOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c5521a480151250bfb764eb013370dfc7e06c03f16e34333e026a58c671f8df)
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
            type_hints = typing.get_type_hints(_typecheckingstub__601180fea6ab763f27fb4f07126cd4fab7c515a526017b809d827b16caa3d75c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1a54c1c3a30c1922b532e6d018ed71d0216065da8006c2280fb3c2bcb13e9a78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AlbListenerRuleActionForwardTargetGroup]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AlbListenerRuleActionForwardTargetGroup]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AlbListenerRuleActionForwardTargetGroup]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__115e7a39afa3d09e77a33425152f1d57f60cd98d4aeac4315ab2c047321d0d03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AlbListenerRuleActionForwardTargetGroupOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.albListenerRule.AlbListenerRuleActionForwardTargetGroupOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__56503b3748bdb5978541380a76cb886f163af2e307b73b5a2a62acefaba2e0f5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetWeight")
    def reset_weight(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeight", []))

    @builtins.property
    @jsii.member(jsii_name="arnInput")
    def arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "arnInput"))

    @builtins.property
    @jsii.member(jsii_name="weightInput")
    def weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightInput"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @arn.setter
    def arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c37fd9b5299df99065d3954676dfd9c35278e06bb62fca3a8f613aa9d2065fb3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arn", value)

    @builtins.property
    @jsii.member(jsii_name="weight")
    def weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weight"))

    @weight.setter
    def weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b00794c9580376f2b3a22232acfd717c1bca3e642bdbd6cb55b9ea0706e2e79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weight", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AlbListenerRuleActionForwardTargetGroup, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AlbListenerRuleActionForwardTargetGroup, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AlbListenerRuleActionForwardTargetGroup, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a41fc833c78c60734e4b738295e0b8320d1afe35a00a1e8b88196bfd1b268959)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AlbListenerRuleActionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.albListenerRule.AlbListenerRuleActionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__47f2301fa8b5450e73c59de2618eeab99e367b0b1fccef4d0a3a0d9ad21c1e7c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AlbListenerRuleActionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b10e39a396dd34442b28592389abf141bb6bec3098559902ce7704373dc2f77)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AlbListenerRuleActionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__228669efdb954c450e2ebc3b479b409557b758b630013ec7ab703709dd6f0de0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__111c715487f79bc93460eabf57666581311ec93ebcc078e0f188da978a47fa5d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7fca9b80979de55418ffd022b1e3bc813f2ecfc5a0c83b67d58e19e88f6b4c55)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AlbListenerRuleAction]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AlbListenerRuleAction]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AlbListenerRuleAction]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dcee98a8b3b51c26913d14406573c624e5471585f26ad33daf691e85ebc1bc6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AlbListenerRuleActionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.albListenerRule.AlbListenerRuleActionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__135dc82903f0f55bf0dfa374f05c0b7521b27942fa2a39254720f0bdafbdfff4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAuthenticateCognito")
    def put_authenticate_cognito(
        self,
        *,
        user_pool_arn: builtins.str,
        user_pool_client_id: builtins.str,
        user_pool_domain: builtins.str,
        authentication_request_extra_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        on_unauthenticated_request: typing.Optional[builtins.str] = None,
        scope: typing.Optional[builtins.str] = None,
        session_cookie_name: typing.Optional[builtins.str] = None,
        session_timeout: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param user_pool_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#user_pool_arn AlbListenerRule#user_pool_arn}.
        :param user_pool_client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#user_pool_client_id AlbListenerRule#user_pool_client_id}.
        :param user_pool_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#user_pool_domain AlbListenerRule#user_pool_domain}.
        :param authentication_request_extra_params: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#authentication_request_extra_params AlbListenerRule#authentication_request_extra_params}.
        :param on_unauthenticated_request: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#on_unauthenticated_request AlbListenerRule#on_unauthenticated_request}.
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#scope AlbListenerRule#scope}.
        :param session_cookie_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#session_cookie_name AlbListenerRule#session_cookie_name}.
        :param session_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#session_timeout AlbListenerRule#session_timeout}.
        '''
        value = AlbListenerRuleActionAuthenticateCognito(
            user_pool_arn=user_pool_arn,
            user_pool_client_id=user_pool_client_id,
            user_pool_domain=user_pool_domain,
            authentication_request_extra_params=authentication_request_extra_params,
            on_unauthenticated_request=on_unauthenticated_request,
            scope=scope,
            session_cookie_name=session_cookie_name,
            session_timeout=session_timeout,
        )

        return typing.cast(None, jsii.invoke(self, "putAuthenticateCognito", [value]))

    @jsii.member(jsii_name="putAuthenticateOidc")
    def put_authenticate_oidc(
        self,
        *,
        authorization_endpoint: builtins.str,
        client_id: builtins.str,
        client_secret: builtins.str,
        issuer: builtins.str,
        token_endpoint: builtins.str,
        user_info_endpoint: builtins.str,
        authentication_request_extra_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        on_unauthenticated_request: typing.Optional[builtins.str] = None,
        scope: typing.Optional[builtins.str] = None,
        session_cookie_name: typing.Optional[builtins.str] = None,
        session_timeout: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param authorization_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#authorization_endpoint AlbListenerRule#authorization_endpoint}.
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#client_id AlbListenerRule#client_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#client_secret AlbListenerRule#client_secret}.
        :param issuer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#issuer AlbListenerRule#issuer}.
        :param token_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#token_endpoint AlbListenerRule#token_endpoint}.
        :param user_info_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#user_info_endpoint AlbListenerRule#user_info_endpoint}.
        :param authentication_request_extra_params: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#authentication_request_extra_params AlbListenerRule#authentication_request_extra_params}.
        :param on_unauthenticated_request: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#on_unauthenticated_request AlbListenerRule#on_unauthenticated_request}.
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#scope AlbListenerRule#scope}.
        :param session_cookie_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#session_cookie_name AlbListenerRule#session_cookie_name}.
        :param session_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#session_timeout AlbListenerRule#session_timeout}.
        '''
        value = AlbListenerRuleActionAuthenticateOidc(
            authorization_endpoint=authorization_endpoint,
            client_id=client_id,
            client_secret=client_secret,
            issuer=issuer,
            token_endpoint=token_endpoint,
            user_info_endpoint=user_info_endpoint,
            authentication_request_extra_params=authentication_request_extra_params,
            on_unauthenticated_request=on_unauthenticated_request,
            scope=scope,
            session_cookie_name=session_cookie_name,
            session_timeout=session_timeout,
        )

        return typing.cast(None, jsii.invoke(self, "putAuthenticateOidc", [value]))

    @jsii.member(jsii_name="putFixedResponse")
    def put_fixed_response(
        self,
        *,
        content_type: builtins.str,
        message_body: typing.Optional[builtins.str] = None,
        status_code: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#content_type AlbListenerRule#content_type}.
        :param message_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#message_body AlbListenerRule#message_body}.
        :param status_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#status_code AlbListenerRule#status_code}.
        '''
        value = AlbListenerRuleActionFixedResponse(
            content_type=content_type,
            message_body=message_body,
            status_code=status_code,
        )

        return typing.cast(None, jsii.invoke(self, "putFixedResponse", [value]))

    @jsii.member(jsii_name="putForward")
    def put_forward(
        self,
        *,
        target_group: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AlbListenerRuleActionForwardTargetGroup, typing.Dict[builtins.str, typing.Any]]]],
        stickiness: typing.Optional[typing.Union[AlbListenerRuleActionForwardStickiness, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param target_group: target_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#target_group AlbListenerRule#target_group}
        :param stickiness: stickiness block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#stickiness AlbListenerRule#stickiness}
        '''
        value = AlbListenerRuleActionForward(
            target_group=target_group, stickiness=stickiness
        )

        return typing.cast(None, jsii.invoke(self, "putForward", [value]))

    @jsii.member(jsii_name="putRedirect")
    def put_redirect(
        self,
        *,
        status_code: builtins.str,
        host: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        port: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[builtins.str] = None,
        query: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param status_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#status_code AlbListenerRule#status_code}.
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#host AlbListenerRule#host}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#path AlbListenerRule#path}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#port AlbListenerRule#port}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#protocol AlbListenerRule#protocol}.
        :param query: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#query AlbListenerRule#query}.
        '''
        value = AlbListenerRuleActionRedirect(
            status_code=status_code,
            host=host,
            path=path,
            port=port,
            protocol=protocol,
            query=query,
        )

        return typing.cast(None, jsii.invoke(self, "putRedirect", [value]))

    @jsii.member(jsii_name="resetAuthenticateCognito")
    def reset_authenticate_cognito(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthenticateCognito", []))

    @jsii.member(jsii_name="resetAuthenticateOidc")
    def reset_authenticate_oidc(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthenticateOidc", []))

    @jsii.member(jsii_name="resetFixedResponse")
    def reset_fixed_response(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFixedResponse", []))

    @jsii.member(jsii_name="resetForward")
    def reset_forward(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForward", []))

    @jsii.member(jsii_name="resetOrder")
    def reset_order(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrder", []))

    @jsii.member(jsii_name="resetRedirect")
    def reset_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirect", []))

    @jsii.member(jsii_name="resetTargetGroupArn")
    def reset_target_group_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetGroupArn", []))

    @builtins.property
    @jsii.member(jsii_name="authenticateCognito")
    def authenticate_cognito(
        self,
    ) -> AlbListenerRuleActionAuthenticateCognitoOutputReference:
        return typing.cast(AlbListenerRuleActionAuthenticateCognitoOutputReference, jsii.get(self, "authenticateCognito"))

    @builtins.property
    @jsii.member(jsii_name="authenticateOidc")
    def authenticate_oidc(self) -> AlbListenerRuleActionAuthenticateOidcOutputReference:
        return typing.cast(AlbListenerRuleActionAuthenticateOidcOutputReference, jsii.get(self, "authenticateOidc"))

    @builtins.property
    @jsii.member(jsii_name="fixedResponse")
    def fixed_response(self) -> AlbListenerRuleActionFixedResponseOutputReference:
        return typing.cast(AlbListenerRuleActionFixedResponseOutputReference, jsii.get(self, "fixedResponse"))

    @builtins.property
    @jsii.member(jsii_name="forward")
    def forward(self) -> AlbListenerRuleActionForwardOutputReference:
        return typing.cast(AlbListenerRuleActionForwardOutputReference, jsii.get(self, "forward"))

    @builtins.property
    @jsii.member(jsii_name="redirect")
    def redirect(self) -> "AlbListenerRuleActionRedirectOutputReference":
        return typing.cast("AlbListenerRuleActionRedirectOutputReference", jsii.get(self, "redirect"))

    @builtins.property
    @jsii.member(jsii_name="authenticateCognitoInput")
    def authenticate_cognito_input(
        self,
    ) -> typing.Optional[AlbListenerRuleActionAuthenticateCognito]:
        return typing.cast(typing.Optional[AlbListenerRuleActionAuthenticateCognito], jsii.get(self, "authenticateCognitoInput"))

    @builtins.property
    @jsii.member(jsii_name="authenticateOidcInput")
    def authenticate_oidc_input(
        self,
    ) -> typing.Optional[AlbListenerRuleActionAuthenticateOidc]:
        return typing.cast(typing.Optional[AlbListenerRuleActionAuthenticateOidc], jsii.get(self, "authenticateOidcInput"))

    @builtins.property
    @jsii.member(jsii_name="fixedResponseInput")
    def fixed_response_input(
        self,
    ) -> typing.Optional[AlbListenerRuleActionFixedResponse]:
        return typing.cast(typing.Optional[AlbListenerRuleActionFixedResponse], jsii.get(self, "fixedResponseInput"))

    @builtins.property
    @jsii.member(jsii_name="forwardInput")
    def forward_input(self) -> typing.Optional[AlbListenerRuleActionForward]:
        return typing.cast(typing.Optional[AlbListenerRuleActionForward], jsii.get(self, "forwardInput"))

    @builtins.property
    @jsii.member(jsii_name="orderInput")
    def order_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "orderInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectInput")
    def redirect_input(self) -> typing.Optional["AlbListenerRuleActionRedirect"]:
        return typing.cast(typing.Optional["AlbListenerRuleActionRedirect"], jsii.get(self, "redirectInput"))

    @builtins.property
    @jsii.member(jsii_name="targetGroupArnInput")
    def target_group_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetGroupArnInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="order")
    def order(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "order"))

    @order.setter
    def order(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a324c4aed00d977ee0c04a7f3ec299232baf20f82931948404759e21300f29b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "order", value)

    @builtins.property
    @jsii.member(jsii_name="targetGroupArn")
    def target_group_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetGroupArn"))

    @target_group_arn.setter
    def target_group_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__457c98873846960b77ea2766e7d02da4f69dbc30582fb1a94dbc5f1ca322fbbe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetGroupArn", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f598f12a6e97d68488aac96e1629e589ad120e985fa07d2ae8db0f7f72e64a25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AlbListenerRuleAction, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AlbListenerRuleAction, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AlbListenerRuleAction, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1317d2cd90207c61691d8a62ad61b82e59ee9769228744388091c7a5fced26d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.albListenerRule.AlbListenerRuleActionRedirect",
    jsii_struct_bases=[],
    name_mapping={
        "status_code": "statusCode",
        "host": "host",
        "path": "path",
        "port": "port",
        "protocol": "protocol",
        "query": "query",
    },
)
class AlbListenerRuleActionRedirect:
    def __init__(
        self,
        *,
        status_code: builtins.str,
        host: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        port: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[builtins.str] = None,
        query: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param status_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#status_code AlbListenerRule#status_code}.
        :param host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#host AlbListenerRule#host}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#path AlbListenerRule#path}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#port AlbListenerRule#port}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#protocol AlbListenerRule#protocol}.
        :param query: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#query AlbListenerRule#query}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f410f66037d15fc29f5d1e91c1f2d3c0cd5adca06a3b4bedef28226998d81436)
            check_type(argname="argument status_code", value=status_code, expected_type=type_hints["status_code"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "status_code": status_code,
        }
        if host is not None:
            self._values["host"] = host
        if path is not None:
            self._values["path"] = path
        if port is not None:
            self._values["port"] = port
        if protocol is not None:
            self._values["protocol"] = protocol
        if query is not None:
            self._values["query"] = query

    @builtins.property
    def status_code(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#status_code AlbListenerRule#status_code}.'''
        result = self._values.get("status_code")
        assert result is not None, "Required property 'status_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#host AlbListenerRule#host}.'''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#path AlbListenerRule#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#port AlbListenerRule#port}.'''
        result = self._values.get("port")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#protocol AlbListenerRule#protocol}.'''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def query(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#query AlbListenerRule#query}.'''
        result = self._values.get("query")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AlbListenerRuleActionRedirect(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AlbListenerRuleActionRedirectOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.albListenerRule.AlbListenerRuleActionRedirectOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__429f4f44f52e0d022381137bc421899a6ac735d8900974cde356f31acbd1cfa1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHost")
    def reset_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHost", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetProtocol")
    def reset_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocol", []))

    @jsii.member(jsii_name="resetQuery")
    def reset_query(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQuery", []))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="statusCodeInput")
    def status_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bfeddb491455ddfc5ed925c9882107f1721312d58044b22874d8c3f61688e0f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3510fc4e85c2394bfa823f17a929ede359cb659b480c70f5eb6bcaef2d1f71ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "port"))

    @port.setter
    def port(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24a4a39c6c46369d69551ce216f77d1b24d3ef793921ccf39bf1cb9c9e28c631)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e03f99e2f625ab0b38a0937c8265843d30e2f20218fe0dbd71dbae18893e95cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68ac99a4ef9139c5b67d87d7e44f4818340529fc70fb3bbd98371f27ddeb5bf0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="statusCode")
    def status_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statusCode"))

    @status_code.setter
    def status_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e9bbb476da98897ddf684b1bd3b6b713932a5407f9b7dcdcf16620175d8e79e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statusCode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AlbListenerRuleActionRedirect]:
        return typing.cast(typing.Optional[AlbListenerRuleActionRedirect], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AlbListenerRuleActionRedirect],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4acbd27aaf3d0772fe64dacb9ea5e92747fdf2b387d9c73887b372d42706466f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.albListenerRule.AlbListenerRuleCondition",
    jsii_struct_bases=[],
    name_mapping={
        "host_header": "hostHeader",
        "http_header": "httpHeader",
        "http_request_method": "httpRequestMethod",
        "path_pattern": "pathPattern",
        "query_string": "queryString",
        "source_ip": "sourceIp",
    },
)
class AlbListenerRuleCondition:
    def __init__(
        self,
        *,
        host_header: typing.Optional[typing.Union["AlbListenerRuleConditionHostHeader", typing.Dict[builtins.str, typing.Any]]] = None,
        http_header: typing.Optional[typing.Union["AlbListenerRuleConditionHttpHeader", typing.Dict[builtins.str, typing.Any]]] = None,
        http_request_method: typing.Optional[typing.Union["AlbListenerRuleConditionHttpRequestMethod", typing.Dict[builtins.str, typing.Any]]] = None,
        path_pattern: typing.Optional[typing.Union["AlbListenerRuleConditionPathPattern", typing.Dict[builtins.str, typing.Any]]] = None,
        query_string: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AlbListenerRuleConditionQueryString", typing.Dict[builtins.str, typing.Any]]]]] = None,
        source_ip: typing.Optional[typing.Union["AlbListenerRuleConditionSourceIp", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param host_header: host_header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#host_header AlbListenerRule#host_header}
        :param http_header: http_header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#http_header AlbListenerRule#http_header}
        :param http_request_method: http_request_method block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#http_request_method AlbListenerRule#http_request_method}
        :param path_pattern: path_pattern block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#path_pattern AlbListenerRule#path_pattern}
        :param query_string: query_string block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#query_string AlbListenerRule#query_string}
        :param source_ip: source_ip block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#source_ip AlbListenerRule#source_ip}
        '''
        if isinstance(host_header, dict):
            host_header = AlbListenerRuleConditionHostHeader(**host_header)
        if isinstance(http_header, dict):
            http_header = AlbListenerRuleConditionHttpHeader(**http_header)
        if isinstance(http_request_method, dict):
            http_request_method = AlbListenerRuleConditionHttpRequestMethod(**http_request_method)
        if isinstance(path_pattern, dict):
            path_pattern = AlbListenerRuleConditionPathPattern(**path_pattern)
        if isinstance(source_ip, dict):
            source_ip = AlbListenerRuleConditionSourceIp(**source_ip)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__784a23ef9a896e28f5285025a52bfa13ae817b000dc99db89ce348fe5a747619)
            check_type(argname="argument host_header", value=host_header, expected_type=type_hints["host_header"])
            check_type(argname="argument http_header", value=http_header, expected_type=type_hints["http_header"])
            check_type(argname="argument http_request_method", value=http_request_method, expected_type=type_hints["http_request_method"])
            check_type(argname="argument path_pattern", value=path_pattern, expected_type=type_hints["path_pattern"])
            check_type(argname="argument query_string", value=query_string, expected_type=type_hints["query_string"])
            check_type(argname="argument source_ip", value=source_ip, expected_type=type_hints["source_ip"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if host_header is not None:
            self._values["host_header"] = host_header
        if http_header is not None:
            self._values["http_header"] = http_header
        if http_request_method is not None:
            self._values["http_request_method"] = http_request_method
        if path_pattern is not None:
            self._values["path_pattern"] = path_pattern
        if query_string is not None:
            self._values["query_string"] = query_string
        if source_ip is not None:
            self._values["source_ip"] = source_ip

    @builtins.property
    def host_header(self) -> typing.Optional["AlbListenerRuleConditionHostHeader"]:
        '''host_header block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#host_header AlbListenerRule#host_header}
        '''
        result = self._values.get("host_header")
        return typing.cast(typing.Optional["AlbListenerRuleConditionHostHeader"], result)

    @builtins.property
    def http_header(self) -> typing.Optional["AlbListenerRuleConditionHttpHeader"]:
        '''http_header block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#http_header AlbListenerRule#http_header}
        '''
        result = self._values.get("http_header")
        return typing.cast(typing.Optional["AlbListenerRuleConditionHttpHeader"], result)

    @builtins.property
    def http_request_method(
        self,
    ) -> typing.Optional["AlbListenerRuleConditionHttpRequestMethod"]:
        '''http_request_method block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#http_request_method AlbListenerRule#http_request_method}
        '''
        result = self._values.get("http_request_method")
        return typing.cast(typing.Optional["AlbListenerRuleConditionHttpRequestMethod"], result)

    @builtins.property
    def path_pattern(self) -> typing.Optional["AlbListenerRuleConditionPathPattern"]:
        '''path_pattern block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#path_pattern AlbListenerRule#path_pattern}
        '''
        result = self._values.get("path_pattern")
        return typing.cast(typing.Optional["AlbListenerRuleConditionPathPattern"], result)

    @builtins.property
    def query_string(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AlbListenerRuleConditionQueryString"]]]:
        '''query_string block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#query_string AlbListenerRule#query_string}
        '''
        result = self._values.get("query_string")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AlbListenerRuleConditionQueryString"]]], result)

    @builtins.property
    def source_ip(self) -> typing.Optional["AlbListenerRuleConditionSourceIp"]:
        '''source_ip block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#source_ip AlbListenerRule#source_ip}
        '''
        result = self._values.get("source_ip")
        return typing.cast(typing.Optional["AlbListenerRuleConditionSourceIp"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AlbListenerRuleCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.albListenerRule.AlbListenerRuleConditionHostHeader",
    jsii_struct_bases=[],
    name_mapping={"values": "values"},
)
class AlbListenerRuleConditionHostHeader:
    def __init__(self, *, values: typing.Sequence[builtins.str]) -> None:
        '''
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#values AlbListenerRule#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16c882a02bad1c7859be6806a3885a9404508569034d0ed9300bfc5cac1d0e8e)
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "values": values,
        }

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#values AlbListenerRule#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AlbListenerRuleConditionHostHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AlbListenerRuleConditionHostHeaderOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.albListenerRule.AlbListenerRuleConditionHostHeaderOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__73883f3ab3bf03684a350ef512fd47f03af31a5e2762e2251e41a05d633ce0b7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfeff253c88e09afe10a68038b583d81fccec60acb3787e2608a8ff81148b699)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AlbListenerRuleConditionHostHeader]:
        return typing.cast(typing.Optional[AlbListenerRuleConditionHostHeader], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AlbListenerRuleConditionHostHeader],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bec135250de57135a4c01659eb7f2a8ac194fa6e6f10d5eb242203fbf1fc12c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.albListenerRule.AlbListenerRuleConditionHttpHeader",
    jsii_struct_bases=[],
    name_mapping={"http_header_name": "httpHeaderName", "values": "values"},
)
class AlbListenerRuleConditionHttpHeader:
    def __init__(
        self,
        *,
        http_header_name: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param http_header_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#http_header_name AlbListenerRule#http_header_name}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#values AlbListenerRule#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6e2f77ba1747033627790b9d50bdbabff16b824a2316d17bd164fcfe01ae55e)
            check_type(argname="argument http_header_name", value=http_header_name, expected_type=type_hints["http_header_name"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "http_header_name": http_header_name,
            "values": values,
        }

    @builtins.property
    def http_header_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#http_header_name AlbListenerRule#http_header_name}.'''
        result = self._values.get("http_header_name")
        assert result is not None, "Required property 'http_header_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#values AlbListenerRule#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AlbListenerRuleConditionHttpHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AlbListenerRuleConditionHttpHeaderOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.albListenerRule.AlbListenerRuleConditionHttpHeaderOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a0992e8c44dc26b8ff34057ac5efbe07910fd7cbee0ccb2488562f88bb219464)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="httpHeaderNameInput")
    def http_header_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpHeaderNameInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="httpHeaderName")
    def http_header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpHeaderName"))

    @http_header_name.setter
    def http_header_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eafbaf24e9befb9407701ae15e588c537fd8a35cd53e459f254ffd982bfe001e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpHeaderName", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d478f9f4d96e83a2ade80a450719d930ee35b0e6c57f8ae6e5a6347a4e7e518)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AlbListenerRuleConditionHttpHeader]:
        return typing.cast(typing.Optional[AlbListenerRuleConditionHttpHeader], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AlbListenerRuleConditionHttpHeader],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f29320f85545ae5d14dc4fcfd6e35e003e90f6e00346b9c894069fe8c801ebbb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.albListenerRule.AlbListenerRuleConditionHttpRequestMethod",
    jsii_struct_bases=[],
    name_mapping={"values": "values"},
)
class AlbListenerRuleConditionHttpRequestMethod:
    def __init__(self, *, values: typing.Sequence[builtins.str]) -> None:
        '''
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#values AlbListenerRule#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acf32acc2664a87b58fdd675bb00d30d9059b74197c005eda99b0b2e2a35cb52)
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "values": values,
        }

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#values AlbListenerRule#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AlbListenerRuleConditionHttpRequestMethod(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AlbListenerRuleConditionHttpRequestMethodOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.albListenerRule.AlbListenerRuleConditionHttpRequestMethodOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cce66c43323f81c0f3f588efa9bfd6c1d11dc9f2de55c1ff3b34ce4372058c5a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4503bd21a00f8fa415c0615b8eb494280fba27153c32387a68eabeb0ffdc2f40)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AlbListenerRuleConditionHttpRequestMethod]:
        return typing.cast(typing.Optional[AlbListenerRuleConditionHttpRequestMethod], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AlbListenerRuleConditionHttpRequestMethod],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07bf64d6b53795e2b4de04dadea89f50c3b0771098e86120178d3cf20d9393fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AlbListenerRuleConditionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.albListenerRule.AlbListenerRuleConditionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__182158133f94dd09262b937cd9615ef288525b5988f7f9a2476afd825d4ace35)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AlbListenerRuleConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4988846f12147cfeb681e669cb9356ddf8a86bf45487835b3614b41a8266a70)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AlbListenerRuleConditionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a7ae30c1f9fc242099813cd3dcb4d7910d5beb1ca061cb605fdd3fecf0cda6b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__57a0e18b5d31307f1f9eb6fe977c497aa29a671a916b943b055063f4f35323fa)
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
            type_hints = typing.get_type_hints(_typecheckingstub__15d676ea1da295d3f45b785bdbfddbc120f34e2e38304b524c214e57ad7321df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AlbListenerRuleCondition]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AlbListenerRuleCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AlbListenerRuleCondition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bac8e7f621d0c69820bb5511b3ee7199142c81e5b8d06f8f8dd33799f4eb9710)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AlbListenerRuleConditionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.albListenerRule.AlbListenerRuleConditionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__72a76a4bb2474e59d91868a134b2c0d73c3b4726292a61a6314e82789a8518fd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putHostHeader")
    def put_host_header(self, *, values: typing.Sequence[builtins.str]) -> None:
        '''
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#values AlbListenerRule#values}.
        '''
        value = AlbListenerRuleConditionHostHeader(values=values)

        return typing.cast(None, jsii.invoke(self, "putHostHeader", [value]))

    @jsii.member(jsii_name="putHttpHeader")
    def put_http_header(
        self,
        *,
        http_header_name: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param http_header_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#http_header_name AlbListenerRule#http_header_name}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#values AlbListenerRule#values}.
        '''
        value = AlbListenerRuleConditionHttpHeader(
            http_header_name=http_header_name, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putHttpHeader", [value]))

    @jsii.member(jsii_name="putHttpRequestMethod")
    def put_http_request_method(self, *, values: typing.Sequence[builtins.str]) -> None:
        '''
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#values AlbListenerRule#values}.
        '''
        value = AlbListenerRuleConditionHttpRequestMethod(values=values)

        return typing.cast(None, jsii.invoke(self, "putHttpRequestMethod", [value]))

    @jsii.member(jsii_name="putPathPattern")
    def put_path_pattern(self, *, values: typing.Sequence[builtins.str]) -> None:
        '''
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#values AlbListenerRule#values}.
        '''
        value = AlbListenerRuleConditionPathPattern(values=values)

        return typing.cast(None, jsii.invoke(self, "putPathPattern", [value]))

    @jsii.member(jsii_name="putQueryString")
    def put_query_string(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["AlbListenerRuleConditionQueryString", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e473c054124f04b670e6a5db3198e037baa4e1ea5f280f8f800c6b7ecb8033ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putQueryString", [value]))

    @jsii.member(jsii_name="putSourceIp")
    def put_source_ip(self, *, values: typing.Sequence[builtins.str]) -> None:
        '''
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#values AlbListenerRule#values}.
        '''
        value = AlbListenerRuleConditionSourceIp(values=values)

        return typing.cast(None, jsii.invoke(self, "putSourceIp", [value]))

    @jsii.member(jsii_name="resetHostHeader")
    def reset_host_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostHeader", []))

    @jsii.member(jsii_name="resetHttpHeader")
    def reset_http_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpHeader", []))

    @jsii.member(jsii_name="resetHttpRequestMethod")
    def reset_http_request_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpRequestMethod", []))

    @jsii.member(jsii_name="resetPathPattern")
    def reset_path_pattern(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPathPattern", []))

    @jsii.member(jsii_name="resetQueryString")
    def reset_query_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryString", []))

    @jsii.member(jsii_name="resetSourceIp")
    def reset_source_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceIp", []))

    @builtins.property
    @jsii.member(jsii_name="hostHeader")
    def host_header(self) -> AlbListenerRuleConditionHostHeaderOutputReference:
        return typing.cast(AlbListenerRuleConditionHostHeaderOutputReference, jsii.get(self, "hostHeader"))

    @builtins.property
    @jsii.member(jsii_name="httpHeader")
    def http_header(self) -> AlbListenerRuleConditionHttpHeaderOutputReference:
        return typing.cast(AlbListenerRuleConditionHttpHeaderOutputReference, jsii.get(self, "httpHeader"))

    @builtins.property
    @jsii.member(jsii_name="httpRequestMethod")
    def http_request_method(
        self,
    ) -> AlbListenerRuleConditionHttpRequestMethodOutputReference:
        return typing.cast(AlbListenerRuleConditionHttpRequestMethodOutputReference, jsii.get(self, "httpRequestMethod"))

    @builtins.property
    @jsii.member(jsii_name="pathPattern")
    def path_pattern(self) -> "AlbListenerRuleConditionPathPatternOutputReference":
        return typing.cast("AlbListenerRuleConditionPathPatternOutputReference", jsii.get(self, "pathPattern"))

    @builtins.property
    @jsii.member(jsii_name="queryString")
    def query_string(self) -> "AlbListenerRuleConditionQueryStringList":
        return typing.cast("AlbListenerRuleConditionQueryStringList", jsii.get(self, "queryString"))

    @builtins.property
    @jsii.member(jsii_name="sourceIp")
    def source_ip(self) -> "AlbListenerRuleConditionSourceIpOutputReference":
        return typing.cast("AlbListenerRuleConditionSourceIpOutputReference", jsii.get(self, "sourceIp"))

    @builtins.property
    @jsii.member(jsii_name="hostHeaderInput")
    def host_header_input(self) -> typing.Optional[AlbListenerRuleConditionHostHeader]:
        return typing.cast(typing.Optional[AlbListenerRuleConditionHostHeader], jsii.get(self, "hostHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="httpHeaderInput")
    def http_header_input(self) -> typing.Optional[AlbListenerRuleConditionHttpHeader]:
        return typing.cast(typing.Optional[AlbListenerRuleConditionHttpHeader], jsii.get(self, "httpHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="httpRequestMethodInput")
    def http_request_method_input(
        self,
    ) -> typing.Optional[AlbListenerRuleConditionHttpRequestMethod]:
        return typing.cast(typing.Optional[AlbListenerRuleConditionHttpRequestMethod], jsii.get(self, "httpRequestMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="pathPatternInput")
    def path_pattern_input(
        self,
    ) -> typing.Optional["AlbListenerRuleConditionPathPattern"]:
        return typing.cast(typing.Optional["AlbListenerRuleConditionPathPattern"], jsii.get(self, "pathPatternInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringInput")
    def query_string_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AlbListenerRuleConditionQueryString"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["AlbListenerRuleConditionQueryString"]]], jsii.get(self, "queryStringInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceIpInput")
    def source_ip_input(self) -> typing.Optional["AlbListenerRuleConditionSourceIp"]:
        return typing.cast(typing.Optional["AlbListenerRuleConditionSourceIp"], jsii.get(self, "sourceIpInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AlbListenerRuleCondition, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AlbListenerRuleCondition, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AlbListenerRuleCondition, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71b8d4a9a7cbe4e3b7b8508cc6434662086a77fe41c26e5aed7046a95d66c3ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.albListenerRule.AlbListenerRuleConditionPathPattern",
    jsii_struct_bases=[],
    name_mapping={"values": "values"},
)
class AlbListenerRuleConditionPathPattern:
    def __init__(self, *, values: typing.Sequence[builtins.str]) -> None:
        '''
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#values AlbListenerRule#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__916fd9f36f0f990c10bdcedff10e6bffe4f61a44a981d26e9d7589ce8282cb66)
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "values": values,
        }

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#values AlbListenerRule#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AlbListenerRuleConditionPathPattern(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AlbListenerRuleConditionPathPatternOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.albListenerRule.AlbListenerRuleConditionPathPatternOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__45eb845909599ecdc49c74e4b78677cda4c9a0962c4fdb17d08630cc6ab8968f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d9ca857f13ac8b3e07e4625b769b4e50c5f5ca172210ec35f4726ba97d22968)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AlbListenerRuleConditionPathPattern]:
        return typing.cast(typing.Optional[AlbListenerRuleConditionPathPattern], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AlbListenerRuleConditionPathPattern],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a2188763957e715e278fcd2b6afe70109d70422d1148263727c2194d61c0863)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.albListenerRule.AlbListenerRuleConditionQueryString",
    jsii_struct_bases=[],
    name_mapping={"value": "value", "key": "key"},
)
class AlbListenerRuleConditionQueryString:
    def __init__(
        self,
        *,
        value: builtins.str,
        key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#value AlbListenerRule#value}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#key AlbListenerRule#key}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f7b87973ce3c06f81333a9e4a121ed314d61da889356c8ce0857ac0f18dcf32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "value": value,
        }
        if key is not None:
            self._values["key"] = key

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#value AlbListenerRule#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#key AlbListenerRule#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AlbListenerRuleConditionQueryString(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AlbListenerRuleConditionQueryStringList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.albListenerRule.AlbListenerRuleConditionQueryStringList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0763822872e2f0b3c28f142b0055996ffd30dff4fa0122c423ddfcce038dd944)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AlbListenerRuleConditionQueryStringOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58b6bd9b0b958389ebd4e8f74614bf811ed861721cda945608cb58e2711109e8)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AlbListenerRuleConditionQueryStringOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf26d6fdc213af58a9f8b7d67e0f16167dc9df09425e2035d8d680dc2e5a0093)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3179c524f873d14100caf11c4e74440a58537d2f45f7c1738ffa538e5bfc70c8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__958eb59e9b3782b4703f45a69ca2a4746a971127df425d94136f5a1282f3cc21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AlbListenerRuleConditionQueryString]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AlbListenerRuleConditionQueryString]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AlbListenerRuleConditionQueryString]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__191e61fff54c186fc5819bc11461e664f3069c644107f0286dc893ed90078a93)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AlbListenerRuleConditionQueryStringOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.albListenerRule.AlbListenerRuleConditionQueryStringOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__95baf01310e6f3376f55d80a46c3f3ad892521e7ca6d0a519d738b734c4da570)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97c7ce5b119571ad8b6951e7d4a2d057e7440d449ca67c63419455f7b093dfc2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__285737e54b0a2a9300bf2eed6d86a80f098874df7da4ec9a7a2d99ddcf3fb7ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AlbListenerRuleConditionQueryString, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AlbListenerRuleConditionQueryString, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AlbListenerRuleConditionQueryString, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95928be1ebc4386e1db223d779ff66def3695bb8b5be3701053a8a09e8fa8590)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.albListenerRule.AlbListenerRuleConditionSourceIp",
    jsii_struct_bases=[],
    name_mapping={"values": "values"},
)
class AlbListenerRuleConditionSourceIp:
    def __init__(self, *, values: typing.Sequence[builtins.str]) -> None:
        '''
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#values AlbListenerRule#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed14cc1755e72506f553d0a2dde9e360c75fcca85c590036f11c74f52b72bea0)
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "values": values,
        }

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#values AlbListenerRule#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AlbListenerRuleConditionSourceIp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AlbListenerRuleConditionSourceIpOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.albListenerRule.AlbListenerRuleConditionSourceIpOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2d58599f412178c1e32c0c61d2b767285812cec97f9f72a44dcae97a0c95f3d0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40a6bb4ddaaff75624bb7ccb2026d3955c6cd4130da14cbd2a4c49e2302a0aaa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AlbListenerRuleConditionSourceIp]:
        return typing.cast(typing.Optional[AlbListenerRuleConditionSourceIp], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AlbListenerRuleConditionSourceIp],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__957ebc08ed8f5318119e3846537cfe778c1e25ba1cc6dd8a19b987d31ed8c408)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.albListenerRule.AlbListenerRuleConfig",
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
        "condition": "condition",
        "listener_arn": "listenerArn",
        "id": "id",
        "priority": "priority",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class AlbListenerRuleConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        action: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AlbListenerRuleAction, typing.Dict[builtins.str, typing.Any]]]],
        condition: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AlbListenerRuleCondition, typing.Dict[builtins.str, typing.Any]]]],
        listener_arn: builtins.str,
        id: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
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
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#action AlbListenerRule#action}
        :param condition: condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#condition AlbListenerRule#condition}
        :param listener_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#listener_arn AlbListenerRule#listener_arn}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#id AlbListenerRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#priority AlbListenerRule#priority}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#tags AlbListenerRule#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#tags_all AlbListenerRule#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc9a09c2413e844ca50a729526d0ff5105bebdbb9c39f56696accbfa8fd02ef3)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
            check_type(argname="argument listener_arn", value=listener_arn, expected_type=type_hints["listener_arn"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action": action,
            "condition": condition,
            "listener_arn": listener_arn,
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
        if priority is not None:
            self._values["priority"] = priority
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
    def action(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AlbListenerRuleAction]]:
        '''action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#action AlbListenerRule#action}
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AlbListenerRuleAction]], result)

    @builtins.property
    def condition(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AlbListenerRuleCondition]]:
        '''condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#condition AlbListenerRule#condition}
        '''
        result = self._values.get("condition")
        assert result is not None, "Required property 'condition' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AlbListenerRuleCondition]], result)

    @builtins.property
    def listener_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#listener_arn AlbListenerRule#listener_arn}.'''
        result = self._values.get("listener_arn")
        assert result is not None, "Required property 'listener_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#id AlbListenerRule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#priority AlbListenerRule#priority}.'''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#tags AlbListenerRule#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/alb_listener_rule#tags_all AlbListenerRule#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AlbListenerRuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AlbListenerRule",
    "AlbListenerRuleAction",
    "AlbListenerRuleActionAuthenticateCognito",
    "AlbListenerRuleActionAuthenticateCognitoOutputReference",
    "AlbListenerRuleActionAuthenticateOidc",
    "AlbListenerRuleActionAuthenticateOidcOutputReference",
    "AlbListenerRuleActionFixedResponse",
    "AlbListenerRuleActionFixedResponseOutputReference",
    "AlbListenerRuleActionForward",
    "AlbListenerRuleActionForwardOutputReference",
    "AlbListenerRuleActionForwardStickiness",
    "AlbListenerRuleActionForwardStickinessOutputReference",
    "AlbListenerRuleActionForwardTargetGroup",
    "AlbListenerRuleActionForwardTargetGroupList",
    "AlbListenerRuleActionForwardTargetGroupOutputReference",
    "AlbListenerRuleActionList",
    "AlbListenerRuleActionOutputReference",
    "AlbListenerRuleActionRedirect",
    "AlbListenerRuleActionRedirectOutputReference",
    "AlbListenerRuleCondition",
    "AlbListenerRuleConditionHostHeader",
    "AlbListenerRuleConditionHostHeaderOutputReference",
    "AlbListenerRuleConditionHttpHeader",
    "AlbListenerRuleConditionHttpHeaderOutputReference",
    "AlbListenerRuleConditionHttpRequestMethod",
    "AlbListenerRuleConditionHttpRequestMethodOutputReference",
    "AlbListenerRuleConditionList",
    "AlbListenerRuleConditionOutputReference",
    "AlbListenerRuleConditionPathPattern",
    "AlbListenerRuleConditionPathPatternOutputReference",
    "AlbListenerRuleConditionQueryString",
    "AlbListenerRuleConditionQueryStringList",
    "AlbListenerRuleConditionQueryStringOutputReference",
    "AlbListenerRuleConditionSourceIp",
    "AlbListenerRuleConditionSourceIpOutputReference",
    "AlbListenerRuleConfig",
]

publication.publish()

def _typecheckingstub__69937200e892b0f4ed12c8e82f932d738c496ba18072dd3515fb8dcda7d085fc(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    action: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AlbListenerRuleAction, typing.Dict[builtins.str, typing.Any]]]],
    condition: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AlbListenerRuleCondition, typing.Dict[builtins.str, typing.Any]]]],
    listener_arn: builtins.str,
    id: typing.Optional[builtins.str] = None,
    priority: typing.Optional[jsii.Number] = None,
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

def _typecheckingstub__a6c255c9a915a1d4a04e293cafa1a909dd31b655d5857fd0bdd0e0f01037c827(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AlbListenerRuleAction, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ea9e795d7b838a8e4ebb0673bcf5df9e16bb4c9d09fbedc13b9ee9e266de72d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AlbListenerRuleCondition, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__671b254a71cdbff08e78928c3b6d781473fcec1f8a16ea1a84139c440ef120d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee430219eb99601d26cc5c7fd3197960c76df915c004e80766a0a0058459017e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79d94c93cc238491afac8d5800dacfc470982771fbb07d6920660587811a956f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__320a370dd0a65cea62d89ca97f9bd8cd8c60e878c9e500d0a2bb6328889c3909(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31370c225ad9b457fa7f8001e950cc9f4a6109abd3804a68e4d8b0aaff53bb6a(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cdd766126aded7c81b4ac5877687fd73bd633394330826679fd5ad69a66f80b(
    *,
    type: builtins.str,
    authenticate_cognito: typing.Optional[typing.Union[AlbListenerRuleActionAuthenticateCognito, typing.Dict[builtins.str, typing.Any]]] = None,
    authenticate_oidc: typing.Optional[typing.Union[AlbListenerRuleActionAuthenticateOidc, typing.Dict[builtins.str, typing.Any]]] = None,
    fixed_response: typing.Optional[typing.Union[AlbListenerRuleActionFixedResponse, typing.Dict[builtins.str, typing.Any]]] = None,
    forward: typing.Optional[typing.Union[AlbListenerRuleActionForward, typing.Dict[builtins.str, typing.Any]]] = None,
    order: typing.Optional[jsii.Number] = None,
    redirect: typing.Optional[typing.Union[AlbListenerRuleActionRedirect, typing.Dict[builtins.str, typing.Any]]] = None,
    target_group_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__977b314855bf5270f2bbe81edc7d6198c10e56ab20faf17cb1641b76a7509245(
    *,
    user_pool_arn: builtins.str,
    user_pool_client_id: builtins.str,
    user_pool_domain: builtins.str,
    authentication_request_extra_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    on_unauthenticated_request: typing.Optional[builtins.str] = None,
    scope: typing.Optional[builtins.str] = None,
    session_cookie_name: typing.Optional[builtins.str] = None,
    session_timeout: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b434e0787e9cbeca805e3a94b70affe881a2a01d2eeba0bf34bf54f3d7641ed9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6608d926fa377a760c61228b449e72d3379562c841911df8ea1737873efc167b(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87bf38778aaad9a62885f98238eca025ba3a431b4e3e9ff1c989a835fb66db7b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57a6cf7a8a2eceab97ae7bc5a8cb97cf67d624c5e9a4910a5bdc50cef763d950(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23b08c022a4463634e08e3246bf9d3e2b795280996c3893bfefde0e92486616c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94eb0bbac89c06d940db0cc959a216d7c2e9ab3a5bcdd8f4ec3b6a3ec45a7156(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4090b2cf5e6203b5df473ebcbdc11106ce0155f8f6d900d4b9b7e6ca135e240(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da279659356e68b628024d2d78c8552a3c600c28af84fbbba28ced8be59af6ec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__614166e07f56d3fdbb68f6ac7a87d77abb0c39684996eff5d237974b9f45e0b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb2f096f87615532e13d4589d35a06138bbaa890785b34003123a74985904e7c(
    value: typing.Optional[AlbListenerRuleActionAuthenticateCognito],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03cdf55bdb7992903f2fa071e0beca93766a3034653f77621dd4285815fe2e8d(
    *,
    authorization_endpoint: builtins.str,
    client_id: builtins.str,
    client_secret: builtins.str,
    issuer: builtins.str,
    token_endpoint: builtins.str,
    user_info_endpoint: builtins.str,
    authentication_request_extra_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    on_unauthenticated_request: typing.Optional[builtins.str] = None,
    scope: typing.Optional[builtins.str] = None,
    session_cookie_name: typing.Optional[builtins.str] = None,
    session_timeout: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c5ad8bb7f069e085c433162d3da608688bd993495271f6b5f9be6550f93d648(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea62975687755234663adc0008d97cc465785c9e462de61c9e4babc42dd50a4a(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c2246f98c7e59b30b6ff2325c8cd6b61335f3073b6e8d4eae20b047416c8bf0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f8f4007258f016c1aa4e311ceaedc1ebd6fad5809e331843533e1566890bfc3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5c363d0fe9d58146e462b654a08a6a285114f369f9dc5e4a0c6515aeec4d4b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6edd962f1064cd2bb3709c4bd269b0d9621798befd02143d620ac847669906d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae0a4222c21f0d64d05553fee65ad0576f743036e82d33221908cd692fa6b7cc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d86d9e6375acf6e9b96b8ada3d9b0afaf68fc053d36bb4a7f081121b05f805f2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2776570fdaa28a5066bff646a59e66b7f6d6ac9c19ed51460760b8502d1e6bd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b07f7a72e71380ca030ffc5449bd637697b1f3b89cfb2d51056f8e9e4b1b960e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0975a06e58e77aa3ab09d2676d520fad284a42e9d294271597ee9dbbada59db4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa2f7cb419a01a50eeeb1d6ba2252f1682a14473dd3bedbceffc312c83a156d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2263d99212521d5fa95f4ff779d8cf87deea0f88730316171ab9816f9d6e3bb0(
    value: typing.Optional[AlbListenerRuleActionAuthenticateOidc],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a562e0c18fe58aab012d7bf62c2dfafb84832043cb63fe6ef0b711009327ea9e(
    *,
    content_type: builtins.str,
    message_body: typing.Optional[builtins.str] = None,
    status_code: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97df3502d248b7773f51f4a04a50ac754828885aa2941b370edbe37c7461943e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0772b9586535d714e96c85ce6fe3b765517b164c5980b84381c09db4f3ddd96b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f983e390282a73db3c8160b0cb4370cde73636764155840b3f72517ae202ebb5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d619f7e3544f8072cc03490939d94cc24d0c1e7c59bd5ba2b0498b53fbe2e556(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a937559973ae74cab20a12b2ac7886497b41079d71b5b654b5f8ffeed9bbd4de(
    value: typing.Optional[AlbListenerRuleActionFixedResponse],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7df073273f0fc53b93177c0212fccb05ef98fb7627d2e2ded53155e34458f91b(
    *,
    target_group: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AlbListenerRuleActionForwardTargetGroup, typing.Dict[builtins.str, typing.Any]]]],
    stickiness: typing.Optional[typing.Union[AlbListenerRuleActionForwardStickiness, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c23070da42572e7d9a501dc135362bd2803fdf9a9d5b432d6c36b3504f641a7d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcf7dc4f6ed3746a1b9912b28743df144f4ed5a423d14439dc988d25785f732e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AlbListenerRuleActionForwardTargetGroup, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__692e9467a722274c500dee9295ebe2739e5c8f87388486b27d76408e8d9e1000(
    value: typing.Optional[AlbListenerRuleActionForward],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a282e6b8432605bd6797d0bc51071388a5a6e050d268518e8c1231b5db32afe(
    *,
    duration: jsii.Number,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72795f053a482bfeeee2452796727b4677dfc6b790bbf33b8040e368d82fae1e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70e766c0c909e1a0f0ffa71163809c0713194dbc31678414b231a78ad12bde21(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b264cbf44e071da8d4deccebceebed5da23dc423c678f0b86b8c5a85b44f0ad(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__677c7a1ace33c6978ca327f7c73324ebf54598b9b352e853501f83bf5adb88eb(
    value: typing.Optional[AlbListenerRuleActionForwardStickiness],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8e04378daf8e413eccceb608c3952d5810cdaa31487a877280ed494b80f103f(
    *,
    arn: builtins.str,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f6e297546ded866fbdaedf61d92e7bde409703237329206539bdb4f5da3c611(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b970e29312f334e97f38248064764dca9a85f1476ef95bda73898a49b05d86c4(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c5521a480151250bfb764eb013370dfc7e06c03f16e34333e026a58c671f8df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__601180fea6ab763f27fb4f07126cd4fab7c515a526017b809d827b16caa3d75c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a54c1c3a30c1922b532e6d018ed71d0216065da8006c2280fb3c2bcb13e9a78(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__115e7a39afa3d09e77a33425152f1d57f60cd98d4aeac4315ab2c047321d0d03(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AlbListenerRuleActionForwardTargetGroup]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56503b3748bdb5978541380a76cb886f163af2e307b73b5a2a62acefaba2e0f5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c37fd9b5299df99065d3954676dfd9c35278e06bb62fca3a8f613aa9d2065fb3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b00794c9580376f2b3a22232acfd717c1bca3e642bdbd6cb55b9ea0706e2e79(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a41fc833c78c60734e4b738295e0b8320d1afe35a00a1e8b88196bfd1b268959(
    value: typing.Optional[typing.Union[AlbListenerRuleActionForwardTargetGroup, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47f2301fa8b5450e73c59de2618eeab99e367b0b1fccef4d0a3a0d9ad21c1e7c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b10e39a396dd34442b28592389abf141bb6bec3098559902ce7704373dc2f77(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__228669efdb954c450e2ebc3b479b409557b758b630013ec7ab703709dd6f0de0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__111c715487f79bc93460eabf57666581311ec93ebcc078e0f188da978a47fa5d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fca9b80979de55418ffd022b1e3bc813f2ecfc5a0c83b67d58e19e88f6b4c55(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dcee98a8b3b51c26913d14406573c624e5471585f26ad33daf691e85ebc1bc6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AlbListenerRuleAction]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__135dc82903f0f55bf0dfa374f05c0b7521b27942fa2a39254720f0bdafbdfff4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a324c4aed00d977ee0c04a7f3ec299232baf20f82931948404759e21300f29b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__457c98873846960b77ea2766e7d02da4f69dbc30582fb1a94dbc5f1ca322fbbe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f598f12a6e97d68488aac96e1629e589ad120e985fa07d2ae8db0f7f72e64a25(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1317d2cd90207c61691d8a62ad61b82e59ee9769228744388091c7a5fced26d7(
    value: typing.Optional[typing.Union[AlbListenerRuleAction, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f410f66037d15fc29f5d1e91c1f2d3c0cd5adca06a3b4bedef28226998d81436(
    *,
    status_code: builtins.str,
    host: typing.Optional[builtins.str] = None,
    path: typing.Optional[builtins.str] = None,
    port: typing.Optional[builtins.str] = None,
    protocol: typing.Optional[builtins.str] = None,
    query: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__429f4f44f52e0d022381137bc421899a6ac735d8900974cde356f31acbd1cfa1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bfeddb491455ddfc5ed925c9882107f1721312d58044b22874d8c3f61688e0f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3510fc4e85c2394bfa823f17a929ede359cb659b480c70f5eb6bcaef2d1f71ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24a4a39c6c46369d69551ce216f77d1b24d3ef793921ccf39bf1cb9c9e28c631(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e03f99e2f625ab0b38a0937c8265843d30e2f20218fe0dbd71dbae18893e95cf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68ac99a4ef9139c5b67d87d7e44f4818340529fc70fb3bbd98371f27ddeb5bf0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e9bbb476da98897ddf684b1bd3b6b713932a5407f9b7dcdcf16620175d8e79e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4acbd27aaf3d0772fe64dacb9ea5e92747fdf2b387d9c73887b372d42706466f(
    value: typing.Optional[AlbListenerRuleActionRedirect],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__784a23ef9a896e28f5285025a52bfa13ae817b000dc99db89ce348fe5a747619(
    *,
    host_header: typing.Optional[typing.Union[AlbListenerRuleConditionHostHeader, typing.Dict[builtins.str, typing.Any]]] = None,
    http_header: typing.Optional[typing.Union[AlbListenerRuleConditionHttpHeader, typing.Dict[builtins.str, typing.Any]]] = None,
    http_request_method: typing.Optional[typing.Union[AlbListenerRuleConditionHttpRequestMethod, typing.Dict[builtins.str, typing.Any]]] = None,
    path_pattern: typing.Optional[typing.Union[AlbListenerRuleConditionPathPattern, typing.Dict[builtins.str, typing.Any]]] = None,
    query_string: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AlbListenerRuleConditionQueryString, typing.Dict[builtins.str, typing.Any]]]]] = None,
    source_ip: typing.Optional[typing.Union[AlbListenerRuleConditionSourceIp, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16c882a02bad1c7859be6806a3885a9404508569034d0ed9300bfc5cac1d0e8e(
    *,
    values: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73883f3ab3bf03684a350ef512fd47f03af31a5e2762e2251e41a05d633ce0b7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfeff253c88e09afe10a68038b583d81fccec60acb3787e2608a8ff81148b699(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bec135250de57135a4c01659eb7f2a8ac194fa6e6f10d5eb242203fbf1fc12c9(
    value: typing.Optional[AlbListenerRuleConditionHostHeader],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6e2f77ba1747033627790b9d50bdbabff16b824a2316d17bd164fcfe01ae55e(
    *,
    http_header_name: builtins.str,
    values: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0992e8c44dc26b8ff34057ac5efbe07910fd7cbee0ccb2488562f88bb219464(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eafbaf24e9befb9407701ae15e588c537fd8a35cd53e459f254ffd982bfe001e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d478f9f4d96e83a2ade80a450719d930ee35b0e6c57f8ae6e5a6347a4e7e518(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f29320f85545ae5d14dc4fcfd6e35e003e90f6e00346b9c894069fe8c801ebbb(
    value: typing.Optional[AlbListenerRuleConditionHttpHeader],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acf32acc2664a87b58fdd675bb00d30d9059b74197c005eda99b0b2e2a35cb52(
    *,
    values: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cce66c43323f81c0f3f588efa9bfd6c1d11dc9f2de55c1ff3b34ce4372058c5a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4503bd21a00f8fa415c0615b8eb494280fba27153c32387a68eabeb0ffdc2f40(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07bf64d6b53795e2b4de04dadea89f50c3b0771098e86120178d3cf20d9393fe(
    value: typing.Optional[AlbListenerRuleConditionHttpRequestMethod],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__182158133f94dd09262b937cd9615ef288525b5988f7f9a2476afd825d4ace35(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4988846f12147cfeb681e669cb9356ddf8a86bf45487835b3614b41a8266a70(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a7ae30c1f9fc242099813cd3dcb4d7910d5beb1ca061cb605fdd3fecf0cda6b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57a0e18b5d31307f1f9eb6fe977c497aa29a671a916b943b055063f4f35323fa(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15d676ea1da295d3f45b785bdbfddbc120f34e2e38304b524c214e57ad7321df(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bac8e7f621d0c69820bb5511b3ee7199142c81e5b8d06f8f8dd33799f4eb9710(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AlbListenerRuleCondition]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72a76a4bb2474e59d91868a134b2c0d73c3b4726292a61a6314e82789a8518fd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e473c054124f04b670e6a5db3198e037baa4e1ea5f280f8f800c6b7ecb8033ea(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AlbListenerRuleConditionQueryString, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71b8d4a9a7cbe4e3b7b8508cc6434662086a77fe41c26e5aed7046a95d66c3ec(
    value: typing.Optional[typing.Union[AlbListenerRuleCondition, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__916fd9f36f0f990c10bdcedff10e6bffe4f61a44a981d26e9d7589ce8282cb66(
    *,
    values: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45eb845909599ecdc49c74e4b78677cda4c9a0962c4fdb17d08630cc6ab8968f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d9ca857f13ac8b3e07e4625b769b4e50c5f5ca172210ec35f4726ba97d22968(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a2188763957e715e278fcd2b6afe70109d70422d1148263727c2194d61c0863(
    value: typing.Optional[AlbListenerRuleConditionPathPattern],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f7b87973ce3c06f81333a9e4a121ed314d61da889356c8ce0857ac0f18dcf32(
    *,
    value: builtins.str,
    key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0763822872e2f0b3c28f142b0055996ffd30dff4fa0122c423ddfcce038dd944(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58b6bd9b0b958389ebd4e8f74614bf811ed861721cda945608cb58e2711109e8(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf26d6fdc213af58a9f8b7d67e0f16167dc9df09425e2035d8d680dc2e5a0093(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3179c524f873d14100caf11c4e74440a58537d2f45f7c1738ffa538e5bfc70c8(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__958eb59e9b3782b4703f45a69ca2a4746a971127df425d94136f5a1282f3cc21(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__191e61fff54c186fc5819bc11461e664f3069c644107f0286dc893ed90078a93(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[AlbListenerRuleConditionQueryString]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95baf01310e6f3376f55d80a46c3f3ad892521e7ca6d0a519d738b734c4da570(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97c7ce5b119571ad8b6951e7d4a2d057e7440d449ca67c63419455f7b093dfc2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__285737e54b0a2a9300bf2eed6d86a80f098874df7da4ec9a7a2d99ddcf3fb7ff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95928be1ebc4386e1db223d779ff66def3695bb8b5be3701053a8a09e8fa8590(
    value: typing.Optional[typing.Union[AlbListenerRuleConditionQueryString, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed14cc1755e72506f553d0a2dde9e360c75fcca85c590036f11c74f52b72bea0(
    *,
    values: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d58599f412178c1e32c0c61d2b767285812cec97f9f72a44dcae97a0c95f3d0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40a6bb4ddaaff75624bb7ccb2026d3955c6cd4130da14cbd2a4c49e2302a0aaa(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__957ebc08ed8f5318119e3846537cfe778c1e25ba1cc6dd8a19b987d31ed8c408(
    value: typing.Optional[AlbListenerRuleConditionSourceIp],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc9a09c2413e844ca50a729526d0ff5105bebdbb9c39f56696accbfa8fd02ef3(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    action: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AlbListenerRuleAction, typing.Dict[builtins.str, typing.Any]]]],
    condition: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[AlbListenerRuleCondition, typing.Dict[builtins.str, typing.Any]]]],
    listener_arn: builtins.str,
    id: typing.Optional[builtins.str] = None,
    priority: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
