'''
# `aws_cognito_risk_configuration`

Refer to the Terraform Registory for docs: [`aws_cognito_risk_configuration`](https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration).
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


class CognitoRiskConfiguration(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoRiskConfiguration.CognitoRiskConfiguration",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration aws_cognito_risk_configuration}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        user_pool_id: builtins.str,
        account_takeover_risk_configuration: typing.Optional[typing.Union["CognitoRiskConfigurationAccountTakeoverRiskConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        client_id: typing.Optional[builtins.str] = None,
        compromised_credentials_risk_configuration: typing.Optional[typing.Union["CognitoRiskConfigurationCompromisedCredentialsRiskConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        risk_exception_configuration: typing.Optional[typing.Union["CognitoRiskConfigurationRiskExceptionConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration aws_cognito_risk_configuration} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param user_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#user_pool_id CognitoRiskConfiguration#user_pool_id}.
        :param account_takeover_risk_configuration: account_takeover_risk_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#account_takeover_risk_configuration CognitoRiskConfiguration#account_takeover_risk_configuration}
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#client_id CognitoRiskConfiguration#client_id}.
        :param compromised_credentials_risk_configuration: compromised_credentials_risk_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#compromised_credentials_risk_configuration CognitoRiskConfiguration#compromised_credentials_risk_configuration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#id CognitoRiskConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param risk_exception_configuration: risk_exception_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#risk_exception_configuration CognitoRiskConfiguration#risk_exception_configuration}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4975405c0a9ecba6d7bf5787ea8f5b108d6ea363ad44eb714630a55be3c59607)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CognitoRiskConfigurationConfig(
            user_pool_id=user_pool_id,
            account_takeover_risk_configuration=account_takeover_risk_configuration,
            client_id=client_id,
            compromised_credentials_risk_configuration=compromised_credentials_risk_configuration,
            id=id,
            risk_exception_configuration=risk_exception_configuration,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAccountTakeoverRiskConfiguration")
    def put_account_takeover_risk_configuration(
        self,
        *,
        actions: typing.Union["CognitoRiskConfigurationAccountTakeoverRiskConfigurationActions", typing.Dict[builtins.str, typing.Any]],
        notify_configuration: typing.Union["CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param actions: actions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#actions CognitoRiskConfiguration#actions}
        :param notify_configuration: notify_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#notify_configuration CognitoRiskConfiguration#notify_configuration}
        '''
        value = CognitoRiskConfigurationAccountTakeoverRiskConfiguration(
            actions=actions, notify_configuration=notify_configuration
        )

        return typing.cast(None, jsii.invoke(self, "putAccountTakeoverRiskConfiguration", [value]))

    @jsii.member(jsii_name="putCompromisedCredentialsRiskConfiguration")
    def put_compromised_credentials_risk_configuration(
        self,
        *,
        actions: typing.Union["CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActions", typing.Dict[builtins.str, typing.Any]],
        event_filter: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param actions: actions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#actions CognitoRiskConfiguration#actions}
        :param event_filter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#event_filter CognitoRiskConfiguration#event_filter}.
        '''
        value = CognitoRiskConfigurationCompromisedCredentialsRiskConfiguration(
            actions=actions, event_filter=event_filter
        )

        return typing.cast(None, jsii.invoke(self, "putCompromisedCredentialsRiskConfiguration", [value]))

    @jsii.member(jsii_name="putRiskExceptionConfiguration")
    def put_risk_exception_configuration(
        self,
        *,
        blocked_ip_range_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        skipped_ip_range_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param blocked_ip_range_list: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#blocked_ip_range_list CognitoRiskConfiguration#blocked_ip_range_list}.
        :param skipped_ip_range_list: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#skipped_ip_range_list CognitoRiskConfiguration#skipped_ip_range_list}.
        '''
        value = CognitoRiskConfigurationRiskExceptionConfiguration(
            blocked_ip_range_list=blocked_ip_range_list,
            skipped_ip_range_list=skipped_ip_range_list,
        )

        return typing.cast(None, jsii.invoke(self, "putRiskExceptionConfiguration", [value]))

    @jsii.member(jsii_name="resetAccountTakeoverRiskConfiguration")
    def reset_account_takeover_risk_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountTakeoverRiskConfiguration", []))

    @jsii.member(jsii_name="resetClientId")
    def reset_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientId", []))

    @jsii.member(jsii_name="resetCompromisedCredentialsRiskConfiguration")
    def reset_compromised_credentials_risk_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompromisedCredentialsRiskConfiguration", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetRiskExceptionConfiguration")
    def reset_risk_exception_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRiskExceptionConfiguration", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="accountTakeoverRiskConfiguration")
    def account_takeover_risk_configuration(
        self,
    ) -> "CognitoRiskConfigurationAccountTakeoverRiskConfigurationOutputReference":
        return typing.cast("CognitoRiskConfigurationAccountTakeoverRiskConfigurationOutputReference", jsii.get(self, "accountTakeoverRiskConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="compromisedCredentialsRiskConfiguration")
    def compromised_credentials_risk_configuration(
        self,
    ) -> "CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationOutputReference":
        return typing.cast("CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationOutputReference", jsii.get(self, "compromisedCredentialsRiskConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="riskExceptionConfiguration")
    def risk_exception_configuration(
        self,
    ) -> "CognitoRiskConfigurationRiskExceptionConfigurationOutputReference":
        return typing.cast("CognitoRiskConfigurationRiskExceptionConfigurationOutputReference", jsii.get(self, "riskExceptionConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="accountTakeoverRiskConfigurationInput")
    def account_takeover_risk_configuration_input(
        self,
    ) -> typing.Optional["CognitoRiskConfigurationAccountTakeoverRiskConfiguration"]:
        return typing.cast(typing.Optional["CognitoRiskConfigurationAccountTakeoverRiskConfiguration"], jsii.get(self, "accountTakeoverRiskConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="compromisedCredentialsRiskConfigurationInput")
    def compromised_credentials_risk_configuration_input(
        self,
    ) -> typing.Optional["CognitoRiskConfigurationCompromisedCredentialsRiskConfiguration"]:
        return typing.cast(typing.Optional["CognitoRiskConfigurationCompromisedCredentialsRiskConfiguration"], jsii.get(self, "compromisedCredentialsRiskConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="riskExceptionConfigurationInput")
    def risk_exception_configuration_input(
        self,
    ) -> typing.Optional["CognitoRiskConfigurationRiskExceptionConfiguration"]:
        return typing.cast(typing.Optional["CognitoRiskConfigurationRiskExceptionConfiguration"], jsii.get(self, "riskExceptionConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="userPoolIdInput")
    def user_pool_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userPoolIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a39dd4a43dfcbf4ed8ea8d7d0dd40abfd09afe04f76d4f7cda93c296ffd5f27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ce0cf2eba8e99928de0b8d044273ff452951856313d6eed37fa42f326c5d8f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="userPoolId")
    def user_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userPoolId"))

    @user_pool_id.setter
    def user_pool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1aa8439a4e87683d2fdcdf1cfa4953c518c280d5e1e7c345f6e4ee0a488fce3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userPoolId", value)


@jsii.data_type(
    jsii_type="aws.cognitoRiskConfiguration.CognitoRiskConfigurationAccountTakeoverRiskConfiguration",
    jsii_struct_bases=[],
    name_mapping={"actions": "actions", "notify_configuration": "notifyConfiguration"},
)
class CognitoRiskConfigurationAccountTakeoverRiskConfiguration:
    def __init__(
        self,
        *,
        actions: typing.Union["CognitoRiskConfigurationAccountTakeoverRiskConfigurationActions", typing.Dict[builtins.str, typing.Any]],
        notify_configuration: typing.Union["CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param actions: actions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#actions CognitoRiskConfiguration#actions}
        :param notify_configuration: notify_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#notify_configuration CognitoRiskConfiguration#notify_configuration}
        '''
        if isinstance(actions, dict):
            actions = CognitoRiskConfigurationAccountTakeoverRiskConfigurationActions(**actions)
        if isinstance(notify_configuration, dict):
            notify_configuration = CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration(**notify_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5062fe94b85761492b37069357124c74c718022d1c9a3ebd480f81093a16736a)
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument notify_configuration", value=notify_configuration, expected_type=type_hints["notify_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "actions": actions,
            "notify_configuration": notify_configuration,
        }

    @builtins.property
    def actions(
        self,
    ) -> "CognitoRiskConfigurationAccountTakeoverRiskConfigurationActions":
        '''actions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#actions CognitoRiskConfiguration#actions}
        '''
        result = self._values.get("actions")
        assert result is not None, "Required property 'actions' is missing"
        return typing.cast("CognitoRiskConfigurationAccountTakeoverRiskConfigurationActions", result)

    @builtins.property
    def notify_configuration(
        self,
    ) -> "CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration":
        '''notify_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#notify_configuration CognitoRiskConfiguration#notify_configuration}
        '''
        result = self._values.get("notify_configuration")
        assert result is not None, "Required property 'notify_configuration' is missing"
        return typing.cast("CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoRiskConfigurationAccountTakeoverRiskConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.cognitoRiskConfiguration.CognitoRiskConfigurationAccountTakeoverRiskConfigurationActions",
    jsii_struct_bases=[],
    name_mapping={
        "high_action": "highAction",
        "low_action": "lowAction",
        "medium_action": "mediumAction",
    },
)
class CognitoRiskConfigurationAccountTakeoverRiskConfigurationActions:
    def __init__(
        self,
        *,
        high_action: typing.Optional[typing.Union["CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighAction", typing.Dict[builtins.str, typing.Any]]] = None,
        low_action: typing.Optional[typing.Union["CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowAction", typing.Dict[builtins.str, typing.Any]]] = None,
        medium_action: typing.Optional[typing.Union["CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumAction", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param high_action: high_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#high_action CognitoRiskConfiguration#high_action}
        :param low_action: low_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#low_action CognitoRiskConfiguration#low_action}
        :param medium_action: medium_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#medium_action CognitoRiskConfiguration#medium_action}
        '''
        if isinstance(high_action, dict):
            high_action = CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighAction(**high_action)
        if isinstance(low_action, dict):
            low_action = CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowAction(**low_action)
        if isinstance(medium_action, dict):
            medium_action = CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumAction(**medium_action)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a41e5b56247b5fa4c5560e62c55b3ca7a531f171d4b68d42f55a0ec5ac62e6d5)
            check_type(argname="argument high_action", value=high_action, expected_type=type_hints["high_action"])
            check_type(argname="argument low_action", value=low_action, expected_type=type_hints["low_action"])
            check_type(argname="argument medium_action", value=medium_action, expected_type=type_hints["medium_action"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if high_action is not None:
            self._values["high_action"] = high_action
        if low_action is not None:
            self._values["low_action"] = low_action
        if medium_action is not None:
            self._values["medium_action"] = medium_action

    @builtins.property
    def high_action(
        self,
    ) -> typing.Optional["CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighAction"]:
        '''high_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#high_action CognitoRiskConfiguration#high_action}
        '''
        result = self._values.get("high_action")
        return typing.cast(typing.Optional["CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighAction"], result)

    @builtins.property
    def low_action(
        self,
    ) -> typing.Optional["CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowAction"]:
        '''low_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#low_action CognitoRiskConfiguration#low_action}
        '''
        result = self._values.get("low_action")
        return typing.cast(typing.Optional["CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowAction"], result)

    @builtins.property
    def medium_action(
        self,
    ) -> typing.Optional["CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumAction"]:
        '''medium_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#medium_action CognitoRiskConfiguration#medium_action}
        '''
        result = self._values.get("medium_action")
        return typing.cast(typing.Optional["CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumAction"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoRiskConfigurationAccountTakeoverRiskConfigurationActions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.cognitoRiskConfiguration.CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighAction",
    jsii_struct_bases=[],
    name_mapping={"event_action": "eventAction", "notify": "notify"},
)
class CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighAction:
    def __init__(
        self,
        *,
        event_action: builtins.str,
        notify: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param event_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#event_action CognitoRiskConfiguration#event_action}.
        :param notify: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#notify CognitoRiskConfiguration#notify}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a85195aa42b3657ec5ead243c522bc929bf85bad285a91e7040d76278e1fd2d0)
            check_type(argname="argument event_action", value=event_action, expected_type=type_hints["event_action"])
            check_type(argname="argument notify", value=notify, expected_type=type_hints["notify"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "event_action": event_action,
            "notify": notify,
        }

    @builtins.property
    def event_action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#event_action CognitoRiskConfiguration#event_action}.'''
        result = self._values.get("event_action")
        assert result is not None, "Required property 'event_action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def notify(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#notify CognitoRiskConfiguration#notify}.'''
        result = self._values.get("notify")
        assert result is not None, "Required property 'notify' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoRiskConfiguration.CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4a20b149ded1d4c03832dab5db0e55fea38cf65e2c9ee0df467cbd8dbd3243b2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="eventActionInput")
    def event_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventActionInput"))

    @builtins.property
    @jsii.member(jsii_name="notifyInput")
    def notify_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "notifyInput"))

    @builtins.property
    @jsii.member(jsii_name="eventAction")
    def event_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventAction"))

    @event_action.setter
    def event_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ccbbf4f4ba681c02a4c99d441c67d14b0fa2ac66047ac99e4f0761b72a34201)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventAction", value)

    @builtins.property
    @jsii.member(jsii_name="notify")
    def notify(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "notify"))

    @notify.setter
    def notify(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5285be13bec1165d3fccb2d09b7260b3867b4c51ab64f93b089a75c622f47bd5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notify", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighAction]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e4a7fa6d893f207e82fbe18aaa2cf28e859609aa6e2d6dbc2183c39462be400)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cognitoRiskConfiguration.CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowAction",
    jsii_struct_bases=[],
    name_mapping={"event_action": "eventAction", "notify": "notify"},
)
class CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowAction:
    def __init__(
        self,
        *,
        event_action: builtins.str,
        notify: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param event_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#event_action CognitoRiskConfiguration#event_action}.
        :param notify: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#notify CognitoRiskConfiguration#notify}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d08ac501776803be321696c7b2cd0b2990f96cff8b094eb9a8bda4cce483e39a)
            check_type(argname="argument event_action", value=event_action, expected_type=type_hints["event_action"])
            check_type(argname="argument notify", value=notify, expected_type=type_hints["notify"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "event_action": event_action,
            "notify": notify,
        }

    @builtins.property
    def event_action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#event_action CognitoRiskConfiguration#event_action}.'''
        result = self._values.get("event_action")
        assert result is not None, "Required property 'event_action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def notify(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#notify CognitoRiskConfiguration#notify}.'''
        result = self._values.get("notify")
        assert result is not None, "Required property 'notify' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoRiskConfiguration.CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__48aa5693849c154f78af9481cb8849eb56898085201f1e0a4afd9c5a6c39c1d3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="eventActionInput")
    def event_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventActionInput"))

    @builtins.property
    @jsii.member(jsii_name="notifyInput")
    def notify_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "notifyInput"))

    @builtins.property
    @jsii.member(jsii_name="eventAction")
    def event_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventAction"))

    @event_action.setter
    def event_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5eb0e38fa735ca18b1142fe1cf4e40ee032ee1160ae876ccd97b679db953c24e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventAction", value)

    @builtins.property
    @jsii.member(jsii_name="notify")
    def notify(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "notify"))

    @notify.setter
    def notify(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c76749de380f4f2db11eeaa131ddd7cffbca4de4ee9d7e6d36b0842c93730993)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notify", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowAction]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9620c7559e866451fc552eb66c0f5155d864afa9223f6d6dede85eab153cb2ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cognitoRiskConfiguration.CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumAction",
    jsii_struct_bases=[],
    name_mapping={"event_action": "eventAction", "notify": "notify"},
)
class CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumAction:
    def __init__(
        self,
        *,
        event_action: builtins.str,
        notify: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param event_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#event_action CognitoRiskConfiguration#event_action}.
        :param notify: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#notify CognitoRiskConfiguration#notify}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a6dff1dbddd68503734520d2e1b10ee095fa2b6f63da1be1c68850e39fc4f87)
            check_type(argname="argument event_action", value=event_action, expected_type=type_hints["event_action"])
            check_type(argname="argument notify", value=notify, expected_type=type_hints["notify"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "event_action": event_action,
            "notify": notify,
        }

    @builtins.property
    def event_action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#event_action CognitoRiskConfiguration#event_action}.'''
        result = self._values.get("event_action")
        assert result is not None, "Required property 'event_action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def notify(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#notify CognitoRiskConfiguration#notify}.'''
        result = self._values.get("notify")
        assert result is not None, "Required property 'notify' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoRiskConfiguration.CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__96ed3bf65f2ac4bbb0472a52ccbe36bec312b259ecd6cd1aa65b925df993204a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="eventActionInput")
    def event_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventActionInput"))

    @builtins.property
    @jsii.member(jsii_name="notifyInput")
    def notify_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "notifyInput"))

    @builtins.property
    @jsii.member(jsii_name="eventAction")
    def event_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventAction"))

    @event_action.setter
    def event_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbb492f781bc1b5c5ba2a141ec602715f95499c27f4a5fedeccdbc65488d4019)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventAction", value)

    @builtins.property
    @jsii.member(jsii_name="notify")
    def notify(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "notify"))

    @notify.setter
    def notify(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55de81d13c13fb82380664aca46099c8af3384c6a1c26451d33b5f3d760f39a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notify", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumAction]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32b1d8396dc8fe0aac85f51169a4105d4d768f16ea61569484594af1c3ae683a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoRiskConfiguration.CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__607f0cfabe7ed8894d933b12643e34f7cc96861bbdcdc86d70039dd49309e0e3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putHighAction")
    def put_high_action(
        self,
        *,
        event_action: builtins.str,
        notify: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param event_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#event_action CognitoRiskConfiguration#event_action}.
        :param notify: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#notify CognitoRiskConfiguration#notify}.
        '''
        value = CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighAction(
            event_action=event_action, notify=notify
        )

        return typing.cast(None, jsii.invoke(self, "putHighAction", [value]))

    @jsii.member(jsii_name="putLowAction")
    def put_low_action(
        self,
        *,
        event_action: builtins.str,
        notify: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param event_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#event_action CognitoRiskConfiguration#event_action}.
        :param notify: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#notify CognitoRiskConfiguration#notify}.
        '''
        value = CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowAction(
            event_action=event_action, notify=notify
        )

        return typing.cast(None, jsii.invoke(self, "putLowAction", [value]))

    @jsii.member(jsii_name="putMediumAction")
    def put_medium_action(
        self,
        *,
        event_action: builtins.str,
        notify: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param event_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#event_action CognitoRiskConfiguration#event_action}.
        :param notify: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#notify CognitoRiskConfiguration#notify}.
        '''
        value = CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumAction(
            event_action=event_action, notify=notify
        )

        return typing.cast(None, jsii.invoke(self, "putMediumAction", [value]))

    @jsii.member(jsii_name="resetHighAction")
    def reset_high_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHighAction", []))

    @jsii.member(jsii_name="resetLowAction")
    def reset_low_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLowAction", []))

    @jsii.member(jsii_name="resetMediumAction")
    def reset_medium_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMediumAction", []))

    @builtins.property
    @jsii.member(jsii_name="highAction")
    def high_action(
        self,
    ) -> CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionOutputReference:
        return typing.cast(CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionOutputReference, jsii.get(self, "highAction"))

    @builtins.property
    @jsii.member(jsii_name="lowAction")
    def low_action(
        self,
    ) -> CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionOutputReference:
        return typing.cast(CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionOutputReference, jsii.get(self, "lowAction"))

    @builtins.property
    @jsii.member(jsii_name="mediumAction")
    def medium_action(
        self,
    ) -> CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionOutputReference:
        return typing.cast(CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionOutputReference, jsii.get(self, "mediumAction"))

    @builtins.property
    @jsii.member(jsii_name="highActionInput")
    def high_action_input(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighAction]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighAction], jsii.get(self, "highActionInput"))

    @builtins.property
    @jsii.member(jsii_name="lowActionInput")
    def low_action_input(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowAction]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowAction], jsii.get(self, "lowActionInput"))

    @builtins.property
    @jsii.member(jsii_name="mediumActionInput")
    def medium_action_input(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumAction]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumAction], jsii.get(self, "mediumActionInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActions]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cab567735a565d3458e78d4f2af45de82fb456bf3f9ffe01bdb3245fda695b2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cognitoRiskConfiguration.CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "source_arn": "sourceArn",
        "block_email": "blockEmail",
        "from_": "from",
        "mfa_email": "mfaEmail",
        "no_action_email": "noActionEmail",
        "reply_to": "replyTo",
    },
)
class CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration:
    def __init__(
        self,
        *,
        source_arn: builtins.str,
        block_email: typing.Optional[typing.Union["CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmail", typing.Dict[builtins.str, typing.Any]]] = None,
        from_: typing.Optional[builtins.str] = None,
        mfa_email: typing.Optional[typing.Union["CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmail", typing.Dict[builtins.str, typing.Any]]] = None,
        no_action_email: typing.Optional[typing.Union["CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmail", typing.Dict[builtins.str, typing.Any]]] = None,
        reply_to: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param source_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#source_arn CognitoRiskConfiguration#source_arn}.
        :param block_email: block_email block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#block_email CognitoRiskConfiguration#block_email}
        :param from_: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#from CognitoRiskConfiguration#from}.
        :param mfa_email: mfa_email block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#mfa_email CognitoRiskConfiguration#mfa_email}
        :param no_action_email: no_action_email block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#no_action_email CognitoRiskConfiguration#no_action_email}
        :param reply_to: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#reply_to CognitoRiskConfiguration#reply_to}.
        '''
        if isinstance(block_email, dict):
            block_email = CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmail(**block_email)
        if isinstance(mfa_email, dict):
            mfa_email = CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmail(**mfa_email)
        if isinstance(no_action_email, dict):
            no_action_email = CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmail(**no_action_email)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1acc44cef8cea03771e23a0bb54b15679655f8a80c47054809fd376a67fcb6a0)
            check_type(argname="argument source_arn", value=source_arn, expected_type=type_hints["source_arn"])
            check_type(argname="argument block_email", value=block_email, expected_type=type_hints["block_email"])
            check_type(argname="argument from_", value=from_, expected_type=type_hints["from_"])
            check_type(argname="argument mfa_email", value=mfa_email, expected_type=type_hints["mfa_email"])
            check_type(argname="argument no_action_email", value=no_action_email, expected_type=type_hints["no_action_email"])
            check_type(argname="argument reply_to", value=reply_to, expected_type=type_hints["reply_to"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "source_arn": source_arn,
        }
        if block_email is not None:
            self._values["block_email"] = block_email
        if from_ is not None:
            self._values["from_"] = from_
        if mfa_email is not None:
            self._values["mfa_email"] = mfa_email
        if no_action_email is not None:
            self._values["no_action_email"] = no_action_email
        if reply_to is not None:
            self._values["reply_to"] = reply_to

    @builtins.property
    def source_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#source_arn CognitoRiskConfiguration#source_arn}.'''
        result = self._values.get("source_arn")
        assert result is not None, "Required property 'source_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def block_email(
        self,
    ) -> typing.Optional["CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmail"]:
        '''block_email block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#block_email CognitoRiskConfiguration#block_email}
        '''
        result = self._values.get("block_email")
        return typing.cast(typing.Optional["CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmail"], result)

    @builtins.property
    def from_(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#from CognitoRiskConfiguration#from}.'''
        result = self._values.get("from_")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mfa_email(
        self,
    ) -> typing.Optional["CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmail"]:
        '''mfa_email block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#mfa_email CognitoRiskConfiguration#mfa_email}
        '''
        result = self._values.get("mfa_email")
        return typing.cast(typing.Optional["CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmail"], result)

    @builtins.property
    def no_action_email(
        self,
    ) -> typing.Optional["CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmail"]:
        '''no_action_email block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#no_action_email CognitoRiskConfiguration#no_action_email}
        '''
        result = self._values.get("no_action_email")
        return typing.cast(typing.Optional["CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmail"], result)

    @builtins.property
    def reply_to(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#reply_to CognitoRiskConfiguration#reply_to}.'''
        result = self._values.get("reply_to")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.cognitoRiskConfiguration.CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmail",
    jsii_struct_bases=[],
    name_mapping={
        "html_body": "htmlBody",
        "subject": "subject",
        "text_body": "textBody",
    },
)
class CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmail:
    def __init__(
        self,
        *,
        html_body: builtins.str,
        subject: builtins.str,
        text_body: builtins.str,
    ) -> None:
        '''
        :param html_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#html_body CognitoRiskConfiguration#html_body}.
        :param subject: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#subject CognitoRiskConfiguration#subject}.
        :param text_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#text_body CognitoRiskConfiguration#text_body}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__505a339a314438d934ed528f037ca2a0dc82b2029fa3301a7df958fc2e107cf4)
            check_type(argname="argument html_body", value=html_body, expected_type=type_hints["html_body"])
            check_type(argname="argument subject", value=subject, expected_type=type_hints["subject"])
            check_type(argname="argument text_body", value=text_body, expected_type=type_hints["text_body"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "html_body": html_body,
            "subject": subject,
            "text_body": text_body,
        }

    @builtins.property
    def html_body(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#html_body CognitoRiskConfiguration#html_body}.'''
        result = self._values.get("html_body")
        assert result is not None, "Required property 'html_body' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subject(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#subject CognitoRiskConfiguration#subject}.'''
        result = self._values.get("subject")
        assert result is not None, "Required property 'subject' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def text_body(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#text_body CognitoRiskConfiguration#text_body}.'''
        result = self._values.get("text_body")
        assert result is not None, "Required property 'text_body' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmail(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoRiskConfiguration.CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1425b73427c9a7dba13eb3cb90a8a1cc463a764c9a94dfad1d0c4953d8a00a14)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="htmlBodyInput")
    def html_body_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "htmlBodyInput"))

    @builtins.property
    @jsii.member(jsii_name="subjectInput")
    def subject_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subjectInput"))

    @builtins.property
    @jsii.member(jsii_name="textBodyInput")
    def text_body_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "textBodyInput"))

    @builtins.property
    @jsii.member(jsii_name="htmlBody")
    def html_body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "htmlBody"))

    @html_body.setter
    def html_body(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a77fcfbbb15e0f13527da0f4514c3be2bb31b2727b44e4d8d1ca40815d6b80f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "htmlBody", value)

    @builtins.property
    @jsii.member(jsii_name="subject")
    def subject(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subject"))

    @subject.setter
    def subject(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f6cadded9e9998a6e0de8ba805c182672bacde2238a77ebcc1b7ee4d3188087)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subject", value)

    @builtins.property
    @jsii.member(jsii_name="textBody")
    def text_body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "textBody"))

    @text_body.setter
    def text_body(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92c8d002a89436341473983ee5b449d8ddf8d105041c8a8a241608e64a0612d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "textBody", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmail]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmail], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmail],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c1f0f1530b86eb887a8d312d4c1faf9a123b5006f9d1d11cdb40c300e09465d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cognitoRiskConfiguration.CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmail",
    jsii_struct_bases=[],
    name_mapping={
        "html_body": "htmlBody",
        "subject": "subject",
        "text_body": "textBody",
    },
)
class CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmail:
    def __init__(
        self,
        *,
        html_body: builtins.str,
        subject: builtins.str,
        text_body: builtins.str,
    ) -> None:
        '''
        :param html_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#html_body CognitoRiskConfiguration#html_body}.
        :param subject: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#subject CognitoRiskConfiguration#subject}.
        :param text_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#text_body CognitoRiskConfiguration#text_body}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04bf5562e491b0803b360f5f498c598e994ef8a3df6a00b029f94cea1858054a)
            check_type(argname="argument html_body", value=html_body, expected_type=type_hints["html_body"])
            check_type(argname="argument subject", value=subject, expected_type=type_hints["subject"])
            check_type(argname="argument text_body", value=text_body, expected_type=type_hints["text_body"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "html_body": html_body,
            "subject": subject,
            "text_body": text_body,
        }

    @builtins.property
    def html_body(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#html_body CognitoRiskConfiguration#html_body}.'''
        result = self._values.get("html_body")
        assert result is not None, "Required property 'html_body' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subject(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#subject CognitoRiskConfiguration#subject}.'''
        result = self._values.get("subject")
        assert result is not None, "Required property 'subject' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def text_body(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#text_body CognitoRiskConfiguration#text_body}.'''
        result = self._values.get("text_body")
        assert result is not None, "Required property 'text_body' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmail(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoRiskConfiguration.CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__04f3a7d6e9f76a1ad9a9013daaedfc0c3a4ce85f0be478b880863c898cc0ad50)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="htmlBodyInput")
    def html_body_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "htmlBodyInput"))

    @builtins.property
    @jsii.member(jsii_name="subjectInput")
    def subject_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subjectInput"))

    @builtins.property
    @jsii.member(jsii_name="textBodyInput")
    def text_body_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "textBodyInput"))

    @builtins.property
    @jsii.member(jsii_name="htmlBody")
    def html_body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "htmlBody"))

    @html_body.setter
    def html_body(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0e2e3be4a8dcf5530bad1ef381f340e766c9b034887abaa0a0b9d4bc4184726)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "htmlBody", value)

    @builtins.property
    @jsii.member(jsii_name="subject")
    def subject(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subject"))

    @subject.setter
    def subject(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5744337d929c2448f343a4b5e193c2503829a09b10204e4999b7a8e81635491)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subject", value)

    @builtins.property
    @jsii.member(jsii_name="textBody")
    def text_body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "textBody"))

    @text_body.setter
    def text_body(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a65ca680a9abeb9162fb77ea47469092e1c33f01ec5d09661559d1c55c475619)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "textBody", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmail]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmail], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmail],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__835fd406f065de9a1fdcad4af4d477eac1c5f2abc3047a2d74b95554ebc05bfc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cognitoRiskConfiguration.CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmail",
    jsii_struct_bases=[],
    name_mapping={
        "html_body": "htmlBody",
        "subject": "subject",
        "text_body": "textBody",
    },
)
class CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmail:
    def __init__(
        self,
        *,
        html_body: builtins.str,
        subject: builtins.str,
        text_body: builtins.str,
    ) -> None:
        '''
        :param html_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#html_body CognitoRiskConfiguration#html_body}.
        :param subject: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#subject CognitoRiskConfiguration#subject}.
        :param text_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#text_body CognitoRiskConfiguration#text_body}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89e81f65bef0d07ab185db2cb06f249645044f77c457394aa3aa2b46d82fff85)
            check_type(argname="argument html_body", value=html_body, expected_type=type_hints["html_body"])
            check_type(argname="argument subject", value=subject, expected_type=type_hints["subject"])
            check_type(argname="argument text_body", value=text_body, expected_type=type_hints["text_body"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "html_body": html_body,
            "subject": subject,
            "text_body": text_body,
        }

    @builtins.property
    def html_body(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#html_body CognitoRiskConfiguration#html_body}.'''
        result = self._values.get("html_body")
        assert result is not None, "Required property 'html_body' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subject(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#subject CognitoRiskConfiguration#subject}.'''
        result = self._values.get("subject")
        assert result is not None, "Required property 'subject' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def text_body(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#text_body CognitoRiskConfiguration#text_body}.'''
        result = self._values.get("text_body")
        assert result is not None, "Required property 'text_body' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmail(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoRiskConfiguration.CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__aa018a7e0f5d8c2fa13809615a1ee9930831ae7be0e2c6c042c99120927f507a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="htmlBodyInput")
    def html_body_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "htmlBodyInput"))

    @builtins.property
    @jsii.member(jsii_name="subjectInput")
    def subject_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subjectInput"))

    @builtins.property
    @jsii.member(jsii_name="textBodyInput")
    def text_body_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "textBodyInput"))

    @builtins.property
    @jsii.member(jsii_name="htmlBody")
    def html_body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "htmlBody"))

    @html_body.setter
    def html_body(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b10327998b794b41de558853a1656d6b9e98f3e7881d7eb3664c461e0f1f7643)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "htmlBody", value)

    @builtins.property
    @jsii.member(jsii_name="subject")
    def subject(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subject"))

    @subject.setter
    def subject(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2cb998415412896ffb42d2911ab0c14eefdfa7a4132cfe3a7709633e6471d9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subject", value)

    @builtins.property
    @jsii.member(jsii_name="textBody")
    def text_body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "textBody"))

    @text_body.setter
    def text_body(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99f15138c2772b67bcf171e1de70aba8a4867a6b4fc46e7f1f8340eb6beb0a83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "textBody", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmail]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmail], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmail],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2420d71fe7f8f98b48bd16f80e4b66486e3837a8102f7d41a222eae9c9e944ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoRiskConfiguration.CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a35060ecd1dab0826faf15874329992f5b1d5a5c9d6569fb0ff4f61338aa9e75)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBlockEmail")
    def put_block_email(
        self,
        *,
        html_body: builtins.str,
        subject: builtins.str,
        text_body: builtins.str,
    ) -> None:
        '''
        :param html_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#html_body CognitoRiskConfiguration#html_body}.
        :param subject: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#subject CognitoRiskConfiguration#subject}.
        :param text_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#text_body CognitoRiskConfiguration#text_body}.
        '''
        value = CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmail(
            html_body=html_body, subject=subject, text_body=text_body
        )

        return typing.cast(None, jsii.invoke(self, "putBlockEmail", [value]))

    @jsii.member(jsii_name="putMfaEmail")
    def put_mfa_email(
        self,
        *,
        html_body: builtins.str,
        subject: builtins.str,
        text_body: builtins.str,
    ) -> None:
        '''
        :param html_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#html_body CognitoRiskConfiguration#html_body}.
        :param subject: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#subject CognitoRiskConfiguration#subject}.
        :param text_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#text_body CognitoRiskConfiguration#text_body}.
        '''
        value = CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmail(
            html_body=html_body, subject=subject, text_body=text_body
        )

        return typing.cast(None, jsii.invoke(self, "putMfaEmail", [value]))

    @jsii.member(jsii_name="putNoActionEmail")
    def put_no_action_email(
        self,
        *,
        html_body: builtins.str,
        subject: builtins.str,
        text_body: builtins.str,
    ) -> None:
        '''
        :param html_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#html_body CognitoRiskConfiguration#html_body}.
        :param subject: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#subject CognitoRiskConfiguration#subject}.
        :param text_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#text_body CognitoRiskConfiguration#text_body}.
        '''
        value = CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmail(
            html_body=html_body, subject=subject, text_body=text_body
        )

        return typing.cast(None, jsii.invoke(self, "putNoActionEmail", [value]))

    @jsii.member(jsii_name="resetBlockEmail")
    def reset_block_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlockEmail", []))

    @jsii.member(jsii_name="resetFrom")
    def reset_from(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFrom", []))

    @jsii.member(jsii_name="resetMfaEmail")
    def reset_mfa_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMfaEmail", []))

    @jsii.member(jsii_name="resetNoActionEmail")
    def reset_no_action_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoActionEmail", []))

    @jsii.member(jsii_name="resetReplyTo")
    def reset_reply_to(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplyTo", []))

    @builtins.property
    @jsii.member(jsii_name="blockEmail")
    def block_email(
        self,
    ) -> CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailOutputReference:
        return typing.cast(CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailOutputReference, jsii.get(self, "blockEmail"))

    @builtins.property
    @jsii.member(jsii_name="mfaEmail")
    def mfa_email(
        self,
    ) -> CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailOutputReference:
        return typing.cast(CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailOutputReference, jsii.get(self, "mfaEmail"))

    @builtins.property
    @jsii.member(jsii_name="noActionEmail")
    def no_action_email(
        self,
    ) -> CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailOutputReference:
        return typing.cast(CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailOutputReference, jsii.get(self, "noActionEmail"))

    @builtins.property
    @jsii.member(jsii_name="blockEmailInput")
    def block_email_input(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmail]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmail], jsii.get(self, "blockEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="fromInput")
    def from_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fromInput"))

    @builtins.property
    @jsii.member(jsii_name="mfaEmailInput")
    def mfa_email_input(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmail]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmail], jsii.get(self, "mfaEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="noActionEmailInput")
    def no_action_email_input(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmail]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmail], jsii.get(self, "noActionEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="replyToInput")
    def reply_to_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replyToInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceArnInput")
    def source_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceArnInput"))

    @builtins.property
    @jsii.member(jsii_name="from")
    def from_(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "from"))

    @from_.setter
    def from_(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd538912d81b4581f05f070e2aceb2590888be1cccc98f00ae483179085f2b07)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "from", value)

    @builtins.property
    @jsii.member(jsii_name="replyTo")
    def reply_to(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replyTo"))

    @reply_to.setter
    def reply_to(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f52013bd6613a75e837fff308c569e9ffd52f2ae0e3a064a91968d876797feb2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replyTo", value)

    @builtins.property
    @jsii.member(jsii_name="sourceArn")
    def source_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceArn"))

    @source_arn.setter
    def source_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55e75846657ec8f4ee2d3518c803fe4bff5fb4b2a3c050c8edd8c3ee96f74f27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98fae82adb33989d5e2f959f522589775e3ae64cdf60ab123b584c6d06b7c0f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CognitoRiskConfigurationAccountTakeoverRiskConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoRiskConfiguration.CognitoRiskConfigurationAccountTakeoverRiskConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1d3cd83682d7d087c32e686911dfc5a9ea36bd187aaaa61d3035be36d99f8315)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putActions")
    def put_actions(
        self,
        *,
        high_action: typing.Optional[typing.Union[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighAction, typing.Dict[builtins.str, typing.Any]]] = None,
        low_action: typing.Optional[typing.Union[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowAction, typing.Dict[builtins.str, typing.Any]]] = None,
        medium_action: typing.Optional[typing.Union[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumAction, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param high_action: high_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#high_action CognitoRiskConfiguration#high_action}
        :param low_action: low_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#low_action CognitoRiskConfiguration#low_action}
        :param medium_action: medium_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#medium_action CognitoRiskConfiguration#medium_action}
        '''
        value = CognitoRiskConfigurationAccountTakeoverRiskConfigurationActions(
            high_action=high_action, low_action=low_action, medium_action=medium_action
        )

        return typing.cast(None, jsii.invoke(self, "putActions", [value]))

    @jsii.member(jsii_name="putNotifyConfiguration")
    def put_notify_configuration(
        self,
        *,
        source_arn: builtins.str,
        block_email: typing.Optional[typing.Union[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmail, typing.Dict[builtins.str, typing.Any]]] = None,
        from_: typing.Optional[builtins.str] = None,
        mfa_email: typing.Optional[typing.Union[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmail, typing.Dict[builtins.str, typing.Any]]] = None,
        no_action_email: typing.Optional[typing.Union[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmail, typing.Dict[builtins.str, typing.Any]]] = None,
        reply_to: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param source_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#source_arn CognitoRiskConfiguration#source_arn}.
        :param block_email: block_email block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#block_email CognitoRiskConfiguration#block_email}
        :param from_: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#from CognitoRiskConfiguration#from}.
        :param mfa_email: mfa_email block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#mfa_email CognitoRiskConfiguration#mfa_email}
        :param no_action_email: no_action_email block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#no_action_email CognitoRiskConfiguration#no_action_email}
        :param reply_to: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#reply_to CognitoRiskConfiguration#reply_to}.
        '''
        value = CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration(
            source_arn=source_arn,
            block_email=block_email,
            from_=from_,
            mfa_email=mfa_email,
            no_action_email=no_action_email,
            reply_to=reply_to,
        )

        return typing.cast(None, jsii.invoke(self, "putNotifyConfiguration", [value]))

    @builtins.property
    @jsii.member(jsii_name="actions")
    def actions(
        self,
    ) -> CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsOutputReference:
        return typing.cast(CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsOutputReference, jsii.get(self, "actions"))

    @builtins.property
    @jsii.member(jsii_name="notifyConfiguration")
    def notify_configuration(
        self,
    ) -> CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationOutputReference:
        return typing.cast(CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationOutputReference, jsii.get(self, "notifyConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="actionsInput")
    def actions_input(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActions]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActions], jsii.get(self, "actionsInput"))

    @builtins.property
    @jsii.member(jsii_name="notifyConfigurationInput")
    def notify_configuration_input(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration], jsii.get(self, "notifyConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfiguration]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__189e1c9696289b5ce288a83662c896cbea5443417912f0f19183fc0746a35ad1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cognitoRiskConfiguration.CognitoRiskConfigurationCompromisedCredentialsRiskConfiguration",
    jsii_struct_bases=[],
    name_mapping={"actions": "actions", "event_filter": "eventFilter"},
)
class CognitoRiskConfigurationCompromisedCredentialsRiskConfiguration:
    def __init__(
        self,
        *,
        actions: typing.Union["CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActions", typing.Dict[builtins.str, typing.Any]],
        event_filter: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param actions: actions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#actions CognitoRiskConfiguration#actions}
        :param event_filter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#event_filter CognitoRiskConfiguration#event_filter}.
        '''
        if isinstance(actions, dict):
            actions = CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActions(**actions)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9e25f74d3838621cd7227f9d117f8c28341cab2b9097d92e9ab8282b6fbe342)
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument event_filter", value=event_filter, expected_type=type_hints["event_filter"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "actions": actions,
        }
        if event_filter is not None:
            self._values["event_filter"] = event_filter

    @builtins.property
    def actions(
        self,
    ) -> "CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActions":
        '''actions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#actions CognitoRiskConfiguration#actions}
        '''
        result = self._values.get("actions")
        assert result is not None, "Required property 'actions' is missing"
        return typing.cast("CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActions", result)

    @builtins.property
    def event_filter(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#event_filter CognitoRiskConfiguration#event_filter}.'''
        result = self._values.get("event_filter")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoRiskConfigurationCompromisedCredentialsRiskConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.cognitoRiskConfiguration.CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActions",
    jsii_struct_bases=[],
    name_mapping={"event_action": "eventAction"},
)
class CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActions:
    def __init__(self, *, event_action: builtins.str) -> None:
        '''
        :param event_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#event_action CognitoRiskConfiguration#event_action}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fa3c30e9ca329d866c909ce42614f65e264f7926f86f318a1f8b68af18d8b2c)
            check_type(argname="argument event_action", value=event_action, expected_type=type_hints["event_action"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "event_action": event_action,
        }

    @builtins.property
    def event_action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#event_action CognitoRiskConfiguration#event_action}.'''
        result = self._values.get("event_action")
        assert result is not None, "Required property 'event_action' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoRiskConfiguration.CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__218516ea9634d74c45a3dcece846ef8e09dc910aa7ad216b22b553baa0a79567)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="eventActionInput")
    def event_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventActionInput"))

    @builtins.property
    @jsii.member(jsii_name="eventAction")
    def event_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventAction"))

    @event_action.setter
    def event_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b36ce35b6428674e8728cf7415abb6643d8a0353e7d50368abca98b2966ec256)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventAction", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActions]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e09e4a23cd57e6f91799f23c842c91913f71ceab1ebaede809465ab5f26d20ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoRiskConfiguration.CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__99e1ddcb75d383f3a6ca12a98b5a6345c1f9c605986bb0b721d97c67ab0bc6ff)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putActions")
    def put_actions(self, *, event_action: builtins.str) -> None:
        '''
        :param event_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#event_action CognitoRiskConfiguration#event_action}.
        '''
        value = CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActions(
            event_action=event_action
        )

        return typing.cast(None, jsii.invoke(self, "putActions", [value]))

    @jsii.member(jsii_name="resetEventFilter")
    def reset_event_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventFilter", []))

    @builtins.property
    @jsii.member(jsii_name="actions")
    def actions(
        self,
    ) -> CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActionsOutputReference:
        return typing.cast(CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActionsOutputReference, jsii.get(self, "actions"))

    @builtins.property
    @jsii.member(jsii_name="actionsInput")
    def actions_input(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActions]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActions], jsii.get(self, "actionsInput"))

    @builtins.property
    @jsii.member(jsii_name="eventFilterInput")
    def event_filter_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "eventFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="eventFilter")
    def event_filter(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "eventFilter"))

    @event_filter.setter
    def event_filter(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ba9d6f130b69e8630048bbc021e1851a34baa562dd174748e1a8934130bf6e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventFilter", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationCompromisedCredentialsRiskConfiguration]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationCompromisedCredentialsRiskConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoRiskConfigurationCompromisedCredentialsRiskConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef55ba96fd48d533fc022708c4d6636d4606b249229f77beb1d2bc294d3caad7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cognitoRiskConfiguration.CognitoRiskConfigurationConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "user_pool_id": "userPoolId",
        "account_takeover_risk_configuration": "accountTakeoverRiskConfiguration",
        "client_id": "clientId",
        "compromised_credentials_risk_configuration": "compromisedCredentialsRiskConfiguration",
        "id": "id",
        "risk_exception_configuration": "riskExceptionConfiguration",
    },
)
class CognitoRiskConfigurationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        user_pool_id: builtins.str,
        account_takeover_risk_configuration: typing.Optional[typing.Union[CognitoRiskConfigurationAccountTakeoverRiskConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
        client_id: typing.Optional[builtins.str] = None,
        compromised_credentials_risk_configuration: typing.Optional[typing.Union[CognitoRiskConfigurationCompromisedCredentialsRiskConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        risk_exception_configuration: typing.Optional[typing.Union["CognitoRiskConfigurationRiskExceptionConfiguration", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param user_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#user_pool_id CognitoRiskConfiguration#user_pool_id}.
        :param account_takeover_risk_configuration: account_takeover_risk_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#account_takeover_risk_configuration CognitoRiskConfiguration#account_takeover_risk_configuration}
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#client_id CognitoRiskConfiguration#client_id}.
        :param compromised_credentials_risk_configuration: compromised_credentials_risk_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#compromised_credentials_risk_configuration CognitoRiskConfiguration#compromised_credentials_risk_configuration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#id CognitoRiskConfiguration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param risk_exception_configuration: risk_exception_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#risk_exception_configuration CognitoRiskConfiguration#risk_exception_configuration}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(account_takeover_risk_configuration, dict):
            account_takeover_risk_configuration = CognitoRiskConfigurationAccountTakeoverRiskConfiguration(**account_takeover_risk_configuration)
        if isinstance(compromised_credentials_risk_configuration, dict):
            compromised_credentials_risk_configuration = CognitoRiskConfigurationCompromisedCredentialsRiskConfiguration(**compromised_credentials_risk_configuration)
        if isinstance(risk_exception_configuration, dict):
            risk_exception_configuration = CognitoRiskConfigurationRiskExceptionConfiguration(**risk_exception_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7166e1216919ad8fbe876f6f31ad742e6f36cc850e760b173a310e3f29069048)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument user_pool_id", value=user_pool_id, expected_type=type_hints["user_pool_id"])
            check_type(argname="argument account_takeover_risk_configuration", value=account_takeover_risk_configuration, expected_type=type_hints["account_takeover_risk_configuration"])
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument compromised_credentials_risk_configuration", value=compromised_credentials_risk_configuration, expected_type=type_hints["compromised_credentials_risk_configuration"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument risk_exception_configuration", value=risk_exception_configuration, expected_type=type_hints["risk_exception_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "user_pool_id": user_pool_id,
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
        if account_takeover_risk_configuration is not None:
            self._values["account_takeover_risk_configuration"] = account_takeover_risk_configuration
        if client_id is not None:
            self._values["client_id"] = client_id
        if compromised_credentials_risk_configuration is not None:
            self._values["compromised_credentials_risk_configuration"] = compromised_credentials_risk_configuration
        if id is not None:
            self._values["id"] = id
        if risk_exception_configuration is not None:
            self._values["risk_exception_configuration"] = risk_exception_configuration

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
    def user_pool_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#user_pool_id CognitoRiskConfiguration#user_pool_id}.'''
        result = self._values.get("user_pool_id")
        assert result is not None, "Required property 'user_pool_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_takeover_risk_configuration(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfiguration]:
        '''account_takeover_risk_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#account_takeover_risk_configuration CognitoRiskConfiguration#account_takeover_risk_configuration}
        '''
        result = self._values.get("account_takeover_risk_configuration")
        return typing.cast(typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfiguration], result)

    @builtins.property
    def client_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#client_id CognitoRiskConfiguration#client_id}.'''
        result = self._values.get("client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def compromised_credentials_risk_configuration(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationCompromisedCredentialsRiskConfiguration]:
        '''compromised_credentials_risk_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#compromised_credentials_risk_configuration CognitoRiskConfiguration#compromised_credentials_risk_configuration}
        '''
        result = self._values.get("compromised_credentials_risk_configuration")
        return typing.cast(typing.Optional[CognitoRiskConfigurationCompromisedCredentialsRiskConfiguration], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#id CognitoRiskConfiguration#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def risk_exception_configuration(
        self,
    ) -> typing.Optional["CognitoRiskConfigurationRiskExceptionConfiguration"]:
        '''risk_exception_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#risk_exception_configuration CognitoRiskConfiguration#risk_exception_configuration}
        '''
        result = self._values.get("risk_exception_configuration")
        return typing.cast(typing.Optional["CognitoRiskConfigurationRiskExceptionConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoRiskConfigurationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.cognitoRiskConfiguration.CognitoRiskConfigurationRiskExceptionConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "blocked_ip_range_list": "blockedIpRangeList",
        "skipped_ip_range_list": "skippedIpRangeList",
    },
)
class CognitoRiskConfigurationRiskExceptionConfiguration:
    def __init__(
        self,
        *,
        blocked_ip_range_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        skipped_ip_range_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param blocked_ip_range_list: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#blocked_ip_range_list CognitoRiskConfiguration#blocked_ip_range_list}.
        :param skipped_ip_range_list: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#skipped_ip_range_list CognitoRiskConfiguration#skipped_ip_range_list}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93c9f44cfc8628cad7edb2caa3998b827088638555c45f92844c5b543c18ce07)
            check_type(argname="argument blocked_ip_range_list", value=blocked_ip_range_list, expected_type=type_hints["blocked_ip_range_list"])
            check_type(argname="argument skipped_ip_range_list", value=skipped_ip_range_list, expected_type=type_hints["skipped_ip_range_list"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if blocked_ip_range_list is not None:
            self._values["blocked_ip_range_list"] = blocked_ip_range_list
        if skipped_ip_range_list is not None:
            self._values["skipped_ip_range_list"] = skipped_ip_range_list

    @builtins.property
    def blocked_ip_range_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#blocked_ip_range_list CognitoRiskConfiguration#blocked_ip_range_list}.'''
        result = self._values.get("blocked_ip_range_list")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def skipped_ip_range_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cognito_risk_configuration#skipped_ip_range_list CognitoRiskConfiguration#skipped_ip_range_list}.'''
        result = self._values.get("skipped_ip_range_list")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CognitoRiskConfigurationRiskExceptionConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CognitoRiskConfigurationRiskExceptionConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cognitoRiskConfiguration.CognitoRiskConfigurationRiskExceptionConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bf5ab6ab585b956db9a58796f1c8ae3189cfe61dc4051e84e7e4071fca4d632c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBlockedIpRangeList")
    def reset_blocked_ip_range_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlockedIpRangeList", []))

    @jsii.member(jsii_name="resetSkippedIpRangeList")
    def reset_skipped_ip_range_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkippedIpRangeList", []))

    @builtins.property
    @jsii.member(jsii_name="blockedIpRangeListInput")
    def blocked_ip_range_list_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "blockedIpRangeListInput"))

    @builtins.property
    @jsii.member(jsii_name="skippedIpRangeListInput")
    def skipped_ip_range_list_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "skippedIpRangeListInput"))

    @builtins.property
    @jsii.member(jsii_name="blockedIpRangeList")
    def blocked_ip_range_list(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "blockedIpRangeList"))

    @blocked_ip_range_list.setter
    def blocked_ip_range_list(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff9ce5f74df8ec55ef512e031cea33c2e9b95d63ab2a880988444710ee937d35)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blockedIpRangeList", value)

    @builtins.property
    @jsii.member(jsii_name="skippedIpRangeList")
    def skipped_ip_range_list(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "skippedIpRangeList"))

    @skipped_ip_range_list.setter
    def skipped_ip_range_list(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2979e51df0b6720a4f52fdac3210e426dfed9f126b38dff45d7b337a3db4ccc8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skippedIpRangeList", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CognitoRiskConfigurationRiskExceptionConfiguration]:
        return typing.cast(typing.Optional[CognitoRiskConfigurationRiskExceptionConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CognitoRiskConfigurationRiskExceptionConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e510e769ba9260ce771280fb69c0c78ecb7a9324816e2ecb3c1a81d92287720e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CognitoRiskConfiguration",
    "CognitoRiskConfigurationAccountTakeoverRiskConfiguration",
    "CognitoRiskConfigurationAccountTakeoverRiskConfigurationActions",
    "CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighAction",
    "CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighActionOutputReference",
    "CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowAction",
    "CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowActionOutputReference",
    "CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumAction",
    "CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumActionOutputReference",
    "CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsOutputReference",
    "CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration",
    "CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmail",
    "CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmailOutputReference",
    "CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmail",
    "CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmailOutputReference",
    "CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmail",
    "CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmailOutputReference",
    "CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationOutputReference",
    "CognitoRiskConfigurationAccountTakeoverRiskConfigurationOutputReference",
    "CognitoRiskConfigurationCompromisedCredentialsRiskConfiguration",
    "CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActions",
    "CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActionsOutputReference",
    "CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationOutputReference",
    "CognitoRiskConfigurationConfig",
    "CognitoRiskConfigurationRiskExceptionConfiguration",
    "CognitoRiskConfigurationRiskExceptionConfigurationOutputReference",
]

publication.publish()

def _typecheckingstub__4975405c0a9ecba6d7bf5787ea8f5b108d6ea363ad44eb714630a55be3c59607(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    user_pool_id: builtins.str,
    account_takeover_risk_configuration: typing.Optional[typing.Union[CognitoRiskConfigurationAccountTakeoverRiskConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    client_id: typing.Optional[builtins.str] = None,
    compromised_credentials_risk_configuration: typing.Optional[typing.Union[CognitoRiskConfigurationCompromisedCredentialsRiskConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    risk_exception_configuration: typing.Optional[typing.Union[CognitoRiskConfigurationRiskExceptionConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__4a39dd4a43dfcbf4ed8ea8d7d0dd40abfd09afe04f76d4f7cda93c296ffd5f27(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ce0cf2eba8e99928de0b8d044273ff452951856313d6eed37fa42f326c5d8f6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1aa8439a4e87683d2fdcdf1cfa4953c518c280d5e1e7c345f6e4ee0a488fce3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5062fe94b85761492b37069357124c74c718022d1c9a3ebd480f81093a16736a(
    *,
    actions: typing.Union[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActions, typing.Dict[builtins.str, typing.Any]],
    notify_configuration: typing.Union[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a41e5b56247b5fa4c5560e62c55b3ca7a531f171d4b68d42f55a0ec5ac62e6d5(
    *,
    high_action: typing.Optional[typing.Union[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighAction, typing.Dict[builtins.str, typing.Any]]] = None,
    low_action: typing.Optional[typing.Union[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowAction, typing.Dict[builtins.str, typing.Any]]] = None,
    medium_action: typing.Optional[typing.Union[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumAction, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a85195aa42b3657ec5ead243c522bc929bf85bad285a91e7040d76278e1fd2d0(
    *,
    event_action: builtins.str,
    notify: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a20b149ded1d4c03832dab5db0e55fea38cf65e2c9ee0df467cbd8dbd3243b2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ccbbf4f4ba681c02a4c99d441c67d14b0fa2ac66047ac99e4f0761b72a34201(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5285be13bec1165d3fccb2d09b7260b3867b4c51ab64f93b089a75c622f47bd5(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e4a7fa6d893f207e82fbe18aaa2cf28e859609aa6e2d6dbc2183c39462be400(
    value: typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsHighAction],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d08ac501776803be321696c7b2cd0b2990f96cff8b094eb9a8bda4cce483e39a(
    *,
    event_action: builtins.str,
    notify: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48aa5693849c154f78af9481cb8849eb56898085201f1e0a4afd9c5a6c39c1d3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5eb0e38fa735ca18b1142fe1cf4e40ee032ee1160ae876ccd97b679db953c24e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c76749de380f4f2db11eeaa131ddd7cffbca4de4ee9d7e6d36b0842c93730993(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9620c7559e866451fc552eb66c0f5155d864afa9223f6d6dede85eab153cb2ec(
    value: typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsLowAction],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a6dff1dbddd68503734520d2e1b10ee095fa2b6f63da1be1c68850e39fc4f87(
    *,
    event_action: builtins.str,
    notify: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96ed3bf65f2ac4bbb0472a52ccbe36bec312b259ecd6cd1aa65b925df993204a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbb492f781bc1b5c5ba2a141ec602715f95499c27f4a5fedeccdbc65488d4019(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55de81d13c13fb82380664aca46099c8af3384c6a1c26451d33b5f3d760f39a1(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32b1d8396dc8fe0aac85f51169a4105d4d768f16ea61569484594af1c3ae683a(
    value: typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActionsMediumAction],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__607f0cfabe7ed8894d933b12643e34f7cc96861bbdcdc86d70039dd49309e0e3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cab567735a565d3458e78d4f2af45de82fb456bf3f9ffe01bdb3245fda695b2e(
    value: typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationActions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1acc44cef8cea03771e23a0bb54b15679655f8a80c47054809fd376a67fcb6a0(
    *,
    source_arn: builtins.str,
    block_email: typing.Optional[typing.Union[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmail, typing.Dict[builtins.str, typing.Any]]] = None,
    from_: typing.Optional[builtins.str] = None,
    mfa_email: typing.Optional[typing.Union[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmail, typing.Dict[builtins.str, typing.Any]]] = None,
    no_action_email: typing.Optional[typing.Union[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmail, typing.Dict[builtins.str, typing.Any]]] = None,
    reply_to: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__505a339a314438d934ed528f037ca2a0dc82b2029fa3301a7df958fc2e107cf4(
    *,
    html_body: builtins.str,
    subject: builtins.str,
    text_body: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1425b73427c9a7dba13eb3cb90a8a1cc463a764c9a94dfad1d0c4953d8a00a14(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a77fcfbbb15e0f13527da0f4514c3be2bb31b2727b44e4d8d1ca40815d6b80f4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f6cadded9e9998a6e0de8ba805c182672bacde2238a77ebcc1b7ee4d3188087(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92c8d002a89436341473983ee5b449d8ddf8d105041c8a8a241608e64a0612d9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c1f0f1530b86eb887a8d312d4c1faf9a123b5006f9d1d11cdb40c300e09465d(
    value: typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationBlockEmail],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04bf5562e491b0803b360f5f498c598e994ef8a3df6a00b029f94cea1858054a(
    *,
    html_body: builtins.str,
    subject: builtins.str,
    text_body: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04f3a7d6e9f76a1ad9a9013daaedfc0c3a4ce85f0be478b880863c898cc0ad50(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0e2e3be4a8dcf5530bad1ef381f340e766c9b034887abaa0a0b9d4bc4184726(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5744337d929c2448f343a4b5e193c2503829a09b10204e4999b7a8e81635491(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a65ca680a9abeb9162fb77ea47469092e1c33f01ec5d09661559d1c55c475619(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__835fd406f065de9a1fdcad4af4d477eac1c5f2abc3047a2d74b95554ebc05bfc(
    value: typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationMfaEmail],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89e81f65bef0d07ab185db2cb06f249645044f77c457394aa3aa2b46d82fff85(
    *,
    html_body: builtins.str,
    subject: builtins.str,
    text_body: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa018a7e0f5d8c2fa13809615a1ee9930831ae7be0e2c6c042c99120927f507a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b10327998b794b41de558853a1656d6b9e98f3e7881d7eb3664c461e0f1f7643(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2cb998415412896ffb42d2911ab0c14eefdfa7a4132cfe3a7709633e6471d9c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99f15138c2772b67bcf171e1de70aba8a4867a6b4fc46e7f1f8340eb6beb0a83(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2420d71fe7f8f98b48bd16f80e4b66486e3837a8102f7d41a222eae9c9e944ba(
    value: typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfigurationNoActionEmail],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a35060ecd1dab0826faf15874329992f5b1d5a5c9d6569fb0ff4f61338aa9e75(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd538912d81b4581f05f070e2aceb2590888be1cccc98f00ae483179085f2b07(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f52013bd6613a75e837fff308c569e9ffd52f2ae0e3a064a91968d876797feb2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55e75846657ec8f4ee2d3518c803fe4bff5fb4b2a3c050c8edd8c3ee96f74f27(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98fae82adb33989d5e2f959f522589775e3ae64cdf60ab123b584c6d06b7c0f6(
    value: typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfigurationNotifyConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d3cd83682d7d087c32e686911dfc5a9ea36bd187aaaa61d3035be36d99f8315(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__189e1c9696289b5ce288a83662c896cbea5443417912f0f19183fc0746a35ad1(
    value: typing.Optional[CognitoRiskConfigurationAccountTakeoverRiskConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9e25f74d3838621cd7227f9d117f8c28341cab2b9097d92e9ab8282b6fbe342(
    *,
    actions: typing.Union[CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActions, typing.Dict[builtins.str, typing.Any]],
    event_filter: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fa3c30e9ca329d866c909ce42614f65e264f7926f86f318a1f8b68af18d8b2c(
    *,
    event_action: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__218516ea9634d74c45a3dcece846ef8e09dc910aa7ad216b22b553baa0a79567(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b36ce35b6428674e8728cf7415abb6643d8a0353e7d50368abca98b2966ec256(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e09e4a23cd57e6f91799f23c842c91913f71ceab1ebaede809465ab5f26d20ca(
    value: typing.Optional[CognitoRiskConfigurationCompromisedCredentialsRiskConfigurationActions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99e1ddcb75d383f3a6ca12a98b5a6345c1f9c605986bb0b721d97c67ab0bc6ff(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ba9d6f130b69e8630048bbc021e1851a34baa562dd174748e1a8934130bf6e5(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef55ba96fd48d533fc022708c4d6636d4606b249229f77beb1d2bc294d3caad7(
    value: typing.Optional[CognitoRiskConfigurationCompromisedCredentialsRiskConfiguration],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7166e1216919ad8fbe876f6f31ad742e6f36cc850e760b173a310e3f29069048(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    user_pool_id: builtins.str,
    account_takeover_risk_configuration: typing.Optional[typing.Union[CognitoRiskConfigurationAccountTakeoverRiskConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    client_id: typing.Optional[builtins.str] = None,
    compromised_credentials_risk_configuration: typing.Optional[typing.Union[CognitoRiskConfigurationCompromisedCredentialsRiskConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    risk_exception_configuration: typing.Optional[typing.Union[CognitoRiskConfigurationRiskExceptionConfiguration, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93c9f44cfc8628cad7edb2caa3998b827088638555c45f92844c5b543c18ce07(
    *,
    blocked_ip_range_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    skipped_ip_range_list: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf5ab6ab585b956db9a58796f1c8ae3189cfe61dc4051e84e7e4071fca4d632c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff9ce5f74df8ec55ef512e031cea33c2e9b95d63ab2a880988444710ee937d35(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2979e51df0b6720a4f52fdac3210e426dfed9f126b38dff45d7b337a3db4ccc8(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e510e769ba9260ce771280fb69c0c78ecb7a9324816e2ecb3c1a81d92287720e(
    value: typing.Optional[CognitoRiskConfigurationRiskExceptionConfiguration],
) -> None:
    """Type checking stubs"""
    pass
