'''
# `aws_sns_platform_application`

Refer to the Terraform Registory for docs: [`aws_sns_platform_application`](https://www.terraform.io/docs/providers/aws/r/sns_platform_application).
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


class SnsPlatformApplication(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.snsPlatformApplication.SnsPlatformApplication",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application aws_sns_platform_application}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        platform: builtins.str,
        platform_credential: builtins.str,
        apple_platform_bundle_id: typing.Optional[builtins.str] = None,
        apple_platform_team_id: typing.Optional[builtins.str] = None,
        event_delivery_failure_topic_arn: typing.Optional[builtins.str] = None,
        event_endpoint_created_topic_arn: typing.Optional[builtins.str] = None,
        event_endpoint_deleted_topic_arn: typing.Optional[builtins.str] = None,
        event_endpoint_updated_topic_arn: typing.Optional[builtins.str] = None,
        failure_feedback_role_arn: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        platform_principal: typing.Optional[builtins.str] = None,
        success_feedback_role_arn: typing.Optional[builtins.str] = None,
        success_feedback_sample_rate: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application aws_sns_platform_application} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#name SnsPlatformApplication#name}.
        :param platform: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#platform SnsPlatformApplication#platform}.
        :param platform_credential: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#platform_credential SnsPlatformApplication#platform_credential}.
        :param apple_platform_bundle_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#apple_platform_bundle_id SnsPlatformApplication#apple_platform_bundle_id}.
        :param apple_platform_team_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#apple_platform_team_id SnsPlatformApplication#apple_platform_team_id}.
        :param event_delivery_failure_topic_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#event_delivery_failure_topic_arn SnsPlatformApplication#event_delivery_failure_topic_arn}.
        :param event_endpoint_created_topic_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#event_endpoint_created_topic_arn SnsPlatformApplication#event_endpoint_created_topic_arn}.
        :param event_endpoint_deleted_topic_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#event_endpoint_deleted_topic_arn SnsPlatformApplication#event_endpoint_deleted_topic_arn}.
        :param event_endpoint_updated_topic_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#event_endpoint_updated_topic_arn SnsPlatformApplication#event_endpoint_updated_topic_arn}.
        :param failure_feedback_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#failure_feedback_role_arn SnsPlatformApplication#failure_feedback_role_arn}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#id SnsPlatformApplication#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param platform_principal: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#platform_principal SnsPlatformApplication#platform_principal}.
        :param success_feedback_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#success_feedback_role_arn SnsPlatformApplication#success_feedback_role_arn}.
        :param success_feedback_sample_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#success_feedback_sample_rate SnsPlatformApplication#success_feedback_sample_rate}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a34c9d58d94498c042e508cd680b688c1b8bca9ffbdea0f4392b9a71dfaca1e7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SnsPlatformApplicationConfig(
            name=name,
            platform=platform,
            platform_credential=platform_credential,
            apple_platform_bundle_id=apple_platform_bundle_id,
            apple_platform_team_id=apple_platform_team_id,
            event_delivery_failure_topic_arn=event_delivery_failure_topic_arn,
            event_endpoint_created_topic_arn=event_endpoint_created_topic_arn,
            event_endpoint_deleted_topic_arn=event_endpoint_deleted_topic_arn,
            event_endpoint_updated_topic_arn=event_endpoint_updated_topic_arn,
            failure_feedback_role_arn=failure_feedback_role_arn,
            id=id,
            platform_principal=platform_principal,
            success_feedback_role_arn=success_feedback_role_arn,
            success_feedback_sample_rate=success_feedback_sample_rate,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetApplePlatformBundleId")
    def reset_apple_platform_bundle_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplePlatformBundleId", []))

    @jsii.member(jsii_name="resetApplePlatformTeamId")
    def reset_apple_platform_team_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplePlatformTeamId", []))

    @jsii.member(jsii_name="resetEventDeliveryFailureTopicArn")
    def reset_event_delivery_failure_topic_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventDeliveryFailureTopicArn", []))

    @jsii.member(jsii_name="resetEventEndpointCreatedTopicArn")
    def reset_event_endpoint_created_topic_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventEndpointCreatedTopicArn", []))

    @jsii.member(jsii_name="resetEventEndpointDeletedTopicArn")
    def reset_event_endpoint_deleted_topic_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventEndpointDeletedTopicArn", []))

    @jsii.member(jsii_name="resetEventEndpointUpdatedTopicArn")
    def reset_event_endpoint_updated_topic_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventEndpointUpdatedTopicArn", []))

    @jsii.member(jsii_name="resetFailureFeedbackRoleArn")
    def reset_failure_feedback_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailureFeedbackRoleArn", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPlatformPrincipal")
    def reset_platform_principal(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlatformPrincipal", []))

    @jsii.member(jsii_name="resetSuccessFeedbackRoleArn")
    def reset_success_feedback_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuccessFeedbackRoleArn", []))

    @jsii.member(jsii_name="resetSuccessFeedbackSampleRate")
    def reset_success_feedback_sample_rate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuccessFeedbackSampleRate", []))

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
    @jsii.member(jsii_name="applePlatformBundleIdInput")
    def apple_platform_bundle_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applePlatformBundleIdInput"))

    @builtins.property
    @jsii.member(jsii_name="applePlatformTeamIdInput")
    def apple_platform_team_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applePlatformTeamIdInput"))

    @builtins.property
    @jsii.member(jsii_name="eventDeliveryFailureTopicArnInput")
    def event_delivery_failure_topic_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventDeliveryFailureTopicArnInput"))

    @builtins.property
    @jsii.member(jsii_name="eventEndpointCreatedTopicArnInput")
    def event_endpoint_created_topic_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventEndpointCreatedTopicArnInput"))

    @builtins.property
    @jsii.member(jsii_name="eventEndpointDeletedTopicArnInput")
    def event_endpoint_deleted_topic_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventEndpointDeletedTopicArnInput"))

    @builtins.property
    @jsii.member(jsii_name="eventEndpointUpdatedTopicArnInput")
    def event_endpoint_updated_topic_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventEndpointUpdatedTopicArnInput"))

    @builtins.property
    @jsii.member(jsii_name="failureFeedbackRoleArnInput")
    def failure_feedback_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "failureFeedbackRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="platformCredentialInput")
    def platform_credential_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "platformCredentialInput"))

    @builtins.property
    @jsii.member(jsii_name="platformInput")
    def platform_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "platformInput"))

    @builtins.property
    @jsii.member(jsii_name="platformPrincipalInput")
    def platform_principal_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "platformPrincipalInput"))

    @builtins.property
    @jsii.member(jsii_name="successFeedbackRoleArnInput")
    def success_feedback_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "successFeedbackRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="successFeedbackSampleRateInput")
    def success_feedback_sample_rate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "successFeedbackSampleRateInput"))

    @builtins.property
    @jsii.member(jsii_name="applePlatformBundleId")
    def apple_platform_bundle_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applePlatformBundleId"))

    @apple_platform_bundle_id.setter
    def apple_platform_bundle_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__149c943c378897fa4a9694c168d5cdeb87829a7cebd2fad0004639f4c73af565)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applePlatformBundleId", value)

    @builtins.property
    @jsii.member(jsii_name="applePlatformTeamId")
    def apple_platform_team_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applePlatformTeamId"))

    @apple_platform_team_id.setter
    def apple_platform_team_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b93d4d3440ac8de4bee076fac6e64a9da143de29152c183863c08c0fb10327c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applePlatformTeamId", value)

    @builtins.property
    @jsii.member(jsii_name="eventDeliveryFailureTopicArn")
    def event_delivery_failure_topic_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventDeliveryFailureTopicArn"))

    @event_delivery_failure_topic_arn.setter
    def event_delivery_failure_topic_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc5f583efaf070e75a69cd2b8a3205e6975ad3f0b2624fbdc3c31bf18a113149)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventDeliveryFailureTopicArn", value)

    @builtins.property
    @jsii.member(jsii_name="eventEndpointCreatedTopicArn")
    def event_endpoint_created_topic_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventEndpointCreatedTopicArn"))

    @event_endpoint_created_topic_arn.setter
    def event_endpoint_created_topic_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c901b45d42f865b24027d5c97488370aa1498b32b5cdddc87288255071c5c7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventEndpointCreatedTopicArn", value)

    @builtins.property
    @jsii.member(jsii_name="eventEndpointDeletedTopicArn")
    def event_endpoint_deleted_topic_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventEndpointDeletedTopicArn"))

    @event_endpoint_deleted_topic_arn.setter
    def event_endpoint_deleted_topic_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35912ebbb1c32d9c64565f1523fcc5bca5e9085fbe1650cb67c56aabe3bec8e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventEndpointDeletedTopicArn", value)

    @builtins.property
    @jsii.member(jsii_name="eventEndpointUpdatedTopicArn")
    def event_endpoint_updated_topic_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventEndpointUpdatedTopicArn"))

    @event_endpoint_updated_topic_arn.setter
    def event_endpoint_updated_topic_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ead68f8ff38acaa66102c13577147da7aefe1d0146eca3527712bf05edddcbea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventEndpointUpdatedTopicArn", value)

    @builtins.property
    @jsii.member(jsii_name="failureFeedbackRoleArn")
    def failure_feedback_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "failureFeedbackRoleArn"))

    @failure_feedback_role_arn.setter
    def failure_feedback_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e43991bcd5a67d8a7cc5c4d173e50bcb30c8496435a2f72eb066a8c31c19fff7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failureFeedbackRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65267e1b04563763f4971da577acb676083b63dce8b6f14807ffd6e3ae43dacc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66537ad4b60b9fa9a26a0907707a547330858d4eb81411c4bc75268154285bfd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="platform")
    def platform(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "platform"))

    @platform.setter
    def platform(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__009d29591e35f61d7d7f909c6260ee7690d3c22201838203a25c247c824e9fdb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "platform", value)

    @builtins.property
    @jsii.member(jsii_name="platformCredential")
    def platform_credential(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "platformCredential"))

    @platform_credential.setter
    def platform_credential(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f920a354d4f87ab87e80621bc7a452f97635815d4a9307c9db3973eaa6391c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "platformCredential", value)

    @builtins.property
    @jsii.member(jsii_name="platformPrincipal")
    def platform_principal(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "platformPrincipal"))

    @platform_principal.setter
    def platform_principal(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c571e9226c47a4dfe6a5cf316e716809df9519ccfdd947cee78c9bb54e113a39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "platformPrincipal", value)

    @builtins.property
    @jsii.member(jsii_name="successFeedbackRoleArn")
    def success_feedback_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "successFeedbackRoleArn"))

    @success_feedback_role_arn.setter
    def success_feedback_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0a76af5ec87bd5992f676d69d19dab25827cc49df5b88d17f4fcbc290f40802)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "successFeedbackRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="successFeedbackSampleRate")
    def success_feedback_sample_rate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "successFeedbackSampleRate"))

    @success_feedback_sample_rate.setter
    def success_feedback_sample_rate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d57892680182da0226c34fc2b807b48b947917b7e506d290fd7cf8a0be115ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "successFeedbackSampleRate", value)


@jsii.data_type(
    jsii_type="aws.snsPlatformApplication.SnsPlatformApplicationConfig",
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
        "platform": "platform",
        "platform_credential": "platformCredential",
        "apple_platform_bundle_id": "applePlatformBundleId",
        "apple_platform_team_id": "applePlatformTeamId",
        "event_delivery_failure_topic_arn": "eventDeliveryFailureTopicArn",
        "event_endpoint_created_topic_arn": "eventEndpointCreatedTopicArn",
        "event_endpoint_deleted_topic_arn": "eventEndpointDeletedTopicArn",
        "event_endpoint_updated_topic_arn": "eventEndpointUpdatedTopicArn",
        "failure_feedback_role_arn": "failureFeedbackRoleArn",
        "id": "id",
        "platform_principal": "platformPrincipal",
        "success_feedback_role_arn": "successFeedbackRoleArn",
        "success_feedback_sample_rate": "successFeedbackSampleRate",
    },
)
class SnsPlatformApplicationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        platform: builtins.str,
        platform_credential: builtins.str,
        apple_platform_bundle_id: typing.Optional[builtins.str] = None,
        apple_platform_team_id: typing.Optional[builtins.str] = None,
        event_delivery_failure_topic_arn: typing.Optional[builtins.str] = None,
        event_endpoint_created_topic_arn: typing.Optional[builtins.str] = None,
        event_endpoint_deleted_topic_arn: typing.Optional[builtins.str] = None,
        event_endpoint_updated_topic_arn: typing.Optional[builtins.str] = None,
        failure_feedback_role_arn: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        platform_principal: typing.Optional[builtins.str] = None,
        success_feedback_role_arn: typing.Optional[builtins.str] = None,
        success_feedback_sample_rate: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#name SnsPlatformApplication#name}.
        :param platform: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#platform SnsPlatformApplication#platform}.
        :param platform_credential: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#platform_credential SnsPlatformApplication#platform_credential}.
        :param apple_platform_bundle_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#apple_platform_bundle_id SnsPlatformApplication#apple_platform_bundle_id}.
        :param apple_platform_team_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#apple_platform_team_id SnsPlatformApplication#apple_platform_team_id}.
        :param event_delivery_failure_topic_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#event_delivery_failure_topic_arn SnsPlatformApplication#event_delivery_failure_topic_arn}.
        :param event_endpoint_created_topic_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#event_endpoint_created_topic_arn SnsPlatformApplication#event_endpoint_created_topic_arn}.
        :param event_endpoint_deleted_topic_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#event_endpoint_deleted_topic_arn SnsPlatformApplication#event_endpoint_deleted_topic_arn}.
        :param event_endpoint_updated_topic_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#event_endpoint_updated_topic_arn SnsPlatformApplication#event_endpoint_updated_topic_arn}.
        :param failure_feedback_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#failure_feedback_role_arn SnsPlatformApplication#failure_feedback_role_arn}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#id SnsPlatformApplication#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param platform_principal: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#platform_principal SnsPlatformApplication#platform_principal}.
        :param success_feedback_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#success_feedback_role_arn SnsPlatformApplication#success_feedback_role_arn}.
        :param success_feedback_sample_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#success_feedback_sample_rate SnsPlatformApplication#success_feedback_sample_rate}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e94879ec9d3bc4f558ed2c844a8e979ca5ec8629b9c62bc68e62ab1fc2c7dda)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument platform", value=platform, expected_type=type_hints["platform"])
            check_type(argname="argument platform_credential", value=platform_credential, expected_type=type_hints["platform_credential"])
            check_type(argname="argument apple_platform_bundle_id", value=apple_platform_bundle_id, expected_type=type_hints["apple_platform_bundle_id"])
            check_type(argname="argument apple_platform_team_id", value=apple_platform_team_id, expected_type=type_hints["apple_platform_team_id"])
            check_type(argname="argument event_delivery_failure_topic_arn", value=event_delivery_failure_topic_arn, expected_type=type_hints["event_delivery_failure_topic_arn"])
            check_type(argname="argument event_endpoint_created_topic_arn", value=event_endpoint_created_topic_arn, expected_type=type_hints["event_endpoint_created_topic_arn"])
            check_type(argname="argument event_endpoint_deleted_topic_arn", value=event_endpoint_deleted_topic_arn, expected_type=type_hints["event_endpoint_deleted_topic_arn"])
            check_type(argname="argument event_endpoint_updated_topic_arn", value=event_endpoint_updated_topic_arn, expected_type=type_hints["event_endpoint_updated_topic_arn"])
            check_type(argname="argument failure_feedback_role_arn", value=failure_feedback_role_arn, expected_type=type_hints["failure_feedback_role_arn"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument platform_principal", value=platform_principal, expected_type=type_hints["platform_principal"])
            check_type(argname="argument success_feedback_role_arn", value=success_feedback_role_arn, expected_type=type_hints["success_feedback_role_arn"])
            check_type(argname="argument success_feedback_sample_rate", value=success_feedback_sample_rate, expected_type=type_hints["success_feedback_sample_rate"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "platform": platform,
            "platform_credential": platform_credential,
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
        if apple_platform_bundle_id is not None:
            self._values["apple_platform_bundle_id"] = apple_platform_bundle_id
        if apple_platform_team_id is not None:
            self._values["apple_platform_team_id"] = apple_platform_team_id
        if event_delivery_failure_topic_arn is not None:
            self._values["event_delivery_failure_topic_arn"] = event_delivery_failure_topic_arn
        if event_endpoint_created_topic_arn is not None:
            self._values["event_endpoint_created_topic_arn"] = event_endpoint_created_topic_arn
        if event_endpoint_deleted_topic_arn is not None:
            self._values["event_endpoint_deleted_topic_arn"] = event_endpoint_deleted_topic_arn
        if event_endpoint_updated_topic_arn is not None:
            self._values["event_endpoint_updated_topic_arn"] = event_endpoint_updated_topic_arn
        if failure_feedback_role_arn is not None:
            self._values["failure_feedback_role_arn"] = failure_feedback_role_arn
        if id is not None:
            self._values["id"] = id
        if platform_principal is not None:
            self._values["platform_principal"] = platform_principal
        if success_feedback_role_arn is not None:
            self._values["success_feedback_role_arn"] = success_feedback_role_arn
        if success_feedback_sample_rate is not None:
            self._values["success_feedback_sample_rate"] = success_feedback_sample_rate

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#name SnsPlatformApplication#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def platform(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#platform SnsPlatformApplication#platform}.'''
        result = self._values.get("platform")
        assert result is not None, "Required property 'platform' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def platform_credential(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#platform_credential SnsPlatformApplication#platform_credential}.'''
        result = self._values.get("platform_credential")
        assert result is not None, "Required property 'platform_credential' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def apple_platform_bundle_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#apple_platform_bundle_id SnsPlatformApplication#apple_platform_bundle_id}.'''
        result = self._values.get("apple_platform_bundle_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def apple_platform_team_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#apple_platform_team_id SnsPlatformApplication#apple_platform_team_id}.'''
        result = self._values.get("apple_platform_team_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def event_delivery_failure_topic_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#event_delivery_failure_topic_arn SnsPlatformApplication#event_delivery_failure_topic_arn}.'''
        result = self._values.get("event_delivery_failure_topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def event_endpoint_created_topic_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#event_endpoint_created_topic_arn SnsPlatformApplication#event_endpoint_created_topic_arn}.'''
        result = self._values.get("event_endpoint_created_topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def event_endpoint_deleted_topic_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#event_endpoint_deleted_topic_arn SnsPlatformApplication#event_endpoint_deleted_topic_arn}.'''
        result = self._values.get("event_endpoint_deleted_topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def event_endpoint_updated_topic_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#event_endpoint_updated_topic_arn SnsPlatformApplication#event_endpoint_updated_topic_arn}.'''
        result = self._values.get("event_endpoint_updated_topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def failure_feedback_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#failure_feedback_role_arn SnsPlatformApplication#failure_feedback_role_arn}.'''
        result = self._values.get("failure_feedback_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#id SnsPlatformApplication#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def platform_principal(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#platform_principal SnsPlatformApplication#platform_principal}.'''
        result = self._values.get("platform_principal")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def success_feedback_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#success_feedback_role_arn SnsPlatformApplication#success_feedback_role_arn}.'''
        result = self._values.get("success_feedback_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def success_feedback_sample_rate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_platform_application#success_feedback_sample_rate SnsPlatformApplication#success_feedback_sample_rate}.'''
        result = self._values.get("success_feedback_sample_rate")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SnsPlatformApplicationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "SnsPlatformApplication",
    "SnsPlatformApplicationConfig",
]

publication.publish()

def _typecheckingstub__a34c9d58d94498c042e508cd680b688c1b8bca9ffbdea0f4392b9a71dfaca1e7(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    platform: builtins.str,
    platform_credential: builtins.str,
    apple_platform_bundle_id: typing.Optional[builtins.str] = None,
    apple_platform_team_id: typing.Optional[builtins.str] = None,
    event_delivery_failure_topic_arn: typing.Optional[builtins.str] = None,
    event_endpoint_created_topic_arn: typing.Optional[builtins.str] = None,
    event_endpoint_deleted_topic_arn: typing.Optional[builtins.str] = None,
    event_endpoint_updated_topic_arn: typing.Optional[builtins.str] = None,
    failure_feedback_role_arn: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    platform_principal: typing.Optional[builtins.str] = None,
    success_feedback_role_arn: typing.Optional[builtins.str] = None,
    success_feedback_sample_rate: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__149c943c378897fa4a9694c168d5cdeb87829a7cebd2fad0004639f4c73af565(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b93d4d3440ac8de4bee076fac6e64a9da143de29152c183863c08c0fb10327c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc5f583efaf070e75a69cd2b8a3205e6975ad3f0b2624fbdc3c31bf18a113149(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c901b45d42f865b24027d5c97488370aa1498b32b5cdddc87288255071c5c7d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35912ebbb1c32d9c64565f1523fcc5bca5e9085fbe1650cb67c56aabe3bec8e4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ead68f8ff38acaa66102c13577147da7aefe1d0146eca3527712bf05edddcbea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e43991bcd5a67d8a7cc5c4d173e50bcb30c8496435a2f72eb066a8c31c19fff7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65267e1b04563763f4971da577acb676083b63dce8b6f14807ffd6e3ae43dacc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66537ad4b60b9fa9a26a0907707a547330858d4eb81411c4bc75268154285bfd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__009d29591e35f61d7d7f909c6260ee7690d3c22201838203a25c247c824e9fdb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f920a354d4f87ab87e80621bc7a452f97635815d4a9307c9db3973eaa6391c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c571e9226c47a4dfe6a5cf316e716809df9519ccfdd947cee78c9bb54e113a39(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0a76af5ec87bd5992f676d69d19dab25827cc49df5b88d17f4fcbc290f40802(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d57892680182da0226c34fc2b807b48b947917b7e506d290fd7cf8a0be115ba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e94879ec9d3bc4f558ed2c844a8e979ca5ec8629b9c62bc68e62ab1fc2c7dda(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    platform: builtins.str,
    platform_credential: builtins.str,
    apple_platform_bundle_id: typing.Optional[builtins.str] = None,
    apple_platform_team_id: typing.Optional[builtins.str] = None,
    event_delivery_failure_topic_arn: typing.Optional[builtins.str] = None,
    event_endpoint_created_topic_arn: typing.Optional[builtins.str] = None,
    event_endpoint_deleted_topic_arn: typing.Optional[builtins.str] = None,
    event_endpoint_updated_topic_arn: typing.Optional[builtins.str] = None,
    failure_feedback_role_arn: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    platform_principal: typing.Optional[builtins.str] = None,
    success_feedback_role_arn: typing.Optional[builtins.str] = None,
    success_feedback_sample_rate: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
