'''
# `aws_ses_configuration_set`

Refer to the Terraform Registory for docs: [`aws_ses_configuration_set`](https://www.terraform.io/docs/providers/aws/r/ses_configuration_set).
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


class SesConfigurationSet(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sesConfigurationSet.SesConfigurationSet",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/ses_configuration_set aws_ses_configuration_set}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        delivery_options: typing.Optional[typing.Union["SesConfigurationSetDeliveryOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        reputation_metrics_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        sending_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tracking_options: typing.Optional[typing.Union["SesConfigurationSetTrackingOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/ses_configuration_set aws_ses_configuration_set} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ses_configuration_set#name SesConfigurationSet#name}.
        :param delivery_options: delivery_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ses_configuration_set#delivery_options SesConfigurationSet#delivery_options}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ses_configuration_set#id SesConfigurationSet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param reputation_metrics_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ses_configuration_set#reputation_metrics_enabled SesConfigurationSet#reputation_metrics_enabled}.
        :param sending_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ses_configuration_set#sending_enabled SesConfigurationSet#sending_enabled}.
        :param tracking_options: tracking_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ses_configuration_set#tracking_options SesConfigurationSet#tracking_options}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__376dfa38d1f493cab87bdca5f9c54dcb5c839235cf2d3427b5caff8004ad856e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SesConfigurationSetConfig(
            name=name,
            delivery_options=delivery_options,
            id=id,
            reputation_metrics_enabled=reputation_metrics_enabled,
            sending_enabled=sending_enabled,
            tracking_options=tracking_options,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putDeliveryOptions")
    def put_delivery_options(
        self,
        *,
        tls_policy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param tls_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ses_configuration_set#tls_policy SesConfigurationSet#tls_policy}.
        '''
        value = SesConfigurationSetDeliveryOptions(tls_policy=tls_policy)

        return typing.cast(None, jsii.invoke(self, "putDeliveryOptions", [value]))

    @jsii.member(jsii_name="putTrackingOptions")
    def put_tracking_options(
        self,
        *,
        custom_redirect_domain: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param custom_redirect_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ses_configuration_set#custom_redirect_domain SesConfigurationSet#custom_redirect_domain}.
        '''
        value = SesConfigurationSetTrackingOptions(
            custom_redirect_domain=custom_redirect_domain
        )

        return typing.cast(None, jsii.invoke(self, "putTrackingOptions", [value]))

    @jsii.member(jsii_name="resetDeliveryOptions")
    def reset_delivery_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeliveryOptions", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetReputationMetricsEnabled")
    def reset_reputation_metrics_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReputationMetricsEnabled", []))

    @jsii.member(jsii_name="resetSendingEnabled")
    def reset_sending_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSendingEnabled", []))

    @jsii.member(jsii_name="resetTrackingOptions")
    def reset_tracking_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrackingOptions", []))

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
    @jsii.member(jsii_name="deliveryOptions")
    def delivery_options(self) -> "SesConfigurationSetDeliveryOptionsOutputReference":
        return typing.cast("SesConfigurationSetDeliveryOptionsOutputReference", jsii.get(self, "deliveryOptions"))

    @builtins.property
    @jsii.member(jsii_name="lastFreshStart")
    def last_fresh_start(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastFreshStart"))

    @builtins.property
    @jsii.member(jsii_name="trackingOptions")
    def tracking_options(self) -> "SesConfigurationSetTrackingOptionsOutputReference":
        return typing.cast("SesConfigurationSetTrackingOptionsOutputReference", jsii.get(self, "trackingOptions"))

    @builtins.property
    @jsii.member(jsii_name="deliveryOptionsInput")
    def delivery_options_input(
        self,
    ) -> typing.Optional["SesConfigurationSetDeliveryOptions"]:
        return typing.cast(typing.Optional["SesConfigurationSetDeliveryOptions"], jsii.get(self, "deliveryOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="reputationMetricsEnabledInput")
    def reputation_metrics_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "reputationMetricsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="sendingEnabledInput")
    def sending_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "sendingEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="trackingOptionsInput")
    def tracking_options_input(
        self,
    ) -> typing.Optional["SesConfigurationSetTrackingOptions"]:
        return typing.cast(typing.Optional["SesConfigurationSetTrackingOptions"], jsii.get(self, "trackingOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0ea0c5f8cf42be850f373423286b800632dcb3c694ec1a7466ad3d84d12e55c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e385349156b32c077dc356718929b3b880423de94b6a23cbc939d8217dc597a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="reputationMetricsEnabled")
    def reputation_metrics_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "reputationMetricsEnabled"))

    @reputation_metrics_enabled.setter
    def reputation_metrics_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32518b91aba476e109d289a9eaff660205e05fd19cfe153363da6e8b67c0f4e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reputationMetricsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="sendingEnabled")
    def sending_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "sendingEnabled"))

    @sending_enabled.setter
    def sending_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb25a19dfad30e32cf6ea22e9d839b3d735f7eab7df4ae416641dfcd1e74eb70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sendingEnabled", value)


@jsii.data_type(
    jsii_type="aws.sesConfigurationSet.SesConfigurationSetConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "delivery_options": "deliveryOptions",
        "id": "id",
        "reputation_metrics_enabled": "reputationMetricsEnabled",
        "sending_enabled": "sendingEnabled",
        "tracking_options": "trackingOptions",
    },
)
class SesConfigurationSetConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        name: builtins.str,
        delivery_options: typing.Optional[typing.Union["SesConfigurationSetDeliveryOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        reputation_metrics_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        sending_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tracking_options: typing.Optional[typing.Union["SesConfigurationSetTrackingOptions", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ses_configuration_set#name SesConfigurationSet#name}.
        :param delivery_options: delivery_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ses_configuration_set#delivery_options SesConfigurationSet#delivery_options}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ses_configuration_set#id SesConfigurationSet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param reputation_metrics_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ses_configuration_set#reputation_metrics_enabled SesConfigurationSet#reputation_metrics_enabled}.
        :param sending_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ses_configuration_set#sending_enabled SesConfigurationSet#sending_enabled}.
        :param tracking_options: tracking_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ses_configuration_set#tracking_options SesConfigurationSet#tracking_options}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(delivery_options, dict):
            delivery_options = SesConfigurationSetDeliveryOptions(**delivery_options)
        if isinstance(tracking_options, dict):
            tracking_options = SesConfigurationSetTrackingOptions(**tracking_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cc09f48d7a6e7578635e84fb3532ad0947927da007fcbe3b8e0db63a5071828)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument delivery_options", value=delivery_options, expected_type=type_hints["delivery_options"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument reputation_metrics_enabled", value=reputation_metrics_enabled, expected_type=type_hints["reputation_metrics_enabled"])
            check_type(argname="argument sending_enabled", value=sending_enabled, expected_type=type_hints["sending_enabled"])
            check_type(argname="argument tracking_options", value=tracking_options, expected_type=type_hints["tracking_options"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
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
        if delivery_options is not None:
            self._values["delivery_options"] = delivery_options
        if id is not None:
            self._values["id"] = id
        if reputation_metrics_enabled is not None:
            self._values["reputation_metrics_enabled"] = reputation_metrics_enabled
        if sending_enabled is not None:
            self._values["sending_enabled"] = sending_enabled
        if tracking_options is not None:
            self._values["tracking_options"] = tracking_options

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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ses_configuration_set#name SesConfigurationSet#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def delivery_options(self) -> typing.Optional["SesConfigurationSetDeliveryOptions"]:
        '''delivery_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ses_configuration_set#delivery_options SesConfigurationSet#delivery_options}
        '''
        result = self._values.get("delivery_options")
        return typing.cast(typing.Optional["SesConfigurationSetDeliveryOptions"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ses_configuration_set#id SesConfigurationSet#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def reputation_metrics_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ses_configuration_set#reputation_metrics_enabled SesConfigurationSet#reputation_metrics_enabled}.'''
        result = self._values.get("reputation_metrics_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def sending_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ses_configuration_set#sending_enabled SesConfigurationSet#sending_enabled}.'''
        result = self._values.get("sending_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def tracking_options(self) -> typing.Optional["SesConfigurationSetTrackingOptions"]:
        '''tracking_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ses_configuration_set#tracking_options SesConfigurationSet#tracking_options}
        '''
        result = self._values.get("tracking_options")
        return typing.cast(typing.Optional["SesConfigurationSetTrackingOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SesConfigurationSetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sesConfigurationSet.SesConfigurationSetDeliveryOptions",
    jsii_struct_bases=[],
    name_mapping={"tls_policy": "tlsPolicy"},
)
class SesConfigurationSetDeliveryOptions:
    def __init__(self, *, tls_policy: typing.Optional[builtins.str] = None) -> None:
        '''
        :param tls_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ses_configuration_set#tls_policy SesConfigurationSet#tls_policy}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a30dd9e2b0973905d1ea77763b1d47249a65a372673d827d6a3066038c984ac)
            check_type(argname="argument tls_policy", value=tls_policy, expected_type=type_hints["tls_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if tls_policy is not None:
            self._values["tls_policy"] = tls_policy

    @builtins.property
    def tls_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ses_configuration_set#tls_policy SesConfigurationSet#tls_policy}.'''
        result = self._values.get("tls_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SesConfigurationSetDeliveryOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SesConfigurationSetDeliveryOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sesConfigurationSet.SesConfigurationSetDeliveryOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__47fa960baf01650e1852d4a277db2e95c3ff240311451e2435afc9d000c45422)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetTlsPolicy")
    def reset_tls_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsPolicy", []))

    @builtins.property
    @jsii.member(jsii_name="tlsPolicyInput")
    def tls_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tlsPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsPolicy")
    def tls_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsPolicy"))

    @tls_policy.setter
    def tls_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0512a07d7e9a6d118d3c0851a5d1706c9c32247da30abee7e46c0cd6426de38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SesConfigurationSetDeliveryOptions]:
        return typing.cast(typing.Optional[SesConfigurationSetDeliveryOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SesConfigurationSetDeliveryOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a684e10a7ab948ae0bd30f373b2b8e2494513077fe1347080a9e13248ca88bb3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.sesConfigurationSet.SesConfigurationSetTrackingOptions",
    jsii_struct_bases=[],
    name_mapping={"custom_redirect_domain": "customRedirectDomain"},
)
class SesConfigurationSetTrackingOptions:
    def __init__(
        self,
        *,
        custom_redirect_domain: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param custom_redirect_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ses_configuration_set#custom_redirect_domain SesConfigurationSet#custom_redirect_domain}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b896cc72d82304c415b4e515c86c5149d74f90c5600d54cac09ab27f025adca3)
            check_type(argname="argument custom_redirect_domain", value=custom_redirect_domain, expected_type=type_hints["custom_redirect_domain"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if custom_redirect_domain is not None:
            self._values["custom_redirect_domain"] = custom_redirect_domain

    @builtins.property
    def custom_redirect_domain(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/ses_configuration_set#custom_redirect_domain SesConfigurationSet#custom_redirect_domain}.'''
        result = self._values.get("custom_redirect_domain")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SesConfigurationSetTrackingOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SesConfigurationSetTrackingOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sesConfigurationSet.SesConfigurationSetTrackingOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9a05c4ccf12607360b3604d5b74699c3fa1a68a951b56bcbbc6ed25feb1b0601)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCustomRedirectDomain")
    def reset_custom_redirect_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomRedirectDomain", []))

    @builtins.property
    @jsii.member(jsii_name="customRedirectDomainInput")
    def custom_redirect_domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customRedirectDomainInput"))

    @builtins.property
    @jsii.member(jsii_name="customRedirectDomain")
    def custom_redirect_domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customRedirectDomain"))

    @custom_redirect_domain.setter
    def custom_redirect_domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d490a3a4fe2e027afae862a271fa0a80d7bc44072d14747b0062ba82dbb9dc4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customRedirectDomain", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SesConfigurationSetTrackingOptions]:
        return typing.cast(typing.Optional[SesConfigurationSetTrackingOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SesConfigurationSetTrackingOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7cd385d66405638ede24de8d01e0ccb0e45e4c8411d406b76b01c604555cfebc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SesConfigurationSet",
    "SesConfigurationSetConfig",
    "SesConfigurationSetDeliveryOptions",
    "SesConfigurationSetDeliveryOptionsOutputReference",
    "SesConfigurationSetTrackingOptions",
    "SesConfigurationSetTrackingOptionsOutputReference",
]

publication.publish()

def _typecheckingstub__376dfa38d1f493cab87bdca5f9c54dcb5c839235cf2d3427b5caff8004ad856e(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    delivery_options: typing.Optional[typing.Union[SesConfigurationSetDeliveryOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    reputation_metrics_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    sending_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tracking_options: typing.Optional[typing.Union[SesConfigurationSetTrackingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__a0ea0c5f8cf42be850f373423286b800632dcb3c694ec1a7466ad3d84d12e55c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e385349156b32c077dc356718929b3b880423de94b6a23cbc939d8217dc597a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32518b91aba476e109d289a9eaff660205e05fd19cfe153363da6e8b67c0f4e4(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb25a19dfad30e32cf6ea22e9d839b3d735f7eab7df4ae416641dfcd1e74eb70(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cc09f48d7a6e7578635e84fb3532ad0947927da007fcbe3b8e0db63a5071828(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    delivery_options: typing.Optional[typing.Union[SesConfigurationSetDeliveryOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    reputation_metrics_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    sending_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tracking_options: typing.Optional[typing.Union[SesConfigurationSetTrackingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a30dd9e2b0973905d1ea77763b1d47249a65a372673d827d6a3066038c984ac(
    *,
    tls_policy: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47fa960baf01650e1852d4a277db2e95c3ff240311451e2435afc9d000c45422(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0512a07d7e9a6d118d3c0851a5d1706c9c32247da30abee7e46c0cd6426de38(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a684e10a7ab948ae0bd30f373b2b8e2494513077fe1347080a9e13248ca88bb3(
    value: typing.Optional[SesConfigurationSetDeliveryOptions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b896cc72d82304c415b4e515c86c5149d74f90c5600d54cac09ab27f025adca3(
    *,
    custom_redirect_domain: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a05c4ccf12607360b3604d5b74699c3fa1a68a951b56bcbbc6ed25feb1b0601(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d490a3a4fe2e027afae862a271fa0a80d7bc44072d14747b0062ba82dbb9dc4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cd385d66405638ede24de8d01e0ccb0e45e4c8411d406b76b01c604555cfebc(
    value: typing.Optional[SesConfigurationSetTrackingOptions],
) -> None:
    """Type checking stubs"""
    pass
