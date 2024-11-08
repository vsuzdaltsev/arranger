'''
# `aws_sns_topic`

Refer to the Terraform Registory for docs: [`aws_sns_topic`](https://www.terraform.io/docs/providers/aws/r/sns_topic).
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


class SnsTopic(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.snsTopic.SnsTopic",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/sns_topic aws_sns_topic}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        application_failure_feedback_role_arn: typing.Optional[builtins.str] = None,
        application_success_feedback_role_arn: typing.Optional[builtins.str] = None,
        application_success_feedback_sample_rate: typing.Optional[jsii.Number] = None,
        content_based_deduplication: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        delivery_policy: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        fifo_topic: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        firehose_failure_feedback_role_arn: typing.Optional[builtins.str] = None,
        firehose_success_feedback_role_arn: typing.Optional[builtins.str] = None,
        firehose_success_feedback_sample_rate: typing.Optional[jsii.Number] = None,
        http_failure_feedback_role_arn: typing.Optional[builtins.str] = None,
        http_success_feedback_role_arn: typing.Optional[builtins.str] = None,
        http_success_feedback_sample_rate: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        kms_master_key_id: typing.Optional[builtins.str] = None,
        lambda_failure_feedback_role_arn: typing.Optional[builtins.str] = None,
        lambda_success_feedback_role_arn: typing.Optional[builtins.str] = None,
        lambda_success_feedback_sample_rate: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        policy: typing.Optional[builtins.str] = None,
        sqs_failure_feedback_role_arn: typing.Optional[builtins.str] = None,
        sqs_success_feedback_role_arn: typing.Optional[builtins.str] = None,
        sqs_success_feedback_sample_rate: typing.Optional[jsii.Number] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/sns_topic aws_sns_topic} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param application_failure_feedback_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#application_failure_feedback_role_arn SnsTopic#application_failure_feedback_role_arn}.
        :param application_success_feedback_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#application_success_feedback_role_arn SnsTopic#application_success_feedback_role_arn}.
        :param application_success_feedback_sample_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#application_success_feedback_sample_rate SnsTopic#application_success_feedback_sample_rate}.
        :param content_based_deduplication: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#content_based_deduplication SnsTopic#content_based_deduplication}.
        :param delivery_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#delivery_policy SnsTopic#delivery_policy}.
        :param display_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#display_name SnsTopic#display_name}.
        :param fifo_topic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#fifo_topic SnsTopic#fifo_topic}.
        :param firehose_failure_feedback_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#firehose_failure_feedback_role_arn SnsTopic#firehose_failure_feedback_role_arn}.
        :param firehose_success_feedback_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#firehose_success_feedback_role_arn SnsTopic#firehose_success_feedback_role_arn}.
        :param firehose_success_feedback_sample_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#firehose_success_feedback_sample_rate SnsTopic#firehose_success_feedback_sample_rate}.
        :param http_failure_feedback_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#http_failure_feedback_role_arn SnsTopic#http_failure_feedback_role_arn}.
        :param http_success_feedback_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#http_success_feedback_role_arn SnsTopic#http_success_feedback_role_arn}.
        :param http_success_feedback_sample_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#http_success_feedback_sample_rate SnsTopic#http_success_feedback_sample_rate}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#id SnsTopic#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_master_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#kms_master_key_id SnsTopic#kms_master_key_id}.
        :param lambda_failure_feedback_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#lambda_failure_feedback_role_arn SnsTopic#lambda_failure_feedback_role_arn}.
        :param lambda_success_feedback_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#lambda_success_feedback_role_arn SnsTopic#lambda_success_feedback_role_arn}.
        :param lambda_success_feedback_sample_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#lambda_success_feedback_sample_rate SnsTopic#lambda_success_feedback_sample_rate}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#name SnsTopic#name}.
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#name_prefix SnsTopic#name_prefix}.
        :param policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#policy SnsTopic#policy}.
        :param sqs_failure_feedback_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#sqs_failure_feedback_role_arn SnsTopic#sqs_failure_feedback_role_arn}.
        :param sqs_success_feedback_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#sqs_success_feedback_role_arn SnsTopic#sqs_success_feedback_role_arn}.
        :param sqs_success_feedback_sample_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#sqs_success_feedback_sample_rate SnsTopic#sqs_success_feedback_sample_rate}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#tags SnsTopic#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#tags_all SnsTopic#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bbfa52b06083b87b43c7250d9c7dba1eb7790344f793b7c08d5902ab23cc64e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SnsTopicConfig(
            application_failure_feedback_role_arn=application_failure_feedback_role_arn,
            application_success_feedback_role_arn=application_success_feedback_role_arn,
            application_success_feedback_sample_rate=application_success_feedback_sample_rate,
            content_based_deduplication=content_based_deduplication,
            delivery_policy=delivery_policy,
            display_name=display_name,
            fifo_topic=fifo_topic,
            firehose_failure_feedback_role_arn=firehose_failure_feedback_role_arn,
            firehose_success_feedback_role_arn=firehose_success_feedback_role_arn,
            firehose_success_feedback_sample_rate=firehose_success_feedback_sample_rate,
            http_failure_feedback_role_arn=http_failure_feedback_role_arn,
            http_success_feedback_role_arn=http_success_feedback_role_arn,
            http_success_feedback_sample_rate=http_success_feedback_sample_rate,
            id=id,
            kms_master_key_id=kms_master_key_id,
            lambda_failure_feedback_role_arn=lambda_failure_feedback_role_arn,
            lambda_success_feedback_role_arn=lambda_success_feedback_role_arn,
            lambda_success_feedback_sample_rate=lambda_success_feedback_sample_rate,
            name=name,
            name_prefix=name_prefix,
            policy=policy,
            sqs_failure_feedback_role_arn=sqs_failure_feedback_role_arn,
            sqs_success_feedback_role_arn=sqs_success_feedback_role_arn,
            sqs_success_feedback_sample_rate=sqs_success_feedback_sample_rate,
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

    @jsii.member(jsii_name="resetApplicationFailureFeedbackRoleArn")
    def reset_application_failure_feedback_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplicationFailureFeedbackRoleArn", []))

    @jsii.member(jsii_name="resetApplicationSuccessFeedbackRoleArn")
    def reset_application_success_feedback_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplicationSuccessFeedbackRoleArn", []))

    @jsii.member(jsii_name="resetApplicationSuccessFeedbackSampleRate")
    def reset_application_success_feedback_sample_rate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplicationSuccessFeedbackSampleRate", []))

    @jsii.member(jsii_name="resetContentBasedDeduplication")
    def reset_content_based_deduplication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentBasedDeduplication", []))

    @jsii.member(jsii_name="resetDeliveryPolicy")
    def reset_delivery_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeliveryPolicy", []))

    @jsii.member(jsii_name="resetDisplayName")
    def reset_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayName", []))

    @jsii.member(jsii_name="resetFifoTopic")
    def reset_fifo_topic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFifoTopic", []))

    @jsii.member(jsii_name="resetFirehoseFailureFeedbackRoleArn")
    def reset_firehose_failure_feedback_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirehoseFailureFeedbackRoleArn", []))

    @jsii.member(jsii_name="resetFirehoseSuccessFeedbackRoleArn")
    def reset_firehose_success_feedback_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirehoseSuccessFeedbackRoleArn", []))

    @jsii.member(jsii_name="resetFirehoseSuccessFeedbackSampleRate")
    def reset_firehose_success_feedback_sample_rate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirehoseSuccessFeedbackSampleRate", []))

    @jsii.member(jsii_name="resetHttpFailureFeedbackRoleArn")
    def reset_http_failure_feedback_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpFailureFeedbackRoleArn", []))

    @jsii.member(jsii_name="resetHttpSuccessFeedbackRoleArn")
    def reset_http_success_feedback_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpSuccessFeedbackRoleArn", []))

    @jsii.member(jsii_name="resetHttpSuccessFeedbackSampleRate")
    def reset_http_success_feedback_sample_rate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpSuccessFeedbackSampleRate", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKmsMasterKeyId")
    def reset_kms_master_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsMasterKeyId", []))

    @jsii.member(jsii_name="resetLambdaFailureFeedbackRoleArn")
    def reset_lambda_failure_feedback_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLambdaFailureFeedbackRoleArn", []))

    @jsii.member(jsii_name="resetLambdaSuccessFeedbackRoleArn")
    def reset_lambda_success_feedback_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLambdaSuccessFeedbackRoleArn", []))

    @jsii.member(jsii_name="resetLambdaSuccessFeedbackSampleRate")
    def reset_lambda_success_feedback_sample_rate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLambdaSuccessFeedbackSampleRate", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamePrefix")
    def reset_name_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamePrefix", []))

    @jsii.member(jsii_name="resetPolicy")
    def reset_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicy", []))

    @jsii.member(jsii_name="resetSqsFailureFeedbackRoleArn")
    def reset_sqs_failure_feedback_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSqsFailureFeedbackRoleArn", []))

    @jsii.member(jsii_name="resetSqsSuccessFeedbackRoleArn")
    def reset_sqs_success_feedback_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSqsSuccessFeedbackRoleArn", []))

    @jsii.member(jsii_name="resetSqsSuccessFeedbackSampleRate")
    def reset_sqs_success_feedback_sample_rate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSqsSuccessFeedbackSampleRate", []))

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
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="owner")
    def owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "owner"))

    @builtins.property
    @jsii.member(jsii_name="applicationFailureFeedbackRoleArnInput")
    def application_failure_feedback_role_arn_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationFailureFeedbackRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationSuccessFeedbackRoleArnInput")
    def application_success_feedback_role_arn_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationSuccessFeedbackRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationSuccessFeedbackSampleRateInput")
    def application_success_feedback_sample_rate_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "applicationSuccessFeedbackSampleRateInput"))

    @builtins.property
    @jsii.member(jsii_name="contentBasedDeduplicationInput")
    def content_based_deduplication_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "contentBasedDeduplicationInput"))

    @builtins.property
    @jsii.member(jsii_name="deliveryPolicyInput")
    def delivery_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deliveryPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="fifoTopicInput")
    def fifo_topic_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "fifoTopicInput"))

    @builtins.property
    @jsii.member(jsii_name="firehoseFailureFeedbackRoleArnInput")
    def firehose_failure_feedback_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "firehoseFailureFeedbackRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="firehoseSuccessFeedbackRoleArnInput")
    def firehose_success_feedback_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "firehoseSuccessFeedbackRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="firehoseSuccessFeedbackSampleRateInput")
    def firehose_success_feedback_sample_rate_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "firehoseSuccessFeedbackSampleRateInput"))

    @builtins.property
    @jsii.member(jsii_name="httpFailureFeedbackRoleArnInput")
    def http_failure_feedback_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpFailureFeedbackRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="httpSuccessFeedbackRoleArnInput")
    def http_success_feedback_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpSuccessFeedbackRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="httpSuccessFeedbackSampleRateInput")
    def http_success_feedback_sample_rate_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "httpSuccessFeedbackSampleRateInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsMasterKeyIdInput")
    def kms_master_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsMasterKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaFailureFeedbackRoleArnInput")
    def lambda_failure_feedback_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lambdaFailureFeedbackRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaSuccessFeedbackRoleArnInput")
    def lambda_success_feedback_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lambdaSuccessFeedbackRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaSuccessFeedbackSampleRateInput")
    def lambda_success_feedback_sample_rate_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "lambdaSuccessFeedbackSampleRateInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namePrefixInput")
    def name_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namePrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="policyInput")
    def policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyInput"))

    @builtins.property
    @jsii.member(jsii_name="sqsFailureFeedbackRoleArnInput")
    def sqs_failure_feedback_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sqsFailureFeedbackRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sqsSuccessFeedbackRoleArnInput")
    def sqs_success_feedback_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sqsSuccessFeedbackRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sqsSuccessFeedbackSampleRateInput")
    def sqs_success_feedback_sample_rate_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sqsSuccessFeedbackSampleRateInput"))

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
    @jsii.member(jsii_name="applicationFailureFeedbackRoleArn")
    def application_failure_feedback_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationFailureFeedbackRoleArn"))

    @application_failure_feedback_role_arn.setter
    def application_failure_feedback_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8ce9ea1895293a7d7e22a1a28a453fef1e5a77e8220d9b0d2800dd61cce23c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationFailureFeedbackRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="applicationSuccessFeedbackRoleArn")
    def application_success_feedback_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationSuccessFeedbackRoleArn"))

    @application_success_feedback_role_arn.setter
    def application_success_feedback_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__515b5af728f2e106506495122114949616750cafbc971c07d712f0d96eaa58ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationSuccessFeedbackRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="applicationSuccessFeedbackSampleRate")
    def application_success_feedback_sample_rate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "applicationSuccessFeedbackSampleRate"))

    @application_success_feedback_sample_rate.setter
    def application_success_feedback_sample_rate(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ac1928ae9433ddaa858b3c90bbffcb56c4c41a6df3d92d044c271e69e58fcce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationSuccessFeedbackSampleRate", value)

    @builtins.property
    @jsii.member(jsii_name="contentBasedDeduplication")
    def content_based_deduplication(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "contentBasedDeduplication"))

    @content_based_deduplication.setter
    def content_based_deduplication(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e53debadcc6456bc5ef70c449c7691913e8b454841626751c824065881d18fe7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentBasedDeduplication", value)

    @builtins.property
    @jsii.member(jsii_name="deliveryPolicy")
    def delivery_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deliveryPolicy"))

    @delivery_policy.setter
    def delivery_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8201ca5d0e6a61d5f30de8b9416b24dfaa30ead3d262f6871369490ecac9dfa0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__172f1e097dd7db45949fcee558b77eb14c6a67854e3fe4430248e2dd7847f228)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="fifoTopic")
    def fifo_topic(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "fifoTopic"))

    @fifo_topic.setter
    def fifo_topic(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f769ad867971f9eefa5b63cffc647ce362bd0539e06491841024a3a3d7d3a1f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fifoTopic", value)

    @builtins.property
    @jsii.member(jsii_name="firehoseFailureFeedbackRoleArn")
    def firehose_failure_feedback_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firehoseFailureFeedbackRoleArn"))

    @firehose_failure_feedback_role_arn.setter
    def firehose_failure_feedback_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d348b8035f876e95b7c08572148d1558e9f81228432dba24b17125fefe48dcb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firehoseFailureFeedbackRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="firehoseSuccessFeedbackRoleArn")
    def firehose_success_feedback_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "firehoseSuccessFeedbackRoleArn"))

    @firehose_success_feedback_role_arn.setter
    def firehose_success_feedback_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd0265487b30633178ab82390c28218b3ae78bbf72be59fee9375ade83592712)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firehoseSuccessFeedbackRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="firehoseSuccessFeedbackSampleRate")
    def firehose_success_feedback_sample_rate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "firehoseSuccessFeedbackSampleRate"))

    @firehose_success_feedback_sample_rate.setter
    def firehose_success_feedback_sample_rate(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba5ac677d31537aebde633cb73f98350a76a206ebba8875951c60d6bed21c497)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "firehoseSuccessFeedbackSampleRate", value)

    @builtins.property
    @jsii.member(jsii_name="httpFailureFeedbackRoleArn")
    def http_failure_feedback_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpFailureFeedbackRoleArn"))

    @http_failure_feedback_role_arn.setter
    def http_failure_feedback_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c95749f4af75e136f524a960b70bf003429351e8f807dad2efd6ca7ccac315c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpFailureFeedbackRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="httpSuccessFeedbackRoleArn")
    def http_success_feedback_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpSuccessFeedbackRoleArn"))

    @http_success_feedback_role_arn.setter
    def http_success_feedback_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69be8c2b0d58fa82a1d152454e56e9cc86520cd6cd8e65412453c40142aefb96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpSuccessFeedbackRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="httpSuccessFeedbackSampleRate")
    def http_success_feedback_sample_rate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "httpSuccessFeedbackSampleRate"))

    @http_success_feedback_sample_rate.setter
    def http_success_feedback_sample_rate(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f68c3a762a0046e74dbe5a6227b70b6064dc767b6615d17846544ed962fa4a6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpSuccessFeedbackSampleRate", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d19339b53e4da46aaacbc053a467c00a2f9bf6328fd4b64049e71faf87112d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="kmsMasterKeyId")
    def kms_master_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsMasterKeyId"))

    @kms_master_key_id.setter
    def kms_master_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8d3e03a3f50670dde06a48f8b982e11d8381099ad593c33d8bc9cd9681e2bea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsMasterKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="lambdaFailureFeedbackRoleArn")
    def lambda_failure_feedback_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lambdaFailureFeedbackRoleArn"))

    @lambda_failure_feedback_role_arn.setter
    def lambda_failure_feedback_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de133de90cffddfcb652cba9d53f206247bce64f0978a1671196abb9a74271d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lambdaFailureFeedbackRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="lambdaSuccessFeedbackRoleArn")
    def lambda_success_feedback_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lambdaSuccessFeedbackRoleArn"))

    @lambda_success_feedback_role_arn.setter
    def lambda_success_feedback_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84134cb3f7187dfbd90c776c0d75d74756a425aae37a108b3f21f31b884e5332)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lambdaSuccessFeedbackRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="lambdaSuccessFeedbackSampleRate")
    def lambda_success_feedback_sample_rate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lambdaSuccessFeedbackSampleRate"))

    @lambda_success_feedback_sample_rate.setter
    def lambda_success_feedback_sample_rate(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3798191c7af62ebefacf093b2a9bff1a93e7dbf685b1f81114b25182172a5118)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lambdaSuccessFeedbackSampleRate", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10c010135b82d2babfe754e1f3b9a2fca90b2074884dbd032b85e44074f6e3f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namePrefix")
    def name_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namePrefix"))

    @name_prefix.setter
    def name_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c520edf89a6012825d28ef12b62a236ff97cf77f1e1620fa839f635ae93c1d59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namePrefix", value)

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policy"))

    @policy.setter
    def policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0f3a16dbf73768f6075a2b50cb03427711dc89a1944de9987aa7337de7ec36e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policy", value)

    @builtins.property
    @jsii.member(jsii_name="sqsFailureFeedbackRoleArn")
    def sqs_failure_feedback_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sqsFailureFeedbackRoleArn"))

    @sqs_failure_feedback_role_arn.setter
    def sqs_failure_feedback_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0180b3f38c33365239ce45dcbcc35885562f701bc99330072d17bb02382b64af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sqsFailureFeedbackRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="sqsSuccessFeedbackRoleArn")
    def sqs_success_feedback_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sqsSuccessFeedbackRoleArn"))

    @sqs_success_feedback_role_arn.setter
    def sqs_success_feedback_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1f3003a4f384a53bbd78061a28f2070623caa730d7caee85c6a484c720d7658)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sqsSuccessFeedbackRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="sqsSuccessFeedbackSampleRate")
    def sqs_success_feedback_sample_rate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sqsSuccessFeedbackSampleRate"))

    @sqs_success_feedback_sample_rate.setter
    def sqs_success_feedback_sample_rate(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__333f94c210f8c5fbcbbd2d04fff4903f4c2d034111aec0891970efb3b08b03c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sqsSuccessFeedbackSampleRate", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4edd33b0b7791e1d6b6e37ebc79674483fa1651a51b0df9e65465324a16f674)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94b6873d512dfbe54bdfadbe0e96d3d15e403e95a8086daf4e7b89778be2e7c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.snsTopic.SnsTopicConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "application_failure_feedback_role_arn": "applicationFailureFeedbackRoleArn",
        "application_success_feedback_role_arn": "applicationSuccessFeedbackRoleArn",
        "application_success_feedback_sample_rate": "applicationSuccessFeedbackSampleRate",
        "content_based_deduplication": "contentBasedDeduplication",
        "delivery_policy": "deliveryPolicy",
        "display_name": "displayName",
        "fifo_topic": "fifoTopic",
        "firehose_failure_feedback_role_arn": "firehoseFailureFeedbackRoleArn",
        "firehose_success_feedback_role_arn": "firehoseSuccessFeedbackRoleArn",
        "firehose_success_feedback_sample_rate": "firehoseSuccessFeedbackSampleRate",
        "http_failure_feedback_role_arn": "httpFailureFeedbackRoleArn",
        "http_success_feedback_role_arn": "httpSuccessFeedbackRoleArn",
        "http_success_feedback_sample_rate": "httpSuccessFeedbackSampleRate",
        "id": "id",
        "kms_master_key_id": "kmsMasterKeyId",
        "lambda_failure_feedback_role_arn": "lambdaFailureFeedbackRoleArn",
        "lambda_success_feedback_role_arn": "lambdaSuccessFeedbackRoleArn",
        "lambda_success_feedback_sample_rate": "lambdaSuccessFeedbackSampleRate",
        "name": "name",
        "name_prefix": "namePrefix",
        "policy": "policy",
        "sqs_failure_feedback_role_arn": "sqsFailureFeedbackRoleArn",
        "sqs_success_feedback_role_arn": "sqsSuccessFeedbackRoleArn",
        "sqs_success_feedback_sample_rate": "sqsSuccessFeedbackSampleRate",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class SnsTopicConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        application_failure_feedback_role_arn: typing.Optional[builtins.str] = None,
        application_success_feedback_role_arn: typing.Optional[builtins.str] = None,
        application_success_feedback_sample_rate: typing.Optional[jsii.Number] = None,
        content_based_deduplication: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        delivery_policy: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        fifo_topic: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        firehose_failure_feedback_role_arn: typing.Optional[builtins.str] = None,
        firehose_success_feedback_role_arn: typing.Optional[builtins.str] = None,
        firehose_success_feedback_sample_rate: typing.Optional[jsii.Number] = None,
        http_failure_feedback_role_arn: typing.Optional[builtins.str] = None,
        http_success_feedback_role_arn: typing.Optional[builtins.str] = None,
        http_success_feedback_sample_rate: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        kms_master_key_id: typing.Optional[builtins.str] = None,
        lambda_failure_feedback_role_arn: typing.Optional[builtins.str] = None,
        lambda_success_feedback_role_arn: typing.Optional[builtins.str] = None,
        lambda_success_feedback_sample_rate: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        name_prefix: typing.Optional[builtins.str] = None,
        policy: typing.Optional[builtins.str] = None,
        sqs_failure_feedback_role_arn: typing.Optional[builtins.str] = None,
        sqs_success_feedback_role_arn: typing.Optional[builtins.str] = None,
        sqs_success_feedback_sample_rate: typing.Optional[jsii.Number] = None,
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
        :param application_failure_feedback_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#application_failure_feedback_role_arn SnsTopic#application_failure_feedback_role_arn}.
        :param application_success_feedback_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#application_success_feedback_role_arn SnsTopic#application_success_feedback_role_arn}.
        :param application_success_feedback_sample_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#application_success_feedback_sample_rate SnsTopic#application_success_feedback_sample_rate}.
        :param content_based_deduplication: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#content_based_deduplication SnsTopic#content_based_deduplication}.
        :param delivery_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#delivery_policy SnsTopic#delivery_policy}.
        :param display_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#display_name SnsTopic#display_name}.
        :param fifo_topic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#fifo_topic SnsTopic#fifo_topic}.
        :param firehose_failure_feedback_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#firehose_failure_feedback_role_arn SnsTopic#firehose_failure_feedback_role_arn}.
        :param firehose_success_feedback_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#firehose_success_feedback_role_arn SnsTopic#firehose_success_feedback_role_arn}.
        :param firehose_success_feedback_sample_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#firehose_success_feedback_sample_rate SnsTopic#firehose_success_feedback_sample_rate}.
        :param http_failure_feedback_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#http_failure_feedback_role_arn SnsTopic#http_failure_feedback_role_arn}.
        :param http_success_feedback_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#http_success_feedback_role_arn SnsTopic#http_success_feedback_role_arn}.
        :param http_success_feedback_sample_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#http_success_feedback_sample_rate SnsTopic#http_success_feedback_sample_rate}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#id SnsTopic#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_master_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#kms_master_key_id SnsTopic#kms_master_key_id}.
        :param lambda_failure_feedback_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#lambda_failure_feedback_role_arn SnsTopic#lambda_failure_feedback_role_arn}.
        :param lambda_success_feedback_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#lambda_success_feedback_role_arn SnsTopic#lambda_success_feedback_role_arn}.
        :param lambda_success_feedback_sample_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#lambda_success_feedback_sample_rate SnsTopic#lambda_success_feedback_sample_rate}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#name SnsTopic#name}.
        :param name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#name_prefix SnsTopic#name_prefix}.
        :param policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#policy SnsTopic#policy}.
        :param sqs_failure_feedback_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#sqs_failure_feedback_role_arn SnsTopic#sqs_failure_feedback_role_arn}.
        :param sqs_success_feedback_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#sqs_success_feedback_role_arn SnsTopic#sqs_success_feedback_role_arn}.
        :param sqs_success_feedback_sample_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#sqs_success_feedback_sample_rate SnsTopic#sqs_success_feedback_sample_rate}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#tags SnsTopic#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#tags_all SnsTopic#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a0c2d8995e775f953b7cab4b54c486b9e68d90ffae36b98f1c10e147d103381)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument application_failure_feedback_role_arn", value=application_failure_feedback_role_arn, expected_type=type_hints["application_failure_feedback_role_arn"])
            check_type(argname="argument application_success_feedback_role_arn", value=application_success_feedback_role_arn, expected_type=type_hints["application_success_feedback_role_arn"])
            check_type(argname="argument application_success_feedback_sample_rate", value=application_success_feedback_sample_rate, expected_type=type_hints["application_success_feedback_sample_rate"])
            check_type(argname="argument content_based_deduplication", value=content_based_deduplication, expected_type=type_hints["content_based_deduplication"])
            check_type(argname="argument delivery_policy", value=delivery_policy, expected_type=type_hints["delivery_policy"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument fifo_topic", value=fifo_topic, expected_type=type_hints["fifo_topic"])
            check_type(argname="argument firehose_failure_feedback_role_arn", value=firehose_failure_feedback_role_arn, expected_type=type_hints["firehose_failure_feedback_role_arn"])
            check_type(argname="argument firehose_success_feedback_role_arn", value=firehose_success_feedback_role_arn, expected_type=type_hints["firehose_success_feedback_role_arn"])
            check_type(argname="argument firehose_success_feedback_sample_rate", value=firehose_success_feedback_sample_rate, expected_type=type_hints["firehose_success_feedback_sample_rate"])
            check_type(argname="argument http_failure_feedback_role_arn", value=http_failure_feedback_role_arn, expected_type=type_hints["http_failure_feedback_role_arn"])
            check_type(argname="argument http_success_feedback_role_arn", value=http_success_feedback_role_arn, expected_type=type_hints["http_success_feedback_role_arn"])
            check_type(argname="argument http_success_feedback_sample_rate", value=http_success_feedback_sample_rate, expected_type=type_hints["http_success_feedback_sample_rate"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument kms_master_key_id", value=kms_master_key_id, expected_type=type_hints["kms_master_key_id"])
            check_type(argname="argument lambda_failure_feedback_role_arn", value=lambda_failure_feedback_role_arn, expected_type=type_hints["lambda_failure_feedback_role_arn"])
            check_type(argname="argument lambda_success_feedback_role_arn", value=lambda_success_feedback_role_arn, expected_type=type_hints["lambda_success_feedback_role_arn"])
            check_type(argname="argument lambda_success_feedback_sample_rate", value=lambda_success_feedback_sample_rate, expected_type=type_hints["lambda_success_feedback_sample_rate"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument name_prefix", value=name_prefix, expected_type=type_hints["name_prefix"])
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            check_type(argname="argument sqs_failure_feedback_role_arn", value=sqs_failure_feedback_role_arn, expected_type=type_hints["sqs_failure_feedback_role_arn"])
            check_type(argname="argument sqs_success_feedback_role_arn", value=sqs_success_feedback_role_arn, expected_type=type_hints["sqs_success_feedback_role_arn"])
            check_type(argname="argument sqs_success_feedback_sample_rate", value=sqs_success_feedback_sample_rate, expected_type=type_hints["sqs_success_feedback_sample_rate"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
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
        if application_failure_feedback_role_arn is not None:
            self._values["application_failure_feedback_role_arn"] = application_failure_feedback_role_arn
        if application_success_feedback_role_arn is not None:
            self._values["application_success_feedback_role_arn"] = application_success_feedback_role_arn
        if application_success_feedback_sample_rate is not None:
            self._values["application_success_feedback_sample_rate"] = application_success_feedback_sample_rate
        if content_based_deduplication is not None:
            self._values["content_based_deduplication"] = content_based_deduplication
        if delivery_policy is not None:
            self._values["delivery_policy"] = delivery_policy
        if display_name is not None:
            self._values["display_name"] = display_name
        if fifo_topic is not None:
            self._values["fifo_topic"] = fifo_topic
        if firehose_failure_feedback_role_arn is not None:
            self._values["firehose_failure_feedback_role_arn"] = firehose_failure_feedback_role_arn
        if firehose_success_feedback_role_arn is not None:
            self._values["firehose_success_feedback_role_arn"] = firehose_success_feedback_role_arn
        if firehose_success_feedback_sample_rate is not None:
            self._values["firehose_success_feedback_sample_rate"] = firehose_success_feedback_sample_rate
        if http_failure_feedback_role_arn is not None:
            self._values["http_failure_feedback_role_arn"] = http_failure_feedback_role_arn
        if http_success_feedback_role_arn is not None:
            self._values["http_success_feedback_role_arn"] = http_success_feedback_role_arn
        if http_success_feedback_sample_rate is not None:
            self._values["http_success_feedback_sample_rate"] = http_success_feedback_sample_rate
        if id is not None:
            self._values["id"] = id
        if kms_master_key_id is not None:
            self._values["kms_master_key_id"] = kms_master_key_id
        if lambda_failure_feedback_role_arn is not None:
            self._values["lambda_failure_feedback_role_arn"] = lambda_failure_feedback_role_arn
        if lambda_success_feedback_role_arn is not None:
            self._values["lambda_success_feedback_role_arn"] = lambda_success_feedback_role_arn
        if lambda_success_feedback_sample_rate is not None:
            self._values["lambda_success_feedback_sample_rate"] = lambda_success_feedback_sample_rate
        if name is not None:
            self._values["name"] = name
        if name_prefix is not None:
            self._values["name_prefix"] = name_prefix
        if policy is not None:
            self._values["policy"] = policy
        if sqs_failure_feedback_role_arn is not None:
            self._values["sqs_failure_feedback_role_arn"] = sqs_failure_feedback_role_arn
        if sqs_success_feedback_role_arn is not None:
            self._values["sqs_success_feedback_role_arn"] = sqs_success_feedback_role_arn
        if sqs_success_feedback_sample_rate is not None:
            self._values["sqs_success_feedback_sample_rate"] = sqs_success_feedback_sample_rate
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
    def application_failure_feedback_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#application_failure_feedback_role_arn SnsTopic#application_failure_feedback_role_arn}.'''
        result = self._values.get("application_failure_feedback_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def application_success_feedback_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#application_success_feedback_role_arn SnsTopic#application_success_feedback_role_arn}.'''
        result = self._values.get("application_success_feedback_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def application_success_feedback_sample_rate(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#application_success_feedback_sample_rate SnsTopic#application_success_feedback_sample_rate}.'''
        result = self._values.get("application_success_feedback_sample_rate")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def content_based_deduplication(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#content_based_deduplication SnsTopic#content_based_deduplication}.'''
        result = self._values.get("content_based_deduplication")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def delivery_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#delivery_policy SnsTopic#delivery_policy}.'''
        result = self._values.get("delivery_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#display_name SnsTopic#display_name}.'''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fifo_topic(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#fifo_topic SnsTopic#fifo_topic}.'''
        result = self._values.get("fifo_topic")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def firehose_failure_feedback_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#firehose_failure_feedback_role_arn SnsTopic#firehose_failure_feedback_role_arn}.'''
        result = self._values.get("firehose_failure_feedback_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def firehose_success_feedback_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#firehose_success_feedback_role_arn SnsTopic#firehose_success_feedback_role_arn}.'''
        result = self._values.get("firehose_success_feedback_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def firehose_success_feedback_sample_rate(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#firehose_success_feedback_sample_rate SnsTopic#firehose_success_feedback_sample_rate}.'''
        result = self._values.get("firehose_success_feedback_sample_rate")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def http_failure_feedback_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#http_failure_feedback_role_arn SnsTopic#http_failure_feedback_role_arn}.'''
        result = self._values.get("http_failure_feedback_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_success_feedback_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#http_success_feedback_role_arn SnsTopic#http_success_feedback_role_arn}.'''
        result = self._values.get("http_success_feedback_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_success_feedback_sample_rate(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#http_success_feedback_sample_rate SnsTopic#http_success_feedback_sample_rate}.'''
        result = self._values.get("http_success_feedback_sample_rate")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#id SnsTopic#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_master_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#kms_master_key_id SnsTopic#kms_master_key_id}.'''
        result = self._values.get("kms_master_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lambda_failure_feedback_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#lambda_failure_feedback_role_arn SnsTopic#lambda_failure_feedback_role_arn}.'''
        result = self._values.get("lambda_failure_feedback_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lambda_success_feedback_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#lambda_success_feedback_role_arn SnsTopic#lambda_success_feedback_role_arn}.'''
        result = self._values.get("lambda_success_feedback_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lambda_success_feedback_sample_rate(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#lambda_success_feedback_sample_rate SnsTopic#lambda_success_feedback_sample_rate}.'''
        result = self._values.get("lambda_success_feedback_sample_rate")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#name SnsTopic#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#name_prefix SnsTopic#name_prefix}.'''
        result = self._values.get("name_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#policy SnsTopic#policy}.'''
        result = self._values.get("policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sqs_failure_feedback_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#sqs_failure_feedback_role_arn SnsTopic#sqs_failure_feedback_role_arn}.'''
        result = self._values.get("sqs_failure_feedback_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sqs_success_feedback_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#sqs_success_feedback_role_arn SnsTopic#sqs_success_feedback_role_arn}.'''
        result = self._values.get("sqs_success_feedback_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sqs_success_feedback_sample_rate(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#sqs_success_feedback_sample_rate SnsTopic#sqs_success_feedback_sample_rate}.'''
        result = self._values.get("sqs_success_feedback_sample_rate")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#tags SnsTopic#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/sns_topic#tags_all SnsTopic#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SnsTopicConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "SnsTopic",
    "SnsTopicConfig",
]

publication.publish()

def _typecheckingstub__9bbfa52b06083b87b43c7250d9c7dba1eb7790344f793b7c08d5902ab23cc64e(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    application_failure_feedback_role_arn: typing.Optional[builtins.str] = None,
    application_success_feedback_role_arn: typing.Optional[builtins.str] = None,
    application_success_feedback_sample_rate: typing.Optional[jsii.Number] = None,
    content_based_deduplication: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    delivery_policy: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    fifo_topic: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    firehose_failure_feedback_role_arn: typing.Optional[builtins.str] = None,
    firehose_success_feedback_role_arn: typing.Optional[builtins.str] = None,
    firehose_success_feedback_sample_rate: typing.Optional[jsii.Number] = None,
    http_failure_feedback_role_arn: typing.Optional[builtins.str] = None,
    http_success_feedback_role_arn: typing.Optional[builtins.str] = None,
    http_success_feedback_sample_rate: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    kms_master_key_id: typing.Optional[builtins.str] = None,
    lambda_failure_feedback_role_arn: typing.Optional[builtins.str] = None,
    lambda_success_feedback_role_arn: typing.Optional[builtins.str] = None,
    lambda_success_feedback_sample_rate: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
    name_prefix: typing.Optional[builtins.str] = None,
    policy: typing.Optional[builtins.str] = None,
    sqs_failure_feedback_role_arn: typing.Optional[builtins.str] = None,
    sqs_success_feedback_role_arn: typing.Optional[builtins.str] = None,
    sqs_success_feedback_sample_rate: typing.Optional[jsii.Number] = None,
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

def _typecheckingstub__f8ce9ea1895293a7d7e22a1a28a453fef1e5a77e8220d9b0d2800dd61cce23c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__515b5af728f2e106506495122114949616750cafbc971c07d712f0d96eaa58ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ac1928ae9433ddaa858b3c90bbffcb56c4c41a6df3d92d044c271e69e58fcce(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e53debadcc6456bc5ef70c449c7691913e8b454841626751c824065881d18fe7(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8201ca5d0e6a61d5f30de8b9416b24dfaa30ead3d262f6871369490ecac9dfa0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__172f1e097dd7db45949fcee558b77eb14c6a67854e3fe4430248e2dd7847f228(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f769ad867971f9eefa5b63cffc647ce362bd0539e06491841024a3a3d7d3a1f7(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d348b8035f876e95b7c08572148d1558e9f81228432dba24b17125fefe48dcb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd0265487b30633178ab82390c28218b3ae78bbf72be59fee9375ade83592712(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba5ac677d31537aebde633cb73f98350a76a206ebba8875951c60d6bed21c497(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c95749f4af75e136f524a960b70bf003429351e8f807dad2efd6ca7ccac315c8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69be8c2b0d58fa82a1d152454e56e9cc86520cd6cd8e65412453c40142aefb96(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f68c3a762a0046e74dbe5a6227b70b6064dc767b6615d17846544ed962fa4a6c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d19339b53e4da46aaacbc053a467c00a2f9bf6328fd4b64049e71faf87112d5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8d3e03a3f50670dde06a48f8b982e11d8381099ad593c33d8bc9cd9681e2bea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de133de90cffddfcb652cba9d53f206247bce64f0978a1671196abb9a74271d8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84134cb3f7187dfbd90c776c0d75d74756a425aae37a108b3f21f31b884e5332(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3798191c7af62ebefacf093b2a9bff1a93e7dbf685b1f81114b25182172a5118(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10c010135b82d2babfe754e1f3b9a2fca90b2074884dbd032b85e44074f6e3f5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c520edf89a6012825d28ef12b62a236ff97cf77f1e1620fa839f635ae93c1d59(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0f3a16dbf73768f6075a2b50cb03427711dc89a1944de9987aa7337de7ec36e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0180b3f38c33365239ce45dcbcc35885562f701bc99330072d17bb02382b64af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1f3003a4f384a53bbd78061a28f2070623caa730d7caee85c6a484c720d7658(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__333f94c210f8c5fbcbbd2d04fff4903f4c2d034111aec0891970efb3b08b03c3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4edd33b0b7791e1d6b6e37ebc79674483fa1651a51b0df9e65465324a16f674(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94b6873d512dfbe54bdfadbe0e96d3d15e403e95a8086daf4e7b89778be2e7c2(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a0c2d8995e775f953b7cab4b54c486b9e68d90ffae36b98f1c10e147d103381(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    application_failure_feedback_role_arn: typing.Optional[builtins.str] = None,
    application_success_feedback_role_arn: typing.Optional[builtins.str] = None,
    application_success_feedback_sample_rate: typing.Optional[jsii.Number] = None,
    content_based_deduplication: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    delivery_policy: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    fifo_topic: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    firehose_failure_feedback_role_arn: typing.Optional[builtins.str] = None,
    firehose_success_feedback_role_arn: typing.Optional[builtins.str] = None,
    firehose_success_feedback_sample_rate: typing.Optional[jsii.Number] = None,
    http_failure_feedback_role_arn: typing.Optional[builtins.str] = None,
    http_success_feedback_role_arn: typing.Optional[builtins.str] = None,
    http_success_feedback_sample_rate: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    kms_master_key_id: typing.Optional[builtins.str] = None,
    lambda_failure_feedback_role_arn: typing.Optional[builtins.str] = None,
    lambda_success_feedback_role_arn: typing.Optional[builtins.str] = None,
    lambda_success_feedback_sample_rate: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
    name_prefix: typing.Optional[builtins.str] = None,
    policy: typing.Optional[builtins.str] = None,
    sqs_failure_feedback_role_arn: typing.Optional[builtins.str] = None,
    sqs_success_feedback_role_arn: typing.Optional[builtins.str] = None,
    sqs_success_feedback_sample_rate: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
