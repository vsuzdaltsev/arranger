'''
# `aws_cloudfront_monitoring_subscription`

Refer to the Terraform Registory for docs: [`aws_cloudfront_monitoring_subscription`](https://www.terraform.io/docs/providers/aws/r/cloudfront_monitoring_subscription).
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


class CloudfrontMonitoringSubscription(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontMonitoringSubscription.CloudfrontMonitoringSubscription",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_monitoring_subscription aws_cloudfront_monitoring_subscription}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        distribution_id: builtins.str,
        monitoring_subscription: typing.Union["CloudfrontMonitoringSubscriptionMonitoringSubscription", typing.Dict[builtins.str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_monitoring_subscription aws_cloudfront_monitoring_subscription} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param distribution_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_monitoring_subscription#distribution_id CloudfrontMonitoringSubscription#distribution_id}.
        :param monitoring_subscription: monitoring_subscription block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_monitoring_subscription#monitoring_subscription CloudfrontMonitoringSubscription#monitoring_subscription}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_monitoring_subscription#id CloudfrontMonitoringSubscription#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d7c451eec309ee7bf13d6fd8eb47753a1190258aca539ee1f2d44648e48f173)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CloudfrontMonitoringSubscriptionConfig(
            distribution_id=distribution_id,
            monitoring_subscription=monitoring_subscription,
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

    @jsii.member(jsii_name="putMonitoringSubscription")
    def put_monitoring_subscription(
        self,
        *,
        realtime_metrics_subscription_config: typing.Union["CloudfrontMonitoringSubscriptionMonitoringSubscriptionRealtimeMetricsSubscriptionConfig", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param realtime_metrics_subscription_config: realtime_metrics_subscription_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_monitoring_subscription#realtime_metrics_subscription_config CloudfrontMonitoringSubscription#realtime_metrics_subscription_config}
        '''
        value = CloudfrontMonitoringSubscriptionMonitoringSubscription(
            realtime_metrics_subscription_config=realtime_metrics_subscription_config
        )

        return typing.cast(None, jsii.invoke(self, "putMonitoringSubscription", [value]))

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
    @jsii.member(jsii_name="monitoringSubscription")
    def monitoring_subscription(
        self,
    ) -> "CloudfrontMonitoringSubscriptionMonitoringSubscriptionOutputReference":
        return typing.cast("CloudfrontMonitoringSubscriptionMonitoringSubscriptionOutputReference", jsii.get(self, "monitoringSubscription"))

    @builtins.property
    @jsii.member(jsii_name="distributionIdInput")
    def distribution_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "distributionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="monitoringSubscriptionInput")
    def monitoring_subscription_input(
        self,
    ) -> typing.Optional["CloudfrontMonitoringSubscriptionMonitoringSubscription"]:
        return typing.cast(typing.Optional["CloudfrontMonitoringSubscriptionMonitoringSubscription"], jsii.get(self, "monitoringSubscriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="distributionId")
    def distribution_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "distributionId"))

    @distribution_id.setter
    def distribution_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a1d7a450ca8897ef03fd271bcc63cc2fedcea3b8149f9aa03aaa210b077fe9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "distributionId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccbe5b84fa919e1aac8f8bed01d5875516bd2f282a1a409e939784f0b9ca784c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="aws.cloudfrontMonitoringSubscription.CloudfrontMonitoringSubscriptionConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "distribution_id": "distributionId",
        "monitoring_subscription": "monitoringSubscription",
        "id": "id",
    },
)
class CloudfrontMonitoringSubscriptionConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        distribution_id: builtins.str,
        monitoring_subscription: typing.Union["CloudfrontMonitoringSubscriptionMonitoringSubscription", typing.Dict[builtins.str, typing.Any]],
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
        :param distribution_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_monitoring_subscription#distribution_id CloudfrontMonitoringSubscription#distribution_id}.
        :param monitoring_subscription: monitoring_subscription block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_monitoring_subscription#monitoring_subscription CloudfrontMonitoringSubscription#monitoring_subscription}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_monitoring_subscription#id CloudfrontMonitoringSubscription#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(monitoring_subscription, dict):
            monitoring_subscription = CloudfrontMonitoringSubscriptionMonitoringSubscription(**monitoring_subscription)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acfb4c0f9abc04392e437f115025b6e31f8d9c4035c087fe25495406aa0575a8)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument distribution_id", value=distribution_id, expected_type=type_hints["distribution_id"])
            check_type(argname="argument monitoring_subscription", value=monitoring_subscription, expected_type=type_hints["monitoring_subscription"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "distribution_id": distribution_id,
            "monitoring_subscription": monitoring_subscription,
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
    def distribution_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_monitoring_subscription#distribution_id CloudfrontMonitoringSubscription#distribution_id}.'''
        result = self._values.get("distribution_id")
        assert result is not None, "Required property 'distribution_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def monitoring_subscription(
        self,
    ) -> "CloudfrontMonitoringSubscriptionMonitoringSubscription":
        '''monitoring_subscription block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_monitoring_subscription#monitoring_subscription CloudfrontMonitoringSubscription#monitoring_subscription}
        '''
        result = self._values.get("monitoring_subscription")
        assert result is not None, "Required property 'monitoring_subscription' is missing"
        return typing.cast("CloudfrontMonitoringSubscriptionMonitoringSubscription", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_monitoring_subscription#id CloudfrontMonitoringSubscription#id}.

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
        return "CloudfrontMonitoringSubscriptionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.cloudfrontMonitoringSubscription.CloudfrontMonitoringSubscriptionMonitoringSubscription",
    jsii_struct_bases=[],
    name_mapping={
        "realtime_metrics_subscription_config": "realtimeMetricsSubscriptionConfig",
    },
)
class CloudfrontMonitoringSubscriptionMonitoringSubscription:
    def __init__(
        self,
        *,
        realtime_metrics_subscription_config: typing.Union["CloudfrontMonitoringSubscriptionMonitoringSubscriptionRealtimeMetricsSubscriptionConfig", typing.Dict[builtins.str, typing.Any]],
    ) -> None:
        '''
        :param realtime_metrics_subscription_config: realtime_metrics_subscription_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_monitoring_subscription#realtime_metrics_subscription_config CloudfrontMonitoringSubscription#realtime_metrics_subscription_config}
        '''
        if isinstance(realtime_metrics_subscription_config, dict):
            realtime_metrics_subscription_config = CloudfrontMonitoringSubscriptionMonitoringSubscriptionRealtimeMetricsSubscriptionConfig(**realtime_metrics_subscription_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd2a2533e19c4e7a8b58e80a3cfeee57fc2c91c747c7932016e8af6217049163)
            check_type(argname="argument realtime_metrics_subscription_config", value=realtime_metrics_subscription_config, expected_type=type_hints["realtime_metrics_subscription_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "realtime_metrics_subscription_config": realtime_metrics_subscription_config,
        }

    @builtins.property
    def realtime_metrics_subscription_config(
        self,
    ) -> "CloudfrontMonitoringSubscriptionMonitoringSubscriptionRealtimeMetricsSubscriptionConfig":
        '''realtime_metrics_subscription_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_monitoring_subscription#realtime_metrics_subscription_config CloudfrontMonitoringSubscription#realtime_metrics_subscription_config}
        '''
        result = self._values.get("realtime_metrics_subscription_config")
        assert result is not None, "Required property 'realtime_metrics_subscription_config' is missing"
        return typing.cast("CloudfrontMonitoringSubscriptionMonitoringSubscriptionRealtimeMetricsSubscriptionConfig", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontMonitoringSubscriptionMonitoringSubscription(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontMonitoringSubscriptionMonitoringSubscriptionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontMonitoringSubscription.CloudfrontMonitoringSubscriptionMonitoringSubscriptionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__df26c7563415717319fc62dbc7dc92e56ee14b649b3d167228a061ed23b065f6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRealtimeMetricsSubscriptionConfig")
    def put_realtime_metrics_subscription_config(
        self,
        *,
        realtime_metrics_subscription_status: builtins.str,
    ) -> None:
        '''
        :param realtime_metrics_subscription_status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_monitoring_subscription#realtime_metrics_subscription_status CloudfrontMonitoringSubscription#realtime_metrics_subscription_status}.
        '''
        value = CloudfrontMonitoringSubscriptionMonitoringSubscriptionRealtimeMetricsSubscriptionConfig(
            realtime_metrics_subscription_status=realtime_metrics_subscription_status
        )

        return typing.cast(None, jsii.invoke(self, "putRealtimeMetricsSubscriptionConfig", [value]))

    @builtins.property
    @jsii.member(jsii_name="realtimeMetricsSubscriptionConfig")
    def realtime_metrics_subscription_config(
        self,
    ) -> "CloudfrontMonitoringSubscriptionMonitoringSubscriptionRealtimeMetricsSubscriptionConfigOutputReference":
        return typing.cast("CloudfrontMonitoringSubscriptionMonitoringSubscriptionRealtimeMetricsSubscriptionConfigOutputReference", jsii.get(self, "realtimeMetricsSubscriptionConfig"))

    @builtins.property
    @jsii.member(jsii_name="realtimeMetricsSubscriptionConfigInput")
    def realtime_metrics_subscription_config_input(
        self,
    ) -> typing.Optional["CloudfrontMonitoringSubscriptionMonitoringSubscriptionRealtimeMetricsSubscriptionConfig"]:
        return typing.cast(typing.Optional["CloudfrontMonitoringSubscriptionMonitoringSubscriptionRealtimeMetricsSubscriptionConfig"], jsii.get(self, "realtimeMetricsSubscriptionConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontMonitoringSubscriptionMonitoringSubscription]:
        return typing.cast(typing.Optional[CloudfrontMonitoringSubscriptionMonitoringSubscription], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontMonitoringSubscriptionMonitoringSubscription],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31df6e16bb5c8480d18262f46be2b8f21303faad06447f4bd87c2d043a034cb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.cloudfrontMonitoringSubscription.CloudfrontMonitoringSubscriptionMonitoringSubscriptionRealtimeMetricsSubscriptionConfig",
    jsii_struct_bases=[],
    name_mapping={
        "realtime_metrics_subscription_status": "realtimeMetricsSubscriptionStatus",
    },
)
class CloudfrontMonitoringSubscriptionMonitoringSubscriptionRealtimeMetricsSubscriptionConfig:
    def __init__(self, *, realtime_metrics_subscription_status: builtins.str) -> None:
        '''
        :param realtime_metrics_subscription_status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_monitoring_subscription#realtime_metrics_subscription_status CloudfrontMonitoringSubscription#realtime_metrics_subscription_status}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__375a23c138d5f5f70ff2b9e64386e95d431f9cdc86db0a20c881bafccc01ccdd)
            check_type(argname="argument realtime_metrics_subscription_status", value=realtime_metrics_subscription_status, expected_type=type_hints["realtime_metrics_subscription_status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "realtime_metrics_subscription_status": realtime_metrics_subscription_status,
        }

    @builtins.property
    def realtime_metrics_subscription_status(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/cloudfront_monitoring_subscription#realtime_metrics_subscription_status CloudfrontMonitoringSubscription#realtime_metrics_subscription_status}.'''
        result = self._values.get("realtime_metrics_subscription_status")
        assert result is not None, "Required property 'realtime_metrics_subscription_status' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudfrontMonitoringSubscriptionMonitoringSubscriptionRealtimeMetricsSubscriptionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudfrontMonitoringSubscriptionMonitoringSubscriptionRealtimeMetricsSubscriptionConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.cloudfrontMonitoringSubscription.CloudfrontMonitoringSubscriptionMonitoringSubscriptionRealtimeMetricsSubscriptionConfigOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__45e00d6abc04f0384936911f3aa8bb70d33918413b518897448eb6cae1988ce7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="realtimeMetricsSubscriptionStatusInput")
    def realtime_metrics_subscription_status_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "realtimeMetricsSubscriptionStatusInput"))

    @builtins.property
    @jsii.member(jsii_name="realtimeMetricsSubscriptionStatus")
    def realtime_metrics_subscription_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "realtimeMetricsSubscriptionStatus"))

    @realtime_metrics_subscription_status.setter
    def realtime_metrics_subscription_status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35e0c54eab4ab9f8c6660744e1da35ba7fdc1e7f8b0bc02414691bea3c958da8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "realtimeMetricsSubscriptionStatus", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudfrontMonitoringSubscriptionMonitoringSubscriptionRealtimeMetricsSubscriptionConfig]:
        return typing.cast(typing.Optional[CloudfrontMonitoringSubscriptionMonitoringSubscriptionRealtimeMetricsSubscriptionConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudfrontMonitoringSubscriptionMonitoringSubscriptionRealtimeMetricsSubscriptionConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf8a48c5d13364cd057557d0b46dd82edf10ade46548eda4bd289b87fd8a0c58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CloudfrontMonitoringSubscription",
    "CloudfrontMonitoringSubscriptionConfig",
    "CloudfrontMonitoringSubscriptionMonitoringSubscription",
    "CloudfrontMonitoringSubscriptionMonitoringSubscriptionOutputReference",
    "CloudfrontMonitoringSubscriptionMonitoringSubscriptionRealtimeMetricsSubscriptionConfig",
    "CloudfrontMonitoringSubscriptionMonitoringSubscriptionRealtimeMetricsSubscriptionConfigOutputReference",
]

publication.publish()

def _typecheckingstub__6d7c451eec309ee7bf13d6fd8eb47753a1190258aca539ee1f2d44648e48f173(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    distribution_id: builtins.str,
    monitoring_subscription: typing.Union[CloudfrontMonitoringSubscriptionMonitoringSubscription, typing.Dict[builtins.str, typing.Any]],
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

def _typecheckingstub__4a1d7a450ca8897ef03fd271bcc63cc2fedcea3b8149f9aa03aaa210b077fe9e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccbe5b84fa919e1aac8f8bed01d5875516bd2f282a1a409e939784f0b9ca784c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acfb4c0f9abc04392e437f115025b6e31f8d9c4035c087fe25495406aa0575a8(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    distribution_id: builtins.str,
    monitoring_subscription: typing.Union[CloudfrontMonitoringSubscriptionMonitoringSubscription, typing.Dict[builtins.str, typing.Any]],
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd2a2533e19c4e7a8b58e80a3cfeee57fc2c91c747c7932016e8af6217049163(
    *,
    realtime_metrics_subscription_config: typing.Union[CloudfrontMonitoringSubscriptionMonitoringSubscriptionRealtimeMetricsSubscriptionConfig, typing.Dict[builtins.str, typing.Any]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df26c7563415717319fc62dbc7dc92e56ee14b649b3d167228a061ed23b065f6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31df6e16bb5c8480d18262f46be2b8f21303faad06447f4bd87c2d043a034cb5(
    value: typing.Optional[CloudfrontMonitoringSubscriptionMonitoringSubscription],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__375a23c138d5f5f70ff2b9e64386e95d431f9cdc86db0a20c881bafccc01ccdd(
    *,
    realtime_metrics_subscription_status: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45e00d6abc04f0384936911f3aa8bb70d33918413b518897448eb6cae1988ce7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35e0c54eab4ab9f8c6660744e1da35ba7fdc1e7f8b0bc02414691bea3c958da8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf8a48c5d13364cd057557d0b46dd82edf10ade46548eda4bd289b87fd8a0c58(
    value: typing.Optional[CloudfrontMonitoringSubscriptionMonitoringSubscriptionRealtimeMetricsSubscriptionConfig],
) -> None:
    """Type checking stubs"""
    pass
