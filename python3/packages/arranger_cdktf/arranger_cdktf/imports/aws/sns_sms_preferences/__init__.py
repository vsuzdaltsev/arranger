'''
# `aws_sns_sms_preferences`

Refer to the Terraform Registory for docs: [`aws_sns_sms_preferences`](https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences).
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


class SnsSmsPreferences(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.snsSmsPreferences.SnsSmsPreferences",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences aws_sns_sms_preferences}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        default_sender_id: typing.Optional[builtins.str] = None,
        default_sms_type: typing.Optional[builtins.str] = None,
        delivery_status_iam_role_arn: typing.Optional[builtins.str] = None,
        delivery_status_success_sampling_rate: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        monthly_spend_limit: typing.Optional[jsii.Number] = None,
        usage_report_s3_bucket: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences aws_sns_sms_preferences} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param default_sender_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#default_sender_id SnsSmsPreferences#default_sender_id}.
        :param default_sms_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#default_sms_type SnsSmsPreferences#default_sms_type}.
        :param delivery_status_iam_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#delivery_status_iam_role_arn SnsSmsPreferences#delivery_status_iam_role_arn}.
        :param delivery_status_success_sampling_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#delivery_status_success_sampling_rate SnsSmsPreferences#delivery_status_success_sampling_rate}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#id SnsSmsPreferences#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param monthly_spend_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#monthly_spend_limit SnsSmsPreferences#monthly_spend_limit}.
        :param usage_report_s3_bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#usage_report_s3_bucket SnsSmsPreferences#usage_report_s3_bucket}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__608809910f61d8af4681efa2ba4eb485a5bce954dab7ef795122db451893b04e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SnsSmsPreferencesConfig(
            default_sender_id=default_sender_id,
            default_sms_type=default_sms_type,
            delivery_status_iam_role_arn=delivery_status_iam_role_arn,
            delivery_status_success_sampling_rate=delivery_status_success_sampling_rate,
            id=id,
            monthly_spend_limit=monthly_spend_limit,
            usage_report_s3_bucket=usage_report_s3_bucket,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetDefaultSenderId")
    def reset_default_sender_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultSenderId", []))

    @jsii.member(jsii_name="resetDefaultSmsType")
    def reset_default_sms_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultSmsType", []))

    @jsii.member(jsii_name="resetDeliveryStatusIamRoleArn")
    def reset_delivery_status_iam_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeliveryStatusIamRoleArn", []))

    @jsii.member(jsii_name="resetDeliveryStatusSuccessSamplingRate")
    def reset_delivery_status_success_sampling_rate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeliveryStatusSuccessSamplingRate", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMonthlySpendLimit")
    def reset_monthly_spend_limit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonthlySpendLimit", []))

    @jsii.member(jsii_name="resetUsageReportS3Bucket")
    def reset_usage_report_s3_bucket(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsageReportS3Bucket", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="defaultSenderIdInput")
    def default_sender_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultSenderIdInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultSmsTypeInput")
    def default_sms_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultSmsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="deliveryStatusIamRoleArnInput")
    def delivery_status_iam_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deliveryStatusIamRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="deliveryStatusSuccessSamplingRateInput")
    def delivery_status_success_sampling_rate_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deliveryStatusSuccessSamplingRateInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="monthlySpendLimitInput")
    def monthly_spend_limit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "monthlySpendLimitInput"))

    @builtins.property
    @jsii.member(jsii_name="usageReportS3BucketInput")
    def usage_report_s3_bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usageReportS3BucketInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultSenderId")
    def default_sender_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultSenderId"))

    @default_sender_id.setter
    def default_sender_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__869314b63d835950890cc2544bf4281e3db96b7edccae634bb9553409b7f2d0e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultSenderId", value)

    @builtins.property
    @jsii.member(jsii_name="defaultSmsType")
    def default_sms_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultSmsType"))

    @default_sms_type.setter
    def default_sms_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba1ea8ebcbef8cd68fd6c11b08a4c1c9b68e3aee2b976b0847da66da7c11ccde)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultSmsType", value)

    @builtins.property
    @jsii.member(jsii_name="deliveryStatusIamRoleArn")
    def delivery_status_iam_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deliveryStatusIamRoleArn"))

    @delivery_status_iam_role_arn.setter
    def delivery_status_iam_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2889e90473e7d004b9dce2ff30105eb8e1ebf0e7c19344e5cfc584962cddf1e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryStatusIamRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="deliveryStatusSuccessSamplingRate")
    def delivery_status_success_sampling_rate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deliveryStatusSuccessSamplingRate"))

    @delivery_status_success_sampling_rate.setter
    def delivery_status_success_sampling_rate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8af100eb6443afed155d38bfe17bd359c2eddc800231f34c8fa9f0f1c02a3cc4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryStatusSuccessSamplingRate", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe02f336b1fb4a54bbcc7fd1cda57b106e9931cc6df2be2393eca3872807de2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="monthlySpendLimit")
    def monthly_spend_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "monthlySpendLimit"))

    @monthly_spend_limit.setter
    def monthly_spend_limit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f06cfa55892c682c88e65ce46b723e826ec587faed750dae6d2f78c8797a3eef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monthlySpendLimit", value)

    @builtins.property
    @jsii.member(jsii_name="usageReportS3Bucket")
    def usage_report_s3_bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usageReportS3Bucket"))

    @usage_report_s3_bucket.setter
    def usage_report_s3_bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfb21c12e21c9a64870a1f69625ac708c5be605cd7119846e83f4569f99d21bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usageReportS3Bucket", value)


@jsii.data_type(
    jsii_type="aws.snsSmsPreferences.SnsSmsPreferencesConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "default_sender_id": "defaultSenderId",
        "default_sms_type": "defaultSmsType",
        "delivery_status_iam_role_arn": "deliveryStatusIamRoleArn",
        "delivery_status_success_sampling_rate": "deliveryStatusSuccessSamplingRate",
        "id": "id",
        "monthly_spend_limit": "monthlySpendLimit",
        "usage_report_s3_bucket": "usageReportS3Bucket",
    },
)
class SnsSmsPreferencesConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        default_sender_id: typing.Optional[builtins.str] = None,
        default_sms_type: typing.Optional[builtins.str] = None,
        delivery_status_iam_role_arn: typing.Optional[builtins.str] = None,
        delivery_status_success_sampling_rate: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        monthly_spend_limit: typing.Optional[jsii.Number] = None,
        usage_report_s3_bucket: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param default_sender_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#default_sender_id SnsSmsPreferences#default_sender_id}.
        :param default_sms_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#default_sms_type SnsSmsPreferences#default_sms_type}.
        :param delivery_status_iam_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#delivery_status_iam_role_arn SnsSmsPreferences#delivery_status_iam_role_arn}.
        :param delivery_status_success_sampling_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#delivery_status_success_sampling_rate SnsSmsPreferences#delivery_status_success_sampling_rate}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#id SnsSmsPreferences#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param monthly_spend_limit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#monthly_spend_limit SnsSmsPreferences#monthly_spend_limit}.
        :param usage_report_s3_bucket: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#usage_report_s3_bucket SnsSmsPreferences#usage_report_s3_bucket}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5635befaff3a85e266ef2f349511effd410f38f117293d6945287170b221cb1)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument default_sender_id", value=default_sender_id, expected_type=type_hints["default_sender_id"])
            check_type(argname="argument default_sms_type", value=default_sms_type, expected_type=type_hints["default_sms_type"])
            check_type(argname="argument delivery_status_iam_role_arn", value=delivery_status_iam_role_arn, expected_type=type_hints["delivery_status_iam_role_arn"])
            check_type(argname="argument delivery_status_success_sampling_rate", value=delivery_status_success_sampling_rate, expected_type=type_hints["delivery_status_success_sampling_rate"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument monthly_spend_limit", value=monthly_spend_limit, expected_type=type_hints["monthly_spend_limit"])
            check_type(argname="argument usage_report_s3_bucket", value=usage_report_s3_bucket, expected_type=type_hints["usage_report_s3_bucket"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
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
        if default_sender_id is not None:
            self._values["default_sender_id"] = default_sender_id
        if default_sms_type is not None:
            self._values["default_sms_type"] = default_sms_type
        if delivery_status_iam_role_arn is not None:
            self._values["delivery_status_iam_role_arn"] = delivery_status_iam_role_arn
        if delivery_status_success_sampling_rate is not None:
            self._values["delivery_status_success_sampling_rate"] = delivery_status_success_sampling_rate
        if id is not None:
            self._values["id"] = id
        if monthly_spend_limit is not None:
            self._values["monthly_spend_limit"] = monthly_spend_limit
        if usage_report_s3_bucket is not None:
            self._values["usage_report_s3_bucket"] = usage_report_s3_bucket

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
    def default_sender_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#default_sender_id SnsSmsPreferences#default_sender_id}.'''
        result = self._values.get("default_sender_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_sms_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#default_sms_type SnsSmsPreferences#default_sms_type}.'''
        result = self._values.get("default_sms_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delivery_status_iam_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#delivery_status_iam_role_arn SnsSmsPreferences#delivery_status_iam_role_arn}.'''
        result = self._values.get("delivery_status_iam_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delivery_status_success_sampling_rate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#delivery_status_success_sampling_rate SnsSmsPreferences#delivery_status_success_sampling_rate}.'''
        result = self._values.get("delivery_status_success_sampling_rate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#id SnsSmsPreferences#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def monthly_spend_limit(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#monthly_spend_limit SnsSmsPreferences#monthly_spend_limit}.'''
        result = self._values.get("monthly_spend_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def usage_report_s3_bucket(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_sms_preferences#usage_report_s3_bucket SnsSmsPreferences#usage_report_s3_bucket}.'''
        result = self._values.get("usage_report_s3_bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SnsSmsPreferencesConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "SnsSmsPreferences",
    "SnsSmsPreferencesConfig",
]

publication.publish()

def _typecheckingstub__608809910f61d8af4681efa2ba4eb485a5bce954dab7ef795122db451893b04e(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    default_sender_id: typing.Optional[builtins.str] = None,
    default_sms_type: typing.Optional[builtins.str] = None,
    delivery_status_iam_role_arn: typing.Optional[builtins.str] = None,
    delivery_status_success_sampling_rate: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    monthly_spend_limit: typing.Optional[jsii.Number] = None,
    usage_report_s3_bucket: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__869314b63d835950890cc2544bf4281e3db96b7edccae634bb9553409b7f2d0e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba1ea8ebcbef8cd68fd6c11b08a4c1c9b68e3aee2b976b0847da66da7c11ccde(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2889e90473e7d004b9dce2ff30105eb8e1ebf0e7c19344e5cfc584962cddf1e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8af100eb6443afed155d38bfe17bd359c2eddc800231f34c8fa9f0f1c02a3cc4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe02f336b1fb4a54bbcc7fd1cda57b106e9931cc6df2be2393eca3872807de2b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f06cfa55892c682c88e65ce46b723e826ec587faed750dae6d2f78c8797a3eef(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfb21c12e21c9a64870a1f69625ac708c5be605cd7119846e83f4569f99d21bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5635befaff3a85e266ef2f349511effd410f38f117293d6945287170b221cb1(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    default_sender_id: typing.Optional[builtins.str] = None,
    default_sms_type: typing.Optional[builtins.str] = None,
    delivery_status_iam_role_arn: typing.Optional[builtins.str] = None,
    delivery_status_success_sampling_rate: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    monthly_spend_limit: typing.Optional[jsii.Number] = None,
    usage_report_s3_bucket: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
