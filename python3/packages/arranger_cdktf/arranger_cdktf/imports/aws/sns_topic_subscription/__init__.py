'''
# `aws_sns_topic_subscription`

Refer to the Terraform Registory for docs: [`aws_sns_topic_subscription`](https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription).
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


class SnsTopicSubscription(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.snsTopicSubscription.SnsTopicSubscription",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription aws_sns_topic_subscription}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        endpoint: builtins.str,
        protocol: builtins.str,
        topic_arn: builtins.str,
        confirmation_timeout_in_minutes: typing.Optional[jsii.Number] = None,
        delivery_policy: typing.Optional[builtins.str] = None,
        endpoint_auto_confirms: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        filter_policy: typing.Optional[builtins.str] = None,
        filter_policy_scope: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        raw_message_delivery: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        redrive_policy: typing.Optional[builtins.str] = None,
        subscription_role_arn: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription aws_sns_topic_subscription} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription#endpoint SnsTopicSubscription#endpoint}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription#protocol SnsTopicSubscription#protocol}.
        :param topic_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription#topic_arn SnsTopicSubscription#topic_arn}.
        :param confirmation_timeout_in_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription#confirmation_timeout_in_minutes SnsTopicSubscription#confirmation_timeout_in_minutes}.
        :param delivery_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription#delivery_policy SnsTopicSubscription#delivery_policy}.
        :param endpoint_auto_confirms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription#endpoint_auto_confirms SnsTopicSubscription#endpoint_auto_confirms}.
        :param filter_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription#filter_policy SnsTopicSubscription#filter_policy}.
        :param filter_policy_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription#filter_policy_scope SnsTopicSubscription#filter_policy_scope}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription#id SnsTopicSubscription#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param raw_message_delivery: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription#raw_message_delivery SnsTopicSubscription#raw_message_delivery}.
        :param redrive_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription#redrive_policy SnsTopicSubscription#redrive_policy}.
        :param subscription_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription#subscription_role_arn SnsTopicSubscription#subscription_role_arn}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f3eea998b2e96456dd3ac41dcb17beb3866375efaa310aa46056962951aba48)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SnsTopicSubscriptionConfig(
            endpoint=endpoint,
            protocol=protocol,
            topic_arn=topic_arn,
            confirmation_timeout_in_minutes=confirmation_timeout_in_minutes,
            delivery_policy=delivery_policy,
            endpoint_auto_confirms=endpoint_auto_confirms,
            filter_policy=filter_policy,
            filter_policy_scope=filter_policy_scope,
            id=id,
            raw_message_delivery=raw_message_delivery,
            redrive_policy=redrive_policy,
            subscription_role_arn=subscription_role_arn,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetConfirmationTimeoutInMinutes")
    def reset_confirmation_timeout_in_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfirmationTimeoutInMinutes", []))

    @jsii.member(jsii_name="resetDeliveryPolicy")
    def reset_delivery_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeliveryPolicy", []))

    @jsii.member(jsii_name="resetEndpointAutoConfirms")
    def reset_endpoint_auto_confirms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpointAutoConfirms", []))

    @jsii.member(jsii_name="resetFilterPolicy")
    def reset_filter_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilterPolicy", []))

    @jsii.member(jsii_name="resetFilterPolicyScope")
    def reset_filter_policy_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilterPolicyScope", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetRawMessageDelivery")
    def reset_raw_message_delivery(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRawMessageDelivery", []))

    @jsii.member(jsii_name="resetRedrivePolicy")
    def reset_redrive_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedrivePolicy", []))

    @jsii.member(jsii_name="resetSubscriptionRoleArn")
    def reset_subscription_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubscriptionRoleArn", []))

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
    @jsii.member(jsii_name="confirmationWasAuthenticated")
    def confirmation_was_authenticated(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "confirmationWasAuthenticated"))

    @builtins.property
    @jsii.member(jsii_name="ownerId")
    def owner_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ownerId"))

    @builtins.property
    @jsii.member(jsii_name="pendingConfirmation")
    def pending_confirmation(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "pendingConfirmation"))

    @builtins.property
    @jsii.member(jsii_name="confirmationTimeoutInMinutesInput")
    def confirmation_timeout_in_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "confirmationTimeoutInMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="deliveryPolicyInput")
    def delivery_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deliveryPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointAutoConfirmsInput")
    def endpoint_auto_confirms_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "endpointAutoConfirmsInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="filterPolicyInput")
    def filter_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filterPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="filterPolicyScopeInput")
    def filter_policy_scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filterPolicyScopeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="rawMessageDeliveryInput")
    def raw_message_delivery_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "rawMessageDeliveryInput"))

    @builtins.property
    @jsii.member(jsii_name="redrivePolicyInput")
    def redrive_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redrivePolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="subscriptionRoleArnInput")
    def subscription_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subscriptionRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="topicArnInput")
    def topic_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "topicArnInput"))

    @builtins.property
    @jsii.member(jsii_name="confirmationTimeoutInMinutes")
    def confirmation_timeout_in_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "confirmationTimeoutInMinutes"))

    @confirmation_timeout_in_minutes.setter
    def confirmation_timeout_in_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4eb7e39a5481aaf8c3ed9196100a22136191f5e69415f785c463d3f1515feab6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "confirmationTimeoutInMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="deliveryPolicy")
    def delivery_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deliveryPolicy"))

    @delivery_policy.setter
    def delivery_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e9c087060300def9223e4b69b3887806068cd941a824aa8750774f73d1960e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f404459efd62122f6dc27443759ece7ba6a960fe8521e19b75aed639ab41ab0e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="endpointAutoConfirms")
    def endpoint_auto_confirms(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "endpointAutoConfirms"))

    @endpoint_auto_confirms.setter
    def endpoint_auto_confirms(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e8d9ee35da6d7b25987b6ddb259d44e7a394a623045fe6b9e84eb59b0b77012)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointAutoConfirms", value)

    @builtins.property
    @jsii.member(jsii_name="filterPolicy")
    def filter_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filterPolicy"))

    @filter_policy.setter
    def filter_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a20c39b1b12f76954ee27c11b211f8ef5756c6be2d32477a261100233d860cf8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filterPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="filterPolicyScope")
    def filter_policy_scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filterPolicyScope"))

    @filter_policy_scope.setter
    def filter_policy_scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46e825f307a7fb327da6710493c0ed0be1b41a1769eff70a066714b8f67b93ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filterPolicyScope", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7bb1ce84f3810924b44242c6d2e3a4308a401a40db0deb0f03dd2f654f41ea2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30ec3e1544657542c96d9ceed66ae732ea9ebce72f64c9e4da0299476ae7ab5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="rawMessageDelivery")
    def raw_message_delivery(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "rawMessageDelivery"))

    @raw_message_delivery.setter
    def raw_message_delivery(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ceed546578bf3ede2f52ffb93dad88c3f7a9123e57b7d86258031ebfb0317b80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rawMessageDelivery", value)

    @builtins.property
    @jsii.member(jsii_name="redrivePolicy")
    def redrive_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redrivePolicy"))

    @redrive_policy.setter
    def redrive_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfdf6db0e358e07aa6cce14257e516110cf083cf0310a1c746df5249ca1ad759)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redrivePolicy", value)

    @builtins.property
    @jsii.member(jsii_name="subscriptionRoleArn")
    def subscription_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subscriptionRoleArn"))

    @subscription_role_arn.setter
    def subscription_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b088d468f33f89a87cb6687d7b821434f0156d7cd8371706a75641713a0a4187)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subscriptionRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="topicArn")
    def topic_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "topicArn"))

    @topic_arn.setter
    def topic_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__791bbab02c103c26bf967923681e744f3300a2e28819d2754e0b0ee6e16ae485)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "topicArn", value)


@jsii.data_type(
    jsii_type="aws.snsTopicSubscription.SnsTopicSubscriptionConfig",
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
        "protocol": "protocol",
        "topic_arn": "topicArn",
        "confirmation_timeout_in_minutes": "confirmationTimeoutInMinutes",
        "delivery_policy": "deliveryPolicy",
        "endpoint_auto_confirms": "endpointAutoConfirms",
        "filter_policy": "filterPolicy",
        "filter_policy_scope": "filterPolicyScope",
        "id": "id",
        "raw_message_delivery": "rawMessageDelivery",
        "redrive_policy": "redrivePolicy",
        "subscription_role_arn": "subscriptionRoleArn",
    },
)
class SnsTopicSubscriptionConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        endpoint: builtins.str,
        protocol: builtins.str,
        topic_arn: builtins.str,
        confirmation_timeout_in_minutes: typing.Optional[jsii.Number] = None,
        delivery_policy: typing.Optional[builtins.str] = None,
        endpoint_auto_confirms: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        filter_policy: typing.Optional[builtins.str] = None,
        filter_policy_scope: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        raw_message_delivery: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        redrive_policy: typing.Optional[builtins.str] = None,
        subscription_role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription#endpoint SnsTopicSubscription#endpoint}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription#protocol SnsTopicSubscription#protocol}.
        :param topic_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription#topic_arn SnsTopicSubscription#topic_arn}.
        :param confirmation_timeout_in_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription#confirmation_timeout_in_minutes SnsTopicSubscription#confirmation_timeout_in_minutes}.
        :param delivery_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription#delivery_policy SnsTopicSubscription#delivery_policy}.
        :param endpoint_auto_confirms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription#endpoint_auto_confirms SnsTopicSubscription#endpoint_auto_confirms}.
        :param filter_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription#filter_policy SnsTopicSubscription#filter_policy}.
        :param filter_policy_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription#filter_policy_scope SnsTopicSubscription#filter_policy_scope}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription#id SnsTopicSubscription#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param raw_message_delivery: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription#raw_message_delivery SnsTopicSubscription#raw_message_delivery}.
        :param redrive_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription#redrive_policy SnsTopicSubscription#redrive_policy}.
        :param subscription_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription#subscription_role_arn SnsTopicSubscription#subscription_role_arn}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__456eb59b19f69f629e448e2aa793177b46c27fdfc95b6eeaf6a9fc069128a9ba)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
            check_type(argname="argument confirmation_timeout_in_minutes", value=confirmation_timeout_in_minutes, expected_type=type_hints["confirmation_timeout_in_minutes"])
            check_type(argname="argument delivery_policy", value=delivery_policy, expected_type=type_hints["delivery_policy"])
            check_type(argname="argument endpoint_auto_confirms", value=endpoint_auto_confirms, expected_type=type_hints["endpoint_auto_confirms"])
            check_type(argname="argument filter_policy", value=filter_policy, expected_type=type_hints["filter_policy"])
            check_type(argname="argument filter_policy_scope", value=filter_policy_scope, expected_type=type_hints["filter_policy_scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument raw_message_delivery", value=raw_message_delivery, expected_type=type_hints["raw_message_delivery"])
            check_type(argname="argument redrive_policy", value=redrive_policy, expected_type=type_hints["redrive_policy"])
            check_type(argname="argument subscription_role_arn", value=subscription_role_arn, expected_type=type_hints["subscription_role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoint": endpoint,
            "protocol": protocol,
            "topic_arn": topic_arn,
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
        if confirmation_timeout_in_minutes is not None:
            self._values["confirmation_timeout_in_minutes"] = confirmation_timeout_in_minutes
        if delivery_policy is not None:
            self._values["delivery_policy"] = delivery_policy
        if endpoint_auto_confirms is not None:
            self._values["endpoint_auto_confirms"] = endpoint_auto_confirms
        if filter_policy is not None:
            self._values["filter_policy"] = filter_policy
        if filter_policy_scope is not None:
            self._values["filter_policy_scope"] = filter_policy_scope
        if id is not None:
            self._values["id"] = id
        if raw_message_delivery is not None:
            self._values["raw_message_delivery"] = raw_message_delivery
        if redrive_policy is not None:
            self._values["redrive_policy"] = redrive_policy
        if subscription_role_arn is not None:
            self._values["subscription_role_arn"] = subscription_role_arn

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
    def endpoint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription#endpoint SnsTopicSubscription#endpoint}.'''
        result = self._values.get("endpoint")
        assert result is not None, "Required property 'endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription#protocol SnsTopicSubscription#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def topic_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription#topic_arn SnsTopicSubscription#topic_arn}.'''
        result = self._values.get("topic_arn")
        assert result is not None, "Required property 'topic_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def confirmation_timeout_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription#confirmation_timeout_in_minutes SnsTopicSubscription#confirmation_timeout_in_minutes}.'''
        result = self._values.get("confirmation_timeout_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def delivery_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription#delivery_policy SnsTopicSubscription#delivery_policy}.'''
        result = self._values.get("delivery_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoint_auto_confirms(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription#endpoint_auto_confirms SnsTopicSubscription#endpoint_auto_confirms}.'''
        result = self._values.get("endpoint_auto_confirms")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def filter_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription#filter_policy SnsTopicSubscription#filter_policy}.'''
        result = self._values.get("filter_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def filter_policy_scope(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription#filter_policy_scope SnsTopicSubscription#filter_policy_scope}.'''
        result = self._values.get("filter_policy_scope")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription#id SnsTopicSubscription#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def raw_message_delivery(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription#raw_message_delivery SnsTopicSubscription#raw_message_delivery}.'''
        result = self._values.get("raw_message_delivery")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def redrive_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription#redrive_policy SnsTopicSubscription#redrive_policy}.'''
        result = self._values.get("redrive_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subscription_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription#subscription_role_arn SnsTopicSubscription#subscription_role_arn}.'''
        result = self._values.get("subscription_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SnsTopicSubscriptionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "SnsTopicSubscription",
    "SnsTopicSubscriptionConfig",
]

publication.publish()

def _typecheckingstub__3f3eea998b2e96456dd3ac41dcb17beb3866375efaa310aa46056962951aba48(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    endpoint: builtins.str,
    protocol: builtins.str,
    topic_arn: builtins.str,
    confirmation_timeout_in_minutes: typing.Optional[jsii.Number] = None,
    delivery_policy: typing.Optional[builtins.str] = None,
    endpoint_auto_confirms: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    filter_policy: typing.Optional[builtins.str] = None,
    filter_policy_scope: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    raw_message_delivery: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    redrive_policy: typing.Optional[builtins.str] = None,
    subscription_role_arn: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__4eb7e39a5481aaf8c3ed9196100a22136191f5e69415f785c463d3f1515feab6(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e9c087060300def9223e4b69b3887806068cd941a824aa8750774f73d1960e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f404459efd62122f6dc27443759ece7ba6a960fe8521e19b75aed639ab41ab0e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e8d9ee35da6d7b25987b6ddb259d44e7a394a623045fe6b9e84eb59b0b77012(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a20c39b1b12f76954ee27c11b211f8ef5756c6be2d32477a261100233d860cf8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46e825f307a7fb327da6710493c0ed0be1b41a1769eff70a066714b8f67b93ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7bb1ce84f3810924b44242c6d2e3a4308a401a40db0deb0f03dd2f654f41ea2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30ec3e1544657542c96d9ceed66ae732ea9ebce72f64c9e4da0299476ae7ab5c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ceed546578bf3ede2f52ffb93dad88c3f7a9123e57b7d86258031ebfb0317b80(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfdf6db0e358e07aa6cce14257e516110cf083cf0310a1c746df5249ca1ad759(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b088d468f33f89a87cb6687d7b821434f0156d7cd8371706a75641713a0a4187(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__791bbab02c103c26bf967923681e744f3300a2e28819d2754e0b0ee6e16ae485(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__456eb59b19f69f629e448e2aa793177b46c27fdfc95b6eeaf6a9fc069128a9ba(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    endpoint: builtins.str,
    protocol: builtins.str,
    topic_arn: builtins.str,
    confirmation_timeout_in_minutes: typing.Optional[jsii.Number] = None,
    delivery_policy: typing.Optional[builtins.str] = None,
    endpoint_auto_confirms: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    filter_policy: typing.Optional[builtins.str] = None,
    filter_policy_scope: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    raw_message_delivery: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    redrive_policy: typing.Optional[builtins.str] = None,
    subscription_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
