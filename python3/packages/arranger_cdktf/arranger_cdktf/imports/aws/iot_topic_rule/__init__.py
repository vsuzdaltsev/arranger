'''
# `aws_iot_topic_rule`

Refer to the Terraform Registory for docs: [`aws_iot_topic_rule`](https://www.terraform.io/docs/providers/aws/r/iot_topic_rule).
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


class IotTopicRule(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRule",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule aws_iot_topic_rule}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        name: builtins.str,
        sql: builtins.str,
        sql_version: builtins.str,
        cloudwatch_alarm: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleCloudwatchAlarm", typing.Dict[builtins.str, typing.Any]]]]] = None,
        cloudwatch_logs: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleCloudwatchLogs", typing.Dict[builtins.str, typing.Any]]]]] = None,
        cloudwatch_metric: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleCloudwatchMetric", typing.Dict[builtins.str, typing.Any]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        dynamodb: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleDynamodb", typing.Dict[builtins.str, typing.Any]]]]] = None,
        dynamodbv2: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleDynamodbv2", typing.Dict[builtins.str, typing.Any]]]]] = None,
        elasticsearch: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleElasticsearch", typing.Dict[builtins.str, typing.Any]]]]] = None,
        error_action: typing.Optional[typing.Union["IotTopicRuleErrorAction", typing.Dict[builtins.str, typing.Any]]] = None,
        firehose: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleFirehose", typing.Dict[builtins.str, typing.Any]]]]] = None,
        http: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleHttp", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        iot_analytics: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleIotAnalytics", typing.Dict[builtins.str, typing.Any]]]]] = None,
        iot_events: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleIotEvents", typing.Dict[builtins.str, typing.Any]]]]] = None,
        kafka: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleKafka", typing.Dict[builtins.str, typing.Any]]]]] = None,
        kinesis: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleKinesis", typing.Dict[builtins.str, typing.Any]]]]] = None,
        lambda_: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleLambda", typing.Dict[builtins.str, typing.Any]]]]] = None,
        republish: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleRepublish", typing.Dict[builtins.str, typing.Any]]]]] = None,
        s3: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleS3", typing.Dict[builtins.str, typing.Any]]]]] = None,
        sns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleSns", typing.Dict[builtins.str, typing.Any]]]]] = None,
        sqs: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleSqs", typing.Dict[builtins.str, typing.Any]]]]] = None,
        step_functions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleStepFunctions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timestream: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleTimestream", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule aws_iot_topic_rule} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#enabled IotTopicRule#enabled}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#name IotTopicRule#name}.
        :param sql: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#sql IotTopicRule#sql}.
        :param sql_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#sql_version IotTopicRule#sql_version}.
        :param cloudwatch_alarm: cloudwatch_alarm block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#cloudwatch_alarm IotTopicRule#cloudwatch_alarm}
        :param cloudwatch_logs: cloudwatch_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#cloudwatch_logs IotTopicRule#cloudwatch_logs}
        :param cloudwatch_metric: cloudwatch_metric block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#cloudwatch_metric IotTopicRule#cloudwatch_metric}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#description IotTopicRule#description}.
        :param dynamodb: dynamodb block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#dynamodb IotTopicRule#dynamodb}
        :param dynamodbv2: dynamodbv2 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#dynamodbv2 IotTopicRule#dynamodbv2}
        :param elasticsearch: elasticsearch block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#elasticsearch IotTopicRule#elasticsearch}
        :param error_action: error_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#error_action IotTopicRule#error_action}
        :param firehose: firehose block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#firehose IotTopicRule#firehose}
        :param http: http block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#http IotTopicRule#http}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#id IotTopicRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param iot_analytics: iot_analytics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#iot_analytics IotTopicRule#iot_analytics}
        :param iot_events: iot_events block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#iot_events IotTopicRule#iot_events}
        :param kafka: kafka block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#kafka IotTopicRule#kafka}
        :param kinesis: kinesis block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#kinesis IotTopicRule#kinesis}
        :param lambda_: lambda block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#lambda IotTopicRule#lambda}
        :param republish: republish block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#republish IotTopicRule#republish}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#s3 IotTopicRule#s3}
        :param sns: sns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#sns IotTopicRule#sns}
        :param sqs: sqs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#sqs IotTopicRule#sqs}
        :param step_functions: step_functions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#step_functions IotTopicRule#step_functions}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#tags IotTopicRule#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#tags_all IotTopicRule#tags_all}.
        :param timestream: timestream block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#timestream IotTopicRule#timestream}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53670b127d5862e8066940465f5e310da6ce613316c0feb9e07d3e802c4a9be4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = IotTopicRuleConfig(
            enabled=enabled,
            name=name,
            sql=sql,
            sql_version=sql_version,
            cloudwatch_alarm=cloudwatch_alarm,
            cloudwatch_logs=cloudwatch_logs,
            cloudwatch_metric=cloudwatch_metric,
            description=description,
            dynamodb=dynamodb,
            dynamodbv2=dynamodbv2,
            elasticsearch=elasticsearch,
            error_action=error_action,
            firehose=firehose,
            http=http,
            id=id,
            iot_analytics=iot_analytics,
            iot_events=iot_events,
            kafka=kafka,
            kinesis=kinesis,
            lambda_=lambda_,
            republish=republish,
            s3=s3,
            sns=sns,
            sqs=sqs,
            step_functions=step_functions,
            tags=tags,
            tags_all=tags_all,
            timestream=timestream,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCloudwatchAlarm")
    def put_cloudwatch_alarm(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleCloudwatchAlarm", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__362133bd6a35384a3c62d526dd83a4fedf91c37edbaedcc8ae2bd418367d6362)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCloudwatchAlarm", [value]))

    @jsii.member(jsii_name="putCloudwatchLogs")
    def put_cloudwatch_logs(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleCloudwatchLogs", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eaa53f1f517b762ecce5381dced00415e52204e2fd19b2972f205933e95f844b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCloudwatchLogs", [value]))

    @jsii.member(jsii_name="putCloudwatchMetric")
    def put_cloudwatch_metric(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleCloudwatchMetric", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5f77882f27a17d3981f2b0e808646e312ab73e3ef5ab472dca280ff57a63ce9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCloudwatchMetric", [value]))

    @jsii.member(jsii_name="putDynamodb")
    def put_dynamodb(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleDynamodb", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__edf76234c332849f67d25b8170310da07b926bf51455d2abab8f267470337500)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDynamodb", [value]))

    @jsii.member(jsii_name="putDynamodbv2")
    def put_dynamodbv2(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleDynamodbv2", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bfb0dca78e7d87ca039dbd7c4696677715921f4c61ccb4d5785a7af2dcba029)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDynamodbv2", [value]))

    @jsii.member(jsii_name="putElasticsearch")
    def put_elasticsearch(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleElasticsearch", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b93fd828f0f89be54d9f98cbe44ee62fac68487e760b15a6f45337bf7bd42c3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putElasticsearch", [value]))

    @jsii.member(jsii_name="putErrorAction")
    def put_error_action(
        self,
        *,
        cloudwatch_alarm: typing.Optional[typing.Union["IotTopicRuleErrorActionCloudwatchAlarm", typing.Dict[builtins.str, typing.Any]]] = None,
        cloudwatch_logs: typing.Optional[typing.Union["IotTopicRuleErrorActionCloudwatchLogs", typing.Dict[builtins.str, typing.Any]]] = None,
        cloudwatch_metric: typing.Optional[typing.Union["IotTopicRuleErrorActionCloudwatchMetric", typing.Dict[builtins.str, typing.Any]]] = None,
        dynamodb: typing.Optional[typing.Union["IotTopicRuleErrorActionDynamodb", typing.Dict[builtins.str, typing.Any]]] = None,
        dynamodbv2: typing.Optional[typing.Union["IotTopicRuleErrorActionDynamodbv2", typing.Dict[builtins.str, typing.Any]]] = None,
        elasticsearch: typing.Optional[typing.Union["IotTopicRuleErrorActionElasticsearch", typing.Dict[builtins.str, typing.Any]]] = None,
        firehose: typing.Optional[typing.Union["IotTopicRuleErrorActionFirehose", typing.Dict[builtins.str, typing.Any]]] = None,
        http: typing.Optional[typing.Union["IotTopicRuleErrorActionHttp", typing.Dict[builtins.str, typing.Any]]] = None,
        iot_analytics: typing.Optional[typing.Union["IotTopicRuleErrorActionIotAnalytics", typing.Dict[builtins.str, typing.Any]]] = None,
        iot_events: typing.Optional[typing.Union["IotTopicRuleErrorActionIotEvents", typing.Dict[builtins.str, typing.Any]]] = None,
        kafka: typing.Optional[typing.Union["IotTopicRuleErrorActionKafka", typing.Dict[builtins.str, typing.Any]]] = None,
        kinesis: typing.Optional[typing.Union["IotTopicRuleErrorActionKinesis", typing.Dict[builtins.str, typing.Any]]] = None,
        lambda_: typing.Optional[typing.Union["IotTopicRuleErrorActionLambda", typing.Dict[builtins.str, typing.Any]]] = None,
        republish: typing.Optional[typing.Union["IotTopicRuleErrorActionRepublish", typing.Dict[builtins.str, typing.Any]]] = None,
        s3: typing.Optional[typing.Union["IotTopicRuleErrorActionS3", typing.Dict[builtins.str, typing.Any]]] = None,
        sns: typing.Optional[typing.Union["IotTopicRuleErrorActionSns", typing.Dict[builtins.str, typing.Any]]] = None,
        sqs: typing.Optional[typing.Union["IotTopicRuleErrorActionSqs", typing.Dict[builtins.str, typing.Any]]] = None,
        step_functions: typing.Optional[typing.Union["IotTopicRuleErrorActionStepFunctions", typing.Dict[builtins.str, typing.Any]]] = None,
        timestream: typing.Optional[typing.Union["IotTopicRuleErrorActionTimestream", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cloudwatch_alarm: cloudwatch_alarm block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#cloudwatch_alarm IotTopicRule#cloudwatch_alarm}
        :param cloudwatch_logs: cloudwatch_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#cloudwatch_logs IotTopicRule#cloudwatch_logs}
        :param cloudwatch_metric: cloudwatch_metric block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#cloudwatch_metric IotTopicRule#cloudwatch_metric}
        :param dynamodb: dynamodb block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#dynamodb IotTopicRule#dynamodb}
        :param dynamodbv2: dynamodbv2 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#dynamodbv2 IotTopicRule#dynamodbv2}
        :param elasticsearch: elasticsearch block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#elasticsearch IotTopicRule#elasticsearch}
        :param firehose: firehose block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#firehose IotTopicRule#firehose}
        :param http: http block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#http IotTopicRule#http}
        :param iot_analytics: iot_analytics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#iot_analytics IotTopicRule#iot_analytics}
        :param iot_events: iot_events block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#iot_events IotTopicRule#iot_events}
        :param kafka: kafka block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#kafka IotTopicRule#kafka}
        :param kinesis: kinesis block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#kinesis IotTopicRule#kinesis}
        :param lambda_: lambda block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#lambda IotTopicRule#lambda}
        :param republish: republish block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#republish IotTopicRule#republish}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#s3 IotTopicRule#s3}
        :param sns: sns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#sns IotTopicRule#sns}
        :param sqs: sqs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#sqs IotTopicRule#sqs}
        :param step_functions: step_functions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#step_functions IotTopicRule#step_functions}
        :param timestream: timestream block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#timestream IotTopicRule#timestream}
        '''
        value = IotTopicRuleErrorAction(
            cloudwatch_alarm=cloudwatch_alarm,
            cloudwatch_logs=cloudwatch_logs,
            cloudwatch_metric=cloudwatch_metric,
            dynamodb=dynamodb,
            dynamodbv2=dynamodbv2,
            elasticsearch=elasticsearch,
            firehose=firehose,
            http=http,
            iot_analytics=iot_analytics,
            iot_events=iot_events,
            kafka=kafka,
            kinesis=kinesis,
            lambda_=lambda_,
            republish=republish,
            s3=s3,
            sns=sns,
            sqs=sqs,
            step_functions=step_functions,
            timestream=timestream,
        )

        return typing.cast(None, jsii.invoke(self, "putErrorAction", [value]))

    @jsii.member(jsii_name="putFirehose")
    def put_firehose(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleFirehose", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__884bf8faf6d9af52bd22a9d972b81205014382bb7c299dd1819717902623dcd7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFirehose", [value]))

    @jsii.member(jsii_name="putHttp")
    def put_http(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleHttp", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbd55a917d80427c9c1994232fe8b47685eef47e9766039a213b6988af7ec4fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHttp", [value]))

    @jsii.member(jsii_name="putIotAnalytics")
    def put_iot_analytics(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleIotAnalytics", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a2b8464aa1eec963de08aa62422be98c48b2cb8e4b8c89986777e5060573b74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIotAnalytics", [value]))

    @jsii.member(jsii_name="putIotEvents")
    def put_iot_events(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleIotEvents", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75742a7bf0f72261f82396af77d5a3e6f25ee5f610e0fdd026d2a32dd9dd947e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIotEvents", [value]))

    @jsii.member(jsii_name="putKafka")
    def put_kafka(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleKafka", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac2ac3e81225d7f8b22c765865c010ac56bf50b0a202c257d8158af333cb9d52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putKafka", [value]))

    @jsii.member(jsii_name="putKinesis")
    def put_kinesis(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleKinesis", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e0e805681e2c0f904591f06a365a590a23a24cc203e3d16e85373ecddd44961)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putKinesis", [value]))

    @jsii.member(jsii_name="putLambda")
    def put_lambda(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleLambda", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9715a0f1d1c15cb4a3c0dc3da760da74be6c9226d3dff46b85e317e1fe20f583)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLambda", [value]))

    @jsii.member(jsii_name="putRepublish")
    def put_republish(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleRepublish", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__708984d01363a1cb9ef913783c71f8f61a9dee6580aa92b75e7109764d78b1e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRepublish", [value]))

    @jsii.member(jsii_name="putS3")
    def put_s3(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleS3", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__caf02f248ff59e8fc4baeb94038cea8ff9a5c0f9a08f49b367388128dff6576e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putS3", [value]))

    @jsii.member(jsii_name="putSns")
    def put_sns(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleSns", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1575481ec878c11843cb1669f8a8d2c4a5a802e4f8ad0bda5753cd57802ff2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSns", [value]))

    @jsii.member(jsii_name="putSqs")
    def put_sqs(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleSqs", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d0f4edf83575d39f709458730769364a836e07c7975df6b565d368aeb3062e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSqs", [value]))

    @jsii.member(jsii_name="putStepFunctions")
    def put_step_functions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleStepFunctions", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97d660355f2d7f2271a0fa6a5f334dd56a11ee0ae93f8c2eb0917ae9b1832dd8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStepFunctions", [value]))

    @jsii.member(jsii_name="putTimestream")
    def put_timestream(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleTimestream", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8de221367533070bdc5ac62657c33a2fb94de45c44118a63a72cff460f17516c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTimestream", [value]))

    @jsii.member(jsii_name="resetCloudwatchAlarm")
    def reset_cloudwatch_alarm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchAlarm", []))

    @jsii.member(jsii_name="resetCloudwatchLogs")
    def reset_cloudwatch_logs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchLogs", []))

    @jsii.member(jsii_name="resetCloudwatchMetric")
    def reset_cloudwatch_metric(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchMetric", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDynamodb")
    def reset_dynamodb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDynamodb", []))

    @jsii.member(jsii_name="resetDynamodbv2")
    def reset_dynamodbv2(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDynamodbv2", []))

    @jsii.member(jsii_name="resetElasticsearch")
    def reset_elasticsearch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetElasticsearch", []))

    @jsii.member(jsii_name="resetErrorAction")
    def reset_error_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorAction", []))

    @jsii.member(jsii_name="resetFirehose")
    def reset_firehose(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirehose", []))

    @jsii.member(jsii_name="resetHttp")
    def reset_http(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttp", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIotAnalytics")
    def reset_iot_analytics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIotAnalytics", []))

    @jsii.member(jsii_name="resetIotEvents")
    def reset_iot_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIotEvents", []))

    @jsii.member(jsii_name="resetKafka")
    def reset_kafka(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKafka", []))

    @jsii.member(jsii_name="resetKinesis")
    def reset_kinesis(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKinesis", []))

    @jsii.member(jsii_name="resetLambda")
    def reset_lambda(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLambda", []))

    @jsii.member(jsii_name="resetRepublish")
    def reset_republish(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepublish", []))

    @jsii.member(jsii_name="resetS3")
    def reset_s3(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3", []))

    @jsii.member(jsii_name="resetSns")
    def reset_sns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSns", []))

    @jsii.member(jsii_name="resetSqs")
    def reset_sqs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSqs", []))

    @jsii.member(jsii_name="resetStepFunctions")
    def reset_step_functions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStepFunctions", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTimestream")
    def reset_timestream(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimestream", []))

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
    @jsii.member(jsii_name="cloudwatchAlarm")
    def cloudwatch_alarm(self) -> "IotTopicRuleCloudwatchAlarmList":
        return typing.cast("IotTopicRuleCloudwatchAlarmList", jsii.get(self, "cloudwatchAlarm"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogs")
    def cloudwatch_logs(self) -> "IotTopicRuleCloudwatchLogsList":
        return typing.cast("IotTopicRuleCloudwatchLogsList", jsii.get(self, "cloudwatchLogs"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchMetric")
    def cloudwatch_metric(self) -> "IotTopicRuleCloudwatchMetricList":
        return typing.cast("IotTopicRuleCloudwatchMetricList", jsii.get(self, "cloudwatchMetric"))

    @builtins.property
    @jsii.member(jsii_name="dynamodb")
    def dynamodb(self) -> "IotTopicRuleDynamodbList":
        return typing.cast("IotTopicRuleDynamodbList", jsii.get(self, "dynamodb"))

    @builtins.property
    @jsii.member(jsii_name="dynamodbv2")
    def dynamodbv2(self) -> "IotTopicRuleDynamodbv2List":
        return typing.cast("IotTopicRuleDynamodbv2List", jsii.get(self, "dynamodbv2"))

    @builtins.property
    @jsii.member(jsii_name="elasticsearch")
    def elasticsearch(self) -> "IotTopicRuleElasticsearchList":
        return typing.cast("IotTopicRuleElasticsearchList", jsii.get(self, "elasticsearch"))

    @builtins.property
    @jsii.member(jsii_name="errorAction")
    def error_action(self) -> "IotTopicRuleErrorActionOutputReference":
        return typing.cast("IotTopicRuleErrorActionOutputReference", jsii.get(self, "errorAction"))

    @builtins.property
    @jsii.member(jsii_name="firehose")
    def firehose(self) -> "IotTopicRuleFirehoseList":
        return typing.cast("IotTopicRuleFirehoseList", jsii.get(self, "firehose"))

    @builtins.property
    @jsii.member(jsii_name="http")
    def http(self) -> "IotTopicRuleHttpList":
        return typing.cast("IotTopicRuleHttpList", jsii.get(self, "http"))

    @builtins.property
    @jsii.member(jsii_name="iotAnalytics")
    def iot_analytics(self) -> "IotTopicRuleIotAnalyticsList":
        return typing.cast("IotTopicRuleIotAnalyticsList", jsii.get(self, "iotAnalytics"))

    @builtins.property
    @jsii.member(jsii_name="iotEvents")
    def iot_events(self) -> "IotTopicRuleIotEventsList":
        return typing.cast("IotTopicRuleIotEventsList", jsii.get(self, "iotEvents"))

    @builtins.property
    @jsii.member(jsii_name="kafka")
    def kafka(self) -> "IotTopicRuleKafkaList":
        return typing.cast("IotTopicRuleKafkaList", jsii.get(self, "kafka"))

    @builtins.property
    @jsii.member(jsii_name="kinesis")
    def kinesis(self) -> "IotTopicRuleKinesisList":
        return typing.cast("IotTopicRuleKinesisList", jsii.get(self, "kinesis"))

    @builtins.property
    @jsii.member(jsii_name="lambda")
    def lambda_(self) -> "IotTopicRuleLambdaList":
        return typing.cast("IotTopicRuleLambdaList", jsii.get(self, "lambda"))

    @builtins.property
    @jsii.member(jsii_name="republish")
    def republish(self) -> "IotTopicRuleRepublishList":
        return typing.cast("IotTopicRuleRepublishList", jsii.get(self, "republish"))

    @builtins.property
    @jsii.member(jsii_name="s3")
    def s3(self) -> "IotTopicRuleS3List":
        return typing.cast("IotTopicRuleS3List", jsii.get(self, "s3"))

    @builtins.property
    @jsii.member(jsii_name="sns")
    def sns(self) -> "IotTopicRuleSnsList":
        return typing.cast("IotTopicRuleSnsList", jsii.get(self, "sns"))

    @builtins.property
    @jsii.member(jsii_name="sqs")
    def sqs(self) -> "IotTopicRuleSqsList":
        return typing.cast("IotTopicRuleSqsList", jsii.get(self, "sqs"))

    @builtins.property
    @jsii.member(jsii_name="stepFunctions")
    def step_functions(self) -> "IotTopicRuleStepFunctionsList":
        return typing.cast("IotTopicRuleStepFunctionsList", jsii.get(self, "stepFunctions"))

    @builtins.property
    @jsii.member(jsii_name="timestream")
    def timestream(self) -> "IotTopicRuleTimestreamList":
        return typing.cast("IotTopicRuleTimestreamList", jsii.get(self, "timestream"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchAlarmInput")
    def cloudwatch_alarm_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleCloudwatchAlarm"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleCloudwatchAlarm"]]], jsii.get(self, "cloudwatchAlarmInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogsInput")
    def cloudwatch_logs_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleCloudwatchLogs"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleCloudwatchLogs"]]], jsii.get(self, "cloudwatchLogsInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchMetricInput")
    def cloudwatch_metric_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleCloudwatchMetric"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleCloudwatchMetric"]]], jsii.get(self, "cloudwatchMetricInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="dynamodbInput")
    def dynamodb_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleDynamodb"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleDynamodb"]]], jsii.get(self, "dynamodbInput"))

    @builtins.property
    @jsii.member(jsii_name="dynamodbv2Input")
    def dynamodbv2_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleDynamodbv2"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleDynamodbv2"]]], jsii.get(self, "dynamodbv2Input"))

    @builtins.property
    @jsii.member(jsii_name="elasticsearchInput")
    def elasticsearch_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleElasticsearch"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleElasticsearch"]]], jsii.get(self, "elasticsearchInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="errorActionInput")
    def error_action_input(self) -> typing.Optional["IotTopicRuleErrorAction"]:
        return typing.cast(typing.Optional["IotTopicRuleErrorAction"], jsii.get(self, "errorActionInput"))

    @builtins.property
    @jsii.member(jsii_name="firehoseInput")
    def firehose_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleFirehose"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleFirehose"]]], jsii.get(self, "firehoseInput"))

    @builtins.property
    @jsii.member(jsii_name="httpInput")
    def http_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleHttp"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleHttp"]]], jsii.get(self, "httpInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="iotAnalyticsInput")
    def iot_analytics_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleIotAnalytics"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleIotAnalytics"]]], jsii.get(self, "iotAnalyticsInput"))

    @builtins.property
    @jsii.member(jsii_name="iotEventsInput")
    def iot_events_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleIotEvents"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleIotEvents"]]], jsii.get(self, "iotEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="kafkaInput")
    def kafka_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleKafka"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleKafka"]]], jsii.get(self, "kafkaInput"))

    @builtins.property
    @jsii.member(jsii_name="kinesisInput")
    def kinesis_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleKinesis"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleKinesis"]]], jsii.get(self, "kinesisInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaInput")
    def lambda_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleLambda"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleLambda"]]], jsii.get(self, "lambdaInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="republishInput")
    def republish_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleRepublish"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleRepublish"]]], jsii.get(self, "republishInput"))

    @builtins.property
    @jsii.member(jsii_name="s3Input")
    def s3_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleS3"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleS3"]]], jsii.get(self, "s3Input"))

    @builtins.property
    @jsii.member(jsii_name="snsInput")
    def sns_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleSns"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleSns"]]], jsii.get(self, "snsInput"))

    @builtins.property
    @jsii.member(jsii_name="sqlInput")
    def sql_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sqlInput"))

    @builtins.property
    @jsii.member(jsii_name="sqlVersionInput")
    def sql_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sqlVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="sqsInput")
    def sqs_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleSqs"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleSqs"]]], jsii.get(self, "sqsInput"))

    @builtins.property
    @jsii.member(jsii_name="stepFunctionsInput")
    def step_functions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleStepFunctions"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleStepFunctions"]]], jsii.get(self, "stepFunctionsInput"))

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
    @jsii.member(jsii_name="timestreamInput")
    def timestream_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleTimestream"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleTimestream"]]], jsii.get(self, "timestreamInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a0da180c557fdef7eeaf6d4b844e4dc9fbe666354f663cc3cc3e281f56e6077)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__1002bc4cffc024a4405efa40cce3cf0fc3b5b9866d2d8c14f74a0b7b9186a590)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2b0360bc44b65c198f54b15f5d937c1c567b77fde48b8aa97a28626dd672f9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2957c80c30e05362fcfdb576136858fc42869f97a541e75fb7cff3fadd1f6052)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sql")
    def sql(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sql"))

    @sql.setter
    def sql(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb8750cf5edda0dba5f823f79018bc9e0ff9f484e6f2f034eb9b28f221790a12)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sql", value)

    @builtins.property
    @jsii.member(jsii_name="sqlVersion")
    def sql_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sqlVersion"))

    @sql_version.setter
    def sql_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc07501312f7cdb84f4591fd4cced1bfa43432c2b16dc0a34dbdf49ec16d4489)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sqlVersion", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c82e9ef65111369fc0838abd2d439e2ceb2260e5bbab0595ec48dfc18abe1fff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8353f54931a3ea375dbae39671085de3b1d9dbeb5438a3f83d01952e5cc957f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleCloudwatchAlarm",
    jsii_struct_bases=[],
    name_mapping={
        "alarm_name": "alarmName",
        "role_arn": "roleArn",
        "state_reason": "stateReason",
        "state_value": "stateValue",
    },
)
class IotTopicRuleCloudwatchAlarm:
    def __init__(
        self,
        *,
        alarm_name: builtins.str,
        role_arn: builtins.str,
        state_reason: builtins.str,
        state_value: builtins.str,
    ) -> None:
        '''
        :param alarm_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#alarm_name IotTopicRule#alarm_name}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param state_reason: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#state_reason IotTopicRule#state_reason}.
        :param state_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#state_value IotTopicRule#state_value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa6578e7a9dfa1954c43c27b2392ffe8d3ff2e44e8e023c853dcfcd8446c5b49)
            check_type(argname="argument alarm_name", value=alarm_name, expected_type=type_hints["alarm_name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument state_reason", value=state_reason, expected_type=type_hints["state_reason"])
            check_type(argname="argument state_value", value=state_value, expected_type=type_hints["state_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "alarm_name": alarm_name,
            "role_arn": role_arn,
            "state_reason": state_reason,
            "state_value": state_value,
        }

    @builtins.property
    def alarm_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#alarm_name IotTopicRule#alarm_name}.'''
        result = self._values.get("alarm_name")
        assert result is not None, "Required property 'alarm_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def state_reason(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#state_reason IotTopicRule#state_reason}.'''
        result = self._values.get("state_reason")
        assert result is not None, "Required property 'state_reason' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def state_value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#state_value IotTopicRule#state_value}.'''
        result = self._values.get("state_value")
        assert result is not None, "Required property 'state_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleCloudwatchAlarm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleCloudwatchAlarmList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleCloudwatchAlarmList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__753d921f45aaa4a54d24f911c286ed849d6356f31893a6b1e1a36b733ab300f2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IotTopicRuleCloudwatchAlarmOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ce3c53a500fa317efdbc15cb8dadaa4551706db16fff5ff6bd293bc2868836c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IotTopicRuleCloudwatchAlarmOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88b8e66ea55a2fdbf22649da9087aefa1dfa56d1df9ce83415ca9261949f1c3d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6e83ac6a5f7be8da0eea80fdf8de7e2997ea7584057e9c3a9d9198e5116cbd5b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4102c2f52dba01eee128e192a176a7d09688b4783bc8b9022062767cd0aeb94b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleCloudwatchAlarm]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleCloudwatchAlarm]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleCloudwatchAlarm]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89872d1a0f337ab1974ec14a3b2bc04a68ca2b55c97649ec95566a2cfe38ee09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotTopicRuleCloudwatchAlarmOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleCloudwatchAlarmOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5e4b802d5a98a745397997e1a816e10646abc5dd0618f791e4d21fdff0949962)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="alarmNameInput")
    def alarm_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alarmNameInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="stateReasonInput")
    def state_reason_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateReasonInput"))

    @builtins.property
    @jsii.member(jsii_name="stateValueInput")
    def state_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateValueInput"))

    @builtins.property
    @jsii.member(jsii_name="alarmName")
    def alarm_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "alarmName"))

    @alarm_name.setter
    def alarm_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d02d2e84a547903ff847b9da4b074c1df42f15941205cfd39258ccf24518077b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alarmName", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39bd7145c97c0947f3e9252f9ff81e3818ce79bcb6afca61446bff76d01d5835)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="stateReason")
    def state_reason(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stateReason"))

    @state_reason.setter
    def state_reason(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d837777cf35bb33a82c72ed82f3346b8d41f096890bb521196e2252709115d5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stateReason", value)

    @builtins.property
    @jsii.member(jsii_name="stateValue")
    def state_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stateValue"))

    @state_value.setter
    def state_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f80ecae0ca2258dcd27bcda5e09972b418a04341ac2bfff923abe0e64b8cfd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stateValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IotTopicRuleCloudwatchAlarm, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IotTopicRuleCloudwatchAlarm, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IotTopicRuleCloudwatchAlarm, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1dc8964e123fceb289cb65b11575d258ca6f168aa51cb8988466d346fedf23df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleCloudwatchLogs",
    jsii_struct_bases=[],
    name_mapping={"log_group_name": "logGroupName", "role_arn": "roleArn"},
)
class IotTopicRuleCloudwatchLogs:
    def __init__(self, *, log_group_name: builtins.str, role_arn: builtins.str) -> None:
        '''
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#log_group_name IotTopicRule#log_group_name}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77878ec06107c8ff2f70638bcd84a18b18cfd86c2b86995f856d50cd36c302ff)
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "log_group_name": log_group_name,
            "role_arn": role_arn,
        }

    @builtins.property
    def log_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#log_group_name IotTopicRule#log_group_name}.'''
        result = self._values.get("log_group_name")
        assert result is not None, "Required property 'log_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleCloudwatchLogs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleCloudwatchLogsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleCloudwatchLogsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__52f6945e1ee95e5d5a7d56a97dbd58f577570b535e40ef9b6d7fc8b14d811047)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IotTopicRuleCloudwatchLogsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b48c398a6000ed19be64b3a7348384a21d6a9f8a068509c501f2ebb645fbbd4)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IotTopicRuleCloudwatchLogsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfb8c4a0e5d11e364cfcba923fa56365e13a83297987a9f35ef79b59db67d60c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ab660c414082a205ad00ab390c4135d800beceefef180028edf393ffc8e9254e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a4735b07201d8ad7bdeec1b7c1e8d744adfde2cde3e8d1e8c7e0c001d8a86346)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleCloudwatchLogs]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleCloudwatchLogs]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleCloudwatchLogs]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea4fb66286bae9d01c5aed5905ca8554f8441c97e15af8765109fa54b41d3492)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotTopicRuleCloudwatchLogsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleCloudwatchLogsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__85cd0ce1ad6e72cfb44d343bc59eaa4189b5d1d9826eca8edb596886d97d41da)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="logGroupNameInput")
    def log_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logGroupName"))

    @log_group_name.setter
    def log_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69fe600bf047ea635d46b2afc7c029d62df44a74598880367283aa99c4704943)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a355274c599434c80dfb9eb51afa5f74f8a3e02637c14c28b61c86b3a2cb600)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IotTopicRuleCloudwatchLogs, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IotTopicRuleCloudwatchLogs, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IotTopicRuleCloudwatchLogs, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf98daa05ee4b73ad6078c2d7ec46c29f92c5b4fd17fb6663a84194c390cba08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleCloudwatchMetric",
    jsii_struct_bases=[],
    name_mapping={
        "metric_name": "metricName",
        "metric_namespace": "metricNamespace",
        "metric_unit": "metricUnit",
        "metric_value": "metricValue",
        "role_arn": "roleArn",
        "metric_timestamp": "metricTimestamp",
    },
)
class IotTopicRuleCloudwatchMetric:
    def __init__(
        self,
        *,
        metric_name: builtins.str,
        metric_namespace: builtins.str,
        metric_unit: builtins.str,
        metric_value: builtins.str,
        role_arn: builtins.str,
        metric_timestamp: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#metric_name IotTopicRule#metric_name}.
        :param metric_namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#metric_namespace IotTopicRule#metric_namespace}.
        :param metric_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#metric_unit IotTopicRule#metric_unit}.
        :param metric_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#metric_value IotTopicRule#metric_value}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param metric_timestamp: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#metric_timestamp IotTopicRule#metric_timestamp}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fc19df14d506b09a7babef300bfea1e701e270c883f45a09f61d5d8169040d9)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument metric_namespace", value=metric_namespace, expected_type=type_hints["metric_namespace"])
            check_type(argname="argument metric_unit", value=metric_unit, expected_type=type_hints["metric_unit"])
            check_type(argname="argument metric_value", value=metric_value, expected_type=type_hints["metric_value"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument metric_timestamp", value=metric_timestamp, expected_type=type_hints["metric_timestamp"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metric_name": metric_name,
            "metric_namespace": metric_namespace,
            "metric_unit": metric_unit,
            "metric_value": metric_value,
            "role_arn": role_arn,
        }
        if metric_timestamp is not None:
            self._values["metric_timestamp"] = metric_timestamp

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#metric_name IotTopicRule#metric_name}.'''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def metric_namespace(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#metric_namespace IotTopicRule#metric_namespace}.'''
        result = self._values.get("metric_namespace")
        assert result is not None, "Required property 'metric_namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def metric_unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#metric_unit IotTopicRule#metric_unit}.'''
        result = self._values.get("metric_unit")
        assert result is not None, "Required property 'metric_unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def metric_value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#metric_value IotTopicRule#metric_value}.'''
        result = self._values.get("metric_value")
        assert result is not None, "Required property 'metric_value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def metric_timestamp(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#metric_timestamp IotTopicRule#metric_timestamp}.'''
        result = self._values.get("metric_timestamp")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleCloudwatchMetric(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleCloudwatchMetricList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleCloudwatchMetricList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bb3fb08a1312c7c68e7bed752c5c3834cf42d613bed55e6f5a601c94a3ac6066)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IotTopicRuleCloudwatchMetricOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c818d4716064284b2e398447f28cc0ec6a6c6d38ffa3827bad1f39ecf5240b3)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IotTopicRuleCloudwatchMetricOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c5110b499a6effa47b74225fb76ebc5b3c59d9ef36d85c683d5e35d45d2fdeb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bc5e62b93f0f2de780710befecbdeb98e372185d8ab354af9f05d07da0c33806)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2064795aa8e7ce4d9cdf88fb39bcaaccec151461eb495bc48797d79aab1d5407)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleCloudwatchMetric]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleCloudwatchMetric]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleCloudwatchMetric]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1aaf5e99a5f7244fef1b31477e976b77c1c6448fd28e62367dec01b151ee603)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotTopicRuleCloudwatchMetricOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleCloudwatchMetricOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3d2c3cbb27871e5eaf24a3d59dc4e26132f97808e6d855e1098200f17c7a5fda)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMetricTimestamp")
    def reset_metric_timestamp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricTimestamp", []))

    @builtins.property
    @jsii.member(jsii_name="metricNameInput")
    def metric_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricNameInput"))

    @builtins.property
    @jsii.member(jsii_name="metricNamespaceInput")
    def metric_namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricNamespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="metricTimestampInput")
    def metric_timestamp_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricTimestampInput"))

    @builtins.property
    @jsii.member(jsii_name="metricUnitInput")
    def metric_unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricUnitInput"))

    @builtins.property
    @jsii.member(jsii_name="metricValueInput")
    def metric_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricValueInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2e8c37309cffa76bbdfb03cff33d8c73557ec9b7b742821c197781b317fe3b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricName", value)

    @builtins.property
    @jsii.member(jsii_name="metricNamespace")
    def metric_namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricNamespace"))

    @metric_namespace.setter
    def metric_namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__407c038387911201db8e67ca268e127ec12f6131b9134cf5cad992291e4d48de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricNamespace", value)

    @builtins.property
    @jsii.member(jsii_name="metricTimestamp")
    def metric_timestamp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricTimestamp"))

    @metric_timestamp.setter
    def metric_timestamp(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cdaf86e150a38a6ae34d4600ce18a79e482308fc37dadcfbeae1f01457672a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricTimestamp", value)

    @builtins.property
    @jsii.member(jsii_name="metricUnit")
    def metric_unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricUnit"))

    @metric_unit.setter
    def metric_unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b8b2a8dc096928b8ed25db0305844693ea39d35970097649489d769415490e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricUnit", value)

    @builtins.property
    @jsii.member(jsii_name="metricValue")
    def metric_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricValue"))

    @metric_value.setter
    def metric_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c1ced0cf34ed15e1923e6c76668230036eca1c6b2cd5338ae6d557d24038917)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricValue", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8310817fdce28a1df7093af85d7cdf6144aa4c0795cdea082ca5355be3e55578)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IotTopicRuleCloudwatchMetric, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IotTopicRuleCloudwatchMetric, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IotTopicRuleCloudwatchMetric, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e3f9b80443e4fbcba16891695564d5602cb8ca7f4dc52807818febbb8b84292)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "enabled": "enabled",
        "name": "name",
        "sql": "sql",
        "sql_version": "sqlVersion",
        "cloudwatch_alarm": "cloudwatchAlarm",
        "cloudwatch_logs": "cloudwatchLogs",
        "cloudwatch_metric": "cloudwatchMetric",
        "description": "description",
        "dynamodb": "dynamodb",
        "dynamodbv2": "dynamodbv2",
        "elasticsearch": "elasticsearch",
        "error_action": "errorAction",
        "firehose": "firehose",
        "http": "http",
        "id": "id",
        "iot_analytics": "iotAnalytics",
        "iot_events": "iotEvents",
        "kafka": "kafka",
        "kinesis": "kinesis",
        "lambda_": "lambda",
        "republish": "republish",
        "s3": "s3",
        "sns": "sns",
        "sqs": "sqs",
        "step_functions": "stepFunctions",
        "tags": "tags",
        "tags_all": "tagsAll",
        "timestream": "timestream",
    },
)
class IotTopicRuleConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        name: builtins.str,
        sql: builtins.str,
        sql_version: builtins.str,
        cloudwatch_alarm: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleCloudwatchAlarm, typing.Dict[builtins.str, typing.Any]]]]] = None,
        cloudwatch_logs: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleCloudwatchLogs, typing.Dict[builtins.str, typing.Any]]]]] = None,
        cloudwatch_metric: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleCloudwatchMetric, typing.Dict[builtins.str, typing.Any]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        dynamodb: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleDynamodb", typing.Dict[builtins.str, typing.Any]]]]] = None,
        dynamodbv2: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleDynamodbv2", typing.Dict[builtins.str, typing.Any]]]]] = None,
        elasticsearch: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleElasticsearch", typing.Dict[builtins.str, typing.Any]]]]] = None,
        error_action: typing.Optional[typing.Union["IotTopicRuleErrorAction", typing.Dict[builtins.str, typing.Any]]] = None,
        firehose: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleFirehose", typing.Dict[builtins.str, typing.Any]]]]] = None,
        http: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleHttp", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        iot_analytics: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleIotAnalytics", typing.Dict[builtins.str, typing.Any]]]]] = None,
        iot_events: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleIotEvents", typing.Dict[builtins.str, typing.Any]]]]] = None,
        kafka: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleKafka", typing.Dict[builtins.str, typing.Any]]]]] = None,
        kinesis: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleKinesis", typing.Dict[builtins.str, typing.Any]]]]] = None,
        lambda_: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleLambda", typing.Dict[builtins.str, typing.Any]]]]] = None,
        republish: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleRepublish", typing.Dict[builtins.str, typing.Any]]]]] = None,
        s3: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleS3", typing.Dict[builtins.str, typing.Any]]]]] = None,
        sns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleSns", typing.Dict[builtins.str, typing.Any]]]]] = None,
        sqs: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleSqs", typing.Dict[builtins.str, typing.Any]]]]] = None,
        step_functions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleStepFunctions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timestream: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleTimestream", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#enabled IotTopicRule#enabled}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#name IotTopicRule#name}.
        :param sql: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#sql IotTopicRule#sql}.
        :param sql_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#sql_version IotTopicRule#sql_version}.
        :param cloudwatch_alarm: cloudwatch_alarm block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#cloudwatch_alarm IotTopicRule#cloudwatch_alarm}
        :param cloudwatch_logs: cloudwatch_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#cloudwatch_logs IotTopicRule#cloudwatch_logs}
        :param cloudwatch_metric: cloudwatch_metric block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#cloudwatch_metric IotTopicRule#cloudwatch_metric}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#description IotTopicRule#description}.
        :param dynamodb: dynamodb block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#dynamodb IotTopicRule#dynamodb}
        :param dynamodbv2: dynamodbv2 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#dynamodbv2 IotTopicRule#dynamodbv2}
        :param elasticsearch: elasticsearch block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#elasticsearch IotTopicRule#elasticsearch}
        :param error_action: error_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#error_action IotTopicRule#error_action}
        :param firehose: firehose block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#firehose IotTopicRule#firehose}
        :param http: http block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#http IotTopicRule#http}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#id IotTopicRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param iot_analytics: iot_analytics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#iot_analytics IotTopicRule#iot_analytics}
        :param iot_events: iot_events block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#iot_events IotTopicRule#iot_events}
        :param kafka: kafka block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#kafka IotTopicRule#kafka}
        :param kinesis: kinesis block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#kinesis IotTopicRule#kinesis}
        :param lambda_: lambda block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#lambda IotTopicRule#lambda}
        :param republish: republish block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#republish IotTopicRule#republish}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#s3 IotTopicRule#s3}
        :param sns: sns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#sns IotTopicRule#sns}
        :param sqs: sqs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#sqs IotTopicRule#sqs}
        :param step_functions: step_functions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#step_functions IotTopicRule#step_functions}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#tags IotTopicRule#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#tags_all IotTopicRule#tags_all}.
        :param timestream: timestream block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#timestream IotTopicRule#timestream}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(error_action, dict):
            error_action = IotTopicRuleErrorAction(**error_action)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9d70340d517c3df6cbffd33caef093f6c567a8b19e7c9bbe31bf883bee3ca1b)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument sql", value=sql, expected_type=type_hints["sql"])
            check_type(argname="argument sql_version", value=sql_version, expected_type=type_hints["sql_version"])
            check_type(argname="argument cloudwatch_alarm", value=cloudwatch_alarm, expected_type=type_hints["cloudwatch_alarm"])
            check_type(argname="argument cloudwatch_logs", value=cloudwatch_logs, expected_type=type_hints["cloudwatch_logs"])
            check_type(argname="argument cloudwatch_metric", value=cloudwatch_metric, expected_type=type_hints["cloudwatch_metric"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument dynamodb", value=dynamodb, expected_type=type_hints["dynamodb"])
            check_type(argname="argument dynamodbv2", value=dynamodbv2, expected_type=type_hints["dynamodbv2"])
            check_type(argname="argument elasticsearch", value=elasticsearch, expected_type=type_hints["elasticsearch"])
            check_type(argname="argument error_action", value=error_action, expected_type=type_hints["error_action"])
            check_type(argname="argument firehose", value=firehose, expected_type=type_hints["firehose"])
            check_type(argname="argument http", value=http, expected_type=type_hints["http"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument iot_analytics", value=iot_analytics, expected_type=type_hints["iot_analytics"])
            check_type(argname="argument iot_events", value=iot_events, expected_type=type_hints["iot_events"])
            check_type(argname="argument kafka", value=kafka, expected_type=type_hints["kafka"])
            check_type(argname="argument kinesis", value=kinesis, expected_type=type_hints["kinesis"])
            check_type(argname="argument lambda_", value=lambda_, expected_type=type_hints["lambda_"])
            check_type(argname="argument republish", value=republish, expected_type=type_hints["republish"])
            check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
            check_type(argname="argument sns", value=sns, expected_type=type_hints["sns"])
            check_type(argname="argument sqs", value=sqs, expected_type=type_hints["sqs"])
            check_type(argname="argument step_functions", value=step_functions, expected_type=type_hints["step_functions"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument timestream", value=timestream, expected_type=type_hints["timestream"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled": enabled,
            "name": name,
            "sql": sql,
            "sql_version": sql_version,
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
        if cloudwatch_alarm is not None:
            self._values["cloudwatch_alarm"] = cloudwatch_alarm
        if cloudwatch_logs is not None:
            self._values["cloudwatch_logs"] = cloudwatch_logs
        if cloudwatch_metric is not None:
            self._values["cloudwatch_metric"] = cloudwatch_metric
        if description is not None:
            self._values["description"] = description
        if dynamodb is not None:
            self._values["dynamodb"] = dynamodb
        if dynamodbv2 is not None:
            self._values["dynamodbv2"] = dynamodbv2
        if elasticsearch is not None:
            self._values["elasticsearch"] = elasticsearch
        if error_action is not None:
            self._values["error_action"] = error_action
        if firehose is not None:
            self._values["firehose"] = firehose
        if http is not None:
            self._values["http"] = http
        if id is not None:
            self._values["id"] = id
        if iot_analytics is not None:
            self._values["iot_analytics"] = iot_analytics
        if iot_events is not None:
            self._values["iot_events"] = iot_events
        if kafka is not None:
            self._values["kafka"] = kafka
        if kinesis is not None:
            self._values["kinesis"] = kinesis
        if lambda_ is not None:
            self._values["lambda_"] = lambda_
        if republish is not None:
            self._values["republish"] = republish
        if s3 is not None:
            self._values["s3"] = s3
        if sns is not None:
            self._values["sns"] = sns
        if sqs is not None:
            self._values["sqs"] = sqs
        if step_functions is not None:
            self._values["step_functions"] = step_functions
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if timestream is not None:
            self._values["timestream"] = timestream

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
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#enabled IotTopicRule#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#name IotTopicRule#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sql(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#sql IotTopicRule#sql}.'''
        result = self._values.get("sql")
        assert result is not None, "Required property 'sql' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sql_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#sql_version IotTopicRule#sql_version}.'''
        result = self._values.get("sql_version")
        assert result is not None, "Required property 'sql_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cloudwatch_alarm(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleCloudwatchAlarm]]]:
        '''cloudwatch_alarm block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#cloudwatch_alarm IotTopicRule#cloudwatch_alarm}
        '''
        result = self._values.get("cloudwatch_alarm")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleCloudwatchAlarm]]], result)

    @builtins.property
    def cloudwatch_logs(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleCloudwatchLogs]]]:
        '''cloudwatch_logs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#cloudwatch_logs IotTopicRule#cloudwatch_logs}
        '''
        result = self._values.get("cloudwatch_logs")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleCloudwatchLogs]]], result)

    @builtins.property
    def cloudwatch_metric(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleCloudwatchMetric]]]:
        '''cloudwatch_metric block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#cloudwatch_metric IotTopicRule#cloudwatch_metric}
        '''
        result = self._values.get("cloudwatch_metric")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleCloudwatchMetric]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#description IotTopicRule#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dynamodb(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleDynamodb"]]]:
        '''dynamodb block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#dynamodb IotTopicRule#dynamodb}
        '''
        result = self._values.get("dynamodb")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleDynamodb"]]], result)

    @builtins.property
    def dynamodbv2(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleDynamodbv2"]]]:
        '''dynamodbv2 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#dynamodbv2 IotTopicRule#dynamodbv2}
        '''
        result = self._values.get("dynamodbv2")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleDynamodbv2"]]], result)

    @builtins.property
    def elasticsearch(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleElasticsearch"]]]:
        '''elasticsearch block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#elasticsearch IotTopicRule#elasticsearch}
        '''
        result = self._values.get("elasticsearch")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleElasticsearch"]]], result)

    @builtins.property
    def error_action(self) -> typing.Optional["IotTopicRuleErrorAction"]:
        '''error_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#error_action IotTopicRule#error_action}
        '''
        result = self._values.get("error_action")
        return typing.cast(typing.Optional["IotTopicRuleErrorAction"], result)

    @builtins.property
    def firehose(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleFirehose"]]]:
        '''firehose block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#firehose IotTopicRule#firehose}
        '''
        result = self._values.get("firehose")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleFirehose"]]], result)

    @builtins.property
    def http(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleHttp"]]]:
        '''http block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#http IotTopicRule#http}
        '''
        result = self._values.get("http")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleHttp"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#id IotTopicRule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iot_analytics(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleIotAnalytics"]]]:
        '''iot_analytics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#iot_analytics IotTopicRule#iot_analytics}
        '''
        result = self._values.get("iot_analytics")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleIotAnalytics"]]], result)

    @builtins.property
    def iot_events(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleIotEvents"]]]:
        '''iot_events block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#iot_events IotTopicRule#iot_events}
        '''
        result = self._values.get("iot_events")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleIotEvents"]]], result)

    @builtins.property
    def kafka(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleKafka"]]]:
        '''kafka block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#kafka IotTopicRule#kafka}
        '''
        result = self._values.get("kafka")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleKafka"]]], result)

    @builtins.property
    def kinesis(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleKinesis"]]]:
        '''kinesis block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#kinesis IotTopicRule#kinesis}
        '''
        result = self._values.get("kinesis")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleKinesis"]]], result)

    @builtins.property
    def lambda_(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleLambda"]]]:
        '''lambda block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#lambda IotTopicRule#lambda}
        '''
        result = self._values.get("lambda_")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleLambda"]]], result)

    @builtins.property
    def republish(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleRepublish"]]]:
        '''republish block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#republish IotTopicRule#republish}
        '''
        result = self._values.get("republish")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleRepublish"]]], result)

    @builtins.property
    def s3(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleS3"]]]:
        '''s3 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#s3 IotTopicRule#s3}
        '''
        result = self._values.get("s3")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleS3"]]], result)

    @builtins.property
    def sns(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleSns"]]]:
        '''sns block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#sns IotTopicRule#sns}
        '''
        result = self._values.get("sns")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleSns"]]], result)

    @builtins.property
    def sqs(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleSqs"]]]:
        '''sqs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#sqs IotTopicRule#sqs}
        '''
        result = self._values.get("sqs")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleSqs"]]], result)

    @builtins.property
    def step_functions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleStepFunctions"]]]:
        '''step_functions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#step_functions IotTopicRule#step_functions}
        '''
        result = self._values.get("step_functions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleStepFunctions"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#tags IotTopicRule#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#tags_all IotTopicRule#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timestream(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleTimestream"]]]:
        '''timestream block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#timestream IotTopicRule#timestream}
        '''
        result = self._values.get("timestream")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleTimestream"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleDynamodb",
    jsii_struct_bases=[],
    name_mapping={
        "hash_key_field": "hashKeyField",
        "hash_key_value": "hashKeyValue",
        "role_arn": "roleArn",
        "table_name": "tableName",
        "hash_key_type": "hashKeyType",
        "operation": "operation",
        "payload_field": "payloadField",
        "range_key_field": "rangeKeyField",
        "range_key_type": "rangeKeyType",
        "range_key_value": "rangeKeyValue",
    },
)
class IotTopicRuleDynamodb:
    def __init__(
        self,
        *,
        hash_key_field: builtins.str,
        hash_key_value: builtins.str,
        role_arn: builtins.str,
        table_name: builtins.str,
        hash_key_type: typing.Optional[builtins.str] = None,
        operation: typing.Optional[builtins.str] = None,
        payload_field: typing.Optional[builtins.str] = None,
        range_key_field: typing.Optional[builtins.str] = None,
        range_key_type: typing.Optional[builtins.str] = None,
        range_key_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param hash_key_field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#hash_key_field IotTopicRule#hash_key_field}.
        :param hash_key_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#hash_key_value IotTopicRule#hash_key_value}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#table_name IotTopicRule#table_name}.
        :param hash_key_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#hash_key_type IotTopicRule#hash_key_type}.
        :param operation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#operation IotTopicRule#operation}.
        :param payload_field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#payload_field IotTopicRule#payload_field}.
        :param range_key_field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#range_key_field IotTopicRule#range_key_field}.
        :param range_key_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#range_key_type IotTopicRule#range_key_type}.
        :param range_key_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#range_key_value IotTopicRule#range_key_value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7168d3679fc39a00d05b9c84bf630a35da1206894e472ca8c0514f3989afd06)
            check_type(argname="argument hash_key_field", value=hash_key_field, expected_type=type_hints["hash_key_field"])
            check_type(argname="argument hash_key_value", value=hash_key_value, expected_type=type_hints["hash_key_value"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            check_type(argname="argument hash_key_type", value=hash_key_type, expected_type=type_hints["hash_key_type"])
            check_type(argname="argument operation", value=operation, expected_type=type_hints["operation"])
            check_type(argname="argument payload_field", value=payload_field, expected_type=type_hints["payload_field"])
            check_type(argname="argument range_key_field", value=range_key_field, expected_type=type_hints["range_key_field"])
            check_type(argname="argument range_key_type", value=range_key_type, expected_type=type_hints["range_key_type"])
            check_type(argname="argument range_key_value", value=range_key_value, expected_type=type_hints["range_key_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "hash_key_field": hash_key_field,
            "hash_key_value": hash_key_value,
            "role_arn": role_arn,
            "table_name": table_name,
        }
        if hash_key_type is not None:
            self._values["hash_key_type"] = hash_key_type
        if operation is not None:
            self._values["operation"] = operation
        if payload_field is not None:
            self._values["payload_field"] = payload_field
        if range_key_field is not None:
            self._values["range_key_field"] = range_key_field
        if range_key_type is not None:
            self._values["range_key_type"] = range_key_type
        if range_key_value is not None:
            self._values["range_key_value"] = range_key_value

    @builtins.property
    def hash_key_field(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#hash_key_field IotTopicRule#hash_key_field}.'''
        result = self._values.get("hash_key_field")
        assert result is not None, "Required property 'hash_key_field' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def hash_key_value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#hash_key_value IotTopicRule#hash_key_value}.'''
        result = self._values.get("hash_key_value")
        assert result is not None, "Required property 'hash_key_value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#table_name IotTopicRule#table_name}.'''
        result = self._values.get("table_name")
        assert result is not None, "Required property 'table_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def hash_key_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#hash_key_type IotTopicRule#hash_key_type}.'''
        result = self._values.get("hash_key_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operation(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#operation IotTopicRule#operation}.'''
        result = self._values.get("operation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def payload_field(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#payload_field IotTopicRule#payload_field}.'''
        result = self._values.get("payload_field")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def range_key_field(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#range_key_field IotTopicRule#range_key_field}.'''
        result = self._values.get("range_key_field")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def range_key_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#range_key_type IotTopicRule#range_key_type}.'''
        result = self._values.get("range_key_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def range_key_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#range_key_value IotTopicRule#range_key_value}.'''
        result = self._values.get("range_key_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleDynamodb(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleDynamodbList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleDynamodbList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2134c403e97e260a14f2c7bf393588becfc649418c1d54520dd8808960ca0e9b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IotTopicRuleDynamodbOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__403b7e127ecf245edb710ae3b76c79c8c7e98b40d0e238a2c7aa9e804a0f9e93)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IotTopicRuleDynamodbOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b006433caa3f6896f1b81b248c58281d2f5d012b7ead671a94bf8228bfe177f3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2d7917cf90a20a2a0291ec8c9360db8b5bb9ba9b3a4a0a9b857e5eea8e54ce7c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2d52832234efabdde1aed0f22777ee019f585f0a02de1887f7d914d3ec72cc41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleDynamodb]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleDynamodb]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleDynamodb]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e9524eb32e582ce99b890041e7d9970d40f0f31d11619f7498ca61def010d86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotTopicRuleDynamodbOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleDynamodbOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4bf15a74fdfdd0c0e9480d715fb2918ee88e135393ca473bc8b2b32b32c91267)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetHashKeyType")
    def reset_hash_key_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHashKeyType", []))

    @jsii.member(jsii_name="resetOperation")
    def reset_operation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperation", []))

    @jsii.member(jsii_name="resetPayloadField")
    def reset_payload_field(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPayloadField", []))

    @jsii.member(jsii_name="resetRangeKeyField")
    def reset_range_key_field(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRangeKeyField", []))

    @jsii.member(jsii_name="resetRangeKeyType")
    def reset_range_key_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRangeKeyType", []))

    @jsii.member(jsii_name="resetRangeKeyValue")
    def reset_range_key_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRangeKeyValue", []))

    @builtins.property
    @jsii.member(jsii_name="hashKeyFieldInput")
    def hash_key_field_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hashKeyFieldInput"))

    @builtins.property
    @jsii.member(jsii_name="hashKeyTypeInput")
    def hash_key_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hashKeyTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="hashKeyValueInput")
    def hash_key_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hashKeyValueInput"))

    @builtins.property
    @jsii.member(jsii_name="operationInput")
    def operation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operationInput"))

    @builtins.property
    @jsii.member(jsii_name="payloadFieldInput")
    def payload_field_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "payloadFieldInput"))

    @builtins.property
    @jsii.member(jsii_name="rangeKeyFieldInput")
    def range_key_field_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rangeKeyFieldInput"))

    @builtins.property
    @jsii.member(jsii_name="rangeKeyTypeInput")
    def range_key_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rangeKeyTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="rangeKeyValueInput")
    def range_key_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rangeKeyValueInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="tableNameInput")
    def table_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableNameInput"))

    @builtins.property
    @jsii.member(jsii_name="hashKeyField")
    def hash_key_field(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hashKeyField"))

    @hash_key_field.setter
    def hash_key_field(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19af3e81e0d2ff304b1be9d72559cff3ecd2350a36fa9c30be34c5396b2d0573)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hashKeyField", value)

    @builtins.property
    @jsii.member(jsii_name="hashKeyType")
    def hash_key_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hashKeyType"))

    @hash_key_type.setter
    def hash_key_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3790184367f5b747e25d4d28974c61070a89827931128f64cf6d4285e373ed32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hashKeyType", value)

    @builtins.property
    @jsii.member(jsii_name="hashKeyValue")
    def hash_key_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hashKeyValue"))

    @hash_key_value.setter
    def hash_key_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e19087e0282dd8d7ad40e755dd87b94471576ede770846dffdbde480e90dea2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hashKeyValue", value)

    @builtins.property
    @jsii.member(jsii_name="operation")
    def operation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operation"))

    @operation.setter
    def operation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f6ad81e6704a85d554c62e6a49952b7c920832f8099f9af6e68368f1975bd37)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operation", value)

    @builtins.property
    @jsii.member(jsii_name="payloadField")
    def payload_field(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "payloadField"))

    @payload_field.setter
    def payload_field(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1f99a9d65cf0c80ed36f1cd6d5b69970cd86d3b95cae9c24dca75f2d55731f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "payloadField", value)

    @builtins.property
    @jsii.member(jsii_name="rangeKeyField")
    def range_key_field(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rangeKeyField"))

    @range_key_field.setter
    def range_key_field(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56dd2b6e9e60e6987c596b81d994c5da595803898ba7783cc0ea5ca0ec3abda9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rangeKeyField", value)

    @builtins.property
    @jsii.member(jsii_name="rangeKeyType")
    def range_key_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rangeKeyType"))

    @range_key_type.setter
    def range_key_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7605f00e39ba137f9df772dac57545a791f3ec9b807925cfeff4a51469ef71e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rangeKeyType", value)

    @builtins.property
    @jsii.member(jsii_name="rangeKeyValue")
    def range_key_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rangeKeyValue"))

    @range_key_value.setter
    def range_key_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4983ad451b955928ccf6bd4d0726fcade83e284d833fa3f0b7bf7f61fddd2000)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rangeKeyValue", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14b9d86bfa1a934051396e423dd763dbeca7c327c2b30f5648a01c286be77119)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="tableName")
    def table_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableName"))

    @table_name.setter
    def table_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8134ab94f715a3a6eeac04dba2c632d3695f93cdf144879f397639aa24c2e5e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IotTopicRuleDynamodb, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IotTopicRuleDynamodb, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IotTopicRuleDynamodb, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27ff570101a9d4cbd8223f59b87606e8ffbc29faa996b4d46c16101412de569a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleDynamodbv2",
    jsii_struct_bases=[],
    name_mapping={"role_arn": "roleArn", "put_item": "putItem"},
)
class IotTopicRuleDynamodbv2:
    def __init__(
        self,
        *,
        role_arn: builtins.str,
        put_item: typing.Optional[typing.Union["IotTopicRuleDynamodbv2PutItem", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param put_item: put_item block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#put_item IotTopicRule#put_item}
        '''
        if isinstance(put_item, dict):
            put_item = IotTopicRuleDynamodbv2PutItem(**put_item)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__461e0f79f63936d7557e6f647a002b1fa65e7cf4bf0c73d7807bfce3cdf9b6d3)
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument put_item", value=put_item, expected_type=type_hints["put_item"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "role_arn": role_arn,
        }
        if put_item is not None:
            self._values["put_item"] = put_item

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def put_item(self) -> typing.Optional["IotTopicRuleDynamodbv2PutItem"]:
        '''put_item block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#put_item IotTopicRule#put_item}
        '''
        result = self._values.get("put_item")
        return typing.cast(typing.Optional["IotTopicRuleDynamodbv2PutItem"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleDynamodbv2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleDynamodbv2List(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleDynamodbv2List",
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
            type_hints = typing.get_type_hints(_typecheckingstub__37cd868a16008764a802191ff88965dc05770c131257c746e239b2d7c95863ee)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IotTopicRuleDynamodbv2OutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4640c34ec3cf29c7173c791e0aa614102e6c2a7c087b27177ea93e5ca6beb131)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IotTopicRuleDynamodbv2OutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ffd2db82491f4d3b10a5396d666e9b0b721ccd8543058386f006102882998b6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ef1209fbd779a24ef2b17d3b9cd8b4df69bbb972267c9673b2f911677f0126a0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5815cba23c65b62f3e87b7cb909dcd687ea3638143424467f885d490b5c88ca7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleDynamodbv2]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleDynamodbv2]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleDynamodbv2]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c272c76ef80f9e716b261ca8e7972cff8d1159208238cc182b665a05c9c0fb88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotTopicRuleDynamodbv2OutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleDynamodbv2OutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4302f82f4c192b8763ceed4d9c6c7be88eb235dac6a8d86c4c6f9dfadbd22c39)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putPutItem")
    def put_put_item(self, *, table_name: builtins.str) -> None:
        '''
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#table_name IotTopicRule#table_name}.
        '''
        value = IotTopicRuleDynamodbv2PutItem(table_name=table_name)

        return typing.cast(None, jsii.invoke(self, "putPutItem", [value]))

    @jsii.member(jsii_name="resetPutItem")
    def reset_put_item(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPutItem", []))

    @builtins.property
    @jsii.member(jsii_name="putItem")
    def put_item(self) -> "IotTopicRuleDynamodbv2PutItemOutputReference":
        return typing.cast("IotTopicRuleDynamodbv2PutItemOutputReference", jsii.get(self, "putItem"))

    @builtins.property
    @jsii.member(jsii_name="putItemInput")
    def put_item_input(self) -> typing.Optional["IotTopicRuleDynamodbv2PutItem"]:
        return typing.cast(typing.Optional["IotTopicRuleDynamodbv2PutItem"], jsii.get(self, "putItemInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__537faa0ca32d8a2044a8c3eddd9bf7199e80812ed299b6e677c452d57683573f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IotTopicRuleDynamodbv2, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IotTopicRuleDynamodbv2, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IotTopicRuleDynamodbv2, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41d816fc8c85f675c3027619f72b1a2b08d8e885848e4a4066811a8b6236e4b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleDynamodbv2PutItem",
    jsii_struct_bases=[],
    name_mapping={"table_name": "tableName"},
)
class IotTopicRuleDynamodbv2PutItem:
    def __init__(self, *, table_name: builtins.str) -> None:
        '''
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#table_name IotTopicRule#table_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecfe3f60378be9e4c952a6d8e753c3c6a9ff73737d93f9b1566dbe3f9cb9e52e)
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "table_name": table_name,
        }

    @builtins.property
    def table_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#table_name IotTopicRule#table_name}.'''
        result = self._values.get("table_name")
        assert result is not None, "Required property 'table_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleDynamodbv2PutItem(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleDynamodbv2PutItemOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleDynamodbv2PutItemOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__abef44bd47ae26ba5dfee9ce94408ba25465c037f459662c2af52553b2afe180)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="tableNameInput")
    def table_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tableName")
    def table_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableName"))

    @table_name.setter
    def table_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a579d15d9ddb5df870fdfbf56c2490a11967f5845c831c80793ac3551832c2cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IotTopicRuleDynamodbv2PutItem]:
        return typing.cast(typing.Optional[IotTopicRuleDynamodbv2PutItem], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IotTopicRuleDynamodbv2PutItem],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d9b22ae856685676de0738bdfa04e7767e3556d4ad607ba021ebf93d13c5126)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleElasticsearch",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint": "endpoint",
        "id": "id",
        "index": "index",
        "role_arn": "roleArn",
        "type": "type",
    },
)
class IotTopicRuleElasticsearch:
    def __init__(
        self,
        *,
        endpoint: builtins.str,
        id: builtins.str,
        index: builtins.str,
        role_arn: builtins.str,
        type: builtins.str,
    ) -> None:
        '''
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#endpoint IotTopicRule#endpoint}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#id IotTopicRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param index: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#index IotTopicRule#index}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#type IotTopicRule#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__640d10f72f2c09f86f2b845a53d980dd19a83a99d3ab81f5a03638ed3e384cb7)
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoint": endpoint,
            "id": id,
            "index": index,
            "role_arn": role_arn,
            "type": type,
        }

    @builtins.property
    def endpoint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#endpoint IotTopicRule#endpoint}.'''
        result = self._values.get("endpoint")
        assert result is not None, "Required property 'endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#id IotTopicRule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def index(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#index IotTopicRule#index}.'''
        result = self._values.get("index")
        assert result is not None, "Required property 'index' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#type IotTopicRule#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleElasticsearch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleElasticsearchList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleElasticsearchList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__13cf2500de0c8745a8c40ef2231b9db85c7c4468de88fa5c9f226974be427983)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IotTopicRuleElasticsearchOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c4d3a888bec13007eaa5673f5368421cb8e8a7bb0e471569f8be9e4f369ef56)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IotTopicRuleElasticsearchOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6779b4aafbb26c29339254c0c21f11a160ae302328cd467e63bef2951926dd8c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8a650e86d70051bdd8ae92d453c303063c132ded47384c5f0d06c3ee714e4dfe)
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
            type_hints = typing.get_type_hints(_typecheckingstub__340fdab86a4054fbe2427a990b3a9dd8f2f68e9e474ce587ccb6e0073f59419e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleElasticsearch]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleElasticsearch]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleElasticsearch]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d185d41cdd4e23f500ff700aafdcfc5ecb010b2a7e1b5cecf099c1acbb8a79ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotTopicRuleElasticsearchOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleElasticsearchOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__53f1d8ed764152e3b275887b8982054ee3de80fc7b8c7eba6e1157d2aecd5bad)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="indexInput")
    def index_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "indexInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ff4d031519a8e78475d8a5b926b75859d5b02f511c0ac1c940bff85fbf820d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93297e1922cf222d064dbd7fbd308a22f5c6715bb3de108276f8b14d04c5a770)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="index")
    def index(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "index"))

    @index.setter
    def index(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__698dfc00ae40e9313c9bc1de4fa2b12cd75859ef6dd49cb87079f6e9a494155e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "index", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17707daa507b75ec0ddfa76f41e35d40ab007da9ba584a6c73fb873952a98f30)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19156c7e511163771b3f35456612b5931c62689c761a00cd8cab6c835d8197f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IotTopicRuleElasticsearch, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IotTopicRuleElasticsearch, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IotTopicRuleElasticsearch, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94c26aa947bc35d7d0ab831ebd6b500adf64965f228989922121db70a4a1663d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorAction",
    jsii_struct_bases=[],
    name_mapping={
        "cloudwatch_alarm": "cloudwatchAlarm",
        "cloudwatch_logs": "cloudwatchLogs",
        "cloudwatch_metric": "cloudwatchMetric",
        "dynamodb": "dynamodb",
        "dynamodbv2": "dynamodbv2",
        "elasticsearch": "elasticsearch",
        "firehose": "firehose",
        "http": "http",
        "iot_analytics": "iotAnalytics",
        "iot_events": "iotEvents",
        "kafka": "kafka",
        "kinesis": "kinesis",
        "lambda_": "lambda",
        "republish": "republish",
        "s3": "s3",
        "sns": "sns",
        "sqs": "sqs",
        "step_functions": "stepFunctions",
        "timestream": "timestream",
    },
)
class IotTopicRuleErrorAction:
    def __init__(
        self,
        *,
        cloudwatch_alarm: typing.Optional[typing.Union["IotTopicRuleErrorActionCloudwatchAlarm", typing.Dict[builtins.str, typing.Any]]] = None,
        cloudwatch_logs: typing.Optional[typing.Union["IotTopicRuleErrorActionCloudwatchLogs", typing.Dict[builtins.str, typing.Any]]] = None,
        cloudwatch_metric: typing.Optional[typing.Union["IotTopicRuleErrorActionCloudwatchMetric", typing.Dict[builtins.str, typing.Any]]] = None,
        dynamodb: typing.Optional[typing.Union["IotTopicRuleErrorActionDynamodb", typing.Dict[builtins.str, typing.Any]]] = None,
        dynamodbv2: typing.Optional[typing.Union["IotTopicRuleErrorActionDynamodbv2", typing.Dict[builtins.str, typing.Any]]] = None,
        elasticsearch: typing.Optional[typing.Union["IotTopicRuleErrorActionElasticsearch", typing.Dict[builtins.str, typing.Any]]] = None,
        firehose: typing.Optional[typing.Union["IotTopicRuleErrorActionFirehose", typing.Dict[builtins.str, typing.Any]]] = None,
        http: typing.Optional[typing.Union["IotTopicRuleErrorActionHttp", typing.Dict[builtins.str, typing.Any]]] = None,
        iot_analytics: typing.Optional[typing.Union["IotTopicRuleErrorActionIotAnalytics", typing.Dict[builtins.str, typing.Any]]] = None,
        iot_events: typing.Optional[typing.Union["IotTopicRuleErrorActionIotEvents", typing.Dict[builtins.str, typing.Any]]] = None,
        kafka: typing.Optional[typing.Union["IotTopicRuleErrorActionKafka", typing.Dict[builtins.str, typing.Any]]] = None,
        kinesis: typing.Optional[typing.Union["IotTopicRuleErrorActionKinesis", typing.Dict[builtins.str, typing.Any]]] = None,
        lambda_: typing.Optional[typing.Union["IotTopicRuleErrorActionLambda", typing.Dict[builtins.str, typing.Any]]] = None,
        republish: typing.Optional[typing.Union["IotTopicRuleErrorActionRepublish", typing.Dict[builtins.str, typing.Any]]] = None,
        s3: typing.Optional[typing.Union["IotTopicRuleErrorActionS3", typing.Dict[builtins.str, typing.Any]]] = None,
        sns: typing.Optional[typing.Union["IotTopicRuleErrorActionSns", typing.Dict[builtins.str, typing.Any]]] = None,
        sqs: typing.Optional[typing.Union["IotTopicRuleErrorActionSqs", typing.Dict[builtins.str, typing.Any]]] = None,
        step_functions: typing.Optional[typing.Union["IotTopicRuleErrorActionStepFunctions", typing.Dict[builtins.str, typing.Any]]] = None,
        timestream: typing.Optional[typing.Union["IotTopicRuleErrorActionTimestream", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param cloudwatch_alarm: cloudwatch_alarm block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#cloudwatch_alarm IotTopicRule#cloudwatch_alarm}
        :param cloudwatch_logs: cloudwatch_logs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#cloudwatch_logs IotTopicRule#cloudwatch_logs}
        :param cloudwatch_metric: cloudwatch_metric block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#cloudwatch_metric IotTopicRule#cloudwatch_metric}
        :param dynamodb: dynamodb block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#dynamodb IotTopicRule#dynamodb}
        :param dynamodbv2: dynamodbv2 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#dynamodbv2 IotTopicRule#dynamodbv2}
        :param elasticsearch: elasticsearch block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#elasticsearch IotTopicRule#elasticsearch}
        :param firehose: firehose block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#firehose IotTopicRule#firehose}
        :param http: http block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#http IotTopicRule#http}
        :param iot_analytics: iot_analytics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#iot_analytics IotTopicRule#iot_analytics}
        :param iot_events: iot_events block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#iot_events IotTopicRule#iot_events}
        :param kafka: kafka block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#kafka IotTopicRule#kafka}
        :param kinesis: kinesis block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#kinesis IotTopicRule#kinesis}
        :param lambda_: lambda block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#lambda IotTopicRule#lambda}
        :param republish: republish block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#republish IotTopicRule#republish}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#s3 IotTopicRule#s3}
        :param sns: sns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#sns IotTopicRule#sns}
        :param sqs: sqs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#sqs IotTopicRule#sqs}
        :param step_functions: step_functions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#step_functions IotTopicRule#step_functions}
        :param timestream: timestream block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#timestream IotTopicRule#timestream}
        '''
        if isinstance(cloudwatch_alarm, dict):
            cloudwatch_alarm = IotTopicRuleErrorActionCloudwatchAlarm(**cloudwatch_alarm)
        if isinstance(cloudwatch_logs, dict):
            cloudwatch_logs = IotTopicRuleErrorActionCloudwatchLogs(**cloudwatch_logs)
        if isinstance(cloudwatch_metric, dict):
            cloudwatch_metric = IotTopicRuleErrorActionCloudwatchMetric(**cloudwatch_metric)
        if isinstance(dynamodb, dict):
            dynamodb = IotTopicRuleErrorActionDynamodb(**dynamodb)
        if isinstance(dynamodbv2, dict):
            dynamodbv2 = IotTopicRuleErrorActionDynamodbv2(**dynamodbv2)
        if isinstance(elasticsearch, dict):
            elasticsearch = IotTopicRuleErrorActionElasticsearch(**elasticsearch)
        if isinstance(firehose, dict):
            firehose = IotTopicRuleErrorActionFirehose(**firehose)
        if isinstance(http, dict):
            http = IotTopicRuleErrorActionHttp(**http)
        if isinstance(iot_analytics, dict):
            iot_analytics = IotTopicRuleErrorActionIotAnalytics(**iot_analytics)
        if isinstance(iot_events, dict):
            iot_events = IotTopicRuleErrorActionIotEvents(**iot_events)
        if isinstance(kafka, dict):
            kafka = IotTopicRuleErrorActionKafka(**kafka)
        if isinstance(kinesis, dict):
            kinesis = IotTopicRuleErrorActionKinesis(**kinesis)
        if isinstance(lambda_, dict):
            lambda_ = IotTopicRuleErrorActionLambda(**lambda_)
        if isinstance(republish, dict):
            republish = IotTopicRuleErrorActionRepublish(**republish)
        if isinstance(s3, dict):
            s3 = IotTopicRuleErrorActionS3(**s3)
        if isinstance(sns, dict):
            sns = IotTopicRuleErrorActionSns(**sns)
        if isinstance(sqs, dict):
            sqs = IotTopicRuleErrorActionSqs(**sqs)
        if isinstance(step_functions, dict):
            step_functions = IotTopicRuleErrorActionStepFunctions(**step_functions)
        if isinstance(timestream, dict):
            timestream = IotTopicRuleErrorActionTimestream(**timestream)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbb1fc763952e8f09002429d5a70475405df6e17540aaf78868f4ee5283f9cc9)
            check_type(argname="argument cloudwatch_alarm", value=cloudwatch_alarm, expected_type=type_hints["cloudwatch_alarm"])
            check_type(argname="argument cloudwatch_logs", value=cloudwatch_logs, expected_type=type_hints["cloudwatch_logs"])
            check_type(argname="argument cloudwatch_metric", value=cloudwatch_metric, expected_type=type_hints["cloudwatch_metric"])
            check_type(argname="argument dynamodb", value=dynamodb, expected_type=type_hints["dynamodb"])
            check_type(argname="argument dynamodbv2", value=dynamodbv2, expected_type=type_hints["dynamodbv2"])
            check_type(argname="argument elasticsearch", value=elasticsearch, expected_type=type_hints["elasticsearch"])
            check_type(argname="argument firehose", value=firehose, expected_type=type_hints["firehose"])
            check_type(argname="argument http", value=http, expected_type=type_hints["http"])
            check_type(argname="argument iot_analytics", value=iot_analytics, expected_type=type_hints["iot_analytics"])
            check_type(argname="argument iot_events", value=iot_events, expected_type=type_hints["iot_events"])
            check_type(argname="argument kafka", value=kafka, expected_type=type_hints["kafka"])
            check_type(argname="argument kinesis", value=kinesis, expected_type=type_hints["kinesis"])
            check_type(argname="argument lambda_", value=lambda_, expected_type=type_hints["lambda_"])
            check_type(argname="argument republish", value=republish, expected_type=type_hints["republish"])
            check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
            check_type(argname="argument sns", value=sns, expected_type=type_hints["sns"])
            check_type(argname="argument sqs", value=sqs, expected_type=type_hints["sqs"])
            check_type(argname="argument step_functions", value=step_functions, expected_type=type_hints["step_functions"])
            check_type(argname="argument timestream", value=timestream, expected_type=type_hints["timestream"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cloudwatch_alarm is not None:
            self._values["cloudwatch_alarm"] = cloudwatch_alarm
        if cloudwatch_logs is not None:
            self._values["cloudwatch_logs"] = cloudwatch_logs
        if cloudwatch_metric is not None:
            self._values["cloudwatch_metric"] = cloudwatch_metric
        if dynamodb is not None:
            self._values["dynamodb"] = dynamodb
        if dynamodbv2 is not None:
            self._values["dynamodbv2"] = dynamodbv2
        if elasticsearch is not None:
            self._values["elasticsearch"] = elasticsearch
        if firehose is not None:
            self._values["firehose"] = firehose
        if http is not None:
            self._values["http"] = http
        if iot_analytics is not None:
            self._values["iot_analytics"] = iot_analytics
        if iot_events is not None:
            self._values["iot_events"] = iot_events
        if kafka is not None:
            self._values["kafka"] = kafka
        if kinesis is not None:
            self._values["kinesis"] = kinesis
        if lambda_ is not None:
            self._values["lambda_"] = lambda_
        if republish is not None:
            self._values["republish"] = republish
        if s3 is not None:
            self._values["s3"] = s3
        if sns is not None:
            self._values["sns"] = sns
        if sqs is not None:
            self._values["sqs"] = sqs
        if step_functions is not None:
            self._values["step_functions"] = step_functions
        if timestream is not None:
            self._values["timestream"] = timestream

    @builtins.property
    def cloudwatch_alarm(
        self,
    ) -> typing.Optional["IotTopicRuleErrorActionCloudwatchAlarm"]:
        '''cloudwatch_alarm block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#cloudwatch_alarm IotTopicRule#cloudwatch_alarm}
        '''
        result = self._values.get("cloudwatch_alarm")
        return typing.cast(typing.Optional["IotTopicRuleErrorActionCloudwatchAlarm"], result)

    @builtins.property
    def cloudwatch_logs(
        self,
    ) -> typing.Optional["IotTopicRuleErrorActionCloudwatchLogs"]:
        '''cloudwatch_logs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#cloudwatch_logs IotTopicRule#cloudwatch_logs}
        '''
        result = self._values.get("cloudwatch_logs")
        return typing.cast(typing.Optional["IotTopicRuleErrorActionCloudwatchLogs"], result)

    @builtins.property
    def cloudwatch_metric(
        self,
    ) -> typing.Optional["IotTopicRuleErrorActionCloudwatchMetric"]:
        '''cloudwatch_metric block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#cloudwatch_metric IotTopicRule#cloudwatch_metric}
        '''
        result = self._values.get("cloudwatch_metric")
        return typing.cast(typing.Optional["IotTopicRuleErrorActionCloudwatchMetric"], result)

    @builtins.property
    def dynamodb(self) -> typing.Optional["IotTopicRuleErrorActionDynamodb"]:
        '''dynamodb block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#dynamodb IotTopicRule#dynamodb}
        '''
        result = self._values.get("dynamodb")
        return typing.cast(typing.Optional["IotTopicRuleErrorActionDynamodb"], result)

    @builtins.property
    def dynamodbv2(self) -> typing.Optional["IotTopicRuleErrorActionDynamodbv2"]:
        '''dynamodbv2 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#dynamodbv2 IotTopicRule#dynamodbv2}
        '''
        result = self._values.get("dynamodbv2")
        return typing.cast(typing.Optional["IotTopicRuleErrorActionDynamodbv2"], result)

    @builtins.property
    def elasticsearch(self) -> typing.Optional["IotTopicRuleErrorActionElasticsearch"]:
        '''elasticsearch block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#elasticsearch IotTopicRule#elasticsearch}
        '''
        result = self._values.get("elasticsearch")
        return typing.cast(typing.Optional["IotTopicRuleErrorActionElasticsearch"], result)

    @builtins.property
    def firehose(self) -> typing.Optional["IotTopicRuleErrorActionFirehose"]:
        '''firehose block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#firehose IotTopicRule#firehose}
        '''
        result = self._values.get("firehose")
        return typing.cast(typing.Optional["IotTopicRuleErrorActionFirehose"], result)

    @builtins.property
    def http(self) -> typing.Optional["IotTopicRuleErrorActionHttp"]:
        '''http block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#http IotTopicRule#http}
        '''
        result = self._values.get("http")
        return typing.cast(typing.Optional["IotTopicRuleErrorActionHttp"], result)

    @builtins.property
    def iot_analytics(self) -> typing.Optional["IotTopicRuleErrorActionIotAnalytics"]:
        '''iot_analytics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#iot_analytics IotTopicRule#iot_analytics}
        '''
        result = self._values.get("iot_analytics")
        return typing.cast(typing.Optional["IotTopicRuleErrorActionIotAnalytics"], result)

    @builtins.property
    def iot_events(self) -> typing.Optional["IotTopicRuleErrorActionIotEvents"]:
        '''iot_events block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#iot_events IotTopicRule#iot_events}
        '''
        result = self._values.get("iot_events")
        return typing.cast(typing.Optional["IotTopicRuleErrorActionIotEvents"], result)

    @builtins.property
    def kafka(self) -> typing.Optional["IotTopicRuleErrorActionKafka"]:
        '''kafka block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#kafka IotTopicRule#kafka}
        '''
        result = self._values.get("kafka")
        return typing.cast(typing.Optional["IotTopicRuleErrorActionKafka"], result)

    @builtins.property
    def kinesis(self) -> typing.Optional["IotTopicRuleErrorActionKinesis"]:
        '''kinesis block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#kinesis IotTopicRule#kinesis}
        '''
        result = self._values.get("kinesis")
        return typing.cast(typing.Optional["IotTopicRuleErrorActionKinesis"], result)

    @builtins.property
    def lambda_(self) -> typing.Optional["IotTopicRuleErrorActionLambda"]:
        '''lambda block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#lambda IotTopicRule#lambda}
        '''
        result = self._values.get("lambda_")
        return typing.cast(typing.Optional["IotTopicRuleErrorActionLambda"], result)

    @builtins.property
    def republish(self) -> typing.Optional["IotTopicRuleErrorActionRepublish"]:
        '''republish block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#republish IotTopicRule#republish}
        '''
        result = self._values.get("republish")
        return typing.cast(typing.Optional["IotTopicRuleErrorActionRepublish"], result)

    @builtins.property
    def s3(self) -> typing.Optional["IotTopicRuleErrorActionS3"]:
        '''s3 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#s3 IotTopicRule#s3}
        '''
        result = self._values.get("s3")
        return typing.cast(typing.Optional["IotTopicRuleErrorActionS3"], result)

    @builtins.property
    def sns(self) -> typing.Optional["IotTopicRuleErrorActionSns"]:
        '''sns block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#sns IotTopicRule#sns}
        '''
        result = self._values.get("sns")
        return typing.cast(typing.Optional["IotTopicRuleErrorActionSns"], result)

    @builtins.property
    def sqs(self) -> typing.Optional["IotTopicRuleErrorActionSqs"]:
        '''sqs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#sqs IotTopicRule#sqs}
        '''
        result = self._values.get("sqs")
        return typing.cast(typing.Optional["IotTopicRuleErrorActionSqs"], result)

    @builtins.property
    def step_functions(self) -> typing.Optional["IotTopicRuleErrorActionStepFunctions"]:
        '''step_functions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#step_functions IotTopicRule#step_functions}
        '''
        result = self._values.get("step_functions")
        return typing.cast(typing.Optional["IotTopicRuleErrorActionStepFunctions"], result)

    @builtins.property
    def timestream(self) -> typing.Optional["IotTopicRuleErrorActionTimestream"]:
        '''timestream block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#timestream IotTopicRule#timestream}
        '''
        result = self._values.get("timestream")
        return typing.cast(typing.Optional["IotTopicRuleErrorActionTimestream"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleErrorAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionCloudwatchAlarm",
    jsii_struct_bases=[],
    name_mapping={
        "alarm_name": "alarmName",
        "role_arn": "roleArn",
        "state_reason": "stateReason",
        "state_value": "stateValue",
    },
)
class IotTopicRuleErrorActionCloudwatchAlarm:
    def __init__(
        self,
        *,
        alarm_name: builtins.str,
        role_arn: builtins.str,
        state_reason: builtins.str,
        state_value: builtins.str,
    ) -> None:
        '''
        :param alarm_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#alarm_name IotTopicRule#alarm_name}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param state_reason: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#state_reason IotTopicRule#state_reason}.
        :param state_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#state_value IotTopicRule#state_value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__beaef60545e1dad110a4d067bb99859a0d2a1a7e123e5ed3dfe19160e2d8d2fd)
            check_type(argname="argument alarm_name", value=alarm_name, expected_type=type_hints["alarm_name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument state_reason", value=state_reason, expected_type=type_hints["state_reason"])
            check_type(argname="argument state_value", value=state_value, expected_type=type_hints["state_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "alarm_name": alarm_name,
            "role_arn": role_arn,
            "state_reason": state_reason,
            "state_value": state_value,
        }

    @builtins.property
    def alarm_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#alarm_name IotTopicRule#alarm_name}.'''
        result = self._values.get("alarm_name")
        assert result is not None, "Required property 'alarm_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def state_reason(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#state_reason IotTopicRule#state_reason}.'''
        result = self._values.get("state_reason")
        assert result is not None, "Required property 'state_reason' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def state_value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#state_value IotTopicRule#state_value}.'''
        result = self._values.get("state_value")
        assert result is not None, "Required property 'state_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleErrorActionCloudwatchAlarm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleErrorActionCloudwatchAlarmOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionCloudwatchAlarmOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9fd66bb8d7b9c8f151bd85aa690acd8b4bf414b6ed8e7ece74fb389d33256cca)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="alarmNameInput")
    def alarm_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alarmNameInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="stateReasonInput")
    def state_reason_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateReasonInput"))

    @builtins.property
    @jsii.member(jsii_name="stateValueInput")
    def state_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateValueInput"))

    @builtins.property
    @jsii.member(jsii_name="alarmName")
    def alarm_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "alarmName"))

    @alarm_name.setter
    def alarm_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d018275d861c2c710f56236d960abfe0a64b1400d13aa929133d3d76c134d7f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alarmName", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3267d6d5e1b1152a9c3ff61179a45fce697c09da9d361f670332ac390f6ff6c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="stateReason")
    def state_reason(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stateReason"))

    @state_reason.setter
    def state_reason(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82daa9591f1dfabcf5b39b0b6ae5c14f1140a2f4c5e94cee878980427bd5a247)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stateReason", value)

    @builtins.property
    @jsii.member(jsii_name="stateValue")
    def state_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stateValue"))

    @state_value.setter
    def state_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__853dcdc1d51e0dc6e8d39adece2f2cc1c7a3440e88ea1583b546d4f65ffe679c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stateValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IotTopicRuleErrorActionCloudwatchAlarm]:
        return typing.cast(typing.Optional[IotTopicRuleErrorActionCloudwatchAlarm], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IotTopicRuleErrorActionCloudwatchAlarm],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e5c40b7c2b93c6b667b928a681982dd221559bdd23f450882ab4ea4a0ce8988)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionCloudwatchLogs",
    jsii_struct_bases=[],
    name_mapping={"log_group_name": "logGroupName", "role_arn": "roleArn"},
)
class IotTopicRuleErrorActionCloudwatchLogs:
    def __init__(self, *, log_group_name: builtins.str, role_arn: builtins.str) -> None:
        '''
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#log_group_name IotTopicRule#log_group_name}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__decb5c3b9d1d9208896355b6529badb531e10c7e9fba722b9e849aecbb99309d)
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "log_group_name": log_group_name,
            "role_arn": role_arn,
        }

    @builtins.property
    def log_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#log_group_name IotTopicRule#log_group_name}.'''
        result = self._values.get("log_group_name")
        assert result is not None, "Required property 'log_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleErrorActionCloudwatchLogs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleErrorActionCloudwatchLogsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionCloudwatchLogsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7e0cb4abcf779690d49f4dba0fd65df5506a5726dd3886a54f769b026108e67c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="logGroupNameInput")
    def log_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logGroupName"))

    @log_group_name.setter
    def log_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2012b43a5eb9cd2f38b6f59426c405f69409497ac8b340f65bd3c7285c9ebe27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f830703abbb73e64dc7cd322c46d1dd82daa3d71182eb4b91aae02f1bf57c632)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IotTopicRuleErrorActionCloudwatchLogs]:
        return typing.cast(typing.Optional[IotTopicRuleErrorActionCloudwatchLogs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IotTopicRuleErrorActionCloudwatchLogs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__411215fde1fa0ea702d43a9d4a2447e75e2f360f2f035dd005178451334d2dec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionCloudwatchMetric",
    jsii_struct_bases=[],
    name_mapping={
        "metric_name": "metricName",
        "metric_namespace": "metricNamespace",
        "metric_unit": "metricUnit",
        "metric_value": "metricValue",
        "role_arn": "roleArn",
        "metric_timestamp": "metricTimestamp",
    },
)
class IotTopicRuleErrorActionCloudwatchMetric:
    def __init__(
        self,
        *,
        metric_name: builtins.str,
        metric_namespace: builtins.str,
        metric_unit: builtins.str,
        metric_value: builtins.str,
        role_arn: builtins.str,
        metric_timestamp: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#metric_name IotTopicRule#metric_name}.
        :param metric_namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#metric_namespace IotTopicRule#metric_namespace}.
        :param metric_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#metric_unit IotTopicRule#metric_unit}.
        :param metric_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#metric_value IotTopicRule#metric_value}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param metric_timestamp: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#metric_timestamp IotTopicRule#metric_timestamp}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d5c31cf675bf38e4ac7587a63c8f879d2ca23067a7a57d203df807fd3061427)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
            check_type(argname="argument metric_namespace", value=metric_namespace, expected_type=type_hints["metric_namespace"])
            check_type(argname="argument metric_unit", value=metric_unit, expected_type=type_hints["metric_unit"])
            check_type(argname="argument metric_value", value=metric_value, expected_type=type_hints["metric_value"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument metric_timestamp", value=metric_timestamp, expected_type=type_hints["metric_timestamp"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metric_name": metric_name,
            "metric_namespace": metric_namespace,
            "metric_unit": metric_unit,
            "metric_value": metric_value,
            "role_arn": role_arn,
        }
        if metric_timestamp is not None:
            self._values["metric_timestamp"] = metric_timestamp

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#metric_name IotTopicRule#metric_name}.'''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def metric_namespace(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#metric_namespace IotTopicRule#metric_namespace}.'''
        result = self._values.get("metric_namespace")
        assert result is not None, "Required property 'metric_namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def metric_unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#metric_unit IotTopicRule#metric_unit}.'''
        result = self._values.get("metric_unit")
        assert result is not None, "Required property 'metric_unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def metric_value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#metric_value IotTopicRule#metric_value}.'''
        result = self._values.get("metric_value")
        assert result is not None, "Required property 'metric_value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def metric_timestamp(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#metric_timestamp IotTopicRule#metric_timestamp}.'''
        result = self._values.get("metric_timestamp")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleErrorActionCloudwatchMetric(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleErrorActionCloudwatchMetricOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionCloudwatchMetricOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__434afc9bef988e206ca27536a5394d44fbb2a8a312547a515dc81013c90347a4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricTimestamp")
    def reset_metric_timestamp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricTimestamp", []))

    @builtins.property
    @jsii.member(jsii_name="metricNameInput")
    def metric_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricNameInput"))

    @builtins.property
    @jsii.member(jsii_name="metricNamespaceInput")
    def metric_namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricNamespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="metricTimestampInput")
    def metric_timestamp_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricTimestampInput"))

    @builtins.property
    @jsii.member(jsii_name="metricUnitInput")
    def metric_unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricUnitInput"))

    @builtins.property
    @jsii.member(jsii_name="metricValueInput")
    def metric_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricValueInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricName"))

    @metric_name.setter
    def metric_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfb11322fc80a7bafce5c0f96573cf007e4642cf429e09a467c8de8e0496c041)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricName", value)

    @builtins.property
    @jsii.member(jsii_name="metricNamespace")
    def metric_namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricNamespace"))

    @metric_namespace.setter
    def metric_namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3b26548d5ac016b09d29b5797a76c5dd1404b808d24b035d04e39e574f6d87b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricNamespace", value)

    @builtins.property
    @jsii.member(jsii_name="metricTimestamp")
    def metric_timestamp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricTimestamp"))

    @metric_timestamp.setter
    def metric_timestamp(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e935b6f95fc7fd10eed28230c0b0fbdf825ee0dc3c6d56795dd816cba9bd500b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricTimestamp", value)

    @builtins.property
    @jsii.member(jsii_name="metricUnit")
    def metric_unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricUnit"))

    @metric_unit.setter
    def metric_unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8c19469e9578fa9065314a9ebbbac67cb73785c29a8536ac5b7a8de101cda55)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricUnit", value)

    @builtins.property
    @jsii.member(jsii_name="metricValue")
    def metric_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricValue"))

    @metric_value.setter
    def metric_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f804c14da875ce3c01854e902c0fe48fd13733890ea1378546de2858728f64cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricValue", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b6ea170b846f51c19d90a177ebaddf576b86e6c97913ca31804a534ed90a02c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[IotTopicRuleErrorActionCloudwatchMetric]:
        return typing.cast(typing.Optional[IotTopicRuleErrorActionCloudwatchMetric], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IotTopicRuleErrorActionCloudwatchMetric],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a85d26bd89eda250ade4b37aeb9e95d6c5ceb2d64c393f2b5130631e8eea8ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionDynamodb",
    jsii_struct_bases=[],
    name_mapping={
        "hash_key_field": "hashKeyField",
        "hash_key_value": "hashKeyValue",
        "role_arn": "roleArn",
        "table_name": "tableName",
        "hash_key_type": "hashKeyType",
        "operation": "operation",
        "payload_field": "payloadField",
        "range_key_field": "rangeKeyField",
        "range_key_type": "rangeKeyType",
        "range_key_value": "rangeKeyValue",
    },
)
class IotTopicRuleErrorActionDynamodb:
    def __init__(
        self,
        *,
        hash_key_field: builtins.str,
        hash_key_value: builtins.str,
        role_arn: builtins.str,
        table_name: builtins.str,
        hash_key_type: typing.Optional[builtins.str] = None,
        operation: typing.Optional[builtins.str] = None,
        payload_field: typing.Optional[builtins.str] = None,
        range_key_field: typing.Optional[builtins.str] = None,
        range_key_type: typing.Optional[builtins.str] = None,
        range_key_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param hash_key_field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#hash_key_field IotTopicRule#hash_key_field}.
        :param hash_key_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#hash_key_value IotTopicRule#hash_key_value}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#table_name IotTopicRule#table_name}.
        :param hash_key_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#hash_key_type IotTopicRule#hash_key_type}.
        :param operation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#operation IotTopicRule#operation}.
        :param payload_field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#payload_field IotTopicRule#payload_field}.
        :param range_key_field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#range_key_field IotTopicRule#range_key_field}.
        :param range_key_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#range_key_type IotTopicRule#range_key_type}.
        :param range_key_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#range_key_value IotTopicRule#range_key_value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__539f1971d506f9d3f01a7b0c52f40a8507b1a74788b619ae7676ee7479f533f5)
            check_type(argname="argument hash_key_field", value=hash_key_field, expected_type=type_hints["hash_key_field"])
            check_type(argname="argument hash_key_value", value=hash_key_value, expected_type=type_hints["hash_key_value"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            check_type(argname="argument hash_key_type", value=hash_key_type, expected_type=type_hints["hash_key_type"])
            check_type(argname="argument operation", value=operation, expected_type=type_hints["operation"])
            check_type(argname="argument payload_field", value=payload_field, expected_type=type_hints["payload_field"])
            check_type(argname="argument range_key_field", value=range_key_field, expected_type=type_hints["range_key_field"])
            check_type(argname="argument range_key_type", value=range_key_type, expected_type=type_hints["range_key_type"])
            check_type(argname="argument range_key_value", value=range_key_value, expected_type=type_hints["range_key_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "hash_key_field": hash_key_field,
            "hash_key_value": hash_key_value,
            "role_arn": role_arn,
            "table_name": table_name,
        }
        if hash_key_type is not None:
            self._values["hash_key_type"] = hash_key_type
        if operation is not None:
            self._values["operation"] = operation
        if payload_field is not None:
            self._values["payload_field"] = payload_field
        if range_key_field is not None:
            self._values["range_key_field"] = range_key_field
        if range_key_type is not None:
            self._values["range_key_type"] = range_key_type
        if range_key_value is not None:
            self._values["range_key_value"] = range_key_value

    @builtins.property
    def hash_key_field(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#hash_key_field IotTopicRule#hash_key_field}.'''
        result = self._values.get("hash_key_field")
        assert result is not None, "Required property 'hash_key_field' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def hash_key_value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#hash_key_value IotTopicRule#hash_key_value}.'''
        result = self._values.get("hash_key_value")
        assert result is not None, "Required property 'hash_key_value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#table_name IotTopicRule#table_name}.'''
        result = self._values.get("table_name")
        assert result is not None, "Required property 'table_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def hash_key_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#hash_key_type IotTopicRule#hash_key_type}.'''
        result = self._values.get("hash_key_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operation(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#operation IotTopicRule#operation}.'''
        result = self._values.get("operation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def payload_field(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#payload_field IotTopicRule#payload_field}.'''
        result = self._values.get("payload_field")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def range_key_field(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#range_key_field IotTopicRule#range_key_field}.'''
        result = self._values.get("range_key_field")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def range_key_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#range_key_type IotTopicRule#range_key_type}.'''
        result = self._values.get("range_key_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def range_key_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#range_key_value IotTopicRule#range_key_value}.'''
        result = self._values.get("range_key_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleErrorActionDynamodb(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleErrorActionDynamodbOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionDynamodbOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__450bbd6747603d1bc1e81ed44ec520abba9d7b5b4c8bb72290c141866c392f99)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHashKeyType")
    def reset_hash_key_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHashKeyType", []))

    @jsii.member(jsii_name="resetOperation")
    def reset_operation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperation", []))

    @jsii.member(jsii_name="resetPayloadField")
    def reset_payload_field(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPayloadField", []))

    @jsii.member(jsii_name="resetRangeKeyField")
    def reset_range_key_field(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRangeKeyField", []))

    @jsii.member(jsii_name="resetRangeKeyType")
    def reset_range_key_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRangeKeyType", []))

    @jsii.member(jsii_name="resetRangeKeyValue")
    def reset_range_key_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRangeKeyValue", []))

    @builtins.property
    @jsii.member(jsii_name="hashKeyFieldInput")
    def hash_key_field_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hashKeyFieldInput"))

    @builtins.property
    @jsii.member(jsii_name="hashKeyTypeInput")
    def hash_key_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hashKeyTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="hashKeyValueInput")
    def hash_key_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hashKeyValueInput"))

    @builtins.property
    @jsii.member(jsii_name="operationInput")
    def operation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operationInput"))

    @builtins.property
    @jsii.member(jsii_name="payloadFieldInput")
    def payload_field_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "payloadFieldInput"))

    @builtins.property
    @jsii.member(jsii_name="rangeKeyFieldInput")
    def range_key_field_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rangeKeyFieldInput"))

    @builtins.property
    @jsii.member(jsii_name="rangeKeyTypeInput")
    def range_key_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rangeKeyTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="rangeKeyValueInput")
    def range_key_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rangeKeyValueInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="tableNameInput")
    def table_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableNameInput"))

    @builtins.property
    @jsii.member(jsii_name="hashKeyField")
    def hash_key_field(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hashKeyField"))

    @hash_key_field.setter
    def hash_key_field(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26f8ec544c22ed46fee6f346fec3e14f27b4de3431f1009f8db0a6be1cd1ee05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hashKeyField", value)

    @builtins.property
    @jsii.member(jsii_name="hashKeyType")
    def hash_key_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hashKeyType"))

    @hash_key_type.setter
    def hash_key_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f21e7e81d5b08784ca8788f93c9b87409302e57546491a910339fc196fb7d275)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hashKeyType", value)

    @builtins.property
    @jsii.member(jsii_name="hashKeyValue")
    def hash_key_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hashKeyValue"))

    @hash_key_value.setter
    def hash_key_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30b44d540bf612a74d3a7870e66afc64227c66ad1a9909f050919b0d5100b5ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hashKeyValue", value)

    @builtins.property
    @jsii.member(jsii_name="operation")
    def operation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operation"))

    @operation.setter
    def operation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea1d5f5e565fad3aa00fc4339b3e9cf73298c23acf7d55a5e44f836aa05cb8d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operation", value)

    @builtins.property
    @jsii.member(jsii_name="payloadField")
    def payload_field(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "payloadField"))

    @payload_field.setter
    def payload_field(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69429016279fc456ce8ace5cce6e66da806e42a0b4c1eea0005a93e5f03dcd2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "payloadField", value)

    @builtins.property
    @jsii.member(jsii_name="rangeKeyField")
    def range_key_field(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rangeKeyField"))

    @range_key_field.setter
    def range_key_field(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8711550187faf0fba669635088c7bc3404400ba1121e03a511f33739400e73a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rangeKeyField", value)

    @builtins.property
    @jsii.member(jsii_name="rangeKeyType")
    def range_key_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rangeKeyType"))

    @range_key_type.setter
    def range_key_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__febe0debd18a15825198940032ea9511cf029882e7df6fdfd6b265e85c8e28cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rangeKeyType", value)

    @builtins.property
    @jsii.member(jsii_name="rangeKeyValue")
    def range_key_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rangeKeyValue"))

    @range_key_value.setter
    def range_key_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35443ecc22923638106e5f7f8ae6baaefcc3c5895a4f3d61904a737049a6ba9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rangeKeyValue", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e63e164edf83390c0fdf3797786cfc66f2e958bcff8b670343eeb7ec6b59a1d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="tableName")
    def table_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableName"))

    @table_name.setter
    def table_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7b59fd9f3113dae2c3829cd4cfa83dc7d72324b00fd928f405287f3d04368c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IotTopicRuleErrorActionDynamodb]:
        return typing.cast(typing.Optional[IotTopicRuleErrorActionDynamodb], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IotTopicRuleErrorActionDynamodb],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1092f1e060603fe07b7b1b5c290d9adc9b460bcd88b965b24a095e2b89b81fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionDynamodbv2",
    jsii_struct_bases=[],
    name_mapping={"role_arn": "roleArn", "put_item": "putItem"},
)
class IotTopicRuleErrorActionDynamodbv2:
    def __init__(
        self,
        *,
        role_arn: builtins.str,
        put_item: typing.Optional[typing.Union["IotTopicRuleErrorActionDynamodbv2PutItem", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param put_item: put_item block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#put_item IotTopicRule#put_item}
        '''
        if isinstance(put_item, dict):
            put_item = IotTopicRuleErrorActionDynamodbv2PutItem(**put_item)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d446592e9ad12e759da66f7d7bdd67e25f9587404923882979002dd33a75212)
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument put_item", value=put_item, expected_type=type_hints["put_item"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "role_arn": role_arn,
        }
        if put_item is not None:
            self._values["put_item"] = put_item

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def put_item(self) -> typing.Optional["IotTopicRuleErrorActionDynamodbv2PutItem"]:
        '''put_item block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#put_item IotTopicRule#put_item}
        '''
        result = self._values.get("put_item")
        return typing.cast(typing.Optional["IotTopicRuleErrorActionDynamodbv2PutItem"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleErrorActionDynamodbv2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleErrorActionDynamodbv2OutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionDynamodbv2OutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ae8d7acf305135c289fbf627cb0b4b142b67543ab106c124bd02d136e9a4a7a2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPutItem")
    def put_put_item(self, *, table_name: builtins.str) -> None:
        '''
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#table_name IotTopicRule#table_name}.
        '''
        value = IotTopicRuleErrorActionDynamodbv2PutItem(table_name=table_name)

        return typing.cast(None, jsii.invoke(self, "putPutItem", [value]))

    @jsii.member(jsii_name="resetPutItem")
    def reset_put_item(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPutItem", []))

    @builtins.property
    @jsii.member(jsii_name="putItem")
    def put_item(self) -> "IotTopicRuleErrorActionDynamodbv2PutItemOutputReference":
        return typing.cast("IotTopicRuleErrorActionDynamodbv2PutItemOutputReference", jsii.get(self, "putItem"))

    @builtins.property
    @jsii.member(jsii_name="putItemInput")
    def put_item_input(
        self,
    ) -> typing.Optional["IotTopicRuleErrorActionDynamodbv2PutItem"]:
        return typing.cast(typing.Optional["IotTopicRuleErrorActionDynamodbv2PutItem"], jsii.get(self, "putItemInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc9e3df6a56b9988214216cbd3f2d890cc5842b2b5abcabe864eb7e5194c7a48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IotTopicRuleErrorActionDynamodbv2]:
        return typing.cast(typing.Optional[IotTopicRuleErrorActionDynamodbv2], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IotTopicRuleErrorActionDynamodbv2],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__276c1f3a36071174ea4b88b9a332158b3b8de18d534851103d26b6a16f2c6444)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionDynamodbv2PutItem",
    jsii_struct_bases=[],
    name_mapping={"table_name": "tableName"},
)
class IotTopicRuleErrorActionDynamodbv2PutItem:
    def __init__(self, *, table_name: builtins.str) -> None:
        '''
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#table_name IotTopicRule#table_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8da4e021796968d9480c39d3d2f177a382ea067f41267e8d758f96e1d04c227f)
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "table_name": table_name,
        }

    @builtins.property
    def table_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#table_name IotTopicRule#table_name}.'''
        result = self._values.get("table_name")
        assert result is not None, "Required property 'table_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleErrorActionDynamodbv2PutItem(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleErrorActionDynamodbv2PutItemOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionDynamodbv2PutItemOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7816f6ef37dce828746524b9178b5aa3938968383348edfa511f586be11aaea8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="tableNameInput")
    def table_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tableName")
    def table_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableName"))

    @table_name.setter
    def table_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46f3e9c2f14c51a34a8fa327d1d6bcb777b7d845cd905566812861930765068b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[IotTopicRuleErrorActionDynamodbv2PutItem]:
        return typing.cast(typing.Optional[IotTopicRuleErrorActionDynamodbv2PutItem], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IotTopicRuleErrorActionDynamodbv2PutItem],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3073e7bc5df6b92f18626afc871bd5e009b89f3395cd966c54b0de94ac4aacf9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionElasticsearch",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint": "endpoint",
        "id": "id",
        "index": "index",
        "role_arn": "roleArn",
        "type": "type",
    },
)
class IotTopicRuleErrorActionElasticsearch:
    def __init__(
        self,
        *,
        endpoint: builtins.str,
        id: builtins.str,
        index: builtins.str,
        role_arn: builtins.str,
        type: builtins.str,
    ) -> None:
        '''
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#endpoint IotTopicRule#endpoint}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#id IotTopicRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param index: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#index IotTopicRule#index}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#type IotTopicRule#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cec014cfa444cc15feab584725dc97be9a75820cf4091650601a636691dd13ef)
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoint": endpoint,
            "id": id,
            "index": index,
            "role_arn": role_arn,
            "type": type,
        }

    @builtins.property
    def endpoint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#endpoint IotTopicRule#endpoint}.'''
        result = self._values.get("endpoint")
        assert result is not None, "Required property 'endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#id IotTopicRule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def index(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#index IotTopicRule#index}.'''
        result = self._values.get("index")
        assert result is not None, "Required property 'index' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#type IotTopicRule#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleErrorActionElasticsearch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleErrorActionElasticsearchOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionElasticsearchOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7a2462de5f93e40a5f2140701556a8db1cd4a9a3a64c222ddfff85991c6188c2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="indexInput")
    def index_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "indexInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3741e7ede219baeefd966ffcd4062d5e76349013638cfd38d7f273cd44d32f9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0b4175310796c6d67fcb1f1982d4fc36820dd69709e538f7c1872f33e11b170)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="index")
    def index(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "index"))

    @index.setter
    def index(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c9d179c5cabbf328d4ee927562d849908c9fae52f05c01c8fae9312f84bdb6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "index", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd3d64fef1be2bc1a29781f71d0327d5d9a43655b418120da7591276f45d394a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b8ab95c63d5e238e893746f4cd6826ae3e0107a9ee126bcffca3d4e72e3f803)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IotTopicRuleErrorActionElasticsearch]:
        return typing.cast(typing.Optional[IotTopicRuleErrorActionElasticsearch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IotTopicRuleErrorActionElasticsearch],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__705ad4b8b9e066b974f4f6a290b12acc09bbb9e44f96a81982f9918a85939bf4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionFirehose",
    jsii_struct_bases=[],
    name_mapping={
        "delivery_stream_name": "deliveryStreamName",
        "role_arn": "roleArn",
        "separator": "separator",
    },
)
class IotTopicRuleErrorActionFirehose:
    def __init__(
        self,
        *,
        delivery_stream_name: builtins.str,
        role_arn: builtins.str,
        separator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param delivery_stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#delivery_stream_name IotTopicRule#delivery_stream_name}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param separator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#separator IotTopicRule#separator}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e18dcf780e6c6c78fd7349b3901c8721013a405b0aa02ecb82120c0011b56ce)
            check_type(argname="argument delivery_stream_name", value=delivery_stream_name, expected_type=type_hints["delivery_stream_name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument separator", value=separator, expected_type=type_hints["separator"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "delivery_stream_name": delivery_stream_name,
            "role_arn": role_arn,
        }
        if separator is not None:
            self._values["separator"] = separator

    @builtins.property
    def delivery_stream_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#delivery_stream_name IotTopicRule#delivery_stream_name}.'''
        result = self._values.get("delivery_stream_name")
        assert result is not None, "Required property 'delivery_stream_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def separator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#separator IotTopicRule#separator}.'''
        result = self._values.get("separator")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleErrorActionFirehose(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleErrorActionFirehoseOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionFirehoseOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__299c8730f5cc5cdc2374aab96a6c20da6d3d05c0683265c87b05bcbc82e464b2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetSeparator")
    def reset_separator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSeparator", []))

    @builtins.property
    @jsii.member(jsii_name="deliveryStreamNameInput")
    def delivery_stream_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deliveryStreamNameInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="separatorInput")
    def separator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "separatorInput"))

    @builtins.property
    @jsii.member(jsii_name="deliveryStreamName")
    def delivery_stream_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deliveryStreamName"))

    @delivery_stream_name.setter
    def delivery_stream_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__145467e9e47dd9591e5b1e33fd0405b14c584fcb2c37b1ccd58675c66e06c7b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryStreamName", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b1a03b518cc4a6e7422a43ed9c7f225bb70eeaac23ca5e0a6b0061496e0a98b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="separator")
    def separator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "separator"))

    @separator.setter
    def separator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d47796e6bdf07388c04f994f9dc6879585e6a1ca16e39bb1f7095fdd9227545)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "separator", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IotTopicRuleErrorActionFirehose]:
        return typing.cast(typing.Optional[IotTopicRuleErrorActionFirehose], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IotTopicRuleErrorActionFirehose],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b34221ccf381a62d5ee09dca34b88027f9a55f83450b6726c5dab54efbb43b24)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionHttp",
    jsii_struct_bases=[],
    name_mapping={
        "url": "url",
        "confirmation_url": "confirmationUrl",
        "http_header": "httpHeader",
    },
)
class IotTopicRuleErrorActionHttp:
    def __init__(
        self,
        *,
        url: builtins.str,
        confirmation_url: typing.Optional[builtins.str] = None,
        http_header: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleErrorActionHttpHttpHeader", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#url IotTopicRule#url}.
        :param confirmation_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#confirmation_url IotTopicRule#confirmation_url}.
        :param http_header: http_header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#http_header IotTopicRule#http_header}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40ac6191e1a3aa9ee1524f6a3c2c1f9687a45536586b0dd1d11e94d72d9d83b1)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument confirmation_url", value=confirmation_url, expected_type=type_hints["confirmation_url"])
            check_type(argname="argument http_header", value=http_header, expected_type=type_hints["http_header"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "url": url,
        }
        if confirmation_url is not None:
            self._values["confirmation_url"] = confirmation_url
        if http_header is not None:
            self._values["http_header"] = http_header

    @builtins.property
    def url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#url IotTopicRule#url}.'''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def confirmation_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#confirmation_url IotTopicRule#confirmation_url}.'''
        result = self._values.get("confirmation_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_header(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleErrorActionHttpHttpHeader"]]]:
        '''http_header block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#http_header IotTopicRule#http_header}
        '''
        result = self._values.get("http_header")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleErrorActionHttpHttpHeader"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleErrorActionHttp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionHttpHttpHeader",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class IotTopicRuleErrorActionHttpHttpHeader:
    def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#key IotTopicRule#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#value IotTopicRule#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__958d61f3c4368d7991b6adfa1ce4f83eae2680a0e1a1d1429b86497e99255225)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#key IotTopicRule#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#value IotTopicRule#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleErrorActionHttpHttpHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleErrorActionHttpHttpHeaderList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionHttpHttpHeaderList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cacc0be7c2f7d593ca658d31386c57fcf635430904244333c6e5e16113bf2fa3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "IotTopicRuleErrorActionHttpHttpHeaderOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b98cf3869470ccdb759e8be87dba516dfc42d7cdb1b2eadb86891e058d627c09)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IotTopicRuleErrorActionHttpHttpHeaderOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ada93e9dec8d026386f32e8be5d9285544011644c43d6ab3c00ff252f57cde4a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__02ac628b9e0983ffa37f3ddc10f3f51e84a40963e44096215b973d3dbc5851c8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__13834c981b8703c6ecd3442517a58cefe5974297a528e1c1eb800ecc874fd270)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleErrorActionHttpHttpHeader]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleErrorActionHttpHttpHeader]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleErrorActionHttpHttpHeader]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1388b6d46624477659dd049bc97d7521d865058c8f80fab9c06f2dc65d1681dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotTopicRuleErrorActionHttpHttpHeaderOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionHttpHttpHeaderOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__42a6f78cfe139865cddb4014d0a78a738e1a2b9fd0e0c09e6d4ef7fa0e9194d4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

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
            type_hints = typing.get_type_hints(_typecheckingstub__d8c2b6ea9634aebfe0d91a60bc4382560c297ba64517ca9914bfdb5fa84c238f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__447af9e7c9cc9ba1a04aaa2e06b3b104c6b3da153849ba76ddab49766f7edb7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IotTopicRuleErrorActionHttpHttpHeader, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IotTopicRuleErrorActionHttpHttpHeader, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IotTopicRuleErrorActionHttpHttpHeader, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__771a19257bd1de991f4a182a8cdcbb1d250def0799117889af403f0a39510f70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotTopicRuleErrorActionHttpOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionHttpOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3156360fea721063d33e3fee53aec2f8ab024700641830e42d402d55e2ec10d0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putHttpHeader")
    def put_http_header(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleErrorActionHttpHttpHeader, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c4382343697a2d14413d8f205caf0a4f89e9948286e5b2643653300c58a4d4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHttpHeader", [value]))

    @jsii.member(jsii_name="resetConfirmationUrl")
    def reset_confirmation_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfirmationUrl", []))

    @jsii.member(jsii_name="resetHttpHeader")
    def reset_http_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpHeader", []))

    @builtins.property
    @jsii.member(jsii_name="httpHeader")
    def http_header(self) -> IotTopicRuleErrorActionHttpHttpHeaderList:
        return typing.cast(IotTopicRuleErrorActionHttpHttpHeaderList, jsii.get(self, "httpHeader"))

    @builtins.property
    @jsii.member(jsii_name="confirmationUrlInput")
    def confirmation_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "confirmationUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="httpHeaderInput")
    def http_header_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleErrorActionHttpHttpHeader]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleErrorActionHttpHttpHeader]]], jsii.get(self, "httpHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="confirmationUrl")
    def confirmation_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "confirmationUrl"))

    @confirmation_url.setter
    def confirmation_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2efd2550098ba7e44cc65f1ac0d90977b80a58e2caac09ea2ce3d7c97068a4c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "confirmationUrl", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__499235f2fa135b91e8b65632da39365e3488b13cc22d25a3a69c355d3f3245b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IotTopicRuleErrorActionHttp]:
        return typing.cast(typing.Optional[IotTopicRuleErrorActionHttp], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IotTopicRuleErrorActionHttp],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c34126ce450572f23301d40c842eb6958038181c49f1865f725987442320d29)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionIotAnalytics",
    jsii_struct_bases=[],
    name_mapping={"channel_name": "channelName", "role_arn": "roleArn"},
)
class IotTopicRuleErrorActionIotAnalytics:
    def __init__(self, *, channel_name: builtins.str, role_arn: builtins.str) -> None:
        '''
        :param channel_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#channel_name IotTopicRule#channel_name}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1055b7b8ace69e182e679dbec49b62f50b565eff8b7661d14856677802fe6d4c)
            check_type(argname="argument channel_name", value=channel_name, expected_type=type_hints["channel_name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "channel_name": channel_name,
            "role_arn": role_arn,
        }

    @builtins.property
    def channel_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#channel_name IotTopicRule#channel_name}.'''
        result = self._values.get("channel_name")
        assert result is not None, "Required property 'channel_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleErrorActionIotAnalytics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleErrorActionIotAnalyticsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionIotAnalyticsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__55d4f3c5922a11426c9318069a506621e3ad3a032ceaa4d1f4f334f6d07862b9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="channelNameInput")
    def channel_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "channelNameInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="channelName")
    def channel_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "channelName"))

    @channel_name.setter
    def channel_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62baff829fcf6a793e09ab9e5d21e70f4fd9989afc2640b73fe72f340a132e75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channelName", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__324835f7b735020406fddc08d8e2eb784513b132815f95b00d60989fa954e713)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IotTopicRuleErrorActionIotAnalytics]:
        return typing.cast(typing.Optional[IotTopicRuleErrorActionIotAnalytics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IotTopicRuleErrorActionIotAnalytics],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab0cd7e555d71ff7f33801b6a249942e5d028a35d22b7afaca6965d8dcfe05c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionIotEvents",
    jsii_struct_bases=[],
    name_mapping={
        "input_name": "inputName",
        "role_arn": "roleArn",
        "message_id": "messageId",
    },
)
class IotTopicRuleErrorActionIotEvents:
    def __init__(
        self,
        *,
        input_name: builtins.str,
        role_arn: builtins.str,
        message_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param input_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#input_name IotTopicRule#input_name}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param message_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#message_id IotTopicRule#message_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d43e0308f540c77658be6fa698efa9cd7ff11ea46b7be333ed404f6b010941c)
            check_type(argname="argument input_name", value=input_name, expected_type=type_hints["input_name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument message_id", value=message_id, expected_type=type_hints["message_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "input_name": input_name,
            "role_arn": role_arn,
        }
        if message_id is not None:
            self._values["message_id"] = message_id

    @builtins.property
    def input_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#input_name IotTopicRule#input_name}.'''
        result = self._values.get("input_name")
        assert result is not None, "Required property 'input_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def message_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#message_id IotTopicRule#message_id}.'''
        result = self._values.get("message_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleErrorActionIotEvents(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleErrorActionIotEventsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionIotEventsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d5fb8f5582ee43868143d2eed06d53ea4def6af726480b3c51fcebee9b50bf29)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMessageId")
    def reset_message_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessageId", []))

    @builtins.property
    @jsii.member(jsii_name="inputNameInput")
    def input_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inputNameInput"))

    @builtins.property
    @jsii.member(jsii_name="messageIdInput")
    def message_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageIdInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="inputName")
    def input_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "inputName"))

    @input_name.setter
    def input_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1b1af86a01d560de9019f824cec5ec29089a4afa37a60fe4c71010255f148fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inputName", value)

    @builtins.property
    @jsii.member(jsii_name="messageId")
    def message_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "messageId"))

    @message_id.setter
    def message_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07b74e4e0cea6b2166a173c87968c5bfcd7acfa8996ad61bdedb702d42ffcfe0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messageId", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9c6b42822a95bfd8caf5ee7a03825ed60d16403d3aeef7e86c2503cc3e5028b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IotTopicRuleErrorActionIotEvents]:
        return typing.cast(typing.Optional[IotTopicRuleErrorActionIotEvents], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IotTopicRuleErrorActionIotEvents],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f7932417e1253cba3feeb5d51baf7d8cbeef5468c3a80d966636dd2304e7293)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionKafka",
    jsii_struct_bases=[],
    name_mapping={
        "client_properties": "clientProperties",
        "destination_arn": "destinationArn",
        "topic": "topic",
        "key": "key",
        "partition": "partition",
    },
)
class IotTopicRuleErrorActionKafka:
    def __init__(
        self,
        *,
        client_properties: typing.Mapping[builtins.str, builtins.str],
        destination_arn: builtins.str,
        topic: builtins.str,
        key: typing.Optional[builtins.str] = None,
        partition: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#client_properties IotTopicRule#client_properties}.
        :param destination_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#destination_arn IotTopicRule#destination_arn}.
        :param topic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#topic IotTopicRule#topic}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#key IotTopicRule#key}.
        :param partition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#partition IotTopicRule#partition}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__086d411045ebbcacfed093e916858978a3344a639efcdcb163b39aacd1e746f6)
            check_type(argname="argument client_properties", value=client_properties, expected_type=type_hints["client_properties"])
            check_type(argname="argument destination_arn", value=destination_arn, expected_type=type_hints["destination_arn"])
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument partition", value=partition, expected_type=type_hints["partition"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_properties": client_properties,
            "destination_arn": destination_arn,
            "topic": topic,
        }
        if key is not None:
            self._values["key"] = key
        if partition is not None:
            self._values["partition"] = partition

    @builtins.property
    def client_properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#client_properties IotTopicRule#client_properties}.'''
        result = self._values.get("client_properties")
        assert result is not None, "Required property 'client_properties' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    @builtins.property
    def destination_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#destination_arn IotTopicRule#destination_arn}.'''
        result = self._values.get("destination_arn")
        assert result is not None, "Required property 'destination_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def topic(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#topic IotTopicRule#topic}.'''
        result = self._values.get("topic")
        assert result is not None, "Required property 'topic' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#key IotTopicRule#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def partition(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#partition IotTopicRule#partition}.'''
        result = self._values.get("partition")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleErrorActionKafka(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleErrorActionKafkaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionKafkaOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8eb7c34c45d47801c5b2cc962da5c107225a5150b61df6964492107d490b75ac)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetPartition")
    def reset_partition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPartition", []))

    @builtins.property
    @jsii.member(jsii_name="clientPropertiesInput")
    def client_properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "clientPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationArnInput")
    def destination_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationArnInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionInput")
    def partition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "partitionInput"))

    @builtins.property
    @jsii.member(jsii_name="topicInput")
    def topic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "topicInput"))

    @builtins.property
    @jsii.member(jsii_name="clientProperties")
    def client_properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "clientProperties"))

    @client_properties.setter
    def client_properties(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d37b5d2ad1b71680cd36a82693463c096e7fa2974e8b00c8d1f8e50872a799b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientProperties", value)

    @builtins.property
    @jsii.member(jsii_name="destinationArn")
    def destination_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationArn"))

    @destination_arn.setter
    def destination_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cda76b5a0961094f9c3581fcf8da654a922df75baddc1f1ada25674754f60b7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationArn", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af2f55611a23cfcedab4dbfa1db6c19eac4bf05ae8a687fd381dbc708bfd1a5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="partition")
    def partition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "partition"))

    @partition.setter
    def partition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b1875269d4c67873f6901b14805df3592a2ad0e4392323b0507175fd3855c45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partition", value)

    @builtins.property
    @jsii.member(jsii_name="topic")
    def topic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "topic"))

    @topic.setter
    def topic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__343eea3ee64c86cc88d218d7502b37beb3dc46cea05b599efa589c87066e6c5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "topic", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IotTopicRuleErrorActionKafka]:
        return typing.cast(typing.Optional[IotTopicRuleErrorActionKafka], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IotTopicRuleErrorActionKafka],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa0ea4b9345acb2531d7474e2ceab4c11a38c753236ad0003548f1ff9baf5ae8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionKinesis",
    jsii_struct_bases=[],
    name_mapping={
        "role_arn": "roleArn",
        "stream_name": "streamName",
        "partition_key": "partitionKey",
    },
)
class IotTopicRuleErrorActionKinesis:
    def __init__(
        self,
        *,
        role_arn: builtins.str,
        stream_name: builtins.str,
        partition_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#stream_name IotTopicRule#stream_name}.
        :param partition_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#partition_key IotTopicRule#partition_key}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53b55d96d8dfe7e8aa052ebbc9cff2754e17533a873b271ed9794fdf325e775e)
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument stream_name", value=stream_name, expected_type=type_hints["stream_name"])
            check_type(argname="argument partition_key", value=partition_key, expected_type=type_hints["partition_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "role_arn": role_arn,
            "stream_name": stream_name,
        }
        if partition_key is not None:
            self._values["partition_key"] = partition_key

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stream_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#stream_name IotTopicRule#stream_name}.'''
        result = self._values.get("stream_name")
        assert result is not None, "Required property 'stream_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def partition_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#partition_key IotTopicRule#partition_key}.'''
        result = self._values.get("partition_key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleErrorActionKinesis(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleErrorActionKinesisOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionKinesisOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b4e25f7a0aa1de1bea0a9c757b6ea92d2bfba843854f0b0c3b398fe3688563fa)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPartitionKey")
    def reset_partition_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPartitionKey", []))

    @builtins.property
    @jsii.member(jsii_name="partitionKeyInput")
    def partition_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "partitionKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="streamNameInput")
    def stream_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streamNameInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionKey")
    def partition_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "partitionKey"))

    @partition_key.setter
    def partition_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c171c1c715a2b9ce7a305fddbc7511312043f85308cd1e0d0ca36b712fe99d2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partitionKey", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29c4d5c1642d7023305a5aab9e29fa7655351991b9c845388784792ad13d4c1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="streamName")
    def stream_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "streamName"))

    @stream_name.setter
    def stream_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff9055812b1134cba4448450dbb6a232cdf96b0ad77a2a01ef04b667832ab403)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IotTopicRuleErrorActionKinesis]:
        return typing.cast(typing.Optional[IotTopicRuleErrorActionKinesis], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IotTopicRuleErrorActionKinesis],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__599ad6b2b54ad5d2ba49e5577f195db8ead0f8ccb1aafb6908e41aca7d63cc03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionLambda",
    jsii_struct_bases=[],
    name_mapping={"function_arn": "functionArn"},
)
class IotTopicRuleErrorActionLambda:
    def __init__(self, *, function_arn: builtins.str) -> None:
        '''
        :param function_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#function_arn IotTopicRule#function_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cad0c071f8b408b5f49ba8aa17c780e03b0edb1b15ec6009bc851b8e3212022a)
            check_type(argname="argument function_arn", value=function_arn, expected_type=type_hints["function_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "function_arn": function_arn,
        }

    @builtins.property
    def function_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#function_arn IotTopicRule#function_arn}.'''
        result = self._values.get("function_arn")
        assert result is not None, "Required property 'function_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleErrorActionLambda(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleErrorActionLambdaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionLambdaOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__03a69401142c922fbcded72aecf31d4321ac48570e8456f2348dee64bde0e4d4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="functionArnInput")
    def function_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "functionArnInput"))

    @builtins.property
    @jsii.member(jsii_name="functionArn")
    def function_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "functionArn"))

    @function_arn.setter
    def function_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61bea8c18fd4c08345c464e6950dbcbc7ae1c74243ac9cb9fbd36ec7591b69a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functionArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IotTopicRuleErrorActionLambda]:
        return typing.cast(typing.Optional[IotTopicRuleErrorActionLambda], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IotTopicRuleErrorActionLambda],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__957a60996b94522980716701dd7bd814f8a29bb580c4cbcfe03fc00afdf30880)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotTopicRuleErrorActionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5ad95c38db6be11029da404dbcf791839cff348fa731b9b9236b1865c00e42ed)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCloudwatchAlarm")
    def put_cloudwatch_alarm(
        self,
        *,
        alarm_name: builtins.str,
        role_arn: builtins.str,
        state_reason: builtins.str,
        state_value: builtins.str,
    ) -> None:
        '''
        :param alarm_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#alarm_name IotTopicRule#alarm_name}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param state_reason: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#state_reason IotTopicRule#state_reason}.
        :param state_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#state_value IotTopicRule#state_value}.
        '''
        value = IotTopicRuleErrorActionCloudwatchAlarm(
            alarm_name=alarm_name,
            role_arn=role_arn,
            state_reason=state_reason,
            state_value=state_value,
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchAlarm", [value]))

    @jsii.member(jsii_name="putCloudwatchLogs")
    def put_cloudwatch_logs(
        self,
        *,
        log_group_name: builtins.str,
        role_arn: builtins.str,
    ) -> None:
        '''
        :param log_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#log_group_name IotTopicRule#log_group_name}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        '''
        value = IotTopicRuleErrorActionCloudwatchLogs(
            log_group_name=log_group_name, role_arn=role_arn
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchLogs", [value]))

    @jsii.member(jsii_name="putCloudwatchMetric")
    def put_cloudwatch_metric(
        self,
        *,
        metric_name: builtins.str,
        metric_namespace: builtins.str,
        metric_unit: builtins.str,
        metric_value: builtins.str,
        role_arn: builtins.str,
        metric_timestamp: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#metric_name IotTopicRule#metric_name}.
        :param metric_namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#metric_namespace IotTopicRule#metric_namespace}.
        :param metric_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#metric_unit IotTopicRule#metric_unit}.
        :param metric_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#metric_value IotTopicRule#metric_value}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param metric_timestamp: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#metric_timestamp IotTopicRule#metric_timestamp}.
        '''
        value = IotTopicRuleErrorActionCloudwatchMetric(
            metric_name=metric_name,
            metric_namespace=metric_namespace,
            metric_unit=metric_unit,
            metric_value=metric_value,
            role_arn=role_arn,
            metric_timestamp=metric_timestamp,
        )

        return typing.cast(None, jsii.invoke(self, "putCloudwatchMetric", [value]))

    @jsii.member(jsii_name="putDynamodb")
    def put_dynamodb(
        self,
        *,
        hash_key_field: builtins.str,
        hash_key_value: builtins.str,
        role_arn: builtins.str,
        table_name: builtins.str,
        hash_key_type: typing.Optional[builtins.str] = None,
        operation: typing.Optional[builtins.str] = None,
        payload_field: typing.Optional[builtins.str] = None,
        range_key_field: typing.Optional[builtins.str] = None,
        range_key_type: typing.Optional[builtins.str] = None,
        range_key_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param hash_key_field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#hash_key_field IotTopicRule#hash_key_field}.
        :param hash_key_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#hash_key_value IotTopicRule#hash_key_value}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#table_name IotTopicRule#table_name}.
        :param hash_key_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#hash_key_type IotTopicRule#hash_key_type}.
        :param operation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#operation IotTopicRule#operation}.
        :param payload_field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#payload_field IotTopicRule#payload_field}.
        :param range_key_field: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#range_key_field IotTopicRule#range_key_field}.
        :param range_key_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#range_key_type IotTopicRule#range_key_type}.
        :param range_key_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#range_key_value IotTopicRule#range_key_value}.
        '''
        value = IotTopicRuleErrorActionDynamodb(
            hash_key_field=hash_key_field,
            hash_key_value=hash_key_value,
            role_arn=role_arn,
            table_name=table_name,
            hash_key_type=hash_key_type,
            operation=operation,
            payload_field=payload_field,
            range_key_field=range_key_field,
            range_key_type=range_key_type,
            range_key_value=range_key_value,
        )

        return typing.cast(None, jsii.invoke(self, "putDynamodb", [value]))

    @jsii.member(jsii_name="putDynamodbv2")
    def put_dynamodbv2(
        self,
        *,
        role_arn: builtins.str,
        put_item: typing.Optional[typing.Union[IotTopicRuleErrorActionDynamodbv2PutItem, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param put_item: put_item block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#put_item IotTopicRule#put_item}
        '''
        value = IotTopicRuleErrorActionDynamodbv2(role_arn=role_arn, put_item=put_item)

        return typing.cast(None, jsii.invoke(self, "putDynamodbv2", [value]))

    @jsii.member(jsii_name="putElasticsearch")
    def put_elasticsearch(
        self,
        *,
        endpoint: builtins.str,
        id: builtins.str,
        index: builtins.str,
        role_arn: builtins.str,
        type: builtins.str,
    ) -> None:
        '''
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#endpoint IotTopicRule#endpoint}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#id IotTopicRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param index: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#index IotTopicRule#index}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#type IotTopicRule#type}.
        '''
        value = IotTopicRuleErrorActionElasticsearch(
            endpoint=endpoint, id=id, index=index, role_arn=role_arn, type=type
        )

        return typing.cast(None, jsii.invoke(self, "putElasticsearch", [value]))

    @jsii.member(jsii_name="putFirehose")
    def put_firehose(
        self,
        *,
        delivery_stream_name: builtins.str,
        role_arn: builtins.str,
        separator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param delivery_stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#delivery_stream_name IotTopicRule#delivery_stream_name}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param separator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#separator IotTopicRule#separator}.
        '''
        value = IotTopicRuleErrorActionFirehose(
            delivery_stream_name=delivery_stream_name,
            role_arn=role_arn,
            separator=separator,
        )

        return typing.cast(None, jsii.invoke(self, "putFirehose", [value]))

    @jsii.member(jsii_name="putHttp")
    def put_http(
        self,
        *,
        url: builtins.str,
        confirmation_url: typing.Optional[builtins.str] = None,
        http_header: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleErrorActionHttpHttpHeader, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#url IotTopicRule#url}.
        :param confirmation_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#confirmation_url IotTopicRule#confirmation_url}.
        :param http_header: http_header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#http_header IotTopicRule#http_header}
        '''
        value = IotTopicRuleErrorActionHttp(
            url=url, confirmation_url=confirmation_url, http_header=http_header
        )

        return typing.cast(None, jsii.invoke(self, "putHttp", [value]))

    @jsii.member(jsii_name="putIotAnalytics")
    def put_iot_analytics(
        self,
        *,
        channel_name: builtins.str,
        role_arn: builtins.str,
    ) -> None:
        '''
        :param channel_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#channel_name IotTopicRule#channel_name}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        '''
        value = IotTopicRuleErrorActionIotAnalytics(
            channel_name=channel_name, role_arn=role_arn
        )

        return typing.cast(None, jsii.invoke(self, "putIotAnalytics", [value]))

    @jsii.member(jsii_name="putIotEvents")
    def put_iot_events(
        self,
        *,
        input_name: builtins.str,
        role_arn: builtins.str,
        message_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param input_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#input_name IotTopicRule#input_name}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param message_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#message_id IotTopicRule#message_id}.
        '''
        value = IotTopicRuleErrorActionIotEvents(
            input_name=input_name, role_arn=role_arn, message_id=message_id
        )

        return typing.cast(None, jsii.invoke(self, "putIotEvents", [value]))

    @jsii.member(jsii_name="putKafka")
    def put_kafka(
        self,
        *,
        client_properties: typing.Mapping[builtins.str, builtins.str],
        destination_arn: builtins.str,
        topic: builtins.str,
        key: typing.Optional[builtins.str] = None,
        partition: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#client_properties IotTopicRule#client_properties}.
        :param destination_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#destination_arn IotTopicRule#destination_arn}.
        :param topic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#topic IotTopicRule#topic}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#key IotTopicRule#key}.
        :param partition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#partition IotTopicRule#partition}.
        '''
        value = IotTopicRuleErrorActionKafka(
            client_properties=client_properties,
            destination_arn=destination_arn,
            topic=topic,
            key=key,
            partition=partition,
        )

        return typing.cast(None, jsii.invoke(self, "putKafka", [value]))

    @jsii.member(jsii_name="putKinesis")
    def put_kinesis(
        self,
        *,
        role_arn: builtins.str,
        stream_name: builtins.str,
        partition_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#stream_name IotTopicRule#stream_name}.
        :param partition_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#partition_key IotTopicRule#partition_key}.
        '''
        value = IotTopicRuleErrorActionKinesis(
            role_arn=role_arn, stream_name=stream_name, partition_key=partition_key
        )

        return typing.cast(None, jsii.invoke(self, "putKinesis", [value]))

    @jsii.member(jsii_name="putLambda")
    def put_lambda(self, *, function_arn: builtins.str) -> None:
        '''
        :param function_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#function_arn IotTopicRule#function_arn}.
        '''
        value = IotTopicRuleErrorActionLambda(function_arn=function_arn)

        return typing.cast(None, jsii.invoke(self, "putLambda", [value]))

    @jsii.member(jsii_name="putRepublish")
    def put_republish(
        self,
        *,
        role_arn: builtins.str,
        topic: builtins.str,
        qos: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param topic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#topic IotTopicRule#topic}.
        :param qos: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#qos IotTopicRule#qos}.
        '''
        value = IotTopicRuleErrorActionRepublish(
            role_arn=role_arn, topic=topic, qos=qos
        )

        return typing.cast(None, jsii.invoke(self, "putRepublish", [value]))

    @jsii.member(jsii_name="putS3")
    def put_s3(
        self,
        *,
        bucket_name: builtins.str,
        key: builtins.str,
        role_arn: builtins.str,
        canned_acl: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#bucket_name IotTopicRule#bucket_name}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#key IotTopicRule#key}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param canned_acl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#canned_acl IotTopicRule#canned_acl}.
        '''
        value = IotTopicRuleErrorActionS3(
            bucket_name=bucket_name, key=key, role_arn=role_arn, canned_acl=canned_acl
        )

        return typing.cast(None, jsii.invoke(self, "putS3", [value]))

    @jsii.member(jsii_name="putSns")
    def put_sns(
        self,
        *,
        role_arn: builtins.str,
        target_arn: builtins.str,
        message_format: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param target_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#target_arn IotTopicRule#target_arn}.
        :param message_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#message_format IotTopicRule#message_format}.
        '''
        value = IotTopicRuleErrorActionSns(
            role_arn=role_arn, target_arn=target_arn, message_format=message_format
        )

        return typing.cast(None, jsii.invoke(self, "putSns", [value]))

    @jsii.member(jsii_name="putSqs")
    def put_sqs(
        self,
        *,
        queue_url: builtins.str,
        role_arn: builtins.str,
        use_base64: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param queue_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#queue_url IotTopicRule#queue_url}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param use_base64: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#use_base64 IotTopicRule#use_base64}.
        '''
        value = IotTopicRuleErrorActionSqs(
            queue_url=queue_url, role_arn=role_arn, use_base64=use_base64
        )

        return typing.cast(None, jsii.invoke(self, "putSqs", [value]))

    @jsii.member(jsii_name="putStepFunctions")
    def put_step_functions(
        self,
        *,
        role_arn: builtins.str,
        state_machine_name: builtins.str,
        execution_name_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param state_machine_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#state_machine_name IotTopicRule#state_machine_name}.
        :param execution_name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#execution_name_prefix IotTopicRule#execution_name_prefix}.
        '''
        value = IotTopicRuleErrorActionStepFunctions(
            role_arn=role_arn,
            state_machine_name=state_machine_name,
            execution_name_prefix=execution_name_prefix,
        )

        return typing.cast(None, jsii.invoke(self, "putStepFunctions", [value]))

    @jsii.member(jsii_name="putTimestream")
    def put_timestream(
        self,
        *,
        database_name: builtins.str,
        dimension: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleErrorActionTimestreamDimension", typing.Dict[builtins.str, typing.Any]]]],
        role_arn: builtins.str,
        table_name: builtins.str,
        timestamp: typing.Optional[typing.Union["IotTopicRuleErrorActionTimestreamTimestamp", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#database_name IotTopicRule#database_name}.
        :param dimension: dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#dimension IotTopicRule#dimension}
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#table_name IotTopicRule#table_name}.
        :param timestamp: timestamp block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#timestamp IotTopicRule#timestamp}
        '''
        value = IotTopicRuleErrorActionTimestream(
            database_name=database_name,
            dimension=dimension,
            role_arn=role_arn,
            table_name=table_name,
            timestamp=timestamp,
        )

        return typing.cast(None, jsii.invoke(self, "putTimestream", [value]))

    @jsii.member(jsii_name="resetCloudwatchAlarm")
    def reset_cloudwatch_alarm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchAlarm", []))

    @jsii.member(jsii_name="resetCloudwatchLogs")
    def reset_cloudwatch_logs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchLogs", []))

    @jsii.member(jsii_name="resetCloudwatchMetric")
    def reset_cloudwatch_metric(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudwatchMetric", []))

    @jsii.member(jsii_name="resetDynamodb")
    def reset_dynamodb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDynamodb", []))

    @jsii.member(jsii_name="resetDynamodbv2")
    def reset_dynamodbv2(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDynamodbv2", []))

    @jsii.member(jsii_name="resetElasticsearch")
    def reset_elasticsearch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetElasticsearch", []))

    @jsii.member(jsii_name="resetFirehose")
    def reset_firehose(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirehose", []))

    @jsii.member(jsii_name="resetHttp")
    def reset_http(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttp", []))

    @jsii.member(jsii_name="resetIotAnalytics")
    def reset_iot_analytics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIotAnalytics", []))

    @jsii.member(jsii_name="resetIotEvents")
    def reset_iot_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIotEvents", []))

    @jsii.member(jsii_name="resetKafka")
    def reset_kafka(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKafka", []))

    @jsii.member(jsii_name="resetKinesis")
    def reset_kinesis(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKinesis", []))

    @jsii.member(jsii_name="resetLambda")
    def reset_lambda(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLambda", []))

    @jsii.member(jsii_name="resetRepublish")
    def reset_republish(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepublish", []))

    @jsii.member(jsii_name="resetS3")
    def reset_s3(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3", []))

    @jsii.member(jsii_name="resetSns")
    def reset_sns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSns", []))

    @jsii.member(jsii_name="resetSqs")
    def reset_sqs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSqs", []))

    @jsii.member(jsii_name="resetStepFunctions")
    def reset_step_functions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStepFunctions", []))

    @jsii.member(jsii_name="resetTimestream")
    def reset_timestream(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimestream", []))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchAlarm")
    def cloudwatch_alarm(self) -> IotTopicRuleErrorActionCloudwatchAlarmOutputReference:
        return typing.cast(IotTopicRuleErrorActionCloudwatchAlarmOutputReference, jsii.get(self, "cloudwatchAlarm"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogs")
    def cloudwatch_logs(self) -> IotTopicRuleErrorActionCloudwatchLogsOutputReference:
        return typing.cast(IotTopicRuleErrorActionCloudwatchLogsOutputReference, jsii.get(self, "cloudwatchLogs"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchMetric")
    def cloudwatch_metric(
        self,
    ) -> IotTopicRuleErrorActionCloudwatchMetricOutputReference:
        return typing.cast(IotTopicRuleErrorActionCloudwatchMetricOutputReference, jsii.get(self, "cloudwatchMetric"))

    @builtins.property
    @jsii.member(jsii_name="dynamodb")
    def dynamodb(self) -> IotTopicRuleErrorActionDynamodbOutputReference:
        return typing.cast(IotTopicRuleErrorActionDynamodbOutputReference, jsii.get(self, "dynamodb"))

    @builtins.property
    @jsii.member(jsii_name="dynamodbv2")
    def dynamodbv2(self) -> IotTopicRuleErrorActionDynamodbv2OutputReference:
        return typing.cast(IotTopicRuleErrorActionDynamodbv2OutputReference, jsii.get(self, "dynamodbv2"))

    @builtins.property
    @jsii.member(jsii_name="elasticsearch")
    def elasticsearch(self) -> IotTopicRuleErrorActionElasticsearchOutputReference:
        return typing.cast(IotTopicRuleErrorActionElasticsearchOutputReference, jsii.get(self, "elasticsearch"))

    @builtins.property
    @jsii.member(jsii_name="firehose")
    def firehose(self) -> IotTopicRuleErrorActionFirehoseOutputReference:
        return typing.cast(IotTopicRuleErrorActionFirehoseOutputReference, jsii.get(self, "firehose"))

    @builtins.property
    @jsii.member(jsii_name="http")
    def http(self) -> IotTopicRuleErrorActionHttpOutputReference:
        return typing.cast(IotTopicRuleErrorActionHttpOutputReference, jsii.get(self, "http"))

    @builtins.property
    @jsii.member(jsii_name="iotAnalytics")
    def iot_analytics(self) -> IotTopicRuleErrorActionIotAnalyticsOutputReference:
        return typing.cast(IotTopicRuleErrorActionIotAnalyticsOutputReference, jsii.get(self, "iotAnalytics"))

    @builtins.property
    @jsii.member(jsii_name="iotEvents")
    def iot_events(self) -> IotTopicRuleErrorActionIotEventsOutputReference:
        return typing.cast(IotTopicRuleErrorActionIotEventsOutputReference, jsii.get(self, "iotEvents"))

    @builtins.property
    @jsii.member(jsii_name="kafka")
    def kafka(self) -> IotTopicRuleErrorActionKafkaOutputReference:
        return typing.cast(IotTopicRuleErrorActionKafkaOutputReference, jsii.get(self, "kafka"))

    @builtins.property
    @jsii.member(jsii_name="kinesis")
    def kinesis(self) -> IotTopicRuleErrorActionKinesisOutputReference:
        return typing.cast(IotTopicRuleErrorActionKinesisOutputReference, jsii.get(self, "kinesis"))

    @builtins.property
    @jsii.member(jsii_name="lambda")
    def lambda_(self) -> IotTopicRuleErrorActionLambdaOutputReference:
        return typing.cast(IotTopicRuleErrorActionLambdaOutputReference, jsii.get(self, "lambda"))

    @builtins.property
    @jsii.member(jsii_name="republish")
    def republish(self) -> "IotTopicRuleErrorActionRepublishOutputReference":
        return typing.cast("IotTopicRuleErrorActionRepublishOutputReference", jsii.get(self, "republish"))

    @builtins.property
    @jsii.member(jsii_name="s3")
    def s3(self) -> "IotTopicRuleErrorActionS3OutputReference":
        return typing.cast("IotTopicRuleErrorActionS3OutputReference", jsii.get(self, "s3"))

    @builtins.property
    @jsii.member(jsii_name="sns")
    def sns(self) -> "IotTopicRuleErrorActionSnsOutputReference":
        return typing.cast("IotTopicRuleErrorActionSnsOutputReference", jsii.get(self, "sns"))

    @builtins.property
    @jsii.member(jsii_name="sqs")
    def sqs(self) -> "IotTopicRuleErrorActionSqsOutputReference":
        return typing.cast("IotTopicRuleErrorActionSqsOutputReference", jsii.get(self, "sqs"))

    @builtins.property
    @jsii.member(jsii_name="stepFunctions")
    def step_functions(self) -> "IotTopicRuleErrorActionStepFunctionsOutputReference":
        return typing.cast("IotTopicRuleErrorActionStepFunctionsOutputReference", jsii.get(self, "stepFunctions"))

    @builtins.property
    @jsii.member(jsii_name="timestream")
    def timestream(self) -> "IotTopicRuleErrorActionTimestreamOutputReference":
        return typing.cast("IotTopicRuleErrorActionTimestreamOutputReference", jsii.get(self, "timestream"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchAlarmInput")
    def cloudwatch_alarm_input(
        self,
    ) -> typing.Optional[IotTopicRuleErrorActionCloudwatchAlarm]:
        return typing.cast(typing.Optional[IotTopicRuleErrorActionCloudwatchAlarm], jsii.get(self, "cloudwatchAlarmInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchLogsInput")
    def cloudwatch_logs_input(
        self,
    ) -> typing.Optional[IotTopicRuleErrorActionCloudwatchLogs]:
        return typing.cast(typing.Optional[IotTopicRuleErrorActionCloudwatchLogs], jsii.get(self, "cloudwatchLogsInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchMetricInput")
    def cloudwatch_metric_input(
        self,
    ) -> typing.Optional[IotTopicRuleErrorActionCloudwatchMetric]:
        return typing.cast(typing.Optional[IotTopicRuleErrorActionCloudwatchMetric], jsii.get(self, "cloudwatchMetricInput"))

    @builtins.property
    @jsii.member(jsii_name="dynamodbInput")
    def dynamodb_input(self) -> typing.Optional[IotTopicRuleErrorActionDynamodb]:
        return typing.cast(typing.Optional[IotTopicRuleErrorActionDynamodb], jsii.get(self, "dynamodbInput"))

    @builtins.property
    @jsii.member(jsii_name="dynamodbv2Input")
    def dynamodbv2_input(self) -> typing.Optional[IotTopicRuleErrorActionDynamodbv2]:
        return typing.cast(typing.Optional[IotTopicRuleErrorActionDynamodbv2], jsii.get(self, "dynamodbv2Input"))

    @builtins.property
    @jsii.member(jsii_name="elasticsearchInput")
    def elasticsearch_input(
        self,
    ) -> typing.Optional[IotTopicRuleErrorActionElasticsearch]:
        return typing.cast(typing.Optional[IotTopicRuleErrorActionElasticsearch], jsii.get(self, "elasticsearchInput"))

    @builtins.property
    @jsii.member(jsii_name="firehoseInput")
    def firehose_input(self) -> typing.Optional[IotTopicRuleErrorActionFirehose]:
        return typing.cast(typing.Optional[IotTopicRuleErrorActionFirehose], jsii.get(self, "firehoseInput"))

    @builtins.property
    @jsii.member(jsii_name="httpInput")
    def http_input(self) -> typing.Optional[IotTopicRuleErrorActionHttp]:
        return typing.cast(typing.Optional[IotTopicRuleErrorActionHttp], jsii.get(self, "httpInput"))

    @builtins.property
    @jsii.member(jsii_name="iotAnalyticsInput")
    def iot_analytics_input(
        self,
    ) -> typing.Optional[IotTopicRuleErrorActionIotAnalytics]:
        return typing.cast(typing.Optional[IotTopicRuleErrorActionIotAnalytics], jsii.get(self, "iotAnalyticsInput"))

    @builtins.property
    @jsii.member(jsii_name="iotEventsInput")
    def iot_events_input(self) -> typing.Optional[IotTopicRuleErrorActionIotEvents]:
        return typing.cast(typing.Optional[IotTopicRuleErrorActionIotEvents], jsii.get(self, "iotEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="kafkaInput")
    def kafka_input(self) -> typing.Optional[IotTopicRuleErrorActionKafka]:
        return typing.cast(typing.Optional[IotTopicRuleErrorActionKafka], jsii.get(self, "kafkaInput"))

    @builtins.property
    @jsii.member(jsii_name="kinesisInput")
    def kinesis_input(self) -> typing.Optional[IotTopicRuleErrorActionKinesis]:
        return typing.cast(typing.Optional[IotTopicRuleErrorActionKinesis], jsii.get(self, "kinesisInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaInput")
    def lambda_input(self) -> typing.Optional[IotTopicRuleErrorActionLambda]:
        return typing.cast(typing.Optional[IotTopicRuleErrorActionLambda], jsii.get(self, "lambdaInput"))

    @builtins.property
    @jsii.member(jsii_name="republishInput")
    def republish_input(self) -> typing.Optional["IotTopicRuleErrorActionRepublish"]:
        return typing.cast(typing.Optional["IotTopicRuleErrorActionRepublish"], jsii.get(self, "republishInput"))

    @builtins.property
    @jsii.member(jsii_name="s3Input")
    def s3_input(self) -> typing.Optional["IotTopicRuleErrorActionS3"]:
        return typing.cast(typing.Optional["IotTopicRuleErrorActionS3"], jsii.get(self, "s3Input"))

    @builtins.property
    @jsii.member(jsii_name="snsInput")
    def sns_input(self) -> typing.Optional["IotTopicRuleErrorActionSns"]:
        return typing.cast(typing.Optional["IotTopicRuleErrorActionSns"], jsii.get(self, "snsInput"))

    @builtins.property
    @jsii.member(jsii_name="sqsInput")
    def sqs_input(self) -> typing.Optional["IotTopicRuleErrorActionSqs"]:
        return typing.cast(typing.Optional["IotTopicRuleErrorActionSqs"], jsii.get(self, "sqsInput"))

    @builtins.property
    @jsii.member(jsii_name="stepFunctionsInput")
    def step_functions_input(
        self,
    ) -> typing.Optional["IotTopicRuleErrorActionStepFunctions"]:
        return typing.cast(typing.Optional["IotTopicRuleErrorActionStepFunctions"], jsii.get(self, "stepFunctionsInput"))

    @builtins.property
    @jsii.member(jsii_name="timestreamInput")
    def timestream_input(self) -> typing.Optional["IotTopicRuleErrorActionTimestream"]:
        return typing.cast(typing.Optional["IotTopicRuleErrorActionTimestream"], jsii.get(self, "timestreamInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IotTopicRuleErrorAction]:
        return typing.cast(typing.Optional[IotTopicRuleErrorAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[IotTopicRuleErrorAction]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__900a945567e929aef4c9c73ed59ec80c0185570af2e59e07eb82d19b5fd0103b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionRepublish",
    jsii_struct_bases=[],
    name_mapping={"role_arn": "roleArn", "topic": "topic", "qos": "qos"},
)
class IotTopicRuleErrorActionRepublish:
    def __init__(
        self,
        *,
        role_arn: builtins.str,
        topic: builtins.str,
        qos: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param topic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#topic IotTopicRule#topic}.
        :param qos: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#qos IotTopicRule#qos}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b60e2c80f842d97d412e1f1594fd7162ef5f9aabab5e7fc2b5959a092cf220e)
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
            check_type(argname="argument qos", value=qos, expected_type=type_hints["qos"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "role_arn": role_arn,
            "topic": topic,
        }
        if qos is not None:
            self._values["qos"] = qos

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def topic(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#topic IotTopicRule#topic}.'''
        result = self._values.get("topic")
        assert result is not None, "Required property 'topic' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def qos(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#qos IotTopicRule#qos}.'''
        result = self._values.get("qos")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleErrorActionRepublish(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleErrorActionRepublishOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionRepublishOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__96c6635e30452bf3939e64e897501b2b39ac709abcb530d96cb109038577a5ca)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetQos")
    def reset_qos(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQos", []))

    @builtins.property
    @jsii.member(jsii_name="qosInput")
    def qos_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "qosInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="topicInput")
    def topic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "topicInput"))

    @builtins.property
    @jsii.member(jsii_name="qos")
    def qos(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "qos"))

    @qos.setter
    def qos(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fd93ae3ce2697ecd1a5383a62ed169cb79bc30dd47d16557d555b3f621629cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "qos", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fe42ea2615166655020b78694fe20b39ef4eeefb4db08b68189476e2ee3b008)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="topic")
    def topic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "topic"))

    @topic.setter
    def topic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63fde58d1fe97df4d26fd6831e04c1b6f0c163492c72dc9a939a7816b8929460)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "topic", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IotTopicRuleErrorActionRepublish]:
        return typing.cast(typing.Optional[IotTopicRuleErrorActionRepublish], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IotTopicRuleErrorActionRepublish],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2709a4a693393af96d5b2fd7b5d1b6a86b04f6ca7313ae5ddc0dfd99bb7ad03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionS3",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "key": "key",
        "role_arn": "roleArn",
        "canned_acl": "cannedAcl",
    },
)
class IotTopicRuleErrorActionS3:
    def __init__(
        self,
        *,
        bucket_name: builtins.str,
        key: builtins.str,
        role_arn: builtins.str,
        canned_acl: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#bucket_name IotTopicRule#bucket_name}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#key IotTopicRule#key}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param canned_acl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#canned_acl IotTopicRule#canned_acl}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e99381188c1b516c2d5cbb32505239b71a7deb0cfd92e6a1e0d9c581b73be248)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument canned_acl", value=canned_acl, expected_type=type_hints["canned_acl"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket_name": bucket_name,
            "key": key,
            "role_arn": role_arn,
        }
        if canned_acl is not None:
            self._values["canned_acl"] = canned_acl

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#bucket_name IotTopicRule#bucket_name}.'''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#key IotTopicRule#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def canned_acl(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#canned_acl IotTopicRule#canned_acl}.'''
        result = self._values.get("canned_acl")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleErrorActionS3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleErrorActionS3OutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionS3OutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5e94be316173b1e5b2d9f100529541abaa109359445638f9d4fd59c62aec6ae9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCannedAcl")
    def reset_canned_acl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCannedAcl", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="cannedAclInput")
    def canned_acl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cannedAclInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b9d7d691a6fe6564a842c54811445df1b85f916b3faa9f3685e6bcf98215d7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="cannedAcl")
    def canned_acl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cannedAcl"))

    @canned_acl.setter
    def canned_acl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcbc7eafa1a8a312a350b9bee04452a3e51535de1dd3ac49e0a527bf87298a8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cannedAcl", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__edb48c43b462dcbf50418d5efc3816b858d8125f9ca9aeaec5c0af36a3ef6e7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce387b41937ea9915e50a23c94671e6fa6ffbe5112fdc9eeeb6ec328596455a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IotTopicRuleErrorActionS3]:
        return typing.cast(typing.Optional[IotTopicRuleErrorActionS3], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[IotTopicRuleErrorActionS3]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c58aa329291360e296fe209b0c38222e82cc078d4ee06af92889d626243fa0fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionSns",
    jsii_struct_bases=[],
    name_mapping={
        "role_arn": "roleArn",
        "target_arn": "targetArn",
        "message_format": "messageFormat",
    },
)
class IotTopicRuleErrorActionSns:
    def __init__(
        self,
        *,
        role_arn: builtins.str,
        target_arn: builtins.str,
        message_format: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param target_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#target_arn IotTopicRule#target_arn}.
        :param message_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#message_format IotTopicRule#message_format}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee29886651af521f5729ff0982164b3ccd04e22af12578f5d91bc8bb3c6cfe8d)
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument target_arn", value=target_arn, expected_type=type_hints["target_arn"])
            check_type(argname="argument message_format", value=message_format, expected_type=type_hints["message_format"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "role_arn": role_arn,
            "target_arn": target_arn,
        }
        if message_format is not None:
            self._values["message_format"] = message_format

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#target_arn IotTopicRule#target_arn}.'''
        result = self._values.get("target_arn")
        assert result is not None, "Required property 'target_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def message_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#message_format IotTopicRule#message_format}.'''
        result = self._values.get("message_format")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleErrorActionSns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleErrorActionSnsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionSnsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f36429db66cf8358e8c7a2659b4c3715fb8915ff6c588b4cd8ee830c432ab1af)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMessageFormat")
    def reset_message_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessageFormat", []))

    @builtins.property
    @jsii.member(jsii_name="messageFormatInput")
    def message_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="targetArnInput")
    def target_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetArnInput"))

    @builtins.property
    @jsii.member(jsii_name="messageFormat")
    def message_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "messageFormat"))

    @message_format.setter
    def message_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be968355196106c080e61052fc6fe5aecbc044e827b4302f4cf080c1bd288c58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messageFormat", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d412b3aae39b1bedbb3eeed6c72fa7723c0bc7ff3f4c3a9d28dae4c7240d862)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="targetArn")
    def target_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetArn"))

    @target_arn.setter
    def target_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb595101b1d9537286c2b14bc398fdc69d756eb3ec1cb4c0de036def5f1a9c18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IotTopicRuleErrorActionSns]:
        return typing.cast(typing.Optional[IotTopicRuleErrorActionSns], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IotTopicRuleErrorActionSns],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3e3bb71425f9e362b3b40a900f51b76f6731776c7de13c63e3a12374144fdc8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionSqs",
    jsii_struct_bases=[],
    name_mapping={
        "queue_url": "queueUrl",
        "role_arn": "roleArn",
        "use_base64": "useBase64",
    },
)
class IotTopicRuleErrorActionSqs:
    def __init__(
        self,
        *,
        queue_url: builtins.str,
        role_arn: builtins.str,
        use_base64: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param queue_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#queue_url IotTopicRule#queue_url}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param use_base64: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#use_base64 IotTopicRule#use_base64}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c92cbcc001eb12caae16f1f318bf07b723adf9eeee01b933c1df2d13aecf0b5)
            check_type(argname="argument queue_url", value=queue_url, expected_type=type_hints["queue_url"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument use_base64", value=use_base64, expected_type=type_hints["use_base64"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "queue_url": queue_url,
            "role_arn": role_arn,
            "use_base64": use_base64,
        }

    @builtins.property
    def queue_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#queue_url IotTopicRule#queue_url}.'''
        result = self._values.get("queue_url")
        assert result is not None, "Required property 'queue_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def use_base64(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#use_base64 IotTopicRule#use_base64}.'''
        result = self._values.get("use_base64")
        assert result is not None, "Required property 'use_base64' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleErrorActionSqs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleErrorActionSqsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionSqsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__aae7c7695de867bdbf21ba0edbb869dfb6e3ba46c2a8a5a2907f03ca60343bac)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="queueUrlInput")
    def queue_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queueUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="useBase64Input")
    def use_base64_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "useBase64Input"))

    @builtins.property
    @jsii.member(jsii_name="queueUrl")
    def queue_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "queueUrl"))

    @queue_url.setter
    def queue_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26f9ed6957ca88ef844b08675ab5a52ac3ab5d06154eceb4616ca53757110b38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queueUrl", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__424b5175fb0a42bc9e0770420bd17682b79469da0ced6beaf359a2bfbec047a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="useBase64")
    def use_base64(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "useBase64"))

    @use_base64.setter
    def use_base64(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28507ebb0a4876dc62a95a1c988d5870249f04d6bc249aa0bf321fe8e9a7bcbe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useBase64", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IotTopicRuleErrorActionSqs]:
        return typing.cast(typing.Optional[IotTopicRuleErrorActionSqs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IotTopicRuleErrorActionSqs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a7129afa33d1f280b26b540c11bcfcc390420b74192409dfaec70fcad43febc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionStepFunctions",
    jsii_struct_bases=[],
    name_mapping={
        "role_arn": "roleArn",
        "state_machine_name": "stateMachineName",
        "execution_name_prefix": "executionNamePrefix",
    },
)
class IotTopicRuleErrorActionStepFunctions:
    def __init__(
        self,
        *,
        role_arn: builtins.str,
        state_machine_name: builtins.str,
        execution_name_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param state_machine_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#state_machine_name IotTopicRule#state_machine_name}.
        :param execution_name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#execution_name_prefix IotTopicRule#execution_name_prefix}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__943a6b0468bcb59a87e20968d36025655d60bb3c8255fb378cc6470ed59c4d8a)
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument state_machine_name", value=state_machine_name, expected_type=type_hints["state_machine_name"])
            check_type(argname="argument execution_name_prefix", value=execution_name_prefix, expected_type=type_hints["execution_name_prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "role_arn": role_arn,
            "state_machine_name": state_machine_name,
        }
        if execution_name_prefix is not None:
            self._values["execution_name_prefix"] = execution_name_prefix

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def state_machine_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#state_machine_name IotTopicRule#state_machine_name}.'''
        result = self._values.get("state_machine_name")
        assert result is not None, "Required property 'state_machine_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def execution_name_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#execution_name_prefix IotTopicRule#execution_name_prefix}.'''
        result = self._values.get("execution_name_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleErrorActionStepFunctions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleErrorActionStepFunctionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionStepFunctionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d9f42ef76916a69015a1399f2ec228ccb09e2d52441e70a99d272b75566f1cee)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetExecutionNamePrefix")
    def reset_execution_name_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExecutionNamePrefix", []))

    @builtins.property
    @jsii.member(jsii_name="executionNamePrefixInput")
    def execution_name_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionNamePrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="stateMachineNameInput")
    def state_machine_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateMachineNameInput"))

    @builtins.property
    @jsii.member(jsii_name="executionNamePrefix")
    def execution_name_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "executionNamePrefix"))

    @execution_name_prefix.setter
    def execution_name_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23a4c65c2900adaf27bd9e3d211c0591047b1218851413ca48419705ee840bcd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionNamePrefix", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c799bcfa0332398fe74da9c6021c8ad6e5a6ce40f7205597939b730750bb8263)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="stateMachineName")
    def state_machine_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stateMachineName"))

    @state_machine_name.setter
    def state_machine_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fedee5cb1e0e59ad3ca60ce89cc4fbf2681ee03be47779cf539e7c3c90b69a6d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stateMachineName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IotTopicRuleErrorActionStepFunctions]:
        return typing.cast(typing.Optional[IotTopicRuleErrorActionStepFunctions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IotTopicRuleErrorActionStepFunctions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98ec2b3e67947d1b0a5f321c45c1e09e5482f15b80f64fb1862932c58d19f4bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionTimestream",
    jsii_struct_bases=[],
    name_mapping={
        "database_name": "databaseName",
        "dimension": "dimension",
        "role_arn": "roleArn",
        "table_name": "tableName",
        "timestamp": "timestamp",
    },
)
class IotTopicRuleErrorActionTimestream:
    def __init__(
        self,
        *,
        database_name: builtins.str,
        dimension: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleErrorActionTimestreamDimension", typing.Dict[builtins.str, typing.Any]]]],
        role_arn: builtins.str,
        table_name: builtins.str,
        timestamp: typing.Optional[typing.Union["IotTopicRuleErrorActionTimestreamTimestamp", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#database_name IotTopicRule#database_name}.
        :param dimension: dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#dimension IotTopicRule#dimension}
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#table_name IotTopicRule#table_name}.
        :param timestamp: timestamp block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#timestamp IotTopicRule#timestamp}
        '''
        if isinstance(timestamp, dict):
            timestamp = IotTopicRuleErrorActionTimestreamTimestamp(**timestamp)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4feb8aba8eb3e89f14c828ddba6dbda67d6a993b7822fce0d8597e6f42c882d9)
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument dimension", value=dimension, expected_type=type_hints["dimension"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            check_type(argname="argument timestamp", value=timestamp, expected_type=type_hints["timestamp"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database_name": database_name,
            "dimension": dimension,
            "role_arn": role_arn,
            "table_name": table_name,
        }
        if timestamp is not None:
            self._values["timestamp"] = timestamp

    @builtins.property
    def database_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#database_name IotTopicRule#database_name}.'''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dimension(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleErrorActionTimestreamDimension"]]:
        '''dimension block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#dimension IotTopicRule#dimension}
        '''
        result = self._values.get("dimension")
        assert result is not None, "Required property 'dimension' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleErrorActionTimestreamDimension"]], result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#table_name IotTopicRule#table_name}.'''
        result = self._values.get("table_name")
        assert result is not None, "Required property 'table_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def timestamp(
        self,
    ) -> typing.Optional["IotTopicRuleErrorActionTimestreamTimestamp"]:
        '''timestamp block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#timestamp IotTopicRule#timestamp}
        '''
        result = self._values.get("timestamp")
        return typing.cast(typing.Optional["IotTopicRuleErrorActionTimestreamTimestamp"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleErrorActionTimestream(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionTimestreamDimension",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class IotTopicRuleErrorActionTimestreamDimension:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#name IotTopicRule#name}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#value IotTopicRule#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f14e387d641be2147a471408e4239bc13535c40ec30e7fd597635beec999162)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#name IotTopicRule#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#value IotTopicRule#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleErrorActionTimestreamDimension(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleErrorActionTimestreamDimensionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionTimestreamDimensionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c3834704304d6d7feb189721ca318b82c4ff2acf70813620ff58b8a3d32f7514)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "IotTopicRuleErrorActionTimestreamDimensionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cbc7b24c0a7ade9124b9a2791ab96a6b9ad61afdc69e04884473474d78e81e0)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IotTopicRuleErrorActionTimestreamDimensionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd03f3e366531e0430156d08a9bc860a4dcf2d75684e8e672ca6bb84928f487c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__aea68f94695aef43f7241009ac6c97e30a78b01f50facd33fedb8f278c5d759f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ad3ad243b1fdcf9c925ba48b9d5cdc04f105edc87298a92b54e2c29da1b1ba52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleErrorActionTimestreamDimension]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleErrorActionTimestreamDimension]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleErrorActionTimestreamDimension]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f58ea3e3b7a1317233f28addc5da54d28f37946377da1728fa5c06f258027852)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotTopicRuleErrorActionTimestreamDimensionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionTimestreamDimensionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__85a6f2a705bce6fa5961dc2bde3903665aad30c729f04e9a20af000cafa4010c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0a8218c651b40827af79ad3c0a27e8ac3e77a3ab56432299f8dd56aa62f4407)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee34c83334934587acdd69d2235937dab9e7ff36b7db5212281885448c4e218b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IotTopicRuleErrorActionTimestreamDimension, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IotTopicRuleErrorActionTimestreamDimension, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IotTopicRuleErrorActionTimestreamDimension, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__878a72c682d2912c60cc0d16fb53827231ababf83e68da600dd23a92b1c06137)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotTopicRuleErrorActionTimestreamOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionTimestreamOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5be186210b4f34d58359c93f562539f7924284d7a126135d2c48cd0161b59b43)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDimension")
    def put_dimension(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleErrorActionTimestreamDimension, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc849e456d118c69e35ba635e52d99f3864eb0e6d0350fdb4b2d5488d73a1efe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDimension", [value]))

    @jsii.member(jsii_name="putTimestamp")
    def put_timestamp(self, *, unit: builtins.str, value: builtins.str) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#unit IotTopicRule#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#value IotTopicRule#value}.
        '''
        value_ = IotTopicRuleErrorActionTimestreamTimestamp(unit=unit, value=value)

        return typing.cast(None, jsii.invoke(self, "putTimestamp", [value_]))

    @jsii.member(jsii_name="resetTimestamp")
    def reset_timestamp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimestamp", []))

    @builtins.property
    @jsii.member(jsii_name="dimension")
    def dimension(self) -> IotTopicRuleErrorActionTimestreamDimensionList:
        return typing.cast(IotTopicRuleErrorActionTimestreamDimensionList, jsii.get(self, "dimension"))

    @builtins.property
    @jsii.member(jsii_name="timestamp")
    def timestamp(self) -> "IotTopicRuleErrorActionTimestreamTimestampOutputReference":
        return typing.cast("IotTopicRuleErrorActionTimestreamTimestampOutputReference", jsii.get(self, "timestamp"))

    @builtins.property
    @jsii.member(jsii_name="databaseNameInput")
    def database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="dimensionInput")
    def dimension_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleErrorActionTimestreamDimension]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleErrorActionTimestreamDimension]]], jsii.get(self, "dimensionInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="tableNameInput")
    def table_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableNameInput"))

    @builtins.property
    @jsii.member(jsii_name="timestampInput")
    def timestamp_input(
        self,
    ) -> typing.Optional["IotTopicRuleErrorActionTimestreamTimestamp"]:
        return typing.cast(typing.Optional["IotTopicRuleErrorActionTimestreamTimestamp"], jsii.get(self, "timestampInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df9208b26b561df9c92746bae8dd3a40093650f12120760760a70bdd25973283)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c8b6804384ad88a44cf7528f49dffaaaa5b3c3a6af2bfec34d999aec9e2b9aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="tableName")
    def table_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableName"))

    @table_name.setter
    def table_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b82db016148a0f42593f46a59dbcc9d4e9c10517382b65a52dce04f47c11cb86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IotTopicRuleErrorActionTimestream]:
        return typing.cast(typing.Optional[IotTopicRuleErrorActionTimestream], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IotTopicRuleErrorActionTimestream],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81862fc920ff1bec852d004bf1894f10f522eafe385453ba540f12dbcc8b28df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionTimestreamTimestamp",
    jsii_struct_bases=[],
    name_mapping={"unit": "unit", "value": "value"},
)
class IotTopicRuleErrorActionTimestreamTimestamp:
    def __init__(self, *, unit: builtins.str, value: builtins.str) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#unit IotTopicRule#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#value IotTopicRule#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78c0e38ed52822b01e79bc090a0b9dd925adda1835addabd11e69eaf28e0209d)
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "unit": unit,
            "value": value,
        }

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#unit IotTopicRule#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#value IotTopicRule#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleErrorActionTimestreamTimestamp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleErrorActionTimestreamTimestampOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleErrorActionTimestreamTimestampOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8a785271e4cce29b6eb87fd3b397c2eb920a97f950cf49ff522b53dafb86e587)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3c8e573f676d006c5cd0d667e2c00dfda62cd50d73c43d8154c729042dbda15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14cd7b0b8a7c041e274ea012c2ddd72ae69df13ad227e137b708d457db9d04d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[IotTopicRuleErrorActionTimestreamTimestamp]:
        return typing.cast(typing.Optional[IotTopicRuleErrorActionTimestreamTimestamp], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IotTopicRuleErrorActionTimestreamTimestamp],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fb1854fb39ba2219ff758b5896987dd32491e4bff1029458ddb13d56632656d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleFirehose",
    jsii_struct_bases=[],
    name_mapping={
        "delivery_stream_name": "deliveryStreamName",
        "role_arn": "roleArn",
        "separator": "separator",
    },
)
class IotTopicRuleFirehose:
    def __init__(
        self,
        *,
        delivery_stream_name: builtins.str,
        role_arn: builtins.str,
        separator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param delivery_stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#delivery_stream_name IotTopicRule#delivery_stream_name}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param separator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#separator IotTopicRule#separator}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__168a06017aec2c64bfa5da8e95abd558a6f8089724db1c68564f85a4e6a582f4)
            check_type(argname="argument delivery_stream_name", value=delivery_stream_name, expected_type=type_hints["delivery_stream_name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument separator", value=separator, expected_type=type_hints["separator"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "delivery_stream_name": delivery_stream_name,
            "role_arn": role_arn,
        }
        if separator is not None:
            self._values["separator"] = separator

    @builtins.property
    def delivery_stream_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#delivery_stream_name IotTopicRule#delivery_stream_name}.'''
        result = self._values.get("delivery_stream_name")
        assert result is not None, "Required property 'delivery_stream_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def separator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#separator IotTopicRule#separator}.'''
        result = self._values.get("separator")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleFirehose(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleFirehoseList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleFirehoseList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__aef0742e3fb80fb9e478c00cb7913db362a64e565f1115e0c328a2782089d582)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IotTopicRuleFirehoseOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__981692c791b0e619de5fbfd11e96eb302e853ddc10354050d0c23d8f63af9c69)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IotTopicRuleFirehoseOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cc95abed0101a044de0efe89a9ba5c07b6c689ee91aba60b778ab5552a46e1b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c7e4e8772e819d7f1fca7a0fdc2037c9b02c5d7ae508b06c017357bf8ce356f6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8c02ae0d5d0ddc38cf32f014559567e55f3705ff9b96385d872bfe7f8efff563)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleFirehose]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleFirehose]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleFirehose]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b06089c530eaa722a592d243f48519736d342f5d9b0be759abe8945630520b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotTopicRuleFirehoseOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleFirehoseOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__003f69c8ab81ff2e48a9ffa942df68bca2cbafda5aeb1efc5c0883e30448dcbd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetSeparator")
    def reset_separator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSeparator", []))

    @builtins.property
    @jsii.member(jsii_name="deliveryStreamNameInput")
    def delivery_stream_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deliveryStreamNameInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="separatorInput")
    def separator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "separatorInput"))

    @builtins.property
    @jsii.member(jsii_name="deliveryStreamName")
    def delivery_stream_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deliveryStreamName"))

    @delivery_stream_name.setter
    def delivery_stream_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2609b1b03ba4dbfc567b6cacd5c3994323e1bbe52130327b61711425ca5344f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryStreamName", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfff0358f17c6be7a0fdceb88effcc7fcb80e6300fec37a59906481cd9d7f34f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="separator")
    def separator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "separator"))

    @separator.setter
    def separator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b71fdcdf0e6b86ff10ec343cd9ff2cfa688bb9e2240fff6c3825221b335da17)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "separator", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IotTopicRuleFirehose, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IotTopicRuleFirehose, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IotTopicRuleFirehose, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff68c33aa017d680b3078af67f4a8f6ae57488c7c0d8a4a29b1f3572a1eff608)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleHttp",
    jsii_struct_bases=[],
    name_mapping={
        "url": "url",
        "confirmation_url": "confirmationUrl",
        "http_header": "httpHeader",
    },
)
class IotTopicRuleHttp:
    def __init__(
        self,
        *,
        url: builtins.str,
        confirmation_url: typing.Optional[builtins.str] = None,
        http_header: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleHttpHttpHeader", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#url IotTopicRule#url}.
        :param confirmation_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#confirmation_url IotTopicRule#confirmation_url}.
        :param http_header: http_header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#http_header IotTopicRule#http_header}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f2cb3f8a9e20713a36e7f9126cdb549e3cc36cc931b5e1918a2cb57ed14e936)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument confirmation_url", value=confirmation_url, expected_type=type_hints["confirmation_url"])
            check_type(argname="argument http_header", value=http_header, expected_type=type_hints["http_header"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "url": url,
        }
        if confirmation_url is not None:
            self._values["confirmation_url"] = confirmation_url
        if http_header is not None:
            self._values["http_header"] = http_header

    @builtins.property
    def url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#url IotTopicRule#url}.'''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def confirmation_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#confirmation_url IotTopicRule#confirmation_url}.'''
        result = self._values.get("confirmation_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_header(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleHttpHttpHeader"]]]:
        '''http_header block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#http_header IotTopicRule#http_header}
        '''
        result = self._values.get("http_header")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleHttpHttpHeader"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleHttp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleHttpHttpHeader",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class IotTopicRuleHttpHttpHeader:
    def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#key IotTopicRule#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#value IotTopicRule#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16e805c0629b698dd3f4b4e933ee0a6b15a9850d2e064f2c6e647cce839ce562)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#key IotTopicRule#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#value IotTopicRule#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleHttpHttpHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleHttpHttpHeaderList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleHttpHttpHeaderList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f986be598d4ec06d08c29952fff20c0b06477fb4c6e543b408542712c2ca2756)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IotTopicRuleHttpHttpHeaderOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4aad8cc9853492fb70ee652291e4d86528de1b5cbc6c65333913edea6401343f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IotTopicRuleHttpHttpHeaderOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f4136b9f770c54a1cb71d261f2c8bd136067403a78271f572123960c334328a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c5a8d052cf5df4a7c24e4d1584e2567fa75347d300b3a28f737d239056e532bd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8f0ca92bbcb2772661644e97b706ef10a56b6392867b1ddb0c7365d77da39887)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleHttpHttpHeader]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleHttpHttpHeader]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleHttpHttpHeader]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7a52cfc8cc8d771e740bbc786a88805a775cbc76480f4aa823a60f6ce55f458)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotTopicRuleHttpHttpHeaderOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleHttpHttpHeaderOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3334f360abd3d74a73d324ae0bfda3782caa8bced8bb385eb15d5a1c298782bc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

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
            type_hints = typing.get_type_hints(_typecheckingstub__306b971728155806a599bb19feedf86c015660faa016045b9cd5a9366690d9d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29f9823c55c86a14a345d7ce94931c1cf5afd40c606c69f6a00c087938fde331)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IotTopicRuleHttpHttpHeader, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IotTopicRuleHttpHttpHeader, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IotTopicRuleHttpHttpHeader, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__022f2b9c831b30823570735680b6adacacfb4f7f2b6e8f5713ff2fa33346402a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotTopicRuleHttpList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleHttpList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__91157a56f9775b87e4db39f1ff35d52351682ab8d711273141ae2779456ff82a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IotTopicRuleHttpOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00718ec468b7b88740bbc75aa619954d3a9c0d3a5e1d4752c32ef2bc24f51a8e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IotTopicRuleHttpOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d3aec4f4bf40e75b9b99b6bf295cfaa494e47796c322ccdc854976bb1d1fb58)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4c53dc303a6e93a99b5967214a79054e71b70ef1f9e2b57d69eaafc320e655e9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6ceff604ad0715da9c81e6bf503ed59551c51e1e6f188a8ae0bc37f0b89b2852)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleHttp]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleHttp]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleHttp]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b133478023a384c2ce65728f139892bf9cc2bb627795517a1f4808c88043a0be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotTopicRuleHttpOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleHttpOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d0183c32ea196b01140956ddf7b6edaa48e5b37bbc6def79148ac85d2b18b788)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putHttpHeader")
    def put_http_header(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleHttpHttpHeader, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__773a08b337b5933de7b0ffe00d87e6a4580d36707abdc01829f6e14486904d21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHttpHeader", [value]))

    @jsii.member(jsii_name="resetConfirmationUrl")
    def reset_confirmation_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfirmationUrl", []))

    @jsii.member(jsii_name="resetHttpHeader")
    def reset_http_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpHeader", []))

    @builtins.property
    @jsii.member(jsii_name="httpHeader")
    def http_header(self) -> IotTopicRuleHttpHttpHeaderList:
        return typing.cast(IotTopicRuleHttpHttpHeaderList, jsii.get(self, "httpHeader"))

    @builtins.property
    @jsii.member(jsii_name="confirmationUrlInput")
    def confirmation_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "confirmationUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="httpHeaderInput")
    def http_header_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleHttpHttpHeader]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleHttpHttpHeader]]], jsii.get(self, "httpHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="confirmationUrl")
    def confirmation_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "confirmationUrl"))

    @confirmation_url.setter
    def confirmation_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5076580fe977b893f2f81f1415a9d5eecdb7d23407a074a09b2dd91689c13ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "confirmationUrl", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b6623866636d8adb9155afffa30907d83ec9d06801680b5899d390c1af280f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IotTopicRuleHttp, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IotTopicRuleHttp, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IotTopicRuleHttp, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6671b54164224b2b4a27d837b820b8c87685f98517655a7331a5f70775b8460)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleIotAnalytics",
    jsii_struct_bases=[],
    name_mapping={"channel_name": "channelName", "role_arn": "roleArn"},
)
class IotTopicRuleIotAnalytics:
    def __init__(self, *, channel_name: builtins.str, role_arn: builtins.str) -> None:
        '''
        :param channel_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#channel_name IotTopicRule#channel_name}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a18aada55e26b453433553747e391919fc19f6156cb247e4f4a56593f44622b)
            check_type(argname="argument channel_name", value=channel_name, expected_type=type_hints["channel_name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "channel_name": channel_name,
            "role_arn": role_arn,
        }

    @builtins.property
    def channel_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#channel_name IotTopicRule#channel_name}.'''
        result = self._values.get("channel_name")
        assert result is not None, "Required property 'channel_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleIotAnalytics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleIotAnalyticsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleIotAnalyticsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3252167bbeda1bc59c933801d6e466a523b08bcb6abd04f968d0015ed11b66f0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IotTopicRuleIotAnalyticsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1009ef484547b63ce1a07f923c1beacb9b5d9c005c8f3882d5b511ffa5ee0ab5)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IotTopicRuleIotAnalyticsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1a6e8a6d36c90d527d5a00c49ecc52b0e9857c5537731dad13eb1fbd863eb71)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ec66b6dcbb9a65e746724fc83723935663587885045ad664ed40df5c10a65877)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8fad7eff0f94e8aa53e132436b5a22a521a08d75fb864a195ebc2a7aee0f560c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleIotAnalytics]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleIotAnalytics]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleIotAnalytics]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfb55304fc0beadecc9cd5e6ae05a65d27b48faa51d5e101ab0e24766465dc23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotTopicRuleIotAnalyticsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleIotAnalyticsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7f43a188ae411250bb2b2b4c83d895254341fd075f07968f4297385b82b2c99b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="channelNameInput")
    def channel_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "channelNameInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="channelName")
    def channel_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "channelName"))

    @channel_name.setter
    def channel_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__590f30285a25fdbfd548d2a8ad3c709519e482b7ba2d468d44c691865bd413fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channelName", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1429a66545bc63d4796e930625a242d7e21316ee5aa8a799bf90272715700aec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IotTopicRuleIotAnalytics, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IotTopicRuleIotAnalytics, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IotTopicRuleIotAnalytics, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b7892c124d102efd801e00e1127dcb70163b86c0a23715e211ffb80056da2ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleIotEvents",
    jsii_struct_bases=[],
    name_mapping={
        "input_name": "inputName",
        "role_arn": "roleArn",
        "message_id": "messageId",
    },
)
class IotTopicRuleIotEvents:
    def __init__(
        self,
        *,
        input_name: builtins.str,
        role_arn: builtins.str,
        message_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param input_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#input_name IotTopicRule#input_name}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param message_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#message_id IotTopicRule#message_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__254a501600da0602ae86ef1710fd77ac450a441adba1b5b179b79e0cc39af057)
            check_type(argname="argument input_name", value=input_name, expected_type=type_hints["input_name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument message_id", value=message_id, expected_type=type_hints["message_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "input_name": input_name,
            "role_arn": role_arn,
        }
        if message_id is not None:
            self._values["message_id"] = message_id

    @builtins.property
    def input_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#input_name IotTopicRule#input_name}.'''
        result = self._values.get("input_name")
        assert result is not None, "Required property 'input_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def message_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#message_id IotTopicRule#message_id}.'''
        result = self._values.get("message_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleIotEvents(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleIotEventsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleIotEventsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__74c1503dddcccfc09e1a0cc23596bd564c4023f1b156a771b363272073cb96e8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IotTopicRuleIotEventsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dbbf90277025bde5f6a631b4d1165585ddfb23983158b8b555c9bb32744b45a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IotTopicRuleIotEventsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd1d3783b1790099b84d4d70e3d61a613d492d88770b5a04d922836935010e61)
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
            type_hints = typing.get_type_hints(_typecheckingstub__db8c1d2ca1329205556ac8e7026416387bf462ec8ee58238a0a5d65b8da88dd1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1a5c2b122d5fea45d4c753f0d61546b8b92683789b52906e60b97fa140c4ccf2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleIotEvents]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleIotEvents]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleIotEvents]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c627d64b825fcdbc46f7d48e264818d0453f68cdad4795f8a18eec68125e662a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotTopicRuleIotEventsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleIotEventsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f74ad1586a805e4149f8ee93b19f721a92552408666ee8a0d5aff1b7c35f0e02)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMessageId")
    def reset_message_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessageId", []))

    @builtins.property
    @jsii.member(jsii_name="inputNameInput")
    def input_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inputNameInput"))

    @builtins.property
    @jsii.member(jsii_name="messageIdInput")
    def message_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageIdInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="inputName")
    def input_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "inputName"))

    @input_name.setter
    def input_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b3c839f54511d900f73fd14634c1d40288ac3e74c8a0dbe7c2b327ffcd20765)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inputName", value)

    @builtins.property
    @jsii.member(jsii_name="messageId")
    def message_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "messageId"))

    @message_id.setter
    def message_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60ebf9a0bc7cae4afb9a2efdb5825951c58771635b51a4cabf003697e2a58cc2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messageId", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f566bbe4cc76d2e80593e89b47f10808f80e78ab5d643c8e9e8f68237acea4c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IotTopicRuleIotEvents, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IotTopicRuleIotEvents, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IotTopicRuleIotEvents, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d6c00752d022361480503e2acb25080382a0e4948d8db87e7e10a48aa1fc3ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleKafka",
    jsii_struct_bases=[],
    name_mapping={
        "client_properties": "clientProperties",
        "destination_arn": "destinationArn",
        "topic": "topic",
        "key": "key",
        "partition": "partition",
    },
)
class IotTopicRuleKafka:
    def __init__(
        self,
        *,
        client_properties: typing.Mapping[builtins.str, builtins.str],
        destination_arn: builtins.str,
        topic: builtins.str,
        key: typing.Optional[builtins.str] = None,
        partition: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#client_properties IotTopicRule#client_properties}.
        :param destination_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#destination_arn IotTopicRule#destination_arn}.
        :param topic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#topic IotTopicRule#topic}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#key IotTopicRule#key}.
        :param partition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#partition IotTopicRule#partition}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__939c6e09606c5c58470821a081e35b12bee5344a7cece6ac35a77fd641202a60)
            check_type(argname="argument client_properties", value=client_properties, expected_type=type_hints["client_properties"])
            check_type(argname="argument destination_arn", value=destination_arn, expected_type=type_hints["destination_arn"])
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument partition", value=partition, expected_type=type_hints["partition"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_properties": client_properties,
            "destination_arn": destination_arn,
            "topic": topic,
        }
        if key is not None:
            self._values["key"] = key
        if partition is not None:
            self._values["partition"] = partition

    @builtins.property
    def client_properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#client_properties IotTopicRule#client_properties}.'''
        result = self._values.get("client_properties")
        assert result is not None, "Required property 'client_properties' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    @builtins.property
    def destination_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#destination_arn IotTopicRule#destination_arn}.'''
        result = self._values.get("destination_arn")
        assert result is not None, "Required property 'destination_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def topic(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#topic IotTopicRule#topic}.'''
        result = self._values.get("topic")
        assert result is not None, "Required property 'topic' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#key IotTopicRule#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def partition(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#partition IotTopicRule#partition}.'''
        result = self._values.get("partition")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleKafka(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleKafkaList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleKafkaList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d2402914a4b76e05b6130e244852160a269766dd2f8b072b3592a24d4a035f41)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IotTopicRuleKafkaOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2104f72770ecd07ba8c9df2d7183f68973e0abcebbf94611263de28606452a98)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IotTopicRuleKafkaOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__504de0ea5295410886ed758616ff21452ae05d42924c7f7e7af17bf72fb864b1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__233510ec858d69aaa012690ee0a6cd46dbee40dcf441550afde21d6059c37ce0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2c7a619f2cdb7610aee97dd8b2b578f129e42383ccf4894b21fd773c769166c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleKafka]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleKafka]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleKafka]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfd7a651a950fd6a572208604aaa1806caa6b85073387b5f6e02a1cf76a422d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotTopicRuleKafkaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleKafkaOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a444ee39d982dca50ae5c9cba71cae318a90ff5cc1816786d5305d448a1eb734)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetPartition")
    def reset_partition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPartition", []))

    @builtins.property
    @jsii.member(jsii_name="clientPropertiesInput")
    def client_properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "clientPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationArnInput")
    def destination_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationArnInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionInput")
    def partition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "partitionInput"))

    @builtins.property
    @jsii.member(jsii_name="topicInput")
    def topic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "topicInput"))

    @builtins.property
    @jsii.member(jsii_name="clientProperties")
    def client_properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "clientProperties"))

    @client_properties.setter
    def client_properties(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__663bc1afe593220fd3cc00b92fddfd6e5bd03d06a6d4a5d2a6b9e7cf6325e43d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientProperties", value)

    @builtins.property
    @jsii.member(jsii_name="destinationArn")
    def destination_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationArn"))

    @destination_arn.setter
    def destination_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f2629f0c694aa07473b397ae5f45d6289ec008a06a5c7a5874b9d2e7a25a9d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationArn", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__726ff73d4d9457d0a4bd97950d08a19f108457c3d0a3c40e3ed4a1144d96d2ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="partition")
    def partition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "partition"))

    @partition.setter
    def partition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ae901b84ccf9abf85ed291958552871494e997bd96c6326d4c47ad7b21537e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partition", value)

    @builtins.property
    @jsii.member(jsii_name="topic")
    def topic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "topic"))

    @topic.setter
    def topic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05018ffd806f4191b38004ad6c70b0ad2e3e20bdbefea80543fe52bb60c22db2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "topic", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IotTopicRuleKafka, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IotTopicRuleKafka, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IotTopicRuleKafka, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3b540f569d773aec747eab3c6fcc9555cecd971f68fa8972b5184d0440ac99a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleKinesis",
    jsii_struct_bases=[],
    name_mapping={
        "role_arn": "roleArn",
        "stream_name": "streamName",
        "partition_key": "partitionKey",
    },
)
class IotTopicRuleKinesis:
    def __init__(
        self,
        *,
        role_arn: builtins.str,
        stream_name: builtins.str,
        partition_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param stream_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#stream_name IotTopicRule#stream_name}.
        :param partition_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#partition_key IotTopicRule#partition_key}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56a0f3ad7249d120423576c4cb1948c052d2d306eed4b7954431c03218724022)
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument stream_name", value=stream_name, expected_type=type_hints["stream_name"])
            check_type(argname="argument partition_key", value=partition_key, expected_type=type_hints["partition_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "role_arn": role_arn,
            "stream_name": stream_name,
        }
        if partition_key is not None:
            self._values["partition_key"] = partition_key

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stream_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#stream_name IotTopicRule#stream_name}.'''
        result = self._values.get("stream_name")
        assert result is not None, "Required property 'stream_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def partition_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#partition_key IotTopicRule#partition_key}.'''
        result = self._values.get("partition_key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleKinesis(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleKinesisList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleKinesisList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0511cb085b1d6745bd3ccfe9c8c8b99a7b94dc6371d046f9c959d07a2e2871c2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IotTopicRuleKinesisOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0831c395bbf4d72fdb3290aa0d7abba7d059163c618666af1815bcb8b297175)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IotTopicRuleKinesisOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43bb2968c0120986f35a82ebd89d0ae7092b504aa7aadc9c846efe22d0981fa7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d52b056bde63459e36cc659bd87424460e802ec345264f6858426d3aba3a72d8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d462b75c1e8956ebf24c0fe85a67c9ecd6db1d34edfaa7298c91e637bd6062b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleKinesis]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleKinesis]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleKinesis]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__767f1bca7782ab147ab648ae74954eadc47daf9826e1ab00860bc2208851e55e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotTopicRuleKinesisOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleKinesisOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6005258836eeb18e4f6c2856d95def58c27d3fa13699b56ebebbe74f7ab8d0f6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPartitionKey")
    def reset_partition_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPartitionKey", []))

    @builtins.property
    @jsii.member(jsii_name="partitionKeyInput")
    def partition_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "partitionKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="streamNameInput")
    def stream_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streamNameInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionKey")
    def partition_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "partitionKey"))

    @partition_key.setter
    def partition_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff2287f62a17604c619b48e749f7c5ed47cf6310af655bfafb7982ebf9f14774)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partitionKey", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d47624c6a9f7303d790fd43d6cc5e259e7dd55f1a90ac16e84046142a370404)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="streamName")
    def stream_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "streamName"))

    @stream_name.setter
    def stream_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6805c52eec1863b54c37df3f5be78f33f0e06aef1a6126fad89f759c4d8565d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IotTopicRuleKinesis, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IotTopicRuleKinesis, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IotTopicRuleKinesis, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec6fd1257a6081e7f349546a4a4929448b9971acf72df661fde5e3880cc1ffb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleLambda",
    jsii_struct_bases=[],
    name_mapping={"function_arn": "functionArn"},
)
class IotTopicRuleLambda:
    def __init__(self, *, function_arn: builtins.str) -> None:
        '''
        :param function_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#function_arn IotTopicRule#function_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__444a8148b0ea55648c1c84808a30d0ca8996f1ee4597b6ed2092b6b8e770dc1b)
            check_type(argname="argument function_arn", value=function_arn, expected_type=type_hints["function_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "function_arn": function_arn,
        }

    @builtins.property
    def function_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#function_arn IotTopicRule#function_arn}.'''
        result = self._values.get("function_arn")
        assert result is not None, "Required property 'function_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleLambda(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleLambdaList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleLambdaList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f3be24dcbc115724d0720e2703bd674acba5a1d44948015f61510df13cf520a3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IotTopicRuleLambdaOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10310d5cf8a10a33db541a35085f95dc4b8dac870ca095bd4a07d35a727af245)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IotTopicRuleLambdaOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c31abe63254aa251534d78d880661b1596c5c1a055aca48589f2b0f79f0d6832)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b152d8394f3183bdbac5291706ba6e7e5a69720251617a638dde9fc2b07f8ae1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__71f94270a0a45403fe21afbe9b0f21ae501e8094cf2f1793deb9d36e2125a7a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleLambda]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleLambda]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleLambda]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14abbac33de293233a32e066fb4f9dad6a7fee477192aa8fc0f7341fb6b281f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotTopicRuleLambdaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleLambdaOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9779f500ef7f0e11e38f698514f213cae9af4599c2004a77ca01ce3292982e5b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="functionArnInput")
    def function_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "functionArnInput"))

    @builtins.property
    @jsii.member(jsii_name="functionArn")
    def function_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "functionArn"))

    @function_arn.setter
    def function_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__877efabb5a8a1c665d7e60941b8bd01e4183289315d6108fcd985ebaad790066)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functionArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IotTopicRuleLambda, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IotTopicRuleLambda, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IotTopicRuleLambda, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a60336d3a21318b1046c5e6fbc1e97756ad45fd19fbe432407813ee025c03952)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleRepublish",
    jsii_struct_bases=[],
    name_mapping={"role_arn": "roleArn", "topic": "topic", "qos": "qos"},
)
class IotTopicRuleRepublish:
    def __init__(
        self,
        *,
        role_arn: builtins.str,
        topic: builtins.str,
        qos: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param topic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#topic IotTopicRule#topic}.
        :param qos: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#qos IotTopicRule#qos}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__693ac0773280dac8fe83cd4ddff30bbfe97e59843b7eca35ebb9a0d9c969f287)
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
            check_type(argname="argument qos", value=qos, expected_type=type_hints["qos"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "role_arn": role_arn,
            "topic": topic,
        }
        if qos is not None:
            self._values["qos"] = qos

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def topic(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#topic IotTopicRule#topic}.'''
        result = self._values.get("topic")
        assert result is not None, "Required property 'topic' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def qos(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#qos IotTopicRule#qos}.'''
        result = self._values.get("qos")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleRepublish(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleRepublishList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleRepublishList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b8fff5d65e0bc2b444842abd59c8ac5ff1afaf297eabbdc7496e1c61b33bde3a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IotTopicRuleRepublishOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84ce08791585773cff7adb5d4daf98662b6c0acdd3bcf0f8d88868f4fd3dc5be)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IotTopicRuleRepublishOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcbd270e059741021ed6ada15a9dcef454499418b6eaab396e89a275e1e2e899)
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
            type_hints = typing.get_type_hints(_typecheckingstub__71c6b36260e3a4cc7c43a6d0adf23f28a1c44b3e205ceacf0c3c2f912a2ed35a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2d25f4434d0f0fe335e37f227aff3d3b144dac2a67e7e6eb2c98185d6510b82b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleRepublish]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleRepublish]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleRepublish]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b799effe6e36e4495afaf4e33bdd7a40d38432ee7b7ea5831aee8b52ddf273d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotTopicRuleRepublishOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleRepublishOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__56f8b1aeb1aa50c488d9f8872b982ddf8f87c5686a3017fb45ab9152cc1ca3be)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetQos")
    def reset_qos(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQos", []))

    @builtins.property
    @jsii.member(jsii_name="qosInput")
    def qos_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "qosInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="topicInput")
    def topic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "topicInput"))

    @builtins.property
    @jsii.member(jsii_name="qos")
    def qos(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "qos"))

    @qos.setter
    def qos(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca62c1c3d64949c671dba098fd28958cc70ff4476e9a38b569211cf0371ab80e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "qos", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d36567cd676174bb9125e12055f5a60cc7aea60bfcb06e811dab1e34264e7757)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="topic")
    def topic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "topic"))

    @topic.setter
    def topic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f076f3626f7360e10c49d1aee3c5a78d3f411cd0b5d42da82b332dbf9424b7ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "topic", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IotTopicRuleRepublish, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IotTopicRuleRepublish, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IotTopicRuleRepublish, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60d05beb136e60c20acef8a4f90148b5b946cfea56609601838262bc952481a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleS3",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "key": "key",
        "role_arn": "roleArn",
        "canned_acl": "cannedAcl",
    },
)
class IotTopicRuleS3:
    def __init__(
        self,
        *,
        bucket_name: builtins.str,
        key: builtins.str,
        role_arn: builtins.str,
        canned_acl: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#bucket_name IotTopicRule#bucket_name}.
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#key IotTopicRule#key}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param canned_acl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#canned_acl IotTopicRule#canned_acl}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__278b808fdd515eeeb3f9cb3ce28373d3694e0d5e7ae31a82076e0c0802956725)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument canned_acl", value=canned_acl, expected_type=type_hints["canned_acl"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket_name": bucket_name,
            "key": key,
            "role_arn": role_arn,
        }
        if canned_acl is not None:
            self._values["canned_acl"] = canned_acl

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#bucket_name IotTopicRule#bucket_name}.'''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#key IotTopicRule#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def canned_acl(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#canned_acl IotTopicRule#canned_acl}.'''
        result = self._values.get("canned_acl")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleS3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleS3List(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleS3List",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c1e0e561312b989991f93588b89fb4b3484f59a1ec892be95f3e012677552c20)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IotTopicRuleS3OutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__786eb782474196818c6f8dcba547a250c5cf2f160d5739eb33246be4b59c056b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IotTopicRuleS3OutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27a554f9ad219c2916f39af234130ffe7015ff1726f42ab1d95173abec7c85a0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3b06eff4dde1eb02a328ba50f9a470829dbba74d4e60915058ce359fe124f602)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4331865b736b90597323bf79bdd5b8967072c04bacc4705a261c2d2c748a18e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleS3]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleS3]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleS3]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__904c4e4512c09c31f1f8ea1d01289489929ed9cea68a43b9cc5cf192f0f832d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotTopicRuleS3OutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleS3OutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3faa9991b0824ed40403f317e951ec5a3e75ccd801b9b83224945e6030ebf38b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCannedAcl")
    def reset_canned_acl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCannedAcl", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="cannedAclInput")
    def canned_acl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cannedAclInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fab121a779f5c9330a3896ba32b28171e601ff15325c5b268bab70b23ac05605)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="cannedAcl")
    def canned_acl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cannedAcl"))

    @canned_acl.setter
    def canned_acl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82fca1f5f64284e08fbdbbb6e335d1a6d3b6ba541aacadca253c1b156c8be0db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cannedAcl", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__147166cdb5205e28e24c2c68babf7a351f55145cfbb3266cdba6be27cb3daf1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8b743a002bf5ceba18849c8fb5df403d1ac75450157be4065245412e8891c53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IotTopicRuleS3, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IotTopicRuleS3, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IotTopicRuleS3, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__303723eed455051e32d232f9bab148e7af4135b988b1972c06b729e00f82b70c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleSns",
    jsii_struct_bases=[],
    name_mapping={
        "role_arn": "roleArn",
        "target_arn": "targetArn",
        "message_format": "messageFormat",
    },
)
class IotTopicRuleSns:
    def __init__(
        self,
        *,
        role_arn: builtins.str,
        target_arn: builtins.str,
        message_format: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param target_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#target_arn IotTopicRule#target_arn}.
        :param message_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#message_format IotTopicRule#message_format}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8f64e9924d03820b84763b08e6f142a2a82fc1af7f4472824d34e9ed8661f26)
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument target_arn", value=target_arn, expected_type=type_hints["target_arn"])
            check_type(argname="argument message_format", value=message_format, expected_type=type_hints["message_format"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "role_arn": role_arn,
            "target_arn": target_arn,
        }
        if message_format is not None:
            self._values["message_format"] = message_format

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#target_arn IotTopicRule#target_arn}.'''
        result = self._values.get("target_arn")
        assert result is not None, "Required property 'target_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def message_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#message_format IotTopicRule#message_format}.'''
        result = self._values.get("message_format")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleSns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleSnsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleSnsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b8d413a3c82c7717041db5eece87031dbffd8a1ca14440d3695df0ca1ae03f55)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IotTopicRuleSnsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61aa44ecbe7b4064e40670b3ba4220a0b3f3e6f9f59c303c883511bddb67d20e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IotTopicRuleSnsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbc049472fb52c97c480a701dea6349c9e86e1e9c5f84aa04fffec067a9bea21)
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
            type_hints = typing.get_type_hints(_typecheckingstub__46b0e468ebaf942fd29d61d146fbbb700d822cb57de70aa01d317e9480f696e5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9800dba56b7b82dd3ec673d9665486f8c8474f86a1adfb2fef443f54fe0acd47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleSns]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleSns]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleSns]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__355fd1f6399e50d0b817aecb37b827b104e8e37aad0262b2acfb27735bb1e754)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotTopicRuleSnsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleSnsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3ce42198c41d752d795ad8736656d300a1bebccd3dbc421340b9515f83fe658e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMessageFormat")
    def reset_message_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessageFormat", []))

    @builtins.property
    @jsii.member(jsii_name="messageFormatInput")
    def message_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="targetArnInput")
    def target_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetArnInput"))

    @builtins.property
    @jsii.member(jsii_name="messageFormat")
    def message_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "messageFormat"))

    @message_format.setter
    def message_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03721972a9de0f5a617fd97cb4aecc6a99bb6475274898860dad3f2f5b05dfd9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messageFormat", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de2493b3e7a8fb4b59841bfc18be827ccd18c8dea4d6585f83bb5eb249ca9464)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="targetArn")
    def target_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetArn"))

    @target_arn.setter
    def target_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e56a861fef6a27a5c1a7e4e169f346f18cc665421e2f4e7e089a67a8cb923f8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IotTopicRuleSns, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IotTopicRuleSns, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IotTopicRuleSns, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__039aab66ba1eef944d2d84f0d3650e10a98fa3d83e1c685b699f73a3e63098ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleSqs",
    jsii_struct_bases=[],
    name_mapping={
        "queue_url": "queueUrl",
        "role_arn": "roleArn",
        "use_base64": "useBase64",
    },
)
class IotTopicRuleSqs:
    def __init__(
        self,
        *,
        queue_url: builtins.str,
        role_arn: builtins.str,
        use_base64: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        '''
        :param queue_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#queue_url IotTopicRule#queue_url}.
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param use_base64: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#use_base64 IotTopicRule#use_base64}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5502758d88d4791c409d5b11e70d84c558f393950bc6b0d1b03883423c517494)
            check_type(argname="argument queue_url", value=queue_url, expected_type=type_hints["queue_url"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument use_base64", value=use_base64, expected_type=type_hints["use_base64"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "queue_url": queue_url,
            "role_arn": role_arn,
            "use_base64": use_base64,
        }

    @builtins.property
    def queue_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#queue_url IotTopicRule#queue_url}.'''
        result = self._values.get("queue_url")
        assert result is not None, "Required property 'queue_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def use_base64(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#use_base64 IotTopicRule#use_base64}.'''
        result = self._values.get("use_base64")
        assert result is not None, "Required property 'use_base64' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleSqs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleSqsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleSqsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3c2a8b18726ca5026fda31bc72080a7a4332eaf7de1cb27906510aeefb849c48)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IotTopicRuleSqsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bac9e142d0bf7566f7a2358e43478261b1fe461d2e0cc87054b49c7c86ea8198)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IotTopicRuleSqsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20a6c80194721f0ef212035f1b72bd098014f44c63e7b98c124f6e16b1c5df45)
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
            type_hints = typing.get_type_hints(_typecheckingstub__81dcbdf8f2124d49ea8e2be5368a7d36ca4fbadc45c1f2117d3337870481bf34)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d3f68e37b2585461d9db30e7abab8d003f9e4b53266ea60802dd5f049d9021b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleSqs]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleSqs]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleSqs]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a0d1c5b321b30c868cbc3d6c815a25e3aa3a687cca640c2473f9c70f968676e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotTopicRuleSqsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleSqsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__14e04648e1f40274baea56dabcd582d216a5d0204b1360c4ab4cb86c4c950f0a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="queueUrlInput")
    def queue_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queueUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="useBase64Input")
    def use_base64_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "useBase64Input"))

    @builtins.property
    @jsii.member(jsii_name="queueUrl")
    def queue_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "queueUrl"))

    @queue_url.setter
    def queue_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__853a402c47af3f6e1612fcc56026dedcb84b13b195862570c1eeb1402c2183ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queueUrl", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06b2aece64cd5bf972ef5931909bd33cf655d8bfd4bbec5184a57d0afa3e1f59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="useBase64")
    def use_base64(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "useBase64"))

    @use_base64.setter
    def use_base64(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d68939543055d711b157707f18661671d44d7a8bf4eb7b96e39b408832e0b502)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useBase64", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IotTopicRuleSqs, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IotTopicRuleSqs, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IotTopicRuleSqs, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17acc6fe6754c9dc8ab5c8559ad0004a7186761740827c82d96629d1f25637a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleStepFunctions",
    jsii_struct_bases=[],
    name_mapping={
        "role_arn": "roleArn",
        "state_machine_name": "stateMachineName",
        "execution_name_prefix": "executionNamePrefix",
    },
)
class IotTopicRuleStepFunctions:
    def __init__(
        self,
        *,
        role_arn: builtins.str,
        state_machine_name: builtins.str,
        execution_name_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param state_machine_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#state_machine_name IotTopicRule#state_machine_name}.
        :param execution_name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#execution_name_prefix IotTopicRule#execution_name_prefix}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__539cb6f2a0e3f86d8abf5c26161a9bf18a7d72e685672e700b2afc33da32b506)
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument state_machine_name", value=state_machine_name, expected_type=type_hints["state_machine_name"])
            check_type(argname="argument execution_name_prefix", value=execution_name_prefix, expected_type=type_hints["execution_name_prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "role_arn": role_arn,
            "state_machine_name": state_machine_name,
        }
        if execution_name_prefix is not None:
            self._values["execution_name_prefix"] = execution_name_prefix

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def state_machine_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#state_machine_name IotTopicRule#state_machine_name}.'''
        result = self._values.get("state_machine_name")
        assert result is not None, "Required property 'state_machine_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def execution_name_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#execution_name_prefix IotTopicRule#execution_name_prefix}.'''
        result = self._values.get("execution_name_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleStepFunctions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleStepFunctionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleStepFunctionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__af55709db4f21d59ce288423741db905cb0317c6cda8d340fb254b58268356fe)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IotTopicRuleStepFunctionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3ef77718c7c0b6f13fa0b4be29ad5d37aed1a0d115b40fc5b3467f096e6f12c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IotTopicRuleStepFunctionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92e0e97be9852ad73089e8f7841b59908cbea4c7e894a56bd525027a8370bca8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7cbb7c1e3551185cdb22fc85e9ef7de1c70d6678bf72b34ec4a81460ec756acc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4904aa8d6028fe4d8f3930a2829769c3e1f2ba37c9eb74ccf8da1518d51d6873)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleStepFunctions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleStepFunctions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleStepFunctions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11fc38ff68d8c9ffd296400caf6d0a0264ac8df1ce7dd648d483c417738a119e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotTopicRuleStepFunctionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleStepFunctionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0b80e9dc0cbaadd9e3fe9ac7acd3732188a8c0cb70130aee63162c08c8c3f4f1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetExecutionNamePrefix")
    def reset_execution_name_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExecutionNamePrefix", []))

    @builtins.property
    @jsii.member(jsii_name="executionNamePrefixInput")
    def execution_name_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionNamePrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="stateMachineNameInput")
    def state_machine_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateMachineNameInput"))

    @builtins.property
    @jsii.member(jsii_name="executionNamePrefix")
    def execution_name_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "executionNamePrefix"))

    @execution_name_prefix.setter
    def execution_name_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ab6c132edaa774d316e85872a7bd4085510abbdc675290da8f096d4ba1f847b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionNamePrefix", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1caa748e270388908c75ffd7f2f65735bf405de878ee676cae4afdf39c4b4857)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="stateMachineName")
    def state_machine_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stateMachineName"))

    @state_machine_name.setter
    def state_machine_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dde41202c8b26e7fed44eccc62aecae43e36fa7bdd023b7d0dfdafe15e959b44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stateMachineName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IotTopicRuleStepFunctions, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IotTopicRuleStepFunctions, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IotTopicRuleStepFunctions, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b25c37b5a1f9bb9d4e219c20d1954725af3117ea3673b290acb39e9fbf21c2ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleTimestream",
    jsii_struct_bases=[],
    name_mapping={
        "database_name": "databaseName",
        "dimension": "dimension",
        "role_arn": "roleArn",
        "table_name": "tableName",
        "timestamp": "timestamp",
    },
)
class IotTopicRuleTimestream:
    def __init__(
        self,
        *,
        database_name: builtins.str,
        dimension: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["IotTopicRuleTimestreamDimension", typing.Dict[builtins.str, typing.Any]]]],
        role_arn: builtins.str,
        table_name: builtins.str,
        timestamp: typing.Optional[typing.Union["IotTopicRuleTimestreamTimestamp", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#database_name IotTopicRule#database_name}.
        :param dimension: dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#dimension IotTopicRule#dimension}
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.
        :param table_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#table_name IotTopicRule#table_name}.
        :param timestamp: timestamp block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#timestamp IotTopicRule#timestamp}
        '''
        if isinstance(timestamp, dict):
            timestamp = IotTopicRuleTimestreamTimestamp(**timestamp)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5855fba72116793c9a92f2f2fc753000542de19b61554e7eb276b6f858eb6af)
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument dimension", value=dimension, expected_type=type_hints["dimension"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            check_type(argname="argument timestamp", value=timestamp, expected_type=type_hints["timestamp"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database_name": database_name,
            "dimension": dimension,
            "role_arn": role_arn,
            "table_name": table_name,
        }
        if timestamp is not None:
            self._values["timestamp"] = timestamp

    @builtins.property
    def database_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#database_name IotTopicRule#database_name}.'''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dimension(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleTimestreamDimension"]]:
        '''dimension block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#dimension IotTopicRule#dimension}
        '''
        result = self._values.get("dimension")
        assert result is not None, "Required property 'dimension' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["IotTopicRuleTimestreamDimension"]], result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#role_arn IotTopicRule#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#table_name IotTopicRule#table_name}.'''
        result = self._values.get("table_name")
        assert result is not None, "Required property 'table_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def timestamp(self) -> typing.Optional["IotTopicRuleTimestreamTimestamp"]:
        '''timestamp block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#timestamp IotTopicRule#timestamp}
        '''
        result = self._values.get("timestamp")
        return typing.cast(typing.Optional["IotTopicRuleTimestreamTimestamp"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleTimestream(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleTimestreamDimension",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class IotTopicRuleTimestreamDimension:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#name IotTopicRule#name}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#value IotTopicRule#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea8d8a5a09a82c4cddfacb32208466adb0ea08e8d2de6086e8d9b351ae3dfc22)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#name IotTopicRule#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#value IotTopicRule#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleTimestreamDimension(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleTimestreamDimensionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleTimestreamDimensionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__38e08d36894fce4ce11f94da09ae131cbcd60c7f1f109ebb745681ccac57f0f7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "IotTopicRuleTimestreamDimensionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a613d5231032f90608f3be4d82949d6313442973dfa14f0cfa787af53aa99603)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IotTopicRuleTimestreamDimensionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f81ba832dcc2597bf19c861c114609aed9f79f447431d5cf035f67dd0ad9ad15)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4c6b4e97071aa48707a96c9ffa2907cb7754ee415eddff526e2181aa0e563a2b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dc48e47a1fa152ea698e35e737e01e4252396b41bf8450fbf23433cf76ff681c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleTimestreamDimension]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleTimestreamDimension]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleTimestreamDimension]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54ffa7610424aad1b0217fd63d6071419305578d12bb41f9f1c8366790905c2f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotTopicRuleTimestreamDimensionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleTimestreamDimensionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1962c9cd131af0cfa59692d641bbbda3da3f17d96ea3d79b5a3d9e8dc40b3639)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e980935adf7078fd524060e7022a70c195ed64cca2c75c9402ca3008eb2bcbd1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7e044036abde0b84c0c63bac503b76054e7f658196be88183142879d05aa4a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IotTopicRuleTimestreamDimension, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IotTopicRuleTimestreamDimension, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IotTopicRuleTimestreamDimension, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4aa1054b4fa9d18bc8d001406c46570e83282efb6f318303b2928ecbfe6105e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotTopicRuleTimestreamList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleTimestreamList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9002d3d4290e5390887e784c5c8184eb9cb244d11fc57bda00e09e6ca79d9fa0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "IotTopicRuleTimestreamOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c788a3fee20b924e540a3b252c8b0dd0fee6ba99ea95ed0fabc4b34c4f80d3e8)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("IotTopicRuleTimestreamOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93ea24a15b6bff23d9e609ec1e816c29f748d125f49cfe295b5bfdbb6ebdb969)
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
            type_hints = typing.get_type_hints(_typecheckingstub__250efad6b384f061436c45738feb20cc091836a6bf69496ad3c0ace24d5c58c1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bdcdba43bd1b7f0ff20367d7f9814bbfc07d61b2c44c9dc93a19274fe2276f97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleTimestream]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleTimestream]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleTimestream]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c64723e609c7657eb3f5a89d282a9c7f3cbb607a030cc00716b56207665981b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class IotTopicRuleTimestreamOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleTimestreamOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ed24720c43d6d8137596d34c8fa25263dac594fde8d5ee53ef09813dfac6d9bf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDimension")
    def put_dimension(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleTimestreamDimension, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e5705a3136d4544e99444625c8b641114eff7474bfc3f0cbedddf990b5f3fca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDimension", [value]))

    @jsii.member(jsii_name="putTimestamp")
    def put_timestamp(self, *, unit: builtins.str, value: builtins.str) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#unit IotTopicRule#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#value IotTopicRule#value}.
        '''
        value_ = IotTopicRuleTimestreamTimestamp(unit=unit, value=value)

        return typing.cast(None, jsii.invoke(self, "putTimestamp", [value_]))

    @jsii.member(jsii_name="resetTimestamp")
    def reset_timestamp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimestamp", []))

    @builtins.property
    @jsii.member(jsii_name="dimension")
    def dimension(self) -> IotTopicRuleTimestreamDimensionList:
        return typing.cast(IotTopicRuleTimestreamDimensionList, jsii.get(self, "dimension"))

    @builtins.property
    @jsii.member(jsii_name="timestamp")
    def timestamp(self) -> "IotTopicRuleTimestreamTimestampOutputReference":
        return typing.cast("IotTopicRuleTimestreamTimestampOutputReference", jsii.get(self, "timestamp"))

    @builtins.property
    @jsii.member(jsii_name="databaseNameInput")
    def database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="dimensionInput")
    def dimension_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleTimestreamDimension]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleTimestreamDimension]]], jsii.get(self, "dimensionInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="tableNameInput")
    def table_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableNameInput"))

    @builtins.property
    @jsii.member(jsii_name="timestampInput")
    def timestamp_input(self) -> typing.Optional["IotTopicRuleTimestreamTimestamp"]:
        return typing.cast(typing.Optional["IotTopicRuleTimestreamTimestamp"], jsii.get(self, "timestampInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4230cee6f6398a5cd4b9c1ac7f1f9ce3d111428d9b9ed68628ed57ae0902361f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c01661dc68219e96791b6c4cec7a4c9800193ff3259fd56eac8e9a86fdf41258)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="tableName")
    def table_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableName"))

    @table_name.setter
    def table_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef31da477c459ca3d33b2ce1e5f5655cd308bbb599960ad6b41185fb89764993)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[IotTopicRuleTimestream, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[IotTopicRuleTimestream, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[IotTopicRuleTimestream, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__768f96fcc93916519ce6253492ad7fe05a80e23444cc2c23147f0716cad99ace)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="aws.iotTopicRule.IotTopicRuleTimestreamTimestamp",
    jsii_struct_bases=[],
    name_mapping={"unit": "unit", "value": "value"},
)
class IotTopicRuleTimestreamTimestamp:
    def __init__(self, *, unit: builtins.str, value: builtins.str) -> None:
        '''
        :param unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#unit IotTopicRule#unit}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#value IotTopicRule#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__973897989e7ab48fb5e3316954309aef8c4b5995566dd16e79fcafb311faa3f8)
            check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "unit": unit,
            "value": value,
        }

    @builtins.property
    def unit(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#unit IotTopicRule#unit}.'''
        result = self._values.get("unit")
        assert result is not None, "Required property 'unit' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/iot_topic_rule#value IotTopicRule#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IotTopicRuleTimestreamTimestamp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class IotTopicRuleTimestreamTimestampOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.iotTopicRule.IotTopicRuleTimestreamTimestampOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0edba47494521c805541d50692e73d4cc08d2bad020167bdc988cc06e3910328)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="unitInput")
    def unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unitInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="unit")
    def unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unit"))

    @unit.setter
    def unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30efa27d4e1e25c8ffc2a0d30c04900220e861fc357f09086ac32cebd0bf93ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unit", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d27f06c3ff5262ba6eeae4aea554799790537509643bdb5eee2e934584f87985)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[IotTopicRuleTimestreamTimestamp]:
        return typing.cast(typing.Optional[IotTopicRuleTimestreamTimestamp], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[IotTopicRuleTimestreamTimestamp],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1637b41ad61a096c99e953e3139a6b9cb2f73b2e4706ffb89bb999e1d2a6a99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "IotTopicRule",
    "IotTopicRuleCloudwatchAlarm",
    "IotTopicRuleCloudwatchAlarmList",
    "IotTopicRuleCloudwatchAlarmOutputReference",
    "IotTopicRuleCloudwatchLogs",
    "IotTopicRuleCloudwatchLogsList",
    "IotTopicRuleCloudwatchLogsOutputReference",
    "IotTopicRuleCloudwatchMetric",
    "IotTopicRuleCloudwatchMetricList",
    "IotTopicRuleCloudwatchMetricOutputReference",
    "IotTopicRuleConfig",
    "IotTopicRuleDynamodb",
    "IotTopicRuleDynamodbList",
    "IotTopicRuleDynamodbOutputReference",
    "IotTopicRuleDynamodbv2",
    "IotTopicRuleDynamodbv2List",
    "IotTopicRuleDynamodbv2OutputReference",
    "IotTopicRuleDynamodbv2PutItem",
    "IotTopicRuleDynamodbv2PutItemOutputReference",
    "IotTopicRuleElasticsearch",
    "IotTopicRuleElasticsearchList",
    "IotTopicRuleElasticsearchOutputReference",
    "IotTopicRuleErrorAction",
    "IotTopicRuleErrorActionCloudwatchAlarm",
    "IotTopicRuleErrorActionCloudwatchAlarmOutputReference",
    "IotTopicRuleErrorActionCloudwatchLogs",
    "IotTopicRuleErrorActionCloudwatchLogsOutputReference",
    "IotTopicRuleErrorActionCloudwatchMetric",
    "IotTopicRuleErrorActionCloudwatchMetricOutputReference",
    "IotTopicRuleErrorActionDynamodb",
    "IotTopicRuleErrorActionDynamodbOutputReference",
    "IotTopicRuleErrorActionDynamodbv2",
    "IotTopicRuleErrorActionDynamodbv2OutputReference",
    "IotTopicRuleErrorActionDynamodbv2PutItem",
    "IotTopicRuleErrorActionDynamodbv2PutItemOutputReference",
    "IotTopicRuleErrorActionElasticsearch",
    "IotTopicRuleErrorActionElasticsearchOutputReference",
    "IotTopicRuleErrorActionFirehose",
    "IotTopicRuleErrorActionFirehoseOutputReference",
    "IotTopicRuleErrorActionHttp",
    "IotTopicRuleErrorActionHttpHttpHeader",
    "IotTopicRuleErrorActionHttpHttpHeaderList",
    "IotTopicRuleErrorActionHttpHttpHeaderOutputReference",
    "IotTopicRuleErrorActionHttpOutputReference",
    "IotTopicRuleErrorActionIotAnalytics",
    "IotTopicRuleErrorActionIotAnalyticsOutputReference",
    "IotTopicRuleErrorActionIotEvents",
    "IotTopicRuleErrorActionIotEventsOutputReference",
    "IotTopicRuleErrorActionKafka",
    "IotTopicRuleErrorActionKafkaOutputReference",
    "IotTopicRuleErrorActionKinesis",
    "IotTopicRuleErrorActionKinesisOutputReference",
    "IotTopicRuleErrorActionLambda",
    "IotTopicRuleErrorActionLambdaOutputReference",
    "IotTopicRuleErrorActionOutputReference",
    "IotTopicRuleErrorActionRepublish",
    "IotTopicRuleErrorActionRepublishOutputReference",
    "IotTopicRuleErrorActionS3",
    "IotTopicRuleErrorActionS3OutputReference",
    "IotTopicRuleErrorActionSns",
    "IotTopicRuleErrorActionSnsOutputReference",
    "IotTopicRuleErrorActionSqs",
    "IotTopicRuleErrorActionSqsOutputReference",
    "IotTopicRuleErrorActionStepFunctions",
    "IotTopicRuleErrorActionStepFunctionsOutputReference",
    "IotTopicRuleErrorActionTimestream",
    "IotTopicRuleErrorActionTimestreamDimension",
    "IotTopicRuleErrorActionTimestreamDimensionList",
    "IotTopicRuleErrorActionTimestreamDimensionOutputReference",
    "IotTopicRuleErrorActionTimestreamOutputReference",
    "IotTopicRuleErrorActionTimestreamTimestamp",
    "IotTopicRuleErrorActionTimestreamTimestampOutputReference",
    "IotTopicRuleFirehose",
    "IotTopicRuleFirehoseList",
    "IotTopicRuleFirehoseOutputReference",
    "IotTopicRuleHttp",
    "IotTopicRuleHttpHttpHeader",
    "IotTopicRuleHttpHttpHeaderList",
    "IotTopicRuleHttpHttpHeaderOutputReference",
    "IotTopicRuleHttpList",
    "IotTopicRuleHttpOutputReference",
    "IotTopicRuleIotAnalytics",
    "IotTopicRuleIotAnalyticsList",
    "IotTopicRuleIotAnalyticsOutputReference",
    "IotTopicRuleIotEvents",
    "IotTopicRuleIotEventsList",
    "IotTopicRuleIotEventsOutputReference",
    "IotTopicRuleKafka",
    "IotTopicRuleKafkaList",
    "IotTopicRuleKafkaOutputReference",
    "IotTopicRuleKinesis",
    "IotTopicRuleKinesisList",
    "IotTopicRuleKinesisOutputReference",
    "IotTopicRuleLambda",
    "IotTopicRuleLambdaList",
    "IotTopicRuleLambdaOutputReference",
    "IotTopicRuleRepublish",
    "IotTopicRuleRepublishList",
    "IotTopicRuleRepublishOutputReference",
    "IotTopicRuleS3",
    "IotTopicRuleS3List",
    "IotTopicRuleS3OutputReference",
    "IotTopicRuleSns",
    "IotTopicRuleSnsList",
    "IotTopicRuleSnsOutputReference",
    "IotTopicRuleSqs",
    "IotTopicRuleSqsList",
    "IotTopicRuleSqsOutputReference",
    "IotTopicRuleStepFunctions",
    "IotTopicRuleStepFunctionsList",
    "IotTopicRuleStepFunctionsOutputReference",
    "IotTopicRuleTimestream",
    "IotTopicRuleTimestreamDimension",
    "IotTopicRuleTimestreamDimensionList",
    "IotTopicRuleTimestreamDimensionOutputReference",
    "IotTopicRuleTimestreamList",
    "IotTopicRuleTimestreamOutputReference",
    "IotTopicRuleTimestreamTimestamp",
    "IotTopicRuleTimestreamTimestampOutputReference",
]

publication.publish()

def _typecheckingstub__53670b127d5862e8066940465f5e310da6ce613316c0feb9e07d3e802c4a9be4(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    name: builtins.str,
    sql: builtins.str,
    sql_version: builtins.str,
    cloudwatch_alarm: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleCloudwatchAlarm, typing.Dict[builtins.str, typing.Any]]]]] = None,
    cloudwatch_logs: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleCloudwatchLogs, typing.Dict[builtins.str, typing.Any]]]]] = None,
    cloudwatch_metric: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleCloudwatchMetric, typing.Dict[builtins.str, typing.Any]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    dynamodb: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleDynamodb, typing.Dict[builtins.str, typing.Any]]]]] = None,
    dynamodbv2: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleDynamodbv2, typing.Dict[builtins.str, typing.Any]]]]] = None,
    elasticsearch: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleElasticsearch, typing.Dict[builtins.str, typing.Any]]]]] = None,
    error_action: typing.Optional[typing.Union[IotTopicRuleErrorAction, typing.Dict[builtins.str, typing.Any]]] = None,
    firehose: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleFirehose, typing.Dict[builtins.str, typing.Any]]]]] = None,
    http: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleHttp, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    iot_analytics: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleIotAnalytics, typing.Dict[builtins.str, typing.Any]]]]] = None,
    iot_events: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleIotEvents, typing.Dict[builtins.str, typing.Any]]]]] = None,
    kafka: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleKafka, typing.Dict[builtins.str, typing.Any]]]]] = None,
    kinesis: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleKinesis, typing.Dict[builtins.str, typing.Any]]]]] = None,
    lambda_: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleLambda, typing.Dict[builtins.str, typing.Any]]]]] = None,
    republish: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleRepublish, typing.Dict[builtins.str, typing.Any]]]]] = None,
    s3: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleS3, typing.Dict[builtins.str, typing.Any]]]]] = None,
    sns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleSns, typing.Dict[builtins.str, typing.Any]]]]] = None,
    sqs: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleSqs, typing.Dict[builtins.str, typing.Any]]]]] = None,
    step_functions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleStepFunctions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timestream: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleTimestream, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__362133bd6a35384a3c62d526dd83a4fedf91c37edbaedcc8ae2bd418367d6362(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleCloudwatchAlarm, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eaa53f1f517b762ecce5381dced00415e52204e2fd19b2972f205933e95f844b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleCloudwatchLogs, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5f77882f27a17d3981f2b0e808646e312ab73e3ef5ab472dca280ff57a63ce9(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleCloudwatchMetric, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edf76234c332849f67d25b8170310da07b926bf51455d2abab8f267470337500(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleDynamodb, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bfb0dca78e7d87ca039dbd7c4696677715921f4c61ccb4d5785a7af2dcba029(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleDynamodbv2, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b93fd828f0f89be54d9f98cbe44ee62fac68487e760b15a6f45337bf7bd42c3f(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleElasticsearch, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__884bf8faf6d9af52bd22a9d972b81205014382bb7c299dd1819717902623dcd7(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleFirehose, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbd55a917d80427c9c1994232fe8b47685eef47e9766039a213b6988af7ec4fd(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleHttp, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a2b8464aa1eec963de08aa62422be98c48b2cb8e4b8c89986777e5060573b74(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleIotAnalytics, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75742a7bf0f72261f82396af77d5a3e6f25ee5f610e0fdd026d2a32dd9dd947e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleIotEvents, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac2ac3e81225d7f8b22c765865c010ac56bf50b0a202c257d8158af333cb9d52(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleKafka, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e0e805681e2c0f904591f06a365a590a23a24cc203e3d16e85373ecddd44961(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleKinesis, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9715a0f1d1c15cb4a3c0dc3da760da74be6c9226d3dff46b85e317e1fe20f583(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleLambda, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__708984d01363a1cb9ef913783c71f8f61a9dee6580aa92b75e7109764d78b1e5(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleRepublish, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__caf02f248ff59e8fc4baeb94038cea8ff9a5c0f9a08f49b367388128dff6576e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleS3, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1575481ec878c11843cb1669f8a8d2c4a5a802e4f8ad0bda5753cd57802ff2e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleSns, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d0f4edf83575d39f709458730769364a836e07c7975df6b565d368aeb3062e0(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleSqs, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97d660355f2d7f2271a0fa6a5f334dd56a11ee0ae93f8c2eb0917ae9b1832dd8(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleStepFunctions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8de221367533070bdc5ac62657c33a2fb94de45c44118a63a72cff460f17516c(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleTimestream, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a0da180c557fdef7eeaf6d4b844e4dc9fbe666354f663cc3cc3e281f56e6077(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1002bc4cffc024a4405efa40cce3cf0fc3b5b9866d2d8c14f74a0b7b9186a590(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2b0360bc44b65c198f54b15f5d937c1c567b77fde48b8aa97a28626dd672f9b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2957c80c30e05362fcfdb576136858fc42869f97a541e75fb7cff3fadd1f6052(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb8750cf5edda0dba5f823f79018bc9e0ff9f484e6f2f034eb9b28f221790a12(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc07501312f7cdb84f4591fd4cced1bfa43432c2b16dc0a34dbdf49ec16d4489(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c82e9ef65111369fc0838abd2d439e2ceb2260e5bbab0595ec48dfc18abe1fff(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8353f54931a3ea375dbae39671085de3b1d9dbeb5438a3f83d01952e5cc957f(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa6578e7a9dfa1954c43c27b2392ffe8d3ff2e44e8e023c853dcfcd8446c5b49(
    *,
    alarm_name: builtins.str,
    role_arn: builtins.str,
    state_reason: builtins.str,
    state_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__753d921f45aaa4a54d24f911c286ed849d6356f31893a6b1e1a36b733ab300f2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ce3c53a500fa317efdbc15cb8dadaa4551706db16fff5ff6bd293bc2868836c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88b8e66ea55a2fdbf22649da9087aefa1dfa56d1df9ce83415ca9261949f1c3d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e83ac6a5f7be8da0eea80fdf8de7e2997ea7584057e9c3a9d9198e5116cbd5b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4102c2f52dba01eee128e192a176a7d09688b4783bc8b9022062767cd0aeb94b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89872d1a0f337ab1974ec14a3b2bc04a68ca2b55c97649ec95566a2cfe38ee09(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleCloudwatchAlarm]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e4b802d5a98a745397997e1a816e10646abc5dd0618f791e4d21fdff0949962(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d02d2e84a547903ff847b9da4b074c1df42f15941205cfd39258ccf24518077b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39bd7145c97c0947f3e9252f9ff81e3818ce79bcb6afca61446bff76d01d5835(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d837777cf35bb33a82c72ed82f3346b8d41f096890bb521196e2252709115d5e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f80ecae0ca2258dcd27bcda5e09972b418a04341ac2bfff923abe0e64b8cfd6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1dc8964e123fceb289cb65b11575d258ca6f168aa51cb8988466d346fedf23df(
    value: typing.Optional[typing.Union[IotTopicRuleCloudwatchAlarm, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77878ec06107c8ff2f70638bcd84a18b18cfd86c2b86995f856d50cd36c302ff(
    *,
    log_group_name: builtins.str,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52f6945e1ee95e5d5a7d56a97dbd58f577570b535e40ef9b6d7fc8b14d811047(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b48c398a6000ed19be64b3a7348384a21d6a9f8a068509c501f2ebb645fbbd4(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfb8c4a0e5d11e364cfcba923fa56365e13a83297987a9f35ef79b59db67d60c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab660c414082a205ad00ab390c4135d800beceefef180028edf393ffc8e9254e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4735b07201d8ad7bdeec1b7c1e8d744adfde2cde3e8d1e8c7e0c001d8a86346(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea4fb66286bae9d01c5aed5905ca8554f8441c97e15af8765109fa54b41d3492(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleCloudwatchLogs]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85cd0ce1ad6e72cfb44d343bc59eaa4189b5d1d9826eca8edb596886d97d41da(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69fe600bf047ea635d46b2afc7c029d62df44a74598880367283aa99c4704943(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a355274c599434c80dfb9eb51afa5f74f8a3e02637c14c28b61c86b3a2cb600(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf98daa05ee4b73ad6078c2d7ec46c29f92c5b4fd17fb6663a84194c390cba08(
    value: typing.Optional[typing.Union[IotTopicRuleCloudwatchLogs, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fc19df14d506b09a7babef300bfea1e701e270c883f45a09f61d5d8169040d9(
    *,
    metric_name: builtins.str,
    metric_namespace: builtins.str,
    metric_unit: builtins.str,
    metric_value: builtins.str,
    role_arn: builtins.str,
    metric_timestamp: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb3fb08a1312c7c68e7bed752c5c3834cf42d613bed55e6f5a601c94a3ac6066(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c818d4716064284b2e398447f28cc0ec6a6c6d38ffa3827bad1f39ecf5240b3(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c5110b499a6effa47b74225fb76ebc5b3c59d9ef36d85c683d5e35d45d2fdeb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc5e62b93f0f2de780710befecbdeb98e372185d8ab354af9f05d07da0c33806(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2064795aa8e7ce4d9cdf88fb39bcaaccec151461eb495bc48797d79aab1d5407(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1aaf5e99a5f7244fef1b31477e976b77c1c6448fd28e62367dec01b151ee603(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleCloudwatchMetric]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d2c3cbb27871e5eaf24a3d59dc4e26132f97808e6d855e1098200f17c7a5fda(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2e8c37309cffa76bbdfb03cff33d8c73557ec9b7b742821c197781b317fe3b5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__407c038387911201db8e67ca268e127ec12f6131b9134cf5cad992291e4d48de(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cdaf86e150a38a6ae34d4600ce18a79e482308fc37dadcfbeae1f01457672a5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b8b2a8dc096928b8ed25db0305844693ea39d35970097649489d769415490e7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c1ced0cf34ed15e1923e6c76668230036eca1c6b2cd5338ae6d557d24038917(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8310817fdce28a1df7093af85d7cdf6144aa4c0795cdea082ca5355be3e55578(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e3f9b80443e4fbcba16891695564d5602cb8ca7f4dc52807818febbb8b84292(
    value: typing.Optional[typing.Union[IotTopicRuleCloudwatchMetric, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9d70340d517c3df6cbffd33caef093f6c567a8b19e7c9bbe31bf883bee3ca1b(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    enabled: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    name: builtins.str,
    sql: builtins.str,
    sql_version: builtins.str,
    cloudwatch_alarm: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleCloudwatchAlarm, typing.Dict[builtins.str, typing.Any]]]]] = None,
    cloudwatch_logs: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleCloudwatchLogs, typing.Dict[builtins.str, typing.Any]]]]] = None,
    cloudwatch_metric: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleCloudwatchMetric, typing.Dict[builtins.str, typing.Any]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    dynamodb: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleDynamodb, typing.Dict[builtins.str, typing.Any]]]]] = None,
    dynamodbv2: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleDynamodbv2, typing.Dict[builtins.str, typing.Any]]]]] = None,
    elasticsearch: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleElasticsearch, typing.Dict[builtins.str, typing.Any]]]]] = None,
    error_action: typing.Optional[typing.Union[IotTopicRuleErrorAction, typing.Dict[builtins.str, typing.Any]]] = None,
    firehose: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleFirehose, typing.Dict[builtins.str, typing.Any]]]]] = None,
    http: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleHttp, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    iot_analytics: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleIotAnalytics, typing.Dict[builtins.str, typing.Any]]]]] = None,
    iot_events: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleIotEvents, typing.Dict[builtins.str, typing.Any]]]]] = None,
    kafka: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleKafka, typing.Dict[builtins.str, typing.Any]]]]] = None,
    kinesis: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleKinesis, typing.Dict[builtins.str, typing.Any]]]]] = None,
    lambda_: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleLambda, typing.Dict[builtins.str, typing.Any]]]]] = None,
    republish: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleRepublish, typing.Dict[builtins.str, typing.Any]]]]] = None,
    s3: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleS3, typing.Dict[builtins.str, typing.Any]]]]] = None,
    sns: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleSns, typing.Dict[builtins.str, typing.Any]]]]] = None,
    sqs: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleSqs, typing.Dict[builtins.str, typing.Any]]]]] = None,
    step_functions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleStepFunctions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timestream: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleTimestream, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7168d3679fc39a00d05b9c84bf630a35da1206894e472ca8c0514f3989afd06(
    *,
    hash_key_field: builtins.str,
    hash_key_value: builtins.str,
    role_arn: builtins.str,
    table_name: builtins.str,
    hash_key_type: typing.Optional[builtins.str] = None,
    operation: typing.Optional[builtins.str] = None,
    payload_field: typing.Optional[builtins.str] = None,
    range_key_field: typing.Optional[builtins.str] = None,
    range_key_type: typing.Optional[builtins.str] = None,
    range_key_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2134c403e97e260a14f2c7bf393588becfc649418c1d54520dd8808960ca0e9b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__403b7e127ecf245edb710ae3b76c79c8c7e98b40d0e238a2c7aa9e804a0f9e93(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b006433caa3f6896f1b81b248c58281d2f5d012b7ead671a94bf8228bfe177f3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d7917cf90a20a2a0291ec8c9360db8b5bb9ba9b3a4a0a9b857e5eea8e54ce7c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d52832234efabdde1aed0f22777ee019f585f0a02de1887f7d914d3ec72cc41(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e9524eb32e582ce99b890041e7d9970d40f0f31d11619f7498ca61def010d86(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleDynamodb]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bf15a74fdfdd0c0e9480d715fb2918ee88e135393ca473bc8b2b32b32c91267(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19af3e81e0d2ff304b1be9d72559cff3ecd2350a36fa9c30be34c5396b2d0573(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3790184367f5b747e25d4d28974c61070a89827931128f64cf6d4285e373ed32(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e19087e0282dd8d7ad40e755dd87b94471576ede770846dffdbde480e90dea2b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f6ad81e6704a85d554c62e6a49952b7c920832f8099f9af6e68368f1975bd37(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1f99a9d65cf0c80ed36f1cd6d5b69970cd86d3b95cae9c24dca75f2d55731f4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56dd2b6e9e60e6987c596b81d994c5da595803898ba7783cc0ea5ca0ec3abda9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7605f00e39ba137f9df772dac57545a791f3ec9b807925cfeff4a51469ef71e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4983ad451b955928ccf6bd4d0726fcade83e284d833fa3f0b7bf7f61fddd2000(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14b9d86bfa1a934051396e423dd763dbeca7c327c2b30f5648a01c286be77119(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8134ab94f715a3a6eeac04dba2c632d3695f93cdf144879f397639aa24c2e5e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27ff570101a9d4cbd8223f59b87606e8ffbc29faa996b4d46c16101412de569a(
    value: typing.Optional[typing.Union[IotTopicRuleDynamodb, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__461e0f79f63936d7557e6f647a002b1fa65e7cf4bf0c73d7807bfce3cdf9b6d3(
    *,
    role_arn: builtins.str,
    put_item: typing.Optional[typing.Union[IotTopicRuleDynamodbv2PutItem, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37cd868a16008764a802191ff88965dc05770c131257c746e239b2d7c95863ee(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4640c34ec3cf29c7173c791e0aa614102e6c2a7c087b27177ea93e5ca6beb131(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ffd2db82491f4d3b10a5396d666e9b0b721ccd8543058386f006102882998b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef1209fbd779a24ef2b17d3b9cd8b4df69bbb972267c9673b2f911677f0126a0(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5815cba23c65b62f3e87b7cb909dcd687ea3638143424467f885d490b5c88ca7(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c272c76ef80f9e716b261ca8e7972cff8d1159208238cc182b665a05c9c0fb88(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleDynamodbv2]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4302f82f4c192b8763ceed4d9c6c7be88eb235dac6a8d86c4c6f9dfadbd22c39(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__537faa0ca32d8a2044a8c3eddd9bf7199e80812ed299b6e677c452d57683573f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41d816fc8c85f675c3027619f72b1a2b08d8e885848e4a4066811a8b6236e4b2(
    value: typing.Optional[typing.Union[IotTopicRuleDynamodbv2, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecfe3f60378be9e4c952a6d8e753c3c6a9ff73737d93f9b1566dbe3f9cb9e52e(
    *,
    table_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abef44bd47ae26ba5dfee9ce94408ba25465c037f459662c2af52553b2afe180(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a579d15d9ddb5df870fdfbf56c2490a11967f5845c831c80793ac3551832c2cd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d9b22ae856685676de0738bdfa04e7767e3556d4ad607ba021ebf93d13c5126(
    value: typing.Optional[IotTopicRuleDynamodbv2PutItem],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__640d10f72f2c09f86f2b845a53d980dd19a83a99d3ab81f5a03638ed3e384cb7(
    *,
    endpoint: builtins.str,
    id: builtins.str,
    index: builtins.str,
    role_arn: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13cf2500de0c8745a8c40ef2231b9db85c7c4468de88fa5c9f226974be427983(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c4d3a888bec13007eaa5673f5368421cb8e8a7bb0e471569f8be9e4f369ef56(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6779b4aafbb26c29339254c0c21f11a160ae302328cd467e63bef2951926dd8c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a650e86d70051bdd8ae92d453c303063c132ded47384c5f0d06c3ee714e4dfe(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__340fdab86a4054fbe2427a990b3a9dd8f2f68e9e474ce587ccb6e0073f59419e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d185d41cdd4e23f500ff700aafdcfc5ecb010b2a7e1b5cecf099c1acbb8a79ac(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleElasticsearch]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53f1d8ed764152e3b275887b8982054ee3de80fc7b8c7eba6e1157d2aecd5bad(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ff4d031519a8e78475d8a5b926b75859d5b02f511c0ac1c940bff85fbf820d9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93297e1922cf222d064dbd7fbd308a22f5c6715bb3de108276f8b14d04c5a770(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__698dfc00ae40e9313c9bc1de4fa2b12cd75859ef6dd49cb87079f6e9a494155e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17707daa507b75ec0ddfa76f41e35d40ab007da9ba584a6c73fb873952a98f30(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19156c7e511163771b3f35456612b5931c62689c761a00cd8cab6c835d8197f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94c26aa947bc35d7d0ab831ebd6b500adf64965f228989922121db70a4a1663d(
    value: typing.Optional[typing.Union[IotTopicRuleElasticsearch, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbb1fc763952e8f09002429d5a70475405df6e17540aaf78868f4ee5283f9cc9(
    *,
    cloudwatch_alarm: typing.Optional[typing.Union[IotTopicRuleErrorActionCloudwatchAlarm, typing.Dict[builtins.str, typing.Any]]] = None,
    cloudwatch_logs: typing.Optional[typing.Union[IotTopicRuleErrorActionCloudwatchLogs, typing.Dict[builtins.str, typing.Any]]] = None,
    cloudwatch_metric: typing.Optional[typing.Union[IotTopicRuleErrorActionCloudwatchMetric, typing.Dict[builtins.str, typing.Any]]] = None,
    dynamodb: typing.Optional[typing.Union[IotTopicRuleErrorActionDynamodb, typing.Dict[builtins.str, typing.Any]]] = None,
    dynamodbv2: typing.Optional[typing.Union[IotTopicRuleErrorActionDynamodbv2, typing.Dict[builtins.str, typing.Any]]] = None,
    elasticsearch: typing.Optional[typing.Union[IotTopicRuleErrorActionElasticsearch, typing.Dict[builtins.str, typing.Any]]] = None,
    firehose: typing.Optional[typing.Union[IotTopicRuleErrorActionFirehose, typing.Dict[builtins.str, typing.Any]]] = None,
    http: typing.Optional[typing.Union[IotTopicRuleErrorActionHttp, typing.Dict[builtins.str, typing.Any]]] = None,
    iot_analytics: typing.Optional[typing.Union[IotTopicRuleErrorActionIotAnalytics, typing.Dict[builtins.str, typing.Any]]] = None,
    iot_events: typing.Optional[typing.Union[IotTopicRuleErrorActionIotEvents, typing.Dict[builtins.str, typing.Any]]] = None,
    kafka: typing.Optional[typing.Union[IotTopicRuleErrorActionKafka, typing.Dict[builtins.str, typing.Any]]] = None,
    kinesis: typing.Optional[typing.Union[IotTopicRuleErrorActionKinesis, typing.Dict[builtins.str, typing.Any]]] = None,
    lambda_: typing.Optional[typing.Union[IotTopicRuleErrorActionLambda, typing.Dict[builtins.str, typing.Any]]] = None,
    republish: typing.Optional[typing.Union[IotTopicRuleErrorActionRepublish, typing.Dict[builtins.str, typing.Any]]] = None,
    s3: typing.Optional[typing.Union[IotTopicRuleErrorActionS3, typing.Dict[builtins.str, typing.Any]]] = None,
    sns: typing.Optional[typing.Union[IotTopicRuleErrorActionSns, typing.Dict[builtins.str, typing.Any]]] = None,
    sqs: typing.Optional[typing.Union[IotTopicRuleErrorActionSqs, typing.Dict[builtins.str, typing.Any]]] = None,
    step_functions: typing.Optional[typing.Union[IotTopicRuleErrorActionStepFunctions, typing.Dict[builtins.str, typing.Any]]] = None,
    timestream: typing.Optional[typing.Union[IotTopicRuleErrorActionTimestream, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__beaef60545e1dad110a4d067bb99859a0d2a1a7e123e5ed3dfe19160e2d8d2fd(
    *,
    alarm_name: builtins.str,
    role_arn: builtins.str,
    state_reason: builtins.str,
    state_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fd66bb8d7b9c8f151bd85aa690acd8b4bf414b6ed8e7ece74fb389d33256cca(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d018275d861c2c710f56236d960abfe0a64b1400d13aa929133d3d76c134d7f6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3267d6d5e1b1152a9c3ff61179a45fce697c09da9d361f670332ac390f6ff6c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82daa9591f1dfabcf5b39b0b6ae5c14f1140a2f4c5e94cee878980427bd5a247(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__853dcdc1d51e0dc6e8d39adece2f2cc1c7a3440e88ea1583b546d4f65ffe679c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e5c40b7c2b93c6b667b928a681982dd221559bdd23f450882ab4ea4a0ce8988(
    value: typing.Optional[IotTopicRuleErrorActionCloudwatchAlarm],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__decb5c3b9d1d9208896355b6529badb531e10c7e9fba722b9e849aecbb99309d(
    *,
    log_group_name: builtins.str,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e0cb4abcf779690d49f4dba0fd65df5506a5726dd3886a54f769b026108e67c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2012b43a5eb9cd2f38b6f59426c405f69409497ac8b340f65bd3c7285c9ebe27(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f830703abbb73e64dc7cd322c46d1dd82daa3d71182eb4b91aae02f1bf57c632(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__411215fde1fa0ea702d43a9d4a2447e75e2f360f2f035dd005178451334d2dec(
    value: typing.Optional[IotTopicRuleErrorActionCloudwatchLogs],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d5c31cf675bf38e4ac7587a63c8f879d2ca23067a7a57d203df807fd3061427(
    *,
    metric_name: builtins.str,
    metric_namespace: builtins.str,
    metric_unit: builtins.str,
    metric_value: builtins.str,
    role_arn: builtins.str,
    metric_timestamp: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__434afc9bef988e206ca27536a5394d44fbb2a8a312547a515dc81013c90347a4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfb11322fc80a7bafce5c0f96573cf007e4642cf429e09a467c8de8e0496c041(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3b26548d5ac016b09d29b5797a76c5dd1404b808d24b035d04e39e574f6d87b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e935b6f95fc7fd10eed28230c0b0fbdf825ee0dc3c6d56795dd816cba9bd500b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8c19469e9578fa9065314a9ebbbac67cb73785c29a8536ac5b7a8de101cda55(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f804c14da875ce3c01854e902c0fe48fd13733890ea1378546de2858728f64cc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b6ea170b846f51c19d90a177ebaddf576b86e6c97913ca31804a534ed90a02c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a85d26bd89eda250ade4b37aeb9e95d6c5ceb2d64c393f2b5130631e8eea8ff(
    value: typing.Optional[IotTopicRuleErrorActionCloudwatchMetric],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__539f1971d506f9d3f01a7b0c52f40a8507b1a74788b619ae7676ee7479f533f5(
    *,
    hash_key_field: builtins.str,
    hash_key_value: builtins.str,
    role_arn: builtins.str,
    table_name: builtins.str,
    hash_key_type: typing.Optional[builtins.str] = None,
    operation: typing.Optional[builtins.str] = None,
    payload_field: typing.Optional[builtins.str] = None,
    range_key_field: typing.Optional[builtins.str] = None,
    range_key_type: typing.Optional[builtins.str] = None,
    range_key_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__450bbd6747603d1bc1e81ed44ec520abba9d7b5b4c8bb72290c141866c392f99(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26f8ec544c22ed46fee6f346fec3e14f27b4de3431f1009f8db0a6be1cd1ee05(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f21e7e81d5b08784ca8788f93c9b87409302e57546491a910339fc196fb7d275(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30b44d540bf612a74d3a7870e66afc64227c66ad1a9909f050919b0d5100b5ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea1d5f5e565fad3aa00fc4339b3e9cf73298c23acf7d55a5e44f836aa05cb8d5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69429016279fc456ce8ace5cce6e66da806e42a0b4c1eea0005a93e5f03dcd2d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8711550187faf0fba669635088c7bc3404400ba1121e03a511f33739400e73a1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__febe0debd18a15825198940032ea9511cf029882e7df6fdfd6b265e85c8e28cf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35443ecc22923638106e5f7f8ae6baaefcc3c5895a4f3d61904a737049a6ba9b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e63e164edf83390c0fdf3797786cfc66f2e958bcff8b670343eeb7ec6b59a1d0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7b59fd9f3113dae2c3829cd4cfa83dc7d72324b00fd928f405287f3d04368c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1092f1e060603fe07b7b1b5c290d9adc9b460bcd88b965b24a095e2b89b81fe(
    value: typing.Optional[IotTopicRuleErrorActionDynamodb],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d446592e9ad12e759da66f7d7bdd67e25f9587404923882979002dd33a75212(
    *,
    role_arn: builtins.str,
    put_item: typing.Optional[typing.Union[IotTopicRuleErrorActionDynamodbv2PutItem, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae8d7acf305135c289fbf627cb0b4b142b67543ab106c124bd02d136e9a4a7a2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc9e3df6a56b9988214216cbd3f2d890cc5842b2b5abcabe864eb7e5194c7a48(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__276c1f3a36071174ea4b88b9a332158b3b8de18d534851103d26b6a16f2c6444(
    value: typing.Optional[IotTopicRuleErrorActionDynamodbv2],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8da4e021796968d9480c39d3d2f177a382ea067f41267e8d758f96e1d04c227f(
    *,
    table_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7816f6ef37dce828746524b9178b5aa3938968383348edfa511f586be11aaea8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46f3e9c2f14c51a34a8fa327d1d6bcb777b7d845cd905566812861930765068b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3073e7bc5df6b92f18626afc871bd5e009b89f3395cd966c54b0de94ac4aacf9(
    value: typing.Optional[IotTopicRuleErrorActionDynamodbv2PutItem],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cec014cfa444cc15feab584725dc97be9a75820cf4091650601a636691dd13ef(
    *,
    endpoint: builtins.str,
    id: builtins.str,
    index: builtins.str,
    role_arn: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a2462de5f93e40a5f2140701556a8db1cd4a9a3a64c222ddfff85991c6188c2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3741e7ede219baeefd966ffcd4062d5e76349013638cfd38d7f273cd44d32f9f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0b4175310796c6d67fcb1f1982d4fc36820dd69709e538f7c1872f33e11b170(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c9d179c5cabbf328d4ee927562d849908c9fae52f05c01c8fae9312f84bdb6e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd3d64fef1be2bc1a29781f71d0327d5d9a43655b418120da7591276f45d394a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b8ab95c63d5e238e893746f4cd6826ae3e0107a9ee126bcffca3d4e72e3f803(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__705ad4b8b9e066b974f4f6a290b12acc09bbb9e44f96a81982f9918a85939bf4(
    value: typing.Optional[IotTopicRuleErrorActionElasticsearch],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e18dcf780e6c6c78fd7349b3901c8721013a405b0aa02ecb82120c0011b56ce(
    *,
    delivery_stream_name: builtins.str,
    role_arn: builtins.str,
    separator: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__299c8730f5cc5cdc2374aab96a6c20da6d3d05c0683265c87b05bcbc82e464b2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__145467e9e47dd9591e5b1e33fd0405b14c584fcb2c37b1ccd58675c66e06c7b9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b1a03b518cc4a6e7422a43ed9c7f225bb70eeaac23ca5e0a6b0061496e0a98b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d47796e6bdf07388c04f994f9dc6879585e6a1ca16e39bb1f7095fdd9227545(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b34221ccf381a62d5ee09dca34b88027f9a55f83450b6726c5dab54efbb43b24(
    value: typing.Optional[IotTopicRuleErrorActionFirehose],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40ac6191e1a3aa9ee1524f6a3c2c1f9687a45536586b0dd1d11e94d72d9d83b1(
    *,
    url: builtins.str,
    confirmation_url: typing.Optional[builtins.str] = None,
    http_header: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleErrorActionHttpHttpHeader, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__958d61f3c4368d7991b6adfa1ce4f83eae2680a0e1a1d1429b86497e99255225(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cacc0be7c2f7d593ca658d31386c57fcf635430904244333c6e5e16113bf2fa3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b98cf3869470ccdb759e8be87dba516dfc42d7cdb1b2eadb86891e058d627c09(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ada93e9dec8d026386f32e8be5d9285544011644c43d6ab3c00ff252f57cde4a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02ac628b9e0983ffa37f3ddc10f3f51e84a40963e44096215b973d3dbc5851c8(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13834c981b8703c6ecd3442517a58cefe5974297a528e1c1eb800ecc874fd270(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1388b6d46624477659dd049bc97d7521d865058c8f80fab9c06f2dc65d1681dc(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleErrorActionHttpHttpHeader]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42a6f78cfe139865cddb4014d0a78a738e1a2b9fd0e0c09e6d4ef7fa0e9194d4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8c2b6ea9634aebfe0d91a60bc4382560c297ba64517ca9914bfdb5fa84c238f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__447af9e7c9cc9ba1a04aaa2e06b3b104c6b3da153849ba76ddab49766f7edb7b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__771a19257bd1de991f4a182a8cdcbb1d250def0799117889af403f0a39510f70(
    value: typing.Optional[typing.Union[IotTopicRuleErrorActionHttpHttpHeader, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3156360fea721063d33e3fee53aec2f8ab024700641830e42d402d55e2ec10d0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c4382343697a2d14413d8f205caf0a4f89e9948286e5b2643653300c58a4d4a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleErrorActionHttpHttpHeader, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2efd2550098ba7e44cc65f1ac0d90977b80a58e2caac09ea2ce3d7c97068a4c6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__499235f2fa135b91e8b65632da39365e3488b13cc22d25a3a69c355d3f3245b9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c34126ce450572f23301d40c842eb6958038181c49f1865f725987442320d29(
    value: typing.Optional[IotTopicRuleErrorActionHttp],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1055b7b8ace69e182e679dbec49b62f50b565eff8b7661d14856677802fe6d4c(
    *,
    channel_name: builtins.str,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55d4f3c5922a11426c9318069a506621e3ad3a032ceaa4d1f4f334f6d07862b9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62baff829fcf6a793e09ab9e5d21e70f4fd9989afc2640b73fe72f340a132e75(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__324835f7b735020406fddc08d8e2eb784513b132815f95b00d60989fa954e713(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab0cd7e555d71ff7f33801b6a249942e5d028a35d22b7afaca6965d8dcfe05c4(
    value: typing.Optional[IotTopicRuleErrorActionIotAnalytics],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d43e0308f540c77658be6fa698efa9cd7ff11ea46b7be333ed404f6b010941c(
    *,
    input_name: builtins.str,
    role_arn: builtins.str,
    message_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5fb8f5582ee43868143d2eed06d53ea4def6af726480b3c51fcebee9b50bf29(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1b1af86a01d560de9019f824cec5ec29089a4afa37a60fe4c71010255f148fc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07b74e4e0cea6b2166a173c87968c5bfcd7acfa8996ad61bdedb702d42ffcfe0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9c6b42822a95bfd8caf5ee7a03825ed60d16403d3aeef7e86c2503cc3e5028b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f7932417e1253cba3feeb5d51baf7d8cbeef5468c3a80d966636dd2304e7293(
    value: typing.Optional[IotTopicRuleErrorActionIotEvents],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__086d411045ebbcacfed093e916858978a3344a639efcdcb163b39aacd1e746f6(
    *,
    client_properties: typing.Mapping[builtins.str, builtins.str],
    destination_arn: builtins.str,
    topic: builtins.str,
    key: typing.Optional[builtins.str] = None,
    partition: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8eb7c34c45d47801c5b2cc962da5c107225a5150b61df6964492107d490b75ac(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d37b5d2ad1b71680cd36a82693463c096e7fa2974e8b00c8d1f8e50872a799b(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cda76b5a0961094f9c3581fcf8da654a922df75baddc1f1ada25674754f60b7c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af2f55611a23cfcedab4dbfa1db6c19eac4bf05ae8a687fd381dbc708bfd1a5d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b1875269d4c67873f6901b14805df3592a2ad0e4392323b0507175fd3855c45(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__343eea3ee64c86cc88d218d7502b37beb3dc46cea05b599efa589c87066e6c5f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa0ea4b9345acb2531d7474e2ceab4c11a38c753236ad0003548f1ff9baf5ae8(
    value: typing.Optional[IotTopicRuleErrorActionKafka],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53b55d96d8dfe7e8aa052ebbc9cff2754e17533a873b271ed9794fdf325e775e(
    *,
    role_arn: builtins.str,
    stream_name: builtins.str,
    partition_key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4e25f7a0aa1de1bea0a9c757b6ea92d2bfba843854f0b0c3b398fe3688563fa(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c171c1c715a2b9ce7a305fddbc7511312043f85308cd1e0d0ca36b712fe99d2a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29c4d5c1642d7023305a5aab9e29fa7655351991b9c845388784792ad13d4c1a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff9055812b1134cba4448450dbb6a232cdf96b0ad77a2a01ef04b667832ab403(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__599ad6b2b54ad5d2ba49e5577f195db8ead0f8ccb1aafb6908e41aca7d63cc03(
    value: typing.Optional[IotTopicRuleErrorActionKinesis],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cad0c071f8b408b5f49ba8aa17c780e03b0edb1b15ec6009bc851b8e3212022a(
    *,
    function_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03a69401142c922fbcded72aecf31d4321ac48570e8456f2348dee64bde0e4d4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61bea8c18fd4c08345c464e6950dbcbc7ae1c74243ac9cb9fbd36ec7591b69a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__957a60996b94522980716701dd7bd814f8a29bb580c4cbcfe03fc00afdf30880(
    value: typing.Optional[IotTopicRuleErrorActionLambda],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ad95c38db6be11029da404dbcf791839cff348fa731b9b9236b1865c00e42ed(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__900a945567e929aef4c9c73ed59ec80c0185570af2e59e07eb82d19b5fd0103b(
    value: typing.Optional[IotTopicRuleErrorAction],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b60e2c80f842d97d412e1f1594fd7162ef5f9aabab5e7fc2b5959a092cf220e(
    *,
    role_arn: builtins.str,
    topic: builtins.str,
    qos: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96c6635e30452bf3939e64e897501b2b39ac709abcb530d96cb109038577a5ca(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fd93ae3ce2697ecd1a5383a62ed169cb79bc30dd47d16557d555b3f621629cf(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fe42ea2615166655020b78694fe20b39ef4eeefb4db08b68189476e2ee3b008(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63fde58d1fe97df4d26fd6831e04c1b6f0c163492c72dc9a939a7816b8929460(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2709a4a693393af96d5b2fd7b5d1b6a86b04f6ca7313ae5ddc0dfd99bb7ad03(
    value: typing.Optional[IotTopicRuleErrorActionRepublish],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e99381188c1b516c2d5cbb32505239b71a7deb0cfd92e6a1e0d9c581b73be248(
    *,
    bucket_name: builtins.str,
    key: builtins.str,
    role_arn: builtins.str,
    canned_acl: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e94be316173b1e5b2d9f100529541abaa109359445638f9d4fd59c62aec6ae9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b9d7d691a6fe6564a842c54811445df1b85f916b3faa9f3685e6bcf98215d7e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcbc7eafa1a8a312a350b9bee04452a3e51535de1dd3ac49e0a527bf87298a8a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edb48c43b462dcbf50418d5efc3816b858d8125f9ca9aeaec5c0af36a3ef6e7c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce387b41937ea9915e50a23c94671e6fa6ffbe5112fdc9eeeb6ec328596455a3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c58aa329291360e296fe209b0c38222e82cc078d4ee06af92889d626243fa0fa(
    value: typing.Optional[IotTopicRuleErrorActionS3],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee29886651af521f5729ff0982164b3ccd04e22af12578f5d91bc8bb3c6cfe8d(
    *,
    role_arn: builtins.str,
    target_arn: builtins.str,
    message_format: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f36429db66cf8358e8c7a2659b4c3715fb8915ff6c588b4cd8ee830c432ab1af(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be968355196106c080e61052fc6fe5aecbc044e827b4302f4cf080c1bd288c58(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d412b3aae39b1bedbb3eeed6c72fa7723c0bc7ff3f4c3a9d28dae4c7240d862(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb595101b1d9537286c2b14bc398fdc69d756eb3ec1cb4c0de036def5f1a9c18(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3e3bb71425f9e362b3b40a900f51b76f6731776c7de13c63e3a12374144fdc8(
    value: typing.Optional[IotTopicRuleErrorActionSns],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c92cbcc001eb12caae16f1f318bf07b723adf9eeee01b933c1df2d13aecf0b5(
    *,
    queue_url: builtins.str,
    role_arn: builtins.str,
    use_base64: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aae7c7695de867bdbf21ba0edbb869dfb6e3ba46c2a8a5a2907f03ca60343bac(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26f9ed6957ca88ef844b08675ab5a52ac3ab5d06154eceb4616ca53757110b38(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__424b5175fb0a42bc9e0770420bd17682b79469da0ced6beaf359a2bfbec047a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28507ebb0a4876dc62a95a1c988d5870249f04d6bc249aa0bf321fe8e9a7bcbe(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a7129afa33d1f280b26b540c11bcfcc390420b74192409dfaec70fcad43febc(
    value: typing.Optional[IotTopicRuleErrorActionSqs],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__943a6b0468bcb59a87e20968d36025655d60bb3c8255fb378cc6470ed59c4d8a(
    *,
    role_arn: builtins.str,
    state_machine_name: builtins.str,
    execution_name_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9f42ef76916a69015a1399f2ec228ccb09e2d52441e70a99d272b75566f1cee(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23a4c65c2900adaf27bd9e3d211c0591047b1218851413ca48419705ee840bcd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c799bcfa0332398fe74da9c6021c8ad6e5a6ce40f7205597939b730750bb8263(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fedee5cb1e0e59ad3ca60ce89cc4fbf2681ee03be47779cf539e7c3c90b69a6d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98ec2b3e67947d1b0a5f321c45c1e09e5482f15b80f64fb1862932c58d19f4bb(
    value: typing.Optional[IotTopicRuleErrorActionStepFunctions],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4feb8aba8eb3e89f14c828ddba6dbda67d6a993b7822fce0d8597e6f42c882d9(
    *,
    database_name: builtins.str,
    dimension: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleErrorActionTimestreamDimension, typing.Dict[builtins.str, typing.Any]]]],
    role_arn: builtins.str,
    table_name: builtins.str,
    timestamp: typing.Optional[typing.Union[IotTopicRuleErrorActionTimestreamTimestamp, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f14e387d641be2147a471408e4239bc13535c40ec30e7fd597635beec999162(
    *,
    name: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3834704304d6d7feb189721ca318b82c4ff2acf70813620ff58b8a3d32f7514(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cbc7b24c0a7ade9124b9a2791ab96a6b9ad61afdc69e04884473474d78e81e0(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd03f3e366531e0430156d08a9bc860a4dcf2d75684e8e672ca6bb84928f487c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aea68f94695aef43f7241009ac6c97e30a78b01f50facd33fedb8f278c5d759f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad3ad243b1fdcf9c925ba48b9d5cdc04f105edc87298a92b54e2c29da1b1ba52(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f58ea3e3b7a1317233f28addc5da54d28f37946377da1728fa5c06f258027852(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleErrorActionTimestreamDimension]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85a6f2a705bce6fa5961dc2bde3903665aad30c729f04e9a20af000cafa4010c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0a8218c651b40827af79ad3c0a27e8ac3e77a3ab56432299f8dd56aa62f4407(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee34c83334934587acdd69d2235937dab9e7ff36b7db5212281885448c4e218b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__878a72c682d2912c60cc0d16fb53827231ababf83e68da600dd23a92b1c06137(
    value: typing.Optional[typing.Union[IotTopicRuleErrorActionTimestreamDimension, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5be186210b4f34d58359c93f562539f7924284d7a126135d2c48cd0161b59b43(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc849e456d118c69e35ba635e52d99f3864eb0e6d0350fdb4b2d5488d73a1efe(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleErrorActionTimestreamDimension, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df9208b26b561df9c92746bae8dd3a40093650f12120760760a70bdd25973283(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c8b6804384ad88a44cf7528f49dffaaaa5b3c3a6af2bfec34d999aec9e2b9aa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b82db016148a0f42593f46a59dbcc9d4e9c10517382b65a52dce04f47c11cb86(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81862fc920ff1bec852d004bf1894f10f522eafe385453ba540f12dbcc8b28df(
    value: typing.Optional[IotTopicRuleErrorActionTimestream],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78c0e38ed52822b01e79bc090a0b9dd925adda1835addabd11e69eaf28e0209d(
    *,
    unit: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a785271e4cce29b6eb87fd3b397c2eb920a97f950cf49ff522b53dafb86e587(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3c8e573f676d006c5cd0d667e2c00dfda62cd50d73c43d8154c729042dbda15(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14cd7b0b8a7c041e274ea012c2ddd72ae69df13ad227e137b708d457db9d04d4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fb1854fb39ba2219ff758b5896987dd32491e4bff1029458ddb13d56632656d(
    value: typing.Optional[IotTopicRuleErrorActionTimestreamTimestamp],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__168a06017aec2c64bfa5da8e95abd558a6f8089724db1c68564f85a4e6a582f4(
    *,
    delivery_stream_name: builtins.str,
    role_arn: builtins.str,
    separator: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aef0742e3fb80fb9e478c00cb7913db362a64e565f1115e0c328a2782089d582(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__981692c791b0e619de5fbfd11e96eb302e853ddc10354050d0c23d8f63af9c69(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cc95abed0101a044de0efe89a9ba5c07b6c689ee91aba60b778ab5552a46e1b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7e4e8772e819d7f1fca7a0fdc2037c9b02c5d7ae508b06c017357bf8ce356f6(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c02ae0d5d0ddc38cf32f014559567e55f3705ff9b96385d872bfe7f8efff563(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b06089c530eaa722a592d243f48519736d342f5d9b0be759abe8945630520b8(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleFirehose]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__003f69c8ab81ff2e48a9ffa942df68bca2cbafda5aeb1efc5c0883e30448dcbd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2609b1b03ba4dbfc567b6cacd5c3994323e1bbe52130327b61711425ca5344f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfff0358f17c6be7a0fdceb88effcc7fcb80e6300fec37a59906481cd9d7f34f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b71fdcdf0e6b86ff10ec343cd9ff2cfa688bb9e2240fff6c3825221b335da17(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff68c33aa017d680b3078af67f4a8f6ae57488c7c0d8a4a29b1f3572a1eff608(
    value: typing.Optional[typing.Union[IotTopicRuleFirehose, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f2cb3f8a9e20713a36e7f9126cdb549e3cc36cc931b5e1918a2cb57ed14e936(
    *,
    url: builtins.str,
    confirmation_url: typing.Optional[builtins.str] = None,
    http_header: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleHttpHttpHeader, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16e805c0629b698dd3f4b4e933ee0a6b15a9850d2e064f2c6e647cce839ce562(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f986be598d4ec06d08c29952fff20c0b06477fb4c6e543b408542712c2ca2756(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4aad8cc9853492fb70ee652291e4d86528de1b5cbc6c65333913edea6401343f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f4136b9f770c54a1cb71d261f2c8bd136067403a78271f572123960c334328a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5a8d052cf5df4a7c24e4d1584e2567fa75347d300b3a28f737d239056e532bd(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f0ca92bbcb2772661644e97b706ef10a56b6392867b1ddb0c7365d77da39887(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7a52cfc8cc8d771e740bbc786a88805a775cbc76480f4aa823a60f6ce55f458(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleHttpHttpHeader]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3334f360abd3d74a73d324ae0bfda3782caa8bced8bb385eb15d5a1c298782bc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__306b971728155806a599bb19feedf86c015660faa016045b9cd5a9366690d9d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29f9823c55c86a14a345d7ce94931c1cf5afd40c606c69f6a00c087938fde331(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__022f2b9c831b30823570735680b6adacacfb4f7f2b6e8f5713ff2fa33346402a(
    value: typing.Optional[typing.Union[IotTopicRuleHttpHttpHeader, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91157a56f9775b87e4db39f1ff35d52351682ab8d711273141ae2779456ff82a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00718ec468b7b88740bbc75aa619954d3a9c0d3a5e1d4752c32ef2bc24f51a8e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d3aec4f4bf40e75b9b99b6bf295cfaa494e47796c322ccdc854976bb1d1fb58(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c53dc303a6e93a99b5967214a79054e71b70ef1f9e2b57d69eaafc320e655e9(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ceff604ad0715da9c81e6bf503ed59551c51e1e6f188a8ae0bc37f0b89b2852(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b133478023a384c2ce65728f139892bf9cc2bb627795517a1f4808c88043a0be(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleHttp]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0183c32ea196b01140956ddf7b6edaa48e5b37bbc6def79148ac85d2b18b788(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__773a08b337b5933de7b0ffe00d87e6a4580d36707abdc01829f6e14486904d21(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleHttpHttpHeader, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5076580fe977b893f2f81f1415a9d5eecdb7d23407a074a09b2dd91689c13ed(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b6623866636d8adb9155afffa30907d83ec9d06801680b5899d390c1af280f3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6671b54164224b2b4a27d837b820b8c87685f98517655a7331a5f70775b8460(
    value: typing.Optional[typing.Union[IotTopicRuleHttp, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a18aada55e26b453433553747e391919fc19f6156cb247e4f4a56593f44622b(
    *,
    channel_name: builtins.str,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3252167bbeda1bc59c933801d6e466a523b08bcb6abd04f968d0015ed11b66f0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1009ef484547b63ce1a07f923c1beacb9b5d9c005c8f3882d5b511ffa5ee0ab5(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1a6e8a6d36c90d527d5a00c49ecc52b0e9857c5537731dad13eb1fbd863eb71(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec66b6dcbb9a65e746724fc83723935663587885045ad664ed40df5c10a65877(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fad7eff0f94e8aa53e132436b5a22a521a08d75fb864a195ebc2a7aee0f560c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfb55304fc0beadecc9cd5e6ae05a65d27b48faa51d5e101ab0e24766465dc23(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleIotAnalytics]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f43a188ae411250bb2b2b4c83d895254341fd075f07968f4297385b82b2c99b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__590f30285a25fdbfd548d2a8ad3c709519e482b7ba2d468d44c691865bd413fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1429a66545bc63d4796e930625a242d7e21316ee5aa8a799bf90272715700aec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b7892c124d102efd801e00e1127dcb70163b86c0a23715e211ffb80056da2ea(
    value: typing.Optional[typing.Union[IotTopicRuleIotAnalytics, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__254a501600da0602ae86ef1710fd77ac450a441adba1b5b179b79e0cc39af057(
    *,
    input_name: builtins.str,
    role_arn: builtins.str,
    message_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74c1503dddcccfc09e1a0cc23596bd564c4023f1b156a771b363272073cb96e8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dbbf90277025bde5f6a631b4d1165585ddfb23983158b8b555c9bb32744b45a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd1d3783b1790099b84d4d70e3d61a613d492d88770b5a04d922836935010e61(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db8c1d2ca1329205556ac8e7026416387bf462ec8ee58238a0a5d65b8da88dd1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a5c2b122d5fea45d4c753f0d61546b8b92683789b52906e60b97fa140c4ccf2(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c627d64b825fcdbc46f7d48e264818d0453f68cdad4795f8a18eec68125e662a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleIotEvents]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f74ad1586a805e4149f8ee93b19f721a92552408666ee8a0d5aff1b7c35f0e02(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b3c839f54511d900f73fd14634c1d40288ac3e74c8a0dbe7c2b327ffcd20765(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60ebf9a0bc7cae4afb9a2efdb5825951c58771635b51a4cabf003697e2a58cc2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f566bbe4cc76d2e80593e89b47f10808f80e78ab5d643c8e9e8f68237acea4c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d6c00752d022361480503e2acb25080382a0e4948d8db87e7e10a48aa1fc3ba(
    value: typing.Optional[typing.Union[IotTopicRuleIotEvents, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__939c6e09606c5c58470821a081e35b12bee5344a7cece6ac35a77fd641202a60(
    *,
    client_properties: typing.Mapping[builtins.str, builtins.str],
    destination_arn: builtins.str,
    topic: builtins.str,
    key: typing.Optional[builtins.str] = None,
    partition: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2402914a4b76e05b6130e244852160a269766dd2f8b072b3592a24d4a035f41(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2104f72770ecd07ba8c9df2d7183f68973e0abcebbf94611263de28606452a98(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__504de0ea5295410886ed758616ff21452ae05d42924c7f7e7af17bf72fb864b1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__233510ec858d69aaa012690ee0a6cd46dbee40dcf441550afde21d6059c37ce0(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c7a619f2cdb7610aee97dd8b2b578f129e42383ccf4894b21fd773c769166c4(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfd7a651a950fd6a572208604aaa1806caa6b85073387b5f6e02a1cf76a422d4(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleKafka]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a444ee39d982dca50ae5c9cba71cae318a90ff5cc1816786d5305d448a1eb734(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__663bc1afe593220fd3cc00b92fddfd6e5bd03d06a6d4a5d2a6b9e7cf6325e43d(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f2629f0c694aa07473b397ae5f45d6289ec008a06a5c7a5874b9d2e7a25a9d5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__726ff73d4d9457d0a4bd97950d08a19f108457c3d0a3c40e3ed4a1144d96d2ec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ae901b84ccf9abf85ed291958552871494e997bd96c6326d4c47ad7b21537e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05018ffd806f4191b38004ad6c70b0ad2e3e20bdbefea80543fe52bb60c22db2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3b540f569d773aec747eab3c6fcc9555cecd971f68fa8972b5184d0440ac99a(
    value: typing.Optional[typing.Union[IotTopicRuleKafka, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56a0f3ad7249d120423576c4cb1948c052d2d306eed4b7954431c03218724022(
    *,
    role_arn: builtins.str,
    stream_name: builtins.str,
    partition_key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0511cb085b1d6745bd3ccfe9c8c8b99a7b94dc6371d046f9c959d07a2e2871c2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0831c395bbf4d72fdb3290aa0d7abba7d059163c618666af1815bcb8b297175(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43bb2968c0120986f35a82ebd89d0ae7092b504aa7aadc9c846efe22d0981fa7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d52b056bde63459e36cc659bd87424460e802ec345264f6858426d3aba3a72d8(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d462b75c1e8956ebf24c0fe85a67c9ecd6db1d34edfaa7298c91e637bd6062b3(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__767f1bca7782ab147ab648ae74954eadc47daf9826e1ab00860bc2208851e55e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleKinesis]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6005258836eeb18e4f6c2856d95def58c27d3fa13699b56ebebbe74f7ab8d0f6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff2287f62a17604c619b48e749f7c5ed47cf6310af655bfafb7982ebf9f14774(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d47624c6a9f7303d790fd43d6cc5e259e7dd55f1a90ac16e84046142a370404(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6805c52eec1863b54c37df3f5be78f33f0e06aef1a6126fad89f759c4d8565d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec6fd1257a6081e7f349546a4a4929448b9971acf72df661fde5e3880cc1ffb5(
    value: typing.Optional[typing.Union[IotTopicRuleKinesis, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__444a8148b0ea55648c1c84808a30d0ca8996f1ee4597b6ed2092b6b8e770dc1b(
    *,
    function_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3be24dcbc115724d0720e2703bd674acba5a1d44948015f61510df13cf520a3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10310d5cf8a10a33db541a35085f95dc4b8dac870ca095bd4a07d35a727af245(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c31abe63254aa251534d78d880661b1596c5c1a055aca48589f2b0f79f0d6832(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b152d8394f3183bdbac5291706ba6e7e5a69720251617a638dde9fc2b07f8ae1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71f94270a0a45403fe21afbe9b0f21ae501e8094cf2f1793deb9d36e2125a7a6(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14abbac33de293233a32e066fb4f9dad6a7fee477192aa8fc0f7341fb6b281f6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleLambda]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9779f500ef7f0e11e38f698514f213cae9af4599c2004a77ca01ce3292982e5b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__877efabb5a8a1c665d7e60941b8bd01e4183289315d6108fcd985ebaad790066(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a60336d3a21318b1046c5e6fbc1e97756ad45fd19fbe432407813ee025c03952(
    value: typing.Optional[typing.Union[IotTopicRuleLambda, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__693ac0773280dac8fe83cd4ddff30bbfe97e59843b7eca35ebb9a0d9c969f287(
    *,
    role_arn: builtins.str,
    topic: builtins.str,
    qos: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8fff5d65e0bc2b444842abd59c8ac5ff1afaf297eabbdc7496e1c61b33bde3a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84ce08791585773cff7adb5d4daf98662b6c0acdd3bcf0f8d88868f4fd3dc5be(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcbd270e059741021ed6ada15a9dcef454499418b6eaab396e89a275e1e2e899(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71c6b36260e3a4cc7c43a6d0adf23f28a1c44b3e205ceacf0c3c2f912a2ed35a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d25f4434d0f0fe335e37f227aff3d3b144dac2a67e7e6eb2c98185d6510b82b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b799effe6e36e4495afaf4e33bdd7a40d38432ee7b7ea5831aee8b52ddf273d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleRepublish]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56f8b1aeb1aa50c488d9f8872b982ddf8f87c5686a3017fb45ab9152cc1ca3be(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca62c1c3d64949c671dba098fd28958cc70ff4476e9a38b569211cf0371ab80e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d36567cd676174bb9125e12055f5a60cc7aea60bfcb06e811dab1e34264e7757(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f076f3626f7360e10c49d1aee3c5a78d3f411cd0b5d42da82b332dbf9424b7ea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60d05beb136e60c20acef8a4f90148b5b946cfea56609601838262bc952481a7(
    value: typing.Optional[typing.Union[IotTopicRuleRepublish, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__278b808fdd515eeeb3f9cb3ce28373d3694e0d5e7ae31a82076e0c0802956725(
    *,
    bucket_name: builtins.str,
    key: builtins.str,
    role_arn: builtins.str,
    canned_acl: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1e0e561312b989991f93588b89fb4b3484f59a1ec892be95f3e012677552c20(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__786eb782474196818c6f8dcba547a250c5cf2f160d5739eb33246be4b59c056b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27a554f9ad219c2916f39af234130ffe7015ff1726f42ab1d95173abec7c85a0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b06eff4dde1eb02a328ba50f9a470829dbba74d4e60915058ce359fe124f602(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4331865b736b90597323bf79bdd5b8967072c04bacc4705a261c2d2c748a18e6(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__904c4e4512c09c31f1f8ea1d01289489929ed9cea68a43b9cc5cf192f0f832d4(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleS3]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3faa9991b0824ed40403f317e951ec5a3e75ccd801b9b83224945e6030ebf38b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fab121a779f5c9330a3896ba32b28171e601ff15325c5b268bab70b23ac05605(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82fca1f5f64284e08fbdbbb6e335d1a6d3b6ba541aacadca253c1b156c8be0db(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__147166cdb5205e28e24c2c68babf7a351f55145cfbb3266cdba6be27cb3daf1c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8b743a002bf5ceba18849c8fb5df403d1ac75450157be4065245412e8891c53(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__303723eed455051e32d232f9bab148e7af4135b988b1972c06b729e00f82b70c(
    value: typing.Optional[typing.Union[IotTopicRuleS3, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8f64e9924d03820b84763b08e6f142a2a82fc1af7f4472824d34e9ed8661f26(
    *,
    role_arn: builtins.str,
    target_arn: builtins.str,
    message_format: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8d413a3c82c7717041db5eece87031dbffd8a1ca14440d3695df0ca1ae03f55(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61aa44ecbe7b4064e40670b3ba4220a0b3f3e6f9f59c303c883511bddb67d20e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbc049472fb52c97c480a701dea6349c9e86e1e9c5f84aa04fffec067a9bea21(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46b0e468ebaf942fd29d61d146fbbb700d822cb57de70aa01d317e9480f696e5(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9800dba56b7b82dd3ec673d9665486f8c8474f86a1adfb2fef443f54fe0acd47(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__355fd1f6399e50d0b817aecb37b827b104e8e37aad0262b2acfb27735bb1e754(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleSns]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ce42198c41d752d795ad8736656d300a1bebccd3dbc421340b9515f83fe658e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03721972a9de0f5a617fd97cb4aecc6a99bb6475274898860dad3f2f5b05dfd9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de2493b3e7a8fb4b59841bfc18be827ccd18c8dea4d6585f83bb5eb249ca9464(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e56a861fef6a27a5c1a7e4e169f346f18cc665421e2f4e7e089a67a8cb923f8e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__039aab66ba1eef944d2d84f0d3650e10a98fa3d83e1c685b699f73a3e63098ef(
    value: typing.Optional[typing.Union[IotTopicRuleSns, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5502758d88d4791c409d5b11e70d84c558f393950bc6b0d1b03883423c517494(
    *,
    queue_url: builtins.str,
    role_arn: builtins.str,
    use_base64: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c2a8b18726ca5026fda31bc72080a7a4332eaf7de1cb27906510aeefb849c48(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bac9e142d0bf7566f7a2358e43478261b1fe461d2e0cc87054b49c7c86ea8198(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20a6c80194721f0ef212035f1b72bd098014f44c63e7b98c124f6e16b1c5df45(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81dcbdf8f2124d49ea8e2be5368a7d36ca4fbadc45c1f2117d3337870481bf34(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3f68e37b2585461d9db30e7abab8d003f9e4b53266ea60802dd5f049d9021b4(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a0d1c5b321b30c868cbc3d6c815a25e3aa3a687cca640c2473f9c70f968676e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleSqs]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14e04648e1f40274baea56dabcd582d216a5d0204b1360c4ab4cb86c4c950f0a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__853a402c47af3f6e1612fcc56026dedcb84b13b195862570c1eeb1402c2183ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06b2aece64cd5bf972ef5931909bd33cf655d8bfd4bbec5184a57d0afa3e1f59(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d68939543055d711b157707f18661671d44d7a8bf4eb7b96e39b408832e0b502(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17acc6fe6754c9dc8ab5c8559ad0004a7186761740827c82d96629d1f25637a9(
    value: typing.Optional[typing.Union[IotTopicRuleSqs, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__539cb6f2a0e3f86d8abf5c26161a9bf18a7d72e685672e700b2afc33da32b506(
    *,
    role_arn: builtins.str,
    state_machine_name: builtins.str,
    execution_name_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af55709db4f21d59ce288423741db905cb0317c6cda8d340fb254b58268356fe(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3ef77718c7c0b6f13fa0b4be29ad5d37aed1a0d115b40fc5b3467f096e6f12c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92e0e97be9852ad73089e8f7841b59908cbea4c7e894a56bd525027a8370bca8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cbb7c1e3551185cdb22fc85e9ef7de1c70d6678bf72b34ec4a81460ec756acc(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4904aa8d6028fe4d8f3930a2829769c3e1f2ba37c9eb74ccf8da1518d51d6873(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11fc38ff68d8c9ffd296400caf6d0a0264ac8df1ce7dd648d483c417738a119e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleStepFunctions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b80e9dc0cbaadd9e3fe9ac7acd3732188a8c0cb70130aee63162c08c8c3f4f1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ab6c132edaa774d316e85872a7bd4085510abbdc675290da8f096d4ba1f847b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1caa748e270388908c75ffd7f2f65735bf405de878ee676cae4afdf39c4b4857(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dde41202c8b26e7fed44eccc62aecae43e36fa7bdd023b7d0dfdafe15e959b44(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b25c37b5a1f9bb9d4e219c20d1954725af3117ea3673b290acb39e9fbf21c2ef(
    value: typing.Optional[typing.Union[IotTopicRuleStepFunctions, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5855fba72116793c9a92f2f2fc753000542de19b61554e7eb276b6f858eb6af(
    *,
    database_name: builtins.str,
    dimension: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleTimestreamDimension, typing.Dict[builtins.str, typing.Any]]]],
    role_arn: builtins.str,
    table_name: builtins.str,
    timestamp: typing.Optional[typing.Union[IotTopicRuleTimestreamTimestamp, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea8d8a5a09a82c4cddfacb32208466adb0ea08e8d2de6086e8d9b351ae3dfc22(
    *,
    name: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38e08d36894fce4ce11f94da09ae131cbcd60c7f1f109ebb745681ccac57f0f7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a613d5231032f90608f3be4d82949d6313442973dfa14f0cfa787af53aa99603(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f81ba832dcc2597bf19c861c114609aed9f79f447431d5cf035f67dd0ad9ad15(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c6b4e97071aa48707a96c9ffa2907cb7754ee415eddff526e2181aa0e563a2b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc48e47a1fa152ea698e35e737e01e4252396b41bf8450fbf23433cf76ff681c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54ffa7610424aad1b0217fd63d6071419305578d12bb41f9f1c8366790905c2f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleTimestreamDimension]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1962c9cd131af0cfa59692d641bbbda3da3f17d96ea3d79b5a3d9e8dc40b3639(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e980935adf7078fd524060e7022a70c195ed64cca2c75c9402ca3008eb2bcbd1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7e044036abde0b84c0c63bac503b76054e7f658196be88183142879d05aa4a3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4aa1054b4fa9d18bc8d001406c46570e83282efb6f318303b2928ecbfe6105e(
    value: typing.Optional[typing.Union[IotTopicRuleTimestreamDimension, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9002d3d4290e5390887e784c5c8184eb9cb244d11fc57bda00e09e6ca79d9fa0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c788a3fee20b924e540a3b252c8b0dd0fee6ba99ea95ed0fabc4b34c4f80d3e8(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93ea24a15b6bff23d9e609ec1e816c29f748d125f49cfe295b5bfdbb6ebdb969(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__250efad6b384f061436c45738feb20cc091836a6bf69496ad3c0ace24d5c58c1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdcdba43bd1b7f0ff20367d7f9814bbfc07d61b2c44c9dc93a19274fe2276f97(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c64723e609c7657eb3f5a89d282a9c7f3cbb607a030cc00716b56207665981b5(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[IotTopicRuleTimestream]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed24720c43d6d8137596d34c8fa25263dac594fde8d5ee53ef09813dfac6d9bf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e5705a3136d4544e99444625c8b641114eff7474bfc3f0cbedddf990b5f3fca(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[IotTopicRuleTimestreamDimension, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4230cee6f6398a5cd4b9c1ac7f1f9ce3d111428d9b9ed68628ed57ae0902361f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c01661dc68219e96791b6c4cec7a4c9800193ff3259fd56eac8e9a86fdf41258(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef31da477c459ca3d33b2ce1e5f5655cd308bbb599960ad6b41185fb89764993(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__768f96fcc93916519ce6253492ad7fe05a80e23444cc2c23147f0716cad99ace(
    value: typing.Optional[typing.Union[IotTopicRuleTimestream, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__973897989e7ab48fb5e3316954309aef8c4b5995566dd16e79fcafb311faa3f8(
    *,
    unit: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0edba47494521c805541d50692e73d4cc08d2bad020167bdc988cc06e3910328(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30efa27d4e1e25c8ffc2a0d30c04900220e861fc357f09086ac32cebd0bf93ee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d27f06c3ff5262ba6eeae4aea554799790537509643bdb5eee2e934584f87985(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1637b41ad61a096c99e953e3139a6b9cb2f73b2e4706ffb89bb999e1d2a6a99(
    value: typing.Optional[IotTopicRuleTimestreamTimestamp],
) -> None:
    """Type checking stubs"""
    pass
